# 💡 今日研究速览 (Daily Summary)

### World Models & Action-Conditioned Dynamics

Today's submissions reveal a field converging on a crucial insight: **the internal representations and design choices of world models matter as much as their raw generative capability**. A cluster of empirical and diagnostic studies exposes fragility in current approaches — action-conditioned latent models prove catastrophically non-invariant to action parameterization (absolute vs. delta), video foundation models achieve human-level physical-reasoning accuracy through non-human scene-statistics shortcuts rather than forward simulation, and World Action Models can generate consequential imagined futures that existing visual-quality and physical-consistency selectors simply fail to recognize. These findings collectively motivate a shift from decision-useful evaluation and principled design disentanglement toward more robust architectures. Promisingly, several works respond directly: geometry-native latent spaces jointly decodable to appearance, depth, and point maps halve camera-trajectory error; implicit 3D-aware memory enables long-horizon cross-viewpoint consistency; and persistent physical belief states support multi-step terrain prediction under partial observability. Mechanistic analysis further reveals superposed intersection features and affordance packing inside transformers, while relational scene-graph supervision and Koopman-backbone Kalman filtering offer structured alternatives to black-box latent dynamics. The overarching trend is unmistakable: the community is moving beyond "can we generate plausible futures?" toward "are our world models' internal dynamics causally grounded, invariant, and decision-useful?"

### Vision-Language-Action & Embodied Control

A striking theme today is the**distillation of world-model representations into compact, real-time policies without test-time generative rollout**. Frozen world-model features can be transferred to VLA policies via a single feature-alignment term, and imagined contact mechanics can be distilled into student policies that require no inference-time tactile sensing — a significant step toward deploying rich physical grounding on resource-constrained robots. Complementing this, uncertainty-prioritized rollouts and residual-confidence-guided cross-attention improve the efficiency and reliability of model-based policy optimization in contact-rich manipulation. On the architecture side, persistent recurrent memory in compact VLA models improves long-horizon decision-making under occlusion, while event-triggered asynchronous inference adapts to scene changes without an explicit world model. Force-conditioned and visuo-tactile extensions push VLA policies into dexterous, contact-rich regimes, and visual-conditioned world action models replace language with grounding prompts for agent-driven manipulation. The collective direction is clear: world models are becoming**training-time and inference-time scaffolds**for policies that must act under real physical constraints, rather than ends in themselves.

### Generative Video & Efficient Visual Synthesis

Efficiency and controllability dominate today's visual generation contributions. A unified framework combining a staging principle with terminal-aligned distillation escapes the high-sparsity trap to achieve up to**265× single-GPU acceleration**of video diffusion transformers at 720P quality — a dramatic result for practical deployment. Analysis of streaming video diffusion design space shows that progressive-history context selection plus pipelining improves both long-video consistency and DiT throughput, while direction-aware optimization and resolution-flexible decoding advance implicit and hybrid neural video representations. On the controllability front, rubric-guided policy optimization stabilizes scalar rewards for RL-based video generation, and geometric analysis of classifier-free guidance in flow matching yields a training-free posterior-mean-capped scheme with clear transfer potential. Physical-plausibility supervision is also maturing: differentiable epipolar and lighting losses enforce consistent mirror reflections, and multi-agent video world models use pose-conditioned memory retrieval and visibility-gated peer sharing for cross-agent consistency. Together these works suggest that**the frontier of video generation is shifting from raw quality to controllable, efficient, and physically consistent synthesis**.

### Autonomous Driving & Navigation

Driving and navigation research today emphasizes**structured, planning-aligned representations**. Event-decomposed world modeling splits future prediction into normal evolution plus event-triggered incremental correction in latent space, improving trajectory-conditioned plan selection. Relationally grounded latent world models align representations with actor-centric scene-graph semantics as privileged supervision, reducing collision rates without test-time overhead, while sparse action-conditioned BEV pretraining targets planning-relevant features directly. In embodied exploration, world-model-guided LiDAR exploration predicts future occupancy and visibility to generate predictive frontiers for UAVs, and phase-grounded temporal navigation with predict-execute-re-observe loops brings explicit semantic progress states to unmanned surface vehicles. These contributions share a common thread:**learned dynamics are being shaped by downstream planning objectives rather than treated as generic prediction tasks**.

