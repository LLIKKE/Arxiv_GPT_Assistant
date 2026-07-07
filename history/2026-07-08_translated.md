# 💡 今日研究速览 (Daily Summary)

### On-Policy Distillation
A major wave of research is consolidating around on-policy distillation as a primary mechanism for transferring reasoning capabilities. Several works demonstrate that distilling from a teacher on the student's own trajectories is superior to static, off-policy data. Key innovations include methods to make this process more stable and efficient, such as using a proximal teacher with trust region constraints (TOP-D), leveraging replayed prefixes to avoid costly environment rollouts in multi-turn settings (ReOPD), and gating supervision based on verifier rewards (RG-OPD). A critical finding is that naive privileged self-distillation can degrade long reasoning traces, particularly around correction steps, highlighting the need for careful token-level signal management. The field is also moving toward heterogeneous and multi-teacher setups, enabling knowledge transfer from diverse, specialized models (H-OPD), and exploring self-distillation where the teacher is derived from the student's own denoising trajectory (dOPSD). A unifying theme is the use of forward-KL divergence to expand the student's support on hard prompts, directly improving downstream GRPO-based reasoning and agentic tasks (TREK).

### Reinforcement Learning for LLMs (RLVR & Agentic RL)
The dominant trend in RL for LLMs is the explosion of sophisticated reward design and credit assignment methods, moving well beyond simple outcome rewards. Process rewards are being systematically validated as superior to outcome rewards for reasoning, especially in small models, by improving trace fidelity. New reward structures include claim-level rubric rewards for dense video captioning, step-wise temporal process rewards for video reasoning, and neuro-symbolic verifiable rewards for long-video QA. For agentic tasks, the focus is on overcoming the sparse reward problem. Methods like RSPO use a reward-swap mechanism to combine dense process rewards with sparse outcome rewards, while STAPO introduces hierarchical group-based RL with trajectory-aware optimization to combat neglect. Continual learning is being addressed by frameworks like CPO, which uses parameter-movement regularization to prevent catastrophic forgetting. A notable sub-trend is the use of RL for non-verifiable tasks, such as instruction following, where an LLM tutor adaptively generates harder prompts to create a self-calibrating training signal, and for confidence calibration, where non-hackable reward schemes are proposed.

### Latent Reasoning & Inference-Time Computation
A paradigm shift is underway towards understanding and harnessing latent reasoning within LLMs. Research is revealing that structured hidden computation occurs even in "filler" tokens, and an unsupervised decoding pipeline has been introduced to read this internal state. This is being directly applied to compress explicit reasoning chains into fast, CoT-free student models (CritiqueDriveVLM) and to improve video reasoning through recurrent latent visual caches trained with contrastive alignment and GRPO. In the diffusion LLM space, joint token commitment mechanisms (CoCommit) are being developed to reduce factorization error, improving the quality of latent generation. This direction challenges the assumption that all reasoning must be explicit and opens the door to more efficient, interpretable models.

### Multimodal & Embodied Reasoning
Multimodal RL is maturing, with a strong emphasis on unifying reasoning across modalities. A key proposal is to frame interleaved text-image reasoning as a unified MDP, enabling joint policy gradient optimization with dense VLM-judge feedback. For embodied agents, faithfulness in reasoning is being directly optimized by using a learned faithfulness critic as a dense RL reward. In the autonomous driving domain, a three-stage framework combines verifier-guided multi-turn RL with latent thought distillation to bridge slow and fast reasoning. The integration of visual and symbolic reasoning is also being explored, such as using an SVG world for multi-turn RL-based iterative refinement, demonstrating the breadth of application for these techniques.

