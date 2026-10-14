# 💡 今日研究速览 (Daily Summary)

### World Models for Embodied Intelligence

The dominant theme across today's submissions is the maturation of world models from passive video predictors into executable, physically grounded simulators that close the loop with policy learning. A clear convergence is emerging around **shared latent dynamics transformers**that jointly evolve visual, geometric, and action representations—exemplified by Thinker-WM's unified RGB-depth-action backbone and D-World's explicit, inspectable digital twin with recursive self-improvement under dual control. Several works attack the long-standing**long-horizon consistency problem**from complementary angles: LongForcing identifies a supervision-horizon gap in autoregressive video diffusion and supervises extended student self-rollouts, while Directional Pullback Regularization introduces a kinematics-aware anisotropic latent metric for driving rollouts, and Order-Consistent Latent Geometry formalizes "self-approachingness" as a planner-facing compatibility condition linking latent dimension to angular capacity. Crucially, the field is moving toward**reliable, benchmarked simulators**: WorldOracle provides the first systematic diagnostic comparing action-conditioned world models against paired real-world rollouts along physical correctness, spatial alignment, and multi-view coherence, while WoVR+ and Trust-Calibrated VLA post-training both use hallucination-aware or reliability-gated imagined rollouts to make RL on VLA policies safe and effective. Physics grounding is deepening beyond pixels—Code2Worlds-2 compiles generated 4D worlds into physics-engine-loadable SimReady scenes, and Pixels to Executable Physics grounds video generation in reconstructed terrain contact dynamics. Finally, a notable strand interrogates**what actually matters**: What Limits Cross-Task Generalization decouples world model from inverse dynamics and shows that a vision-to-action loss redirecting future generation toward action-relevant detail is key, echoing Physics-Aware Object-Centric SE(3) Forecasting's argument that compact contact-relevant futures suffice over dense visual prediction.

### World-Action Models and VLA Policy Learning

A second major direction concerns the tight coupling of world models with action generation, with several papers pushing toward**lightweight, deployment-ready world-action models**. WAVE-0 bridges VLA policies and world-action models via lightweight latent future prediction without pixel reconstruction or large-scale video pretraining, while StreamingWAM tackles the real-time control bottleneck through chunk-wise staircase flow matching and prefix rollout for cross-chunk continuity. LoopWAM addresses the practical reality of learning from**mixed-quality deployment rollouts**via source-dependent noise sampling and quality steering, and OccWAM introduces an occupancy-native formulation with joint scene-to-ego flow matching that enables reciprocal interaction between prediction and planning. On the policy-improvement side, ForkCast uses candidate-conditioned counterfactual futures to select recovery interventions for frozen VLA policies, ReEnvision maintains a joint future-action belief for selective action repair, and BELIEFWEAVER combines persistent relational belief states with an implicit world model for long-horizon failure recovery—together suggesting a shift from monolithic policies toward**modular anticipate-diagnose-repair loops**. Data efficiency is also a focus: Act4R achieves kinematics-free control via action-conditioned 4D reconstruction, DR-VLA transfers egocentric human video to quadruped navigation through domain-invariant scene representations, and EgoMatrix converts human videos into physically faithful robot demonstrations. The emergence of Data-Free Continual Learning for world action models, which reveals that forgetting concentrates specifically in inverse dynamics, offers an important diagnostic for future continual-learning work in this space.

### Video Generation and Generative Modeling

Today's video generation work is characterized by**efficiency, controllability, and structural fidelity**rather than raw scale. LinMorph improves Video DiT linearization via a learned softmax-to-linear weight morphism, and FlashVSR+ combines hybrid attention with reward-yield distribution matching for efficient super-resolution—both reflecting a broader push to distill large generative models without sacrificing quality. Consistency across long horizons remains a central challenge: CineMem introduces attention-aligned fine-grained memory retrieval with online-clustered KV caches for multi-shot generation, GAD transfers cross-frame correspondences from a frozen geometry model into video attention, and 4LC proposes a 4D latent cache reusing composite static-dynamic representations for efficient spatiotemporal control. Text alignment is strengthened by VARI's group-structured intent alignment with form-contrastive flow-DPO and FlowCred's hierarchical credit assignment for joint prompt-generator post-training. More specialized contributions include Multics' hierarchical communication for multi-player world models, hierarchical curriculum learning for surgical video, and H-DDCM's Hadamard codebooks for training-free generative compression. In image generation, PixelMoE scales pixel-space diffusion with LLM-style mixture-of-experts, and Diagnose-to-Generate addresses structural distortions via patch-level grounded alignment—both offering architectural ideas with plausible transfer to video.

