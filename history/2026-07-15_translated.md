# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
The field of reinforcement learning for large language models is undergoing a profound geometric and algorithmic maturation. A key trend is the move beyond the limitations of PPO-Clip, with **Riemannian Isometric Policy Optimization (RIPO)**identifying and correcting the fundamental exploration collapse caused by Euclidean clipping in the policy space. Concurrently, the community is addressing reward signal quality from multiple angles:**SCOPE-RL**densifies sparse verifiable rewards for math reasoning, while**RLVP**introduces continuous physics-based rewards for code generation, expanding the verifiable reward horizon. Stability remains a central challenge, addressed by**ARMOR**, which uses off-policy anchor samples to mitigate over-optimization in on-policy RL, and**Predictive Divergence Masks**, which refine trust-region updates. For agentic and multi-turn settings, frameworks like**Agentic-DPO**offer a lightweight, offline alternative to online RL, while**STAMP**and**DC-GRPO**provide sophisticated credit assignment mechanisms for search agents and jailbreaking, respectively. The critical analysis of reward suites in**"When the Reward Suite Is Leaky"**serves as a necessary caution, revealing that RL can exploit pre-existing error modes rather than learning new ones, directly informing more robust reward design.

### On-Policy Distillation & Post-Training Paradigms
On-policy self-distillation is a dominant theme, but it is no longer a naive process.**"Diagnosing and Mitigating Thinking Collapse"**reveals a critical failure mode where models lose their native reasoning capacity during distillation, proposing an adaptive dual-perspective objective to preserve it. A modular paradigm shift is emerging with**PUST**, which decouples exploration from alignment by using a lightweight proxy model to generate transferable update signals, effectively separating the roles of exploration and supervision. This is complemented by**EasyOPD**, which provides a unified, easy-to-use framework for various on-policy distillation methods, lowering the barrier for adoption. For code generation,**"The Verifier is the Curriculum"**demonstrates that a deterministic launch verifier can gate the distillation loop, creating an effective curriculum. These works collectively suggest a future where post-training is not a monolithic process but a modular, multi-stage pipeline.

### Latent Reasoning & Interpretability
Latent reasoning is transitioning from a novelty to a deeply studied phenomenon with practical implications.**"Interpreting Latent CoT Reasoning as Dynamical Systems"**provides a rigorous theoretical lens, revealing structured dynamics and stability classes in models like COCONUT. This is complemented by practical diagnostic tools like**SPARK**, which uses hidden-state susceptibility to profile and steer latent reasoning states. The application space is expanding:**"When Reasoning Hurts Legal Drafting"**demonstrates a clear advantage of implicit over explicit CoT for tasks like patent claim generation, while**Structured Thoughts**introduces a hybrid approach that organizes CoT into scratch and summary blocks for improved context pruning. The extension of latent reasoning to non-Transformer backbones is also underway with**Looped State-Space Language Models**, which enable recurrent latent computation in Mamba architectures. A critical trade-off is highlighted in**"Length Penalties Make Chain-of-Thought Less Monitorable,"**warning that compressing reasoning can obscure the model's internal steering, a crucial consideration for safety.

### Agents & Tool Use
Agent research is increasingly focused on scalable, verifiable, and efficient RL training. For computer use agents,**SCALECUA**and**EvoCUA-1.5**provide unified frameworks for scaling online RL with verifiable task synthesis, while**SETA**focuses on generating scalable terminal environments. The challenge of credit assignment in long-horizon agentic tasks is being tackled by**STAMP**, which uses provenance-guided signals for deep search agents. For retrieval-augmented generation,**GRASP**introduces a granularity-aware search policy trained via RL to jointly optimize accuracy, groundedness, and efficiency. Reliability is a key concern, addressed by**Abstention-Aware RL (AWA-RL)**, which trains agents to dynamically decide when to abstain from answering, directly mitigating search-agent hallucinations. The**CycleGRPO**framework unifies region understanding and localization for multimodal agents via a self-evaluating cycle-consistency reward, showcasing the power of model-in-the-loop reward design.

### Alignment & Preference Optimization
Beyond standard RLHF, there is a strong focus on robustness and efficiency in preference optimization.**Metadata-Free Meta-Reweighted DPO**tackles the pervasive problem of noisy preference labels by learning to reweight training samples without requiring any external metadata, a significant practical advance. On the inference side,**Depth-Entropy Guided Sampling**offers a training-free method to harness layer-wise entropy collapse as an intrinsic quality signal, achieving RL-like gains without any training, which could dramatically reduce the cost of reasoning improvement. Finally,**"Read It Back"** extends the concept of reward models to the multimodal domain by using pretrained MLLMs as zero-shot reward models for text-to-image generation, proposing a self-improving closed-loop variant that is both elegant and practical.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 9/10

