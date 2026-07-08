# 💡 今日研究速览 (Daily Summary)

### RL for LLMs and Agents
The dominant theme in today’s papers is the maturation of reinforcement learning (RL) as a core training paradigm for large language models (LLMs) and agents, moving beyond simple reward hacking towards principled, structured, and verifiable optimization. A critical finding from the analysis of self-play reward hacking (Paper 1) warns that reference-free judges can reward plausibility over correctness, a failure mode that the community must address through de-anchoring techniques. To counter this, several works propose grounding rewards in objective signals: from mixed-mode advantage estimation to mitigate hallucination in reasoning models (Paper 7), to verifiable economic outcomes for LLM negotiation (Paper 9), and visual-action outcome alignment for physical reasoning (Paper 10). For agentic systems, the field is converging on offline and on-policy frameworks that treat the *control* of a frozen agent’s harness as a distinct MDP (Paper 2), using information gain to budget tree-structured rollout exploration (Paper 3), and employing turn-level distillation for long-horizon tasks (Paper 11). The integration of cross-episode memory (Paper 4) and failure-driven dynamic data curation (Paper 6) further refines the agentic post-training loop, while a systematic study of reward function composition (Paper 8) confirms that reward design is the primary determinant of optimization success in process model generation.

### Multimodal and Structured Reasoning
A significant trend is the application of RL fine-tuning to enhance structured, multimodal reasoning in large models. The proposed Scene Graph Thinking framework (Paper 5) directly addresses a key gap by introducing graph-based rewards that reinforce visually grounded, structured reasoning in MLLMs, aligning perfectly with the RL-for-LLMs criteria. Complementing this, the VAORA approach (Paper 10) bridges physical reasoning and task generalization by designing rewards that align visual outcomes with action sequences, effectively grounding a vision-language model’s reasoning in the physical world. Together, these works signal a move away from purely text-based RL rewards toward richer, multi-modal reward structures that can guide models toward more interpretable and causally sound reasoning.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chenyu Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a fundamental failure mode in self-play RL for LLMs where judges reward plausibility over correctness, and proposes a de-anchoring method to prevent reward hacking.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05904)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haiwen Yi, Xinyuan Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel offline RL framework (Harness MDP) for learning to control the execution harness of frozen LLM agents, using advantage-weighted regression with terminal rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05458)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yijun Zhang, Fan Xu, Jiaxin Ding, Yule Xie, Shiqing Gao, Xin Ding, Haoxiang Zhang, Luoyi Fu, Xinbing Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes IGRPO, a policy optimization framework that uses information gain to allocate rollout budget in tree-structured exploration for multi-turn LLM agents, unifying adaptive exploration with principled policy learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.06223)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Muhammad Zain Amin, Kibele Sebnem Yildirim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SRRL, an on-policy RL framework with self-review steps and cross-episode memory distillation that directly improves LLM reasoning via policy gradients.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05541)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhiwei Yang, Yuanchen Wu, Nan Zhang, Yucong Meng, Ke Yan, Shouhong Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL fine-tuning method with graph-based rewards for structured visual reasoning in MLLMs, directly matching RL-for-LLMs criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05716)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Dingzirui Wang, Xuanliang Zhang, Keyan Xu, Qingfu Zhu, Wanxiang Che

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a failure-driven dynamic data curation framework for agentic post-training that iteratively evolves curation strategies using on-policy trajectory feedback.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.06140)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kaishen Wang, Tong Zheng, Xuehao Cui, Ruibo Chen, Tianyi Xiong, Heng Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MARGO, a reinforcement learning framework that uses mixed-mode (thinking and non-thinking) rollouts for advantage estimation to mitigate thinking-induced hallucination in factuality QA.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05861)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Alexander Rombach, Chantale Lauer, Nijat Mehdiyev

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically investigates reward function design for RL-based process model generation with LLMs, showing that reward composition is a primary determinant of optimization outcomes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.06175)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao, Xin Chen, David Simchi-Levi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RLVR training recipe for LLM negotiation, where the reward is anchored to objective economic outcomes, enabling strategic market exploration and surplus extraction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05863)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Han-Jun Ko, Jr-Jen Chen, Haobo Yuan, Hsin-Ying Lee, Tiancheng Shen, Ming-Hsuan Yang, Yu-Chiang Frank Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel reward design (VAORA) with visual and visual-action alignment rewards to ground VLM reasoning and actions, directly improving RL for LLMs in physical reasoning tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.06522)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuhang Zhou, Kai Zheng, Haoling Li, Dengyun Peng, Can Xu, Jingjing Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TurnOPD, a turn-level budgeting strategy for on-policy distillation that improves efficiency in long-horizon agent training via adaptive rollout-depth and progressive loss normalization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05804)

---