### Alignment & Safety
The alignment landscape is seeing advances in both data efficiency and safety optimization. A significant theoretical contribution provides unbiased loss functions that mathematically correct for noise in preference data, enabling direct training from noisy datasets without clean supervision. For safety, a multi-stage RL framework (Oyster-II) specifically addresses the challenges of safety generalization and CoT over-generalization. Inference-time alignment is being formalized through a Lagrangian dual framework that augments rewards to strictly enforce safety constraints, improving the helpfulness-harmlessness tradeoff. Other work focuses on selective prediction, using RL to directly optimize for metrics like AURC to make models more reliable when they choose to abstain from answering.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Qixiang Yin, Huanjin Yao, Yuchen Cai, Jianghao Chen, Ziyi Wang, Min Yang, Fei Su, Zhicheng Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a confidence-aware heterogeneous multi-teacher on-policy distillation framework for multimodal reasoning, directly advancing on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02592)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Baohao Liao, Hanze Dong, Christof Monz, Xinxing Xu, Li Dong, Furu Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ReOPD, a novel on-policy distillation method for multi-turn agentic tasks that uses replayed prefixes to avoid costly environment interactions while addressing the prefix trap distribution shift.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04763)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Phuong Tuan Dat, Qi Li, Xinchao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces dOPSD, a novel on-policy self-distillation method for diffusion LLMs that derives teacher privilege from the student's own denoising trajectory, improving reasoning without external labels.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04428)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhengpeng Xie, Li Lyna Zhang, Zeke Xie, Mao Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Trust Region Policy Distillation (TOP-D), a new on-policy distillation method that stabilizes training via a proximal teacher, with theoretical convergence guarantees and strong empirical results on math reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04751)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yuanda Xu, Zhengze Zhou, Kayhan Behdin, Jelena Markovic-Voronov, Hejian Sang, Xiaomin Li, Wenhui Zhu, Xinchen Du, Aida Rahmattalabi, Ran He, Sen Na, Zhipeng Wang, Alborz Geramifard

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TREK, a staged distillation-then-RL method that uses forward-KL to expand the student's on-policy support for hard prompts, directly improving GRPO-based reasoning and agentic task performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05339)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shiyuan Feng, Huan-ang Gao, Haohan Chi, Hanlin Wu, Zhilong Zhang, Zheng Jiang, Bingxiang He, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Direct On-Policy Distillation (Direct-OPD), a novel method that transfers the policy shift from a weak teacher's RL run to a strong student via implicit reward from log-ratios, enabling efficient weak-to-strong generalization without explicit reward models or expensive RL on the target model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05394)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhaohong Liu, Hao Ye, Xianlin Zhang, Mengshi Qi

**机构**: Beijing University of Posts and Telecommunications

**💡 亮点 (Highlight)**: Proposes a unified three-stage framework combining verifier-guided multi-turn RL for LLM reasoning and latent thought distillation to compress reasoning into a fast, CoT-free student, directly advancing RL-for-LLMs and latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04179)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Mohammad Sadegh Akhondzadeh, Vijay Lingam, Atula Tejaswi, Chanakya Ekbote, Sujay Sanghavi, Aleksandar Bojchevski

**机构**: University of Copenhagen (UoC)

**💡 亮点 (Highlight)**: Introduces RG-OPD, a novel on-policy distillation method that uses verifier rewards to gate teacher logit supervision, improving student reasoning and coding performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04037)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Simran Kaur, Narutatsu Ri, Yinghui He, Liam Fowl, Sanjeev Arora

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a critical failure mode in privileged self-distillation for thinking models, showing it degrades long reasoning traces, and links this to token-level signal around correction steps, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05184)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Harsh Goel, S P Sharan, Sahil Shah, Minkyu Choi, Joungbin An, Kristen Grauman, Sandeep P. Chinchali

**机构**: University of Texas at Austin

