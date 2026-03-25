# 项目结构与功能说明文档 (Project Structure & Functions)

本项目(Arxiv_GPT_Assistant)旨在从 ArXiv 自动抓取论文，使用大语言模型（如 GPT、DeepSeek）对论文进行过滤与评分，并通过腾讯云进行标题和摘要的中文翻译，最后通过 Slack 和邮件将生成的每日论文推送给用户。

为提高代码的可维护性与扩展性，现已对项目代码进行了模块化重构与规范化。以下为整理后的代码架构说明。

## 📁 目录结构 (Directory Structure)

```
Arxiv_GPT_Assistant/
├── configs/                # 配置文件目录（Prompts, Authors, config.ini等）
├── docs/                   # 项目文档目录
├── in/                     # 输入示例数据目录
├── out/                    # 输出结果目录（生成的 JSON 和 Markdown 结果将存放于此）
├── src/                    # 核心源代码包
│   ├── filter/             # 论文过滤与评估模块
│   ├── notify/             # 消息通知模块 (Slack, Email)
│   ├── scraper/            # 数据抓取模块 (ArXiv, Semantic Scholar)
│   ├── translate/          # 翻译模块 (腾讯云机器翻译)
│   └── utils/              # 通用工具函数模块
├── main.py                 # 项目主入口文件
└── requirements.txt        # Python 依赖清单
```

---

## 📄 核心文件与函数功能说明

### 1. `main.py`
**功能**：项目的主入口，作为各个模块的编排者(Orchestrator)。
**主要函数/流程**：
- `get_papers_from_arxiv`: 从配置文件读取领域，调用爬虫模块获取论文。
- `main`: 主函数流程。初始化环境变量与配置 -> 调用 `scraper` 获取论文 -> 调用 `filter_papers` 过滤并由 LLM 评分 -> 调用 `translate` 翻译摘要与标题 -> 调用 `formatters` 生成 markdown / JSON，并写入到 `out/` 文件夹。

### 2. `src/scraper/arxiv_scraper.py`
**功能**：负责从 ArXiv 获取最新的研究论文。
**主要类与函数**：
- `Paper`: 数据类(dataclass)，用于统一存储论文的信息（如：作者、标题、摘要、ID）。
- `get_papers_from_arxiv_rss`: 通过解析 ArXiv RSS feed 获取最新发布的论文。
- `get_papers_from_arxiv_api`: 通过 ArXiv 官方 API 进行大范围时间内的论文搜索。
- `get_papers_from_arxiv_rss_api`: 综合 RSS 和 API 策略的爬虫入口。

### 3. `src/scraper/semantic_scholar.py`
**功能**：负责调用 Semantic Scholar API 以获取作者的详细信息、引用量和 h-index。
**主要函数**：
- `get_author_batch` / `get_one_author`: 获取特定作者详细元数据。
- `get_papers`: 获取论文的元数据。

### 4. `src/filter/filter_papers.py`
**功能**：论文的核心筛选和评估逻辑，包含基于作者匹配以及调用大型语言模型 (LLMs) 进行打分和判定。
**主要函数**：
- `filter_by_author`: 基于预设的重点作者列表对论文进行初步过滤。
- `filter_papers_by_title`: 借助 LLM 根据论文标题进行初步的快速筛除，降低后续处理的 Token 成本。
- `run_on_batch`: 将论文批量打包，发送给 LLM，根据 `base_prompt.txt` 等配置文件评估并返回 JSON。
- `filter_by_gpt`: 完整的大模型评估流程编排，筛选出高 Relevance 和 Novelty 的论文。

### 5. `src/translate/tencent_translate.py`
**功能**：接入腾讯云机器翻译(TMT) API，将英文论文的标题和摘要翻译为中文。
**主要类与函数**：
- `TencentCloudTranslator`: 翻译器的封装类，包含鉴权和请求逻辑。
- `TencentCloudTranslator.translate()`: 将英文文本转为中文并包含错误重试机制。

### 6. `src/notify/slack.py`
**功能**：将格式化后的论文列表推送到 Slack 频道。
**主要函数**：
- `push_to_slack`: 主推送入口。
- `build_block_list`: 构建 Slack 所需的 Block-kit 格式。
- `send_main_message` / `send_thread`: 发送主消息与 Thread 跟帖。

### 7. `src/notify/send_email.py`
**功能**：通过 SMTP (如 QQ 邮箱) 将生成的 HTML/Markdown 报告通过邮件发送给指定订阅者。
**主要函数**：
- `send_daily_email`: 邮件发送的完整逻辑封装，包含读取 HTML 报告、组合内容以及发送。

### 8. `src/utils/formatters.py`
**功能**：包含用于处理输出格式的辅助函数（原 `parse_json_to_md.py`）。
**主要函数**：
- `render_paper`: 将单篇论文的数据转换为 Markdown 格式字符串。
- `render_md_string`: 将筛选后的论文字典转换为完整的 Markdown 报告。

### 9. `src/utils/helpers.py`
**功能**：通用基础工具函数。
**主要类与函数**：
- `EnhancedJSONEncoder`: 增强版 JSON 编码器，支持 dataclass 序列化。
- `batched`: 提供对列表进行固定长度分块的功能。
- `argsort`: 原生 Python 的排序索引获取函数。

---

## 🛠️ 规范化与重构说明 (Refactoring Details)
1. **模块化 (Modularization)**：废弃了之前扁平化堆砌在根目录的做法。使用 `src` 包管理，将功能单一职责化。
2. **规范化 (Standardization)**：
   - 为各个主要函数添加了 `Docstrings`（文档字符串）和 `Type Hints`（类型提示）。
   - 优化了依赖导入结构，剔除或合并了冗余模块。
   - 对 LLM API 和爬虫的 Error Handling 进行了统一封装，增加了异常日志（`logging` 替代单纯的 `print`）。
3. **消除重复代码 (DRY Principle)**：将原来散落在多个文件中的 `batched`, `argsort`, 和 `EnhancedJSONEncoder` 集中收拢到 `src/utils/helpers.py` 中供全局调用。