### Multimodal, Spatial, and Representation Learning

Several papers probe the**representational foundations** underlying embodied and multimodal systems. What Makes a Good Visual Representation for Spatial Understanding in MLLMs systematically evaluates which transferred representations best support 3D/4D reasoning, providing actionable guidance for dynamics modeling. What Makes a Latent Space Shared? analyzes when shared latent spaces are directly compatible versus merely recoverable, with direct implications for cross-schema latent dynamics and motion representation alignment. Vision-Predictor-Action replaces autoregressive VLA decoding with a JEPA latent predictor plus flow-matching action chunking, and MemoryVLN demonstrates ego-aware 2D/3D/pose memory tokens with hierarchical reuse for long-horizon navigation. On the multimodal conditioning front, Listen Before Act introduces audio-conditioned manipulation with an audio-action binding objective, and Contact Trajectory Prompting encodes motion and contact dynamics into ordered prompts for one-shot transfer of contact-rich behaviors. Physical-Field-Bridged Material Parameter Inference offers a dynamics-relevant representation for deformable object prediction, while CityCode builds persistent, agent-operable 3D city representations from sparse aerial observations. Finally, Walk Like This enables independent velocity and style control for physics-based locomotion via example-driven diffusion, and Learning Robot Policies for Whole-Body Mobility Assistance generates responsive care-recipient dynamics through an adversarial motion prior—both illustrating how learned generative dynamics can substitute for hand-crafted simulation in human-robot interaction.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**:  Thinker Team, Peng Gao, Jichao Jiao, Chen Liao, Daqin Luo, Yiming Ma, Baiyu Pan, Hailin Shi, Jiyuan Wang, Xiangming Xu, Xiongwei Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified multimodal world model jointly evolving RGB, metric depth, and robot action in a shared dynamics transformer, supporting action-conditioned generation, world prediction, and inverse dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18447v1)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ruo Chen, Jiahua Pang, Yingjie Niu, Hongyi Lin, Jun Tian, Yang Zhu, Chao Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a physically consistent quadruped world model by grounding video generation in reconstructed terrain contact dynamics, enabling iterative rollouts and better action-consequence prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17630v1)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 7/10

**作者**: Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Junfeng Ni, Ting-Bing Xu, Zhicheng Liu, Mu Xu

**机构**: AMAP, Alibaba Group

