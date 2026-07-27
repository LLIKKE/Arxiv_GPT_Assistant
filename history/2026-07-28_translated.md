# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
The field of reinforcement learning for LLMs is seeing a pronounced shift toward co-evolutionary and meta-skill training paradigms, moving beyond simple reward maximization. Frameworks like MetaEvolve and Skill Self-Play introduce structured, multi-agent RL loops—one using verifiable code execution rewards to cultivate self-reflection, the other co-evolving proposer and solver agents to bridge structured verification with open-ended exploration. This trend is complemented by a deeper theoretical and practical understanding of RL dynamics: a comprehensive analysis now explains why on-policy RL inherently mitigates task conflicts during model merging, while ESTR tackles the practical bottleneck of asynchronous training by scaling importance ratios with token entropy, achieving a 2.6x speedup over synchronous methods. Efficiency is further advanced by VIGOR, which uses variance-guided rollout allocation to reduce compute by up to 2.3x. The Nanbeige4.2-3B release exemplifies a complete, production-grade RL pipeline that combines mixed-mode RLHF, length-controlled reasoning RL, and agentic RL with outcome/process rewards, demonstrating that compact models can unlock sophisticated agentic capabilities through careful RL recipe design.

### Distillation & Reasoning
On-policy distillation is being re-engineered to overcome the tokenizer barrier and enable more effective reasoning transfer. The Byte-Prefix Marginalization (BPM) method directly addresses the fundamental limitation of cross-tokenizer distillation by preserving teacher probability mass in a shared byte space, allowing full-vocabulary, on-policy training without architectural constraints. In parallel, LeAct introduces a novel paradigm where the student recovers latent reasoning chains from expert actions by optimizing its own probability of generating the action, effectively learning from self-generated CoTs. These approaches signal a maturation of distillation techniques, moving from simple imitation to structured, student-aware learning processes that can bridge architectural and vocabulary gaps.

### Latent Reasoning
A new frontier is emerging in latent reasoning, where models reason in compressed, non-linguistic spaces. J-CoT introduces J-space—a vocabulary-indexed coefficient space—as an intermediate interface for recurrent reasoning, avoiding both full hidden-state recurrence and explicit natural language chains. This approach challenges the dominant CoT paradigm by suggesting that the most efficient reasoning may occur in a structured latent space, potentially offering a path to more compute-efficient and scalable inference without the verbose token overhead of explicit chain-of-thought.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shujin Wu, Cheng Qian, Xiusi Chen, Heng Ji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces MetaEvolve, a framework using RL with verifiable rewards to train LLMs on self-evolution meta-skills (self-reflection, iterative refinement) from code execution feedback, showing strong transfer to out-of-distribution tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.21971v1)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shujin Wu, Cheng Qian, Xiusi Chen, Heng Ji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MetaEvolve, a framework using RL with verifiable rewards from code execution to cultivate self-evolution meta-skills in LLMs, directly advancing RL-for-LLMs with a new training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.21971)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Hao Wang, Kun Yuan, Wenlin Zhong, Minglei Zhang, Han Xiao, Ming Sun, Honggang Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Byte-Prefix Marginalization (BPM), a novel method for cross-tokenizer on-policy distillation that preserves teacher probability mass in a shared byte space, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22334v1)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Junde Wu, Jiayuan Zhu, Fengling Liu, Minhao Hu, Jiazhen Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces J-CoT, a novel latent reasoning framework that uses vocabulary-indexed coefficients (J-space) as an intermediate interface, enabling recurrent reasoning without full hidden-state recurrence or explicit natural language.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.21981v1)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Nanbeige Lab,  :, Chen Yang, Chengrui Huang, Fufeng Lan, Hanhui Chen, Hao Zhou, Huatong Song, Jiaqi Cao, Jiaying Zhu, Jinlin Niu, Kai Wang, Lisheng Huang, Qiliang Liang, Ran Le, Ruixiang Feng, Shuang Sun, Tao Gu, Tao Zhang, Tianyu Luo, Yang Song, Yun Xing, Yuntao Wen, Ziyao Xu, Zongchao Chen, Zongqiang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a comprehensive RL pipeline for LLMs including mixed-mode RLHF, length-controlled reasoning RL, and agentic RL with outcome/process rewards, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22083v1)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Junde Wu, Jiayuan Zhu, Fengling Liu, Minhao Hu, Jiazhen Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces J-CoT, a novel latent reasoning framework that uses vocabulary-indexed coefficients (J-space) as an intermediate interface, avoiding full hidden-state recurrence and explicit natural language chains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.21981)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Hao Wang, Kun Yuan, Wenlin Zhong, Minglei Zhang, Han Xiao, Ming Sun, Honggang Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Byte-Prefix Marginalization (BPM) to enable full-vocabulary on-policy distillation across different tokenizers, achieving strong gains on math and programming benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22334)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ziran Yang, Chengshuai Shi, Raj Ghugare, Benjamin Eysenbach, Karthik Narasimhan, Chi Jin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LeAct, a novel on-policy distillation framework that recovers latent reasoning chains from expert actions by optimizing the student's own probability of recovering the action, directly improving reasoning via self-generated CoTs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.21856)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Guanqun Zhao, Zijun Xie, Binbin Zheng, Enlei Gong, Jiafeng Lu, Yehan Yang, Aoqi Hu, Zeyu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Entropy-Scaled Trust Region (ESTR) for asynchronous RL in LLM post-training, addressing off-policy instability by scaling importance ratios with token entropy, achieving 2.6x speedup over synchronous GRPO.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22186v1)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, Shijie Zhou, Ziyi Yang, Gangwei Jiang, Mengyu Zhou, Yu Cheng, Xiaoxi Jiang, Guanjun Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Skill Self-Play, a co-evolutionary RL framework with a proposer, solver, and skill controller that bridges structured verification and open-ended exploration for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22529)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Heyang Jiang, Henry Liu, Baharan Mirzasoleiman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes VIGOR, a variance-guided online rollout allocation method for RLVR that dynamically allocates rollout budget to high-variance examples, achieving up to 2.3x fewer rollouts on math tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22002v1)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zixuan Ren, Jinliang Lu, Junhong Wu, Yang Zhao, Dai Dai, Hua Wu, Haifeng Wang, Chengqing Zong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a systematic analysis and theoretical explanation of why RL training (on-policy data, objective, joint optimization) reduces task conflicts in LLM merging, directly relevant to RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22039)

---

