# 💡 今日研究速览 (Daily Summary)

### RL for LLMs

The dominant theme in RL for LLMs today is the move beyond binary, outcome-only rewards toward denser, more structured, and more adaptive reward signals. This is evident in RLPF's staged reward design for code generation, which combines execution progress with relative efficiency, and in RefineSVG's closed-loop visual feedback mechanism that enables self-correction through a Diff-Map residual signal. The field is also actively tackling the efficiency and stability of RL training itself: Kalman-filter-based dynamic prompt selection (Kalman Meets Curriculum) and latent-guided prompt sampling (LEEPS) both address the critical bottleneck of rollout efficiency and policy drift in RLVR, while LSPO introduces a sampling-time LoRA scaffold to recover gradients on zero-reward prompts, a clever solution to the sparse-reward cliff problem. The emerging consensus from probing studies (Probing the Origins of Reasoning Performance) is that RL fine-tuning produces fundamentally better, more linearly separable representations than SFT, providing mechanistic justification for the RL-centric post-training paradigm. Notably, a rigorous efficiency analysis (Sample More, Reflect Less) challenges the value of costly self-refinement loops, suggesting that at equal token budgets, simple repeated sampling is often superior—a finding that has direct implications for how we allocate compute in RL pipelines. Finally, the application space is expanding rapidly, from cybersecurity triage and HPC task optimization to machine unlearning and visual edit reasoning, with new reward formulations (exponential, PageRank-inspired, confidence-modulated) being tailored to each domain's unique constraints.

### On-Policy Distillation

On-policy distillation has clearly crystallized as the central paradigm for transferring reasoning capabilities, with today's papers focusing on two critical frontiers: the source of supervision and the stability of training. The "expand-then-compress" philosophy (Beyond the Best Teacher) and cross-teacher approaches (Lightning OPD 2.0) are pushing beyond single-teacher distillation, with the latter introducing style-bias residualization to mitigate the risk of copying superficial stylistic patterns rather than genuine reasoning. The theoretical unification of policy optimization and distillation is also advancing: β-OPSD provides a principled KL-regularized bridge between the two objectives, while Flux-OPD offers a formal decomposition of the reverse KL objective to stabilize targets and downweight conflicting gradients. Multimodal distillation is maturing as well, with OPLD transferring reasoning into latent representations and VAD tackling the source-mixing problem through counterfactual target reconstruction for fine-grained visual reasoning. On the safety front, a routing-based approach models distribution divergence directly, enabling template-robust realignment that preserves capabilities while improving safety—a crucial consideration as distillation becomes a primary alignment tool. Together, these works indicate that on-policy distillation is evolving from a simple imitation heuristic into a theoretically grounded, multi-source, and modality-aware training framework.

### Latent Reasoning & Architecture

Latent reasoning is moving from a conceptual idea to a practical architectural principle, with a clear focus on efficiency and hierarchical structure. The depth division of labor revealed in Understanding Is Done Early suggests that LLMs compress information into intermediate layers, enabling a novel memory architecture that caches these states and recomputes only upper layers—a significant step toward unbounded-context memory with self-distillation. The SCSE architecture for looped transformers (Looped Transformers with Source-Centered State Evolution) tackles the tension between input conditioning and shared recurrence, providing a principled mechanism for latent reasoning in iterative computation. Hierarchical Latent Reasoning for Recommendation introduces layer-aware process rewards, demonstrating that latent reasoning objectives can be tailored to specific downstream tasks. The convergence of these approaches—latent distillation (OPLD), latent-guided sampling (LEEPS), and hierarchical latent objectives—suggests that the community is converging on latent space as the primary medium for both reasoning and efficient training.

### Agents & Tool Use

Agentic RL is grappling with the fundamental challenge of sparse and delayed rewards in multi-turn interactions. The transition-aware policy optimization (TAPO) framework addresses this by adding action-conditioned next-observation prediction as a dense auxiliary supervision signal, while Harness-G redesigns the policy-environment interface itself with a graph-structured action space and structured credit assignment for search agents. The visual domain is seeing sophisticated reward engineering: Beacon introduces a Necessity-Aware Adaptive Reward to teach agents when to use tools, and FaithEyes employs a multi-agent self-judging framework with a helpful-tool-ratio reward scaling to improve tool-use faithfulness. A key insight from CRPO is the identification of exposure bias in multi-turn agentic RL, where contrastive self-distillation helps stabilize the policy against distribution shift. These works collectively suggest that the next major leap in agentic capabilities will come not from larger models, but from better interfaces between policy, environment, and reward—making the agent's learning signal denser and more informative.

