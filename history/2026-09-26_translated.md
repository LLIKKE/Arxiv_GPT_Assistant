# 💡 今日研究速览 (Daily Summary)

### World Models & Predictive Planning

The day's most striking result may be the simplest: *Aim Short to Reach Far* shows that frozen visual world models plan better when scored toward retrieved intermediate observed targets rather than the final goal — a reminder that how we query a model can matter more than what we train. This insight threads through a cluster of papers refining the world-model recipe along three axes. First, **what to predict**: *DeltaWAM* and *Streaming-WAM* replace dense future-frame prediction with sparse visual deltas and committed action prefixes, cutting cost while improving bimanual and asynchronous manipulation. Second, **what the latent must preserve**: *AD-WM* regularizes joint-embedding dynamics with inverse-dynamics and action-recovery objectives so that counterfactual action differences survive in latent space, while *Beyond Compression* demonstrates that reconstruction-only latents are fundamentally ill-suited to long-horizon rollout, and that Koopman structure plus noise injection and multi-step fine-tuning repairs them. Third, **robustness and scale**: *DAWN* bakes depth-denoising and contrastive alignment into the model for zero-shot quadruped parkour, *Visual Representation and History Modeling* systematically ablates visual encoders and introduces cached linear attention for long-context navigation, and *HelloWorld* scales a controllable 2B driving world model with block-causal generation and few-step distillation. Complementing these, *OCC4M* and *Underwater C3-JEPA* push object-centric, persistent memory for long-horizon reasoning under real-world lag and viewpoint change. Notably, *Do World Models Make Better Robots?* surveys 160 benchmarks and proposes advantage-aware metrics to isolate whether predictive models actually beat direct VLA policies — a question the field has largely assumed rather than measured.

### Agents & Embodied Reasoning

A distinct thread concerns the agent harness around the policy rather than the dynamics model itself. *World Action Agent* gives VLM-driven manipulation a world-model-style rehearsal loop, previewing actions in a visual workspace before execution, while *AquaMend* addresses latent-belief failures through minimal re-probing and conditional rollback — a decision-theoretic complement to learned dynamics. *ActGaze* derives action-grounded gaze supervision from counterfactual visual interventions to sharpen VLA attention for high-precision tasks, and *STRAND* builds an object-centric spatio-temporal monitoring benchmark that exposes persistent-tracking weaknesses in video LLMs while yielding transferable representations. On the training side, *Uncertainty-Gated Exploration Noise* identifies and mitigates task collapse during online RL fine-tuning of flow-matching VLA policies. Finally, *GPT-6-Astra Lights Up Embodied Navigation* offers zero-shot continuous vision-and-language navigation evidence, suggesting foundation models are becoming credible navigation planners even absent bespoke dynamics training.

### Multimodal Generation & Reinforcement Learning

Generative modeling advances concentrated on post-training and controllability. *AV-GRPO* introduces modality-anchored decoupled diffusion RL, improving joint audio-video quality, text alignment, and cross-modal synchronization — a sign that GRPO-style preference optimization is migrating from LLMs into multimodal diffusion. *WanPE* applies the same family of ideas to prompt enhancement, training a large cinematic planner with semantic-consistency GRPO for long-horizon text-to-video. On the 4D reconstruction front, *WildHSR* delivers feed-forward metric people-scene reconstruction from monocular video via a 3D foundation model, relevant to spatio-temporal scene dynamics though not generative video per se. Two narrower contributions round out the category: *Heartian* embeds controllable cardiac-cycle albedo into relightable Gaussian head avatars, and *STRAND* bridges video-LLM monitoring with dynamics understanding.

**Overall:** The dominant theme is a maturation of world models from "predict everything densely" toward *task-aligned, action-discriminative, and query-aware* predictive latents — with evaluation rigor (surveys, benchmarks, counterfactual metrics) finally catching up to architectural ambition.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xvyuan Liu, Jianjie Fang, Chen Gao, Yong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that frozen visual world models plan better when scoring toward retrieved intermediate observed targets rather than the final goal, a broadly useful insight for world-model-based planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30036)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhiyu Xu, Weilong Yan, Yufei Shi, Shiyang Li, Yihao Liu, Kin-Man Lam, Yuewen Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces modality-anchored decoupled diffusion RL post-training that improves joint audio-video generation quality, text alignment, and cross-modal synchronization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29816)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Han Yan, Zishang Xiang, Haokai Jiang, Zeyu Zhang, Qilin Wang, Weiyu Guo, Yandong Guo, Boxin Shi, Hao Tang

**机构**: AIGeeksGroup

