# 💡 今日研究速览 (Daily Summary)

### World Models & Action-Conditioned Dynamics

Today's strongest cluster of work pushes world models from passive prediction toward closed-loop decision-making, with a clear emphasis on action-conditioned dynamics for robotics. DIDO distills the interaction-centric dynamics of a multi-step video world-action model into a single denoising step, explicitly preserving gripper-object interaction for low-latency control, while "From Prediction to Decision" demonstrates a world-action model that ranks excavation candidates by predicting signed terrain change and loaded volume on real machines. GLAM and WLA$^3$ extend the representation side: the former trains a goal-conditioned JEPA-style latent world model over global spatiotemporal memory for exploration and navigation, and the latter learns compact latent actions from multimodal state transitions as transferable supervision for generalist policies. Efficiency and control are addressed by LePlanner, which amortizes latent-space planning into an iterative controller over a frozen predictor to avoid horizon-reset procrastination in contact-rich tasks, and JEPLO, which learns a proprio-exteroceptive JEPA world model over raw LiDAR for robust legged locomotion. Notably, the paradigm is migrating beyond vision: an immune world model forecasts intervention effects across cellular, tissue, and patient scales, and online LiDAR identification of robot-induced soil deformation supplies interpretable observable states for soil-aware robotics. A cautionary counterpoint comes from the compute-value audit of test-time scaling for video world models, which finds that sampling headroom is not converted into selection gain—an important negative result for anyone betting on inference-time compute to fix world-model fidelity. Complementing these, "One Model, Two Physical Stories" provides a physics-grounded auditing pipeline for internal and external misalignment between generated video and physical/text predictions, a diagnostic layer the field currently lacks.

### Video Generation & Controllable Synthesis

Controllable, interactive, and efficient video generation dominates the generative side of today's list. LynnReal-Omni presents a unified native multimodal framework spanning reference-guided, structural, editing, restoration, and long-video generation, with a real-time Flash variant that directly targets deployable agentic visual workflows. DiVA attacks the long-horizon problem in interactive digital-life simulation via an Anchored Video Continuation module that returns characters to stable states, reducing drift and camera jitter in multi-turn action-conditioned generation. On the distillation front, CrossDistill introduces a noise-regime-split hybrid scheme that preserves global modes at high noise while sharpening local detail at low noise, expanding the few-step quality-diversity frontier for text-to-video diffusion. Subject-centric control is advanced by BEACON, which disentangles identity from expressive facial behavior through dual image/video conditioning, and SignMimic, which factorizes sign-language generation into rigid canonicalization, non-rigid adaptation, and pose completion before conditional diffusion, improving spatiotemporal consistency and identity preservation. Finally, Open-UniMo unifies motion-language understanding and generation in a shared token space with motion-consistent chain-of-thought, a narrower but coherent contribution to dynamics generation.

### Agents & Embodied Reasoning

Work on agents today splits between long-horizon physical task management and structured temporal reasoning. "Toward Self-Adaptive Physical AI" offers a zero-shot multi-agent LLM framework that manages long-horizon physical tasks and adapts to environmental shifts, suggesting that self-adaptive embodied behavior can emerge without learned world models. HarnessVLN contributes a training-free embodied navigation harness with hierarchical event memory and a spatiotemporal graph, whose spatial-memory and recovery mechanisms are directly relevant to world-model-based agents even absent learned dynamics. VideoScout applies agentic sequential evidence acquisition with adaptive reasoning pacing to long-video understanding, sitting adjacent to world-model-style temporal reasoning. On the evaluation side, V-ICAL Bench benchmarks video in-context learning for multimodal agents in interactive environments, probing video-conditioned policy induction. Planning-in-backbone approaches are represented by DiffAdapterVLA, which injects trajectory tokens into VLM late layers for continuous closed-loop driving planning, and by BLInD, which learns a multimodal distribution over future ego trajectories from vehicle-state history alone as a lightweight intent dynamics model for downstream safety triggering.

### Representation Learning & Interpretability

