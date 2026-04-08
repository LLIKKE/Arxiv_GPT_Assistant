import re
import json
import configparser
import os
import io
import logging
import datetime
import shutil
from typing import List, Tuple, Set
from concurrent.futures import ThreadPoolExecutor, as_completed

from zhipuai import ZhipuAI
from openai import OpenAI

from src.scraper.arxiv_scraper import get_papers_from_arxiv_rss_api, Paper
from src.filter.filter_papers import filter_by_gpt
from src.utils.formatters import render_md_string
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
    # Remove any hallucinated old dates from summary
    text = re.sub(r'2024[年-]?0?4[月-]?16日?', '', text)
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
        
    beijing_tz = datetime.timezone(datetime.timedelta(hours=8))
    today_str = datetime.datetime.now(beijing_tz).strftime("%Y-%m-%d")
    
    papers_context = ""
    for idx, (paper_id, paper) in enumerate(selected_papers.items(), 1):
        title = paper.get('title', 'Unknown Title')
        comment = paper.get('COMMENT', '')
        papers_context += f"{idx}. {title}\nHighlight: {comment}\n\n"
        
    prompt = (
        "You are an expert AI researcher. I will provide you with a list of the most important AI papers published today, "
        "along with a brief highlight for each. \n\n"
        f"CRITICAL: Today's date is {today_str}. Please use this date if you need to mention it, but do NOT include a date header.\n\n"
        "Your task is to write a highly professional 'Daily Research Summary'. \n"
        "Please categorize your summary based on the main research directions (e.g., SFT, RL for LLMs, Agents, Multimodal, Compression). \n"
        "For each direction that has relevant papers today, write ONE concise and insightful paragraph summarizing the general trend or key breakthroughs. \n"
        "Do NOT just list the papers again. Synthesize the information.\n\n"
        "Output the summary in Markdown format. Use `###` for direction headers.\n"
        "IMPORTANT: DO NOT include a title like '# Daily Summary' or '# 每日调研汇总' or any date header. Just start with the category headers.\n"
        "DO NOT use any old dates like 2024-04-16. Use ONLY the date provided above if needed.\n\n"
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
    history_path = "history/"
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(history_path, exist_ok=True)
    
    # Get Beijing Time (UTC+8) for the date string
    beijing_tz = datetime.timezone(datetime.timedelta(hours=8))
    today_str = datetime.datetime.now(beijing_tz).date().isoformat()

    if config["OUTPUT"].getboolean("dump_json", fallback=True):
        # Create a single dict to hold everything for the date
        daily_data = {
            "summary_en": daily_summary_en,
            "summary_cn": daily_summary_cn,
            "papers": selected_papers
        }
        # Save to history
        with open(os.path.join(history_path, f"{today_str}.json"), "w", encoding="utf-8") as outfile:
            json.dump(daily_data, outfile, indent=4, ensure_ascii=False)
        # Also save as latest output.json in out/ for backward compatibility
        with open(os.path.join(output_path, "output.json"), "w", encoding="utf-8") as outfile:
            json.dump(selected_papers, outfile, indent=4, ensure_ascii=False)

    if config["OUTPUT"].getboolean("dump_md", fallback=True):
        # Generate standard markdown
        md_content = render_md_string(selected_papers, daily_summary_en)
        with open(os.path.join(history_path, f"{today_str}.md"), "w", encoding="utf-8") as f:
            f.write(md_content)
        with open(os.path.join(output_path, "output.md"), "w", encoding="utf-8") as f:
            f.write(md_content)
            
        # Generate translated markdown
        translated_md_content = f"# 💡 今日研究速览 (Daily Summary)\n\n{daily_summary_cn}\n\n---\n\n"
        for idx, (paper_id, paper) in enumerate(selected_papers.items(), 1):
            translated_md_content += f"## {idx}. {paper.get('title_cn', 'Untitled')}\n\n"
            translated_md_content += f"**作者**: {', '.join(paper.get('authors', []))}\n\n"
            translated_md_content += f"**机构**: {paper.get('AFFILIATIONS', 'Unknown Institution')}\n\n"
            translated_md_content += f"**摘要**: {paper.get('abstract_cn', 'No abstract')}\n\n"
            translated_md_content += f"[阅读原文](https://arxiv.org/abs/{paper_id})\n\n---\n\n"
            
        with open(os.path.join(history_path, f"{today_str}_translated.md"), "w", encoding="utf-8") as f:
            f.write(translated_md_content)
        with open(os.path.join(output_path, "output_translated.md"), "w", encoding="utf-8") as f:
            f.write(translated_md_content)

    # Copy all history JSON files to out/ so the webpage can fetch them
    for filename in os.listdir(history_path):
        if filename.endswith(".json"):
            shutil.copy(os.path.join(history_path, filename), os.path.join(output_path, filename))

    # Generate a list of available dates
    available_dates = sorted([f.replace('.json', '') for f in os.listdir(history_path) if f.endswith('.json') and not f.startswith('output')], reverse=True)
    with open(os.path.join(output_path, "dates.json"), "w", encoding="utf-8") as f:
        json.dump(available_dates, f, indent=4)

    # Generate index.html for the web homepage
    index_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Arxiv Papers</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        .controls {{ margin-bottom: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef; }}
        select {{ padding: 8px; font-size: 16px; border-radius: 4px; border: 1px solid #ced4da; }}
        .summary {{ background: #eef2f7; padding: 20px; border-radius: 8px; margin-bottom: 30px; border-left: 5px solid #2c3e50; }}
        .paper {{ margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid #eee; }}
        .paper-title {{ font-size: 1.2em; font-weight: bold; margin-bottom: 10px; }}
        .paper-authors {{ color: #666; font-style: italic; margin-bottom: 10px; }}
        .paper-abstract {{ margin-bottom: 15px; text-align: justify; white-space: pre-wrap; }}
        .paper-link a {{ display: inline-block; padding: 5px 10px; background: #007bff; color: white; text-decoration: none; border-radius: 4px; }}
        .paper-link a:hover {{ background: #0056b3; }}
        #loading {{ text-align: center; color: #666; font-style: italic; display: none; }}
    </style>
</head>
<body>
    <h1>📚 Daily Arxiv Paper Recommendations</h1>
    
    <div class="controls">
        <label for="date-select"><strong>Select Date: </strong></label>
        <select id="date-select" onchange="loadPapers()"></select>
    </div>

    <div id="loading">Loading papers...</div>
    <div id="summary-container" class="summary" style="display:none;"></div>
    <div id="papers-container"></div>

    <script>
        let dates = [];

        async function init() {{
            try {{
                const response = await fetch('dates.json');
                dates = await response.json();
                
                const select = document.getElementById('date-select');
                if (dates.length === 0) {{
                    select.innerHTML = '<option value="">No data available</option>';
                    return;
                }}
                
                dates.forEach(date => {{
                    const option = document.createElement('option');
                    option.value = date;
                    option.textContent = date;
                    select.appendChild(option);
                }});
                
                // Load the most recent date by default
                loadPapers();
            }} catch (error) {{
                console.error('Error loading dates:', error);
                document.getElementById('papers-container').innerHTML = '<p>Error loading dates list. Please try again later.</p>';
            }}
        }}

        async function loadPapers() {{
            const select = document.getElementById('date-select');
            const date = select.value;
            if (!date) return;

            const container = document.getElementById('papers-container');
            const summaryContainer = document.getElementById('summary-container');
            const loading = document.getElementById('loading');
            
            container.innerHTML = '';
            summaryContainer.innerHTML = '';
            summaryContainer.style.display = 'none';
            loading.style.display = 'block';

            try {{
                const response = await fetch(`${{date}}.json`);
                const data = await response.json();
                
                loading.style.display = 'none';
                
                // Handle both new format (with summary) and old format (just papers)
                const papers = data.papers || data;
                const summary = data.summary_cn || data.summary_en || "";

                if (summary) {{
                    summaryContainer.innerHTML = '<h3>💡 今日研究速览 (Daily Summary)</h3>' + summary.replace(/\n/g, '<br>');
                    summaryContainer.style.display = 'block';
                }}
                
                if (Object.keys(papers).length === 0) {{
                    container.innerHTML = '<p>No papers found for this date.</p>';
                    return;
                }}

                for (const [id, paper] of Object.entries(papers)) {{
                    const paperDiv = document.createElement('div');
                    paperDiv.className = 'paper';
                    
                    const title = paper.title_cn && paper.title_cn !== '[Translation Failed]' ? paper.title_cn : paper.title;
                    const abstract = paper.abstract_cn && paper.abstract_cn !== '[Translation Failed]' ? paper.abstract_cn : paper.abstract;
                    const authors = paper.authors ? paper.authors.join(', ') : 'Unknown Authors';
                    const link = `https://arxiv.org/abs/${{id}}`;
                    
                    paperDiv.innerHTML = `
                        <div class="paper-title">${{title}}</div>
                        <div class="paper-authors">${{authors}}</div>
                        <div class="paper-abstract">${{abstract}}</div>
                        <div class="paper-link"><a href="${{link}}" target="_blank">Read Paper</a></div>
                    `;
                    
                    container.appendChild(paperDiv);
                }}
            }} catch (error) {{
                console.error('Error loading papers:', error);
                loading.style.display = 'none';
                container.innerHTML = '<p>Error loading papers for selected date. Please try again later.</p>';
            }}
        }}

        // Initialize the page
        init();
    </script>
</body>
</html>"""
    
    with open(os.path.join(output_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html_content)
        
    logging.info("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