**💡 亮点 (Highlight)**: World-action model that predicts sparse visual deltas instead of dense future frames and adds streaming delta memory, improving bimanual manipulation success while cutting training and inference cost.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28811)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang, Lei Qiao, Xuyang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Object-centric multi-view latent world model that predicts task-object state evolution under control and hydrodynamic lag, supporting MPC and imagined-rollout training for underwater ROV salvage.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30214)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Andreas E. Robertson, Ashley T. Lenau, John D. Shimanek, Benjamin A. Jasperson, Vivek Oommen, David L. Damm, Krishna Garikipati, Remi Dingreville

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that latent dynamics representations trained only for reconstruction are ill-suited to long-horizon rollout, and that Koopman learning plus noise injection and multi-step fine-tuning restructure the latent space for stable autoregressive prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30198)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiabin Qiu, Zixuan Chen, Hongye Cao, Jieqi Shi, Jing Huo, Yang Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces action-discriminative joint-embedding world models with inverse-dynamics and action-recovery regularization so latent dynamics preserve counterfactual action differences for MPC.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30264)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xuyao Huang, Yixuan Wang, Zengyao Ye, Boyuan Zhao, Chenyang Yu, Haoran Wen, Zhijie Deng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Couples action-conditioned future visual prediction with asynchronous control by conditioning on committed action prefixes, improving world-action model efficiency while maintaining success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28927)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yohan Choi, Min-Jun Kim, Jin-Sung Kim, Yong-Jae Kim, Youn-Hee Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds noise robustness directly into a depth-based world model via denoising reconstruction and contrastive latent alignment, enabling zero-shot quadruped parkour without hand-tuned filters.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29092)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Guangfu Guo, Xiaoqian Lu, Rui Liu, Yutong Chen, Kunpeng Liu, Long Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically studies visual representation choice and introduces cached linear-attention history modeling for efficient long-context, multi-query action-conditioned navigation world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29555)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Fan Lu, Hanshi Wang, Zijing Wang, Quan Feng, Zhi Wang, Shijie Chen, Xianming Zeng, Yujian Zhang, Jiazhe Wang, Xin Zha, Kai Wang, Zhijie Zhao, Lin Zhu, Tianyi Yang, Yucheng Xu, Tao Ji, Haodong Zhang, Zhipeng Zhang, Peixi Peng, Guang Chen, Xingliang Liu, Lei Yang, Jianyun Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a controllable 2B driving world model with block-causal generation, multi-camera RGB and LiDAR synthesis, and few-step distillation for interactive counterfactual simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28931)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Jack B. Jedlicki, Tanguy Dieudonn\'e, Heng Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an object-centric 4D memory with persistent tracks and temporal/motion/containment relations that supports long-horizon spatiotemporal reasoning and viewpoint-invariant state recall for manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28798)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yehang Zhang, Haojian Huang, Yifan Chang, Jianchong Su, Bohan Zhou, Yingjie Xu, Wosong Chen, Tianhao Zhou, Chenxu Wang, Tianyi Zhang, Yangkai Wei, Wenqian Li, Shiyuan Deng, Yinchuan Li, Ying-Cong Chen, Zexi Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a visual action workspace with an Imagination Agent that rehearses and previews actions before execution, giving a world-model-style closed-loop harness for VLM-driven manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29964)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves long-horizon text-to-video generation by training a large prompt-enhancement model for shot-level cinematic planning with semantic-consistency GRPO.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30221)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jerrin Bright, John Zelek

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Feed-forward metric 4D people-scene reconstruction from monocular video with learned scale readout and identity association, relevant to spatio-temporal scene dynamics modeling though not a generative video model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29106)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Xiaoyue Fan, Jose Echevarria, Akshay Paruchuri, Kaan Ak\c{s}it

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Embeds controllable cardiac-cycle albedo modulation into relightable Gaussian head avatars, a narrow avatar-specific contribution with limited transferable video-generation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28539)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jinxuan Zhu, Jiaheng Wang, Chao Tang, Mengfan Wang, Hao Wei, Shengbao Li, Hong Yin, Yiwen Gao, Chenrui Tie, Tingguang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Derives action-grounded gaze supervision from counterfactual visual interventions to focus VLA attention, relevant to action-conditioned visual dynamics but not a world-model or video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28955)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Thong Nguyen, Tri Cao, Khoi Le, Cong-Duy Nguyen, Quynh Vo, See-Kiong Ng, Bryan Hooi Kuen-Yew

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Object-centric spatio-temporal monitoring framework for video LLMs that improves persistent object tracking and temporal reasoning, offering transferable representations for dynamics understanding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29607)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Mehmet Turan Yard{\i}mc{\i}, Yunus Emre \c{C}o\u{g}urcu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies task collapse during online RL fine-tuning of a flow-matching VLA policy and proposes uncertainty-gated exploration noise, an RL training insight only weakly connected to learned dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28838)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yufan Liu, Shang Luo, Yang Liu, Haoxuan Jia, Feiyu Han, Qian Li, Chen Li, Yingguang Yang, Chongyang Zhang, Hao Zheng, Kefu Xu, Bin Chong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Addresses latent-belief failures in embodied agents via re-probing and rollback, offering a weakly related decision-theoretic view of state correction rather than a learned dynamics model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28973)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 3/10

**作者**: Gaytri Jena, Kapil Wanaskar, Vinija Jain, Aman Chadha, Vasu Sharma, Amitava Das

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Survey mapping 160 benchmarks and proposing an evaluation loop and advantage-aware metrics to isolate the closed-loop benefit of predictive world models over direct VLA policies.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29669)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 3/10

**作者**: Guangzhao Dai, Qianru Sun, Qi Wu, Bin Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Zero-shot evaluation of a foundation model for continuous vision-and-language navigation, offering embodied-navigation evidence relevant to world-model-based planning but without a new dynamics or generative method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.29861)

---

