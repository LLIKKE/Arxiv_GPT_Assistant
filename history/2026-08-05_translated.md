# 💡 今日研究速览 (Daily Summary)

### RL for LLMs

A dominant theme today is the evolution of RL-based post-training beyond simple outcome rewards, with a strong focus on credit assignment, reward design, and capability retention. Several works tackle the granularity of credit, from **BiCAA**'s bidirectional dense process rewards and**GradCuit**'s credit-assigned gradient flow to**EAGLE-GRPO**'s element-aware decomposition for structured outputs and**CRISP**'s critical-step perception with backward evidence induction. Another key trend is addressing the fragility of on-policy optimization:**Verifier-Induced Support Reshaping**analyzes how RL can harm future trainability, while**Toward Plasticity-Preserving KL Regularization**proposes a correctness-conditioned objective to retain prior skills. The field is also maturing in its treatment of multi-objective and safety-aligned scenarios, with**PRISM**decomposing policies to resolve conflicting rewards and**C-Guard**using a constitution-grid for data-efficient alignment. Finally,**Abstention as an Action**provides a crucial theoretical warning about collapse in error-penalized RL, proposing a structural repair via confidence reporting.

### On-Policy Distillation & Self-Improvement

A significant cluster of papers converges on the idea of using on-policy distillation not just as a regularization term, but as a primary learning signal, particularly to correct errors and recover gradients from sparse rewards.**Distill What the Student Can See**introduces a capacity-aware, Fisher-projected method that adapts teacher feedback to the student's perceptual space, while**Look Ahead Before You Distill**validates teacher guidance by simulating short future trajectories.**Distill Where You Fail**and**HindSearch**both focus on mining failed trajectories to recover learning signals, using adaptive teacher guidance and hindsight critique, respectively. This theme extends to self-improvement loops, where**Self-Improving LLMs via Progressive Experience Evolution**and**Self-Play Meets Skill Evolution**show how agents can generate their own curriculum and distill the resulting experience. The breadth of this trend is underscored by applications in specialized domains, from**SERL-SQL**'s selective hindsight distillation for text-to-SQL to**Native Multilingual CoT**'s cross-distillation for low-resource languages and**MAGA**'s structured action distillation for GUI agents.

### Latent Reasoning & Test-Time Computation

Today's papers reveal a strong push toward making latent reasoning more robust, interpretable, and controllable.**LUT**introduces a utility-aware training objective for latent reasoning, while**GradCuit**offers a test-time alternative by directly optimizing hidden states with credit-assigned gradients. Architecturally,**Recursive Vision Language Models**and**Agentic Graph Token Reasoning**propose novel frameworks for dynamic, step-by-step latent computation. On the practical side,**ThinkReset**addresses long-horizon context overflow by learning to construct reusable intermediate interfaces, and**SeDeM**enables efficient long-context QA through selective decompression of hidden-state memories. A related memory-centric approach,**Learning What to Remember**, uses test-time training to distill long-context knowledge into fast weights, while**TRAM**leverages trajectory-derived auxiliary memory without additional training. This collective work signals a maturation of latent reasoning from a conceptual idea to a suite of practical, trainable, and interpretable techniques.

### Multimodal & Visual Reasoning

Multimodal research is increasingly integrating RL and distillation techniques to address specific failure modes like visual forgetting and token inefficiency.**Remember-R1**directly targets long-context visual forgetting by using process-level rewards to supervise visual evidence usage in reasoning trajectories.**AdaThinkV**introduces an RL-based adaptive reasoning framework with a novel ThinkGain reward to optimize token efficiency in video reasoning.**From Pixels to PCells**demonstrates a verifier-driven GRPO loop for photonic component generation, while**Same Semantics, Different Paths**aligns vision-text compressed representations via on-policy distillation and preference optimization. Finally,**Credit the Right Box**tackles the challenge of providing box-level credit in structured visual perception within a GRPO framework, showing a clear trend toward more fine-grained and RL-driven multimodal post-training.

### Agents & Search-Augmented Reasoning

