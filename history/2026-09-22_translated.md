# 💡 今日研究速览 (Daily Summary)

### World Models for Embodied Control and Manipulation

The dominant thrust today is the maturation of *world-action models* into a unified substrate for embodied intelligence, spanning driving, manipulation, and contact-rich interaction. A clear convergence is emerging around joint visual-dynamics-and-action prediction: Skel-WAM and SkelWAM both leverage hand-skeleton conditioning as a shared geometric interface to enable human-to-robot transfer and zero-shot cross-embodiment manipulation, while ME-Dex 1.0 extends this paradigm to heterogeneous tactile sensing by treating tactile signals as future observations within a flow-matching Mixture-of-Transformers. Complementing these, FOCAL-VLA and PSR inject implicit world modeling and predictive sensorimotor representations into VLA policies—via subtask-guided geometry distillation and contact-dynamics forecasting respectively—suggesting that the field is moving beyond reactive policy learning toward anticipatory, physically grounded action generation. Notably, ZYT-World pushes the frontier of real-time closed-loop simulation with causal consistency distillation and implicit memory for long-horizon driving, while Robotic Multiphase Interaction demonstrates that action-conditioned world models can tractably capture coupled liquid-solid porous dynamics. The unifying trend is a shift from task-specific dynamics predictors toward modular, interface-driven world-action architectures that share geometric or skeletal state across embodiments and modalities.

### World Model Training, Adaptation, and Efficiency

A second cluster of work targets the practical bottlenecks of training and deploying world models under distribution shift and compute constraints. Sandwich-Residuals introduces parameter-efficient test-time adaptation by freezing the predictor and learning small residual corrections from self-supervised prediction error, directly addressing rollout reliability degradation. In parallel, Adaptive Rollout Truncation exploits epistemic uncertainty to cut offline rollout computation by roughly 72% while matching fixed-horizon accuracy—an important step toward making long-horizon world-model training economically viable. WM-VS contributes a progress-aligned latent world model that reorients predicted action consequences into a target-centric servo coordinate, improving closed-loop visual servoing and transfer. Together, these papers reflect a maturing recognition that world-model quality is not solely a function of architecture scale but of *where* and *how* adaptation and truncation occur, with uncertainty quantification becoming a first-class design signal rather than a post-hoc diagnostic.

### Evaluation, Benchmarks, and the Science of World Models

A notable methodological turn today is the critical interrogation of how we evaluate world models. Same World, Different Knowledge introduces an information-interface audit that separates fidelity from availability gaps, showing that repair selection depends on deployment information paths—a caution against isolated audits that misjudge world-model repairs. Benchmarking World Models for Continual Learning on Compositional Tasks factorizes knowledge reuse along action and perception axes, revealing modularity's trade-off between reuse and forgetting. RecreationWorld and AgentVidBench extend evaluation into interactive computer-use environments and multi-hop video reasoning, respectively, while PolyBridgeBench grounds physical dynamics assessment in executable bridge-design rollouts. The collective message is that the community is moving from leaderboard-style fidelity metrics toward deployment-aware, interface-sensitive, and compositionally structured evaluations—an essential correction as world models transition from research artifacts to control-loop components.

### Generative Dynamics and Physics-Consistent Video

On the generative side, CompAdapt advances physics-consistent text-to-video by modeling composite motions—coupled, multi-stage, and collision dynamics—with dynamics-aware prior matching for one-shot adaptation to unseen physical laws. JEPA Guided Diffusion offers a complementary strategy, decoupling predictive world representation learning from video synthesis by aligning frozen V-JEPA latents into a frozen diffusion model's conditioning space, enabling efficient traffic future-video forecasting. WS-NeRF reframes NeRF deblurring as a dynamic evolution process with temporal memory and world-state-aware priors, a weakly transferable but conceptually adjacent dynamics-modeling idea. Meanwhile, The Weight Is Over contributes on-device diffusion pipeline optimizations that, while targeting image generation, carry direct implications for efficient video generation under memory constraints. The throughline is a growing emphasis on *physical consistency* and *representation decoupling*—generative models are increasingly judged not by perceptual realism alone but by their adherence to learned or specified dynamics.

