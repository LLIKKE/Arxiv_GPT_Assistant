# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
The field is experiencing a significant methodological maturation, with multiple papers addressing fundamental bottlenecks in reward design and optimization stability. The introduction of Surrogate Latent Policy Optimization (SLPO) provides a principled RL method for autoregressive latent reasoners, enabling outcome-reward RL and test-time scaling in a previously challenging regime. Concurrently, the Thinking Checklist Reward (TCR) framework tackles the critical issue of process-oriented supervision by using sample-specific checklists and an EMA residual to isolate reasoning-level signals beyond simple outcome rewards, directly improving preference alignment. A crucial methodological advance comes from the analysis of binary-reward Evolutionary Strategies, which identifies a failure mode in z-score normalization and provides a closed-form analysis of population-size requirements, offering practical guidelines for stable training. Furthermore, the application of RL with verifiable rewards (DAPO) to train LLMs for selective evidence adoption from contaminated retrieval results demonstrates how RL can directly shape reasoning behavior in realistic, noisy settings.

### On-Policy Distillation and Agent Training
A clear trend is the pursuit of cost-effective alternatives to standard on-policy distillation while maintaining its performance benefits. The Multi-teacher On-Policy Distillation (MOPD) framework consolidates multiple specialist models into a single generalist LLM, directly addressing capability integration. The REGEN method offers a compelling alternative by recycling replay memory from teacher RL training for offline distillation, matching on-policy performance at a lower computational cost. The Prefix-GRPO framework decomposes teacher trajectories into replayed prefixes and online continuations for small-model agent distillation, achieving on-policy quality without full online generation. On the application side, selective on-policy distillation (SOPD-SocialNav) for vision-language social navigation uses entropy-based token selection to efficiently transfer knowledge from large to small models, while PyroDash proposes a cost-aware SLM-LLM collaborative inference framework using token-level control tokens and GRPO-based alignment, blurring the line between distillation and collaborative inference.

### Reasoning and Latent Computation
Research into reasoning mechanisms is advancing along two parallel tracks: explicit chain-of-thought and implicit latent reasoning. The direct evaluation of the CoTFormer architecture formalizes Chain-of-Thought as recurrent latent computation, providing a concrete architectural foundation for this paradigm. The EvoThink framework introduces a novel RL-based method that reduces overthinking in large reasoning models through self-pruning training and "Aha-Moment" preference optimization, directly improving reasoning efficiency. The "Notes to Self" framework proposes that LLMs can extract experiential abstractions from their own solution traces and use them via RL with augmented prompts, creating a self-improving reasoning loop. The Trace environment introduces a taxonomy-guided benchmark for multidomain visual reasoning with verifiable rewards, enabling RLVR for vision-language models and demonstrating transfer improvements, expanding reasoning research into the multimodal domain.

### Specialized Applications and Methodological Tools
Several papers demonstrate the power of RL-based methods for highly specific domains. The FormulaSPIN framework applies self-play fine-tuning with execution feedback to the niche but practically important task of spreadsheet formula generation, showing how on-policy improvement can be adapted for structured output domains. The Solar Open 2 technical report contributes the MOPD framework for consolidating specialist models, a practical methodology for building more capable generalist systems. These works collectively show that the core RL-for-LLMs techniques are being systematically adapted and optimized for diverse, real-world applications, from code generation to social navigation.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Runyang You, Zhiyuan Liu, Yongqi Li, Wenjie Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Surrogate Latent Policy Optimization (SLPO), a novel RL method for autoregressive latent reasoners that enables outcome-reward RL and test-time scaling in latent reasoning, directly advancing both RL-for-LLMs and latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19691)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Beining Wang, Weihang Su, Hongtao Tian, Hao Kong, Tao Yang, Ting Yao, Qingyi Pan, Yueyue Wu, Qingyao Ai, Min Zhang, Yiqun Liu

**机构**: WeChat Search, Tencent

