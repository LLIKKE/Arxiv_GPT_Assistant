# 💡 今日研究速览 (Daily Summary)

### World Models & Video Generation

The dominant theme today is the maturation of **world models**from passive predictors into controllable, physically consistent simulators. A clear convergence is emerging around training these models on**unsupervised video**: Action Forcing recovers grounded egomotion action bases via PCA to make unlabeled video controllable, while Praxis distills physical interaction priors from egocentric demonstrations. Complementing this, OneWorld enforces a *shared latent physical mechanism* across counterfactual action-conditioned futures, and StarWM uses self-supervised attention routing to preserve dynamics-relevant state while discarding distractors over long-horizon imagination. Efficiency and fidelity are also being tackled jointly: DyMD adapts distribution-matching distillation to preserve interaction dynamics in few-step video world models, and MVAgent combines typed conditioning with shot-level Trunk-GDPO RL to improve cross-shot consistency in multi-agent, multi-shot generation. Notably, the field is beginning to demand *rigorous evaluation* rather than visual plausibility alone—TrafficImag's counterfactual benchmark diagnoses conditional video execution as the primary bottleneck, while Action Forcing introduces reference-free metrics for controllability, conjuring, and geometric integrity. Together, these works signal a shift from "does it look right?" to "does it obey the right physics and respond to the right controls?"

### Agents & Embodied Planning

A second major thread concerns **world-action models** for test-time planning and embodied control. MA-WAM predicts joint-action consequences with explicit cross-agent dependencies for efficient test-time planning, while AtomWorld-Mem introduces memory-restored atomistic world states to recover hidden dynamical state from instantaneous snapshots—crucial for long-horizon evolution and zero-shot transfer. In the VLA space, VLaRL uses a VLA's internal vision-language latent as a sim-to-real interface for residual control, and Towards VLA-Dreamer trains a predictive world model directly in the VLA vision encoder's embedding space for action-conditioned short-term planning. Data scaling is being addressed from multiple angles: NavGen repurposes text-to-video generative models as a scalable data engine for embodied 3D navigation with style diversification for long-tail scenes, while SciHorizon-eLab builds an agentic protocol-to-task compiler for scientific embodied benchmarking. Perhaps most notably, Kintsugi-VLA reframes *failure as data*—converting failed rollouts into recovery training data via interventional recoverability estimation, a dynamics-aware curation strategy that could meaningfully improve closed-loop policy robustness.

### Autonomous Driving & Real-World Control

Autonomous driving continues to serve as a demanding testbed for world-model-derived representations. WALT aligns a compact trajectory latent space with a *frozen* driving world model, demonstrating how to extract action-relevant semantics from visual world representations for planning. INTERACT pushes toward interactive closed-loop planning via anchor-conditioned reactive prediction and trust-region refinement, offering a transferable insight for world models that condition on *intent* rather than exact trajectory. Beyond driving, HIRE tackles visually aliased, history-dependent precision manipulation through history-conditioned interaction-state reasoning and a high-rate executor—directly relevant to partial observability in action-conditioned world models. In real-world control, "Precision at Speed" demonstrates sample-efficient online model-based RL with a probabilistic dynamics ensemble for MPC on a hydraulic excavator, a compelling validation of learned dynamics for physical systems. Finally, Enabling Unified Cross-Domain Representation offers an interaction-centric canonical gripper-frame representation with flow-matching action chunks, improving cross-embodiment transfer and reinforcing the value of interaction-centric abstraction.

### Representation & Compression

