# 💡 今日研究速览 (Daily Summary)

### World Models & Embodied Simulation

The dominant theme in today's batch is the maturation of world models from passive video predictors into controllable, physically grounded simulators for embodied intelligence. Pelican-Sim 1.0 exemplifies this shift with a general action-conditioned simulator built on a unified 28-D action space, action-visual injection, and sparse MoE, enabling few-step autoregressive rollouts for controllable embodied video prediction. Complementing this, VideoTok4D attacks the representation bottleneck by disentangling static and dynamic tokens with track-aware attention, yielding compact 4D world representations that make scene generation more efficient. Perhaps most interesting is IMPLY, which delivers a cautionary result: self-consistency alone cannot detect when a world model has failed to internalize correct object dynamics, and anchoring rollout selection to calibration or physical evidence is necessary. This trio suggests the field is converging on a view of world models as *evaluated simulators*—where controllability, compactness, and physical faithfulness are jointly optimized rather than assumed.

### Vision-Language-Action & Robotics

A second cluster focuses on closing the loop between prediction and action in robotic control. Dynin-Robotics proposes a unified diffusion VLA that jointly models action-conditioned next-observation and goal-state prediction, then leverages future-state prediction for test-time action selection and refinement—an elegant way to convert generative world modeling into a decision-making asset. DWMP takes a complementary hybrid approach for humanoid obstacle traversal, fusing a Koopman-linearized proprioceptive dynamics model with an RSSM visual world model, showing that structured linear dynamics and learned latent dynamics can be productively combined rather than treated as competing paradigms. Together these works signal a trend toward *multi-model fusion* in embodied policies, where analytical priors and neural world models are composed to handle the distinct time-scales and modalities of locomotion and manipulation.

### Training Dynamics & Credit Assignment

Two papers target the foundational problem of learning reliable long-horizon dynamics. "Large Distant Gradients Need Not Be Reliable" introduces reliability-weighted credit assignment for long-horizon autoregressive rollouts, demonstrating that gradient magnitude is a poor proxy for gradient trustworthiness—an insight that transfers directly to long-horizon video and world-model prediction, where error compounding is the central failure mode. In parallel, the work on Fundamental Dynamical Units proposes composable signed three-node primitives for physics-informed structural inference from perturbation time-series in networked systems, offering a transferable representational vocabulary for learned dynamics. Both point toward a broader recognition that *structural priors and reliability estimates*—not just scale—are what make long-horizon dynamical learning tractable.

### Scene Understanding & Streaming Interaction

The remaining papers probe spatial and temporal structure at the perception frontier. ProClosure performs hierarchical room-object assignment via progressive boundary closure from monocular video, contributing spatial scene-graph structure that could serve as scaffolding for world models even though it does not itself learn dynamics or generation. ProactiveBench rounds out the set by asking whether streaming video models can genuinely interact like humans, introducing a benchmark for proactive temporal decision-making. Though weakly coupled to world modeling proper, both works highlight a growing demand for *evaluation and structure*—benchmarks that stress interactivity, and representations that ground spatial layout—as necessary complements to the generative and control advances above.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shilong Zou, Shilin Zhang, Yingji Zhang, Yuhang Huang, Yi Zhang, Zeyuan Ding, Han Dong, Junwei Liao, Yong Dai, Jian Tang, Xiaozhu Ju

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: General action-conditioned world-model simulator with unified 28-D action space, action-visual injection, sparse MoE, and few-step autoregressive rollout for controllable embodied video prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.12036)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xinyi Chen, Hanxin Zhu, Xijun Wang, Xingrui Wang, Sen Liang, Xin Li, Zhibo Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: 4D-aware video tokenizer that disentangles static/dynamic tokens with track-aware attention, yielding compact world representations and efficient 4D scene generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.12874)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Aman Mehta, Riya Baviskar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes physics-anchored consistency scoring for world-model rollouts, showing that self-consistency alone cannot detect wrong object internalization and that anchoring to calibration evidence improves rollout selection.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.12441v1)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hoeun Lee, Jaeik Kim, Jusang Oh, Jinhyeok Kim, Geon Choi, Hyeonggeun Kim, Jaeyoung Do

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified diffusion VLA that jointly models action-conditioned next-observation and goal-state prediction, using future-state prediction for test-time action selection and refinement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.13053)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Rongjun Jin, Jianming Ma, Yue Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Dual world-model policy for humanoids that fuses a Koopman-linearized proprioceptive dynamics model with an RSSM visual world model for obstacle traversal.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.12347)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Junhao Zhao, David Michael Simberg, Jacob Kang, Colin Connor Kurniawan, Nan Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces reliability-weighted credit assignment for long-horizon autoregressive rollouts, a training insight transferable to long-horizon video/world-model prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.12890)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Nima Nouri

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces composable signed three-node dynamical primitives for physics-informed structural inference of networked dynamics, offering a transferable representation for learned dynamics models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.11934)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Vinoth Kumar Muthuraj, Soumyadeep Banik, Kushal Sharma, Hardik Jain

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Monocular-video room segmentation via progressive boundary closure; weakly related to world modeling through spatial scene-graph structure rather than learned dynamics or generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.12614)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Kaixuan Du, Xin Wan, YuKun Wang, Hang Zhang, Meng Cao, Dai Guan, Ming Chen, Ni Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for proactive streaming video understanding that probes temporal decision-making, weakly relevant to interactive/streaming video models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.12658)

---