**💡 亮点 (Highlight)**: Proposes a neuro-symbolic verifiable reward for RL post-training of vision-language models on long-video QA, directly matching RL-for-LLMs with a novel reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02959)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Kangheng Lin, Jisheng Yin, Dingming Li, En Yu, Yana Wei, Han Zhou, Liang Zhao, Hongyu Zhou, Hongbo Peng, Jianjian Sun, Zheng Ge, Xiangyu Zhang, Daxin Jiang, Jingyu Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a visual-symbolic reasoning paradigm with a think-with-SVG pipeline and multi-turn RL for iterative refinement, directly contributing to RL for LLMs and latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03530)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yongheng Zhang, Zhipeng Xu, Hao Wu, Yinghui Li, Di Yin, Xing Sun, Philip S. Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a recurrent latent visual cache for video reasoning LMMs, trained with contrastive alignment and GRPO with a latent grounding reward, directly advancing latent reasoning for multimodal models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02607)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhilong Zhang, Hongli Yu, Huan-ang Gao, Hanlin Wu, Yuxuan Song, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a post-hoc spectral editing method (SAR) that extracts reasoning-effective components from RL-based LLM updates, improving reasoning and multi-domain performance with minimal parameters.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03065)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jakob Hartmann, James Harvey, Jhonathan Navott, Erik Y. Wang, Luckeciano C. Melo, Flaviu Cipcigan, Cheng Zhang, Alessandro Abate

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces ASIG, a fine-tuning approach that amortises Bayesian Experimental Design into LLM policies via multi-turn GRPO with an Expected Information Gain reward, directly improving sequential information gathering.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03426)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yujin Kim, Namgyu Ho, Sangmin Hwang, Joonkee Kim, Yongjin Yang, Sangmin Bae, Seungone Kim, Jaehun Jung, Se-Young Yun, Hwanjun Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework for non-verifiable instruction following where an LLM tutor adaptively generates harder prompts via atomic constraints, creating a self-calibrating training signal.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04412)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Kaley Brauer, Claudio Mayrink Verdun, Samuel Marks

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies latent reasoning by showing that filler tokens host structured hidden computation, and introduces an unsupervised decoding pipeline to read it, which is a central contribution to latent reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03502)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jiaqi Deng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a causal 'wrong-dip' in LLM internal representations and proposes a mid-layer LoRA fine-tuning penalty that reduces this dip and improves compression robustness, directly contributing to RL/alignment for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04640)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zefeng Wang, Minxi Yan, Jinhe Bi, Sikuan Yan, Volker Tresp, Yunpu Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a recursive two-timescale meta-skill evolution framework for LLM agents that self-improves both task skills and the improvement procedure itself via on-policy distillation from execution traces.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05297)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zican Hu, Xuyang Hu, Yiming Liu, Zuwei Long, Wei Liu, Yunzhuo Hao, Jiawei Gu, Linjie Li, Yu Cheng, Zhenhong Sun, Weibo Gu, Xing Sun, Zhi Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified MDP formulation for RL over interleaved text-image reasoning, enabling joint policy gradient optimization across modalities with dense VLM-judge feedback.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03748)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xinqi Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces MR-GRPO, a class-conditioned reward for GRPO that improves counterfactual normative reasoning in LLMs via solver-verified environments and on-policy RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03957)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Anagha Radhakrishna Palandye, Rebecca Glick, Osheen Kaul

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically compares process vs outcome reward granularity in RLVR for small LLMs, showing process rewards substantially improve reasoning accuracy and trace fidelity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02869)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziwei Ye, Peter Vickers

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a verifiable reward RL recipe (RLVR with GRPO) for adapting audio-language models to code-switched ASR, combining error rate and script fidelity rewards with a two-pass draft-and-refinement procedure.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02757)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiang Liu, Taian Guo, Ruizhi Qiao, Xing Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Reward-Swap Policy Optimization (RSPO), a new RL method for multi-turn LLM agents that uses a reward-swap mechanism to leverage dense process rewards while maintaining consistency with sparse outcome rewards, improving convergence and performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04713)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junze Ye, Jiayi Cheng, Miao Lu, Michal Mankowski, Jose Blanchet, Mohsen Bayati

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Frames on-policy data construction for agent post-training as a budget-allocation problem, showing that few teacher steps at learner-induced contexts outperform longer or filtered alternatives.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04574)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shengyi Hua, Kangzhe Hu, Conghui He, Xiaofan Zhang, Shaoting Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies RL with verifiable rewards to train LLMs for iterative evidence-seeking diagnostic reasoning, introducing a novel reward suite and a high-fidelity examination simulator.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02983)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiuyi Qi, Tian Liang, Mutian Bao, Jinjian Zhang, Dongnan Liu, Wei Zhou, Linjian Mo, Ming Kong, Jie Liu, Feng Zhang, Qiang Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes STAPO, a hierarchical group-based RL framework for LLM agents that uses normalized entropy to detect and optimize trajectory neglect via a joint reward-penalty mechanism, directly advancing RL for LLMs with a new reward design and training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04963)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chee Heng Tan, Zhuoyi Lin, Mehul Motani, Wee Sun Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes non-hackable confidence reward schemes for RL-based confidence calibration in LLMs, directly addressing reward design for RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04332)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mao-Lin Luo, Zhe-Xu Wang, Zi-Hao Zhou, Bo Ye, Jian Zhao, Min-Ling Zhang, Tong Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Continual Policy Optimization (CPO), a replay-free RL framework with a theoretically justified parameter-movement regularization to mitigate catastrophic forgetting in continual post-training of vision-language models, directly addressing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04364)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zichao Li, Gang Wu, Zichao Wang, Ruiyi Zhang, Wanrong Zhu, Ryan A. Rossi, Vlad I Morariu, Jihyung Kil

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Hindsight Supervised Learning (HSL), an on-policy distillation method that relabels agent trajectories with achieved goals for additional fine-tuning, improving SFT and DPO.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04235)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yaswanth Chittepu, Ativ Joshi, Sohini Chintala, Scott Niekum

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a principled Lagrangian dual framework for inference-time alignment with safety constraints, introducing a calibrated augmented reward that improves the helpfulness-harmlessness tradeoff in both sequence-level and token-level decoding methods.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02781)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Weiyang Guo, Zesheng Shi, Longhui Zhang, Zeen Zhu, Min Zhang, Jing Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-feedback retry framework for LLM agents that uses pivotal-aware credit assignment and local retry to improve experience exploitation, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03702)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mingxuan Fan, Peiyang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new step-level group RL method for LLM agents that uses rollout-based state potentials for credit assignment, directly improving RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04242)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Gaoxiang Luo, Yifan Wu, Sinian Zhang, Aryan Deshwal, Ju Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based alignment framework (RLSR) that directly optimizes selective prediction metrics (AURC) for LLMs, introducing a new reward design and training objective for reliability.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03528)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Handong Li, Longteng Guo, Zikang Liu, Dongze Hao, Yepeng Tang, Zijia Zhao, Jie Jiang, Zhiwei Jin, Chen Chen, Haonan Lu, Jing Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a step-wise temporal process reward for RL-based video reasoning, directly advancing RL-for-LLMs with a new reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05089)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Niu Lian, Alan Chen, Zhehao Yu, Chengzhen Duan, Fazhan Liu, Hui Liu, Pei Fu, Jian Luan, Yaowei Wang, Shu-Tao Xia, Jinpeng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes UI-MOPD, a multi-teacher on-policy distillation method for continual learning in GUI agents, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04425)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Matthew Foutter, Matteo Cercola, Lena Wild, Yunshan Wang, Michelle Li, Daniele Gammelli, Marco Pavone

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a learned faithfulness critic used as a dense RL reward for post-training embodied VLA policies, directly contributing a new reward design and RL pipeline for LLM-based reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04681)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Eric Lei, Hsiang Hsu, Chun-Fu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Best-of-Better-N, an in-context learning framework that shifts the sampling distribution toward high-reward regions via retrieval and restyling of high-reward examples, directly improving inference-time alignment for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03453)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, Boxin Wang, Zihan Liu, Sungwon Kim, Yang Chen, Arushi Goel, Rajarshi Roy, Wenliang Dai, Zhuolin Yang, Yangyi Chen, Dongfu Jiang, Sreyan Ghosh, Tuomas Rintamaki, Andrew Tao, Jonathan Raiman, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping

**机构**: NVIDIA

**💡 亮点 (Highlight)**: Proposes multi-domain on-policy distillation as a key training stage for a unified audio-text LLM, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05196)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Raj Jaiswal, Dhruv Jain, Rishabh Dhawan, Sree Krishna Uppalapati, Shin'ichi Satoh, Tanuja Ganu, Rajiv Ratn Shah

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a step-level reward framework with structured feedback and policy gradient for correcting reasoning errors in small language models, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05199)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yujiang Li, Zhenyu Hou, Yi Jing, Jie Tang, Yuxiao Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CompactionRL, a novel RL training strategy for long-horizon agentic LLMs that jointly optimizes task execution and context-compaction summary generation, directly improving RL for LLMs with a new reward/optimization design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05378)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu Li, Xiuyu Li, Mingyang Yi, Jiaxing Wang, zhangliangxu, Zhaolong Xing, Zhen Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Selective Importance Sampling (SIS), a plug-in method that uses token-level rejection sampling to turn off-policy tokens on-policy for RL post-training of LLMs, reducing variance and improving alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04728)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mingqi Gao, Hongyuan Dong, Yifei Chen, Zhisheng Zhong, Zheng Ruan, Wenjin Hou, Yu Chen, Han Hu, Yansong Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Claim-Level Rubric Rewards (CuRe), a structured reward framework for RL in dense video captioning that decomposes holistic evaluation into fine-grained claim-level verification, directly addressing reward design for LLM alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05150)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lin Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CoCommit, a marker-gated coordination pass for diffusion LLMs that approximates joint-mode decoding to reduce factorization error, advancing latent reasoning by improving token commitment without auxiliary models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04469)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haotian Zhou, Weiran Huang, Siqi Liu, Xiting Wang, Xin Zhang, Zhihao Wen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TR-RAG, a teacher-regularized RL recipe combining reward optimization with on-policy distillation on student-visited prefixes for cross-lingual RAG, directly addressing on-policy distillation and RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02966)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jialiang Wang, Xianming Liu, Xiong Zhou, Hui Liu, Haoliang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes unbiased reward model and DPO losses that mathematically correct preference noise, enabling direct training from noisy datasets without clean supervision.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03248)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a general-purpose verification framework using continuous scoring token logits that provides dense feedback for RL, improving sample efficiency of GRPO on reasoning benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.05391)

