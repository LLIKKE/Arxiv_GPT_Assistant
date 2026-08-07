# 💡 今日研究速览 (Daily Summary)

### RL for LLMs

A significant trend this cycle is the push toward denser, more informative reward signals for reinforcement learning in LLMs. Rather than relying solely on sparse outcome rewards, researchers are developing methods to construct richer training signals. This includes ranking-based constructions that unlock the potential of generative reward models (RRC), evidence-oriented turn-level credit assignment for search agents (CIPO), and trajectory-level optimization that jointly refines both code generation and critique sequences (RA-CAD). Another key direction is the incorporation of cost-awareness and external-state optimization into policy learning, as seen in frameworks that co-optimize runtime harnesses for long-horizon agents (EvoHarness-RL). For social intelligence, we see the emergence of variance-gated, utterance-level goal rewarding within hierarchical RL frameworks to improve dialogue outcomes. These works collectively move beyond simple scalar rewards toward structured, multi-faceted feedback that can guide agents through complex, multi-step tasks.

### On-Policy Distillation and Self-Improvement

The dominant theme today is the maturation of on-policy self-distillation as a primary mechanism for LLM post-training. A family of new methods tackles the core challenge of generating high-quality training signals without external supervision, using self-consistency voting (On-Policy Self-Distillation), divergence-adaptive supervision horizons (DASH), and recursive self-distillation for turn-level credit (AgentOPSD). Beyond these core improvements, the field is expanding in scope and sophistication. We see adaptations for multilingual reasoning that use reasoning pivots to guide transfer (RP-OPSD), and for specialized domains like math, where the probability gap between a teacher and its base model defines a new, effective distillation objective (OPD²). The concept of "distillation" is also being broadened: from distilling skills from external knowledge sources (Search2Skill) and oracle-conditioned policies for robust tool use, to using privileged next-screenshot information for GUI agents (Gated Hindsight Distillation). A particularly interesting development is the use of weak models to diagnose and correct reasoning bugs in strong models (Woodpecker Distillation), and the investigation into the hidden mechanisms of subliminal learning, which reveals how non-semantic information can be transferred via weight noise and steering vectors, a critical consideration for auditing these pipelines. Safety and reliability are also being integrated into the self-improvement loop, with verifier-based gating to prevent skill contamination and circuit-anchored evolution to preserve safety during capability improvement. This collective work demonstrates a clear trajectory toward more autonomous, robust, and safe self-improvement algorithms.

### Reasoning and Latent Representations

A major architectural trend is the move beyond chain-of-thought to latent and hierarchical reasoning paradigms. Hierarchical Latent Prediction (HiLP) offers a new architecture that mitigates error accumulation in latent-space rollouts, improving long-horizon performance. For multimodal tasks, ChronoVision introduces latent state reconstruction via a dedicated visual head, coupling it with implicit process grounding for temporal reasoning. In the context of diffusion LLMs, researchers have identified a "commitment order" pathology and proposed a frontier-gated intervention to recover reasoning capabilities without sacrificing parallel decoding. Finally, the integration of retrieval feedback into chain-of-thought generation, trained via retrieval-oriented RL, highlights a novel way to ground reasoning in external evidence for multimodal retrieval tasks.

### Post-Training Optimization and Synthesis

Beyond RL and distillation, we see innovation in the underlying optimization and synthesis strategies. Evolution strategies are being enhanced with subspace-based descent direction merging (Hyper-ES), providing a gradient-free alternative for post-training. For long-horizon terminal tasks, a recursive verified synthesis framework combines rejection-sampled SFT with agentic PPO to achieve significant performance gains. Finally, the concept of scaffold-mediated post-training introduces a co-evolution loop where procedural scaffolds and model parameters are jointly optimized through discovery, distillation, and recompilation, blurring the lines between external tools and internalized skills.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a critic-free recursive self-distillation method for turn-level credit assignment in agentic RL, directly advancing on-policy distillation and RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05987)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yijiang Li, Bingyang Wang, Yijun Liang, Yunjie Tian, Di Fu, Nuno Vasconcelos

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a fully unsupervised on-policy self-distillation method that uses self-consistency voting to construct pseudo-solutions and distills them into the model's own incorrect completions, directly advancing on-policy distillation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06296)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: ZhiYan Hou, Xinyu Tang, Hongyan An, Jianjin Zhang, Weizhen Wang, Yunyun Han, Gengsheng Li, Xiangzhao Hao, Haiyun Guo, Wenbin Hu, Jinqiao Wang, Yafeng Deng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces DASH, a divergence-adaptive supervision horizon method that improves on-policy self-distillation for reasoning models by adapting token-level weights to the temporal structure of divergence sequences.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06243)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chang Shi, Tim Pearce, Manan Tomar, Siddhartha Sen, John Langford

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Hierarchical Latent Prediction (HiLP), a new latent reasoning architecture that reduces error accumulation in latent-space rollouts and improves long-horizon reasoning and coding benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05806)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xinye Wang, Junxiao Liu, Shujian Huang

**机构**: Nanjing University

