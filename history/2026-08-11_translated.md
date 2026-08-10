# 💡 今日研究速览 (Daily Summary)

### RL for LLMs & Agents

The dominant theme across today's research is the maturation of Reinforcement Learning (RL) as the primary driver for enhancing LLM agentic capabilities. A significant focus is on moving beyond monolithic, outcome-based rewards toward fine-grained, dense, and structurally aware credit assignment. Works like **DiDPO**and**FACTOR**exemplify this by leveraging code diffs and action-to-token allocations, respectively, to provide more precise learning signals.**Gated-BEPO**introduces a Bellman fixed-point approach for advantage estimation, while**Trajectory-Relative Hindsight Distillation (TRIAL)**proposes a critic-free, trajectory-relative density for supervision. This collective push toward granular credit assignment indicates a clear shift from "if it works" to "why and how it works," enabling more sample-efficient and robust training for complex, multi-turn tasks.

This trend is complemented by a surge in domain-specific RL applications, each introducing novel reward design and training loops. From clinical decision-making (**ResidencyRL**) and hypothesis testing (**Fisher-R1**) to web development (**WebGrader**) and privacy-preserving anonymization (**GRASP**), the field is rapidly expanding into specialized verticals. The introduction of verifiable, programmatic, or self-evolving rewards—as seen in**WebGrader's**self-evolving grader and**NTDH's**tolerance-aware verification—is a critical enabler, allowing RL to be applied where traditional, hand-crafted reward functions are infeasible. Furthermore,**IB-RL's**bilateral training paradigm and**Capek 0.5's**execution-centric taxonomy with verifiable rewards highlight a move toward more sophisticated training paradigms that address generalization to unseen environments and opponents, a key hurdle for real-world deployment.

### On-Policy Distillation & Model Compression

A second major research thrust is the refinement of on-policy distillation (OPD) to bridge the gap between large teacher models and smaller student models. The core challenge being addressed is state and trajectory misalignment, where a student's rollouts diverge from the teacher's expertise.**MemOPD**tackles this head-on with memory-state alignment, while**Simple-OPD**demystifies the warm-up phase, identifying teacher-compatible chain-of-thought supervision and LoRA-based training as critical ingredients for success. These works collectively suggest that effective distillation is not just about transferring knowledge, but about carefully orchestrating the student's learning trajectory to remain within the teacher's competence region.