The agentic research today centers on improving training signals and credit assignment for complex, multi-step tasks.**Scaling Scientific Discovery Environments**introduces a framework for turn-level agentic RL with process-verifiable environments, while**EviSD**uses evidence-conditioned self-distillation to correct GRPO advantages in search-augmented agents.**Cross-Domain Hybrid OPD**mitigates the alignment tax in search agents by combining agentic RL with cross-domain expert distillation.**Progressive Agent Skill Generation**introduces a rollback reward to enable progressive skill acquisition. The focus on search is particularly strong, with**BiCAA**and**HindSearch**both proposing new credit assignment and critique mechanisms for search-augmented RL.**TAPR**and**LEAP** round out this category by applying GRPO-based RL to prompt rewriting and GPU kernel generation, respectively, showcasing the versatility of RL for optimizing agentic and code-related behaviors.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shaohang Wei, Zikun Su, Feifan Song, Wen Luo, Wei Li, Guangyue Peng, Houfeng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies verifier-induced support reshaping in on-policy RLVR, showing how RL can harm future trainability and proposing/analyzing constraints including on-policy distillation, with clear methodological substance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00220)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Longtian Bao, Jianyou Wang, Yang Zhang, Youze Zheng, Ramamohan Paturi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving curriculum with question generation and RL fine-tuning that breaks performance plateaus on competition math, directly advancing RL-for-LLMs with a novel training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01522)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jianan Xie, Xin Sun, Zhongqi Chen, Xing Zheng, Shu Wu, Bowen Song, Liang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an evidence-conditioned self-distillation framework that uses privileged evidence to correct GRPO advantages, directly improving search-augmented agents via on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01359)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jiaxuan Kang, Siyu Chen, Mingda Li, Mingjie Liu, Tianyue Wang, Zhaoyang Wei, Yongheng Zhang, Yanchao Hao, Zheng Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a latent reasoning framework with utility-aware distillation and latent attribution policy optimization, directly advancing latent CoT/reasoning with a new training objective.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00743)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhijian Zhou, Long Li, Xuan Zhang, Zongkai Liu, Yulei Qin, Ke Li, Xing Sun, Xiaoyu Tan, Chao Qu, Yuan Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a categorical critic objective (HL-Gauss) for PPO in RLVR, improving value calibration and advantage estimation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02181)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Leyan Xue, Feng Xiong, Mingjun Ma, Changqing Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Fisher-Projected On-Policy Distillation, a capacity-aware on-policy distillation method that projects teacher corrections onto the student's local visual tangent space, directly improving vision-language model distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01263)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shijie Ren, Xiting Wang, Meng Li, Yujie Guo, Yunhang Yao, Ziheng Peng, Xunlong Wang, Yuetan Chen, Haoyang Zhou, Yunlong Liang, Fandong Meng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified self-improvement framework with explicit experience evolution and on-policy self-distillation, directly advancing on-policy distillation and RL for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02139)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhaoxin Yu, Qi Shen, Hengli Li, Zhaowei Zhang, Song-Chun Zhu, Chi Zhang, Zilong Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel test-time latent reasoning method that directly optimizes hidden states via credit-assigned gradients, improving reasoning accuracy and robustness.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02585)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chishui Chen, Yaoyou Fan, Te Sun, Yi Yang, Chenghao Sun, Delin Mao, Hongbo Qiao, Zuowei Zhang, Junxi Wang, Chenxing Sun, Yangen Hu, Lu Pan, Xuyang Liu, Linfeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FutureBridge-OPD, a novel on-policy distillation method that validates teacher guidance via short future trajectory bridges, directly improving agentic task performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01953)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhuowen Han, Jinwei Xiao, Zhengxi Lu, Renren Jin, Zhiyuan Yao, Yuxin Liu, Hongyan Hao, Yueqing Sun, Yu Yang, Qi GU, Xunliang Cai, Deyi Xiong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RSTG, a selective on-policy distillation method that recovers learning signals from negative RL groups by combining GRPO with adaptive teacher guidance, directly addressing sparse reward and gradient loss in RLVR.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00782)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xinheng Han, Jianfei Wang, Yu Chen, Xiang Wang, Shuai Li, Weixing Li, Feng Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a marginal contribution reward assignment framework for GRPO, providing box-level credit in structured visual perception, a novel reward design for RL-based LLM post-training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01055)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Li Wang, Xiaodong Lu, Xiaohan Wang, Jiajun Chai, Wei Lin, Tianhao Peng, Guojun Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new correctness-conditioned KL regularization objective for RL-based LLM post-training that preserves prior capabilities while improving target-task learning, directly addressing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01743)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ruiming Liang, Yi Zhong, Yizhen Yuan, Yinan Zheng, Tianyi Tan, Tianyue Wang, Haiyun Guo, Jinqiao Wang, Xianyuan Zhan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new multi-reward RL framework (PRISM) that decomposes policy space into standalone positive and negative policies, directly addressing reward conflict and enabling controllable inference-time composition for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29246)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yucheng Xu, Keyi Zhang, Yuyang Yu, Min Zhang, Shiyuan Meng, Pei Chu, Zhongying Tu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a scalable framework for turn-level agentic RL with process-verifiable environments and verifier-filtered trajectory synthesis, directly advancing RL-for-LLMs with a new training signal.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28990)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Omid Nejati Manzari, Guillaume Lajoie, Hassan Rivaz

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a recursive reasoning framework with latent-state refinement and deep supervision, directly advancing latent reasoning architectures for symbolic tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01534)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhuoyi Peng, Yi Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces agentic graph token reasoning, a new latent reasoning paradigm where the model dynamically selects and encodes graph views as tokens during step-by-step reasoning, trained with a preference optimization loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00542)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haowei Liu, Jiamian Wang, Hsin-Tai Wu, Zhiqiang Tao, Yi Fang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a hindsight critique-based on-policy distillation signal for GRPO, directly improving search-augmented RL for LLMs by leveraging failed trajectories.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01597)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuzhou Liu, Xiyang Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a topology-guided preference-mining framework that derives preference supervision from hidden-state geometry, directly advancing RL-for-LLMs via a novel reward design and semi-supervised preference optimization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01014)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Fei Ding, Yongkang Zhang, Runhao Liu, Yuhao Liao, Zijian Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces ThinkReset, a latent-reasoning-adjacent method that constructs reusable intermediate interfaces to address context overflow and premature guessing in long-horizon reasoning, directly optimizing post-reset continuation success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28642)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jingqi Tian, Haoji Zhang, Lin Chen, Hongbo Jin, Haonan Xu, Tianrui Zhu, Xingming Shui, Shilin Ma, Wenjing Yang, Yansong Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an RL-based adaptive reasoning framework (AdaThinkV) with a novel ThinkGain reward and Variance Recovery Policy Optimization, directly improving token-efficient video reasoning via on-policy RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01980)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haosi Mo, Zihao Yan, Ruiqing Zhang, Zhongli Li, Hexuan Deng, Xuebo Liu, Min Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a critical-step perception framework with backward evidence induction and efficiency-aware rewards for RL-based training of deep search agents, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01867)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tao Liu, Tao Feng, Xiangheng Li, Jinwang Song, Yifan Li, Xiaoqing Cheng, Dixuan Zhang, Siquan Li, Lin Lan, Hongying Zan, Kunli Zhang, Chao Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a selective execution-grounded RL framework with teacher-student likelihood gap weighting for localized credit assignment in Text-to-SQL agents, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00485)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yibin Huang, Bin Xu, Hailong Cao, Conghui Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a bidirectional credit assignment framework with dense process rewards for search-augmented agents, directly advancing RL-for-LLMs via a new reward design and training pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01321)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai, Haoyu Wu, Minghui Wu, Chenxu Zhao, Ante Wang, Guannan He, Changwei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving loop where skill memory co-evolves with self-play task generation, directly improving on-policy training trajectories and policy learning for LLM search agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29468)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianyu Liang, Xiangxi Zheng, Yilin Wang, Dongxing Mao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving alignment framework combining on-policy distillation and preference optimization to align vision-text compressed representations with native-text semantics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02109)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xujun Che, Yuchen Yuan, Weida Zhao, Chenyang Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical and empirical analysis of a failure mode in error-penalized RL for LLMs (abstention collapse) and proposes a structural repair via confidence-report training, directly relevant to reward design for RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00301)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zixuan Wang, Xingyu Dang, Rui-Jie Zhu, Zixin Wen, Hengyu Fu, Wenhao Chai, Jason D. Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a test-time training framework that distills long-context teacher knowledge into short-window student fast weights via hidden-state discrepancy, a novel on-policy distillation mechanism for latent reasoning and memory allocation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01672)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Aadarsh Agarwal, Kenaish Al Qubaisi, Dirk Englund

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a verifier as a reward signal for GRPO-based RL training of a multimodal LLM, demonstrating a verifier-driven RL loop for improving visual-to-parametric generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00084)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junhao Shen, Zhanqiu Zhang, Yiwen Guo, Hong Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a reinforcement learning method with a rollback reward for progressive agent skill generation, directly advancing RL-based self-improvement for LLM agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01678)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Maryam Haghifam, Jason Cong, Yizhou Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a selective decompression framework that decouples compact memory storage from decoder conditioning, enabling efficient long-context QA with hidden-state memory blocks and query-conditioned selection.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00311)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Oliver Savolainen, Emanuele Bastianelli, Hosein Azarbonyad

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a task-aware prompt rewriter trained with GRPO and LLM-as-judge rewards, directly contributing to RL-based optimization of LLM behavior.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28657)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sean Gip Lim, William Chandra Tjhi, Hai Leong Chieu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an on-policy cross-distillation algorithm with a translator agentic loop and joint-embedding alignment to improve native multilingual reasoning, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00533)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kang Liu, Zijing Wang, Yongkang Liu, Mengjie Zhao, Xiaocui Yang, Shi Feng, Yifei Zhang, Daling Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free latent memory pathway derived from the model's own reasoning trajectory, directly addressing latent reasoning and on-policy self-improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01922)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wonseok Lee, Jimyeong Kim, Jungmin Ko, Wonjong Rhee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a method to integrate external policy rollouts with on-policy rollouts for diffusion LLM RL, addressing length and reward processing challenges to improve reasoning performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01717)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tankun Li, Zhi Chen, Yaohua Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a multi-turn RL framework with difficulty-conditioned pruning and rank-based rewards for code generation, directly advancing RL-for-LLMs with a new reward design and training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01804)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jingtong Chen, Jiahui Wang, Xue Zhao, ShaoGuo Liu, Minghao Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EAGLE-GRPO, a novel element-aware credit assignment method for GRPO-based RLHF that decomposes rewards over predefined elements with a closed-form solution, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00584)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongzhan Chen, Xiaoyu Liu, Dengming Zhang, Minzhou Huang, Dongliang Xu, Jingcheng Xie, Dongxiang Fang, Bowen Qin, Minsheng Hao, Yaozong Shen, Xiaojun Quan, Mona Zhou, Haosheng Zou, Jeff Chen

