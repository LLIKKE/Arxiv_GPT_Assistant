# 💡 今日研究速览 (Daily Summary)

### World Models & Video Generation

Today's submissions reveal a striking convergence around the maturation of world models from research curiosities into deployable systems, with three complementary thrusts. First, **efficiency and real-time interactivity**are being aggressively pursued: Waypoint-1.5 delivers playable video generation on consumer hardware, HelixWorld extends this to synchronized audio-visual rollouts, and SoL-Refiner collapses high-resolution refinement into a single denoising step—collectively signaling that the field is optimizing for latency-bound deployment rather than raw sample quality alone. Second,**memory and long-horizon consistency**have become a central bottleneck: Honeycomb's constant-size scene memory, Compress-to-Remember's on-policy distillation of compact memory tokens, MemEvo's automated discovery of streaming memory programs, and Rollout-Marginal Distillation all attack the problem of persistent state without unbounded storage growth, suggesting the community is converging on the view that memory architecture—not model scale—is the key lever for temporal coherence. Third,**reward alignment and evaluation integrity** are receiving overdue scrutiny: CoRe identifies latent reward hacking in video diffusion, RolloutFaith audits how persistent interventions propagate through generated frames, and CrossTimeEdit demonstrates reward-guided editing with multi-reward Flow-GRPO, indicating that as world models become policies, the fidelity of their reward signals and the auditability of their internal corrections will be as important as their generative capacity.

### Latent Dynamics & Planning Representations

A rich cluster of work today interrogates the *geometry* of latent spaces used for planning and control, moving beyond the assumption that well-behaved representations emerge from generic regularization. The Anisotropic Representations paper shows that isotropic latent regularization in JEPA-style models actively misaligns the planning metric with task cost—a pointed critique of a common default—while ATLAS preserves relational latent geometry via pairwise structure transport, and the Bilinear World Models work enforces action recoverability through bilinear-parameterized dynamics to achieve orders-of-magnitude faster planning. Abductive World Modeling adds causal structure by inferring latent causes, and Lucid Dreaming introduces transition-level doubt with multiplicative trust propagation for uncertainty-aware imagination. Together these papers suggest a field-wide shift from "learn a good representation and plan in it" toward "engineer the latent geometry so that planning is well-posed," with anisotropy, action-recoverability, relational structure, and calibrated uncertainty emerging as first-class design objectives rather than emergent properties.

### Robot Learning & Embodied Action from World Models

The most active frontier today is the translation of pretrained world models into robot action, with several papers demonstrating that frozen generative backbones can be *actualized* rather than fine-tuned. One-from-Infinity shows a tiny task-conditioned selector suffices to extract actions from a frozen video world model; World4Scorer supervises a trajectory-conditioned JEPA model with simulator outcome labels to score unexecuted plans; and MVG-WAM structures multi-view observations as epipolar-constrained geometric states for manipulation. On the data side, Real2Gym builds interactive simulation gyms from real videos, VidAct learns object-centric 3D-aware policies from in-the-wild monocular video, and Video2STL grounds VLM-generated temporal specifications into robot policies—collectively reducing the dependence on teleoperated demonstrations. Complementing these, CogWAM aligns semantic cognition with world-action modeling via event-driven interfaces, and the Staircase Policy streams inference for large action chunks. The throughline is clear: the field is converging on world models as *reusable action substrates*, where the core challenge shifts from learning dynamics to faithfully extracting and conditioning on them for closed-loop control.

### Memory, State Abstraction & Agentic Systems

A distinct thread today addresses how agents should remember, forget, and reuse experience—spanning both robot policies and video agents. Simple Agentic Memory argues provocatively that compact interaction-derived state outperforms retained visual history for memory-dependent control, while Remember-What-You-Did adds action-history memory with dual-expert denoising for long-horizon VLA policies. VideoLoop introduces a bounded working-memory rewrite loop to combat semantic thrashing in long-form video agents, and the "Successful Memories Mislead" paper shows that post-retrieval memory adaptation is necessary because retrieved trajectories can actively harm task-conditioned execution. This cluster collectively challenges the intuitive "more context is better" assumption, suggesting that *structured, compact, and task-conditioned* state abstractions—rather than raw history retention—are the key to long-horizon agentic competence.