Beyond simple imitation, there is a clear movement toward self-evolving and proximal methods for skill acquisition.**SkillProx**introduces a proximal-gradient-inspired framework for agents to refine their own skills, and**FutureBridge** innovates on collaborative decoding by using the student's own reasoning ability as a counterfactual training signal. This represents a conceptual shift from static distillation to a dynamic, interactive process where the student actively shapes its own learning curriculum, potentially leading to more robust and adaptable small models that can surpass their initial teacher's performance on specific tasks.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhiyuan Liu, Tinghong Ye, Chenghao Liu, Yizhuo Li, Songfang Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces MemOPD, a memory-state-aligned on-policy distillation method that corrects state misalignment during context compression, providing dense teacher supervision on student rollouts and significantly improving long-horizon agent performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07068)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Valentin Li\'{e}vin, Samuel Schmidgall, Tim Strother, Alex Bijamov, Akshay Goel, Anil Palepu, Chunjong Park, Vahid Balazadeh, Min Woo Sun, Marius Guerard, Justin Chen, Dave Steiner, Vikram Dhillon, Ibrahim Azar, Akhil Mehta, Nicholas Spetsieris, Shilpan Shah, Maen Abdelrahim, Amit Dahiya, Yun Liu, Katherine Chou, Yossi Matias, Avinatan Hassidim, Dale R. Webster, Quoc V. Le, Raia Hadsell, Joelle Barral, Carey Radebaugh, Aleksandra Faust, Shekoofeh Azizi, Mike Schaekermann, Po-Hsuan Cameron Chen, Tao Tu, David Racz, Lin Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a multi-turn RL training framework with structured rewards for clinical decision-making, directly advancing RL-for-LLMs with a novel reward design and training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07418)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hongxi Yan, Ziyue Huang, Shichao Fan, Qingjie Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel Bellman fixed-point credit assignment method for RL training of LLM agents, directly advancing RL-for-LLMs with a new advantage estimation technique.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06861)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ying Chen, Weizhen Li, Zhe Hu, Zhenjiang Li, Rui Jiang, Zhifeng Gu, Lihuang Fang, Jiangping Liu, Lei Yi, Jie Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an execution-centric capability taxonomy for embodied VLM training, using RL with verifiable rewards per capability and weight-space merging plus routed policy-space distillation, directly relevant to RL-for-LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06756)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a scalable instruction-tuning method with explicit creativity spans and shows RL (GRPO) benefits from creative checkpoints, directly improving RL-for-LLM training substrate.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07460)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xucong Wang, Zhe Zhao, Liheng Yu, Di Wu, Xiaofeng Cao, Pengkun Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DiDPO, a critic-free RL method with fine-grained credit assignment based on code diffs for coding agents, directly advancing RL for LLMs with a novel reward/credit design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07147)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Senhao Wang, Chenghao Cai, Haitao Hu, Mingxing Huang, Xingguang Wang, Wenhao Li, Zecheng Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new bilateral RL training paradigm with isolated per-agent advantages and updates, directly addressing the static-counterpart mismatch in strategic dialogue and improving generalization to unseen counterparts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06735)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Boshui Chen, Huiping Liu, Shaolei Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving programmatic grader that autonomously derives executable reward contracts for RL training of LLMs in web development, directly advancing reward design for RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06474)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lichao Ma, Yang Sun, Shuaitao Zhao, Yangyi Fang, Cong Qin, Xiaoliang Fu, Yuhang Tian, Yuchen Wei, Junbo Zhu, Yang Wei, Lu Pan, Jiaye Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces FACTOR, a credit-conscientious action-to-token allocation method for multi-turn agent RL, directly improving RL training for LLM agents via a new credit assignment objective.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07118)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Mingxuan Zheng, Yujin Zhou, Chuxue Cao, Boqin Yin, Yuyao Zhang, Jiapeng Sun, Shuaishuai Gong, Sirui Han, Yike Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SkillProx, a proximal-gradient-inspired self-evolving skill refinement framework with closed-loop diagnosis and utility-aware deletion, directly advancing on-policy distillation for LLM agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07449)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Quanquan Li, Hongbo Zhang, Yihe Chi, Jingyu Li, Xidong Xi, Liuyang Song, Hongzhen Zhang, Yuxiang Huang, Jing Ke, Siyuan Ma, Junyi Lin, Guitao Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel token-selection method for collaborative decoding that ranks candidates by the SLM's ability to continue reasoning, directly improving SLM reasoning via a counterfactual training signal.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06819)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shi Chen, Hayato Aida, Makoto Morinaga, Shohei Tanaka, Kosuke Arima

**机构**: Stockmark Inc.

**💡 亮点 (Highlight)**: Applies DAPO-based RL with a task-level reward for structured document parsing, demonstrating RL's effectiveness beyond SFT and addressing forgetting control, directly relevant to RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06758)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tao Liu, Taiqiang Wu, Mao Zheng, Xuan Luo, Runming Yang, Xuewei Yang, Junjie Wang, Yujiu Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Simple-OPD, a plug-and-play warm-up initialization method for on-policy distillation that identifies teacher-compatible CoT supervision and LoRA-based training as key factors, directly advancing the on-policy distillation topic.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06802)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoyu Zheng, Yun Zhu, Qing Wang, Wenqiao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TRIAL, a trajectory-relative hindsight distillation framework that allocates dense supervision across turns via a signed log-probability gap, improving agentic RL performance over GRPO on WebShop and ALFWorld.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07371)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tianlei Zhu, Zhiwei Liu, Yuyan Wang, Xiao-Yang Liu, Sophia Ananiadou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a verifiable-reward RL pipeline (GRPO) with tolerance-aware verification and directional hints for affective reasoning, directly advancing RL-for-LLMs with a new reward design and training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06425)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sajjad Ghiasvand, Nader Sehatbakhsh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces GRASP, an online RL (GRPO) framework with a self-generated reward for privacy-preserving text anonymization, directly optimizing the privacy-utility objective and improving over DPO-distilled baselines.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06526)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiacheng Miao, Jin Mu, Guanhua Chen, James Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Fisher-R1, an RL-trained LLM agent for hypothesis testing with a verified statistical reward, directly advancing RL-for-LLMs with a new reward design and training pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07437)

---

