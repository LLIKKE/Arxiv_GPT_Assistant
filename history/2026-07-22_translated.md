# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
A clear convergence is emerging around on-policy distillation as a powerful paradigm for post-training, with multiple papers demonstrating its ability to bridge the gap between compact models and large-scale RL-trained systems. **CADENCE**and**Trace-Based On-Policy Distillation**both show that leveraging the teacher's denoising trajectories or coverage-adaptive scheduling can unlock reasoning capabilities previously exclusive to massive compute budgets.**Distilled RL**takes this further by integrating teacher supervision directly into the RL objective, outperforming both standard RL and pure distillation. For non-verifiable tasks,**LLM-as-a-Coach**replaces scalar rewards with dense textual feedback from a teacher, mitigating reward hacking and improving generalization. On the optimization front,**OR Else**introduces a differentiable trust region as a drop-in replacement for the clipped surrogate in PPO/GRPO, while**Group Entropy-Controlled Policy Optimization**and**PPO-HSC**tackle mode collapse through entropy-based advantage shaping and novelty rewards, respectively.**Normalized Rewards**offers a simple yet effective length-normalized regularization for DPO/SimPO, and**CIGPO**addresses reward-variance collapse in multi-turn agents by injecting turn-level information gain. The field is also seeing domain-specific RL innovations, from**WeedExpert-R1**for botanical reasoning to**Med-OPD**for medical VLMs, demonstrating the versatility of verifiable reward design.

### On-Policy Distillation & Self-Improvement
The theme of self-improving systems via on-policy distillation is now deeply intertwined with agentic and reasoning domains.**Self-Modifying Lean Proof Agents**exemplify this by evolving their own benchmarks through verifier-grounded coevolution, creating a tight self-improvement loop.**KITE**tackles the critical issue of model collapse in iterative instruction tuning, diagnosing failure modes and using boundary-aware uncertainty to guide data generation—a direct challenge to naive self-distillation. Conversely,**Why Does Feedback-Augmented Self-Distillation Fail**identifies a novel "decoding collapse" in agentic search, proposing an EMA teacher to stabilize supervision.**CriPO**enhances rubric-based RL with on-policy self-distillation to avoid train-inference mismatch on unexplored criteria. For retrieval-augmented generation,**RIMS**leverages on-policy rejection sampling to generate preference data for small language models, paired with a soft multi-pair aggregation mechanism. Together, these works underscore that the success of on-policy distillation hinges on careful trajectory curation, failure-aware data selection, and stabilizing mechanisms to prevent collapse.

### Preference Optimization & Alignment
The quality and structure of preference data remain central to alignment research.**Rater State Bias in RLHF Preference Data**provides a rigorous audit framework, identifying rater state as a structured confound with falsifiable predictions—a crucial step toward more reliable human feedback.**A Geometric Perspective on Stabilizing Value Conflict Resolution**offers a new lens, showing that chain-of-thought reasoning smooths the loss landscape in moral dilemmas and proposing a novel CoT design for better value alignment.**TRACE**takes a different approach, learning a trajectory-based safety patch to restore alignment after fine-tuning, effectively treating safety as a plug-in module.**CIGPO**and**RIMS**also contribute to this space by refining how rewards and preferences are aggregated across turns or multiple pairs, moving beyond simple pairwise comparisons.

### Reasoning & Latent Structure
Uncovering and controlling the internal reasoning processes of LLMs is gaining traction.**Uncovering Latent Reasoning Strategies**proposes a variational objective to decompose and identify hidden reasoning structures, opening the door to more interpretable models.**Can We Break LLMs Out of Self-Loops**introduces activation steering to detect and correct reasoning loops, offering fine-grained control over latent states.**Training Continuous Chain of Thought Models**reveals a dual-regime phenomenon in training continuous CoTs, where direct supervision via averaged embeddings works well for short traces but struggles with long ones.**WeedExpert-R1**and**Med-OPD**both demonstrate how domain-specific CoT pipelines can be incentivized through RL to produce verifiable, grounded reasoning in multimodal contexts.

### Agents & Multi-Turn Interaction
Agentic systems are increasingly adopting RL-based post-training with specialized reward designs.**CIGPO**directly addresses the challenge of sparse and variance-prone rewards in multi-turn evidence-reading agents by injecting information gain at each turn.**MADA-RL**proposes a multi-agent debate framework with counterfactual critics for parameter-efficient reasoning in compact models.**Toward Anthropomorphic Dialogue**uses GRPO with a cognitive-diagnostic reward based on Vygotsky's Zone of Proximal Development to produce more human-like chat interactions. The**Self-Modifying Lean Proof Agents**paper also fits here, as it creates a self-evolving benchmark through agent-environment coevolution. These works highlight a shift from single-turn to multi-turn RL pipelines that require temporally-aware rewards and credit assignment.

