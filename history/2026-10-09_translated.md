# 💡 今日研究速览 (Daily Summary)

### World Models & Interactive Dynamics
Today's papers show a decisive shift from passive video prediction toward *interactive, action-conditioned world models* that can be queried, planned within, and even repaired. A notable cluster focuses on making latent rollouts both cheaper and more accurate: cost-gradient token selection and parallel causal trajectory prediction each attack the core bottleneck of autoregressive decoding, trading sequential feedback for sparsity or parallelism while preserving control performance. A second theme is *diagnosis and repair* — work on failure insensitivity and physics-violation correction (via counterfactual replay and adversarial preference optimization) treats released world models as artifacts to be audited and fixed rather than retrained, while SGF+ and the ultrasound world model push the frontier on long-horizon and modality-specific (clinical, untracked video) interactive prediction. A third thread distills world-model structure into policy learning: action tangent fields and JEPA-style predictive latents serve as teachers for VLA policies and robot manipulation, suggesting that the field is converging on world models as *supervisory infrastructure* for embodied control rather than as ends in themselves. Finally, graph-based surveys and object-centric memory representations (persistent 3D object memory, instance-centric Gaussian forecasting) point toward more structured, interpretable dynamics backbones for dynamic environments.

### Vision-Language-Action & Embodied Agents
VLA research today is dominated by the problem of *reliability under closed-loop execution*. State hallucination is analyzed mechanistically and mitigated through sparse-feature unlearning, while diversity-driven RL fine-tuning and task-progress distillation both target generalization by expanding or abstracting the space of successful behaviors. A recurring insight is that supervision should be *execution-grounded*: policy-in-the-loop refinement for humanoid motion tracking and physics-grounded post-training of interaction generators both convert rollout failures into learning signal, echoing the world-model repair theme above. Complementing these, automated video-language grounding enriches manipulation data with contact and semantic annotations, and language-guided tempo control adds a controllability axis to VLA policies. Benchmarks like RoboQuest expose a complementary weakness — frontier multimodal agents terminate exploration prematurely — reinforcing that the central challenge is no longer perception but sustained, physically plausible interaction.

### Video Generation & Controllable Synthesis
The video generation papers converge on *decoupling and control* as the levers for quality and efficiency. Decoupled gradient flows enable 24-hour extrapolation without long-video fine-tuning, while parallel adapter composition brings joint audio-video generation into real-time streaming regimes. Controllability is addressed from multiple angles: geometry-grounded pose tokenization for camera trajectories, relational abstractions for structured spatial reasoning, and contextual grounding that converts viewer/source context into executable constraints for interactive storytelling. Efficiency remains a first-class concern, with offline-to-online RL cache scheduling targeting terminal rather than step error under explicit speedup budgets — a mature framing that treats acceleration as a fidelity-constrained optimization problem rather than a heuristic.