### Efficient Video Restoration & Generation Infrastructure

Several papers target the inference-time efficiency of video systems, offering transferable techniques for the broader generation stack. ReCaVSR recycles SR latents with learned layer-wise KV-cache routing, RelayVSR combines sparse keyframe relay with dual-memory transformers and RL-based reference optimization, and FastVR achieves streaming one-step diffusion restoration with chunk-wise causal attention. Salt++ introduces causal self-flow and context-aligned autoregressive DMD for few-step streaming audio-video generation, while MeanFlowAdvantage proposes an advantage-weighted objective that preserves native few-step sampling. These works collectively indicate that *cache management, latent recycling, and distillation-aware objectives* are becoming the standard toolkit for making high-fidelity video systems tractable at streaming rates—a prerequisite for the interactive world models above.

### Simulation, Physics & Structured Dynamics

A smaller but notable set of papers grounds learned dynamics in differentiable physics and structured simulators. PowerSim couples power-diagram scene representations with differentiable MPM physics, offering a physically grounded substrate relevant to world models. The low-fidelity sim-to-real result for robotic fish makes the counterintuitive but valuable point that dynamics fidelity need not reside in the simulator when the controller is robust. Variational Koopman autoencoders bring uncertainty-aware latent linear dynamics to time-series forecasting, and the physics-guided microstructure evolution model demonstrates long-horizon learned dynamics surrogates in a scientific domain. These papers reinforce that *structured, physics-aware inductive biases* remain competitive with—and often complementary to—large-scale learned dynamics.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jack Wei Lun Shi, Kaichen Zhou, Haoyu Chen, Yufeng Weng, Keane Ong, Ruojin Cai, Hang Hua, Justin K. W. Yeoh, Mengyu Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces HexMemory, a constant-size low-rank plane representation for persistent scene memory in video world models, enabling long-horizon consistency without growing storage.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37690)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Lei Ke, Jiahao Pan, Zeyue Tian, Jiaming Wang, Haoyuan Huang, Kam Man Wu, Pengjun Fang, Hongyu Liu, Chenyang Qi, Lin Wang, Ruibin Yuan, Weijia Chen, Fangneng Zhan, Qifeng Chen, Wei Xue, Yike Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends interactive world models to synchronized spatial audio-visual rollouts with 6-DoF camera control and few-step streaming distillation, adding a new multisensory dimension to world simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38123)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 7/10

