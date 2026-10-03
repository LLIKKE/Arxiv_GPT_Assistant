# 💡 今日研究速览 (Daily Summary)

### World Models & Latent Dynamics

The dominant thread today is the maturation of world models from monolithic latent predictors into structured, factorized, and verifiable systems. Several works attack the core representational problem: World-as-Graph injects explicit relational inductive bias via object-centric latent graphs, while CF-JEPA factors JEPA latents into controllable versus uncontrollable subspaces to prevent collapse under distractor signals. Complementing these, DeepJEPA reframes scaling as adaptive per-transition depth allocation, concentrating compute at decision-critical events like contact onset—a notable shift from uniform-depth scaling. On the theory side, the chaos extrapolation result is striking: autoregressive transformers trained only on local trajectories recover global attractor structure, suggesting learned dynamics generalize far beyond their training manifold. Together these papers signal a field moving past "can we predict the future?" toward "what structure makes the future predictable and controllable?"

### Video World Models & Generative Simulation

Video generation is rapidly consolidating around controllability and physical grounding. 4Director and Generative Cinematographer both condition diffusion models on explicit 3D geometry—rigid 4D meshes and scene-scaffold guidance maps respectively—enabling precise camera and object motion control that pure text conditioning cannot achieve. HiPhy takes a different route, using hierarchical RL alignment to enforce multiple concurrent physical principles, while PhysDEM and PMosFM bring physics-defined energy matching and manifold preconditioning to spatiotemporal field generation. A recurring theme is the decoupling of observation from action: World Observer jointly generates actor views with panoramic observers for persistent out-of-view evolution, and Completion Aware Guidance steers sampling toward task-completing futures. Notably, VTR-Bench and Ego2Act expose concrete failure modes—visual text rendering and multi-step physical reasoning—reminding us that benchmarks are catching up to capabilities.

### Action-Conditioned Models & Robotics

World-action models are diversifying their state representations away from raw pixels. SkeleWAM uses sparse 3D skeletons, Token-World operates in compressed VLM visual-token space, and TacDyn-WAM predicts implicit tactile dynamics rather than reconstructing tactile pixels—all converging on the insight that compact, task-relevant abstractions beat photorealistic reconstruction for closed-loop control. DashVMC offers a clean validation of this paradigm by training controllers entirely within frozen-model rollouts for real-time 60-Hz gameplay. On the memory front, Divide-and-Remember learns action-relevant recursive memory for long-horizon VLA policies, and CtrlWAM aligns perturbed actions with their simulated visual consequences via warped noise schedules. The egocentric humanoid pretraining work (Towards a General Humanoid Loco-Manipulation Model) and PACT's joint pose-contact-force estimation suggest embodied dynamics learning is increasingly mining human video as a scalable supervision source.

### Agents & Interactive Environments

A verification-oriented thread is emerging in agentic world modeling. Kepler represents agent hypotheses as executable world models validated by retrospective transition and conditional prediction checks—an auditable framework particularly relevant to ARC-AGI-3. AutoGUIWorld cleverly repurposes image generators as visual world models for GUI agents, synthesizing interaction trajectories without deploying real software. DramaAgent applies hierarchical agentic control with persistent character states and reflection-guided repair to long-horizon storytelling video. On the evaluation side, the Embodied Agent Arena study questions whether frontier VLM agents are ready to be robot generalists, while Game-Guided Skill Discovery shows self-play can yield compact discrete action abstractions. The convergence of executable verification, synthetic trajectory generation, and self-play skill discovery points toward agents that learn and validate their own environment models.

### Multimodal Generation & Tokenization

Efficiency and semantic alignment dominate the generation infrastructure work. SemanTok introduces DINO-feature reconstruction heads for semantically aligned coarse-to-fine video tokens, improving autoregressive fidelity, while Soundwich transforms frozen joint audio-video flow-matching into separately editable synchronized audio stems. PickMoment unifies deblurring and continuous-time blur-to-video generation through interval-mean integration—an elegant reformulation. Memory-Guided B-Roll Generation builds entity-centric memory for identity-consistent multi-shot synthesis, and Bootstrapping Video Interaction Generation constructs synthetic state-transition data with State-Guided Sampling. Collectively, these papers reflect a shift from raw generative capability toward composable, editable, and semantically grounded multimodal pipelines.

