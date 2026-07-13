# 💡 今日研究速览 (Daily Summary)

### SFT & Distillation
The field is seeing a significant shift towards **on-policy distillation**as a core technique for both efficiency and capability transfer. The introduction of Multi-Teacher On-Policy Distillation (MOPD) with a routed reverse-KL objective represents a principled advance, moving beyond static, offline knowledge transfer. This is reinforced by the MOSAIC framework, which applies dual-teacher on-policy distillation to the architectural search space for vision-language models. Together, these works signal a maturation of distillation methods, where the focus is now on dynamic, student-aware training regimes that maximize the utility of multiple high-capacity teachers.

### RL for LLMs & Reasoning
Reinforcement Learning continues to be the dominant paradigm for imbuing models with advanced reasoning, with three distinct innovations emerging today. First, the concept of**token-level and latent reasoning**is being refined for efficiency, as seen in HALO's hybrid adaptive latent refinement and the Hybrid Median-length Policy Optimization (HMPO) objective, which aims to make reasoning chains more token-efficient. Second, the critical problem of**reward hacking**is being systematically investigated in multimodal contexts, with the NRFR metric providing a new tool for robustness analysis. Third,**process reward modeling**is evolving beyond simple step-level scoring; KV-PRM introduces a highly efficient method that reuses KV-cache from the generation process, enabling practical multi-agent test-time scaling. This trio of advances—efficiency, robustness, and scalable reward modeling—points to a more mature and practical application of RL to LLMs.

### Agents & Multimodal
A key trend is the integration of**RL with hindsight and relabeling** to dramatically improve sample efficiency in interactive, agentic settings. Learning from Hindsight (LfH) directly addresses the sparse reward problem in Vision-Language-Action (VLA) models by leveraging failed rollouts, turning them into valuable training data. This technique, combined with the advances in efficient reward modeling (KV-PRM) and adaptive reasoning (HALO), suggests a future where agents can learn and adapt with far fewer environment interactions, a crucial step towards real-world deployment.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Foundation Model Team

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Multi-Teacher On-Policy Distillation (MOPD) with a routed reverse-KL objective and Hybrid Median-length Policy Optimization (HMPO) for token-efficient reasoning, directly advancing on-policy distillation and RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09375)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuncheng Yang, Feiyang Ye, Shixian Luo, Yinna Zhu, Lianlei Shan, Wangcai Zhao, Kuo Zhang, Yan Chen, Yong Wu, Yan Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dual-teacher on-policy distillation method for efficient VLM architecture search, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09029)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jiayu Yao, Yiwei Wang, Anmeng Zhang, Zhe Sun, Songsong Wang, Lingrui Mei, Yuyao Ge, Shenghua Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically studies reward hacking in multimodal LLM RL, introducing a new metric (NRFR) and analyzing how reward design, scaling, and algorithms affect robustness.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09492)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Peng Kuang, Haibo Jin, Xiaoyu Han, Yanli Wang, Xiaopeng Yuan, Ye Yu, Kaidi Xu, Haohan Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces KV-PRM, a novel process reward model that leverages KV-cache transfer for efficient scoring in multi-agent test-time scaling, directly advancing RL-for-LLMs with a new reward modeling method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09153)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Micah Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HALO, a hybrid adaptive latent refinement method that selectively applies second-stage latent reasoning to tokens, improving efficiency and accuracy over fixed refinement baselines.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08775)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Iris Xu, Sunshine Jiang, John Marangola, Nitish Dashora, Richard Li, Thomas Liu, Zexue He, Yuheng Zhi, Alex Pentland, Pulkit Agrawal, Zhang-Wei Hong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Learning from Hindsight (LfH), a novel RL method for VLA models that uses hindsight relabeling of instructions and rewards from failed rollouts to improve sample efficiency, directly contributing to RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09042)

---

