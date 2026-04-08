import json
from datetime import datetime, timezone, timedelta
from typing import Dict

def render_paper(paper_entry: Dict, idx: int) -> str:
    """
    Renders a single paper entry into styled HTML/Markdown.
    """
    arxiv_id = paper_entry.get("arxiv_id", "")
    title = paper_entry.get("title", "")
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
    abstract = paper_entry.get("abstract", "")
    authors = paper_entry.get("authors", [])
    affiliations = paper_entry.get("AFFILIATIONS", "Unknown Institution")
    comment = paper_entry.get("COMMENT", "")
    
    # Render with HTML for better card layout in markdown parsers
    paper_string = f'<div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; margin-bottom: 20px; background-color: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">'
    paper_string += f'<h2 style="margin-top: 0; color: #0366d6;">{idx}. <a href="{arxiv_url}" target="_blank" style="text-decoration: none; color: inherit;">{title}</a> <a id="link{idx}"></a></h2>'
    
    paper_string += f'<p style="font-size: 14px; color: #586069; margin: 5px 0;">'
    paper_string += f'<strong>ArXiv ID:</strong> {arxiv_id} | '
    if "RELEVANCE" in paper_entry and "NOVELTY" in paper_entry:
        paper_string += f'<strong>Relevance:</strong> <span style="background-color: #e6f3ff; padding: 2px 6px; border-radius: 4px;">{paper_entry["RELEVANCE"]}</span> | '
        paper_string += f'<strong>Novelty:</strong> <span style="background-color: #e6f3ff; padding: 2px 6px; border-radius: 4px;">{paper_entry["NOVELTY"]}</span>'
    paper_string += f'</p>'
    
    paper_string += f'<p style="font-size: 15px; margin: 10px 0;"><strong>👥 Authors:</strong> <em>{", ".join(authors)}</em></p>'
    paper_string += f'<p style="font-size: 14px; color: #444; margin: 5px 0 15px 0;"><strong>🏫 Affiliations:</strong> {affiliations}</p>'
    
    if comment:
        paper_string += f'<div style="background-color: #fffbdd; border-left: 4px solid #ffe564; padding: 10px 15px; margin-bottom: 15px; border-radius: 0 4px 4px 0;">'
        paper_string += f'<strong>💡 Highlight:</strong> {comment}'
        paper_string += f'</div>'
        
    paper_string += f'<details style="margin-top: 10px; cursor: pointer;">'
    paper_string += f'<summary style="font-weight: bold; color: #0366d6;">View Abstract</summary>'
    paper_string += f'<p style="margin-top: 10px; line-height: 1.6; color: #24292e;">{abstract}</p>'
    paper_string += f'</details>'
    
    paper_string += f'</div>\n\n'
    
    return paper_string

def render_title_and_author(paper_entry: Dict, idx: int) -> str:
    """
    Renders the title and author for the Table of Contents.
    """
    title = paper_entry.get("title", "")
    authors = paper_entry.get("authors", [])
    paper_string = f"{idx}. [{title}](#link{idx})\n"
    paper_string += f'**Authors:** {", ".join(authors)}\n'
    return paper_string

def render_md_string(papers_dict: Dict, daily_summary: str = "") -> str:
    """
    Renders the entire collection of selected papers into a single Markdown string.
    """
    try:
        with open("configs/paper_topics.txt", "r") as f:
            criterion = f.read()
    except FileNotFoundError:
        criterion = "Criteria not found."

    # Header section with Date
    output_string = (
        f"# 📚 Personalized Daily Arxiv Papers - {datetime.now(timezone(timedelta(hours=8))).strftime('%B %d, %Y')}\n\n"
        f"**Total relevant papers:** {len(papers_dict)}\n\n"
    )

    # Daily Summary Section
    if daily_summary:
        output_string += (
            f"## 💡 Daily Research Summary\n"
            f"<div style='background-color: #f6f8fa; border-left: 4px solid #24292e; padding: 15px; margin-bottom: 20px; border-radius: 4px;'>\n"
            f"{daily_summary}\n"
            f"</div>\n\n"
        )

    # Table of Contents
    output_string += "## 📑 Table of Contents\n\n"
    title_strings = [
        render_title_and_author(paper, i)
        for i, paper in enumerate(papers_dict.values(), 1)
    ]
    output_string += "\n".join(title_strings) + "\n\n---\n\n"
    
    # Paper Details
    output_string += "## 📝 Detailed Papers\n\n"
    paper_strings = [
        render_paper(paper, i) for i, paper in enumerate(papers_dict.values(), 1)
    ]
    output_string += "\n".join(paper_strings)
    
    # Footer Criteria
    output_string += "\n\n---\n\n"
    output_string += f"<details><summary>Click to view Paper Selection Criteria</summary>\n\n{criterion}\n</details>"
    
    return output_string

if __name__ == "__main__":
    # Test script functionality
    try:
        with open("out/output.json", "r") as f:
            output = json.load(f)
        with open("out/output.md", "w") as f:
            f.write(render_md_string(output))
    except FileNotFoundError:
        print("No output.json found to render.")
