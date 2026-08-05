# 💡 今日研究速览 (Daily Summary)

### RL for LLMs & Reasoning
A significant cluster of papers focuses on improving reinforcement learning for large language models (LLMs), particularly in reasoning tasks. A key theme is the move beyond monolithic outcome rewards toward more granular, process-level, or structure-aware credit assignment. **CausalOPD**introduces first-wrong-step supervision within a curriculum online process distillation framework, while**PAMT**applies step-level process rewards for multi-domain machine translation.**StructPO**internalizes multi-stage writing workflows via explicit stage tokens and fine-grained credit assignment. Another emerging direction is label-free RLVR, exemplified by**OM-GRPO**, which decouples reward estimation from policy optimization by masking answer-token gradients.**CVPO**and**Hi-TTRL**propose dynamic curricula and test-time reward shaping (via MCMC hints) to stabilize training and regulate exploration.**BODHI**provides a critical analysis, revealing that RLVR may reduce genuine inferential branching, while**When Correct Solutions Repeat**corrects structure-level credit concentration in GRPO.**SFT Conflicts, RL Coexists**offers theoretical grounding, showing RL induces sparse, orthogonal multi-task updates and proposing a decoupled training paradigm (**Parallel-RL**), while**Robust General Utility**introduces a minimax framework against reward misspecification for safety alignment. Finally,**DiagLoop**and**PBT/PGR**leverage self-generated data flywheels and probe-guided filtering to create more effective on-policy training signals.

### On-Policy Distillation
On-policy distillation (OPD) has emerged as a dominant paradigm for transferring knowledge from a teacher to a student policy, with a strong emphasis on mitigating off-policy drift and leveraging privileged information.**OPTD**directly tackles off-policy drift in few-step diffusion language models via consistency-guided adaptive compression.**Any-OPD**extends this to heterogeneous flow-matching models by bridging representation spaces, enabling cross-architecture teacher correction.**ReflectRL**and**TurnSight**introduce novel supervision sources: the former learns from golden negative trajectories via reflective reasoning, and the latter derives supervision from execution-conditioned hindsight in tool-integrated settings.**Rubrics as Privileged Information**shows that soft rubric-based PI outperforms hard reference PI for open-ended generation. The critical issue of teacher quality is addressed by**When Teachers Mislead**, which filters spurious token-level supervision based on input-groundedness.**SMOPD**tackles multi-reward settings via a specialize-and-merge strategy, and**Language-Specialized Multi-Teacher OPD**applies a similar multi-teacher concept to multilingual ASR.**Latent Reward Registers**(RG-OPD) bypass expensive rollouts by using latent reward registers for dense estimation, while**Stuck on "A"**diagnoses and repairs interface injury in attention-to-linear conversion using on-policy DPO.

### Latent Reasoning & Recurrent Architectures
A third major thrust is the development and analysis of latent reasoning—performing computations in a compressed hidden state space rather than in token space.**LatentGuard**compresses textual rationales into compact latent states for guard models, featuring a staged curriculum and an inspectable audit decoder.**LiLa-WAM**applies this to robotic manipulation with a lightweight latent world-action model. For architectural efficiency,**Maglev**proposes a recurrent Transformer with sliding memory and a memory consistency loss, while**LoopMTP**guides intermediate hidden states in a looped transformer via latent multi-token prediction.**PI-Mem**extends long-context reasoning to 3.6M tokens using a parallel-iterative memory mechanism optimized with RL.**The Ignition Is Real**provides a rigorous mechanistic analysis, confirming the reality of compositional ignition at the readout in recurrent-depth models, offering a pre-registered methodology for studying hidden-state reasoning.

