# 💡 今日研究速览 (Daily Summary)

### World Models & Action-Conditioned Prediction

The dominant thread across today's submissions is a maturation of world-action modeling (WAM) from raw generative fidelity toward *what actually matters for control*. Several papers converge on the insight that the value of future modeling lies in *preparing* rather than *generating* the future: the empirical isolation of this effect (What Makes World Action Models Generalize) and Simple-WAM's single-forward-pass scheme show that latent-space preparation retains generalization at a fraction of pixel-generation cost, echoed by LRC-JEPA's disentanglement of controllable dynamics from residual context and AquaWAM's choice to model passive physical dynamics (inertia, buoyancy, drift) in compact navigation states rather than images. A second cluster attacks the *reliability* of recursive rollouts: state-affine latent transitions (Beyond One-Step Accuracy) demonstrate that eliminating nonlinear error propagation beats one-step accuracy for closed-loop planning, while ReSync diagnoses the commitment-evidence gap between asynchronous action and world-denoising clocks, and Revision-Not-Restart reframes predicted futures as *revisable* action conditions via a learned revision bridge. A third front targets *efficiency and horizon*: WorldAttention's hybrid sparse attention with hierarchical KV cache, WorldPlay2's compressed memory tokens and Stable Forcing distillation, Scope-WM's scoped latent computation, and training-free adaptive intermediate-state reuse collectively push interactive rollouts toward real-time latency without sacrificing historical context. Finally, the theory and evaluation side is catching up—What Must a World Model Distinguish formalizes mechanism/response/decision sufficiency as query-dependent, while OPIS and VehDyn expose that preserving specific input instances and kinematic consistency are far harder than generating plausible content, and that visual fidelity correlates weakly with dynamic correctness. The overall signal is a field shifting from "can we predict the future?" to "which projection of the future, at what cost, and sufficiency for which planning query?"

### Memory & Long-Horizon Reasoning

Memory is being reconceived from a passive buffer into an *active, learned retrieval problem*. Learning What to Recall introduces future-aware adaptive multi-cue episodic recall that learns which memories and retrieval cues to trust—directly targeting the long-horizon failure mode where agents retrieve plausible-but-irrelevant experience. This complements Where Memory Belongs (Ledger), which architecturally separates short-term in-policy memory from an external object ledger for VLA manipulation, improving object permanence under partial observability, and OPIS's benchmark finding that input-grounded instance preservation—not content plausibility—is the true bottleneck. On the reasoning side, WM-VLM probes internal world models for interleaved visual-textual reasoning, showing that generating intermediate visual states measurably improves mental rotation, while World SLAM Model unifies persistent SLAM-style state maintenance with future visual prediction for closed-loop navigation. Together these suggest a convergence on *structured, queryable, externally maintained* memory rather than monolithic context, with retrieval policy itself becoming a learnable component.

### Agents, Planning & Control

The agentic thread is defined by closing the loop between prediction and action under real-world imperfection. Counterfactual planning over WAM rollouts (Dynamic Manipulation) overcomes target-response collapse, and Test-Time Spatial Reasoning via generative real-to-sim runs massively parallel physics rollouts at test time—both treating the world model as a *simulator to be queried*, not just a predictor. Robustness under degraded sensing is a notable sub-theme: Learning to Act under Visual Interruptions pairs an action-conditioned world model with optical-flow extrapolation for camera loss, while SwingRL's age-aware world model propagates stale payload observations to the current control step. Self-Evolving Coding Agents proposes a striking representational shift—encoding task state and execution *as code*—with world-action models as callable tools, enabling reusable, revisable long-horizon behavior. Finally, safety-oriented work (Predictive Semantic Safety) converts VLM-predicted physical events into calibrated occupancy for safety-critical control, and PF-RL learns a goal-conditioned progress field to supply dense credit for long-horizon VLA tasks—together indicating that planning is increasingly framed as *value geometry over learned latent dynamics* rather than search over explicit states.

### Vision-Language-Action & Robot Learning

