# 💡 今日研究速览 (Daily Summary)

### RL for LLMs & On-Policy Distillation

A dominant theme today is the convergence of reinforcement learning (RL) and on-policy distillation to create self-improving systems. Instead of merely imitating static expert data, frameworks like EvoReason, SAF-OPD, and Adaptive FastOPD leverage the model's own rollouts and advantage signals to iteratively refine its policy. This paradigm is being extended to address fundamental RL failure modes: ThinkReset tackles context overflow in long-horizon tasks by learning reusable intermediate interfaces, while CaRL introduces capability-aligned reward shaping to train models to abort futile reasoning paths. The field is also moving towards more nuanced credit assignment, as seen in PRISM, which decomposes policy optimization into separate positive and negative policies to handle conflicting multi-reward objectives, and in the turn-level agentic RL framework for scientific discovery, which uses verifier-based signals to guide exploration in complex environments.

### On-Policy Distillation for Agents & Reasoning

A significant cluster of papers focuses on making on-policy distillation more efficient and robust for agentic and reasoning tasks. Innovations like DASH-OPD and Adaptive FastOPD introduce dynamic mechanisms—such as discrepancy-aware switching and progress-aware rollout horizon expansion—to optimize the training signal and reduce computational waste. The approach is being applied across diverse domains: from distilling defensive policies into lightweight RL agents for cyber operations, to self-evolving search agents that convert on-policy failures into reusable skills, and to GUI agents where structured action distillation (MAGA) reallocates training signal to erroneous tokens. The theoretical underpinnings are also being examined, with new work (OVI) showing that interactive on-policy imitation can relax representational demands, requiring only expert-value realizability rather than full policy realizability.

### Latent Reasoning & Efficiency

Another major direction is the pursuit of efficient and explicit latent reasoning. LatentRM proposes a novel reward model that learns latent reasoning traces end-to-end via on-policy optimization, potentially offering a more scalable alternative to outcome-based rewards. On the efficiency front, BLADE introduces a dynamic early-exit framework with multi-granular checkpoints to reduce token generation during reasoning while preserving accuracy. The theme of adaptive reasoning is also central to Translation with Thought, which uses a difficulty-adaptive RL framework with a hybrid reward to jointly optimize for translation quality and reasoning efficiency. These works collectively suggest a move towards more flexible, compute-aware reasoning processes that can dynamically adjust their depth based on task complexity.

### Security, Safety, & Alignment

The RL-for-LLMs toolkit is being applied to novel alignment and security challenges. TextCloak introduces an RL-driven framework (GRPO-UE) to generate "unlearnable" text, effectively poisoning data to prevent unauthorized fine-tuning—a proactive approach to data protection. In a different vein, preference optimization is being used to shape the delicate balance between competing objectives in high-stakes domains, such as counseling, where a framework was developed to trade off goal persistence against relational attunement. These applications highlight the growing maturity of RL as a general-purpose tool for behavior modification, extending beyond standard reasoning benchmarks to address complex, real-world constraints and safety considerations.

### Multimodal & Specialized Applications