### Multimodal & Domain-Specific Applications
Multimodal LLMs are benefiting from RL-based post-training with verifiable, domain-specific rewards.**Med-OPD**is a standout, integrating evidence-aware on-policy distillation for medical VLMs with a novel Medical Evidence Advantage signal for token-level reweighting.**WeedExpert-R1**applies GRPO to botanical reasoning in MLLMs for precision weed grounding, demonstrating that verifiable rewards can be designed for fine-grained visual tasks.**Robust Summarization of Doctor-Patient Conversations**uses DAPO with a concept-matching reward to improve faithfulness in clinical text generation. These applications validate that the on-policy distillation and RL-for-LLMs paradigms are not just theoretical advances but are deployable in high-stakes, specialized domains.

### Off-Policy & Data-Efficient Methods
While on-policy methods dominate, off-policy approaches are making strides in data efficiency and distribution shift.**It Takes 8 Tokens**introduces weak-to-strong off-policy RL by injecting short auxiliary segments from a weak model to expand exploration support, achieving strong reasoning gains with training speedup.**Token-Level Off-Policy Learning**reframes faithful generation as a token-level correctness prediction task, directly addressing distribution shift.**Let the Data Decide** analyzes trade-offs between language modeling and knowledge distillation objectives during continued pre-training, proposing adaptive routing for off-policy distillation. These methods offer complementary advantages, particularly when access to the teacher or online interaction is limited.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Haolin Ren, Ziyang Huang, Chenhao Yuan, Jun Zhao, Kang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes trace-based on-policy distillation (TOPD) for masked diffusion LLMs, using on-policy denoising trajectories and Reverse-KL teacher supervision to match RL-trained reasoning performance with massive compute savings.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16872)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Satyam Kumar, Saurabh Jha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CADENCE, a unified on-policy distillation framework with coverage-adaptive scheduling, dense rewards, and bootstrapped self-distillation that significantly improves reasoning in compact LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16955)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chen Wang, Zhaochun Li, Jionghao Bai, Yining Zhang, Hexuan Deng, Ge Lan, Yue Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Distilled RL, a novel method integrating teacher supervision into the RL objective to provide fine-grained guidance and selectively transfer knowledge, outperforming both standard RL and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17247)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianzhu Ye, Li Dong, Guanheng Chen, He Zhu, Xun Wu, Shaohan Huang, Furu Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Experiential Learning, a novel on-policy distillation method that replaces scalar RL rewards with dense textual feedback from an LLM-as-a-Coach, improving generalization and mitigating reward hacking for non-verifiable tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18110)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuqing Li, Zeguan Wu, Yu Gan, Junyu Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving Lean proof agent with verifier-grounded benchmark coevolution, which is a strong match for on-policy distillation via self-improvement loops.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17352)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Elena Kopteva, Vitaliy Hlynianyi-Zhuk

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel audit framework identifying rater state bias as a structured confound in RLHF preference data, with falsifiable predictions and a protocol for detection.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16195)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Dayu Wang, Jiaye Yang, Weikang Li, Jiahui Liang, Liwei Qian, Xin Pei, Jizhou Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes W2SPO, an off-policy RL method that injects short auxiliary segments from a weak model into target trajectories to expand exploration support and improve reasoning, achieving strong results with training speedup.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16205)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Awni Altabaa, John Lafferty

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel variational objective to uncover latent reasoning strategies in LLMs, directly addressing latent reasoning decomposition.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17674)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Mingxuan Xia, Yuhang Yang, Chao Ye, Shuai Zhu, Shenzhi Yang, Guangcheng Zhu, Yuhang Zhang, Cheng Peng, Haobo Wang, Siqing Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CriPO, a rubric-based RL method enhanced by on-policy self-distillation to address unexplored and suppressed criteria without train-inference mismatch.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18082)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yunhang Qian, Jiaquan Yu, Jiawei Liu, Meng Wang, Hongwei Bran Li, Xiaobin Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Med-OPD, a unified post-training framework integrating on-policy distillation with evidence-aware supervision for Med-VLMs, introducing a novel Medical Evidence Advantage signal for token-level and trajectory-level reweighting.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16303)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaonan Luo, Yue Huang, Kehan Guo, Ping He, Chuan Zou, Ting Hua, Xiangliang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes KITE, a two-stage framework for iterative instruction tuning that diagnoses and mitigates model collapse via failure-guided data generation and boundary-aware uncertainty curation, directly addressing on-policy distillation challenges.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17043)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chinmay Rane, Kanishka Tyagi, Michael Manry

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a smooth, differentiable trust-region objective (Output Reset) as a direct replacement for the clipped surrogate in PPO/GRPO for LLM post-training, with clear RL methodology and empirical comparison.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18163)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xingjian Tao, Yiwei Wang, Yujun Cai, Jing Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a dense reward framework for GRPO that uses token-wise KL divergence from guided prompts and a staged length bonus, directly improving RL for LLM spatial reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17243)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shawn Im, Federico Danieli, Skyler Seto, Barry-John Theobald, Katherine Metcalf

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a length-normalized reward regularization for DPO/SimPO that mitigates over-optimization and improves alignment quality, directly contributing a new reward design for RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16240)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiangan Yuan, Zhixuan Li, Han Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes adaptive objective routing for off-policy distillation in continued pre-training, analyzing supervision trade-offs between LM and KD objectives.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16246)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov, Zifeng Ding, Volker Tresp, Yunpu Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-agent RL framework with a counterfactual critic advantage for parameter-efficient reasoning in compact LLMs, directly improving RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18006)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yujie Shen, Haowen Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PPO-HSC, an RL framework for LLM fine-tuning that adds a novelty-reward term to encourage diverse reasoning paths, directly addressing mode collapse in RLVR.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16206)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Fan Yang, Rui Meng, Yuxin Wen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a novel failure mode (decoding collapse) in on-policy self-distillation for agentic search and proposes an EMA teacher to stabilize supervision, directly contributing to on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17558)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wentao Liu, Siyu Song, Xi Chen, Youjia Li, Xiaokun Wang, Min Ji, Ji Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a closed-loop framework for anthropomorphic dialogue that uses GRPO with a cognitive-diagnostic, ZPD-aware reward, directly contributing to RL for LLMs with a novel reward design and training pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17191)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Aivo Olev, Tanel Alum\"ae