A smaller but methodologically interesting cluster addresses the **latent design**underpinning generative and world models. FuseReg regularizes layer-fusion robustness in representation autoencoders to narrow the reconstruction-generation gap—a generic latent-design idea with indirect but real implications for video world models, where the tension between faithful reconstruction and controllable generation is especially acute. This connects to the broader trend seen across today's world-model papers: the quality of the learned latent space—whether it preserves dynamics-relevant state (StarWM), supports action-relevant semantics (WALT), or enables efficient few-step distillation (DyMD)—is increasingly the deciding factor in downstream planning and control performance.**Overall takeaway:** Today's research reflects a field consolidating around *controllable, physically grounded world models* trained on ever-more-scalable supervision (unsupervised video, generative data engines, failed rollouts), with evaluation rigor and latent-space design emerging as the critical bottlenecks for real-world embodied deployment.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ashish Sundar, Tiankuo Hou, Zhong Fan, Chunbo Luo, Xiaoyang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Recovers grounded egomotion action bases from unlabeled video via PCA to train controllable video world models, plus a reference-free evaluation of controllability, plausibility, conjuring, and geometric integrity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30595)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ke He, Yichen Ding, Bin Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Enforces a shared latent physical mechanism across counterfactual action-conditioned futures in a flow-based video world model, improving cross-intervention physical consistency with a new multi-intervention evaluation protocol.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30946)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haojun Xu, Jie Huang, Xin Lu, Mingchen Zhong, Zihao Fan, Linjiang Huang, Si Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adapts DMD teacher supervision and critic fitting to preserve interaction dynamics in few-step video world models, improving motion fidelity and downstream action planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31349)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiangyu Kong, Wenjie Zhou, Fengping Tian, Lihua Fang, Haoqin Sun, Chenyang Lyu, Longyue Wang, Weihua Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Multi-agent pipeline with typed conditioning, continuity memory, and shot-level Trunk-GDPO reinforcement learning that improves cross-shot consistency and narrative coherence in multi-shot video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30609)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tian Luo, Ruge Zhang, Haozhi Han, Yifrng Chen, Yunquan Zhang, Yunxin Liu, Ting Cao, Kun Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a memory-restored atomistic world model that recovers hidden dynamical state from instantaneous snapshots to improve long-horizon evolution prediction and zero-shot transfer.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31133)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guowei Zou, Haitao Wang, Guoxin Wang, Beiwen Zhang, Zhiquan Chen, Guojie Wang, Hejun Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a multi-agent world-action model that predicts joint-action consequences with cross-agent dependencies for efficient test-time planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31281)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zeqiang Zhang, Fabian Wurzberger, Maximilian Otte, Daniel Schmid, Sebastian Gottwald, Arne Peter Raulf, Daniel Alexander Braun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: StarWM uses self-supervised attention routing to decide where reconstruction applies, yielding a world model that preserves dynamics-relevant state while discarding distractors over long-horizon imagination.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30667)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Parsa Mastouri Kashani, Jan-Gerrit Habekost, Stefan Wermter

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes training a predictive world model in a VLA vision encoder's embedding space for action-conditioned future prediction and short-term planning, offering a world-model insight for embodied control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31313)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Xijie Huang, Yongyang Wan, Chengbin Dong, Zimo Ding, Mo Zhu, Yijin Wang, Zhiyang Liu, Fei Gao, Yuze Wu, Xin Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses text-to-video generative models as a scalable data engine for embodied navigation, with style diversification for long-tail scenes and world-action-model transfer to real flight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30770)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Mingkai Jia, Jiaxin Guo, Zhijian Shu, Jiawei Xu, Mingxiao Li, Jintao Cheng, Ping Tan, Wei Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: WALT aligns a compact trajectory latent space with a frozen driving world model, showing how to extract action-relevant semantics from visual world representations for planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30436)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Aron Distelzweig, Andreas Look, Faris Janjo\v{s}, Steffen Hagedorn, Luigi Palmieri, Joschka Boedecker

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Interactive closed-loop planning with anchor-conditioned reactive prediction and trust-region refinement offers a transferable insight for action-conditioned world models that condition on intent rather than exact trajectory.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31137)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Rongji Li, Wenhao He, Cewu Lu, Xingyu Chen, Xu-Yao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: History-conditioned interaction-state reasoning with a high-rate executor addresses visually aliased, history-dependent manipulation, offering a latent-state/partial-observability insight relevant to action-conditioned world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30828)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Claudio Canales, Fang Nan, Marco Hutter, Javier Ruiz-del-Solar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Online model-based RL with a probabilistic dynamics ensemble for MPC on a hydraulic excavator, showing sample-efficient learned dynamics for real-world control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31025)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Ivan Snegirev, Elizaveta Semenyakina, Dmitrii Maliukov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Converts failed simulator rollouts into recovery training data via interventional recoverability estimation, providing a dynamics-aware data-curation insight for closed-loop policy learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31048)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Hongyang Du, Yunfei Xie, Junjie Ye, Jiawei Yang, Xiaoyan Cong, Haodong Zhang, Yongchao Huang, Haiyu Wu, Zongxia Li, Shihang Gui, Dawei Liu, Runhao Li, Jingcheng Ni, Chen Wei, Randall Balestriero, Yue Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: FuseReg regularizes layer-fusion robustness in representation autoencoders to narrow the reconstruction-generation gap, a generic image-generation latent-design idea with only indirect video relevance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31620)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Xiangyu Li, Tianyi Wang, Zhihao Dou, Christian Claudel, Zhaomiao Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for counterfactual roadside traffic video generation with an actor-level intervention program and validity dimensions, diagnosing conditional video execution as the main bottleneck.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30722)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Namiko Saito, Kinam Kim, Heecheol Kim, Katsushi Ikeuchi, Yasuyuki Matsushita

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a VLA's internal vision-language latent as a sim-to-real interface for residual control, offering a transferable latent-dynamics insight for embodied world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30868)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Shuliang He, Ruiyan Xu, Bo Yue, Hengming Zhang, Huayi Zhou, Shuai Wang, Wei-Shi Zheng, Guiliang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distills physical interaction priors from egocentric video demonstrations for whole-body manipulation, offering a weakly supervised route to learning dynamics priors from video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30735)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Maokai Qin, Chuan Qin, Qi Zhang, Dianyu Liu, Zirui Liu, Hongting Niu, Yuanchun Zhou, Hengshu Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a protocol-to-task compiler that generates executable embodied laboratory environments and expert demonstrations, offering a weakly related pipeline for scalable construction of interactive embodied simulation tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.30971)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Guanlin Li, Shifeng Bao, Yihan Zhao, Haitao Shen, Haoyang Li, Chen Zhao, Tong Yang, Jie Tang, Jing Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Interaction-centric canonical gripper-frame representation with flow-matching action chunks improves cross-embodiment manipulation transfer, a weakly related embodied-dynamics contribution rather than a world-model or video-generation advance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.31207)

---