**💡 亮点 (Highlight)**: Identifies a supervision-horizon gap in autoregressive video diffusion and introduces long-horizon temporal manifold matching that supervises extended student self-rollouts, improving long-horizon world rollout consistency and enabling 24-hour interactive rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18289v1)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junlin Wu, Wen Fan, Dandan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies self-approachingness as a planner-facing compatibility condition for latent world-model planning, proving that acute bends in latent geometry cause candidate-order reversals and linking latent dimension to angular capacity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18570v1)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haomin Wang, Anqiong Ji, Ke Wang, Zhongshan Liu, Ru Ying, Ran Zheng, Zhipeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Lightweight latent world model that predicts future representations to condition a VLA action expert, unifying latent planning and future prediction without pixel reconstruction or large-scale video pretraining.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18568v1)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mingxuan Zhu, Hohei Chan, Shiyuan Liu, Yuanxing Zhang, Lu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Group-structured intent alignment framework with group-consistent distillation and form-contrastive flow-DPO that improves text-to-video semantic robustness and cross-prompt-form consistency without inference-time modules.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18189v1)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kaipeng Fang, Hangxu Liu, Chaojian Shi, Yunsong Zhou, Hongzi Zhu, Minyi Guo, Jingkuan Song, Lianli Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Enables data-free continual learning for video-generation-based world action models via rectified generative replay that truncates rollouts at task completion and filters physically inconsistent action-observation pairs, revealing forgetting concentrates in inverse dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18038v1)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xuan Wen, Baichao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds an explicit inspectable world model as an executable digital twin with measurement-grounded recursive self-improvement and dual-control action selection, offering a broadly useful alternative to implicit weight- or video-based world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17114v1)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shatadal Mishra, Ahmadreza Moradipari, Nejib Ammar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Directional Pullback Regularization, a kinematics-aware anisotropic latent metric that improves long-horizon latent world-model rollout for autonomous driving without changing the predictor architecture.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16139v1)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junfeng Ni, Ziyu Zhu, Fan Jiang, Yu Liu, Chiyu Wang, Jiawei Zhang, Zhaoxu Sun, Mu Xu, Siyuan Huang, Yixin Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Geometry Attention Distillation transfers cross-frame correspondences from a frozen geometry model into video attention, improving long-range scene and temporal consistency without extra inference modules.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18779v1)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoyu Zhang, Siming Li, Zeyu Zhang, Yi Zhang, Tat-Seng Chua, Hao Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Turns generated 4D visual worlds into executable, physics-engine-loadable simulations via a SimReady scene compiler and simulator-in-the-loop refinement, adding collision geometry, physical attributes, and contact dynamics for embodied world simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17651v1)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shaojie Ren, Jingwen Sun, Zezhi Liu, Hongjin Chen, Xin Jin, Wei Zou, Zhibo Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Streaming world-action model with chunk-wise staircase flow matching, prefix rollout for cross-chunk continuity, and dense video-history memory improves action continuity and reduces replanning latency for video-generation-based robot control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.15585v1)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaoxue Wu, Xinyu Gao, Fang Yu, Yu Qiao, Xinyuan Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Attention-aligned fine-grained memory retrieval with online-clustered KV cache and query-level retrieval improves long-range consistency across shot transitions in autoregressive multi-shot video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17926v1)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenzhan Li, Yiran Qin, Heng Zhou, Huirui Wang, Yulan Guo, Ruimao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trust-calibrated VLA post-training that couples policy optimization with an online-updated world model and reward proxy, using simulator reliability to control imagined-data ratio and rollout horizon for recursive imagination.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16517v1)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenxuan Guo, Yingping Liang, Zhaoguo Wang, Ziyuan Li, Angyuan Ma, Zhenyu Wu, Chengkun Wang, Bingyao Yu, Ze Chen, Borui Zhang, Xiuwei Xu, Meng Zhang, Erjin Zhou, Jiwen Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Closed-loop world-action model that learns from mixed-quality deployment rollouts via source-dependent noise sampling and quality steering, letting action-conditioned video prediction inform action generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18873v1)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kaiyi Huang, Wangbo Yu, Yukun Huang, Jiwen Yu, Kunhao Liu, Donglin Yang, Wenbo Hu, Ying Shan, Xihui Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces hierarchical player/group/global communication for multi-player interactive video world models, improving cross-player consistency and scaling to more players without retraining.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17201v1)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mingxuan Zhu, Yanwei Huang, Shiyuan Liu, Xinzhi Zhang, Shujie Li, Yuanxing Zhang, Lu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes hierarchical credit assignment and functional coordination for joint prompt-generator post-training, improving text-to-video quality and story consistency without extra decoding or reward budgets.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18142v1)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qihang Huang, Wenhui Huang, Collister Chua, Shiyu Fang, Zhan Chen, Songyan Zhang, Zhidong Wang, Daiying Tian, Chen Lv

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an occupancy-native world-action model that jointly generates future occupancy and ego trajectories via two-stage scene-to-ego flow matching, enabling reciprocal interaction between world prediction and planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17688v1)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jianhui Zhang, Zuyao Lin, Pengxin Xu, Jingdong Wang, Xingyu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a 4D latent cache that reuses composite visual representations of static and dynamic content to condition video generation, enabling efficient spatiotemporal control and scene consistency for dynamic world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17625v1)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chen Zhao, Zipeng Ye, Yihan Lin, Yuchen Xie, Jing Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses cross-task generalization failures in world action models by decoupling world model and inverse dynamics, and introduces a vision-to-action loss that redirects future generation toward action-relevant detail.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16641v1)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Shangqing Zhou, Zhennan Jiang, Ning Ma, Xin Fu, Yupeng Zheng, Shuai Tian, Huangrui Li, Jiahao Liu, Chao Yu, Zhongpu Xia, Haoran Li, Dongbin Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends a hallucination-aware action-conditioned world model into a reliable simulator for VLA policy RL, with multi-view prediction, chunk-wise noise for exploration, and stage-local imagined training for long-horizon tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17922v1)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiahui Sun, Ran Bi, Yifei Liu, Xiaolong Zhou, Yishuo Xu, Yuanqi Li, Congcong Zhu, Lei Yang, Yanwen Guo, Zhihang Zhong, Hongjie Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds persistent, agent-operable 3D city world representations from sparse aerial images with generative completion, supporting long-horizon querying, editing, and state restoration.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18342v1)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Lingyi Long, Congyue Zhao, Xiaoou Li, Yanmin Qian, Tao Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves Video DiT linearization efficiency and final generation quality by learning a softmax-to-linear weight morphism that transfers pretrained knowledge before recovery.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17914v1)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Ruchang Yao, Shi Guo, Junhao Zhuang, Mingde Yao, Xin Cai, Jiahao Zhan, Bin Fu, Xinyuan Chen, Yu Qiao, Tianfan Xue

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves video super-resolution efficiency and preference alignment via hybrid attention and reward-weighted distribution matching distillation, with transferable video-generation training insights.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17552v1)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Shuzheng Wang, Haoxuan Li, Shengzhen Li, Chenxi Wu, Yajing Sun, Lu Hou, Wenyu Liu, Xinggang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified World-Language-Action model with Mixture-of-Transformers experts and cross-expert attention jointly predicts future scene dynamics and trajectories for autonomous driving.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17903v1)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zhaoliang Zhang, Chenhao Yu, Zhimin Shao, Xijun Liu, Cheng Peng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Action-conditioned 4D reconstruction that predicts robot 3D scene flow from action signals via a spatial-action encoder, enabling inverse control without kinematics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17462v1)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Shikun Ban, Shohei Nagai, Qingyang Song, Hanxi Wan, Eric Zhao, Thomas Wang, Zackory Erickson

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a human motion policy with an adversarial motion prior to generate responsive care-recipient dynamics for training whole-body assistive robot policies, offering a learned-dynamics simulation insight for human-robot interaction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17750v1)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yeonseok Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replaces autoregressive VLA decoding with a JEPA latent predictor plus flow-matching action chunking, offering a lightweight latent-dynamics control loop relevant to world-model-based embodied prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.15556v1)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Chenru Wen, Huajian Zeng, Haokai Ding, Jian Kang, Anqing Duan, Dawei Zhou, Dezhen Song, Xingxing Zuo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a candidate-conditioned world model to forecast counterfactual futures and select recovery interventions for frozen VLA policies, improving manipulation success under occlusion and object slip.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18650v1)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 5/10

