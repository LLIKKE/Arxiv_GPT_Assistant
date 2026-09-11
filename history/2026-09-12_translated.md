# 💡 今日研究速览 (Daily Summary)

### World Models and Predictive Dynamics

Today's submissions reveal a clear consolidation around world models as the central abstraction for embodied intelligence, with two distinct thrusts: making them *constructive* and making them *diagnostic*. On the constructive side, Valerant demonstrates that a pretrained action-conditioned world model can be repurposed at inference time into a navigable map generator by coupling predictive rollouts with SLAM-based reconstruction—no training required—while Recursive Code World Models push the idea further by representing 3D scenes as executable recursive programs, bridging neural rollouts with symbolic compositionality. UniMPA extends this line with a unified memory-prediction-action architecture whose visual-action memory banks ground predicted transitions in executable evidence, directly attacking the hallucination problem that plagues long-horizon prediction. Equally notable is the emergence of world models as *readable instruments* rather than mere generators: FARM shows that failure signals are linearly decodable from the frozen predictive states of a robotic world model, enabling causal execution monitoring with zero backbone updates, and the counterfactual fork-ledger protocol formalizes when an individual world-model update is actually worth making during continual adaptation—a question the field has largely answered by intuition until now. HuRo's robotization of human video into aligned observation-action trajectories supplies exactly the kind of weak-supervision dynamics data these models need, while ReactHuman's physics-grounded benchmark supplies the evaluation pressure. The through-line is unmistakable: the frontier has shifted from *can we predict the future* to *can we trust, inspect, and selectively update what we predict*.

### Controllable and Efficient Video Generation

Video generation research today is preoccupied with the twin failure modes of controllability and diversity collapse. On controllability, Harnessing Intrinsic Subject-Aware Attention mines attention maps already latent in DiTs to enforce multi-subject identity consistency, combining guided attention with RL preference pairs to suppress semantic drift—an elegant argument that the control signal need not be injected externally but merely *surfaced* from existing representations. On diversity, Uncertainty DMD diagnoses a structured collapse in few-step autoregressive distillation, where DMD-style objectives systematically narrow the output distribution, and restores motion and variation through timestep perturbation and stochastic cache writing without touching the architecture. Complementing both, From Evaluation to Enhancement closes the loop between diagnosis and repair by benchmarking "think-with-video" physical and logical reasoning and deploying a VLM-based prompt rewriter to improve it. Read together, these papers signal a maturation of the field: rather than scaling compute, the leverage now lies in understanding *where* generative video loses fidelity—identity, motion, or physical plausibility—and applying surgical, often training-light interventions at exactly those points.

### Reasoning, Policy Learning, and Embodied Evaluation

A smaller but coherent cluster addresses decision-making under structured constraints and physical grounding. LTLDiff brings finite linear temporal logic into multi-agent manipulation, using LTLf specifications to guide both data generation and diffusion policy learning—temporal-logic conditioning is a promising route to verifiable, compositional control, though its contribution remains on the policy side rather than in learned dynamics. CARLAverse offers a distributed, multimodal human-in-the-loop driving simulator whose modularity is valuable for interactive environment research, even if it contributes infrastructure rather than learned-dynamics insight. ReactHuman's physics-grounded benchmark for reactive decision-making in embodied MLLMs is the most pointed of the three, probing whether multimodal models possess intuitive physical dynamics under safety-critical conditions—precisely the capability that world-model-based agents will be expected to exhibit. The collective message is that evaluation and constraint specification are catching up to generation: as policies grow more capable, the binding constraints are shifting from *what can be learned* to *what can be verified, specified, and safely acted upon*.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yiran Qiao, Feng Wang, Jing Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free framework that turns a pretrained action-conditioned world model into a WAM by coupling predictive visual rollouts with SLAM-based spatial reconstruction to build persistent 3D game maps.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.09418)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Niange Yu, Ye Tian, Biaolong Chen, Miao Lu, Aixi Zhang, Hao Jiang, Yunhai Tong, Pipei Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Exploits intrinsic subject-aware attention maps in DiTs for controllable multi-subject video generation, improving identity consistency and reducing semantic drift via guided attention and RL preference pairs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11507)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zixuan Duan, Xunzhi Xiang, Yabo Chen, Xin Zhang, Changhan Liu, Haibin Huang, Chi Zhang, Qi Fan, Xuelong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses structured uncertainty collapse in DMD-distilled autoregressive video generators and restores diversity/motion via timestep perturbation and stochastic cache writing without architectural changes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11265)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wei Li, Rui Shao, Jie He, Lingsen Zhang, Ziwei Liu, Liqiang Nie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified memory-prediction-action model with action-grounded transition modeling, persistent-selective future prediction, and visual-action memory banks to ground predicted transitions in executable evidence.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11875)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhiqi Li, Yuxuan Liao, Bo Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Recursive Code World Models that reconstruct complex 3D worlds as executable recursive scene programs from a single image, advancing code-based world-model construction and compositional scene representation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11499)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Haoran Pei, Mingrui Luo, Senbao Wang, Haoran Lv, Jie Guo, Sheng Zhong, Ruixi Ci

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that frozen pretrained robotic world-model predictive states contain decodable failure information, enabling lightweight causal execution monitoring without updating the dynamics backbone.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11445)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Meng Luo, Yicheng Liu, Jiahao Wang, Yuanxing Zhang, Xin Tao, Pengfei Wan, Kun Gai, Hao Fei

**机构**: KlingTeam (Kuaishou)

**💡 亮点 (Highlight)**: Benchmarks and improves 'think-with-video' reasoning in video generators via a VLM-based prompt rewriter, offering a diagnostic lens on physical/logical correctness of generated video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11242)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Anqi Peter Li, Kaden Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a counterfactual fork-ledger protocol that measures the utility of individual world-model updates during continual adaptation, offering a broadly useful insight for deciding when to update learned dynamics models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.10954)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Patrick Rebling, Philipp Nenninger, Reiner Kriesten

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distributed human-in-the-loop driving simulation framework with modular multimodal clients; relevant to interactive environment simulation but offers limited learned-dynamics or video-generation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11478)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Chuhan Meng, Haiyan Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: LTLf-guided data generation and diffusion policies for multi-agent manipulation; temporal-logic conditioning is adjacent to controllable dynamics but the contribution is primarily policy learning rather than world modeling or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11043)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim, Hanjung Kim, Seon Joo Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Robotizes human videos into robot-aligned observations and action trajectories for VLA pretraining, offering weak-supervision dynamics data relevant to world-model learning from video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.10706)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Yizhan Li, Jianxin You, Mengyang Xiong, Yinhuan Chen, Zicheng Zhao, Dekun Wu, Dongqing Zhang, Bang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Physics-grounded benchmark for reactive decision-making in embodied MLLMs that probes intuitive physical dynamics and safety-critical action, indirectly relevant to world-model evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.10895)

---