VLA research today splits between *future-aware policy learning* and *scalable adaptation*. SLIP-VLA equips policies with single-step latent imagination via action-conditioned latent world modeling and inverse dynamics, tightly coupling future latent transitions to actions—an efficient alternative to full rollouts. MM-ABC uses a training-only future-imagination branch as auxiliary supervision for mobile manipulation, and FutureDuet decouples main and wrist future supervision to separately capture scene evolution and local interaction dynamics. On adaptation, RoboFL's federated expert assembly via slotted LoRA adapters and routing distillation, WAM-OPD's on-policy distillation with prefix-weighted trajectory replay, and AnyStep-WAM's budget-aligned distillation all target *post-training without repeated environment rollouts*—a pragmatic response to the cost of real-world data. Data-efficiency and self-improvement round out the picture: F4R reconstructs real-world failures into interactive object-centric simulations for closed-loop refinement, and Robot-GST builds a Gaussian-Splatting real-to-sim environment to evaluate candidate action sequences before execution.

### Video Generation & Diffusion Distillation

Few-step and post-training methods for video diffusion are consolidating around *distribution-matching objectives with better-behaved critics*. PDMD introduces a projected distribution-matching distillation that filters critic error to stabilize few-step sampling across visual, motion, and audio quality, while From Scores to Samples (Elastic Forcing) replaces DMD score models entirely with an MMD objective in frozen self-supervised video representation spaces—enabling memory-efficient few-step autoregressive post-training and new style acquisition. G³-LoRA organizes reward-weighted video post-training data by *gradient compatibility* rather than reward alone, a transferable recipe for reward-weighted fine-tuning. On the geometric side, Lagrangian–Hamiltonian Flows brings a symplectic perspective to video prediction and image generation, improving efficiency and FID via transport-source dynamics. Capability control is also maturing: CapField-OPD learns a continuous capability field for multi-teacher on-policy distillation in flow models, enabling coordinate-based control that should transfer directly to controllable video generation.

### 3D, Geometry & Novel View Synthesis

Geometry-conditioned generation is emerging as the reliability layer for world-consistent synthesis. GeoVerse injects video-generative appearance priors into a 3D geometric latent diffusion model with global spatial memory, while GenNVS conditions a video diffusion model on *disentangled* 3D Gaussian geometry priors for spatial coherence—both converging on the idea that explicit geometric latents, not implicit video priors alone, are what enforce cross-view consistency. RoGSW4RLD pushes this into robotics, using feed-forward 4D Gaussian lifting to convert action-conditioned multi-camera rollouts into a unified, time-queryable metric scene, and CoDrive applies shared world-coordinate positional encoding with interleaved local/global attention for cross-vehicle consistent driving video. VideoPhysEdit closes the loop between geometry and physics by reconstructing rigid-body scenes and simulating interventions to guide downstream motion generation.

### Physical Dynamics & Simulation

Learned dynamics models are increasingly *hybrid*—coupling learned components with known physical structure. NEMSim compiles event-attribute priors into executable control-conditioned transition structure, improving generalization and data efficiency, while the graph-network coarse-step model uses Newmark-beta semi-implicit updates with virtual-hub coupling to recover *unobserved* mechanical response over long horizons. VIDEAS distills explicit action preconditions and effects from demonstration videos into language-based world models with prior-guided trajectory simulation for physical consistency. Notably, AD-E2E-JEPA's SIGReg-regularized learnable projector shrinks JEPA planning patches for 100× faster action-conditioned rollouts in end-to-end driving—a reminder that representation geometry, not just architecture, governs planning cost.

### Benchmarks, Evaluation & Theory

A welcome evaluative turn is visible. OPIS isolates multi-object memory failures with input-grounded object-centric probing, and VehDyn provides synchronized vehicle-dynamics ground truth revealing weak correlation between visual fidelity and kinematic consistency—both challenging the field's implicit assumption that better-looking rollouts mean better world models. What Must a World Model Distinguish supplies the missing theoretical scaffolding with a hierarchy of mechanism, response, and decision sufficiency, and Robot-GST offers geometry-aware evaluation of candidate actions pre-execution. Together these suggest the community is beginning to demand *task-relative* evidence of world-model quality rather than perceptual metrics alone.

### Efficiency, Compression & Inference

