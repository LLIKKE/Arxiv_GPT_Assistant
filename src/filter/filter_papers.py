import configparser
import dataclasses
import json
import os
import re
from typing import List, Dict, Any, Tuple
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

import retry
from tqdm import tqdm

from src.scraper.arxiv_scraper import Paper
from src.utils.helpers import EnhancedJSONEncoder, batched

def filter_by_author(all_authors: Dict, papers: List[Paper], author_targets: set, config: configparser.ConfigParser) -> Tuple[Dict, Dict]:
    """
    Filter and parse papers based on a target set of authors.
    """
    selected_papers = {}
    all_papers = {}

    for paper in papers:
        all_papers[paper.arxiv_id] = paper
        for author in paper.authors:
            if author in all_authors:
                for alias in all_authors[author]:
                    if alias["authorId"] in author_targets:
                        selected_papers[paper.arxiv_id] = {
                            **dataclasses.asdict(paper),
                        }
                        break
    return selected_papers, all_papers


def filter_papers_by_hindex(all_authors: Dict, papers: List[Paper], config: configparser.ConfigParser) -> List[Paper]:
    """
    Filters papers by checking to see if there's at least one author with an h-index > cutoff.
    (Currently cutoff logic is commented out in original, returning all matched).
    """
    paper_list = []
    for paper in papers:
        max_h = 0
        for author in paper.authors:
            if author in all_authors:
                max_h = max(
                    max_h, max([alias.get("hIndex", 0) for alias in all_authors[author]])
                )
        # if max_h >= float(config["FILTERING"]["hcutoff"]):
        paper_list.append(paper)
    return paper_list


def calc_price(model: str, usage: Any) -> float:
    """
    Calculate the estimated price of the LLM API call.
    """
    if model == "gpt-4-1106-preview":
        return (0.01 * usage.prompt_tokens + 0.03 * usage.completion_tokens) / 1000.0
    elif model == "gpt-4":
        return (0.03 * usage.prompt_tokens + 0.06 * usage.completion_tokens) / 1000.0
    elif model in ["gpt-3.5-turbo", "gpt-3.5-turbo-1106"]:
        return (0.0015 * usage.prompt_tokens + 0.002 * usage.completion_tokens) / 1000.0
    elif model == "deepseek-chat":
        return ((0.014 * usage.prompt_tokens) / 1_000_000) + ((0.28 * usage.completion_tokens) / 1_000_000)
    elif model == "glm-4-flash":
        return 0.0
    return 0.0


@retry.retry(tries=3, delay=2)
def call_chatgpt(full_prompt: str, openai_client: Any, model: str) -> Any:
    """
    Wrapper to call OpenAI API with retry logic.
    """
    return openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0,
        seed=0
    )


def run_and_parse_chatgpt(full_prompt: str, openai_client: Any, config: configparser.ConfigParser) -> Tuple[List[Dict], float]:
    """
    Runs the LLM prompt and attempts to parse the resulting JSON.
    """
    completion = call_chatgpt(full_prompt, openai_client, config["SELECTION"]["model"])
    out_text = completion.choices[0].message.content
    out_text = re.sub(r"```jsonl\n", "", out_text)
    out_text = re.sub(r"```", "", out_text)
    out_text = re.sub(r"\n+", "\n", out_text)
    out_text = re.sub(r"},", "}", out_text).strip()
    
    json_dicts = []
    for line in out_text.split("\n"):
        if not line.strip():
            continue
        try:
            json_dicts.append(json.loads(line))
        except Exception as ex:
            if config["OUTPUT"].getboolean("debug_messages", fallback=False):
                logging.error(f"Exception happened parsing JSON: {ex}")
                logging.debug(f"Failed line: {line}")
            continue
            
    cost = calc_price(config["SELECTION"]["model"], completion.usage) if hasattr(completion, 'usage') else 0.0
    return json_dicts, cost


def paper_to_string(paper_entry: Paper) -> str:
    """
    Renders each paper into a string to be processed by GPT.
    """
    return (
        f"ArXiv ID: {paper_entry.arxiv_id}\n"
        f"Title: {paper_entry.title}\n\n"
        f"Abstract: {paper_entry.abstract[:4000]}"
    )


def paper_to_titles(paper_entry: Paper) -> str:
    """
    Formats the paper title and ID.
    """
    return f"ArXiv ID: {paper_entry.arxiv_id} Title: {paper_entry.title}\n"


def filter_papers_by_title(
    papers: List[Paper], config: configparser.ConfigParser, openai_client: Any, base_prompt: str, criterion: str
) -> Tuple[List[Paper], float]:
    """
    Uses LLM to filter out obviously irrelevant papers based purely on their titles.
    """
    filter_postfix = (
        'Identify any papers that are absolutely and completely irrelevant to the criteria, '
        'formatted as a list of arxiv ids like ["ID1", "ID2", "ID3"..]. '
        'Be extremely cautious, and if you are unsure at all, do not add a paper in this list. '
        'You will check it in detail later.\n Directly respond with the list, do not add ANY extra text before or after the list.'
    )
    batches_of_papers = batched(papers, 1)
    final_list = []
    total_cost = 0.0
    
    model = config["SELECTION"]["model"]
    
    def process_batch(batch):
        papers_string = "".join([paper_to_titles(paper) for paper in batch])
        full_prompt = f"{base_prompt}\n {criterion}\n{papers_string}{filter_postfix}"
        try:
            completion = call_chatgpt(full_prompt, openai_client, model)
            out_text = completion.choices[0].message.content
            return json.loads(out_text), batch
        except Exception as ex:
            logging.error(f"Exception parsing list in title filtering: {ex}")
            return [], batch

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_batch, batch): batch for batch in batches_of_papers}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Filtering by title"):
            filtered_ids, batch = future.result()
            filtered_set = set(filtered_ids)
            for paper in batch:
                if paper.arxiv_id not in filtered_set:
                    final_list.append(paper)
                else:
                    logging.debug(f"Filtered out paper by title: {paper.title}")
            
    return final_list, total_cost


