# 💡 今日研究速览 (Daily Summary)

### World Models & Interactive Simulation

The dominant thread today is the maturation of world models from passive predictors into physically consistent, interactive simulators. DeltaWorld and XGenAct both push action-conditioned latent dynamics toward long-horizon manipulation, with XGenAct unifying RGB, action, depth, normal, and segmentation within a single video diffusion transformer. A striking convergence is the treatment of video diffusion priors as latent physical knowledge: Parasitic Co-Denoising recovers 3D human motion from a frozen video model, while "Does Physics Live in the Activations?" shows physical quantities are linearly decodable and steerable. Complementing this, SpectralCache and TRAC attack the inference cost of diffusion and autoregressive world models respectively, with SpectralCache achieving up to 5.22x acceleration via training-free singular subspace reuse. Collectively, the field is shifting from "can we generate plausible futures" to "can we generate controllable, physically grounded, and efficient ones."

### Plannability, Action Sensitivity & Continual Adaptation

A critical self-examination is underway regarding whether low latent prediction error actually implies usable dynamics. "Keeping JEPA World Models Plannable" and the Counterfactual Action Evaluation audit both diagnose action-insensitivity and observation bottlenecks in JEPA-style models, with the former repairing plannability via an inverse-dynamics auxiliary loss without retraining. TwinJEPA extends this line by injecting offline-mined action-preference supervision into JEPA representations for goal-conditioned control, while VIGOR enforces augmentation-invariant latent dynamics to combat compounding errors. On the continual side, "What Should World Models Forget?" reframes retention as a stratified problem by invariance timescale, arguing that revising instance-level knowledge is required behavior rather than catastrophic forgetting. Together these works signal a maturation in evaluation: the community is no longer satisfied with representation quality metrics and is instead probing whether learned dynamics are actionable, sensitive, and appropriately plastic.

### Long-Horizon & Consistent Video Generation

Consistency over extended rollouts remains a central challenge, with several training-free approaches emerging. Weave Forcing introduces compositional memory routing with semantic slot masking and coverage-adaptive RoPE for cross-shot subject and background consistency, while Custom Forcing uses persistent KV-cache anchor frames with drift-adaptive value amplification for subject customization. LoGo blends global and spatially localized rewards for fine-grained credit assignment, reducing 3D inconsistency and object drift. SymRegFlow brings symmetry-regularized flow matching for multi-view consistency without novel-view RGB supervision, and DuoMatching improves few-step streaming generation via joint-marginal distribution matching. The trend is clear: training-free, memory-centric interventions are becoming the preferred lever for long-horizon coherence, sidestepping expensive retraining.

### Embodied Reasoning, Planning & Policy Learning

World models are increasingly being positioned as substrates for reasoning and planning rather than mere simulators. ProAR turns autoregressive video generation into goal-directed reasoning via goal-frame prediction and future-representation self-alignment, while "Rethinking World-Action Model" plans visual subgoals and jointly predicts future trajectories and actions for compositional manipulation. Native Action-Prior Learning pretrains policies directly from observation-only videos via flow-matching supervision, and Proprioceptive Sketches provides long-horizon intent without costly video or subgoal-image forecasts. EpiWorld grounds an LLM policy agent in a learned epidemiological world model for counterfactual rollouts, and Ego2World compiles egocentric cooking videos into executable symbolic planning environments with separate world and belief states. The unifying insight is that world models are becoming the interface layer between perception, memory, and action selection.

### Benchmarks, Evaluation & Safety

A notable cluster of work targets rigorous evaluation of world-grounded understanding. World Embedding Benchmark probes how video embeddings encode physical information, 4DCodeBench tests agents on inverse graphics of dynamic scenes, and TerraVis evaluates world-grounded visual consistency in text-to-image generation via MLLM workflows. CriticHack offers a cautionary analysis of how learned visual rewards can amplify wrong-object failures during robot policy optimization, while SceneFactory-3D and TerrainForge provide physics-grounded counterfactual driving simulators for safety evaluation. World Editing formulates interventions on executable worlds along an intervention-depth axis. The collective message is that as world models proliferate, the bottleneck is shifting from generation capability to trustworthy, standardized evaluation of physical fidelity and controllability.