**作者**: Zhicheng Cai, Xinyuan Guo, Hanlin Wu, Mingxuan Wang, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies the fundamental geometric flaw in PPO-Clip for LLM RL and proposes Riemannian Isometric Policy Optimization (RIPO) to correct exploration collapse, achieving significant gains on competition benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10169)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xiaojian Liu, Han Xu, Jianqiang Xia, Zhixuan Li, Ke Xu, Yiwei Dai, Xinran Chen, Changwo Wu, Yuchen Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SCOPE-RL, a two-stage RLVR framework that densifies sparse verifiable rewards with prefix-decomposed and process-shape rewards, improving accuracy and token efficiency on math reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11506)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Keqin Peng, Chen Li, Yuanxin Ouyang, Yancheng Yuan, Liang Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies and mitigates 'Thinking Collapse' in on-policy self-distillation for LLMs via a novel adaptive dual-perspective objective that preserves native reasoning capacity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10805)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Daocheng Fu, Rong Wu, Yu Yang, Xuemeng Yang, Jianbiao Mei, Licheng Wen, Pinlong Cai, Yong Liu, Botian Shi, Yu Qiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PUST, a novel post-training framework that decouples exploration from alignment by using a lightweight proxy model to generate transferable update signals, directly advancing RL-for-LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11505)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chenyu Zhou, Qiliang Jiang, Shuning Wu, Xu Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an execution-gated self-distillation loop using a deterministic launch verifier, demonstrating strong on-policy distillation gains for code generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09709)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sabari Iyyappan Duraipandian, Shreya Sanjay Boyane, Manju Nagesh, Jerome Francis, Archana Vaidheeswaran, Kevin Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies dynamical systems analysis to interpret latent CoT reasoning in models like CODI and COCONUT, revealing structured dynamics and stability classes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09698)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Bowen Lv, Xiao Liu, Yanyu Ren, Hanyu Lai, Bohao Jing, Hanchen Zhang, Yanxiao Zhao, Shuntian Yao, Jie Tang, Yuxiao Dong

**机构**: Tsinghua University

