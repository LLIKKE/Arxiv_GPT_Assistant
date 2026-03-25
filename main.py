import re
import json
import configparser
import os
import io
import logging
from typing import List, Tuple, Set
from concurrent.futures import ThreadPoolExecutor, as_completed

from zhipuai import ZhipuAI
from openai import OpenAI

from src.scraper.arxiv_scraper import get_papers_from_arxiv_rss_api, Paper
from src.filter.filter_papers import filter_by_gpt, filter_by_author
from src.utils.formatters import render_md_string
from src.notify.slack import push_to_slack
from src.translate.tencent_translate import TencentCloudTranslator

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_papers_from_arxiv(config: configparser.ConfigParser) -> Set[Paper]:
    """
    Fetch papers from Arxiv based on categories specified in the configuration.
    """
    area_list = config["FILTERING"]["arxiv_category"].split(",")
    paper_set = set()
    for area in area_list:
        papers = get_papers_from_arxiv_rss_api(area.strip(), config)
        paper_set.update(set(papers))
        
    if config["OUTPUT"].getboolean("debug_messages", fallback=False):
        logging.info(f"Number of papers fetched: {len(paper_set)}")
        
    return paper_set

def parse_authors(lines: List[str]) -> Tuple[List[str], List[str]]:
    """
    Parse a comma-separated author list, ignoring empty lines or comments starting with '#'.
    """
    author_ids = []
    authors = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        author_split = line.split(",")
        if len(author_split) >= 2:
            authors.append(author_split[0].strip())
            author_ids.append(author_split[1].strip())
    return authors, author_ids

def clean_markdown_formatting(text: str) -> str:
    """
    Cleans up common markdown formatting issues often introduced by LLMs or translation.
    """
    if not text:
        return text
    # Fix spaces inside bold tags: "** text **" -> "**text**"
    text = re.sub(r'\*\*\s+([^\*]+?)\s+\*\*', r'**\1**', text)
    # Fix left space: "** text**" -> "**text**"
    text = re.sub(r'\*\*\s+([^\*]+?)\*\*', r'**\1**', text)
    # Fix right space: "**text **" -> "**text**"
    text = re.sub(r'\*\*([^\*]+?)\s+\*\*', r'**\1**', text)
    # Fix combined heading and bold: "#** text **" -> "### text"
    text = re.sub(r'#+\s*\*\*\s*(.+?)\s*\*\*', r'### \1', text)
    # Fix missing space after heading: "#text" -> "# text"
    text = re.sub(r'^(#{1,6})([^#\s])', r'\1 \2', text, flags=re.MULTILINE)
    return text

