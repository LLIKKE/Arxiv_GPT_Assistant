# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
The RL for LLMs field is undergoing a significant maturation, moving beyond basic PPO and GRPO implementations to address systemic bottlenecks in training efficiency, credit assignment, and reward design. A clear trend is the push for **token-level and granular credit assignment**, exemplified by CoRT's counterfactual replay for rubric-conditioned GRPO and ODYSSE's episode-wise GRPO (ESPO) for personalized agentic reasoning. This granularity is complemented by efforts to**optimize compute budgets**and**reduce wasted rollouts**, as seen in SARA's sequential adaptive rollout allocation for RLVR. Simultaneously, researchers are tackling fundamental RL stability and generalization issues: ReCo addresses distributional concentration in GRPO, while a game-theoretic framework for KL-regularized fine-tuning provides a principled approach to setting regularization coefficients. The integration of**meta-learning**for reward shaping and**self-evolving rubrics**(SERPO) for open-ended generation further demonstrates a shift toward more adaptive and autonomous RL pipelines. Notably, the field is also confronting practical deployment challenges with HiFloat4 enabling end-to-end FP4 quantization for RL post-training, bridging the gap between research and production.

### On-Policy Distillation and Knowledge Transfer
On-policy distillation is emerging as a dominant paradigm for both aligning LLMs and injecting specialized knowledge, moving beyond simple imitation to more sophisticated, value-aware, and contrastive methods. The core innovation is the**use of on-policy, student-generated data**to bridge the distribution gap between teacher and student, as directly studied in the shared SFT lessons work. W2S-OPD advances this by distilling from multiple weak models using contrast-based proxy teachers and on-policy reverse KL, while RoCo-ACE introduces rollout-conditioned distillation that reweights learning to reference-supported tokens. The Veritas++ framework extends this to AIGI detection with a value-aware mechanism that prioritizes high-value on-policy signals. A parallel thread involves**distilling reasoning and temporal capabilities**, with the time-truncation harness enabling efficient distillation of temporal search and reasoning for future prediction. These works collectively illustrate a move from static, off-policy distillation to dynamic, adaptive, and performance-aware knowledge transfer that is tightly coupled with the student's own learning trajectory.