A final thread concerns structured, interpretable representations of temporal and object-centric dynamics. EventGraph and EventField provide a structured temporal representation that improves both accuracy and inspectability of video reasoning, offering a transferable temporal-dynamics substrate for video understanding. MM-LMPC combines mode-specific terminal design with bandit-based exploration for learning MPC, yielding transferable insights for learned dynamics and long-horizon planning. Visible Touch delivers contact signals directly in the policy's visual frame to improve visuomotor manipulation, a modest but practical embodied-dynamics contribution. On the cautionary side, an empirical analysis of attention-guided masking questions whether it genuinely helps object discovery in object-centric learning, a useful corrective for representation work that is only weakly tied to learned visual dynamics.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jing Lyu, Shuanghao Bai, Runze Xiao, Zhenyu Liao, Wenxing Tan, Zihan Tang, Ruochuan Shi, Cheng Peng, Yuheng Ji, Yihao Wang, Badong Chen, Pengwei Wang, Zhongyuan Wang, Xiaoguang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distills interaction-centric dynamics of a multi-step video world-action model into a single denoising step, preserving gripper-object interaction dynamics for low-latency closed-loop robotic control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15570)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaofeng Mao, Peijia Lin, Shaohao Rui, Yibo Zhang, Haibin Wan, Weijie Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified native multimodal video generation framework supporting reference-guided, structural, editing, restoration, and long-video generation with a real-time Flash variant, directly advancing controllable and efficient video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15863)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Geigh Zollicoffer, Minh Vu, Rajiv Ranasinghe, Manish Bhattarai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Audits internal and external misalignment between a multimodal world model's generated video and its physical/text predictions, providing a physics-grounded pipeline and contract-based diagnostics for world-model fidelity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.14833)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Cheng Chen, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Wen Wang, Yihao Meng, Hanlin Wang, Yixuan Li, Jiacheng Wei, Zhenshan Tan, Yanhong Zeng, Yujun Shen, Guosheng Lin, Fayao Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds an interactive long-horizon digital-life video simulator with an Anchored Video Continuation module that returns characters to stable states, reducing drift and camera jitter in multi-turn action-conditioned generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13830)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuxi Liu, Haoyu Li, Yixiang Cai, Tengxu Sun, Zekun Zhang, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kun Yuan, Kai Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a noise-regime-split hybrid distillation that preserves global modes at high noise and sharpens local detail at low noise, expanding the few-step quality-diversity frontier for text-to-video diffusion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.14725)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ailing Zhang, Fan Gao, Song Zhang, Kawa Leong, Ziyu Wu, Yafei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: World-Action Model predicts signed terrain change and loaded volume to rank excavation candidates in closed loop, a concrete action-conditioned dynamics model with real-machine deployment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15382)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: I-Tak Ieong, Ruizhi Feng, Zhaoyang Lu, Yifei Cao, Jiayao Zhao, Leon Li, Senhua Zhu, Wenbo Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains a goal-conditioned JEPA-style latent world model over global spatiotemporal map memory to jointly predict future map representations and waypoint latents for active exploration and navigation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.14561)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Peidong Liu, Zhiyuan Xiang, Mingyang Li, Wenhao Li, Jiale Zhang, Jiahao Sun, Jiawei Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns compact latent actions from multimodal world-state transitions to supervise generalist policies, offering a transferable world-model representation of dynamics, semantics, and kinematics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15870)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Saksham Bansal, Om Naphade, Chayan Aggarwal, Vrishin M

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Amortizes latent-space planning into an iterative controller over a frozen world-model predictor, cutting rollout cost while avoiding horizon-reset procrastination in contact-rich control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13845)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Qihao Yuan, Yixuan Qiu, Ziyu Cao, Ming Cao, Kailai Li

**机构**: ASIG-X

