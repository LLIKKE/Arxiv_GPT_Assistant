# 📚 ArXiv GPT Assistant

A powerful, automated daily ArXiv paper scanner that leverages Large Language Models (like DeepSeek, GPT-4, GLM) to find, summarize, translate, and deliver the most relevant AI research papers tailored specifically to your interests.

![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-V3-blue?style=for-the-badge)

---

## ✨ Key Features

- **🎯 LLM-Powered Filtering**: Uses advanced LLMs to evaluate daily ArXiv submissions based on your specific research criteria (e.g., SFT, RLHF, Agents, Multimodal).
- **⚡ Concurrent Processing**: High-speed, multi-threaded evaluation and translation (reduces processing time from minutes to seconds).
- **📝 Daily Research Summary**: Automatically generates a highly professional, synthesized daily newsletter summarizing the trends from the selected papers.
- **🌐 Bilingual Support**: Automatically translates paper titles, abstracts, and daily summaries into Chinese using the Tencent Cloud TMT API.
- **🎨 Beautiful UI & Delivery**: 
  - Automatically deploys a modern, card-based static website to GitHub Pages.
  - Sends beautifully formatted HTML emails with the daily summary directly to your inbox.
  - Optional Slack bot integration for team channels.

---

## 🚀 Quick Start (Running on GitHub Actions)

The easiest way to use this assistant is to fork this repository and let GitHub Actions do the work for you entirely for free!

1. **Fork this repository**.
2. **Configure your interests**: 
   - Edit `configs/paper_topics.txt` to define the research topics and criteria you care about.
   - Adjust `configs/config.ini` to set the `arxiv_category` (e.g., `cs.CL, cs.LG, cs.AI, cs.CV, cs.IR`).
3. **Set up GitHub Secrets**:
   Go to your repository settings -> **Secrets and variables** -> **Actions** and add the following secrets:
   - `OAI_KEY`: Your LLM API key (DeepSeek / OpenAI / ZhipuAI).
   - `FROM_ADDR` & `PASSWORD`: Your sender email address and SMTP password (e.g., App-specific password for QQ/Gmail).
   - `TO_ADDR`: The email address where you want to receive the daily newsletter.
   - `SECRET_ID` & `SECRET_KEY`: (Optional) Your Tencent Cloud API keys for Chinese translation.
4. **Enable GitHub Pages**:
   Go to your repository settings -> **Pages** -> Build and deployment -> Source: select **GitHub Actions**.
5. **Enable Workflows**:
   Go to the **Actions** tab in your forked repo and enable the workflows. The `Run daily arxiv` action will now run every day at 21:00 UTC automatically!

---

## 💻 Running Locally

If you prefer to run or debug the code on your local machine:

1. Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your environment variables:
```bash
export OAI_KEY="your_api_key_here"
export SECRET_ID="your_tencent_secret_id"  # Optional for translation
export SECRET_KEY="your_tencent_secret_key" # Optional for translation
```

3. Run the main script:
```bash
python main.py
```

The output JSON and Markdown files will be generated in the `out/` folder.

---

## ⚙️ How It Works (The Pipeline)

1. **Scraping (`src/scraper/`)**: Fetches all new papers from the specified ArXiv RSS feeds/API within the last 24 hours.
2. **Title Pre-filtering (`src/filter/`)**: Uses LLMs to quickly discard obviously irrelevant papers based purely on their titles, saving API costs.
3. **Deep Evaluation (`src/filter/`)**: The remaining papers are sent to the LLM in concurrent batches. The LLM evaluates them against your `paper_topics.txt`, extracting affiliations and writing a 1-sentence highlight (`COMMENT`).
4. **Summarization (`main.py`)**: The LLM synthesizes all selected papers into a comprehensive "Daily Research Summary".
5. **Translation (`src/translate/`)**: Titles, abstracts, and summaries are translated into Chinese concurrently via Tencent Cloud.
6. **Formatting & Delivery (`src/notify/`)**: The results are rendered into beautiful HTML/Markdown and delivered via GitHub Pages, Email, and Slack.

---

## 📂 Project Structure

```
Arxiv_GPT_Assistant/
├── configs/                # Prompts, filter criteria, and config.ini
├── docs/                   # Detailed project documentation
├── out/                    # Generated JSON and Markdown outputs
├── src/                    # Core source code
│   ├── filter/             # LLM evaluation and filtering logic
│   ├── notify/             # Email and Slack delivery modules
│   ├── scraper/            # ArXiv and Semantic Scholar API clients
│   ├── translate/          # Tencent Cloud translation wrapper
│   └── utils/              # Markdown formatters and helpers
└── main.py                 # Main orchestrator script
```
*For a detailed breakdown of every module and function, please see [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md).*

---

## 🤝 Acknowledgments

This repository is a heavily refactored, modernized, and feature-enhanced version of the original concept by Tatsunori Hashimoto. 

**Recent Major Updates:**
- Modularized architecture (`src/` structure).
- Fully asynchronous/concurrent LLM and Translation API calls.
- Addition of an LLM-generated Daily Summary.
- Beautiful card-based UI for GitHub Pages and Email Newsletters.
- Institution/Affiliation extraction.