### Data Engines, Simulation, and Cross-Embodiment Transfer

Finally, several works address the data and simulation infrastructure underpinning world-model and VLA training. Demonstration Synthesis from a Single Scan via Gaussian Splatting builds a 3DGS-based data engine that synthesizes photorealistic visuomotor demonstrations from a single scan, while CRISP provides a high-fidelity contact-rich physics simulator with optimization-based collision detection and augmented Lagrangian solvers. GALA introduces geometry-aware latent action modeling that augments image-based latent actions with 3D end-effector motion for cross-embodiment VLA pretraining. On the memory and mapping front, Adaptive World Memory 3D Foundation Model contributes a gated recurrent world-memory mechanism for persistent 3D mapping and renderable scene modeling. These contributions collectively lower the cost of acquiring physically grounded training data and broaden the embodiment coverage of learned policies—an enabling layer that the more architecturally focused world-action models above will increasingly depend upon.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Boni Hu, Xiong Wei, Haoming Huang, Yong Huang, Chenbo Wang, Yi Yang, Jiancheng Wang, Ruicheng Zhu, Zhimin Yang, Guanglai Liu, Qiaowan Jin, Dongzhuo Wang, Haiwei Kuang, Jiajun Fan, Yue Wu, Jiaxin Wei, Hao Sun, Feihong Yan, Wei Bi, Kaixuan Wang, Zichao Guo, Xiaozhi Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a real-time controllable multi-view driving world model with causal consistency distillation, one-step streaming generation, and an implicit-memory module for long-horizon closed-loop simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21712)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zetao Cai, Yaping Li, Yiqun Wang, Xinyu Zhan, Yuyin Yang, Haoxiang Ma, Kailin Li, Tao Lu, Jiangmiao Pang, Linning Xu, Dahua Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a hand-skeleton-conditioned world action model that jointly learns visual and skeletal dynamics via a Mixture-of-Transformers, enabling human-to-robot manipulation transfer through a shared motion interface.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21514)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yixuan Feng, Peng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds an action-conditioned world model over coupled liquid-solid porous dynamics, showing reduced retained-water prediction error and improved action selection for robotic multiphase manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21448)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoran Qin (Harbin Institute of Technology, China), Renlong Wu (Harbin Institute of Technology, China), Tianyu Huang (Harbin Institute of Technology, China), Yukang Ding (Taobao, Alibaba Group, China), Hui Li (Harbin Institute of Technology, China), Wangmeng Zuo (Harbin Institute of Technology, China)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Physics-consistent text-to-video framework that models composite motions (coupled, multi-stage, collisions) with dynamics-aware prior matching for one-shot adaptation to unseen physical laws.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21455)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Krishnam Soni, Aditya Sehgal, Vedant Dave, Elmar Rueckert

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Lightweight test-time adaptation for latent world models that freezes the predictor and learns small residual corrections from self-supervised prediction error, improving rollout reliability under distribution shift.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21740)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Nikodem Sebastian Zymla, Laurin Thiele, Johannes Pitz

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Epistemic-uncertainty-driven adaptive rollout truncation for offline world-model training, cutting rollout computation ~72% while matching fixed-horizon prediction accuracy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21482)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guanzhong Sun, Junyi Ma, Yixuan Zhou, Yuxuan Wu, Yanzi Miao, Hesheng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a progress-aligned action-conditioned latent world model whose predicted action consequences are aligned to a target-centric servo coordinate, improving closed-loop visual servoing and transfer.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20892)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pengjun Niu, Yujia Xie, Rui Peng, Hang Zhao, Ke Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a skeleton-guided world-action model with a shared geometric state and video-action transformer that predicts future visual states and action chunks for zero-shot cross-embodiment manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21983)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xuancheng Zhang, Xuetao Liu, Qianying Tang, Jizhe Wang, Zhijing Cheng, Bochen Lin, Haoran Wen, Ming Li, Kun Zhan, Yu Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unifies visual, tactile, and action prediction in a flow-matching Mixture-of-Transformers world-action model, treating tactile signals as future observations to improve manipulation dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21449)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Trinh Tra Giang Nguyen, Thanh Nguyen Vo, Nguyen Hoai Thuong Bui, Ha Duc Bui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decouples predictive world representation learning from video synthesis by aligning frozen V-JEPA latents into a frozen diffusion model's conditioning space for efficient traffic future-video forecasting.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21379)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zhiyuan Gao, Di Wen, Yanxiang Zhan, Mohammad Khoshnazar, Jeroen Sch\"afer, Kunyu Peng, Michael Beetz

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds subtask-guided geometry distillation and implicit world modeling of future 3D interaction dynamics to VLA models, improving spatial and temporal understanding for long-horizon manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21228)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Rui Min, Xianyao Li, Fang Xu, Sofiane Lachab, Jing Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an information-interface audit for world models that separates fidelity from availability gaps and shows repair selection depends on deployment information paths, with closed-loop control evidence.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21155)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 5/10