### Physical Dynamics & Identifiability

A smaller but theoretically important cluster addresses what is fundamentally learnable from observation. The identifiability theory for nonlinear scalar dynamics from video (On Parameters of Nonlinear Scalar Dynamics from Video) delineates which physical parameters can be recovered from visual data—a question with direct implications for world model guarantees. The divergence between accuracy and mechanism consistency in time series world models formalizes a critical warning: high prediction accuracy does not imply correct action-response, motivating directional supervision. These results, alongside the chaos extrapolation finding, suggest the field is beginning to formalize the gap between predictive performance and genuine dynamical understanding—arguably the most important open question in world modeling today.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yaqi Yang, Shuo Huang, Yujin Huang, Fucai Ke, Jiatong Han, Xin Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a graph-based object-centric world model with relation-aware structure induction and object-level memory transitions, adding explicit relational inductive bias to JEPA-style latent dynamics prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38927)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decouples observing from acting by jointly generating an actor view with panoramic observers, enabling persistent out-of-view object evolution and state preservation in video world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02162)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yilun Liu, Yi Zhang, Ganyu Wu, Sikuan Yan, Mengyue Wang, Alois Knoll, Volker Tresp, Yunpu Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows autoregressive transformers trained on local trajectories extrapolate global chaotic dynamics and attractor structure, giving a strong insight into learned dynamics generalization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38814)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zijian Jin, Yunbei Zhang, Yuanzhe Liu, Ming Liu, Baian Chen, Weirui Ye, Shilong Liu, Marco Pavone

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reframes world-model scaling as adaptive per-transition depth allocation in a weight-tied JEPA planner, concentrating computation at decision-critical events like contact onset.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00368)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R, Shimon Vainer, Mark Boss, Yaoyao Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Conditions a video world model on explicit rigid 4D mesh geometry with a Motion Adapter, enabling precise camera and object motion control and view-consistent synthesis.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02160)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chensheng Peng, Wenhao Ding, Ran Tian, Zewei Zhou, Jef Packer, Maximilian Igl, Peter Karkus, Yan Wang, Masayoshi Tomizuka, Boris Ivanovic, Marco Pavone, Yuxiao Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Aligns perturbed actions with their simulated visual consequences and introduces warped video-action noise schedules for more controllable joint world-action models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00859)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tahira Kazimi, Shubhankar Borse, Munawar Hayat, Fatih Porikli, Pinar Yanardag

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a hierarchical RL alignment framework that enforces multiple concurrent physical principles in video generation, directly improving physical plausibility of generative world simulators.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02197)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haochen Zhang, Jiaheng Guo, Zhen Xu, Zachary Plotkin, Nicholas Konz, Zhen Tan, Tianlong Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formalizes time-series world models and introduces mechanism consistency, showing prediction accuracy diverges from correct action-response and proposing directional supervision to fix it.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01842)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Juyi Sheng, Hua Wang, Mengyuan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Represents manipulation scenes as sparse 3D skeletons for joint action generation and future-state prediction, offering a compact geometric world-action model without visual reconstruction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02120)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chuyao Fu, Xiaowei Chi, Yuhan Rui, Yu-kai Wang, Zezhong Qian, Xiaojie Zhang, Yunfan Lou, Kevin Zhang, Kuangzhi Ge, Chak Wing Mak, Zhiyang Chen, Athena Zhuoming Zhong, Hongyang Chen, Haoran Li, Yike Guo, Sirui Han, Shanghang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Models action-conditioned world dynamics in a compressed VLM visual-token space, improving long-horizon feature fidelity and closed-loop policy correlation over RGB-predicting world-model simulators.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00575)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiho Jang, Jinyoung Kim, Nojun Kwak, Kyungjune Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a synthetic start/end-state interaction dataset with a State-Guided Sampling technique that improves physical plausibility and state-transition quality in generated interaction videos.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01039)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Enyi Wang, Mingxin Wang, Quan Shi, Hetian Guo, Hongyu Wang, Xi Wang, Bin Qian, Yupeng Zheng, Wenxuan Song, Houde Liu, Yong Xu, Cheng Chi, Wenchao Ding, Yilun Chen, Yan Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a visuo-tactile world action model that predicts implicit tactile dynamics in a learned representation space instead of reconstructing tactile pixels, improving robustness of action-conditioned future prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00638)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mikhail Dereviannykh, Vikram Voleti, Simon Donne, Mallikarjun Byrasandra Ramalinga Reddy, Shimon Vainer, Mark Boss

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a flexible video tokenizer with DINO-feature reconstruction heads that yields semantically aligned coarse-to-fine tokens, improving autoregressive video generation fidelity and efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00686)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Seungyeon Kim, Junhoo Lee, Baekseung Kim, Minkyu Kim, Nojun Kwak

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces training-free Completion Aware Guidance that steers World Action Model sampling toward task-completing visual futures, reducing task-incomplete imagination in action-conditioned rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01559)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiahan Zhang, Chaohao Yang, Namitha Guruprasad, Vivekjyoti Banerjee, Trong-Tung Nguyen, Alan Yuille, Anand Bhattad

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces 3D scene-scaffold guidance maps that jointly encode camera and piecewise-rigid object motion, improving camera-relative controllability and geometric consistency in pretrained video diffusion models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02180)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Morgan Byrd, Robert Wright, Sehoon Ha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Factors JEPA world-model latents into controllable and uncontrollable subspaces to prevent latent collapse and improve control robustness under distractor signals.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00727)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Florent Tariolle, Florian Yger

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a compact action-conditioned world model from gameplay video and validates its dynamics by training controllers entirely in frozen-model rollouts for real-time 60-Hz control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.40003)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xuehui Yu, Eason Yu, Meiyi Wang, Haozhe Du, Stefano V. Albrecht, Harold Soh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns an action-relevant recursive memory for long-horizon VLA policies, offering a transferable insight for memory and state abstraction in world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00982)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junseong Shin, Hyeonsu Jo, Daehyun Kim, Tae Hyun Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reformulates motion blur as interval-mean integration to unify deblurring and continuous-time blur-to-video generation in a single deterministic model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01279)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhuo Ning, AmirHossein Naghi Razlighi, Sagi Polaczek, Daniel Cohen-Or, Ali Mahdavi-Amiri

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Transforms a frozen joint audio-video flow-matching model into separately editable, synchronized audio stems via a shared scene representation, improving source-level audiovisual control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00691)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Wensen Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Represents agent hypotheses as executable world models validated by retrospective transition and conditional prediction checks, offering a verification-aware framework for interactive environment dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00834)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Cheng Yang, Yifan Wu, Yutao Huang, Zhaohua Zhang, Beiduo Chen, Muxi Chen, Chenchen Zhao, Hexuan Deng, Haolin Yang, Geyuan Zhu, Sa Zhu, Jianhuan Zhuo, Qiuyong Xiao, Jianhao Ruan, Yiran Peng, Jiayi Zhang, Tian Ye, Xinlei Yu, Tianwen Jiang, Jihong Zhang, Yuyu Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses image generators as visual world models to synthesize action-conditioned GUI interaction trajectories, improving agent learning without deploying real software environments.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01215)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Ting Huang, Biao Wu, Ronghao Chen, Zeyu Zhang, Tengfei Cheng, Qizhen Lan, Huacan Wang, Hao Tang