**机构**: Tencent (Yuanbao, Hunyuan)

**💡 亮点 (Highlight)**: Proposes a hybrid training framework combining agentic RL with cross-domain expert On-Policy Distillation to mitigate the alignment tax, directly addressing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02101)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jianmin Chen, Jiaqi Tang, Wei Wei, Xiaogang Xu, Jiafei Wu, Zhe Liu, Qianzhou Wang, Yingying Yan, Botong Geng, Yuyang Xia, Lei Zhang, Qifeng Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel RL framework with process-level rewards that directly supervise visual evidence usage in long reasoning trajectories, mitigating visual forgetting in MLLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.01314)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lily Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a constitution-grid data generation instrument and per-cell learnability scoring for data-efficient RL alignment, directly addressing conflicting objectives in safety training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00180)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mehrdad Ghassabi, Hamidreza Baradaran Kashani, Pedram Rostami, Sadra Hakim, Zahra Kazemi, Audrina Ebrahimi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces two novel RLAIF frameworks for preference-based reasoning in a medical LLM, directly targeting RL for LLMs with a new reward/feedback design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.00932)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hang Yan, Zhangxuan GU, Beitong Zhou, Jiaxuan Chen, Runze Li, Yusong Hu, Shuheng Shen, Changhua Meng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a structured action distillation method for on-policy distillation of GUI agents, focusing learning on erroneous action tokens to improve cross-environment policy merging.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.29320)

---

