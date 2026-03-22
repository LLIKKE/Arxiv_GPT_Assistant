import json
import os
from datetime import datetime
from typing import List, Dict

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from src.utils.helpers import batched

def send_main_message(block_list: List, channel_id: str, client: WebClient) -> str:
    """
    Sends the main message blocks to Slack.
    """
    try:
        result = client.chat_postMessage(
            channel=channel_id,
            blocks=block_list,
            text="Arxiv update",
            unfurl_links=False,
        )
        print(f"Message sent successfully: {result['ts']}")
        return result["ts"]
    except SlackApiError as e:
        print(f"Error sending main message: {e}")
        return ""

def send_thread(block_list: List, channel_id: str, thread_id: str, client: WebClient):
    """
    Sends additional message blocks to the thread in Slack.
    """
    try:
        batches = batched(block_list, 50)
        for batch in batches:
            result = client.chat_postMessage(
                thread_ts=thread_id,
                text="Arxiv full update",
                channel=channel_id,
                blocks=batch,
                unfurl_links=False,
            )
            print(f"Thread message sent successfully: {result['ts']}")
    except SlackApiError as e:
        print(f"Error sending thread message: {e}")

def render_paper(paper_entry: Dict, counter: int) -> str:
    """
    Renders a paper to a slack-compatible mrkdwn string.
    """
    arxiv_id = paper_entry.get("arxiv_id", "")
    title = paper_entry.get("title", "")
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
    abstract = paper_entry.get("abstract", "")
    authors = paper_entry.get("authors", [])
    
    paper_string = f"<{arxiv_url}|*{counter}. {title.replace('&', '&amp;')}*>\n"
    paper_string += f'*Authors*: {", ".join(authors)}\n\n'
    paper_string += f"*Abstract*: {abstract}\n\n"
    
    if "RELEVANCE" in paper_entry and "NOVELTY" in paper_entry:
        paper_string += f"*Relevance*: {paper_entry['RELEVANCE']}\t"
        paper_string += f"*Novelty*: {paper_entry['NOVELTY']}\t"
    if "COMMENT" in paper_entry:
        paper_string += f"*Comment*: {paper_entry['COMMENT']}\n"
        
    return paper_string

def render_title(paper_entry: Dict, counter: int) -> str:
    """
    Renders the title of the paper to a slack-compatible mrkdwn string.
    """
    arxiv_id = paper_entry.get("arxiv_id", "")
    title = paper_entry.get("title", "")
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
    authors = paper_entry.get("authors", [])
    
    paper_string = f"<{arxiv_url}|*{counter}. {title.replace('&', '&amp;')}*>\n"
    paper_string += f'*Authors*: {", ".join(authors)}\n\n'
    return paper_string

def build_block_list(title_strings: List[str], paper_strings: List[str]) -> tuple[List[Dict], List[Dict]]:
    """
    Builds a list of Slackbot blocks from a list of markdown formatted papers.
    """
    slack_block_list = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Paper alert bot update on {datetime.today().strftime('%m/%d/%Y')}",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Total relevant papers (max 50 in thread): {len(title_strings)}\n Top 20 titles shown below",
            },
        },
        {"type": "divider"},
    ]

    for paper in title_strings[:20]:
        slack_block_list.append({"type": "section", "text": {"type": "mrkdwn", "text": paper}})

    thread_blocks = []
    for paper in paper_strings[:50]:
        thread_blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": paper}})
        thread_blocks.append({"type": "divider"})

    return slack_block_list, thread_blocks

def push_to_slack(papers_dict: Dict):
    """
    Main entry point to push a dictionary of papers to Slack.
    """
    channel_id = os.environ.get("SLACK_CHANNEL_ID")
    slack_key = os.environ.get("SLACK_KEY")
    
    if not channel_id or not slack_key:
        print("Missing SLACK_CHANNEL_ID or SLACK_KEY. Skipping slack notification.")
        return
        
    client = WebClient(token=slack_key)
    
    if not papers_dict:
        print("No papers to push to slack.")
        return
        
    title_strings = [render_title(paper, i) for i, paper in enumerate(papers_dict.values())]
    paper_strings = [render_paper(paper, i) for i, paper in enumerate(papers_dict.values())]
    
    blocks, thread_blocks = build_block_list(title_strings, paper_strings)
    
    ts = send_main_message(blocks, channel_id, client)
    if ts:
        send_thread(thread_blocks, channel_id, ts, client)

if __name__ == "__main__":
    try:
        with open("out/output.json", "r") as f:
            output = json.load(f)
        push_to_slack(output)
    except FileNotFoundError:
        print("No output.json found to push to slack.")