**作者**: Haoyu Zhou, Joe Watson, Anson Lei, Ingmar Posner

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a compositional continual-learning benchmark for robot-manipulation world models that factorizes knowledge reuse along action and perception axes, revealing modularity's trade-off between reuse and forgetting.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22055)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jiaxing Chen, Hengduo Zou, YuKai Qin, Yiren Zhao, Lidong Yu, Bolin Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces risk-aware occupancy as a dense, temporally aligned, trajectory-queryable scene representation for multimodal trajectory generation and ranking in end-to-end driving, offering a transferable dynamics-representation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21486)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Tim Engelbracht, Ren\'e Zurbr\"ugg, Mayank Mittal, Marco Hutter, Marc Pollefeys, Hermann Blum, Zuria Bauer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies physics-informed digital twins of articulated objects from instrumented human interaction, learning parametric dynamics with a structured neural residual for state-dependent mechanism forces usable as a feedforward dynamics model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21751)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Shengbao Li, Peng Xu, Chao Tang, Hao Wei, Jiaheng Wang, Hong Yin, Jiangtao Chen, Jinxuan Zhu, Zhong Zhou, Mengfan Wang, Tingguang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a hierarchy of predictive sensorimotor representations by jointly forecasting future contact dynamics, augmenting a VLA policy's action stream for contact-rich manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21753)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yichen Liu, Puzhen Yuan, Xiang Zhu, Yanjiang Guo, Jianyu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Geometry-aware latent action modeling that augments image-based latent actions with 3D end-effector motion for cross-embodiment VLA pretraining, indirectly relevant to action-conditioned dynamics learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21948)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Beichen Wang, Yuen-Hei Yeung, V. R. Sridhar Devarakonda, Xuesu Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a 3DGS-based data engine that synthesizes photorealistic visuomotor demonstrations from a single scan, offering a generative environment-simulation pipeline relevant to world-model training data.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21112)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Tianchen Deng, Guole Shen, Yilin Shen, Wenhua Wu, Yilin Fang, Ziqi Ma, Tianjun Zhang, Shenghai Yuan, Wolfram Burgard, Hesheng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an adaptive recurrent world-memory mechanism with gated updates and temporal-spatial regulation for persistent 3D mapping and renderable scene modeling, relevant to memory-centric world models though focused on reconstruction rather than dynamics prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21502)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Shuai Bai, Jiayong Deng, Yikun Fu, Chang Gao, Xuhao Hu, Mianqiu Huang, Yizhen Jiang, Yuheng Jing, Dehui Kong, Keliang Li, Ning Li, Wanli Li, Dayiheng Liu, Dunjie Lu, Changwei Luo, Que Shen, Zheyuan Wang, Zijian Wang, Jie Wu, Gao Wu, Zhihui Xie, Rui Xie, Haiyang Xu, An Yang, Jiakang Yuan, Yanming Zhang, Jiajun Zhang, Xi Zhang, Zhenru Zhang, Zhuo Zhen, Mingkang Zhu, Bowen Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides scalable verifiable interactive computer-use environments with execution-grounded rewards and visual verification, offering a reusable testbed for action-conditioned agentic world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22000)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Etienne Guichard, Stefano Nichele

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes hidden-channel dynamics in neural cellular automata and transfers them for few-shot learning, offering a weak but plausible connection to learned dynamical representations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21870)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Qianru Li, Xuyang Chen, Xuqin Wang, Zhenghao Zhang, Hongyi Luo, Tao Wu, Daniel Cremers, Lu Liu, Yanfeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reframes long-term indoor video relocalization as verification of spatially extended video queries against a compact semantic scene graph, a video-understanding method with only indirect generative/dynamics relevance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21804)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zixiang Zhao, Yansong Feng, Yang Yang, Chaoyu Wang, Haoran Xiao, Hui Zhang, Chuang Cheng, Jianjun Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Closed-loop VLA execution with semantic commitment monitoring and local correction improves long-horizon manipulation but offers only indirect relevance to learned dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21908)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Sichang Su, Benjamin Yang, Zhiyun Deng, Boyuan Liang, Yip Fun Yeung, Zelin Wang, Lingfeng Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Real-world subtask RL fine-tuning for long-horizon manipulation improves policy success but uses no explicit world model or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21788)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zhengyu Tao, Xin Li, Xin Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Forecasting-based tactile-vision-language-action model that predicts future tactile states to guide manipulation, a narrow contact-dynamics forecasting contribution with limited transferable video-generation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20980)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Haolin He, Yunfei Chu, Qi Chen, Wen Huang, Yuan Feng, Muzhi Zhu, Zheqi Dai, Haoning Xu, Dongchao Yang, Chunyat Wu, Zining Liang, Zhengxi Liu, Xiquan Li, Xie Chen, Xize Cheng, Qize Yang, Jin Xu, Qiuqiang Kong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses video generation to synthesize audio-visual dialogue data and benchmarks omni models, a weakly related generative-data contribution with limited direct world-model or video-generation method insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21465)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Somang Lee, Sunkyung Park, Jinhee Yun, Seoki An, Dongjun Lee