### Multimodal & Cross-Domain Transfer

Several works push world modeling beyond vision into**touch, motion, and multi-agent communication**. Visuo-tactile world-action models extend pretrained video diffusion to distributed fingertip tactile latents, modeling contact evolution as part of the predicted world state, while haptic world-action models imagine future contact mechanics for contact-rich manipulation. In humanoid control, predictive action diffusion jointly generates actions and internal future-state trajectories, and noise-space trajectory optimization synthesizes physically plausible interaction references from text-conditioned motion models. Multi-robot teams demonstrate that frozen self-supervised perceptual latents can serve as compact shared communication messages, and a real-time interactive avatar stack introduces a directed Granger-gain metric for audio-conditioned motion. A non-visual patient world model with exposure-conditioned dynamics illustrates both the reach and the causal-interpretation limits of latent-state forecasting in digital health. The trend here is**representation transfer across modalities and embodiments**, with self-supervised latents emerging as a common currency for communication, control, and prediction.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a camera-queryable implicit 3D-aware memory jointly trained with a video generator, substantially improving long-horizon and cross-viewpoint consistency for interactive video world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24984)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yixin Zheng, Jiangran Lyu, Yuntian Deng, Kai Liu, Yizhou Zhou, Yizhou Wang, Xiaoguang Zhao, He Wang, Zhizheng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Dual-system world action model decoupling global world-action planning from wrist-observation local refinement enables high-frequency closed-loop control while retaining long-horizon visual prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24868)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ahmed Karim, Leon Chlon

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reveals that action-conditioned latent world models are catastrophically non-invariant to action parameterization (absolute vs. delta), with a diagnostic test and objective-averaging repair that improves rollout robustness.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23252)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuxi Liu, Haoyu Li, Zekun Zhang, Tengxu Sun, Yixiang Cai, Jiayong Li, Yifei Xia, Tianle Liu, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kai Zhang, Kun Yuan, Bin Cui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a staging principle and terminal-aligned distillation to escape the high-sparsity trap, enabling up to 265x single-GPU acceleration of video diffusion transformers with strong 720P quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23153)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Markus Karmann, Shile Li, Christian Intern\`o, Bruno Andreis, David Klindt, Randall Balestriero, Jindong Gu, Philip Torr, Qi Zhang, Peng-Tao Jiang, Hao Zhang, Bo Li, Onay Urfalioglu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DISReg, a temporal-difference embedding regularizer that prevents feature collapse in JEPA latent world models and improves downstream planning under distractors.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23881)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yikun Miao, Fangqi Zhu, Quanxin Shou, Xiaoyi Pang, Zhengyang Yan, Junhao Li, Haodong Wang, Zicong Hong, Song Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces active online simulator querying plus counterfactual causality-aware fine-tuning to improve action controllability and long-tail dynamics in generative world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23753)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiahao Lu, Minghao Yin, Wenbo Hu, Hengyu Liu, Wang Zhao, Sai-Kit Yeung, Ying Shan, Yuan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a geometry-native autoencoder latent space jointly decodable to appearance, depth, cameras, and point maps, improving 3D-consistent video/world generation and halving camera-trajectory error.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24981)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuyang Tian, Penghui Yang, Pengyuan Wu, Haoran Yang, Chenhui Li, Pengfei Han, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a recurrent world model of LiDAR observation dynamics to predict future occupancy/visibility and generate predictive frontiers for UAV exploration, a concrete learned-dynamics contribution for embodied planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23656)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pierre Beckmann, Matthieu Queloz, Andre Freitas

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Mechanistic analysis of a transformer's internal map representation reveals superposed intersection features and affordance packing that improve world-modeling capacities, offering broadly useful insight into how learned dynamics are represented.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21748)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qianxun Xu, Xianfang Zeng, Xinyao Liao, Wei Cheng, Gang Yu, Chi Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces pose-conditioned memory retrieval and visibility-gated peer sharing for multi-agent video world models, improving cross-time and cross-agent consistency in camera-controlled generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22641)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mikhail Sannikov, Ilya Mikhalchuk, Konstantin Gubernatorov, Petr Kovalev, Ogunwoye Faith Oluwatobi, Dzmitry Tsetserukou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: World-action model that imagines future contact mechanics and distills tactile-conditioned dynamics into a student policy without inference-time tactile sensing, advancing action-conditioned world modeling for contact-rich manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23888)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kejia Hu, Wentong Zhai, Bo Zhao, Shuai Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments VLA reinforcement learning with an action-conditioned visual-torque latent world model whose predicted futures and residual-confidence priors improve action evaluation in contact-rich manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24033)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongchen Zhang (University of Chinese Academy of Sciences)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes streaming video diffusion design space and shows progressive-history context selection plus pipelining improves long-video consistency and DiT throughput.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22283)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoran Yuan, Zekai Wang, Boning Shao, Haoran Lu, Trevor Darrell, Ismini Lourentzou, Wei Zhan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends a pretrained video diffusion world-action model to distributed fingertip tactile latents, showing contact evolution can be modeled as part of the predicted world state for dexterous manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24976)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongyi Lin, Song Zhang, Haiquan Liu, Yang Liu, Jinhua Zhao, Xiaobo Qu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces persistent physical belief with world-addressed deformation and physical-response memory for interaction-driven world modeling, enabling multi-step terrain prediction and action ranking under partial observability.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22858)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junjie Yang, Qingwei Zeng, Youyou Li, Zicheng Ding, Ziyi Shi, Shuqi Shen, Hongliang Lu, Hai Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decomposes driving world-model future prediction into normal evolution plus event-triggered incremental correction in latent feature space, improving trajectory-conditioned future-feature prediction and plan selection.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22317)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Trung Dao, Sankalp Yamsani, Jaden Park, Joohyung Kim, Yong Jae Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that a frozen world model's internal features can be distilled into a compact VLA policy via a single feature-alignment term, transferring physical grounding without test-time generative rollout.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24682)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Jianhao Yuan, Yu Yuan, Benjamin Ramtoula, Lukas Vierling, Paul Newman, Lars Kunze, Philip Torr, Daniele De Martini

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Empirical study showing that world action models can generate consequential imagined futures but current visual-quality, physical-consistency, and task-progression selectors fail to recognize them, motivating decision-useful evaluation of world-model predictions.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24745)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Chao Tang, Haoqing Wang, Zilang Cen, Weishi Mi, Wei Xia, Fangcheng Liu, Anda Cheng, Yeqing Shen, Xiaohui Cui, Xiaoyuan Zhang, Yehui Tang, Tingguang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically disentangles causal structure, latent space, and training objectives in World Action Models, yielding broadly useful design principles for world-model-based control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24048)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zhenchen Tang, Yang Li, Songlin Yang, Bo Peng, Xiaotong Zhao, Shuai Li, Haotian Fan, Alan Zhao, Jing Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a rubric-guided video reward model with RGPO to stabilize scalar rewards and mitigate drift, providing a more reliable signal for RL-based video generation improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22947)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yicheng Jiang, Zesen Gan, Xiaobo Wang, Tianlun He, Chenxu Zhao, Minghui Wu, Xinyue Wang, Jiaxu Wang, Junhao He, Jianan Wang, Qiming Shao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Visual-conditioned world action model that predicts scene evolution in latent states while decoding actions, replacing language with grounding prompts and operation tokens for agent-driven manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23578)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Fanhong Li, Shurui Zheng, Zi Yin, Junbo Cui, Lei Ji, Jia Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distributional evaluation revealing that video foundation models reach human-level physical-reasoning accuracy via non-human scene-statistics strategies rather than forward simulation, offering a useful diagnostic for world-model dynamics understanding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22788)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yifei Sheng, Haoxiang Ren, Zhilong Zhang, Haonan Wang, Runjie Xu, Yihao Sun, Nan Tang, Zhichao Wu, Lei Yuan, Haoxin Lin, Yang Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses policy uncertainty to prioritize which states receive world-model rollouts in VLA policy optimization, a transferable insight for efficient model-based rollout generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22879)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Fabian Schmidt, Markus Enzweiler, Abhinav Valada

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Aligns latent driving world-model representations with actor-centric scene-graph semantics as privileged supervision, improving trajectory prediction and collision rate without test-time overhead.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24626)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Mintaek Oh, Jeonghun Park, Nir Shlezinger, Yonina C. Eldar, Jinseok Choi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns latent linear dynamics via a Koopman backbone for blind Kalman filtering of unknown dynamics, offering a structured latent-dynamics representation relevant to learned world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24763)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Shuheng Ge, Hongwei Ren, Li Zhang, Xiangqian Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Enforces geometric and perceptual reflection consistency in diffusion via differentiable epipolar and lighting losses, offering transferable physical-plausibility supervision for generative visual models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23442)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Lei Ye, Haibo Gao, Yitang Li, Peng Xu, Zetong Jing, Junhan Sun, Fanrong Dong, Ziqi Han, Xue Wang, Jianhua Sun, Cewu Lu, Hao Zhao, Liang Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Jointly diffuses actions and an internal future-state trajectory for steerable humanoid control, giving a predictive-dynamics representation usable for test-time motion objectives.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24840)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Lalit Jayanti, Kashu Yamazaki, Yuto Shibata, Kotaro Amaya, Katerina Fragkiadaki

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Optimizes noise-space trajectories of a pretrained text-conditioned motion model to synthesize physically plausible humanoid interaction references, a narrow but transferable motion-generation technique.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22611)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jishen Peng, Zheng Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a geometric analysis of classifier-free guidance in flow matching and a training-free posterior-mean-capped guidance scheme that could transfer to video flow/diffusion generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24287)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Artem Kravtsov, Dmitrii Ziganshin, Vsevolod Poletaev, Gleb Balitskiy, Anastasia Tikhonova, Egor Burkov, Vadim Lebedev

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a real-time interactive dyadic avatar stack with an autoregressive flow-matching motion generator and a new directed Granger-gain metric for audio-conditioned motion, offering limited but plausible transferable insight for controllable video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22913)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Howard Wang, Han Zheng, Cathy Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows frozen self-supervised perceptual latents can serve as compact, shared communication messages in multi-robot teams, giving a relevant latent-representation insight for partially observable dynamics and embodied coordination.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23269)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jieling Wu, Yuehao Huang, Jiajun Lv, Tao Huang, Yong Liu, Weiwei Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Phase-grounded temporal navigation with predict-execute-re-observe closed-loop rollout for USVs offers a weakly transferable world-model insight via explicit semantic progress state fused with visual-motion history.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23423)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jan-Gerrit Habekost, Parsa Mastouri Kashani, Connor G\"ade, Matthias Kerzel, Philipp Allgeuer, Cornelius Weber, Stefan Wermter, Jae Hee Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Persistent recurrent memory in a VLA policy improves long-horizon embodied decision-making under occlusion, offering a modest memory/state-abstraction insight for world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22854)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Yunlong Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Latent-state patient world model with exposure-conditioned dynamics and weekly hazard rollouts for forecasting health campaign outcomes, illustrating non-visual learned dynamics and the limits of causal interpretation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23333)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Fukang Liu, Yipu Chen, Jaehwi Jang, Danfei Xu, Zsolt Kira, Ye Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds explicit force conditioning to a VLA policy for contact-rich humanoid manipulation, a weakly related embodied-dynamics contribution without a learned visual world model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23968)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jingzhi Cui, Xuefeng Liu, Feng Han, Xinyu Liu, Wei Chen, Jianwei Niu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a generative shape prior to imagine occluded geometry and plan uncertainty-aware next-best-views, offering a weakly related active-perception take on learned spatial/affordance dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23504)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Wenbo Li, Yiteng Chen, Wei Zhang, Wenhao Li, Jun Yang, Qingyao Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a structured action-conditioning state covering task progression, scene dynamics, and spatial grounding via staged grounding, offering indirect relevance to controllable dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23275)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Rui Zhou, Zihan Zhu, Wei Zhang, Zizhou Luo, Norbert Haala, Marc Pollefeys

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Separates robot motion from elevator transport motion in visual-inertial Gaussian-splatting SLAM, a narrow but relevant contribution to disentangling scene dynamics from egomotion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23491)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Kunyang Lin, Xutao Wen, Jingxi Lin, Lanyong Lin, Jiaming Liu, Tianshuo Yang, Xianchi Chen, Yue Han, Yiduo Li, Zhanpeng Zhang, Ping Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Transfers in-the-wild egocentric human video to dexterous dual-arm manipulation via geometric view alignment and human-robot training, with limited but plausible relevance to embodied dynamics learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23755)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Guanxiong Chen, Yiduo Qu, Qianjun Xia, Pengyu Jing, Yixian Cheng, Bole Ma, Pengzhi Yang, Bingyang Zhou, Ziming Li, Shashwat Suri, Gongbo Sun, Chao Liu, Peter Yichen Chen, Ziqiu Zeng, Fan Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Agentic generate-simulate-diagnose-refine loop produces simulation-ready deformable assets, offering a weakly related physical-plausibility feedback mechanism for robotic simulation rather than a video or dynamics world model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23103)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yansong Wu, Huaqing Li, Tianding Hou, Lingyun Chen, Alois Knoll

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Event-triggered asynchronous inference for VLA policies adapts the inference gap to observed scene changes, improving reactivity to environment dynamics but without an explicit learned world model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22587)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Qingyu Mao, Jiacong Chen, Shuai Liu, Yongsheng Liang, Youneng Bao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Direction-aware optimizer for implicit neural video representation improves reconstruction convergence and PSNR/MS-SSIM, a video-representation optimization contribution only indirectly tied to video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23052)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Taiga Hayami, Masaya Takabe, Hiroshi Watanabe

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a resolution-flexible decoder with progressive 2x upsampling and intermediate supervision for hybrid neural video representations, a narrow but transferable video-representation improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23555)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jaeha Song, Soonmin Hwang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Action-conditioned sparse BEV pretraining targets for planning-relevant representations, tangentially related to learned dynamics but focused on autonomous-driving planning rather than generative world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22868)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yuxuan Nai, Leixin Chang, Liangjing Yang, Shuo Yang, Zhongyu Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: End-effector-conditioned real-time whole-body motion generator that transfers UMI manipulation skills to humanoids, offering only indirect relevance to learned dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22829)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Boyu Qiao, Zixin Tang, Xiaoshuai Hao, Wenbo Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for black-box game replication via visual interaction, weakly relevant as it probes inducing dynamics/rules from pixels but offers no new world-model or video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22308)

---

## 47. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 3/10

**作者**: Chuyang Xiao, Haotian Zhan, Sriram Krishna, Peilin Meng, Muhammad Zubair Irshad, Sergey Zakharov, David Held

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for human-to-robot transfer that evaluates policies learned from human video, only weakly connected to world models or video generation via its use of video demonstrations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24778)

---

## 48. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 2/10

**作者**: Nick Lemke, Niklas Ihm, John Kalkhof, Mirko Konstantin, Henry J. Krumb, Daniel M. Lang, Ehsan Pajouheshagar, Ario Sadafi, Arjan Kuijper, Karim Lekadir, Marco Lorenzi, Carsten Marr, Julia A. Schnabel, Anirban Mukhopadhyay

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Survey of neural cellular automata for simulation and image synthesis is only loosely connected to learned dynamics or video generation, with no new method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.24595)

---

