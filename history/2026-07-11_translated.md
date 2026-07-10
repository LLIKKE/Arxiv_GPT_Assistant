# 💡 今日研究速览 (Daily Summary)

### RL for LLMs and Verifiable Rewards
A significant cluster of papers today advances reinforcement learning for LLMs, particularly using verifiable rewards (RLVR/GRPO). The field is moving beyond simple reward models toward more sophisticated credit assignment and curriculum design. **TACO**addresses a critical flaw in RL training by calibrating credit for low-probability "tail tokens" that often get incorrectly reinforced, directly improving policy gradient stability. Meanwhile,**Compete Then Collaborate**introduces a novel multi-agent framework where frontier models compete to generate verifiable coding curricula, then collaborate to train a student via GRPO, showing that structured competition can produce more effective training signals than single-teacher distillation. The application of GRPO also extends to speech recognition in**When Synthetic Speech Is All You Have**, demonstrating the generality of verifiable-reward RL beyond text domains. These works collectively indicate a maturation of RL-based post-training, focusing on signal quality, curriculum design, and cross-modal transfer.

### On-Policy Self-Distillation and Iterative Self-Improvement
A powerful trend is the use of on-policy self-distillation to bootstrap capabilities without human annotation.**DeepSearch-World**formalizes this for web agents, iteratively generating, filtering, and fine-tuning on-policy trajectories in a verifiable environment—a direct application of the on-policy distillation paradigm. Similarly,**OPSD-V**adapts this to autoregressive video generation, using real video context to provide dense supervision during few-step rollouts.**Hallucination Self-Play**extends the concept to safety, combining RLAIF with rule-based RL to evolve a generator that produces better adversarial examples for training a hallucination detector.**Selective Left-Shift**ties these ideas together by using test-time compute and difficulty-based curation to generate high-quality on-policy training data for low-resource code generation, followed by RLVR fine-tuning. The common thread is a closed loop where the model's own rollouts, filtered by verifiable signals, become the primary source of training data.

### Latent Reasoning Architectures and Computation Scaling
Several papers propose fundamental shifts in how LLMs perform reasoning, moving computation into a latent space.**Hidden Decoding**introduces a method to scale computation with sequence length via stream-factorized attention, enabling fixed-backbone scaling that avoids the quadratic costs of standard attention.**Latent Memory Palace**reformulates control policies as autoregressive variational inference, creating a latent reasoning architecture trained with RL.**A First-Principles Theory of Slow Thinking**provides a theoretical foundation for these approaches, deriving latent reasoning architectures and training objectives from the concept of "active lifting." These works suggest a convergence toward architectures where reasoning occurs in a compressed, latent state space, decoupling computational depth from token generation length. The**Switch-Reasoner**paper complements this by using GRPO to learn when to invoke different reasoning modes in MLLMs, adding a meta-cognitive layer that balances accuracy and efficiency.