### Multimodal & Cross-Modal Fusion

Cross-modal grounding continues to deepen, with UniDynamics fusing event and RGB streams for unified future 4D dynamic scene generation via event-latent motion priors. SimpleTouch augments a VLA with a tactile expert trained through multi-horizon future tactile latent prediction—a weakly world-model-flavored objective for contact-rich manipulation—raising the question of whether VLA models can master contact-rich tasks without tactile policy pretraining. World Action Learning distills interaction-centric latent actions from egocentric video by separating observer-induced motion from hand-object interaction. The trend here is toward richer sensory fusion and disentangled representations that isolate the agent's contribution from exogenous dynamics.

### Motion Representation & Generative Efficiency

Finally, representation-level innovations are reshaping motion and action generation. "Rethinking Fixed Temporal Grids" introduces wavelet-based frequency-disentangled motion representation with unified residual quantization, improving high-frequency fidelity with transferability to temporally heterogeneous video generation. "How To Train Your World Model" systematically compares fine-tuning versus RAG for LM-based text world models, proposing a hybrid with counterfactual retrieval-error estimation. Together with the caching and acceleration work above, these papers reflect a broader push toward efficiency and structured representations that respect the temporal and frequency characteristics of real-world dynamics.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Boyuan Hou, Xiaoge Cao, Chaofan Zhang, Shuo Wang, Shaowei Cui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces action-conditioned latent increment prediction with interaction-aware alignment to produce physically consistent long-horizon interactive world-simulator rollouts for manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02691)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Daikun Liu, Xin Zhan, Teng Wang, Xiaoping Wang, Changyin Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates future 4D dynamic scenes (RGB, depth, flow) from a single event-RGB pair via event-latent motion priors and a perceptual dynamics space that enforces geometric-motion consistency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03473)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziyi Wang, Junchi Yao, Heqian Qiu, Wenbo Shi, Chengjiu Wang, Jinyang He, Binkai Hong, Hongliang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free compositional memory routing with semantic slot masking and coverage-adaptive RoPE improves cross-shot subject and background consistency in interactive long video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03510)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shukai Gong, Xuanran Zhai, Yintianrun Zhang, Ruopeng Cui, Ye Huang, Yiyang Fu, Dexuan Lyu, Chaojie Li, Xinyi Song, Peiwen Lin, Chuang Wang, Mingyuan Jia, Yufan Deng, Jiaxin Fang, Bo Liang, Jiaxin Li, Yuxiang Gao, Hao Liu, Daquan Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Hierarchical world-action model that plans visual subgoals and jointly predicts future visual trajectories and actions, enabling compositional and in-context robotic manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02368)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhendong Mi, Pu Zhao, Ziyu Hu, Xiaodong Yu, Yanzhi Wang, Grace Li Zhang, Shaoyi Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free spectral feature caching that reuses stable singular subspaces across denoising steps to accelerate diffusion-based interactive world models by up to 5.22x.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02660)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Florian Strohm, Patrick Wagner, Jannik Schwab, Marco Huber

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses action-insensitivity in JEPA latent world models on low-motion scenes and repairs plannability with an inverse-dynamics auxiliary loss plus a cheap action-sensitivity probe, enabling language-goal planning without retraining.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03137)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tingting Du, Ziyao Wang, Guoheng Sun, Ang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unifies RGB, action, depth, normal, and segmentation prediction into a single video diffusion transformer world action model, improving closed-loop manipulation success and future spatial prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03516)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Turns autoregressive video generation into goal-directed reasoning via goal-frame prediction with asymmetric attention and future-representation self-alignment, improving long-range coherence and embodied reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03664)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziqi Ma, Shreya Sharma, Mohamed El Banani, Katja Schwarz, Chongjie Ye, Chao-Yuan Wu, Li Fei-Fei, Ben Mildenhall, Georgia Gkioxari, Justin Johnson, Gowthami Somepalli

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves long-horizon camera-controlled video generation by blending global and spatially localized rewards for fine-grained credit assignment, reducing 3D inconsistency and object drift.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03636)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Nishit Anand, Ramani Duraiswami, Dinesh Manocha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates continual world models with stratified retention by invariance timescale, arguing that revising outdated instance-level knowledge is required behavior and proposing differential retention metrics that separate invariant regression from revision latency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03713)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jonas Kneifl, Jakub Skalski, Bart{\l}omiej Twardowski, Kamil Deja

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Probes video diffusion transformers to show physical quantities are linearly decodable and localized in activations, and that probe directions can steer generation, giving insight into whether video models internalize physics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03154)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhaochong An, Fei Zhang, Menglin Jia, Duncan Frost, Zijian Zhou, Yikai Wang, Xudong Wang, Aditya Patel, Belinda Zeng, Tao Xiang, Serge Belongie, Amir Bar, Sen He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Pretrains an action policy directly from observation-only videos via future-video flow-matching supervision propagated through transition-structured joint attention, enabling scalable world-action model learning without action labels.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03391)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yunseung Ok (Kyung Hee University), Hyunsoo Kim (The University of Texas at Austin), Minseo Kim (Kyung Hee University), Suhyun Kim (Kyung Hee University)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free subject customization for autoregressive video generation using persistent KV-cache anchor frames with drift-adaptive value amplification and anchor contrast guidance to preserve identity over long rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02914)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xi Ye, Yuzhu Wang, Xiaoyang Liu, Jiayi Wang, Yangyang Xu, Ruyu Wang, Wenlin Chen, Duo Su, Jun Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Symmetry-regularized flow matching enables multi-view-consistent video world models across continuous camera poses without novel-view RGB supervision, improving FVD and instance preservation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02726)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Arjun Subramanian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Audits joint-embedding predictive world models to show low latent error does not imply action sensitivity, isolating observation bottlenecks and representation geometry issues in learned dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02860)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Jiaxing Song, Weiqi Yan, You Huang, Mingte Qiu, Huazhong Liu, Xiaofeng Zhu, Yunshan Zhong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free acceleration for autoregressive video generation that addresses error accumulation across chunk-level denoising trajectories via cumulative scheduling, trajectory-aware guidance, and spectral structure correction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02779)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves few-step streaming video generation by adding marginal frame-level distribution matching from an image teacher to joint video matching, with LatentBridge for latent mismatch and Latent Variation Sampling for temporal supervision spread.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03543)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yunjiao Zhou, Junlang Qian, Lihua Xie, Jianfei Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that frozen video diffusion models implicitly encode recoverable 3D human motion across the denoising schedule and decodes it via a parasitic co-denoising flow-matching decoder, revealing motion knowledge in video generative priors.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03047)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Max Ku, Nok-Kan Law, Yu-Chien Tang, Shih-Ying Yeh, Ping Nie, Andy Zheng, Tat Hei Lai, Fei-Yueh Chen, Nikko Yu, Wei-Chieh Sun, Suzy Huang, Chiao-Wei Hsu, Chih-Chuan Huang, Chak-Wing Mak, Ho Yin Sam Ng, Edisy Kin Wai Chan, Min-Hung Chen, Ho Kei Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates world editing as interventions on executable worlds with an intervention-depth axis, providing a benchmark and insight into controllable world-model manipulation distinct from generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02331)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Feiran You, Hongyang Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments JEPA latent-dynamics world models with offline-mined action-preference supervision (reward-gap regression plus preference classification) to improve goal-conditioned control representations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02922)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zeeshan Memon, Yiqi Su, Kai Shu, Naren Ramakrishnan, Liang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Grounds an LLM policy agent in a learned action-conditioned epidemiological world model enabling counterfactual rollouts for closed-loop policy selection.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02744)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zhiming Liu, Yikun Miao, Ying Chen, Hongrui Yin, Fangqi Zhu, Xiaoyi Pang, Quanxin Shou, Zhengyang Yan, Haodong Wang, Song Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distills interaction-centric latent actions from egocentric video by separating observer-induced motion from hand-object interaction and aligning low-frequency spectral structure with robot behaviors for policy transfer.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03607)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Mingyu Park, Samyeul Noh, Hyun Myung, Donghwan Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves zero-shot visual generalization in model-based RL by enforcing augmentation-invariant latent dynamics consistency, addressing compounding errors in recursive latent rollouts of learned world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02801)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 5/10

