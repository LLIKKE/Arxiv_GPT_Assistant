import configparser
import dataclasses
from dataclasses import dataclass
import json
import logging
import os
import re
from datetime import datetime, timedelta
from html import unescape
from typing import List, Optional, Tuple

import arxiv
import feedparser

from src.utils.helpers import EnhancedJSONEncoder

@dataclass
class Paper:
    """
    Data class representing a research paper.
    """
    authors: List[str]
    title: str
    abstract: str
    arxiv_id: str

    def __hash__(self):
        return hash(self.arxiv_id)

def is_earlier(ts1: str, ts2: str) -> bool:
    """
    Compare two arxiv_ids to check if ts1 is earlier than ts2.
    arxiv_id format is usually 'XXXX.XXXXXvX'.
    """
    try:
        id1_num = int(ts1.split('v')[0].replace('.', ''))
        id2_num = int(ts2.split('v')[0].replace('.', ''))
        return id1_num < id2_num
    except ValueError:
        return False

def get_papers_from_arxiv_api(area: str, timestamp: Optional[datetime], last_id: Optional[str], intervals=7) -> List[Paper]:
    """
    Fetch papers from arXiv API for a specific category within a time interval.
    """
    end_date = timestamp if timestamp else datetime.utcnow()
    start_date = end_date - timedelta(days=intervals)

    query = f"cat:{area} AND submittedDate:[{start_date.strftime('%Y%m%d')} TO {end_date.strftime('%Y%m%d')}]"
    search = arxiv.Search(
        query=query,
        max_results=200,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    
    api_papers = []
    for result in search.results():
        new_id = result.get_short_id()
        if last_id and is_earlier(last_id, new_id):
            continue
            
        authors = [author.name for author in result.authors]
        summary = unescape(re.sub(r"\n", " ", result.summary))
        
        if area in result.categories:
            paper = Paper(
                authors=authors,
                title=result.title,
                abstract=summary,
                arxiv_id=new_id,
            )
            api_papers.append(paper)
            
    return api_papers

def get_papers_from_arxiv_rss(area: str, config: Optional[dict]) -> Tuple[List[Paper], Optional[datetime], Optional[str]]:
    """
    Fetch papers from arXiv RSS feed for a specific category.
    """
    updated = datetime.utcnow() - timedelta(days=1)
    updated_string = updated.strftime("%a, %d %b %Y %H:%M:%S GMT")
    feed = feedparser.parse(
        f"https://export.arxiv.org/rss/{area}",
        modified=updated_string
    )
    
    logging.info(f"Feed Status: {feed.status}")
    logging.info(f"Feed entries count: {len(feed.entries)}")

    if feed.status == 304:
        if config and config.get("OUTPUT", {}).getboolean("debug_messages", fallback=False):
            logging.info(f"No new papers since {updated_string} for {area}")
        return [], None, None

    entries = feed.entries
    if not entries:
        logging.info(f"No entries found for {area}")
        return [], None, None

    last_id = entries[0].link.split("/")[-1]

    updated_field = feed.feed.get('updated', None)
    timestamp = None
    if updated_field:
        logging.info(f"Updated field from feed: {updated_field}")
        try:
            timestamp = datetime.strptime(updated_field, "%a, %d %b %Y %H:%M:%S +0000")
            logging.info(f"Parsed timestamp: {timestamp}")
        except ValueError as e:
            logging.error(f"Error parsing timestamp: {e}")
    else:
        logging.warning("No updated field found in feed.")

    paper_list = []
    force_primary = config.get("FILTERING", "force_primary", fallback="false").strip().lower() == "true" if config else False

    for entry in entries:
        if entry.get("arxiv_announce_type", "") != "new":
            continue
            
        paper_area = entry.tags[0].term if 'tags' in entry and len(entry.tags) > 0 else ""
        
        if area != paper_area and force_primary:
            logging.info(f"Ignoring {entry.title} as it belongs to {paper_area} instead of {area}")
            continue
            
        authors = [
            unescape(re.sub(r"<[^<]+?>", "", author)).strip()
            for author in entry.author.replace("\n", ", ").split(",")
        ]
        
        summary = re.sub(r"<[^<]+?>", "", entry.summary)
        summary = unescape(re.sub(r"\n", " ", summary))
        title = re.sub(r"\(arXiv:[0-9]+\.[0-9]+v[0-9]+ \[.*\]\)$", "", entry.title).strip()
        arxiv_id = entry.link.split("/")[-1]
        
        if area in paper_area:
            new_paper = Paper(authors=authors, title=title, abstract=summary, arxiv_id=arxiv_id)
            paper_list.append(new_paper)
        else:
            logging.debug(f"Skipping paper {title} as it does not belong to {area}")
            
    return paper_list, timestamp, last_id

def get_papers_from_arxiv_rss_api(area: str, config: Optional[dict]) -> List[Paper]:
    """
    Comprehensive method to fetch papers combining RSS and API.
    """
    paper_list, timestamp, last_id = get_papers_from_arxiv_rss(area, config)
    intervals = 3
    logging.info(f"Today's papers from RSS: {len(paper_list)}")
    
    if len(paper_list) == 0:
        logging.info(f"Attempting to fetch papers from API for {area}...")
        # Cap the timestamp to be recent
        if timestamp and timestamp < datetime.utcnow() - timedelta(days=7):
            logging.warning(f"Timestamp from RSS is too old ({timestamp}), using current time.")
            timestamp = datetime.utcnow()
        
        api_paper_list = get_papers_from_arxiv_api(area, timestamp, last_id, intervals)
        
        if len(api_paper_list) == 0:
            logging.info(f"No papers found via API for {area}. Trying wider search options...")
            extended_timestamp = timestamp - timedelta(days=intervals) if timestamp else None
            api_paper_list = get_papers_from_arxiv_api(area, extended_timestamp, last_id, intervals)
            
        paper_list = api_paper_list

    return paper_list

def get_papers(config: dict) -> List[Paper]:
    """
    Fetch all papers for predefined categories.
    """
    area_list = ["cs.AI", "cs.LG"]
    all_papers = []
    for area in area_list:
        papers = get_papers_from_arxiv_rss_api(area, config)
        all_papers.extend(papers)
    return all_papers

def save_papers(papers: List[Paper], output_path: str):
    """
    Save fetched papers to a JSON file.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_file = os.path.join(output_path, "papers.json")
    with open(output_file, "w", encoding='utf-8') as outfile:
        json.dump([dataclasses.asdict(paper) for paper in papers], outfile, indent=4, ensure_ascii=False, cls=EnhancedJSONEncoder)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    config = configparser.ConfigParser()
    config.read("configs/config.ini")
    all_papers = get_papers(config)
    save_papers(all_papers, "./output/")
    print(f"Fetched {len(all_papers)} papers.")
    if len(all_papers) > 0:
        print("\nTitles of the first ten papers:")
        for idx, paper in enumerate(all_papers[:10], 1):
            print(f"{idx}. {paper.title}")
    else:
        print("No papers fetched.")