**作者**: Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn, Anmol Agarwal, Ryan Craig, Andrew Lapp, Mithun Hunsur, Sami BuGhanem, Scottie Fox, Aaron Sanders Carson Poole, Irene Park, Dave Rossi, Spencer Frazier, Louis Castricato

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a real-time interactive diffusion world model generating playable video conditioned on dense keyboard/mouse input, with a data pipeline, architecture, and runtime system for consumer-hardware latency constraints.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37107)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junchi Yao, Ziyi Wang, Youling Huang, Lijie Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a framework for auditing persistent internal interventions in visual world models, showing that sustained corrections propagate through generated frames or recurrent memory and proposing Delayed LoReFT to reward future consequences.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36843)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhaolong Su, Yujin Han, Feng Wang, Jameson Dong, Hins Hu, Difan Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies latent reward hacking in video diffusion alignment and introduces a co-evolving reward framework that refits the reward model on current generator samples to preserve perceptual and motion quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36245)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu Xu, Yuxin Zhang, Xiao Yang, Haotian Yang, Yizhi Wang, Xinwei Huang, Minxuan Lin, Angtian Wang, Chongyang Ma, Fan Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SplitMoE, a split-role sparse architecture with semantic and generic experts plus prototype-guided routing that improves video diffusion scaling, convergence, and generation quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38140)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sen Wang, Liu Liu, Xinjiang Wang, Zequn Chen, Haoyi Jiang, Taojun Ding, Tingyang Xiao, Zhizhong Su, Jie Wang, Sanping Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a cognition-guided world-action model with a persistent Semantic State and progress-conditioned WORLD/ACTION queries that align future-world prediction with task progress for closed-loop manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37721)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mingu Kang, Yoori Oh, Sookyung Kim, Joonseok Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that isotropic latent regularization in JEPA world models misaligns the planning metric with task cost, and fixes it with a learnable anisotropic covariance target that improves action-conditioned planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37441)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaoyu Wu, Weihang Guo, Yifei Wang, Xinze Feng, Lydia E. Kavraki, Zhiwei Steven Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns compact memory tokens via on-policy distillation from a frozen video generator to improve long-video memory and consistency without modifying the base model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36364)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haozhe Liu, Tian Ye, Shuchen Xue, Yitong Li, Junsong Chen, Haopeng Li, Jincheng Yu, Duomin Wang, Ruihua Zhang, Lei Zhu, Song Han, Enze Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: One-step refiner converts low-resolution video outputs into 4K video with a single denoising step, substantially improving high-resolution video generation efficiency and quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37969)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenbo Chen, Tianfu Li, Haoxuan Xu, Zhihao Cao, Zhenghan Chen, Zhengming Zhu, Zizhou Luo, Guosheng Yang, Yuan Liu, Lujia Wang, Wen Chen, Haoang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a multi-view geometry-aware world-action model that structures synchronized camera observations as epipolar-constrained global and view-indexed geometric states for robotic manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37793)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Antonio Pariente, Ignacio Boero, Nikolai Matni, Alejandro Ribeiro

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a JEPA-style world model with bilinear-parameterized latent dynamics that enforces action recoverability and enables orders-of-magnitude faster planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36305)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongbin Lin, Chaoda Zheng, Yiming Yang, Xiangyu Li, Shijia Chen, Jinhao Deng, Kangjie Chen, Dongbin Zhang, Jie Feng, Yu Zhang, Xianming Liu, Shuguang Cui, Boyang Wang, Zhen Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses an action-vision faithfulness evaluator to filter video world-model rollouts for closed-loop RL post-training of autonomous driving policies, addressing action-conditioning mismatch.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36851)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Gang Hua, Jianwen Xie, Zezhou Cheng, Zhuowen Tu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces last-frame layout as an explicit control signal for image-to-video generation under large viewpoint changes, with on-policy self-distillation transferring dense-layout teacher control to a sparse last-frame student.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38146)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chenjian Gao, Zhihao Hu, Jianqi Ma, Jun Zhang, Weidong Zhang, Tianfan Xue

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes rollout-marginal distillation that scores each autoregressive video chunk independently against a chunk teacher before video-level DMD, improving long-horizon visual quality and temporal coherence.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37925)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bang Du, Yichen Xie, Shuqi Zhao, Yuxin Chen, Menglin Wu, Masayoshi Tomizuka

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that a frozen pretrained video world model can be actualized into robot actions by a tiny task-conditioned selector, avoiding fine-tuning the world-model backbone.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36413)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jieyuan Pei, Meiyi Lu, Sining Ang, Yubo Zhao, Zhangyi Hu, Mingwei Xu, Haokai Ding, Wei Li, Zihan You, Jianwei Zheng, Li Yu, Yifeng Pan, Ji Tao, Rongjunchen Zhang, Yan Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trajectory-conditioned JEPA-style world model whose predicted states are supervised by simulator outcome labels, enabling scoring of unexecuted plans and improving closed-loop planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36438)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ke Fang, Yupu Yao, Lu Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: ATLAS preserves relational latent geometry via pairwise structure transport and Wasserstein marginal calibration, improving planning-relevant novelty structure and multi-step prediction in latent world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36333)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guoheng Sun, Chen Chen, Jin Wang, Ang Li, Teresa Lv

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Staircase Policy streams inference for world-action models by partitioning action chunks into staggered denoising sub-chunks and re-predicting future latents, improving long-horizon execution throughput.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36471)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziqi Liu, Songhan Yang, Linfan Zhou, Jiatong Liu, Lijun Peng, Long Wan, Yinqi Bai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces abductive inference of latent causes (entity/dynamic/relation) into latent-space world modeling, improving physical prediction, causal reasoning, and action understanding over V-JEPA.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36985)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziqi Wen, Ting Xu, Lianyu Wang, Xian Lin, Yanda Meng, Huazhu Fu, Meng Wang, Ching-Yu Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds Subjective-Logic transition-level doubt and multiplicative trust propagation to latent world models, improving uncertainty-aware imagination and planning without extra parameters or forward passes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37156)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xingtong Ge, Yutong Wang, Lunjie Zhu, Haitao Lin, Fangyu Lin, Yushi Huang, Xin Zhang, Yi Zhang, Yu Liu, Jun Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces causal self-flow and context-aligned autoregressive DMD for few-step streaming audio-video generation, improving visual and motion quality in causal video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36995)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yu Yuan, Yawen Lu, Guoxian Song, Kevin Duarte, Ratheesh Kalarot, Di Chang, Xijun Wang, Stanley H. Chan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Disentangles an editable dynamics token from visual context via self-supervised reconstruction, enabling language-guided video dynamics editing, retiming, and appearance-controlled re-rendering.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36496)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Songlin Yang, Xiaotong Zhao, Jiacheng Zhang, Zhe Wang, Toyota Li, Eric Liu, Alan Zhao, Anyi Rao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces adaptive reward routing and cross-modal influence-guided update localization to improve joint audio-video diffusion quality, alignment, and synchronization via forward-process RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37200)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kerui Ren, Yingxiang Xu, Kaiwen Song, Linning Xu, Bo Dai, Mulin Yu, Tao Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds interactive simulation gyms from real videos via Real2Sim2Real, reconstructing editable scenes and validating actions through physics execution to transfer manipulation skills to robots.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37089)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhenghao Ni, Weimin Qiu, Meng Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses self-consistency over multiple video-generation rollouts and distills consensus into the model, improving video-based reasoning and temporal prediction quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36826)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Xijun Wang, Xin Li, Suhang Yao, Zirui Lang, Bingchen Li, Zhibo Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves streaming video super-resolution efficiency and temporal consistency via recycled SR latents and learned layer-wise KV-cache routing, a transferable video-generation inference technique.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37831)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Trong-Tung Nguyen, Anand Bhattad

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Couples power-diagram scene representations with differentiable MPM physics for physically grounded dynamics and rendering, offering a differentiable simulation insight relevant to world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38153)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Guohong Liu, Jialei Ye, Shanhui Zhao, Yunxin Liu, Yuanchun Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Searches over executable memory programs to discover bounded streaming video memory mechanisms, relevant to long-horizon temporal state abstraction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36581)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Kaijun Luo, Yudi Huang, Qijun Zhong, Xinshuai Song, Yang Liu, Liang Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Active-vision manipulation policy that distills future evolution from a pretrained 4D model into a robot-centric 3D representation, providing future-aware geometric guidance relevant to predictive dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37292)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Anthony Frion, Lucas Drumetz, Guillaume Tochon, Mauro Dalla Mura, Ali Can Bekar, Abdeldjalil A\"issa El Bey

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a variational Koopman autoencoder with normalizing flows for uncertainty-aware latent linear dynamics, offering a transferable world-model insight for probabilistic long-horizon forecasting.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37435)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: T. Konstantin Rusch, Tim Seyde, Jared Boyer, Zach J. Patterson, Daniela Rus

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a depth-recurrent actor that adaptively allocates computation via shared-block looping, providing a latent-state dynamics/planning insight relevant to world-model-style sequential decision-making.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37432)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xijun Wang, Xin Li, Zirui Lang, Suhang Yao, Haoran Li, Zhibo Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a sparse keyframe relay plus dual-memory video transformer and RL-based reference optimization for efficient streaming real-world video super-resolution, a narrow but transferable video-generation efficiency idea.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37850)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Merve Atasever, Keyan Azbijari, Cagan Bakirci, Bo-Ruei Huang, Tolga Izdas, Zahra Shahrooei, Richard Yang, Erdem Biyik, Jyotirmoy V. Deshmukh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Converts observation-only videos into grounded temporal logic specifications for robot policy learning, offering a reusable representation of task dynamics from video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37519)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Hang Li, Mingxin Zhang, Zihan Wu, Yang Tian, Dong Chen, Fengyi Shen, Yuan Meng, Xiangtong Yao, Heng Zhang, Ziyuan Liu, Zhenshan Bing, Alois Knoll

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns object-centric 3D-aware manipulation policies from in-the-wild monocular videos by reconstructing object meshes and motion with residual trajectory transfer, providing object-centric dynamics supervision.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36870)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Michael Trimboli, Wenxi Liu, Xianqi Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Physics-guided fully convolutional spatiotemporal model for multi-frame 3D microstructure evolution prediction, offering transferable insight into long-horizon learned dynamics surrogates.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36504)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Liam Maloney, Simon Ramchandani, Mike Y. Michelis, Ronan Hinchet, Robert K. Katzschmann

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows a deliberately low-fidelity stateless fluid simulator suffices for zero-shot sim-to-real closed-loop control, offering a useful insight about where dynamics fidelity must reside.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36993)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xuyi Hu, Francesco Palandra, Shangzhe Wu, Daniel Cremers, Riccardo Marin, Silvia Zuffi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free monocular 4D reconstruction of articulated animals that decouples pose from shape and enforces temporal consistency, offering a weakly supervised route to recovering object-centric dynamics from video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37986)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xiaoxu Chen, Qin Yang, Haoran Bai, Sibin Deng, Ying Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Streaming one-step diffusion video restoration with lightweight VAE and chunk-wise causal attention improves temporal consistency and efficiency, offering transferable ideas for efficient video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36757)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yuyou Zhang, Yunbei Zhang, Miao Li, Janet Wang, Zijian Jin, Shilong Liu, Ding Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free structured state-based memory layer for robot policies, arguing compact interaction-derived state outperforms retained visual history for memory-dependent control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36595)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Haocheng Tang, Tianchi Xie, Xingqiao Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an advantage-weighted objective for few-step average-velocity generators that preserves native few-step sampling, with transferable relevance to efficient video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37670)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Junghyun Kim, Ngseo Kim, ChungWoo Lee, Seoyeon Lee, Woo-Jeong Baek, Adam Zhou, Chip Huyen, Jun-Ki Lee, Gi-Cheon Kang, Byoung-Tak Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns domain-invariant future latents for VLA policies via lookahead prediction, offering a weakly related latent-dynamics representation insight for embodied world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37165)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Hanwen Lu, Jun He, Mingjia Yang, Hao Wei, Jinhao Huang, Yi Lin, Xiang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Cross-view historical street-view generation framed as editing with multi-reward Flow-GRPO training, offering a transferable recipe for temporally grounded, physically plausible video editing.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36616)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains an MLLM to decode summary tokens into a compact 3D Gaussian Splatting scene representation, offering a weakly related spatial-representation insight rather than a dynamics or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38177)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Tan-Dzung Do, Tuan Dat Phuong, Nico Bohlinger, Cuc T. Trinh, Siwei Ju, Vien Anh Ngo, Jan Peters, Xinchao Wang, An T. Le

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distills a shared latent behavior space across humanoid embodiments via a unified encoder, offering a transferable latent-dynamics representation relevant to action-conditioned world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38087)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yaxin Zhao, Dianye Huang, Chenwei Wang, Chenguang Yang, Zhongliang Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Action-history memory with dual-expert denoising for long-horizon VLA policies; memory-conditioned steering is adjacent to world-model state abstraction but the contribution is policy-centric.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37307)

---

## 47. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jinfa Huang, Jianming Xu, Jingyang Lin, Zhengyuan Yang, Jiebo Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Bounded working-memory rewrite loop mitigates semantic thrashing in long-form video agents; a memory-management insight for long-horizon video understanding rather than generation or dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38119)

---

## 48. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: No\'e Lallouet, Michael Fischer, Elie Michel

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Performs reference-free 3D Gaussian splatting inpainting in a 3D-native generative prior space, adjacent to generative scene modeling but without a temporal dynamics contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37816)

---

## 49. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnostic benchmark for visual text rendering and in-place editing in video generation, with a benchmark-aligned preference-optimization signal that improves text fidelity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36598)

---

## 50. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Quanquan Li, Hongbo Zhang, Yihe Chi, Liuyang Song, Jingyu Li, Yuxiang Huang, Hongzhen Zhang, Guitao Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Post-retrieval memory adaptation for embodied agents that converts trajectories into condition-action-effect transitions, offering a weakly transferable insight for state abstraction and experience reuse in world-model-driven agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35808)

---