### Reasoning, Agents, and Structured Generation
The intersection of reasoning, reinforcement learning, and agentic systems is producing novel architectures and training paradigms focused on**efficiency, personalization, and skill composition**. Penelope introduces localized latent recurrence, confining recurrent computation to a narrow decoder interval to reduce inference latency on structured reasoning tasks, a key advancement for practical deployment. For agents, SkillRise proposes a unified framework for cross-task skill evolution using decoupled credit assignment and an evolving skill document, directly tackling the challenge of generalizable agentic behavior. ODYSSE's personalized agentic reasoning and the interactive reward agent (IRA) for GUI tasks highlight a growing emphasis on**environment-aware and user-specific** agent training. The DHRCL framework for code LLMs demonstrates the power of dense hierarchical rewards and curriculum learning to guide complex behavior, while the DMAPO method shows that high-quality, data-centric preference optimization (using multi-evaluator agreement) can achieve better alignment with less data. Finally, the work on robust PPO for small-scale language model agents identifies critical failure modes and proposes practical fixes, underscoring that scaling laws are not the only path to progress.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Fangxu Yu, Zinan Lin, Xiaodong Liu, Weijia Xu, Michael Xu, Tianyi Zhou, Jianfeng Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Weak-to-Strong On-Policy Distillation (W2S-OPD), a novel framework that distills from multiple weak models to improve a strong student via contrast-based proxy teachers and on-policy reverse KL, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26246)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zibin Meng, Zhenyu Zhao, Chunqiang Run

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an online, entropy-proxy-driven knowledge-point selector for verifiable-reward RL, directly improving reasoning-oriented RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24833)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jianze Wang, Kunwang Zheng, Ying Liu, Yu Cao, Qilong Zhang, Jinlong Chen, Hua Yang, Qianglong Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving rubric policy optimization (SERPO) for test-time RL in open-ended generation, co-evolving response archives, rubrics, and policy parameters without external rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26873)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Bo-Wen Zhang, Junwei He, Wen Wang, Song-Lin Lv, Wentao Ma, Rongyi Lin, Shuhan Zhong, Lan-Zhe Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CoRT, a token-level credit weighting method for rubric-conditioned GRPO that uses counterfactual replay to redistribute advantages across tokens without an auxiliary scorer, directly improving RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25659)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Keegan Harris, Brian W. Lee, Ian Waudby-Smith, Philip Amortila, Nika Haghtalab, Michael I. Jordan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a game-theoretic framework for KL-regularized RL fine-tuning that provides a principled method for setting the regularization coefficient, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26358)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a sequential adaptive rollout allocation method (SARA) for compute-efficient RLVR, directly improving RL training for LLMs by reducing wasted rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26253)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hei Yi Mak, Shadan Golestan, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Yaoyuan Wang, Yao Wang, Junsong Wang, Tianchi Hu, Fengchen He, Guipeng Hu, Tanzila Rahman, Anandharaju Durai Raju

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HiFloat4 format and Rollout-ResQ to enable end-to-end FP4 RL post-training for LLMs, addressing quantization-induced rollout-training mismatch.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26515)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yutong Chen, Shouqian Shi, Xinran Liu, Haochen Wang, Jiaying Wang, Tianxing Xu, Yuanxi Wang, Zirui Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Penelope, a latent reasoning framework that localizes recurrent computation to a narrow decoder interval, reducing inference latency while maintaining accuracy on structured reasoning tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25915)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies and fixes specific failure modes in PPO for small LLMs, proposing a capacity-headroom hypothesis and a robust training pipeline with practical techniques.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25091)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuhang Wang, Ziming Li, Hui Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DHRCL, a novel RL framework for code LLMs with dense hierarchical rewards and curriculum learning, directly improving LLM behavior via explicit reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26457)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhengtao Yao, Runhao Li, Xupeng Chen, Jiayi Cheng, Chenqian Le, Michael Yue, Siheng Wang, Haoyan Xu, Yuqi Li, Chenhao Wei, Zhengdao Li, Rongchao Zhang, Guang Yang, Yidong Wang, Junhao Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DMAPO, a data-centric method using multi-evaluator agreement on on-policy responses to create a small, high-quality preference dataset for KTO training, directly improving alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25136)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hao Tan, Jun Lan, Zichang Tan, Ajian Liu, Zijian Yu, Chuanbiao Song, Huijia Zhu, Weiqiang Wang, Jun Wan, Zhen Lei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Value-aware On-Policy Distillation (VaOPD) for AIGI detection, a new adaptive distillation mechanism that prioritizes high-value on-policy signals from a privileged self-teacher.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27113)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wanxu Cai, Zhengyu Chen, Huaisheng Zhu, Wei Wang, Jingang Wang, Qiang Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a time-truncation harness for on-policy distillation of temporal search and reasoning data into LLMs, directly improving future prediction capabilities.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25554)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hao Jiang, Peiru Du, Pengfei Yao, Mengting Li, Siyuan Lou, Kuo Cai, Sheng Yu, Qiang Luo, Jian Liang, Ruiming Tang, Fei Pan, Peng Jiang, Wenwu Ou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent reasoning framework for recommendation models that compresses explicit CoT into learnable latent tokens, directly addressing latent reasoning efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26621)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Anton de la Fuente, Arthur Conmy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies on-policy SFT data mixing to preserve capabilities during alignment, a core on-policy distillation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26173)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yunpeng Chu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a meta-learned reward shaping framework for RLHF that improves alignment and training stability with theoretical guarantees.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26094)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junoh Park, Junseo Hwang, Wonguk Cho, Taesup Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ReCo, a reweighting method for GRPO that addresses distributional concentration in RL for LLMs, improving reasoning coverage.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26862)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yan Hong, Wei Li, Kedong Xiu, Jun Lan, Shuheng Zhou, Zhongcai Lyu, Huijia Zhu, Weiqiang Wang, Jianfu Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RoCo-ACE, a rollout-conditioned online distillation objective for knowledge injection that reweights distillation to reference-supported tokens and adds sparse correction, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24771)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chenrui Shi, Yuwei Wu, Yang Liu, Ruining Feng, Zirui Shang, Zhi Gao, Lifeng Fan, Che Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel interactive reward agent (IRA) for GUI task evaluation that verifies environment state, and demonstrates its use as a reward signal for RL training of GUI agents, directly matching RL-for-LLMs criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25904)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiaqi Zhang, Tong Chen, Junliang Yu, Quoc Viet Hung Nguyen, Hongzhi Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Episode-wise GRPO (ESPO), a novel RL fine-tuning framework for personalized agentic reasoning with episode-level rewards and advantage estimation, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25369)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhiyuan Yao, Yuxin Chen, Zhengxi Lu, Zishan Xu, Yueqing Sun, Yifu Guo, Yuquan Lu, Zhengzhou Cai, Kangning Zhang, Zhuowen Han, Zi-Han Wang, Ziang Ye, Qi Gu, Xunliang Cai, Weiwen Liu, Yongliang Shen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SkillRise, a unified RL framework for cross-task skill evolution in LLM agents via decoupled credit assignment and an evolving skill document, directly matching RL-for-LLMs and on-policy distillation criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26784)

---