### Physical Consistency, Simulation & Evaluation
A strong evaluative current runs through today's submissions. The counterfactual benchmark for physical plausibility (shadows, reflection, support, occlusion) provides a diagnostic lens directly applicable to generative visual models, while the deformable-linear-object work demonstrates that structured dynamics can be learned end-to-end from video for simulation under user control. For autonomous driving, instance-centric 4D Gaussian forecasting offers compact object-centric dynamics, and simulation-in-the-loop uncertainty assessment reframes the question from perception uncertainty to *decision-critical* uncertainty via fast-slow VLM collaboration. Generative 2D-3D hand motion recovery and long-context clinical video benchmarks round out a set that emphasizes temporal consistency and cross-representation correspondence over single-frame accuracy. Collectively, these works signal a maturation of evaluation: the field is building targeted diagnostics for the specific failure modes — physical implausibility, horizon drift, premature termination — that separate demo-quality from deployment-quality systems.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Keke Yang, Erqi Wang, Sainan Guan, Hongliang Ren

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Self-distills a video foundation model into an interactive ultrasound world model from untracked clinical videos, using an Acoustic Sampling Map to encode probe pose and imaging geometry for action-conditioned future prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09785)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decouples context-writing from denoising parameters in autoregressive video generation, improving visual quality and enabling 24-hour long-horizon extrapolation without long-video fine-tuning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10429)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yingchen Xu, Edward Grefenstette

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free cost-gradient token selector that makes latent planning in token-based visual world models substantially cheaper while preserving control performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10274)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ke Wu, Hanwen Huang, Bo Gu, Kaizhao Zhang, Xiangting Meng, Yupeng Zheng, Zijun Xu, Jieru Zhao, Wenchao Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Distills action tangent fields from an action-conditioned world model into world action models, concentrating future-prediction supervision on action-relevant dynamics for more robust robot policies.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09734)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiuyi Xu, Xiao Hu, Meida Chen, Peng Gao, Yang Ye, Yangming Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses failure insensitivity in robot world models and introduces execution-verified counterfactual replay (CureWM) to repair released checkpoints, improving success-failure discrimination without architectural changes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09134)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kerui Li, Zhe Jing, Chenyi Huang, Xiaofeng Wang, Zheng Zhu, Haoming Cui, Huaibo Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces adversarial physics preference optimization in flow-matching denoising space to correct localized physics violations in robotic manipulation video generation, improving downstream execution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09454)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wanjin Feng, Baobin Zhang, Ao Yu, Shibo Feng, Xi Wang, Xingyu Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replaces autoregressive rollout with parallel causal trajectory prediction in a visual world model, removing decoded-state feedback to improve long-horizon prediction accuracy and CEM planning speed.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08627)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuchen Zhu, Chenyi Xu, Yulin Zhang, Gang Xu, Wentao Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds an action-conditioned JEPA world model that serves as predictive teacher and adaptable dynamics model for VLA policies, improving closed-loop rollout and test-time adaptation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09940)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jingyu Li, Xiaoxiao Xiang, Yiwen Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Parallel adapter composition enables real-time streaming joint audio-video generation with few-step sampling, improving video-generation efficiency and long-horizon coherence.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10343)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhenyang Liu, Chenjie Cao, Yisu Zhang, Xuhui Zuo, Xiangyang Xue, Yanwei Fu, Tengfei Wang, Chunchao Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Autoregressive camera-trajectory generator with geometry-grounded pose tokenization enables controllable, collision-aware camera paths for video generation and robotic perception.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09513)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Shravan Chaudhari, William Paul, Suchi Saria, Rama Chellappa, Homanga Bharadhwaj

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a persistent 3D object memory from egocentric video that tracks object locations, histories, and context for later spatial queries, offering a useful object-centric memory representation for embodied world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10538)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang, Teng Hu, Songhang Shen, Bohao Feng, Hongqian Deng, Ran Yi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Latent-aware offline-to-online RL cache scheduling for video diffusion acceleration that targets terminal rather than step error, improving fidelity under user-specified speedup budgets.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10457)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Akshun Sharma, Kimia Forghani, Yancy Diaz-Mercado

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a structured dynamics model of deformable linear objects directly from video, enabling parameter estimation and simulation of thread motion under user-defined control inputs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10039)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Bingxuan Li, Yiwen Song, Xueqing Wu, Yanzhou Pan, Yang Li, Kuang Su, Jingyun Liu, Sebastian Ko, Huan Zhang, Tong Zhang, Nanyun Peng, Tomas Pfister, Yale Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates contextual grounding for interactive video storytelling, converting heterogeneous viewer/source context into executable constraints for controllable video continuation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09326)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Shuaijun Liu, Chenglong Zhang, Xuhao Liu, Feiyang You, Yifan Liao, Shuyang Hao, Chaozhe Zhang, Chengyu Wu, Zhen Sun, Ningxin Su

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses policy-in-the-loop execution feedback to refine video-driven humanoid motion tracking, turning rollout failures into supervision for physically plausible motion generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09055)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Hwanhee Jung, SeungHyeon Kim, Inkyu Koo, Qixing Huang, Sang Ho Yoon, Sangpil Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Instance-centric 3D Gaussian query representation for temporally consistent 4D occupancy forecasting, offering a compact object-centric dynamics model for autonomous driving.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09444)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Chen Xu, Yunqi Li, Binbin Huang, Brent Yi, Shenghua Gao, Yi Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generative joint 2D-3D hand motion recovery from video learns temporal dynamics and cross-representation correspondence, yielding smoother, more temporally consistent motion than per-frame pose estimation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10512)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Kerui Chen, Jianrong Zhang, Kai Lv, Hehe Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Co-adaptive generator-tracker framework uses physics-grounded preference alignment (DPO) to make generated humanoid interaction motions more physically plausible and executable in simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10322)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: M. Moein Esfahani, Sepehr Salem, Mohammed Alser, Vince Calhoun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a counterfactual benchmark for diagnosing physical plausibility violations (shadows, reflection, support, occlusion) in edited images, providing a diagnostic lens relevant to physical consistency in generative visual models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09205)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jiho Lee, Jeongeun Park, Heayoun Choi, Taekyung Kim, Eunwoo Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes and mitigates state hallucination in VLA policies via sparse-feature unlearning, giving a mechanistic insight into unreliable dynamics/state tracking in embodied models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09496)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jiayi Chen, Shuai Wang, Guangxu Zhu, Derrick Wing Kwan Ng, Chengzhong Xu, Kaibin Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Simulation-in-the-loop uncertainty assessment for fast-slow VLM collaboration in driving, using scene realizations to evaluate planning-relevant uncertainty rather than perception uncertainty alone.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09520)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Ana Ezquerro, Ozan \"Ozdenizci

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses object-centric relational abstractions to guide diffusion models toward structured spatial reasoning constraints, with transferable representation ideas for controllable generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09780)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Haoru Li, Jinmei Liu, Zhiyong Wang, Xiaoming Li, Zhenhong Sun, Daoyi Dong, Chunlin Chen, Zhi Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diversity-driven RL fine-tuning for VLA policies improves closed-loop generalization, offering a weakly related insight into exploration and successful-mode coverage in embodied rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09943)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Wenxi Gan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Task-progress distillation for small agents is only weakly tied to learned dynamics or video generation, but its stage-based subgoal abstraction is loosely relevant to state abstraction in sequential decision making.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10332)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yeonseo Lee, Hyosup Shin, Guebin Hwang, Sungho Jo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Language-guided tempo control for VLA policies is adjacent to controllable action-conditioned generation, though it offers limited direct insight into world models or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09451)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Songbo Hu, Qiayuan Liao, Yufeng Chi, Kevin Zakka, Yakun Sophia Shao, Pieter Abbeel, Koushil Sreenath

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns whole-body humanoid loco-manipulation from robot-free human demonstrations via a visual planner plus RL tracker with mutual error augmentation, offering limited but plausible dynamics-modeling insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09117)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Samira Huber, Ruben Hammele, S\"oren Pirk

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Curiosity-driven object-ownership learning with long-term spatial memory supports embodied reasoning and navigation, tangentially relevant to world-model memory and state abstraction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09358)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Masatoshi Tateno, Takehiko Ohkawa, Yueh-Hua Wu, Hanlong Li, Tatsuya Matsushima, Yoichi Sato, Kei Ota

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Automated video-language grounding enriches manipulation demonstrations with contact and semantic annotations, indirectly supporting action-conditioned video understanding for VLA alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.09718)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Leon Mayer, Lucas Luttner, Patrick Godau, Kai Fritzsche, Annika Reinke, Leonie Boland, Jule Brandt, Janne Heinecke, Chloe K. Nobuhara, Niklas Holzwarth, Evangelia Christodoulou, Marcel Knopp, Dominik Michael, Pascale Piermarco, Saliq Neyaz, Korhan Derin \"Ozarslan, Jakob Hennighausen, Carlos Aumente-Maestro, Tim R\"adsch, Dheeraj Baji, Peter Maximilian Full, Finn Aichholz, Justus Veit Erpenbeck, Linus Finn Schott, Bastian Winkelhausen, Claas de Boer, Bianca G\"uttner, Anneli Hummel, Gregor Just, Max Kirchner, Chenyang Li, Rozenn Raffaut, Ariel Rodriguez, Danush Kumar Venkatesh, Kevin Wang, Jinjing Xu, Mona Sheikh Zeinoddin, Salman Khan, Thomas M. Pausch, Stefanie Speidel, Danail Stoyanov, Daniel A. Hashimoto, Fiona R. Kolbinger, Thomas G. Weiser, Lena Maier-Hein

**机构**: Heidelberg University

**💡 亮点 (Highlight)**: Long-context video understanding benchmark probing cumulative temporal consistency over hours-long procedures, offering evaluation insight relevant to long-horizon video modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10156)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Liu Renhang, Navonil Majumder, Tej Deep Pala, Soujanya Poria

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for goal-directed embodied exploration highlights that frontier multimodal agents stop exploring too early, giving indirect insight into interactive dynamics and information-gathering behavior.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10388)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 2/10

**作者**: Marco Giberna, Miguel Fernandez-Cortizas, Jose Luis Sanchez Lopez, Holger Voos

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Surveys graph-based world models for dynamic environments, organizing representations, construction pipelines, and downstream exploitation with emphasis on hybrid factor-scene graph models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.08800)

---