**💡 亮点 (Highlight)**: Proposes a unified framework for scaling online RL with verifiable rewards for computer use agents, including a verifiable task synthesis pipeline and efficient training techniques.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11185)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yixiong Chen, Alan Yuille

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Agentic-DPO, a lightweight offline policy optimization method that converts expert trajectories into state-level preference supervision for LLM agents, requiring no online rollouts or reward models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10601)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Pengfei Cai, Utkarsh Utkarsh, Alan Edelman, Christopher Vincent Rackauckas, Rafael Gomez-Bombarelli

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces RLVP, a novel RL post-training framework for LLM code generation that uses a hybrid verifier with continuous physics rewards, directly advancing RL-for-LLMs with a new reward design and training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10474)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chuyifei Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a rigorous causal analysis of false positives in RLVR reward suites for code, revealing that RL exploits pre-existing error modes rather than learning new ones, with implications for reward design in RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11022)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zibin Meng, Peng Xie, Kani Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free test-time method that uses layer-wise entropy collapse as an intrinsic quality signal for LLM reasoning, achieving RL-like gains without training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09693)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Runhui Huang, Qihui Zhang, Zhe Liu, Yu Gao, Jie Wu, Hengshuang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free reward function for image-generation RL that uses prompt recovery likelihood from MLLMs, including a self-improving closed-loop variant.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11886)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xin Zhang, Haochen Wang, Yikang Zhou, Jason Li, Robby T. Tan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CycleGRPO, a unified RL framework for MLLMs that jointly optimizes region understanding and localization via a self-evaluating cycle-consistency reward.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11581)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junyoung Park, Namgyu Park, Sechan Lee, Yoon-Chan Jhi, Jihoon Cho, Sangdon Park

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DC-GRPO, a turn-level credit assignment framework for multi-turn RL (GRPO) that significantly improves LLM jailbreaking, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11070)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Dongxu Zhang, Yiding Sun, Zihao Guo, Xiangyang Yang, Kai Tang, Lin Chen, Cheng Tan, Jihua Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces SPARK, a method using length-controlled hidden-state susceptibility to diagnose and steer latent reasoning states in LLMs, directly advancing latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10296)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bryce Little

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reveals a compression-monitorability trade-off in length-penalized RL for CoT, showing that shorter reasoning hides steering influences, which is directly relevant to RL for LLMs and latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09786)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mingyuan Wu, Jingcheng Yang, Shengyi Qian, Xudong Wang, Jize Jiang, Qifan Wang, Aashu Singh, Khoi Pham, Fei Liu, Zhaolun Su, Zhuokai Zhao, Klara Nahrstedt, Jianyu Wang, Hanchao Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-turn RL framework (GRPO-based) where the model's own self-verification provides a learning signal for multimodal reasoning, directly improving RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10966)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ke Xu, Han Xu, Xinran Chen, Yuqian Wang, Zhixuan Li, Xiaojian Liu, Changwo Wu, Jianqiang Xia, Yuchen Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes STAMP, a provenance-guided credit assignment method for RL-based deep search agents that uses a reference-based verifier and sign-preserving advantage modulation to improve step-level credit, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11172)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kexin Huang, Junkang Wu, Jinda Lu, Shuo Yang, Chiyu Ma, Jiancan Wu, Xiang Wang, Xiangnan He, Guoyin Wang, Jingren Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ARMOR, a framework using off-policy anchor samples and mixed optimization to stabilize on-policy RL for LLMs by mitigating over-optimization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10481)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jie Sun, Mao Zheng, Mingyang Song, Qiyong Zhong, Gengsheng Li, Zhepei Hong, Chang Wu, Pengfei Liu, Junfeng Fang, Xiang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces EasyOPD, a unified framework for on-policy distillation of LLMs that separates supervision logic from execution, enabling cross-tokenizer, self-distillation, and step-wise OPD methods.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.11012)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhenxuan Yu, Takeshi Kojima, Yutaka Matsuo, Yusuke Iwasawa

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes looped state-space (Mamba) architectures for recurrent latent computation, extending latent reasoning to non-Transformer backbones with adaptive exit-state selection.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10110)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hua Qu, Yifan Li, Xiaodong Yuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a bilevel optimization framework for DPO that learns to reweight noisy preference data without metadata, directly improving LLM alignment under label noise.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09796)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mianqiu Huang, Taofeng Xue, Chong Peng, Jinrui Ding, Sicheng Fan, Jiale Hong, Yufei Gao, Xiaocheng Zhang, Linsen Guo, Xin Yang, Dengchang Zhao, Yuchen Xie, Peng Pei, Xunliang Xie, Xipeng Qiu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a practical online RL framework (STEPO, DTAC) for multi-turn computer-use agents, directly advancing RL-for-LLMs with verifiable rewards and scalable training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.09773)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qijia Shen, Zhiqi Huang, Vamsidhar Kamanuru, Aznaur Aliev, Jay Rainton, Ahmed Awelkair, Zhichen Zeng, Jiajun Li, Shi Dong, Yueming Yuan, Boyuan Ma, Qizheng Zhang, Jiwei Fu, Yuzhen Mao, Wendong Fan, Ping Nie, Philip Torr, Bernard Ghanem, Changran Hu, Jonathan Lingjie Li, Urmish Thakker, Guohao Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a scalable framework for generating verifiable terminal environments for RL training of LLM agents, demonstrating gains with GRPO on a new benchmark.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10891)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiangxin Zhou, Jiarui Yao, Penghui Qi, Bowen Ping, Jiaqi Tang, Haonan Wang, Tianyu Pang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a predictive divergence mask for LLM RL that improves trust-region updates by aligning the direction criterion with the divergence used for the proximity criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10848)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Varun Gandhi, Jaewook Lee, Shantanu Todmal, Franck Dernoncourt, Ryan Rossi, Zichao Wang, Andrew Lan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GRASP, an RL framework for training LLM agents to adaptively coordinate retrieval tools via a reward that jointly accounts for accuracy, grounded reading, and efficiency, directly matching RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10463)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zain Sarwar, Supriyo Chakraborty, Berkcan Kapusuzoglu, Chia-Hsuan Lee, Anirban Das, Stephen Rawls, Kartik Balasubramaniam, Sambit Sahu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Structured Thoughts, a latent reasoning framework that organizes CoT into alternating scratch and summary blocks, enabling context pruning and memory savings while improving reasoning accuracy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10386)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Fengji Zhang, Tianyu Fan, Yuxiang Zheng, Xinyao Niu, Chengen Huang, Jacky Keung, Bei Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Abstention-Aware RL (AWA-RL) with a dynamically shaped abstention reward and on-policy training to mitigate search-agent hallucinations, directly improving LLM reliability via RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10738)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lekang Jiang, Wenjun Sun, Stephan Goetz

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that implicit (latent) CoT outperforms explicit CoT for legal drafting, directly contributing to latent reasoning methods.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.10480)

---

