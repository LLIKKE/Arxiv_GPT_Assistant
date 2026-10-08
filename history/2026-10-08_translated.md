# 💡 今日研究速览 (Daily Summary)

### World Models for Video and Physical Dynamics

The dominant theme today is the maturation of world models from pure generative curiosities into controllable, geometry-grounded simulators. Several works confront the fundamental weakness of autoregressive rollouts: error accumulation over long horizons. Parallel Predictive World Models and GeoWM both sidestep recursive decoded-state feedback—the former via parallel causal trajectory prediction for faster CEM planning, the latter by directly forecasting scene geometry with flow matching—while Commit While Futures Agree turns the world model into a decision-making oracle, using Bayesian change-point detection over imagined futures to adaptively set action-chunk execution horizons. Complementing these efficiency and control advances, Identifiable World Models shows that frozen diffusion world models can be endowed with causally interpretable latent coordinates through lightweight contrastive alignment, and Tracking Is Not Permanence exposes a striking deficit: frozen video world models (V-JEPA 2, VideoMAE, Cosmos) fail to retain hidden objects, though object permanence can be cheaply installed as a training prior. The field is converging on the view that a useful world model must be explicit about geometry, state, and belief rather than merely plausible in pixels.

### Embodied Agents and Vision-Language-Action Models

A second cluster pushes VLA and embodied policies toward tighter coupling with predictive dynamics and structured exploration. ViDAL anchors continuous action latents in future visual dynamics via an Action VAE, yielding a dynamics-grounded action space that improves policy learning and optionally predicts future video. AutodidactWAM exploits the video-action asymmetry directly, self-distilling actions recovered from generated video through hand-pose estimation and inverse kinematics to boost closed-loop robot success. On the exploration side, EigenDEXplore demonstrates that human-motion priors are most effective when used to structure perturbations along eigenvector-correlated directions rather than reshaping the action representation itself. For long-horizon manipulation, PACE introduces progress-aligned demonstration context with fast-weight execution memory to combat stage confusion, and Humanoid Horizon scales whole-body loco-manipulation through parallel stage streams and dynamic starting. Notably, Artemis brings multi-agent structure to driving world models with a shared explicit 3D state and progressive memory updates, improving cross-view consistency and out-of-sight agent recovery.

### Navigation, Planning, and Belief-State Estimation

Navigation and planning papers today emphasize calibrated uncertainty and self-improving world models. RIWANav introduces a recursive self-improvement loop that jointly adapts an action-conditioned world model and policy via imagined rollouts and grounded self-curriculum, directly addressing the staleness problem when a world model must track an evolving policy. A Belief-State World Model for Catheter Navigation argues—in a planar proof of concept—that calibrated belief, not point-estimate accuracy, is the essential ingredient for reliable dynamics prediction under sparse fluoroscopy, framing the task as a POMDP with a physics-based belief model. Seeing the Invisible takes a complementary approach for VLA navigation, using physics-guided dynamic visual prompting to steer a frozen policy around invisible temperature and radiation hazards. Together these works suggest that robust embodied navigation increasingly depends on maintaining explicit, uncertainty-aware state representations rather than reactive perception.

### Representation Learning and Data Scaling for Embodied Systems