**💡 亮点 (Highlight)**: Learns a proprio-exteroceptive JEPA world model over raw LiDAR for legged locomotion, showing predictive egocentric terrain representations improve robustness under degraded perception.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15770)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yuhua Jiang, Junjie Lu, Feifei Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Compute-Value Audit shows test-time scaling headroom in video world models is not converted into selection gain, a useful negative insight for video-generation inference and verification.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13257)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Zhewen He (New York University Abu Dhabi), Junyi Yu (New York University Abu Dhabi), Haomian Huang (New York University Abu Dhabi), Zhenhua Li (ChatSign Technology), Yi Fang (New York University Abu Dhabi, ChatSign Technology)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Factorizes sign-language video generation into rigid canonicalization, non-rigid adaptation, and pose completion before conditional diffusion, improving spatio-temporal consistency and identity preservation in a narrow but transferable video-generation pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.14122)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Pokrzywa Baptiste, Nabyl Quignon, Yara Bahram, Muhammad Osama Zeeshan, Antitza Dantcheva, Eric Granger

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Disentangles identity from expressive facial behavior via dual image/video conditioning to improve subject-specific expressivity in video diffusion generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13264)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Weixin Xu, Zhenyu Yang, Bing Wang, Shengsheng Qian, Changsheng Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Agentic sequential evidence acquisition for long video understanding with adaptive viewing pace; adjacent to world-model-style temporal reasoning but primarily a video-understanding agent rather than a generative or dynamics model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15606)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Changxin Lu, Xiaoliang Meng, Yu Wu, Rui Huang, Honglin Li, Tao Chen, Kaixuan Zhou, Yadong Shao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Injects trajectory tokens into VLM late layers for continuous closed-loop driving planning, a weakly related planning-in-backbone approach without a substantive video-generation or visual-dynamics contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15322)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Metin Alp Dogan, Edward Sun, Feng Xu, Daniel Wu, Allen Peng, Dennis Hong, Yuchen Cui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Delivers contact signals in the policy's visual frame to improve visuomotor manipulation, a weakly related embodied-dynamics contribution rather than a world-model or video-generation advance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.14156)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Wataru Hashimoto, Kazumune Hashimoto, Masako Kishida

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Mode-specific terminal design and bandit exploration for learning MPC improves long-horizon control and exploration, offering a transferable insight for learned dynamics and planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15623)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Guocun Wang, Kenkun Liu, Guorui Song, Jing Lin, Zhe Huang, Luyuan Zhang, Dake Zhong, Choo Sin Wai, Xiaoguang Han, Haoqian Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified motion-language token space with motion-consistent chain-of-thought improves human-motion generation and understanding, a narrow but plausible dynamics-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.14615)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Taoyong Cui, Xi Wang, Zonghang Li, Jinchao Ding, Lingsen You, Yuzhi Xu, Wanghan Xu, Fang Wu, Kejun Ying, Wanli Ouyang, Pheng Ann Heng, Ling Yang, Zhenfei Yin, Yingcheng Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds an action-conditioned multiscale immune world model that forecasts intervention effects across cellular, tissue, and patient levels, illustrating transferable action-conditioned dynamics modeling outside vision.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.14709)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Durgendra Narayan Singh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Structured EventGraph/EventField temporal representation improves video reasoning accuracy and inspectability, offering a transferable temporal-dynamics representation for video understanding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13258)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Tom Montagnon, Johann Laconte, Benoit Thuilot, Wonjae Cho, Roland Lenain

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Online lidar-based reduced-order parametric model estimates robot-induced soil deformation, giving an interpretable observable state representation of environment dynamics for soil-aware robotics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15667)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Varun Kaushik, Yayun Tan, Xiaofan Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Zero-shot multi-agent LLM framework for long-horizon physical task management adapts to environmental shifts, offering insight into self-adaptive embodied agents without learned world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13436)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yang Chen, Lirong Che, Zhenyu Huang, Wenbo Fu, Chuang Wang, Xu Cao, Daqi Liu, Yuzhe Yang, Jian Su, Lan-Zhe Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a training-free embodied navigation harness with hierarchical event memory and a spatiotemporal graph, offering spatial-memory and recovery ideas relevant to world-model-based embodied agents but no learned dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15195)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Flavian Pegado, Ronit Hire, Shreyas Rajesh, Soham Phade

**机构**: Wayve

**💡 亮点 (Highlight)**: Learns a multimodal distribution over future ego trajectories from vehicle-state history alone, a lightweight learned dynamics model for intent prediction and downstream safety triggering.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13941)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Ziqian Fan, Shibo Xu, Junjie Li, Xiangyu Zhao, Shengyuan Ding, Yifan Yang, Zhenjie Yang, Haodong Duan, Yue Zhou, Zhihang Zhong, Xue Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmarks video in-context learning for multimodal agents in interactive environments, offering evaluation insight into video-conditioned policy induction but no new generative or dynamics method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15683)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Youliang Tao, Yanhua Han, Bin Zhao, Juho Kannala, Joni Pajarinen, Rongzhen Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes attention-guided masking for object-centric slot learning, offering a cautionary empirical insight about object-centric representations that is only weakly connected to learned visual dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.15187)

---

