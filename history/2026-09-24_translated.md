# 💡 今日研究速览 (Daily Summary)

### World Models & Generative Simulation

The dominant theme today is the maturation of world models from passive video predictors into structured, interactive, and executable substrates for embodied intelligence. A clear architectural split is emerging: several works explicitly decouple *what happens* from *how it looks*, with Code Plans, Diffusion Renders and GameDirector both separating rule-based or code-based logic from diffusion rendering, enabling persistent memory, player-configurable dynamics, and better state tracking. Complementing this, MachEmbodied-U0 and An Action Is Worth One Patch (PatchWAM) push toward unification, jointly generating RGB, depth, normals, optical flow, and actions within a single backbone, while Skytopia and ForeDrive argue that the *representation* underlying action-conditioned prediction—not the prediction itself—is what policies actually need, discarding the predictor at deployment or conditioning planners on JEPA-style latent futures. Efficiency and fidelity are advancing in tandem: QuantWM shows training-free 2-bit KV cache quantization can preserve temporal consistency in video world models, while Fysiverse-3D-Vision and φ-RIE generate executable, interactive 3D environments from single images or 3DGS reconstructions. Notably, the field is converging on a "generate-then-simulate" pipeline for robotics and driving (DreamStream, PhyVisGen, MotionForge), where generative priors supply physically grounded data and closed-loop testbeds rather than mere pixels.

### Embodied Agents, VLA & Robotic Control

Embodied policy learning is increasingly organized around predictive, geometry-aware, and uncertainty-aware representations rather than reactive mapping. HABILIS Brain 0 and Spatial-Interactor both inject dynamics-prediction signals into VLA training—via multiview geometry-change tokens and action-conditioned state-transition modeling respectively—suggesting that weakly supervised *dynamics pretraining* is becoming a standard recipe for spatial and physical reasoning. CableVLA and VisForce extend this conditioning to task-specific modalities, distilling future topology or grounding contact forces, while PLAT demonstrates that privileged latent transition learning can unlock long-horizon, goal-conditioned humanoid control from sparse keyframes. On the control side, learned dynamics models are being coupled with classical planners: deep bilinear Koopman models drive MPC for heavy machinery, biLSTM dynamics feed MPPI for deformable linear objects, and history-conditioned flow matching brings probabilistic, uncertainty-aware dynamics to continuum robots. Safety and deployment concerns are also surfacing, with SafeLoop introducing risk-aware rollback for manipulation and Deploying Foundation Models for Embodied Navigation tackling long-horizon memory via active memory heads—an abstraction insight likely transferable to world models more broadly.

### Evaluation & Benchmarks

A striking cluster of today's work targets the evaluation gap in world models, moving decisively beyond single-view visual quality. TriWorldBench introduces synchronized tri-view consistency as a metric for embodied world models, while FireWorldBench probes latent state inference, causal mechanisms, and intervention reasoning through coupled-field fire dynamics. RoboTwin-Phys directly interrogates whether WAMs and VLAs understand physics by varying mass, friction, and joint dynamics with ground-truth parameters, exposing robustness gaps, and MotionForge supplies a large-scale dynamic-manipulation benchmark with domain-shift and latency-aware protocols. Together these efforts signal a field-wide recognition that generative fidelity is a poor proxy for physical competence, and that benchmarks must stress causal, multi-view, and out-of-distribution generalization to be meaningful.

### Generative Methods & Infrastructure

Finally, several contributions offer transferable machinery for the broader generative stack. Mean Velocity Matching reformulates diffusion dynamics through a single-field mean-velocity parameterization that directly yields stochastic reverse-SDE drift—a potentially generalizable trick for video diffusion. COVER embeds watermarks in the latent space of a frozen generative video autoencoder with a differentiable codec surrogate, addressing provenance for generative video. Meanwhile, Generative Embodied Multiple Behavior Control Systems combines habit-memory controllers with context-aware world models for value estimation in human-like agents, hinting at tighter integration between behavior architectures and predictive world models.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zixun Fang, Yawen Shao, Kai Zhu, Jie Xiao, Shihan Chen, Yu Liu, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Explicitly constructs an executable code-based world with diffusion rendering to enable long-term memory, open-ended interaction, autonomous evolution, and persistent multi-agent dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26458)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decouples rule-based gameplay logic from video world-model rendering via an agentic director, improving state tracking, rule adherence, and action quality in interactive game world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25652)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free 2-bit KV cache quantization that preserves attention logits and temporal-spatial token selection to reduce flickering and improve temporal consistency in video generation and world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26425)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoran Wen, Wenfu Wang, Kunsong Shi, Jingke Wang, Wancheng Feng, Yiren Zhang, Yueran Zhao, Xuancheng Zhang, Nanfei Ye, Xingru Chen, Zhaohong Sun, Chengmin Yang, Zikang Yu, Penghao Bi, Jia Shi, Yu Liu, Kun Zhan, Yan Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified embodied model jointly generates future RGB, depth, normals, and optical flow alongside actions, providing a concrete visual-dynamics world-model contribution for control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25627)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziyang Leng, Sicheng Mo, Seth Z. Zhao, Haoyuan Cai, Yu Zeng, Rowan McAllister, Bolei Zhou