**机构**: AIGeeksGroup

**💡 亮点 (Highlight)**: Proposes a hierarchical agentic control layer with persistent character/story states and reflection-guided repair that improves long-horizon coherence and identity consistency in text-to-video-and-audio generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00097)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Zhenyu Liang, Yining Huang, Yubo Zhao, Jack C. P. Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Physics-defined diffusion that generates spatiotemporal physical fields from sparse measurements, giving a transferable mechanism for physics-consistent dynamics generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01759)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Chongyang Xu, Zhao Wu, Jin Chen, Yiming Jiang, Jinhui Ye, Yuming Jiang, Shifeng Zhang, Ziliang Feng, Mu Xu, Yilun Chen, Li Lu, Steven C. H. Hoi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a whole-body humanoid VLA policy from egocentric human video pretraining, offering a scalable route to learning embodied dynamics from human experience.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00438)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Rikhat Akizhanov (MBZUAI), Yangsong Zhang (MBZUAI), Nikolai Kaliazin (MBZUAI), Peter Wolf (ETH Z\"urich), Yoshihiko Nakamura (MBZUAI), Pascal Fua (EPFL), Fabio Pizzati (MBZUAI), Ivan Laptev (MBZUAI)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Jointly estimates human pose, contacts, and forces from video with physics-based supervision, providing a physically grounded dynamics representation relevant to world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00451)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Wenjie Wang, Yuanyuan Wang, Zixiang Jiang, Shaoan Xie, Mingming Gong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides identifiability theory for recovering nonlinear scalar dynamics parameters from video, offering insight into what physical parameters are learnable from visual observations of dynamical systems.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38877)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Cusuh Ham, Fabian Caba Heilbron, Josef Sivic, Bryan Russell

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds an entity-centric memory from user video collections to ground and iteratively critique multi-shot B-roll generation, improving identity and sequence-level consistency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01884)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 7/10