---

## 47. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiuyi Qi, Jinjian Zhang, Mutian Bao, Tian Liang, Guocong Li, Dongnan Liu, Wei Zhou, Jie Liu, Ming Kong, Linjian Mo, Feng Zhang, Qiang Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a constraint-aware RL framework (CARL) that uses a novel reward comparing output distributions under constrained vs unconstrained inputs to improve LLM planning, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.04854)

---

## 48. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiyang Guan, Yong Xie, Jun Chen, Jiexi Liu, Zipeng Ye, Defeng Li, Jiayu Shen, Jialing Tao, Hui Xue

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Oyster-II, a multi-stage RL framework for constructive safety alignment that addresses safety generalization and CoT over-generalization, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02914)

---

## 49. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Juan Diego Rodriguez, Jocelyn Zhang, Katrin Erk, Greg Durrett

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel frequency-corrected generator-validator consistency training objective that directly improves LLM alignment and performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.02668)

---

## 50. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zijun Xie, Yuyang You, Yongzhi Li, Enlei Gong, Zeyu Chen, Quan Chen, Yanhua Cheng, Peng Jiang, Yadong Mu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ACPO, a token-level credit assignment RL method for LLMs using a mode-local surrogate entropy to modulate policy updates, improving reasoning on math and coding benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.03126)

---