**机构**: VAIL-UCLA

**💡 亮点 (Highlight)**: Builds a simulator-grounded autoregressive video world model for closed-loop driving simulation, preserving policy-relevant scene layout and dynamic-object temporal consistency, plus a new policy-oriented sim-to-real metric.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26792)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sinuo Wang, Zichong Gu, Yuhan Huang, Wenxin Wen, Xun Yang, Yiqing Zhang, Xingyu Zhang, Ningyu Che, Jie Ling, Qiankun Yu, Wei Liu, Jing Xu, Xinggang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a planning-relevant JEPA-style latent world model and asymmetrically conditions a DiT planner on multi-horizon future latents via gated fusion and trajectory-adaptive bias.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26299)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Argues a policy needs the representation underlying action-conditioned prediction rather than the prediction itself, training a forward/inverse latent world model whose predictor is discarded at deployment for monocular drone navigation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26007)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tianheng Wang, Zhou Xie, Heng Jia, Jianhua Xu, Tong Zhang, Kaicheng Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unifies visual world prediction and continuous action generation in a single patch-based generative backbone via Action-as-Patch, removing the need for separate action heads or experts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25961)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Hang Yang, Tingcong Liu, Junjie Xiong, Fangju Yang, Ke Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a history-conditioned physics-informed flow-matching framework for probabilistic dynamics prediction of continuum robots, contributing a broadly useful approach to uncertainty-aware learned dynamics under incomplete observations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25658)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Kaixiang Yao, Xu Wang, Miao Pan, Hu Xiyue, Weishi Wang, Daniel Dahlmeier, Jintao Chen, Yongliang Shen, Xuhong Zhang, Wenqi Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains VLMs to model action-conditioned physical state transitions and integrate them over long interaction trajectories, yielding a useful representation-level world-model insight for embodied spatial reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23038)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jinu Pahk, Jesoon Kang, Taegeon Park, Jisu An, Soo Min Kimm, Jaejoon Kim, Byoung-Tak Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns multiview future-current geometry-change tokens as an embodiment-agnostic predictive representation for VLA policies, providing a weakly supervised dynamics-prediction signal relevant to world-model pretraining.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25558)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Dingkang Yang, Yizhou Liu, Wendong Cheng, Zizhi Chen, Shunli Wang, Yang Liu, Hongsheng Li, Lihua Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates executable 3D scenes from a single image by decoupling spatial layout reasoning from asset synthesis, yielding physically consistent, interactive environments relevant to world-model simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25741)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Zepeng Wang, Jiangxing Wang, Chao Ma, Xiaochuan Shi, Zongqing Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Privileged latent transition learning enables sparse timed keyframe humanoid motion tracking, offering a latent-dynamics insight for long-horizon goal-conditioned control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25754)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yu Zheng, Qiyu Feng, Yixin Wu, Baoquan Yang, Yixuan Zhou, Bingyang Hu, Kemeng Huang, Guansheng Yang, Hesheng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates physically and visually high-fidelity robotic manipulation data via IPC-based soft-contact coupling and real-scene path tracing, relevant to simulation-based dynamics and embodied data generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25653)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Chongyu Bao, Haokai Yang, Yuhan Wang, Zhaochong An, Kunpeng Liu, Xiaolan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Combines a habit-memory controller with a context-aware world model for action-consequence prediction and value estimation in embodied human-like agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22691)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Runyi Yang, Deheng Zhang, Xiaoye Wang, Kanzhi Wu, Lei Sun, Ajad Chhatkuli, Kunyu Peng, Luc Van Gool, Danda Pani Paudel

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Converts 3DGS reconstructions into interactive simulator assets by coupling movable-asset construction with background removal and completion, enabling object-level change and contact in reconstructed scenes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26795)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 7/10