Several contributions target the substrate beneath embodied learning: better representations, data, and simulation infrastructure. LEAP shows that privileged point-cloud reconstruction with wrist-view dropout materially improves geometric visual representations for visuomotor policies, a simple recipe with broad applicability. EmbodiedSmith scales embodied pretraining data through a recursive self-improvement flywheel in simulation, jointly refining scenes and tasks, though its direct methodological contribution to world modeling is limited. ALIVE improves first-frame-guided video editing by making inserted objects participate in coherent interactions via a curated interaction dataset and VLM-predicted guidance, enhancing source preservation and temporal coherence. Finally, WorldSolver offers a benchmark-only probe of whether LLM agents can generate physics solvers that reproduce dynamic system behavior—an intriguing diagnostic of agentic physical reasoning. Across these papers, the trend is toward grounding representations and data pipelines in explicit physical and interaction structure rather than scale alone.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Peng Xie, Amr Alanwar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Probes what frozen video world models (V-JEPA 2, VideoMAE, Cosmos) retain about hidden objects, revealing object-permanence deficits in latent predictors and showing permanence can be cheaply installed as a training prior.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07355)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sitian Shen, Jiuming Liu, Mengmeng Liu, Yian Wang, Michael Ying Yang, Francesco Nex, Hao Cheng, Daniele De Martini, Ayush Tewari, Per Ola Kristensson

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a geometry-grounded multi-agent driving world model with a shared explicit 3D state, progressive memory update, and decomposed foreground-background control maps to improve cross-view consistency and out-of-sight agent recovery in generated video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07031)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuan Xu, Yixiang Chen, Qisen Ma, Jiabing Yang, Peiyan Li, Kai Wang, Jianhua Yang, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Anchors continuous action latents in future visual dynamics via an Action VAE, yielding a dynamics-grounded action representation that improves VLA policies and enables optional future-video prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08150)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wanjin Feng, Baobin Zhang, Ao Yu, Shibo Feng, Xi Wang, Xingyu Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replaces autoregressive world-model rollouts with parallel causal trajectory prediction, removing decoded-state feedback to improve long-horizon prediction accuracy and CEM planning speed.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08627)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jing Xie, Shouwei Ruan, Yubin Wang, Yuxiang Zhang, Haitao Yang, Songchang Jin, Dianxi Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a recursive self-improvement loop that jointly adapts an action-conditioned world model and policy via imagined rollouts and grounded self-curriculum, addressing world-model staleness during policy evolution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08640)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mehrdad Noori, Guile Wu, Sam Hosseini, Dongfeng Bai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a geometry world model that directly forecasts future scene geometry at specified horizons via flow matching, avoiding recursive rollout error accumulation and reducing inference cost.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07381)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuyan Li, Yujia Wang, Yusong Huang, Junjie Yang, Yanggang Sheng, Ziyi Shi, Wenpeng Xu, Xiaoyang Zhou, Haoang Li, Hongliang Lu, Xinhu Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses an action-conditioned world model to imagine futures of candidate action chunks and derives execution horizon via Bayesian change-point inference on future consensus, a broadly useful world-model insight for closed-loop control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07949)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shangye Song, Dong Gong, Hong Jia, Yun Sing Koh, Xinyu Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free control-aware caching for interactive video world models that schedules denoising reuse based on action transitions and a frequency-mixed history prior, improving efficiency and WBench scores.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08777)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ruchi Sandilya, Conor Liston, Logan Grosenick

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows frozen pretrained diffusion world models can be equipped with identifiable, causally interpretable latent coordinates via a lightweight contrastive alignment map, advancing latent dynamics identifiability.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07028)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zhenghong Zhou, Zhe Lin, Jiebo Luo, Yuqian Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves first-frame-guided video editing by making inserted objects participate in coherent interactions, using a curated interaction dataset and VLM-predicted guidance for better source preservation and temporal coherence.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08779)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Sergei Kurchev, Iaroslav Kolomiets, Miguel Altamirano Cabrera, Artem Lykov, Dzmitry Tsetserukou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Exploits the video-action asymmetry in world-action models by self-distilling actions recovered from generated video via hand-pose estimation and inverse kinematics, improving closed-loop robot success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08119)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Stefano Maria Pizzamiglio, Stefano Pagani, Francesco Regazzoni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends Latent Dynamics Networks to variable initial conditions via auto-decoding and meta-learning, yielding a resolution-independent latent dynamics surrogate with structured, physically meaningful latent states.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08475)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Damini Rijhwani

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates sparse-fluoroscopy navigation as a POMDP with a physics-based belief-state world model, arguing calibrated belief rather than point-estimate accuracy is essential for reliable dynamics prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08469)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yenan Chen, Junjie Shi, Lu Chen, Zhongxiang Zhou, Rong Xiong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces progress-aligned demonstration context with fast-weight execution memory to mitigate stage confusion in long-horizon robot manipulation, offering a transferable insight for action-conditioned world-model rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07917)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Siru Jiang, Yongzhe Lyu, Shuo Lu, Yubin Wang, Yuxiang Zhang, Yue Liao, Bin Wang, Jian Liang, Tieniu Tan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmarks LLM agents on generating physics solvers for dynamic system simulation, providing a benchmark-only probe of whether agents can reproduce physical dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08720)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Harsh Gupta, Tyler Ga Wei Lum, Changhao Wang, Chuer Pan, C. Karen Liu, Jeannette Bohg, Shuran Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows human-motion priors are best used to structure exploration via eigenvector-correlated perturbations rather than changing action representation, a transferable insight for embodied dynamics learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07681)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yikai Qin, Yifei Deng, Mingjian Liang, Wenxuan Song, Zepeng Lin, Zhiyi Jiang, Jiajun Fu, Qiao Sun, Huashuo Lei, Xicheng Gong, Jiayi Chen, Han Zhao, Shuanghao Bai, Pengxiang Ding, Pengwei Wang, Haoang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Simulation data-generation flywheel with joint scene-task refinement for embodied pretraining; relevant to embodied dynamics data but offers limited direct world-model or video-generation method insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07969)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Haozhuo Zhang, Qiang Zhang, Jian Tang, Mingzhe Ni, Michele Caprio, Angelo Cangelosi, Wei Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Long-horizon whole-body loco-manipulation policy training with parallel stage streams and dynamic starting; adjacent to long-horizon embodied dynamics but no learned world model or video generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08320)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Hojoon Son, Fan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses physics-guided dynamic visual prompting to steer a frozen VLA policy around invisible hazards, a weakly related but transferable idea for controllable embodied dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07558)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Han Fang, Yunpeng Jiang, Jianshu Hu, Zhiyuan Guan, Ruiguo Sun, Shujia Li, Paul Weng, Xiao Li, Yutong Ban

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Privileged point-cloud reconstruction with wrist-view dropout improves geometric visual representations for visuomotor policies, offering a weakly related representation-learning insight for embodied dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.07015)

---

