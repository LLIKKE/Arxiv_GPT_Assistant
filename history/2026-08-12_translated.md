# 💡 今日研究速览 (Daily Summary)

### On-Policy Self-Distillation (OPD) & Reasoning Distillation

The dominant theme today is the rapid maturation of On-Policy Self-Distillation (OPSD) as a core post-training paradigm. The field is moving beyond simple token-matching toward a deeper theoretical and practical understanding of *what* constitutes effective privileged information. Key papers dissect the underlying mechanisms—such as ablating the reference solution to show teacher context-induced behavior is the primary driver, or formally separating token credit from outcome credit to avoid conflating likelihood with value. This theoretical rigor is paired with significant engineering innovation: frameworks now propose adaptive anchoring to combat rollout-conditioned signal degradation, variational target interpolation with Renyi divergence for stability, and mixture-constrained co-training to address optimization instability. A clear consensus is emerging that the *quality* and *structure* of the teacher signal matter more than raw agreement, with methods like TIDE correcting token mismatch via Hellinger shaping, and SKALD using abstract skill cards as dense privileged signals when group-relative rewards are uninformative. The application scope is also broadening, extending from pure reasoning to code agents (FailForge), multimodal LLMs (visual distillation from counterfactual blind spots), and even flow-matching generative models (DreOPD), establishing OPD as a general-purpose capability injection mechanism.

### Reinforcement Learning for LLMs (RLVR & Policy Optimization)

Reinforcement learning with verifiable rewards (RLVR) is undergoing a phase of algorithmic refinement aimed at improving credit assignment, exploration, and robustness. The trend is away from monolithic policy updates toward more granular, structure-aware optimization. SoftmaxGRPO replaces brittle z-score normalization with a softmax advantage estimator, while Multi-Branch Policy Optimization introduces tree-based segment-level credit assignment for multimodal reasoning. Exploration is being enhanced through parameter-space perturbations (Parameter Exploration for RLVR) and representation-based intrinsic rewards (Search-G1) that co-evolve with the policy. A critical new focus is on generalization robustness: PIRL tackles prompt-invariance in multimodal RL, and a new paper identifies "reasoning collapse" in subjective tasks, proposing conditional length-penalized post-training and persona-routing. Reward design is also becoming more sophisticated, with knowledge-guided hybrid rewards for medical math (MedCalc-R1) and counterfactual evidence audits for visual reasoning (Evidence-RL). Finally, the connection between RL and distillation is blurring, with methods like RL-Native Distillation exploiting RL teacher trajectories for few-step generation and Omni2LoRA using GRPO to allocate rank for parametric memory.

### Agents & Test-Time Scaling

Research on LLM agents and inference-time compute is converging on the idea of *structured* and *selective* scaling. Instead of brute-force sampling, the field is moving toward principled methods for allocating compute and guiding search. Thought-Level Beam Search offers a new inference-time compute allocation method that prunes and branches on partial reasoning trajectories, while Consilience provides a verifier-free framework for selecting the best trajectory based on confidence. For agents, the focus is on closing the loop between environmental feedback and policy updates: multi-timescale credit assignment methods extract environment-grounded process signals to reweight returns, and frameworks like LookAgain use closed-loop visual reflection with GRPO for GUI grounding. The concept of "compiling" experience into reusable assets is a strong emerging theme, whether it is distilling reasoning traces into skills to amortize cost (Reason Wide, Not Deep) or using MCTS to generate reasoning trees for skill evolution (Branch2Skill). Zeroth-order optimization (Beyond the Capability Boundary) is also introduced as a way to perturb parameters and help agents learn beyond their current capability boundary, effectively creating a self-evolution loop with SFT.

### Multimodal & Efficiency

Multimodal research is increasingly intertwined with RL and distillation, focusing on two key axes: robustness and compression. On the robustness front, frameworks like StructReward provide dense structured process rewards for self-correcting multimodal reasoning, and ADOPD introduces reference-privileged distillation for industrial anomaly detection without inference-time retrieval. A significant sub-theme is the preservation of capability under compression: the Motif 3 technical report and a paper on vision-text compression both leverage multi-teacher or cross-modal agentic policy self-distillation to bridge the "agentic policy gap," ensuring that compressed models retain their reasoning and grounding abilities. Efficiency is also being addressed at the architectural level with latent reasoning models (Full-bandwidth transformer, Relit), which aim to perform deep computation in hidden states to reduce explicit token generation. Omni2LoRA pushes this further by distilling multimodal context into LoRA adapters via a GRPO-based rank allocation policy, using counterfactual rewards to maintain coherence while compressing memory.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 9/10