**机构**: TalTech

**💡 亮点 (Highlight)**: Applies DAPO reinforcement learning with a concept-matching reward to improve LLM summarization of doctor-patient conversations, directly contributing to RL for LLMs with a verifiable reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17230)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hao Dou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CIGPO, a turn-level reward injection method using information gain to fix reward-variance collapse in GRPO for multi-turn LLM agents, directly addressing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16244)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zitong Huang, Gustavo Lucas Carvalho, Deqing Fu, Robin Jia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a token-level off-policy labeling (TOPL) method for faithful generation that reframes post-training as a token-level correctness prediction task, directly addressing distribution shift and improving generalization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17524)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Varun Yerram, He He, Eunsol Choi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes C-MTP, a direct supervision method for training continuous chain-of-thought models using averaged embeddings, and reveals limitations of current methods on long reasoning traces.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16972)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pei Tian, Zihan Dong, Tianci Liu, Linjun Zhang, Haoyu Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RIMS, a preference optimization framework for SLMs that uses on-policy rejection sampling for data generation and a novel soft aggregation mechanism for multi-pair preference optimization, directly relevant to on-policy distillation and RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16431)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zonglin Yang, Wei-Zhen Liang, Nevin Lawrence, Xin Qiao, Benjamin Riggan, Chi-En Chiang, Fuchen Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO with verifiable rewards for botanical reasoning in MLLMs, directly contributing to RL-for-LLMs with a new reward design and domain-specific CoT pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16492)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sheldon Yu, Tong Yu, Xunyi Jiang, Rohan Surana, Gagan Mundada, Sungchul Kim, Lina Yao, Julian McAuley, Junda Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces SOPHIA, a method for fine-grained control of reasoning via latent state steering and self-loop detection, directly targeting latent reasoning control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18100)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Saket Reddy, Andy Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a geometric perspective on value conflict resolution in RLHF, showing CoT reasoning smooths the loss landscape and introduces a new CoT design for improved moral reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.17946)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Changyue Li, Jiaming He, Youliang Yuan, Jialin Wu, Boxi Yu, Zhicong Huang, Pinjia He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TRACE, a trajectory-based safety patch learning framework that optimizes a plug-in patch to recover LLM safety after fine-tuning, directly addressing RL-based alignment via offline patch learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16242)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guangran Cheng, Chengqi Lyu, Songyang Gao, Wenwei Zhang, Kai Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GEPO, a lightweight extension to GRPO that uses group entropy for asymmetric advantage shaping, directly improving RL for LLMs on heterogeneous tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16850)

---