### Efficient Safety Alignment via Latent Representations
A notable breakthrough in safety alignment is presented by**Latent Personality Alignment (LPA)** , which operates on latent personality traits rather than explicit behaviors or responses. This approach achieves strong adversarial robustness with minimal data and compute by modifying the model's underlying "personality" in a compressed representation space. This contrasts with traditional adversarial training that requires extensive example generation and retraining. LPA represents a shift from surface-level behavioral modification to deeper, more efficient architectural interventions for safety, potentially offering a more scalable and generalizable path to alignment.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xiuyi Lou, Zicheng Xu, Yu-Neng Chuang, Hoang Anh Duy Le, Zhaozhuo Xu, Guanchu Wang, Vladimir Braverman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TACO, a novel credit assignment method for RL-based LLM training that mitigates positive contamination from low-probability tail tokens, directly improving RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.07976)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Aiwei Liu, Cheng Shi, Chuhan Wu, Ci Lei, Di Lu, Donald He, Fan Zhang, Fanhao Kong, Feifei Zhang, Guan Wang, Haicheng Wang, Haoyu Liu, Houjin Yu, Jiachen Ding, Jiayi Feng, Jie Zhou, Jijun Chi, Jindi Shi, Jing Lei, Junjie Zhang, Laiyi Li, Le Tian, Linhao Zhang, Miao Fan, Sijun Zhang, Wei Jia, Weiwei Shi, Wenhan Li, Wentao Zhao, Wenteng Liang, Xiao Zhou, Xiaojin Zhou, Xihuai Wang, Xinyu Gao, Xuanliang Wang, Xuyang Ao, Yang Yu, Yangxiu You, Yinuo Zhao, Yufei Kuang, Yufei Wang, Yuan Liu, Yuan Liu, Yuwen Chen, Zhencong Tian, Zhongyin Zhao, Zilin Yu, Zitao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Hidden Decoding, a sequence-length scaling method for latent computation in LLMs via stream-factorized attention, enabling fixed-backbone scaling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08186)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Mohamed Amine Merzouk, Nolan Smyth, Damiano Fornasiere, Linh Le, David Williams-King, Adam Oberman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Latent Personality Alignment (LPA), a novel and highly efficient adversarial training method for safety alignment that operates on latent personality traits, achieving strong robustness with minimal data and compute.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.07918)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chuning Zhu, Eva Xu, Jose Barreiros, Krishnan Srinivasan, Paarth Shah, Abhishek Gupta

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent reasoning architecture for control policies via autoregressive variational inference and RL, directly advancing latent reasoning with a new method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08724)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hongkang Yang, Zhi-Qin John Xu, Feiyu Xiong, Weinan E

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a first-principles theory of slow thinking/active perception for LLMs, deriving latent reasoning architectures and training objectives from active lifting.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08196)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Miseong Shawn Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a compete-then-collaborate framework using execution-based verification to build a curriculum for RLVR (GRPO) training of a coding student, directly advancing RL-for-LLMs with verifiable rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08255)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinyu Geng, Xuanhua He, Sixiang Chen, Yanjing Xiao, Fan Zhang, Shijue Huang, Haitao Mi, Zhenwen Liang, Tianqing Fang, Yi R. Fung

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-distillation framework (DeepSearch-Evolve) for web agents that iteratively generates, filters, and fine-tunes on-policy trajectories in a verifiable environment, directly matching on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.07820)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yiyang Fang, Pei Fu, Jinjie Li, Jian Liang, Wenke Huang, Ruijie Luo, Shaojie Zhang, Jian Luan, Yi R. Fung, Mang Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a GRPO-based framework for MLLMs that learns to adaptively select reasoning modes, balancing accuracy and efficiency via dual-level regulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08572)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongyu Liu, Chun Wang, Feng Gao, Xuanhua He, Yue Ma, Ziyu Wan, Yong Zhang, Xiaoming Wei, Qifeng Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an on-policy self-distillation paradigm for few-step autoregressive video diffusion models, using real video context to provide dense trajectory-level supervision during rollout.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08766)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shashi Kumar, Yanis Labrak, Hasindri Watawana, Sergio Burdisso, Esa\'u Villatoro-Tello, Kadri Hacio\u{g}lu, Petr Motlicek, Andreas Stolcke

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO (a verifiable-reward RL method) to ASR adaptation from synthetic speech, demonstrating a clear RL-for-LLMs pipeline with reward design and behavior-level improvements.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.08409)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shiping Yang, Shining Liang, Weihao Liu, Wenbiao Ding, Linjun Shou, Lu Cheng, Angel X. Chang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-play framework combining RLAIF and rule-based RL to iteratively improve a hallucination detector via an evolved generator, directly matching RL for LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.07993)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Didula Samaraweera, Anjana Supun, Srinath Perera

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a three-phase pipeline combining offline data synthesis, SFT, and RLVR with on-policy rollouts to improve low-resource code generation, directly relevant to RL for LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.07748)

---