**作者**: Xi Wang, Ziyang Cai, Zheng Zhan, Harry Dong, Ying Fan, Gustavo de Rosa, Tim Pearce, John Langford

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces latent feedback to widen the vertical channel in transformers, enabling non-verbalized computation to re-enter the stack and improving reasoning efficiency with shorter traces.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08888)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jiaxin Guo, Yanwei Yue, Xuanbo Fan, Chunyu Yang, Yan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a fully unsupervised on-policy self-distillation framework that uses consensus and disagreement signals from the model's own rollouts, directly advancing on-policy distillation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08764)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhuo Sun, Entong Li, Yanlong Zhao, Xiaoyuan Cheng, Wenxuan Yuan, Kaiyu Li, Che Liu, Huihang Liu, Harrison Bo Hua Zhu, Li Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-referenced on-policy self-distillation method with a variational target interpolation and Renyi divergence projection, directly improving the stability and effectiveness of on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09745)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yubo Jiang, Fengying Xie, Zhiguo Jiang, Haopeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces SKALD, an on-policy self-distillation framework that uses abstract skill cards as privileged signals to provide dense supervision when group-relative RL rewards are uninformative, directly advancing on-policy distillation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09826)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yifan Li, Ruxin Sun, Tongzhou Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes StructReward, a compute-efficient framework providing dense structured process rewards via lightweight matching rules and a gated GRPO objective, with rollout recycling for self-correction, directly advancing RL for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08326)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Meilin Yang (Renmin University of China, Beijing, China), Zixuan Ding (Renmin University of China, Beijing, China), Jianhao Nie (Renmin University of China, Beijing, China), Weite Zhang (Renmin University of China, Beijing, China), Yuxin Zhang (Renmin University of China, Beijing, China), Zhiming Shao (Renmin University of China, Beijing, China), Li Yu (Renmin University of China, Beijing, China), Zhe Fu (Renmin University of China, Beijing, China)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified on-policy self-distillation framework with adaptive canonical-context anchoring to mitigate rollout-conditioned signal degradation, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07935)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zichao Yu, Chengzhi Yu, Shengze Xu, Yujin Han, Bingqing Jiang, Xu Wang, Difan Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TIDE, a novel on-policy distillation correction method that addresses teacher-student token mismatch via bounded Hellinger shaping and teacher top-K injection, directly improving LLM reasoning post-training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09836)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zehao Chen, Gongxun Li, Tianxiang Ai, Yifei Li, Zixuan Huang, Wang Zhou, Tao Huang, Fuzhen Zhuang, Xianglong Liu, Jianxin Li, Deqing Wang, Yikun Ban

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a mixture-constrained co-training method for on-policy distillation with two trainable policies, directly addressing instability in OPD and showing strong reasoning/code gains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09447)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shravan Venkatraman, Omkar Thawakar, Ritesh Thawkar, Abdelrahman Shaker, Rao Muhammad Anwer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a fully self-contained on-policy token-level visual distillation framework for MLLMs that identifies counterfactual blind spots and converts them into dense contrastive supervision, directly advancing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09931)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yangyang Feng, Zhuoyan Feng, Junlan Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces PAST, a novel on-policy self-distillation method that uses complete student trajectories as privileged information for the teacher, improving reasoning benchmarks over vanilla OPSD.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08726)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, Junpei Komiyama

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly dissects on-policy self-distillation by ablating the reference solution, showing teacher context-induced behavior is the key driver, a central contribution to on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09228)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Bingzhen Liu, Xiaomeng Fan, Yuwei Wu, Zhi Gao, Mingyang Gao, Chuanhao Li, Yunde Jia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a zeroth-order self-evolution framework that perturbs LoRA parameters to enable LLM agents to learn beyond their capability boundary, forming a closed loop with SFT on sampled trajectories.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09292)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Vatsal Venkatkrishna, Nico Daheim, Iryna Gurevych

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces parameter-space exploration for RLVR via perturbed policy sampling, directly improving GRPO training for LLM reasoning and code generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09805)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Dongyi Lv, Fushun E, Aichen Cai, Liang Huang, Ya Zhang, Qiuyu Ding, Canhui Wu, Zhi Wang, Yuesong Zhang, Jiaqi Wang, Nan Duan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces FailForge, an agentic framework that converts failed rollouts into training signal via skill-guided second attempts, directly improving code agent performance through on-policy distillation from failures.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08570)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yongkang Yang, Zhezheng Hao, Hong Zhang, Yi Liu, Xiankun Lin, Wence Ji, Fanjunduo Wei, Jiarui Yu, Qiang Lin, Xiaoyun Liang, Hande Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified optimization framework for on-policy self-distillation that jointly optimizes token selection and privileged information, directly advancing the on-policy distillation topic.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08176)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yanwei Ren, Haotian Zhang, Likang Xiao, Jiaxing Huang, Jiayan Qiu, Baosheng Yu, Quan Chen, Liu Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel framework that uses Monte Carlo tree search to generate a reasoning tree and distills multi-step evidence into skill updates, directly improving on-policy distillation efficiency for LLM reasoning and agentic tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08677)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Abhishek Panwar, Maheep Singh, Saksham Bansal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a recursive latent implicit transformer that performs deep reasoning in hidden states, directly addressing latent CoT with a novel hybrid architecture.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08113)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jefferson Hernandez, Jaywon Koo, Zilin Xiao, Chen Wei, Vicente Ordonez

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a new group-based RL objective (SoftmaxGRPO) that replaces z-score normalization with softmax advantages, directly improving RL-for-LLM training with verifiable rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09271)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianjun Pan, Yuan Li, Hongda Wang, Linbo Jin, Mengfei Song, Lei Gao, Qiming Shi, Shaokang Fu, Jiarong Zhao, Chengyu Wang, Chengfu Huo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a bidirectional context self-distillation framework that rescales RL advantages with complementary token-level signals, directly improving skill utilization in LLM agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09555)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xuanchen Li, Haitao Li, Yujia Zhou, Qingyi Pan, Heng Wang, Yiqun Liu, Min Zhang, Qingyao Ai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces SLIFT, a selective self-learning framework that decomposes user feedback into Fix/Spec/Null components and trains Generalist/Specialist LoRA adapters via feedback-conditioned self-distillation, directly advancing on-policy distillation for LLM improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09109)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Pengfei Zhou, Zhiwei Tang, Xiaopeng Peng, Chenrui Zhou, Lama Moukheiber, Yixing Ma, Bin Xu, Jiajun Song, Zhenglin Wan, Wangbo Zhao, Jiasheng Tang, Bohan Zhuang, Fan Wang, Yang You

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PIRL, a Prompt-Invariant RLVR method with a dynamic trinary reward and consistency regularizer to improve generalization robustness of multimodal RL, directly advancing RL for LLMs with verifiable rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08802)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Shuai Lyu, Yuning Gong, Ruiling Gao, Xiaoran Shang, Zhonghong Ou, Ping Zong, Yifan Zhu, Yuan Sun, Yang Qin, Peng Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Multi-Branch Policy Optimization, a tree-based RL framework with segment-level credit assignment for multimodal LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07581)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jinkun Hou, Zhuo Liu, Huimin Ren, Hongsheng Xin, Pan Zhou, Kun Zhan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces rubric-informed selective exploration for open-ended RL, using missed criteria to elicit privileged trajectories and a separate auxiliary objective to improve LLM alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09123)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Mingfeng Lin, Chengfei Cai, Lin Xu, Yuxiang Wei, Liang Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel on-policy distillation method for flow-matching models that converts implicit reward extrapolation into closed-form velocity regression, directly advancing on-policy distillation for generative models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09233)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lecheng Kong, Like Hui, Haitao Mao, Jun Huan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel confidence-trajectory-based selection framework for verifier-free test-time scaling, directly improving LLM reasoning on complex tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09898)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Puneet Mathur, Manan Suri, Dinesh Manocha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a GRPO-based rank allocation policy with a counterfactual reward to distill multimodal context into LoRA adapters, directly advancing RL-driven optimization for LLM efficiency and latent memory compression.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09227)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chengyu Lai, Jiuning Lin, Zhibo Xiao, Xiaodong Zhu, Ruiquan Lan, Bin Zhang, Zihong Huang, Wendong Zhang, Chuxin Chen, Yinjiang Cai, Shuai Zhong, Lingqing Zhang, Dimin Wang, Jialin Zhu, Han Zhu