**机构**: INRoL

**💡 亮点 (Highlight)**: Introduces a high-fidelity contact-rich physics simulator with optimization-based collision detection and augmented Lagrangian solvers, adjacent to world-model simulation but not a learned dynamics contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21761)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Seth Isaacson, William Hong, Katherine A. Skinner, Ram Vasudevan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses 3D Gaussian Splatting scene representations for risk-aware quadrotor motion planning, a weakly related spatial-representation contribution without learned dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21226)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Hang Jiang, Jinghao Wang, Yiming Zhang, Xinhong Wang, Luwei Ran, Yinfeng Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Frames NeRF deblurring as a dynamic evolution process with temporal memory and world-state-aware priors, offering a weakly transferable dynamics-modeling idea for temporal generative reconstruction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21391)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Frieder Ganz, Maximilian M\"uller

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents on-device diffusion pipeline optimizations (embedding translator, speed/quality/memory sweep) that could transfer to efficient video generation, though the work targets image generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21849)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Hiroaki Kingetsu, Hiroaki Kurihara, Kaoru Yokoo, Kenji Fukumizu, Manohar Kaul

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses LLM-guided synthetic demonstrations to break the zero-reward barrier in VLA adaptation, relevant to embodied dynamics learning but with world modeling only as an auxiliary component.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21650)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Saksham Singh, Zheyuan Hu, Max Sobol Mark, Jeffrey Yu, Zackory Erickson, Aviral Kumar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns subtask-elicited Q-value functions for long-horizon manipulation, offering a value-based long-horizon credit-assignment insight adjacent to world-model planning but without explicit dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.22085)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Haojie Dai, Xiangyi Wang, Liuyi Wang, Kai Sheng, Zongtao He, Chengju Liu, Wei Ye, Qijun Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Dynamic-pedestrian VLN benchmark and policy adaptation with limited world-model insight, only weakly connected to learned visual dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21504)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Seoyeon An, Hyeonseo Jang, Minsu Kim, Chanho Lee, Younghan Park, Kangwook Lee

**机构**: Krafton AI

**💡 亮点 (Highlight)**: Benchmark for multi-hop spatial, temporal, and causal video reasoning in MLLM agents; relevant to dynamics understanding but offers no generative or world-model method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21386)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Zicheng Zhao, Dongyin Chen, Rui Xu, Yinghui Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Executable physics benchmark for bridge design with post-failure rollout evidence; touches physical dynamics and repair but is a benchmark rather than a world-model or video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.21493)

---