### Multimodal & Generative Models
Advances in RL are also being applied to multimodal and generative domains.**GROW**introduces a group-relative advantage-weighted on-policy RL method for flow-matching text-to-speech, while**Video-DeepResearch**presents a two-stage (SFT + GRPO) training recipe for a multimodal deep-research agent, breaking the imitation-learning ceiling.**RAPO**proposes a dual-channel risk-aware RL fine-tuning framework for continual multimodal post-training, explicitly governing optimization risk.**LiLa-WAM**(also mentioned above) targets robotic manipulation, and**Language-Specialized Multi-Teacher OPD**applies distillation to LLM-based ASR. Finally,**SP3O** offers a reward-model-free, gradient-based RL algorithm for segment preferences, which is broadly applicable to long-horizon tasks including multimodal ones.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yuanshen Guan, Zipeng Feng, Zhiwei Xiong, Peiqin Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces latent reward registers for dense reward estimation in diffusion models and an on-policy distillation method (RG-OPD) that bypasses expensive rollouts, directly advancing RL-for-LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03929)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jian Zhang, Bingyi Wang, Yizhi Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a curriculum online process distillation framework with first-wrong-step supervision and short-horizon RL, directly targeting on-policy distillation for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03673)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces OM-GRPO, a label-free RLVR framework that decouples reward estimation from policy optimization by masking answer-token gradients, directly advancing RL for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03119)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Deepika Bablani, Ajay Gupta, Wanming Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces rubric-based privileged information for on-policy self-distillation, showing soft rubric PI outperforms hard reference PI and rubric-as-reward RL for open-ended generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02948)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xiaocheng Lu, Hualei Zhang, Shuhan Guo, Jie Zhang, Xiaoyi Pang, Jian Liu, Haoxi Li, Bohai Gu, Haoxuan Che, Jingcai Guo, Song Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an on-policy transition distillation method with consistency-guided adaptive compression for few-step diffusion language models, directly addressing the off-policy drift problem in distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02942)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ranxu Zhang, Guinan Chen, Chenshaodong, Jinghao Lin, Xiaozhou Xu, Sunzhe, Yanyong Zhang, Chao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel RL framework (ADRS) that uses self-distilled reward shaping with return-associated token-level credit assignment for LLM agents, directly advancing RL-for-LLMs with a new reward design and training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03223)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jinhe Bi, Chennan Zhou, Zengjie Jin, Aniri, Shuo Lu, Wenke Huang, Hu Cao, Xun Xiao, Zhihong Zhu, Volker Tresp, Fei Shen, Yunpu Ma, Tat-Seng Chua

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel on-policy distillation framework that learns from expert failure trajectories via reflective reasoning, directly improving LLM reasoning across multiple backbones and training methods.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03972)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yinuo Jiang, Yongjie Ye, Zhou Tao, Xiang Zhuang, Qiang Zhang, Huajun Chen, Tiankai Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a spurious-signal-aware on-policy distillation framework that filters misleading token-level supervision based on input-groundedness, directly improving OPD optimization for LLMs and VLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03632)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Changle Qu, Sunhao Dai, Hengyi Cai, Yuqi Zhou, Xinran Chen, Simon, Jun Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a turn-level hindsight self-distillation framework that derives on-policy supervision from execution-conditioned hindsight and adaptively modulates RL advantages, directly advancing on-policy distillation for tool-integrated reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04007)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Soumadeep Saha, Krish Sharma, Akshay Chaturvedi, Nicholas Asher

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a novel analysis of RLVR-trained LLMs using semantic tree extraction, revealing that RLVR reduces genuine inferential branching, which is a central contribution to understanding RL for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02867)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhinan Liu, Jie Li, Mingyu Kang, Jiayi Ji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces LatentGuard, a latent reasoning framework for guard models that compresses textual rationales into compact latent states, directly advancing latent CoT reasoning with a novel staged curriculum and inspectable audit decoder.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03838)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Guanrou Yang, Tian Tan, Qian Chen, Ziyang Ma, Yakun Song, Zhikang Niu, Qi Chen, Wenming Tu, Haitao Li, Shan Yang, Xie Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a group-relative advantage-weighted on-policy RL method for flow-matching text-to-speech, directly advancing RL-based training for generative models with a novel reward weighting scheme.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03215)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ronglong Bao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses and repairs interface injury in attention-to-linear conversion using on-policy DPO and distillation, directly addressing latent reasoning architecture efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02689)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Kejian Zhu, Zhuoran Jin, Shangqing Tu, Hongbang Yuan, Yushi Bai, Kang Liu, Juanzi Li, Jun Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical and empirical analysis showing RL induces sparse, orthogonal multi-task updates, and proposes Parallel-RL, a decoupled multi-task RL training paradigm.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03573)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yibei Liu, Jiajun Chen, Qianle Zhang, Tangyue Jin, Mengying Zhu, Meng Xi, Yangyang Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a dual-channel risk-aware RL fine-tuning framework (RAPO) that explicitly governs optimization risk in continual post-training of multimodal LLMs, directly advancing RL-for-LLMs with a new reward/update scaling mechanism.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03660)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Fan Yang, Yuting Su, Xiaobo Wang, Yuncheng You, Fugui Fan, Yuting Wu, Minghui Wu, Chenxu Zhao, JiaHong Ning, Peiguang Jing

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a lightweight latent world-action model with a compact latent reasoning space and a language-free task representation, directly advancing latent reasoning for control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03701)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Bo Liu, Qiang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a recurrent Transformer with sliding memory and a memory consistency loss that aligns decoder memories with full-attention targets, enabling latent recurrent computation for efficient inference.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02870)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Meicong Zhang, Tiancheng Su, Jiahao Cheng, Guoxiu He, Xinqi Tao, Dejia Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a struct-aware policy learning framework (StructPO) that internalizes multi-stage writing workflows into a single-pass policy via explicit stage tokens and fine-grained credit assignment, directly advancing RL-for-LLMs with a novel reward/policy design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03138)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jian Zhang, Bingyi Wang, Yizhi Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a counterfactual data flywheel with stage-localized reinforcement learning for diagnostic LLMs, directly advancing RL-for-LLMs and on-policy distillation via a novel self-improvement loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03674)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Evan Assmus, Qining Zhang, Lei Ying

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a reward-model-free, gradient-based RL algorithm for segment preferences, directly applicable to LLM finetuning and long-horizon tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.02951)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zixuan Liu, Fangzheng Wu, Brian Summa, Zizhan Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a robust general-utility RL framework with minimax training against utility misspecification, with convergence guarantees and experiments on LLM safety alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03562)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Dawei Liu, Haixu Song, Shuang Cheng, Shijie Wang, Haozheng Hou, Kaifeng Liu, Ermo Hua, Zhonghang Yuan, Zhijie Zhong, Yuchen Fan, Biqing Qi, Bowen Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a parallel-iterative memory mechanism for long-context reasoning, using RL with a turn-efficiency reward to optimize the reasoning process, directly advancing latent reasoning and RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03048)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Siming Fu, Zheming Fu, Ruizhe He, Hualiang Wang, Jie Huang, Xiaoxiao Ma, Mingchen Zhong, Weihu Huang, Xiaoxuan He, Haojun Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel on-policy distillation framework for heterogeneous flow-matching models, bridging representation spaces to enable teacher correction of student outputs across different architectures.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03316)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Simon Lam-Muir

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a rigorous mechanistic analysis of latent reasoning in a recurrent-depth model, confirming the reality of compositional ignition at the readout and offering a pre-registered methodology for studying hidden-state reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03263)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Behzad Shomali, Markus Frey, David Berghaus, Joachim Koehler, Mehdi Ali

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a looped transformer with latent multi-token prediction supervision, directly advancing latent reasoning architectures by guiding intermediate hidden states across loops.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03624)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuan Xie, Jiaqi Song, Xianliang Wang, Ming Lei, Jie Gao, Jie Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a language-specialized multi-teacher on-policy distillation framework with RL-optimized teachers and token-level distillation, directly advancing on-policy distillation for LLM-based ASR.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03610)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziqi Jia, Yalu Ouyang, Bo Pang, Panpan Li, Hangfei Xu, Shengzhao Wen, Shiyong Li, Yanpeng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a value-variance-aware advantage adjustment and dynamic curriculum for RL-based LLM reasoning, directly improving exploration and training stability.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03068)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhen Fang, Yu Zeng, Wenxuan Huang, Yiming Zhao, Shiting Huang, Tianfei Ren, Qi Lu, Qingnan Ren, Qisheng Su, Lionel Z. Wang, Qingyu Yin, Shuang Chen, Zehui Chen, Lin Chen, Zhenfei Yin, Yao Hu, Shaohui Lin, Wanli Ouyang, Shaosheng Cao, Feng Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a two-stage training recipe (SFT + GRPO) for a multimodal deep-research agent, directly applying RL to improve tool-augmented reasoning and breaking the imitation-learning ceiling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03979)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhe Cao, Miaowen Wen, Fangjiong Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a rarity-aware credit redistribution rule for GRPO that corrects structure-level credit concentration in RLVR, improving repeated-sampling performance on competition math.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03467)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guoyao Yu, Xiaoqing Sun, Ziqi Huang, Shaojing Fan, Zhongyi Zhang, Xiaomeng Hu, Xiaobo Xue, Yangyang Shi, Xiong Xiao, Yang Song, Biao Lyu, Rong Wen, Xing Li, Qinming He, Shunming Zhu, Zhenguang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a probe-guided framework (PBT/PGR) that uses hidden-state correctness signals to filter self-generated tool-call data for fine-tuning and to rerank candidates at inference, directly contributing to on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03071)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wen Wang, Jiahua Bao, Tu Yongsiqi, Yihao Liu, Haotian Zhou, Haoxuan Ma, Mengyu Zhou, Wenkui Fan, Junwei He, Xiaoxi Jiang, Guanjun Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a specialize-and-merge online policy distillation method for multi-reward RL, directly addressing reward balancing and combining teacher capabilities into a student policy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03092)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a process-aligned RL framework with step-level process rewards for multi-domain machine translation, directly addressing credit assignment in RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03077)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kunbin Xu, Xingzuo Li, Xuefeng Bai, Kehai Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a test-time RL framework that regulates consensus strength via MCMC hints, directly improving LLM reasoning through a novel reward/advantage shaping mechanism.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.03545)

---