**作者**: Zhangyong Liang, Haibin Ling

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: One-step physics-constrained flow matching with manifold preconditioning improves sampling efficiency for physical field generation, only indirectly transferable to video world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.40287)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Yu Huang, Jungang Li, Zhiyuan Wang, Yonghua Hei, Song Dai, Jiayu Yang, Deyuan Liu, Xiang Zheng, Xiaoshuang Shi, Hao Cheng, Kaidi Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmarks visual text rendering in video generation and proposes a keyframe-guided agentic refinement framework, exposing a concrete failure mode of current video models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01499)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Seungeun Rho, Jeonghwan Kim, Xue Bin Peng, Sehoon Ha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Self-play skill discovery yields a compact discrete action abstraction for controllable embodied agents, weakly relevant to action-conditioned world-model control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.40137)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana, Qinrong Cui, Erland Hilman Fuadi, Zayd M. K. Zuhri, Nanda Ryaas Absar, Ahmed Elshabrawy, Wilfried Ariel Mulyawan, Shoubin Yu, Yue Zhang, Mohit Bansal, Alham Fikri Aji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a goal-directed egocentric video-generation benchmark and reference-free judge revealing failures in multi-step physical reasoning and persistent world modeling, useful for evaluating world-simulator capabilities.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01092)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye, Rocky Duan, Nika Haghtalab, S. Shankar Sastry, Pieter Abbeel, Haozhi Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds simulation-based practice tasks and symbolic skills for embodied agents without weight updates, weakly related to world-model learning via simulation-based self-improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02204)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yoshiki Takebayashi, Giovanni Perantoni, Hikaru Sasaki, Matteo Saveriano, Takamitsu Matsubara

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Estimates demonstration feasibility from the robot's own experience for imitation from observation, weakly relevant to learned dynamics under embodiment mismatch.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01171)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Edward W. Staley, Connor O. Pyles, Rahul Hingorani, Frank Camargo, Griffin Milsap, Jared Markowitz, Matthew S. Fifer, Michael Wolmetz

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Explores EMG and visual segmentation as continuous task conditioning for VLA policies, showing gains in cluttered out-of-distribution scenes but only weakly touching world-model or video-generation interests.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01794)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Wonguen Cho, Junhoo Lee, Nojun Kwak

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a renderable metric-pose-anchored 3D Gaussian dataset with per-scene reliability for robot manipulation, offering only indirect relevance to learned dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.01744)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Haojian Huang, Pukun Zhao, Zexi Li, Yehang Zhang, Yangkai Wei, Wenqian Li, Han Yang, Kaiwen Zhou, Ying-Cong Chen, Yinchuan Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark study of VLM agents on embodied tasks that offers limited world-model or video-generation insight, but is plausibly adjacent to embodied dynamics understanding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.00854)

---