**作者**: Youngbin Kong, Seungho Lee, Jae Kyung Shin, Jong-hyuk Ahn, Hyoun-Joong Kong, Kyu Eun Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Hierarchical phase/task/action curriculum transfer learning for surgical text-to-video diffusion improves FVD/FID, offering a reusable coarse-to-fine training strategy for domain-specific video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17684v1)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Linrui Shou, Jie Li, Yu Liu, Tao Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Bridges multi-view deformation videos to material parameters via dense physical fields, offering a dynamics-relevant representation for future-state prediction of deformable objects.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17591v1)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Zhenhua Yang, Jiafeng Liang, Xingyu Zhou, Yi Jiang, Xiayu Cao, Zui Chen, Luqi Wang, Haiyang Sun, Yufei Xiang, Chang Li, Rongchuan Mu, Bowen Chi, Zihe Tong, Mingyu Li, Huijie Ma, Yiqiao Yang, Baoqi Ren, Zhiming Ma, Zhihao Zhu, Jiahao Ji, Zhuoyao Wang, Qianyu Wang, Xiangyu Liu, Wang Zixiang, Shunliang Zhang, Ming Liu, Xiaocheng Feng, Duyu Tang, Bing Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proactive physical AI system with a streaming timing model that continuously observes world states to decide when to intervene, contributing insight into temporal dynamics and timely action initiation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16967v1)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jun Tian, Yingjie Niu, Ruo Chen, Hongyi Lin, Chao Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses latent world modeling with a domain-invariant scene representation and flow-matching action expert to transfer egocentric human video into quadruped navigation policies.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18373v1)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Haldun Balim, Yilun Du, Na Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes learning a generative diffusion prior over action sequences as a proposal distribution refined by learned dynamics, reward, and value models, offering a model-based planning perspective relevant to world-model-based decision making.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18677v1)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yirui Zhou, Hongli Xu, Ying Zheng, Yi Wang, Lap-Pui Chau

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Object-centric SE(3) rigid-body forecasting for proactive grasping argues compact contact-relevant physical futures suffice instead of dense visual prediction, a useful abstraction insight for dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17843v1)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xueyao Wei, Yifei Wang, Delun Li, Shaoan Wang, Junzhi Yu, Wenjie Song, Xingyu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Memory-driven VLN system with ego-aware 2D/3D/pose memory tokens and hierarchical memory reuse, offering transferable insights on long-horizon spatial memory for embodied agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18478v1)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xiyin Zeng, Xuewei Huang, Yi Lu, Weihao Yuan, Hao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Future-guided selective action repair maintains a joint future-action belief updated by execution feedback, offering a transferable insight into anticipating how deviations propagate through predicted action sequences for long-horizon control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17977v1)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xiyang Wu, Zhichao Liu, Shengxin zhang, Zongxia Li, Ming Li, Tianyi Zhou, Dinesh Manocha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: BELIEFWEAVER combines persistent relational belief state with an implicit world model that evaluates repair hypotheses and predicts progress, offering a transferable mechanism for long-horizon recovery and prospective reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18082v1)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Joshua Aurand, Agon Serifi, Sammy Christen, Ruben Grandia, Espen Knoop, Marco Hutter, Moritz Bächer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Enables independent velocity and style control for physics-based locomotion via an autoregressive diffusion model conditioned on a style encoder, with transferable relevance to controllable motion generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18147v1)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yuqi Ye, Caigao Jiang, Zhuonan Wang, Congyuan Pei, Chao Qu, Changhao Peng, Junhong Lin, Qize Yu, Zetian Song, Guangzhao Fu, Chongruo Wu, Shiyu Huang, Shuchang Zhou, Honggou Yang, Wei Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unifies diffusion-based action generation with autoregressive CoT understanding in a driving VLA, offering a low-latency generation/understanding scheme with limited direct world-model or video-generation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16985v1)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Youpeng Wen, Gang Wang, Tianyu Huang, Weiwei Zhang, Zhijian Huang, Wei Chen, Xieyuanli Chen, Yunhui Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Long-horizon robotic manipulation agent that maintains shared context of subtask progress and object locations, offering a weakly related planning/memory insight for embodied world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18352v1)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xiaohu Huang, Yumin Guo, Kai Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematic study of which transferred visual representations best support 3D/4D spatial reasoning in MLLMs, yielding transferable insight for spatial-temporal representations of dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17844v1)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 4/10