def run_on_batch(
    paper_batch: List[Paper], base_prompt: str, criterion: str, postfix_prompt: str, openai_client: Any, config: configparser.ConfigParser
) -> Tuple[List[Dict], float]:
    """
    Runs the LLM evaluation on a batch of papers.
    """
    batch_str = [paper_to_string(paper) for paper in paper_batch]
    full_prompt = "\n".join([
        base_prompt,
        criterion + "\n",
        "\n\n".join(batch_str) + "\n",
        postfix_prompt,
    ])
    return run_and_parse_chatgpt(full_prompt, openai_client, config)


def filter_by_gpt(
    paper_list: List[Paper], config: configparser.ConfigParser, openai_client: Any, all_papers: Dict[str, Paper], selected_papers: Dict[str, Dict]
) -> None:
    """
    Orchestrates the filtering process using an LLM based on given prompts.
    Updates the selected_papers dictionary in place.
    """
    try:
        with open("configs/base_prompt.txt", "r") as f:
            base_prompt = f.read()
        with open("configs/paper_topics.txt", "r") as f:
            criterion = f.read()
        with open("configs/postfix_prompt.txt", "r") as f:
            postfix_prompt = f.read()
    except FileNotFoundError as e:
        logging.error(f"Prompt config file missing: {e}")
        return

    all_cost = 0.0
    if config["SELECTION"].getboolean("run_openai", fallback=True):
        
        if config["FILTERING"].getboolean("filter_by_title", fallback=True):
            paper_list, cost = filter_papers_by_title(
                paper_list, config, openai_client, base_prompt, criterion
            )
            if config["OUTPUT"].getboolean("debug_messages", fallback=False):
                logging.info(f"{len(paper_list)} papers after title filtering. Title filtering cost: ${cost}")
            all_cost += cost
        else:
            if config["OUTPUT"].getboolean("debug_messages", fallback=False):
                logging.info("Skipping title filtering as configured.")

        batch_size = int(config["SELECTION"].get("batch_size", 5))
        batch_of_papers = batched(paper_list, batch_size)
        scored_batches = []
        
        def process_full_batch(batch):
            return run_on_batch(batch, base_prompt, criterion, postfix_prompt, openai_client, config)

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(process_full_batch, batch): batch for batch in batch_of_papers}
            for future in tqdm(as_completed(futures), total=len(futures), desc="Scoring papers"):
                scored_in_batch = []
                json_dicts, cost = future.result()
                all_cost += cost
                
                for jdict in json_dicts:
                    arxiv_id = jdict.get("ARXIVID")
                    if not arxiv_id or arxiv_id not in all_papers:
                        continue
                        
                    # Also keep RELEVANCE boolean check just in case, but rely primarily on score
                    is_relevant = bool(jdict.get("RELEVANCE", False))
                    try:
                        score = int(jdict.get("RELEVANCE_SCORE", 0))
                    except ValueError:
                        score = 0
                        
                    try:
                        novelty = int(jdict.get("NOVELTY_SCORE", 0))
                    except ValueError:
                        novelty = 0
                    
                    threshold = config["FILTERING"].getint("relevance_score_threshold", fallback=6)
                    novelty_threshold = config["FILTERING"].getint("novelty_score_threshold", fallback=5)
                    
                    if is_relevant and score >= threshold and novelty >= novelty_threshold:
                        selected_papers[arxiv_id] = {
                            **dataclasses.asdict(all_papers[arxiv_id]),
                            **jdict,
                        }
                        
                    scored_in_batch.append({
                        **dataclasses.asdict(all_papers[arxiv_id]),
                        **jdict,
                    })
                scored_batches.append(scored_in_batch)
            
        # Keep top K papers by RELEVANCE_SCORE and NOVELTY_SCORE
        top_k = config["FILTERING"].getint("top_k_papers", fallback=60)
        # Sort papers by sum of relevance and novelty scores descending
        def get_sort_key(item):
            rel_score = int(item[1].get("RELEVANCE_SCORE", 0) if str(item[1].get("RELEVANCE_SCORE", 0)).isdigit() else 0)
            nov_score = int(item[1].get("NOVELTY_SCORE", 0) if str(item[1].get("NOVELTY_SCORE", 0)).isdigit() else 0)
            return (rel_score + nov_score, rel_score) # sum first, then relevance score as tiebreaker
            
        sorted_papers = sorted(
            selected_papers.items(), 
            key=get_sort_key, 
            reverse=True
        )
        
        # Clear and repopulate with only the top K
        selected_papers.clear()
        for k, v in sorted_papers[:top_k]:
            selected_papers[k] = v

        if config["OUTPUT"].getboolean("dump_debug_file", fallback=False):
            debug_file = os.path.join(config["OUTPUT"].get("output_path", "out/"), "gpt_paper_batches.debug.json")
            with open(debug_file, "w") as outfile:
                json.dump(scored_batches, outfile, cls=EnhancedJSONEncoder, indent=4)
                
        if config["OUTPUT"].getboolean("debug_messages", fallback=False):
            logging.info(f"{len(selected_papers)} papers selected after title and abstract filtering.")
            logging.info(f"Total filtering cost: ${all_cost}")