### Multimodal & Specialized Applications

The multimodal frontier is characterized by task-specific RL formulations that leverage domain structure. The GRPO-based recipe for minimalist RAG (B1ade) demonstrates that emergent attribution can arise without explicit reward engineering, suggesting that simple RL objectives can unlock complex behaviors in small models. RefineSVG's image-to-SVG generation represents a novel intersection of RL and structured output generation, using visual feedback as a natural reward signal. The application of RL to AI-edit reasoning in images (Can VLMs Reason about AI Edits?) shows the versatility of accuracy-based rewards in teaching VLMs to evaluate visual manipulations. The cybersecurity domain (Cybersecurity Detection Classification) combines verifiable rewards with a novel confidence calibrator, addressing the critical need for calibrated uncertainty in high-stakes applications. HARGO's heterogeneity-aware approach to HPC tasks introduces confidence-modulated advantage weighting, a generalizable technique for handling diverse task distributions in RL post-training. Across these applications, a common thread emerges: the most effective RL formulations are those that deeply exploit the specific structure of the target domain, whether that be execution traces, visual feedback, or hierarchical task decompositions.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Songshuo Lu, Zhi Chen, Yaohua Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an expand-then-compress framework with multi-teacher on-policy distillation (TU-OPD) and RGRPO, directly improving LLM reasoning via a novel teacher-union distillation loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27770)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xingjian Wu, Junlin Liu, Xingchen Liu, Xuhang Zhu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CRPO, a contrastive reformulation of on-policy self-distillation that addresses exposure bias in multi-turn agentic RL, directly targeting both RL-for-LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28026)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jiawei Xu, Minghui Liu, Juzheng Zhang, Tom Goldstein, Furong Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces beta-OPSD, a principled generalization of on-policy self-distillation that bridges policy optimization and distillation via a controllable KL regularization parameter, improving reasoning performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28582)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shoutai Zhu, Tianyang Xu, Bin Sun, Mingyuan Xu, Yu Liu, Qinzhen Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes on-policy latent distillation that transfers multimodal CoT reasoning capability into latent representations, directly advancing both latent reasoning and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28154)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yecheng Wu, Song Han, Han Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly addresses cross-teacher on-policy distillation with a novel style-bias residualization method, showing clear gains on reasoning benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28449)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Kangning Zhang, Yixing Li, Shuai Shao, Qingyao Li, Zhengxi Lu, Zhiyuan Yao, Jianghao Lin, Wenxiang Jiao, Yuan Lu, Weiwen Liu, Weinan Zhang, Yong Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a counterfactual target-reconstruction method for multimodal on-policy distillation, directly addressing the source-mixing problem in teacher corrections and improving fine-grained visual reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28590)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Huihao Jing, Haozhe Cui, Wenbin Hu, Shaojin Chen, Haochen Shi, Changxuan Fan, Yuxuan Liu, Hanyu Yang, Sirui Zhang, Ziyi Chen, Haoran Li, Yangqiu Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a staged reward design for code generation that combines execution progress and relative efficiency, directly advancing RL for LLMs with a novel reward function.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27271)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yuran Wang, Zekun Wang, Bohan Zeng, Ruixu Zhang, Wenxuan Liu, Liu Yang, Yifan Dai, Yang Shi, Bozhou Li, Chengzhuo Tong, Daili Hua, Yuanxing Zhang, Wentao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Flux-OPD, a novel on-policy distillation paradigm that uses evolving contexts as in-training supervision with a theoretical decomposition of the reverse KL objective to stabilize targets and downweight conflicts, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28022)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yongjian Guo, Wanlun Ma, Lingyu Shen, Xi Xiao, Sheng Wen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a routing-based on-policy distillation framework that models distribution divergence for robust LLM safety realignment, directly addressing template robustness and capability preservation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27081)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou, Yan Zhan, Weiqi Tan, Zhiqiong Lu, Zhengping Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a closed-loop visual feedback RL framework for image-to-SVG generation, using a Diff-Map residual signal and agentic RL to enable self-correction, directly advancing RL-for-LLMs with a novel reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27699)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ken Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a sampling-time LoRA scaffold that recovers RL gradients on zero-reward cliff prompts, directly improving RLVR for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27787)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haodong Zhu, Yangyang Ren, Yanjing Li, Sheng Xu, Haiguang Liu, Linlin Yang, Baochang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a Kalman-filter-based dynamic prompt selection method for RL finetuning that adapts to policy drift and improves rollout efficiency, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27610)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hanzuo Liu, Xuan Qi, Chunyu Liu, Haotian Zhong, Yulong Wang, Rayying, Key, Alex Lamb, Mingyu Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a latent-reasoning-inspired memory architecture that caches intermediate-layer states and recomputes upper layers, achieving efficient long-context memory with self-distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28263)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Qixun Wang, Yang Shi, Letian Cheng, Zhuoran Zhang, Yan He, Yuqi Tang, Qi Zhang, Xinlei Yu, Ruizhe Chen, Tianrun Xu, Yuanxing Zhang, Pengfei Wan, Haotian Wang, Xianghua Ying

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel RL framework with Necessity-Aware Adaptive Reward and Hint-Guided Capability Expansion to improve adaptive tool use in agentic visual reasoning, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28595)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yanning Hou, Haoyuan Chen, Sihang Zhou, Xiaoshu Chen, Xirui Liu, Duanyang Yuan, Lingyuan Meng, Quan Liu, Jian Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Redesigns the policy-environment interface for RL search agents with a graph-structured action space and structured credit assignment, directly improving RL training for LLM agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27652)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Bum Jun Kim, Kohei Hayashi, Shunsuke Kamiya, Masanori Koyama, Yusuke Iwasawa, Yutaka Matsuo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel latent reasoning architecture (SCSE) for looped transformers that reconciles input conditioning with reference-preserving shared recurrence, directly advancing latent CoT/reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27656)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Iliya Mirzaei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a rigorous controlled comparison showing that self-refine/reflexion methods underperform repeated sampling at equal token cost, directly informing RL-for-LLMs and on-policy distillation design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28576)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuang Liang, Haoyang Zhou, Yifan Gong, Guowei Wang, Xiting Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a latent-guided prompt sampling method for RLVR that balances exploration and exploitation, directly improving RL training efficiency for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28077)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Peiyu Hu, Siying Gu, Weihai Lu, Zhuodong Liu, Yuntian Tang, Jiahao Liang, Yiying Xie, Jiang Rong, Zhaokai Luo, Zhiyong Wang, Jia Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a hierarchical latent reasoning framework with layer-aware process rewards for LLM-based recommendation, directly advancing latent reasoning with a new training objective.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27760)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoqing Wang, Xingrun Xing, Wei Xia, Ziheng Li, Yehui Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a multi-agent self-judging framework with a helpful-tool-ratio reward scaling to improve tool-use faithfulness in VLMs via SFT+RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28225)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu, Shudong Liu, Zhan Su, Zhuojian Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a transition-aware policy optimization framework that adds action-conditioned next-observation prediction supervision to RL for LLM agents, directly improving policy learning with dense environmental feedback.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27973)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Antyabha Rahman, Akshaj Gurugubelli, Omar Ankit, Kevin Zhu, Aishwarya Balwani

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides mechanistic evidence that RL fine-tuning creates more linearly separable and hierarchical representations than SFT, directly informing RL-for-LLM training design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26119)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Efstratios Zaradoukas, Davide Gabrielli, Bardh Prenkaj, Gjergji Kasneci

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes new reward functions (exponential and PageRank-inspired) for RLVR-based machine unlearning, directly advancing reward design for RL-based LLM post-training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27968)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shreyas Subramanian, Mecit Gungor, Vikram Elango

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a GRPO-based RL training recipe for a small language model that shows emergent attribution without explicit reward engineering, directly advancing RL-for-LLMs with a novel reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.27506)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Darsha Udayanga, Pin-Yu Chen, Payel Das, Qiang Ji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO-based RL to train VLMs to reason about AI edits, using simple accuracy and format rewards, directly advancing RL-for-LLMs with a novel application.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28464)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Amol Khanna, Manu Nandan, Cristian Viorel Popa, Joan Pujol-Roig, Diana Bolocan, Laura Vasilie, Alexandru Apostu, Chase Helwig, Mihaela Gaman, Michael Brautbar, Edward Raff, Chase Midler, Sven Krasser

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly combines RL with verifiable rewards and self-training for a reasoning-enabled triage classifier, with a novel calibrator for confidence estimation, strongly matching RL-for-LLMs and on-policy distillation criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28460)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tiangang Li, Xiangbo Tian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new reward-guided RL post-training method (HARGO) with confidence-modulated advantage weighting for heterogeneous tasks, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.28301)

---