def generate_daily_summary(selected_papers: dict, client: OpenAI, config: configparser.ConfigParser) -> str:
    """
    Generate a daily summary using LLM based on the selected papers.
    """
    if not selected_papers:
        return "No relevant papers found today."
        
    papers_context = ""
    for idx, (paper_id, paper) in enumerate(selected_papers.items(), 1):
        title = paper.get('title', 'Unknown Title')
        comment = paper.get('COMMENT', '')
        papers_context += f"{idx}. {title}\nHighlight: {comment}\n\n"
        
    prompt = (
        "You are an expert AI researcher. I will provide you with a list of the most important AI papers published today, "
        "along with a brief highlight for each. \n\n"
        "Your task is to write a highly professional 'Daily Research Summary'. \n"
        "Please categorize your summary based on the main research directions (e.g., SFT, RL for LLMs, Agents, Multimodal, Compression). "
        "For each direction that has relevant papers today, write ONE concise and insightful paragraph summarizing the general trend or key breakthroughs. "
        "Do NOT just list the papers again. Synthesize the information.\n\n"
        "Output the summary in Markdown format. Use `###` for direction headers.\n\n"
        f"Here are the papers:\n{papers_context}"
    )
    
    try:
        response = client.chat.completions.create(
            model=config["SELECTION"]["model"],
            messages=[
                {"role": "system", "content": "You are a senior AI research scientist writing a newsletter summary."},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            temperature=0.7,
        )
        return clean_markdown_formatting(response.choices[0].message.content.strip())
    except Exception as e:
        logging.error(f"Failed to generate daily summary: {e}")
        return "Failed to generate daily summary due to an API error."

def translate_to_chinese_via_deepseek(text: str, client: OpenAI, config: configparser.ConfigParser) -> str:
    """
    Optional alternative: Translate English text to Chinese using DeepSeek API.
    """
    try:
        response = client.chat.completions.create(
            model=config["SELECTION"]["model"],
            messages=[
                {"role": "system", "content": "You are a helpful assistant that translates English text to Chinese."},
                {"role": "user", "content": f"Translate the following text to Chinese:\n\n{text}"},
            ],
            stream=False,
            temperature=1.0,
            seed=0
        )
        return clean_markdown_formatting(response.choices[0].message.content.strip())
    except Exception as e:
        logging.error(f"Translation failed: {e}")
        return text

def main():
    config = configparser.ConfigParser()
    config.read("configs/config.ini")

    # API Keys
    S2_API_KEY = os.environ.get("S2_KEY")
    secret_id = os.environ.get("SECRET_ID")
    secret_key = os.environ.get("SECRET_KEY")
    OAI_KEY = os.environ.get("OAI_KEY")
    
    if OAI_KEY is None:
        raise ValueError("OpenAI key is not set - please set OAI_KEY to your API key")

    # Initialize AI Client
    if "deepseek" in config["SELECTION"]["model"]:
        openai_client = OpenAI(api_key=OAI_KEY, base_url="https://api.deepseek.com")
    elif "glm" in config["SELECTION"]["model"]:
        openai_client = ZhipuAI(api_key=OAI_KEY)
    else:
        openai_client = OpenAI(api_key=OAI_KEY) # Fallback to default OpenAI

    # Load author list
    try:
        with io.open("configs/authors.txt", "r", encoding="utf-8") as fopen:
            author_names, author_ids = parse_authors(fopen.readlines())
        author_id_set = set(author_ids)
    except FileNotFoundError:
        logging.warning("configs/authors.txt not found, author filtering will be skipped.")
        author_id_set = set()

    # Fetch papers
    papers = list(get_papers_from_arxiv(config))
    
    all_authors = set()
    for paper in papers:
        all_authors.update(set(paper.authors))

    if config["OUTPUT"].getboolean("debug_messages", fallback=False):
        logging.info(f"Gathered {len(all_authors)} unique authors from papers.")

    # Note: Semantic Scholar author fetching and author-based filtering is disabled by default
    # If needed, it can be re-enabled here using src.scraper.semantic_scholar

    all_papers = {paper.arxiv_id: paper for paper in papers}
    selected_papers = {}

    # Filter papers via GPT
    logging.info("Starting GPT filtering...")
    filter_by_gpt(papers, config, openai_client, all_papers, selected_papers)

    # Generate Daily Summary
    logging.info("Generating daily summary...")
    daily_summary_en = generate_daily_summary(selected_papers, openai_client, config)

    # Translate titles and abstracts using Tencent Cloud
    daily_summary_cn = daily_summary_en
    if secret_id and secret_key:
        logging.info("Starting translation...")
        translator = TencentCloudTranslator(secret_id, secret_key)
        
        # Translate the daily summary
        logging.info("Translating daily summary...")
        try:
            translated_summary = translator.translate(daily_summary_en)
            if translated_summary:
                daily_summary_cn = clean_markdown_formatting(translated_summary)
        except Exception as e:
            logging.error(f"Failed to translate daily summary: {e}")

        def translate_paper(paper_id, paper):
            try:
                title_cn = clean_markdown_formatting(translator.translate(paper.get('title', '')))
                abstract_cn = clean_markdown_formatting(translator.translate(paper.get('abstract', '')))
                return paper_id, {
                    'title_cn': title_cn if title_cn else "[Translation Failed]",
                    'abstract_cn': abstract_cn if abstract_cn else "[Translation Failed]"
                }
            except Exception as e:
                logging.error(f"Failed to translate paper {paper_id}: {e}")
                return paper_id, {
                    'title_cn': "[Translation Failed]",
                    'abstract_cn': "[Translation Failed]"
                }

        logging.info("Translating papers concurrently...")
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(translate_paper, pid, p): pid for pid, p in selected_papers.items()}
            for future in as_completed(futures):
                pid, translated_data = future.result()
                selected_papers[pid].update(translated_data)
                
    else:
        logging.warning("Tencent Cloud SECRET_ID or SECRET_KEY missing. Skipping translation.")

    # Output generation
    output_path = config["OUTPUT"].get("output_path", "out/")
    os.makedirs(output_path, exist_ok=True)

    if config["OUTPUT"].getboolean("dump_json", fallback=True):
        with open(os.path.join(output_path, "output.json"), "w", encoding="utf-8") as outfile:
            json.dump(selected_papers, outfile, indent=4, ensure_ascii=False)

    if config["OUTPUT"].getboolean("dump_md", fallback=True):
        # Generate standard markdown
        with open(os.path.join(output_path, "output.md"), "w", encoding="utf-8") as f:
            f.write(render_md_string(selected_papers, daily_summary_en))
            
        # Generate translated markdown
        with open(os.path.join(output_path, "output_translated.md"), "w", encoding="utf-8") as f:
            # Add translated summary to the top
            f.write(f"# 💡 今日研究速览 (Daily Summary)\n\n{daily_summary_cn}\n\n---\n\n")
            
            for idx, (paper_id, paper) in enumerate(selected_papers.items(), 1):
                f.write(f"## {idx}. {paper.get('title_cn', 'Untitled')}\n\n")
                f.write(f"**作者**: {', '.join(paper.get('authors', []))}\n\n")
                f.write(f"**机构**: {paper.get('AFFILIATIONS', 'Unknown Institution')}\n\n")
                f.write(f"**摘要**: {paper.get('abstract_cn', 'No abstract')}\n\n")
                f.write(f"[阅读原文](https://arxiv.org/abs/{paper_id})\n\n---\n\n")
                
    logging.info("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