Efficiency work today is unusually *inference-centric and training-free*. Efficient World Action Model Inference adapts retained intermediate denoising/replan states across replans, steps, and layers without retraining; Scope-WM scopes computation to prediction-relevant latent regions and reuses promising action sequences; AnyStep-WAM allocates denoising steps in a scene-dependent, budget-aligned manner. On the architecture side, WorldAttention's hierarchical KV cache and WorldPlay2's compressed memory tokens attack the long-horizon memory-latency tradeoff directly, while AD-E2E-JEPA's shrunken projector achieves order-of-magnitude rollout speedups. The unifying theme is *adaptive, content-aware compute allocation*—spending FLOPs where the planning query demands them—rather than uniform compression, which aligns neatly with the sufficiency-based framing emerging in the theory literature.

### Human & Multimodal Generation

Interactive human generation is moving toward *persistent, adaptive, streaming* behavior. FlowAct-R2 combines streaming multimodal references with rolling action prompts and historical motion conditioning to reduce drift in long-horizon humanoid video, and EvolvingAvatar applies test-time training with persistent fast weights so a causal head-motion generator adapts to unfolding conversational context—a transferable mechanism for any dynamics model that must track a non-stationary context. WorldTS extends latent world modeling to multimodal covariate-aware time-series forecasting, a reminder that the latent-dynamics recipe generalizes well beyond pixels.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Renping Zhou, Zanlin Ni, Zihao Fan, Guohao Fu, Zeyu Liu, Hao Shi, Jie Zhang, Chi Bene Chen, Yang Yue, Xueyang Fu, Gao Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Empirically isolates why future modeling in world action models aids generalization, showing the benefit comes from preparing (not generating) the future, and proposes Simple-WAM, a single-forward-pass future-modeling scheme that retains generalization at latent-WAM efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34981v1)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Haiyu Zhang, Wenqiang Sun, Tengfei Wang, Junta Wu, Jun Zhang, Yunhong Wang, Yu Qiao, Chunchao Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Interactive video world model with factorized hybrid control, compressed memory tokens for long-horizon rollouts, and Stable Forcing distillation for real-time responsiveness.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35560v1)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zeyu Zhang, Jinyuan Mao, Dakai An, Wangbo Zhao, Hanfeng Lu, Jiasheng Tang, Yinghao Yu, Wei Wang, Bohan Zhuang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Efficient attention architecture with hybrid sparse attention and hierarchical KV cache enabling long-horizon, low-latency interactive video world models without sacrificing historical context.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34606v1)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xi Lin, Feihong Zhang, Yulong Shi, Yanghong Mei, Zuxing Lu, Xiaofan Zhu, Zihao Liang, Zhirui Gao, Zhaowen Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes the commitment-evidence gap between asynchronous action and world denoising clocks in world-action models and re-aligns computation to improve rollout success without retraining.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33944v1)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Beomsu Kim, Chieh-Hsin Lai, Bac Nguyen, Amir Bar, Jong Chul Ye, Yuki Mitsufuji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes future-aware adaptive multi-cue episodic recall that learns which memories and retrieval cues to trust, directly advancing long-horizon memory in world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34677v1)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Boyuan Zhang, Yingjun Du, Xiantong Zhen, Ling Shao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows state-affine latent transitions eliminate nonlinear error propagation in recursive rollouts, improving closed-loop visual planning despite worse one-step accuracy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33595v1)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Luzhe Huang, Lei Chu, Jingyi Liang, Yuhuan Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Disentangles controllable dynamics from residual visual context in a compact JEPA world model, improving latent-space planning efficiency and robustness.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34375v1)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuheng Zha, Yilei Wang, Qiyue Gao, Junrong Chen, Yujia Wu, Zhengfeng Lai, Zhengzhong Liu, Eric P. Xing

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Equips a VLM with a lightweight world-model branch that generates intermediate visual states for spatial reasoning, showing internal visual dynamics improve mental-rotation performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34826v1)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sunwoo Park, Wonbin Lee, Seonghyun Jin, Youngmin Kim, Jangho Park, Jong Chul Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a world-action model's predictive rollout for counterfactual planning to overcome target-response collapse in dynamic manipulation, a concrete world-model insight for controllable rollout.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33172v1)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jia Song, Wenhow Li, Lichen Bai, Bada Ye, Zeke Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Gradient-guided grouped LoRA organizes reward-weighted video post-training data by gradient compatibility, a transferable training strategy for improving text-to-video quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35189v1)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Vinay Sharma, Olga Fink

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Graph-network dynamics model with Newmark-beta semi-implicit updates and virtual-hub coupling enables long-horizon coarse-step prediction and recovers unobserved mechanical response, a broadly useful learned-dynamics insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30344)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jianan Wang, Haoquan Zhai, Siyang Zhang, Bin Li, Juan Chen, Jingtao Qi, Zhuo Zhang, Enze Wang, Haoxiang Jin, Chen Qian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distills explicit action preconditions and effects from demonstration videos into language-based world models, with prior-guided trajectory simulation for physical consistency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33464v1)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Minghui Qin, Yijun Yuan, Weicheng Zheng, Kenan Li, Weibang Wang, Chang Sun, Junhao Huang, Anmin Liu, Yicheng Yao, Hang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unifies SLAM-style persistent state maintenance and backend refinement with future visual state prediction for long-horizon world modeling and closed-loop navigation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.32626v1)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pengyiang Liu, Junbo Niu, Wenhao Zheng, Xinchen Chen, Canyu Li, Zhongyue Shi, Jiahao Xie, Si Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Maintains predicted visual futures as revisable action conditions via a learned revision bridge, improving closed-loop world-action model control after execution feedback.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35439v1)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Rongzhe Wei, Hans Hao-Hsun Hsu, Peizhi Niu, Yifan Li, Pan Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formalizes a hierarchy of mechanism, response, and decision sufficiency for world models, showing what a model must preserve depends on the planning query and proposing a modular query-conditioned design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33030v1)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chunzheng Li, Zesheng Jia, Hongda Zhang, Jiaying Tang, Yuntian Wang, Siao Liu, Jin Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Scopes computation to prediction-relevant latent regions and reuses promising action sequences, cutting visual world-model planning memory and latency while preserving task performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33218v1)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tingyu Yuan, Ziming Ji, Biaoliang Guan, Wen Ye, Wenrui Tian, Zhaopeng Gu, Feihong Zhang, Xu Yang, Yan Huang, Zhaowen Li, Chaoyang Zhao, Jinqiao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes dynamic next-state prediction that supervises a world-action model across multiple projections of the same future, improving cross-embodiment dynamics learning and control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34414v1)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiawei Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a symplectic Lagrangian-Hamiltonian flow framework for video prediction and image generation, improving efficiency and FID via geometric transport-source dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35710v1)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chi Zhang, Yueyi Liu, Haoyang Shi, Ruichuan An, Haoyu Li, Yuhang Wu, Sen Cui, Miao Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replaces DMD score models with an MMD objective in frozen self-supervised video representation spaces, enabling memory-efficient few-step autoregressive video post-training and new style acquisition.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35491v1)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoran Zhu, Wancong Zhang, Yann LeCun, Anna Choromanska

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a SIGReg-regularized learnable projector that shrinks JEPA world-model planning patches and embeddings for 100x faster action-conditioned rollouts in end-to-end driving.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34085v1)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zimo Wang, Junkun Yuan, Angtian Wang, Haotian Yang, Canyu Zhang, Siyuan Yuan, Xingchang Huang, Bo Liu, Yizhi Wang, Yiding Yang, Chongyang Ma, Gordon Guocheng Qian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a projected distribution-matching distillation objective that filters critic error to stabilize few-step video diffusion sampling and improve visual quality, motion, and audio.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35768v1)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jie Wu, Yuzhi Huang, Junqi Liu, Weichen Zhang, Haibin Huang, Yin Chen, Jingyan Jiang, Chi Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decouples main and wrist future supervision in a world action model, using RGB, interaction masks, and latent prediction to better capture scene evolution and local interaction dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34362v1)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jin Hyun Kim, Min Young Kim, Soohwan Song, Daekyum Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Feed-forward 4D Gaussian lifting that converts action-conditioned multi-camera world-model rollouts into a unified, cross-view-consistent, time-queryable metric scene.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35311v1)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Cunhao Zhu, Yifeng Wang, Dongliang Xu, Yunzhong Hou, Yue Yao, Chi Harold Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a dynamics-aware world action model that explicitly captures passive physical dynamics such as inertia, buoyancy, and drift in compact navigation states rather than predicting future images.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33299v1)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tianfu Li, Haoxuan Xu, Wenbo Chen, Haitian Li, Changchuan Yang, Xinhu Zheng, Jun Ma, Yuan Liu, Lujia Wang, Haoang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Equips VLA policies with single-step latent imagination via action-conditioned latent world modeling and inverse dynamics, coupling future latent transitions to actions for efficient future-aware control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33575v1)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu Meng, Baining Zhao, Junta Wu, Tengfei Wang, Rongze Tang, Haiyu Zhang, Wenqiang Sun, Chen Gao, Zhibo Chen, Xinlei Chen, Yong Li, Xiao-Ping Zhang, Chunchao Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Multi-vehicle driving world model that jointly generates cross-agent consistent video with precise trajectory control via interleaved local/global attention and shared world-coordinate positional encoding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34749v1)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Conghan Yue, Yuanjie Chen, Yue Han, Ya Gao, Yunyan Xiao, WeiYao Zhang, Zhineng Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces physical counterfactual video editing that reconstructs rigid-body scenes and simulates interventions to guide downstream motion and interaction generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35134v1)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junsong Yu, Junjie Xie, Pengwei Liu, Dong Ni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a neural event-mechanism simulator that compiles event-attribute priors into executable control-conditioned transition structure, improving generalization and data efficiency for learned physical dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30718)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Injects video-generative appearance priors into a 3D geometric latent diffusion model with global spatial memory to improve cross-view world-consistent novel view synthesis.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35734v1)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Ziyao Huang, Zhengkun Rong, Shiyang Qin, Shuang Liang, Wentao Hu, Yuxuan Luo, Yuan Zhang, Mingyuan Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Streaming multimodal reference diffusion transformer with rolling action prompts and historical motion conditioning that reduces drift for long-horizon interactive humanoid video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35728v1)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Mingle Jiang, Rui Xu, Yunke Wang, Chang Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies closed-loop VLA behavior under camera loss and proposes an action-conditioned world model plus optical-flow extrapolation to supplement missing observations during manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35003v1)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zhinnan Liu, Haozhi Han, Ruge Zhang, Teng Ma, Tao Ma, Zheng Liu, Yifeng Chen, Yunquan Zhang, Ting Cao, Yunxin Liu, Kun Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free inference acceleration for world action models by adapting retained intermediate denoising/replan state across replans, steps, and layers, improving closed-loop rollout latency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34608v1)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Hongcheng Gao, Jingjing Zhou, Zelin Zheng, Shijia Ge, Jay Zhu, Yazhe Wang, Jianshu Zeng, Xuan Shangguan, Di Wu, Lingyu He, Zhiqi Jia, Sihang Wu, Xiao He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes representing task state and execution as code for physical agents, using world-action models as tools and enabling reusable, revisable long-horizon behavior.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35432v1)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 5/10