**作者**: Haoyi Duan, Liliang Chen, Nan Wang, Yang Zhang, Yuhang Lu, Xiaotong Chen, Wei-Cheng Tseng, Shenyuan Gao, Zhaoshuo Li, Jingyi Jin, Pooya Jannaty, Dhruv Shah, Yuke Zhu, Ming-Yu Liu, Maoqing Yao, Guanghui Ren

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark evaluating action-conditioned world models against paired real-world rollouts along physical state correctness, spatial alignment, and multi-view action coherence, providing a systematic diagnostic foundation for manipulation world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18826v1)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Xian Nie, Yujie Zang, Yuhang Zheng, Yupeng Zheng, Songen Gu, Wendi Chen, Chuan Wen, Cewu Lu, Wenchao Ding, Junchi Yan, Shuicheng Yan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Encodes motion and contact dynamics into an ordered contact trajectory prompt for one-shot transfer of contact-rich manipulation, providing a dynamics-relevant conditioning signal for closed-loop action generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18848v1)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Iago Brito, Walcy Rios, Lucas Fernandes, Kaiki de Oliveira, Arlindo Galvão Filho

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes when shared latent spaces are directly compatible versus merely recoverable, with implications for cross-schema latent dynamics and motion representation alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17376v1)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Or Ronai, Vladimir Kulikov, Tomer Michaeli

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Hadamard-dictionary codebooks and a streaming KV-cache re-encoding scheme for training-free generative video compression, an efficiency-oriented contribution adjacent to video generation rather than a dynamics or quality advance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18125v1)

---

## 47. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jiaqi Fan, Rui Xu, Jiakun Xia, Xuyu Fan, Shuailei Ma, Yuefeng Wang, Qing Wang, Jiarui Zhang, Yili Fu, Xu Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Audio-conditioned VLA policy with an audio-action binding objective; relevant mainly as a multimodal dynamics/conditioning signal rather than a video-generation or world-model contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16313v1)

---

## 48. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Ruixiao Dong, Jianmin Bao, Bozhi Luan, Zijie Meng, Xin Tao, Pengfei Wan, Kun Gai, Li Li, Houqiang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Scales pixel-space diffusion with LLM-style mixture-of-experts and hierarchical flow matching, an image-generation method whose sparse-capacity and resolution-scheduling ideas may transfer to video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18857v1)

---

## 49. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yifan Li, Lishuai Gao, Tong Zhang, Qilong Huang, Chen Zhao, Zhuoliang Kang, Jie Hu, Yujie Zhong, Fenghe Tang, S Kevin Zhou, Xiaoming Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Patch-level grounded alignment with trajectory-preserving stochastic sampling improves structural fidelity of flow-based image generators, with only indirect transferability to video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17882v1)

---

## 50. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Ziheng Wang, Yanming Shao, Ting Mao, Kaihan Chen, Yiqun Wang, Xuanye Wu, Yao Mu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Converts egocentric human videos into physically faithful paired robot observation videos via HOI reconstruction, retargeting, RL, and joint rendering, providing a data-engine insight for generating consistent robot-object motion and contact.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18822v1)

---