**作者**: Yunhong Zhang, Changjie Cao, Zhihua Zhang, Bingli Liu, Zongjie Cao, Zongyong Cui, Ying Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a single-field mean-velocity parameterization that directly yields stochastic reverse-SDE drift, a generative-dynamics reformulation potentially transferable to video diffusion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25444)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Armin Abdolmohammadi, Navid Mojahed, Dinesh Kumar, Bahram Ravani, Shima Nazari

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns deep bilinear Koopman dynamics models of vehicle-terrain interaction for predictive control, offering a data-driven latent dynamics insight relevant to world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26580)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Shufan Sun, Chen Wang, Enxin Song, Jiatao Gu, Lingjie Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Hierarchical agentic reasoning with geometry refinement reconstructs compositional 3D scenes from a single image; adjacent to spatial world modeling but without temporal dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26793)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yuxin Cao, Hao Yang, Ziqi Ding, Jie Hao, Wei Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Embeds watermarks in the latent space of a frozen generative video autoencoder with a differentiable codec surrogate, a video-generation-adjacent technique for codec-robust latent payload recovery.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26236)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Mohan Liu, Dengchen Mei, Haotian Xian, Ruyang Han, Jiayi Sun, Xuanyu Chen, Haitian Zhang, Luxi Li, Kaimin Mao, Lin Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a large-scale dynamic-manipulation simulation benchmark and data-generation pipeline with domain-shift and latency-aware protocols, offering a testbed for evaluating learned dynamics in continuously evolving scenes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25689)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Jiaqi Zhang, Feng Ye, Mingjia Yang, Zhihong Chen, Mingkang Xiang, Xinglin Yao, Yanbin Li, Siwei Ma, Chuanmin Jia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Physics-diverse manipulation benchmark with ground-truth physical parameters and demonstrations that exposes robustness gaps in WAMs and VLAs under varying mass, friction, and joint dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26292)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Qiang Chen, Hao Guo, Huatai Zhu, Tairan Huang, Yichao Cao, Hongyan Xu, Keke Huang, Haifeng Li, Yi Chen, Xiu Su

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for coupled-field physical world intelligence that probes latent state inference, causal mechanisms, and intervention reasoning in fire dynamics, offering a stress-test for world-model evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23064)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Xuanyi Liu, Haofeng Wang, Ruiqi Li, Danni Yu, Rui Wan, Ruixu Zhang, Siyu Tao, Xue Yang, Shaofeng Zhang, Zicheng Zhang, Jiaqi Zhang, Siwei Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark evaluating embodied world models via synchronized head and wrist-view consistency, extending world-model evaluation beyond single-view visual quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26314)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Vishnu Sashank Dorbala, Dinesh Manocha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces active memory management via a memory head for long-horizon embodied navigation, offering a transferable insight for memory and state abstraction in world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25666)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Junjie Xie, Chuxuan He, Angen Ye, Yujia Song, Dapeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Hierarchical VLA framework for closed-loop medical robot manipulation; relevant to action-conditioned control but offers limited world-model or video-generation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25756)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zhifei Teng, Bo Feng, Xiang Zou, Jinpeng Xiao, Min Li, Zhouping Yin, Yiqun Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distills future cable-topology and contact dynamics into representations for a VLA policy, a weakly related dynamics-modeling contribution for manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25606)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jung-Woo Lee, Soo-Chul Lim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Grounds current and desired contact forces visually for goal-conditioned dexterous manipulation, a narrow dynamics-conditioning idea with limited transfer to video or world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.25785)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zeyu Lou, Tianran Zhang, Xinquan Yue, Ya Jing, Chenyang Si

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains a vision-proprioception risk predictor for hazard anticipation and rollback in VLA manipulation, a weakly related predictive-dynamics safety mechanism.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26313)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Lukas Zeh, Johannes Meiwaldt, Zexu Zhou, Armin Lechler, Alexander Verl

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns biLSTM dynamics of deformable linear objects for MPPI control, a narrow learned-dynamics model for manipulation rather than a visual world model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.26238)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Boxun Hu, Jiawei Ge, Axel Krieger, Peng Wang, Tinoosh Mohsenin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Edge-deployed active-perception next-best-view loop with distilled human mesh recovery, offering a narrow but plausible closed-loop visual dynamics/embodied perception connection.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.23974)

---