**作者**: Hao Wang, Tao Yu, Liuzhou Zhang, HeXin Wang, Haopeng Jin, Yuxuan Zhou, Xinming Wang, Hongzhu Yi, Xinye Li, Yuanlei Wang, Ping Nie, Yan Huang, Yuxuan Zhang, Pengfei Zhou, Yanyan Zou, Wei Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an input-grounded object-centric benchmark that isolates multi-object memory failures in video world models, revealing that preserving specific input instances is harder than generating plausible content.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35052v1)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 5/10

**作者**: Tianyi Wang, Wangsheng Du, Jiazhou Chen, Tianyi Zeng, Xiangyu Li, Jiseop Byeon, Yujin Wang, Yiming Xu, Yangyang Wang, Bingzhao Gao, Sikai Chen, Zhaomiao Guo, Junfeng Jiao, Christian Claudel, Alexandre Bayen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a controlled driving world-model benchmark with synchronized vehicle dynamics ground truth, revealing that visual fidelity correlates weakly with kinematic/dynamic consistency in generated futures.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33264v1)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Pengyang Ling, Yujie Zhou, Jiazi Bu, Yibin Wang, Xiaoxiao Ma, Yi Jin, Huaian Chen, Yuhang Zang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a continuous capability field for multi-teacher on-policy distillation in flow models, enabling coordinate-based capability control that could transfer to controllable video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34658v1)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Rongyu Zhang, Ruizhi Fan, Yunfan Lou, Hengyu Fang, Shenli Zheng, Chenrui Wu, Yili Jin, Li Du, Dan Wang, Yuan Du, Shanghang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Federated expert assembly for world-action models via slotted LoRA adapters and routing distillation, relevant to scalable training of action-conditioned world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34968v1)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Taekyung Kim, Salem Fradi, Yanning Dai, Mateusz Ostaszewski, Jürgen Schmidhuber

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a VLM to predict future physical events and object displacements, converting them into calibrated occupancy predictions for safety-critical control, offering a predictive visual-dynamics insight for robot world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34356v1)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Ivan Kapelyukh, Yafei Hu, Ran Gong, Brandon May, Tushar Kusnur, Laura Herlant, Karl Schmeckpeper, Edward Johns, Xiaohan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Performs test-time spatial reasoning by reconstructing real scenes into simulation-ready assets and running massively parallel physics rollouts, a generative real-to-sim approach relevant to learned dynamics and planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33982v1)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Guangming Wang, Xiaoyu Zhang, Yucheng Xin, Wanli Ma, Jiucai Liu, Yunxiang Ma, Joe Ingham, Haibing Wu, Yixiong Jing, Olaf Wysocki, Brian Sheil

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Age-aware world model propagates stale payload observations to the current control step, offering a narrow but useful insight on time-aligned latent state estimation under delayed sensing.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33053v1)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Zhuoyuan Yu, Jiacheng Wang, Tianle Liu, Yihua Ren, Peng Yu, Chen Bai, Ziheng Zhang, Yufei Jia, Jindou Jia, Yuhang Zhang, Xinrui Zhang, Shang Yujing, Yuxiang Chen, Chuhao Zhou, Tiancai Wang, Jianfei Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reconstructs real-world failures into interactive object-centric simulated environments for closed-loop policy refinement, offering a real-to-sim-to-real dynamics-learning loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35575v1)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Tanguy Dieudonné, Jack B. Jedlicki, Heng Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Splits short-term in-policy memory from an external object ledger for long-horizon VLA manipulation, improving object permanence and reference in partially observed tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34554v1)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Junjie Chen, Fei Wang, Kun Li, Yiqi Nie, Xun Yang, Yanbin Hao, Linfeng Zhang, Meng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Test-time training with persistent fast weights adapts a causal head-motion generator to evolving conversational context, offering a transferable idea for adaptive dynamics generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35616v1)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yuhan Zhu, Xiangfei Qiu, Hanyin Cheng, Wangmeng Shen, Chenjuan Guo, Bin Yang, Jilin Hu, Christian S. Jensen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Latent-space world-modeling forecasting framework that conditions learned state dynamics on multimodal covariates, offering a transferable latent-dynamics insight though not visual.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31162)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a video diffusion model conditioned on disentangled 3D Gaussian geometry priors to improve spatial coherence in novel-view synthesis, offering a transferable geometry-conditioning idea for video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34579v1)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Qiwei Liang, Guangyu Chen, Shaolong Zhu, Zikuan Xiao, Jinxuan Lu, Yifan Xie, Renjing Xu, Wenbo Ding, Tianxing Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Employs a training-only future-imagination branch as auxiliary supervision for mobile manipulation, providing a world-model-style predictive signal that improves perception and intent prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.35652v1)