**💡 亮点 (Highlight)**: Proposes DynamicRubric, a co-evolution framework for evaluator and policy that directly addresses the bottleneck of collapsed score gaps in RL for LLMs, with strong theoretical motivation and practical deployment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.20083)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Cy Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-play fine-tuning framework (SPIN variant) with execution feedback for iterative on-policy improvement in formula generation, directly relevant to on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19354)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sungrae Park (University of Seoul), Sanghoon Kim (University of Seoul), Gyoungjin Gim (University of Seoul), Jungho Cho (University of Seoul), Hyunwoong Ko (University of Seoul), Minbyul Jeong (University of Seoul), Minjeong Kim (University of Seoul), Keunwoo Choi (University of Seoul), Chaehun Shin (University of Seoul), Chanwoong Yoon (University of Seoul), Dongjun Kim (University of Seoul), Eunwon Kim (University of Seoul), Gyungin Shin (University of Seoul), Hyeonju Lee (University of Seoul), Hyungkyu Kang (University of Seoul), Inseo Song (University of Seoul), Jisu Bae (University of Seoul), Jiyoon Han (University of Seoul), Jiyun Lee (University of Seoul), Joonkee Kim (University of Seoul), Junyeop Lee (University of Seoul), Mikyoung Cha (University of Seoul), Sangwon Yu (University of Seoul), Sehwan Joo (University of Seoul), Seokyoon Kang (University of Seoul), Seonghoon Yang (University of Seoul), Seung Shin (University of Seoul), Seunghyun Lee (University of Seoul), Seungseop Lim (University of Seoul), Seungyoun Shin (University of Seoul), Sukyung Lee (University of Seoul), Taegyeong Eo (University of Seoul), Taehwan Oh (University of Seoul), Taewhoo Lee (University of Seoul), Wonho Song (University of Seoul), Wonjun Oh (University of Seoul), Wonseok Hwang (University of Seoul), Yunsu Kim, Yura Shim, Hwalsuk Lee, Sunghun Kim, Du-Seong Chang, Kyunghyun Cho, Seungju Han, Yejin Choi, Junsuk Choe, Hwaran Lee, Minjeong Ban, Yun Taewon, Hwanjun Song, Jae-Gil Lee, KyungTae Lim, Alice Oh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Multi-teacher On-Policy Distillation (MOPD) to consolidate specialist models into a single LLM, a direct contribution to on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.20062)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yunjie Chen, Xiaoxin Chen, Fang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes REGEN, an offline RL method that recycles replay memory from teacher RL training to distill a generalist LLM, matching on-policy distillation at lower cost.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19450)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chang Liu, Xinyu Li, Artur Dubrawski

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a framework where LLMs extract experiential abstractions from their own solution traces and use them via RL with augmented prompts, directly improving reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.20372)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xubo Liu, Wenya Guo, Ruxue Yan, Xinying Qian, Ying Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Thinking Checklist Reward (TCR), a process-oriented reward for RL-based preference alignment that uses sample-specific checklists and an EMA residual to isolate reasoning-level supervision beyond outcome rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19824)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yanyu Chen, Yue Li, Yongyi Cui, Dongsheng Shi, Lichang Dai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies RL (DAPO) with verifiable rewards to train LLMs for selective evidence adoption from contaminated retrieval, directly improving alignment and reasoning behavior.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.20090)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Md Tanvirul Alam

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a taxonomy-guided environment for multidomain visual reasoning with verifiable rewards, enabling RLVR for vision-language models and showing transfer improvements.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19790)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Aras Kavuncu, Bryan Vullo, Alberto Berni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly evaluates the CoTFormer architecture, which formalizes Chain-of-Thought as recurrent latent computation, a core latent reasoning method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19405)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sung Cho, Gyubin Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a critical failure mode in binary-reward ES for LLM fine-tuning due to z-score normalization, and provides a closed-form analysis of population-size requirements, directly advancing RL-for-LLMs methodology.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19408)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinyu Zhang, Zishuo Wang, Ling Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a selective on-policy distillation method with entropy-based token selection for transferring social navigation knowledge from a large teacher VLM to a lightweight student VLM.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19850)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Niqi Lyu, Pengtao Shi, Wei Qiu, Jianlin Zhong, Sicong Xia, Jianyao Ma, Yicheng Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a cost-aware SLM-LLM collaborative inference framework using token-level control tokens and GRPO-based alignment, directly relevant to RL for LLMs via reward design and on-policy optimization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.20327)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinbang Dai, Zheyu Xin, Huikang Hu, Lin Ren, Rihui Jin, Guohui Xiao, Guilin Qi, Kuicai Dong, Zhaocheng Du, Yuyang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EvoThink with Self-Pruning Training and Aha-Moment Preference Optimization, a new RL-based method that reduces overthinking and improves reasoning in LRMs via on-policy trajectory pruning and preference optimization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19962)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yihan Wang, Zhong Guan, Haoran Sun, Jiale Huang, Likang Wu, Hongke Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Prefix-GRPO, an on-policy RL framework that decomposes teacher trajectories into replayed prefixes and online continuations for small-model agent distillation, directly matching on-policy distillation and RL-for-LLMs criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19395)

---