The principles of on-policy optimization are also being translated to other modalities and specialized tasks. In visual generation, a verifier-gated on-policy distillation loop is used to train a prompter, creating a scalable self-improvement loop for text-conditioned generation. For embodied AI, CLIFT presents a non-invasive closed-loop fine-tuning method that converts deployment-time reward feedback into API-compatible supervised data, enabling policy improvement for humanoid robots without direct weight access. Finally, TELLER applies iterative on-policy preference optimization with error-refreshed data to the specialized task of table entity linking, demonstrating the broad applicability of these techniques across different data modalities and problem structures.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhuang Zhuang, Zhipeng Wei, Rongfeng Guo, Shijie Li, Peng Zhao, Jie Chen, Fei Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving latent reasoning framework with primitive-guided on-policy distillation, directly addressing latent reasoning and on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29010)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Sanwoo Lee, Clive Bai, Hsiu-Yuan Huang, Kun Liang, Weijie Liu, Yunfang Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LatentRM, a reward model that learns latent reasoning traces end-to-end via on-policy optimization, directly advancing RL-for-LLMs and latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29185)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yifan Ding, Xincheng Wei, Yoshua Y. Li, Ziheng Li, Yuquan Lu, Siyu Zhang, Dongsheng Ma, Rongxiang Weng, Xunliang Cai, Yun Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a stable advantage fusion framework for combining RLVR and on-policy distillation, directly addressing the target topic of on-policy distillation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29209)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ruiming Liang, Yi Zhong, Yizhen Yuan, Yinan Zheng, Tianyi Tan, Tianyue Wang, Haiyun Guo, Jinqiao Wang, Xianyuan Zhan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces PRISM, a multi-reward RL framework that decomposes policy optimization into standalone positive and negative policies, enabling controllable composition and outperforming existing multi-reward RL baselines for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29246)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Fei Ding, Yongkang Zhang, Runhao Liu, Yuhao Liao, Zijian Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ThinkReset, a method that constructs reusable intermediate interfaces to address context overflow in long-horizon reasoning, directly tackling a key failure mode of outcome-reward RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28642)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zilong Chen, Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes verifier-gated on-policy distillation for training a prompter, directly improving text-conditioned visual generation via a scalable self-improvement loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29679)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yucheng Xu, Keyi Zhang, Yuyang Yu, Min Zhang, Shiyuan Meng, Pei Chu, Zhongying Tu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a scalable framework for turn-level agentic RL in scientific discovery with verifier-based credit assignment, directly contributing to RL-for-LLMs with a new training signal and environment design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28990)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Luca Viano, Antoine Moulin, Audrey Huang, Volkan Cevher, Philip Amortila, Dylan J. Foster

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces OVI, an interactive on-policy imitation learning algorithm that relaxes representational demands by requiring only expert-value realizability, directly relevant to on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29617)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chengshuai Zhao, Pingchuan Ma, Dawei Li, Bohan Jiang, Zhiyuan Yu, Zhen Tan, Huan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an RL-driven framework (GRPO-UE) that generates unlearnable text to protect data from unauthorized LLM fine-tuning, directly contributing a new reward design and RL training loop for LLM behavior modification.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28862)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Siran Peng, Cuiyu Yang, Tianyu Fu, Tianshuo Zhang, Haoyuan Zhang, Weisong Zhao, Anyang Su, Minghui Wu, Huiying Li, Xiangyu Zhu, Chenxu Zhao, Zhen Lei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-supervised, on-policy skill optimization loop that uses LLM-judge comparisons of self-generated probes to iteratively improve agent skills without ground-truth labels.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28777)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Weiying Chen, Junlong Shen, Zhexuan Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a preference-optimization framework with on-policy negatives to trade goal persistence and relational attunement in counseling, directly advancing RL-for-LLMs with a novel reward design and failure-profile analysis.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28814)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yan Song, Xidong Feng, Bo Liu, Xinyu Cui, Haotian Fu, Zichen Liu, Mengyue Yang, Cheng Deng, Jian Zhao, Jun Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Stateful Knowledge Learning (SKL) with self-distillation and RL variants, directly targeting on-policy distillation and RL for LLM agents to learn state-grounded predictive knowledge.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28638)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuxin Chen, Hari Srikanth, Nathan Jew, Menglin Wu, Pengcheng Wang, Junli Ren, Masayoshi Tomizuka, Peng Xu, Jinyu Xie, Thomas Tian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a closed-loop iterative fine-tuning method that converts deployment-time reward feedback into API-compatible supervised data, enabling on-policy policy improvement for humanoid manipulation without weight access.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29172)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai, Haoyu Wu, Minghui Wu, Chenxu Zhao, Ante Wang, Guannan He, Changwei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving skill memory loop where on-policy search failures are distilled into reusable skills that shape future training, directly advancing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29468)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hang Yan, Zhangxuan GU, Beitong Zhou, Jiaxuan Chen, Runze Li, Yusong Hu, Shuheng Shen, Changhua Meng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a structured action distillation method for on-policy distillation of GUI agents, reallocating training signal to focus on erroneous action tokens, directly advancing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29320)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yixin Peng, Kehao Li, Stefan Decker

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces iterative on-policy preference optimization with error-refreshed data and length-normalized regularized preference optimization for table entity linking, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28680)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qian Tan, Huaifei Liang, Xuanyu Zhu, Lei Jiang, Yuqiang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a progress-aware rollout horizon expansion strategy for on-policy distillation, directly improving training efficiency and performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29494)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Konur Tholl, Fran\c{c}ois Rivest, Mariam El Mezouar, Adrian Taylor, Ranwa Al Mallah

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an online policy distillation framework that transfers an LLM teacher's defensive policy into a lightweight RL agent, directly addressing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28826)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Keshu Fu, Keqin Peng, Jun Bai, Shuhan Qin, Chen Li, Junzhu Liang, Yefei Chen, Jiaqi Li, Yuanxin Ouyang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a dynamic early-exit framework for LLM reasoning that uses multi-granular checkpoints and learned probe layers to reduce token generation while preserving accuracy, directly addressing latent reasoning efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28966)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a difficulty-adaptive RL framework with a hybrid reward that jointly optimizes translation quality and reasoning efficiency, directly advancing RL-for-LLMs and latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29287)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuchen Xia, Qianguo Sun, Chao Song, Junlong Wu, Yiyan Qi, Yunjian Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a discrepancy-aware switching mechanism with hysteresis for on-policy distillation, directly addressing the target topic of on-policy distillation for LLM agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29078)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinyan Guan, Jiali Zeng, Chunlei Xin, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun, Fandong Meng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CaRL, a capability-aligned RL method with reward shaping and hindsight refusal augmentation to train LLMs to abort futile reasoning, directly improving reasoning behavior via RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29211)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhuang Zhuang, Shanshan Feng, Hangwei Qian, Mingqi Yang, Heng Qi, Yanming Shen, Baocai Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified SFT+RL framework for LLM-based POI recommendation with novel advantage weighting mechanisms (epistemic uncertainty and reward normalization) that directly improve RL-based reasoning and exploration.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28997)

---