---

## 47. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Panjun Liu, Xiaohan Lei, Shiqi Zhang, Yikun Wang, Yongxin Zhang, Mingyi Hu, Shida Sun, Jiateng Shou, Wengang Zhou, Jiajun Deng, Zhiwei Xiong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: On-policy distillation for world action models with prefix-weighted trajectory replay to adapt task performance without repeated environment rollouts, relevant to closed-loop dynamics learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.34250v1)

---

## 48. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Rui Wang, Xiangyu Wang, Donglin Yang, Yibo Li, Canyang Chen, Zhongrui Wang, Xiaojuan Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Budget-aligned distillation and adaptive denoising-step scheduling for world action models, improving efficiency of predictive visual-action generation with scene-dependent compute allocation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33748v1)

---

## 49. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a Gaussian-Splatting real-to-sim environment for simulating and evaluating candidate action sequences before execution, offering a geometry-aware dynamics model for long-horizon manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.33872v1)

---

## 50. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yunpeng Qing, Yilun Kong, Sixu Lin, Ming Zhou, Yiming Fei, Shuang Luo, Yixiao Chi, Haoming Gu, Jingyuan Liu, Changxu Wei, Zhi Hou, Changqing Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a structured goal-conditioned progress field over VLA features to provide dense credit, a latent dynamics/progress representation relevant to long-horizon world-model-style value geometry.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.32634v1)

---