**机构**: Alibaba Group

**💡 亮点 (Highlight)**: Introduces a production-grade on-policy distillation loop with reward-augmented training and self-competitive curriculum for LLM-based ranking strategies, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09440)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Binwen Tan, Jingchao Wang, Dengzhe Hou, Lingyu Jiang, Zeyuan Wu, Yunhan Shen, Fangzhou Lin, Kazunori Yamada, Atsushi Koike

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a control-based regularizer for RL post-training that decouples shared control bottlenecks, improving multi-task reasoning over GRPO.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08224)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Qingying Niu, Ruiyang Ren, Wayne Xin Zhao, Yaliang Li

**机构**: Renmin University of China (RUCAIBox)

**💡 亮点 (Highlight)**: Introduces a brief-guided corrective preference distillation framework that uses state-matched preference pairs to correct search-control drift in LLM agents, directly advancing on-policy distillation for capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08768)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ting Zhou, Zhenqing Ling, Daoyuan Chen, Qianli Shen, Yilun Huang, Ying Shen, Yaliang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a learnability-based static prior for task sampling in LLM RL post-training, directly improving data efficiency and complementing online schedulers.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09217)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuhan Li, Fangao Zeng, Sicong Kang, Mengfei Xu, Hao Zhou, Wei Li, Pipei Huang, Bingbing Ni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a single-stage RL-distillation co-training framework that uses reward-scored trajectories from an RL teacher for few-step image generation, directly advancing on-policy distillation for LLM-adjacent generative models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09226)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Juncheng Dong, Ding Tong, Ishan Gupta, Yuyan Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies reasoning collapse in RLVR for subjective tasks and proposes a conditional length-penalized post-training algorithm plus persona-routing architecture, directly advancing RL-for-LLMs with a new training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08889)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haojie Huang, Xinlei Yu, Chengming Xu, Zhangquan Chen, Cheng Yang, Qingdong He, Yu Yang, Jiangning Zhang, Xiaobin Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Counterfactual Evidence Disentanglement, a training-time evidence audit integrated into GRPO that rewards evidence-dependent answers, directly advancing RL-based post-training for VLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08021)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hongli Shen, Shaopeng Fu, Qinbo Zhang, Jian Li, Di Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dual-adversarial framework that generates a compact reasoning dataset for safety alignment, enabling LRMs to internalize unsafety knowledge and improve jailbreak robustness with minimal utility loss.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09542)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Cheng Ruoxi, Ma Haoxuan, Zhang Hongyi, Zhang Junming, Duan Ranjie, Xia Qiaolin, Wang Hao, Lu Yu, Shi Haibo, Ma Xingjun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a representation-based intrinsic reward framework for search agents that measures evidence grounding and co-evolves with the policy during RL, improving the grounding-search-cost trade-off.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07531)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junghwan Lim, Joon Son Chung, Sungmin Lee, Wai Ting Cheung, Gihun Cho, Minsu Ha, Sangho Kang, Beomgyu Kim, Dongseok Kim, Jangwoong Kim, Taehyun Kim, Taewhan Kim, Jeesoo Lee, Jeongdoo Lee, Junhyeok Lee, Dongpin Oh, Hyeyeon Cho, Dahye Choi, Jaeheui Her, Hanbin Jung, Changjin Kang, Minjae Kim, Youngrok Kim, Hyukjin Kweon, Hongjoo Lee, Yeongjae Park, Bokki Ryu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Multi-teacher On-Policy Distillation as a core post-training component, directly advancing the on-policy distillation topic with a concrete training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09119)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Cheng Fan, Junyi Zhou, Tingzhang Luo, RongJian Xu, Qiyanhui Lu, Mingjian Zhu, Hanting Chen, Jianyuan Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a cross-modal agentic policy self-distillation framework with online RL supervision, directly addressing on-policy distillation for LLM capability preservation under vision-text compression.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08960)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Wenxiao Zhao, Shu Wang, Ying Nian Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving token credit mechanism for DPO that adapts KL regularization based on the model's own internal signals, directly improving RLHF-style preference optimization for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09568)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Renshan Zhang, Haoyang Meng, Yixiao He, Rui Shao, April Hua Liu, Liqiang Nie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a closed-loop GUI grounding framework with post-prediction visual reflection and GRPO-based RL training, directly advancing RL-for-LLMs with a novel reward design and iterative refinement loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09723)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lijie Yang, Hongyin Luo, Tri Dao, Ravi Netravali

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces thought-level beam search, a novel inference-time compute allocation method that prunes and branches on partial reasoning trajectories, directly improving reasoning efficiency and accuracy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08020)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hongchen Wei, Yuanzhe Wang, Bei Liu, Yifan Yang, Qi Dai, Kai Qiu, Yunsheng Li, Dongdong Chen, Chong Luo, Zhenzhong Chen, Baining Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a mutable-state document harness environment with end-to-end RL training for compact VLM agents, directly advancing RL-for-LLMs via a novel environment and training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07527)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xuan-Phi Nguyen, Shrey Pandit, Yiran Zhao, Anurag Koul, Zeyu Liu, Shafiq Joty

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly addresses on-policy self-distillation for LLMs by formally separating token credit from outcome credit, with empirical validation on AIME, a central contribution to on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09263)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Agamdeep Singh, Srishti Gautam, Priyanshu Gupta, Nikita Mehrotra, Tanmay Bakshi, Sumit Gulwani

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a distillation method that compiles reasoning traces into reusable skills, amortizing reasoning cost and recovering most of the reasoning gap with far fewer tokens, directly advancing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07885)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ambuj Mehrish, Sebastiano Vascon

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a graph-based consensus reward via replicator dynamics for test-time RL, generalizing majority voting and providing graded self-supervised rewards for LLM rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09324)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yifu Huo, Shunjie Xing, Chenglong Wang, Peinan Feng, Qiaozhi He, Yan Ding, Anxiang Ma, Yuxin Gao, Tongran Liu, Tong Xiao, Jingbo Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-timescale credit assignment method that extracts environment-grounded process signals to reweight returns, improving long-horizon agentic RL for LLM agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08255)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhengze Huang, Luyang Yu, Di Hong, Xinzhe Huang, Wanyu Lin, Zhixuan Chu, Zhan Qin, Tianhang Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces REIN, an RL alignment framework with reflection and abstention rewards that directly reduces hallucination in large reasoning models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07931)

---

## 47. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jingtai He, Shiyuan Meng, Wenchao Meng, Qinmin Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a reference-privileged on-policy distillation framework where a teacher supervises a query-only student using matched/mismatched reference log-ratios, directly improving MLLM anomaly detection without inference-time retrieval.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.09789)

---

## 48. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ling Lin, Yang Bai, Congcong Zhu, Jiangming Shi, Meng Wang, Yang Long, Jingrun Chen, Ling Shao, Huazhu Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an advantage-guided gating framework with Monte Carlo value evaluation on reasoning trees to dynamically intervene and correct deviations in MLLM open-ended reasoning, directly improving reasoning quality via a novel training and inference procedure.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.07987)

---

## 49. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuaitao Zhao, Feng Ni, Lichao Ma, Jiaye Lin, Fei Han, Yang Wei, Lu Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a graph-based compliance detection framework that uses scaling-guided adaptive sample selection and on-policy distillation to improve small-model performance, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08146)

---

## 50. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haotian Wang, Lian Yan, Xingzhi Yao, Fanshu Meng, Ye He, Jingchi Jiang, Yi Guan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a knowledge-guided hybrid reward framework for RLVR in medical math reasoning, directly advancing reward design for RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.08623)

---