**作者**: Dhananjay Ashok, Shantanu Agarwal, Vivek Datla, Jonathan May, Alfy Samuel

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically compares fine-tuning versus RAG for LM-based text world models and proposes a hybrid system with counterfactual retrieval-error estimation and hierarchical query reformulation for more accurate transition dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02542)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yang Chen, Yicheng Zhu, zhenning Li, Tao Li, Zilin Bian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Couples road-geometry edits with four-wheel vehicle dynamics to propagate counterfactual changes through motion, camera viewpoint, and clearance, yielding a physics-grounded generative driving-scene framework relevant to controllable dynamics simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02825)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Fangyuan Wang, Songhao Huang, Haoxiang Sun, Shipeng Lyu, Chengyang He, Anqing Duan, Peng Zhou, David Navarro-Alarcon

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generative action policy that jointly predicts a timing-free proprioceptive sketch of the remaining joint-space path and a dense action chunk, providing long-horizon intent without costly video or subgoal-image forecasts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02759)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yicheng Zhu, Linfeng Tian, Tianmu Zhao, Yang Chen, Fan Zuo, Tao Li, Zilin Bian

**机构**: SmallWorldLab

**💡 亮点 (Highlight)**: Physics-grounded multi-agent driving simulator enabling matched counterfactual closed-loop rollouts under varying friction and terrain, useful for evaluating learned dynamics and policy robustness.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02874)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yunjiao Zhou, Junlang Qian, Gen Li, Xinying Guo, Lihua Xie, Jianfei Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Wavelet-based frequency-disentangled motion representation with unified residual quantization improves high-frequency motion fidelity, transferable to temporally heterogeneous video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03012)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Qinchuan Cheng, Zhantao Gong, Pengzhan Sun, Angela Yao, Shijie Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Compiles egocentric cooking videos into executable symbolic planning environments with separate world state and belief state, offering a reusable testbed for studying how memory and planning choices affect action validity and observation demand in partially observed dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02715)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Yiqi Liu, Ruifeng Yuan, Yang Wang, Long Li, Fengyu Cai, Hou Pong Chan, Jialin Yu, Hao Zhang, Chenghua Lin, Chenghao Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark probing how video embeddings encode physical information, showing retrieval-augmented references improve physical fidelity of generated videos.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03632)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jiaxuan Luo, Xingguo Xu, Shanshan Wang, Yuhan Zhou, Zhen Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes how learned visual reward models can amplify wrong-object failures during robot policy optimization, offering a tilt-model account of reward-driven outcome shifts relevant to embodied dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02527)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Chen Yang, Linzhe Shi, Changjie Wu, Hang Zhang, Ronghan Chen, Lingjun Zhang, Xu Hu, Mu Xu, Jiansheng Fan, Chen Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments a VLA with a tactile expert trained via multi-horizon future tactile latent prediction, a weakly world-model-flavored dynamics objective for contact-rich manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02784)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Ruihong Shen, \v{Z}iga Kova\v{c}i\v{c}, Peter Kulits, Xingrui Wang, Zizhang Li, Joshua B. Tenenbaum, Alan Yuille, Jieneng Chen, Jiajun Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for 4D inverse graphics via code generation that probes agents' ability to represent dynamic scene structure and physical dynamics, offering a testbed for world-dynamics understanding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.03715)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Shuai Fu, Jing Gu, Jian Zhou, Zicheng Duan, Gengze Zhou, Qi Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an MLLM-based evaluation framework for world-grounded visual consistency in generated images, offering a diagnostic taxonomy relevant to physical plausibility in generative models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.02959)

---