**💡 亮点 (Highlight)**: Introduces a reasoning-pivot-guided on-policy self-distillation method that explicitly prioritizes critical reasoning signals for multilingual transfer, directly advancing on-policy distillation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06347)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yu Gu, Zhi Zheng, Yunpeng Ba, Xialiang Tong, Mingxuan Yuan, Zhenkun Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a subspace-based evolution strategy that merges gradient-derived descent directions for LLM reasoning, directly improving RL-free post-training optimization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05541)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, Xiaoyang Hao, Yuxin Gao, Tianhua Zhou, Xiaojia Chang, Tongran Liu, Jingbo Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a ranking-based reward construction method that enables generative reward models to provide effective RL training signals, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06310)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ethan Hadley, Eren Gultepe

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates subliminal learning as non-semantic distillation, revealing weight-noise and steering-vector mechanisms that enable hidden bias transfer, with implications for auditing on-policy distillation pipelines.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05734)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yifan Shen, Jian Xu, Boyi Li, Yuner Zhang, Tianjiao Yu, Bingxuan Li, Houze Yang, Rushi Wang, Xu Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces latent state reconstruction via a Reconstructive Visual Head and RL with implicit process grounding, directly advancing latent reasoning for multimodal temporal tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05631)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Linfang Shang, Ming Xu, Yiding Sun, Tianle Xia, Lingxiang Hu, Lan Xu, Ning Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a verifier-based gating mechanism to prevent skill contamination in self-evolving agents, directly addressing on-policy distillation and self-improvement loops.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05810)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Shuhao Yan, Changhao He, Xi Peng, Peng Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a state-aware text-to-CAD agent with a Generate-Execute-Critique-Rewrite loop, using trajectory-level GRPO to optimize both code and critique sequences, directly advancing RL-for-LLMs with a novel reward design and learnable critique mechanism.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05714)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhongzhi Li, Yucheng Shi, Zongxia Li, Ruhan Wang, Anhao Li, Zixun Huang, Junyao Yang, Lei Ke, Ninghao Liu, Haitao Mi, Leowei Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a recursive verified synthesis framework for long-horizon terminal tasks, with rejection-sampled SFT and agentic PPO training that directly improves LLM reasoning and task performance, strongly matching RL-for-LLMs and on-policy distillation criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05466)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zelong Sun, Jun Wang, Kaicheng Yang, Tiancheng Gu, Ziyong Feng, Zhiwu Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces retrieval-centric CoT generation conditioned on retrieval feedback, trained with retrieval-oriented RL, directly advancing RL-for-LLMs and latent reasoning in multimodal retrieval.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06060)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jewon Yeom, Jaewon Sok, Seonghyeon Park, Jeongjae Park, Hwiyeong Lee, Taesup Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a reasoning pathology in masked diffusion LLMs and proposes a frontier-gated commitment intervention that recovers reasoning performance while preserving parallel decoding, directly advancing latent/ordered reasoning mechanisms.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05687)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yan Liu, Jie Fu, Tsung-Yi Ho

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Circuit-Anchored Evolution, a novel safety-preserving self-evolution method for LLMs that anchors a causally identified safety circuit during RL-style evolution, directly addressing safe capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05158)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xingyu Guo, Wei Chen, Linlin Yang, Baochang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an evidence-oriented RL framework (CIPO) with dense turn-level credit for evidence use, directly improving LLM search-agent reasoning via a new reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06128)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Fei Ding, Yongkang Zhang, Runhao Liu, Yuhao Liao, Zijian Zeng, Huiming Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces scaffold-mediated post-training where procedural scaffolds co-evolve with model parameters via discovery, distillation, and recompilation, directly addressing on-policy distillation and skill internalization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05156)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xiaoqing Wu, Xingyu Fan, Feifei Li, Wenhui Que

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an on-policy distillation method that transfers an oracle-conditioned teacher policy to a student observing polluted histories, directly improving tool-use reliability under misleading multi-turn contexts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06057)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Weiwei Li, Junzhuo Liu, Tong Chu, Hengfu Yu, Wen Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Gated Hindsight Distillation, an on-policy distillation method using privileged next-screenshot information to improve GUI agent training, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.06065)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xuying Ning, Dongqi Fu, Tianxin Wei, Hanqing Zeng, Yuanchen Bei, Bingxuan Li, Zihao Li, Qifan Wang, Xiang Shen, Yifan Wu, Jiayi Liu, Hong Li, Yinglong Xia, Xiangjun Fan, Hanghang Tong, Jingrui He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel RL-based framework (EvoHarness-RL) for learning runtime harness policies in long-horizon LLM agents, combining supervised fine-tuning with cost-aware GRPO to optimize external-state construction and coordination, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05446)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Muyang Ye, Tian Lan, Feihu Jiang, Yongshi Ye, Wuyunsiqin, Bin Zhu, Qianghuai Jia, Zhao Xu, Weihua Luo, Ye Wang, Jinyang Zhang, Longyue Wang, Lingfeng Bao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Search2Skill, a rubric-based RL framework that distills external knowledge into reusable skills for LLM agents, directly addressing on-policy distillation and RL-for-LLMs with a novel joint optimization of search and skill generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05245)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Dayu Wang, Jiaye Yang, Weikang Li, Jiahui Liang, Yang Li, Deguo Xia, Jizhou Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a weak-to-strong contrastive distillation framework that uses local interventions to correct reasoning bugs in strong models, directly advancing on-policy distillation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05168)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes On-Policy Delta Distillation (OPD^2), a new on-policy distillation objective using the probability gap between a post-trained teacher and its base model, showing improvements in multilingual math reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05802)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junzhuo Liu, Weiwei Li, Jun Ling, Peng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces state-matched routing and contextualized self-distillation to fix privileged guidance mismatch in on-policy multi-turn agent training, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05219)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaofeng Wang, Kakam Chong, Shuai Xiao, DeXin Kong, Qingyuan Tian, Chen Ju, Xu Yan, Shuai Zhao, Fei Huang, Rui Wang, Shuguang Han, jufeng chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a hierarchical RL framework with variance-gated rewards for social dialogue, directly improving LLM goal completion via a new reward design and training pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05832)

---

