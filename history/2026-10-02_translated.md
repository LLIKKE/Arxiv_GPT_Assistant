# 💡 今日研究速览 (Daily Summary)

### World Models & Latent Dynamics

Today's submissions reveal a maturing consensus that the central challenge in world modeling is no longer architectural scale but the *fidelity and diagnosability of latent dynamics*. MEND attacks the silent compounding of autoregressive errors by unifying detection, localization, and correction of latent hallucination in a single conditional score network operating on frozen backbones—an elegant reframing of hallucination as a measurable latent-space pathology rather than a surface artifact. Complementing this, the cellular-automata diagnosis paper provides a rare mechanistic post-mortem: conventional world models fail not because of capacity but because they violate spatial/temporal locality and temporal stability in information flow, and enforcing these inductive biases yields near-perfect rollouts without touching the backbone. Abductive world modeling pushes in the opposite direction, inferring latent causal factors (entity, dynamic, relation) from predicted futures to improve physical and causal reasoning over V-JEPA. A striking convergence emerges around *action-conditioned* world models as practical control substrates: RoboCoach uses imagined failures to actively select demonstrations for compositional skills, LocoWM drives preactive residual corrections for high-precision locomotion, and the planning-learning loop paper closes the gap via hybrid multi-step TD targets with disagreement-aware terminal values. Notably, the air-hockey distillation result suggests that a diagonal linear recurrent memory suffices to capture the memory-dependent structure of a DreamerV3 policy—a provocative data point that much of what we call "world-model memory" may be lower-rank than assumed.

### Embodied Agents & Vision-Language-Action Policies

The VLA literature today is converging on a shared thesis: *future-awareness is the missing ingredient for reliable closed-loop control*. MotionWeave grounds action-induced motion in local visual regions and injects horizon-residual cues, deliberately avoiding full-frame prediction—an implicit argument that world models for control should model motion, not pixels. EWAM's emergent depth-wise specialization (semantics → visual foresight → action) offers a concrete mechanistic picture of how a unified embodied model can hand off across abstraction levels. DSDyn-VLA and the stage-aware two-step flow denoising paper both target the latency bottleneck, with the latter's stage-aware denoising directly transferable to faster action-conditioned video generation. Around memory and state abstraction, action-conditioned bisimulation for GUI agents and the skill-level memory benchmark for partially observable manipulation both point to the same gap: agents need compact internal representations of *hidden* task state, not just longer context. EVOKE's elicitation of internalized world knowledge via goal-diverse action ranking at fixed states is a clever workaround for agents that cannot afford explicit future prediction. Meanwhile, the robustness picture is sobering: the camera-fault failure-mode analysis and the instruction-action binding diagnosis both show that current VLAs degrade catastrophically under distributional perturbations, and the GPT-6 Astra evaluation underscores a persistent gap between high-level task reasoning and reliable physical control. The biophysically detailed *C. elegans* dynamical core is an outlier but raises a genuinely interesting question about whether fixed, evolutionarily-shaped dynamical priors can outperform learned ones in low-data embodied regimes.

### Video Generation & Physical Consistency

Video generation research today splits cleanly into *controllability* and *physics*. On controllability, the mid-stream prompt-switch work introduces a training-free segue planner with span-restricted DMD supervision to enforce faithful state transitions rather than shortcuts—a subtle but important distinction between *appearing* to transition and actually transitioning. ThinkV2V activates MLLM reasoning as refined conditioning for instruction-guided editing, with inference-time thinking scaling improving causally demanding edits. TripleFlow's training-free coupling of residual erasure and native synthesis, and PARK's query-preserving sparse attention for video DiTs, both push efficiency without sacrificing fidelity. On physics, PhyProbe's lightweight evaluator trained with a unified ranking/regression/calibration objective is a welcome reusable signal, and MindWorldBench's finding that image-to-video models exhibit an *omniscient bias*—failing to align behavior with latent mental states—is a sharp diagnosis of a failure mode that physical-consistency benchmarks alone would miss. The stereo audio-visual correspondence work and Audible World Models both extend world state into persistent multimodal territory, with the latter's spatially anchored, listener-dependent sound being a genuinely novel axis of environment state. Uncertainty-aware consistency distillation achieving 4-step generation from a 50-step teacher is a solid efficiency result, and the precipitation nowcasting paper is a useful reminder that domain-specific dynamics priors plus timestep-aware RL can outperform generic video backbones on scientific forecasting.

### Efficiency, Compression & Representation

Quantization and token compression are increasingly being co-designed with the downstream control or generation objective rather than treated as post-hoc optimizations. SteerQuant's action-guided 4-bit quantization for world-action models is the clearest example: rather than minimizing uniform numerical error, it steers error toward computations with less influence on final actions—an objective-aware compression principle that should generalize well beyond this setting. CoVisco's codec-native vision encoder with native token compression targets long-video understanding, and RESUME's stateful codec representation where predictive frames update a carried latent state offers a recurrence mechanism that could plausibly transfer to video dynamics modeling. The continuous-video SSL work (StreamMAE) addresses a real gap—most video pretraining assumes clip boundaries that do not exist in streaming deployment—and its stream-aware regularization and motion-biased crops are simple but well-motivated.

### Evaluation, Safety & Benchmarks

Two benchmark contributions stand out for probing *interactive* and *mental-state* reasoning rather than static perception: WorldAuditBench's interactive 3D world auditing with multimodal agents, and MindWorldBench's mental-state-to-behavior evaluation. Both expose failure modes that standard video or VQA benchmarks miss. On the safety side, BadAction's backdoor study on interactive video generation is the first systematic demonstration that action-guided triggers can freeze future frames and break action controllability—a threat model that becomes far more consequential as these systems move into closed-loop deployment. The physical failure-mode analysis of VLAs under camera faults rounds out a picture in which robustness and adversarial exposure are becoming first-class concerns rather than afterthoughts.

### Simulation, Dynamics & Cross-Cutting Methods

A quieter but potentially important thread concerns *differentiable and physically-grounded simulators* as substrates for learned dynamics. PneuTac's unification of MPM dynamics with 3D Gaussian splatting for soft-robot and tactile simulation, and the terrain traversability work's uncertainty-aware continual learning of pre-contact interaction dynamics, both represent the kind of grounded dynamics models that pure video-based world models struggle to match in contact-rich regimes. The neural cellular automata reasoning paper is a conceptual outlier worth flagging: strictly local asynchronous updates producing dynamics that generalize to larger grids and longer rollouts is precisely the locality property that the cellular-automata diagnosis paper identified as missing from conventional world models—suggesting that NCA-style architectures may deserve renewed attention as decentralized alternatives for learned visual dynamics. Finally, the egocentric human data scaling study within a unified world-action model offers a useful empirical anchor: human-robot alignment, task diversity, and video-only supervision all matter, but not uniformly, and the field would benefit from more such controlled scaling analyses.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ali J Alrasheed, Aryan Yazdan Parast, Basim Azam, James Bailey, Naveed Akhtar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a single conditional score network that detects, localizes, and corrects latent hallucination in frozen world models at inference time, addressing silent compounding autoregressive errors in learned visual dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39182)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Shaoyang Guo, Ziming Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses why conventional world models fail to learn exact cellular-automata dynamics and shows that spatial/temporal locality and temporal-stability fixes in information flow yield near-perfect rollouts without changing the backbone.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39604)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ziqi Liu, Songhan Yang, Linfan Zhou, Jiatong Liu, Lijun Peng, Long Wan, Yinqi Bai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes abductive world modeling that infers latent causal factors (entity, dynamic, relation) from predicted futures, improving physical prediction, causal reasoning, and action understanding over V-JEPA.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36985)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zejing Rao, Ketong Ren, Xiaoqiang Liu, Yiping Meng, Guoxin Zhang, Fan Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free segue planner plus span-restricted DMD supervision to make mid-stream prompt switches in streaming video generation execute faithful state transitions rather than shortcuts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38691)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhihao Zheng, Mooi Choo Chuah

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns an action-conditioned latent world model from egocentric RGB video with a realizable inverse-dynamics objective, using nominal-realizable discrepancy as a safety signal for planning in social navigation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.40177)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yun Dai, Jiarui Wen, Huiping Zhuang, Cen Chen, Ziqian Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free sparse attention with query-preserving and query-aware key clustering improves block retrieval accuracy, accelerating video diffusion transformers while preserving generation quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38978)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jingqiu Wang, Yan Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Motion-centric future-dynamics framework for VLA policies that grounds action-induced motion in local visual regions and injects horizon-residual motion cues, offering a useful world-model insight for action-conditioned dynamics without predicting full future frames.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39324)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hao Wang, Jiajun Wen, Jingzhi Liu, Shuoshuo Xue, Zhiliang Chen, Min Lin, Yicheng Chang, Xiaoyu Guo, Yukang Zhuo, Zheng Chong, Yunshuang Nie, Jian Zhang, Weijia Liufu, Qingman Wu, Heming Xu, Bingchang Song, Dantong Wu, Zhiyuan Wang, Hang Xu, Jianhua Han, Bokui Chen, Shen Zhao, Rui Li, Xiaodan Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified embodied model with asymmetric joint attention that learns an emergent depth-wise handoff from semantic features to predicted future frames to action, giving a concrete world-action modeling insight for visual foresight in control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39973)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces uncertainty-aware consistency distillation that reweights spatiotemporal supervision by local temporal difficulty, enabling high-quality 4-step video generation from a 50-step teacher.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39132)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongjia Zhai, Xiyu Zhang, Haoran Zhang, Zhichao Ye, Haomin Liu, Guofeng Zhang, Ian Reid, Xingxing Zuo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an HOI-aware exocentric-to-egocentric video generation framework with a unified 4D HOI prior and decomposed gated cross-attention that improves object consistency and hand-object interaction preservation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38615)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiajun Liu, Yifan Chen, Yichao Liu, Jiayi Zhang, Ruoqu Chen, Shaoxuan Xie, Guocai Yao, Mengdi Xu, Sen Cui, Changshui Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses an action-conditioned world model (COACHWORLD) to imagine failures and actively select demonstrations for compositional robot skill improvement, demonstrating world models as coaches for modular policy learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39685)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Zijie Zhao, Shengqian Chen, Xiaoxu Wang, Han Jiang, Yuanheng Zhu, Dongbin Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Action-conditioned world model predicts future physical states to drive preactive residual action corrections for high-precision locomotion, a concrete world-model-guided control insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39179)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Kowndinya Boyalakuntla, Yuhan Liu, Abdeslam Boularias

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Closes the planning-learning loop for learned world models via hybrid multi-step TD targets, disagreement-aware terminal values, and return-weighted actor distillation, improving high-dimensional control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39751)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: F. Olivia Fan, Oliver Obst

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that a diagonal linear recurrent memory suffices to distil a DreamerV3 world-model policy for memory-dependent robot air-hockey control, offering a broadly useful insight about minimal recurrent dynamics in learned world-model policies.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39151)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yunhan Wang, Haodong Wang, Zhiming Liu, Zicong Hong, Qianli Liu, Xiaoyi Pang, Yangjia Hu, Quanxin Shou, Yikun Miao, Song Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes action-guided 4-bit quantization for world-action models that steers numerical error toward computations with less influence on final actions, enabling efficient denoising rollouts with minimal control degradation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39056)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Duowen Chen, Jinjin He, Gouthaman KV, Sandeep Bangalore Venkatesh, Bo Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds spatially anchored, listener-dependent sound to generated 3D worlds, extending world models to persistent multimodal (audio-visual) environment state.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38444)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuhan Guo, Jinming Liu, Liang Xu, Ziqiang Li, Jianguo Huang, Zhicheng Wang, Hu Zhu, Qiuyu Chen, Yuntao Wei, Xin Jin, Wenjun Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Elicits internalized world knowledge in LLM agents via goal-diverse action ranking at fixed states, improving transferable decision-making without explicit future-observation prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38334)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hanmo Chen, Chengcheng Liu, Tianxiao Chen, Zheyu Zhang, Siming Zheng, Jinwei Chen, Xu Yang, Cheng Deng, Bo Li, Peng-tao Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Binds visual source motion to stereo audio via motion tracks and residual track RoPE, improving dynamic spatial correspondence in joint video-audio generation with a new dataset and benchmark.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38748)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Donghao Zhou, Haoyang He, Fan Zhang, Hao Yang, Guisheng Liu, Xin Gao, Zhongwei Wan, Xingyuan Bu, Jie Wang, Qiangpeng Yang, Shilei Wen, Chi-Wing Fu, Pheng-Ann Heng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Activates MLLM reasoning as refined conditioning for instruction-guided video editing, improving controllability on implicit and causally demanding edits via curriculum training and inference-time thinking scaling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38541)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Wenhao Li, Xiu Su, Yu Han, Yichao Cao, Shan You, Chang Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Dual-stream VLA with optical-flow motion perception and future-state awareness for latency-compensated, closed-loop dynamic manipulation, relevant to action-conditioned world modeling and foresighted planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39198)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Songhe Wang, Lifu Wei, Shuolin Xu, Charles A. Kamhoua, David Miller

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free triple-flow framework that couples residual erasure with native synthesis to reconstruct occluded backgrounds, improving spatiotemporal consistency in video object removal.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39157)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Mayalen Etcheverry, Pietro Miotti, Aidan Sirbu, Konstantin Sch\"urholt, Mariia Drozdova, Arna Ghosh, Blaise Ag\"uera y Arcas, James Manyika, Blake Richards, Eyvind Niklasson

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Neural cellular automata with strictly local asynchronous updates produce spatio-temporal dynamics that generalize to larger grids and longer rollouts, offering a decentralized alternative for learned visual dynamics and reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.36126)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Zhihang Wu, Zhongqi Wang, Jie Zhang, Fengming Gu, Shiguang Shan, Xilin Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: First systematic backdoor study on interactive video generation, showing action-guided triggers can freeze future frames and break action controllability, an insight relevant to controllable video world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39047)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Ivan Martinovi\'c, Lukas Knobel, Yuki M. Asano

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies self-supervised pretraining on continuous video streams and proposes StreamMAE with stream-aware regularization and motion-biased crops, offering transferable insight for video representation learning relevant to world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.40333)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Hongbo Zhang, Liuyang Song, Quanquan Li, Daqian Yang, Yan Wen, Zhengtao Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Defines an action-conditioned bisimulation merge rule over an empirical predictive state graph for GUI agent memory, providing a dynamics-based state abstraction insight relevant to world-model state representation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38778)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Can Zhang, Xiaotian Han, Junyuan Shang, Yuchen Ding, Zhenyu Zhang, Shuohuan Wang, Dianhai Yu, Ruirui Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a stateful codec representation where predictive frames update a carried latent state, improving temporal reasoning and order sensitivity in video-language models with a recurrence idea relevant to video dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39563)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Zhihao Sun, Liu Liu, Xinjiang Wang, Haoyi Jiang, Wei Feng, Huiqiang Zhang, Xiaosong Jia, Zhizhong Su, Zuxuan Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematic study within a unified world-action model showing that human-robot alignment, task diversity, and video-only supervision shape downstream robot gains, with implications for learning dynamics from egocentric video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.40341)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Junyao Gao, Sibo Liu, Weidong Zhang, Cairong Zhao, Jun Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds SMPL-X-derived 3D mesh guidance and audio/face cross-attention to a video diffusion backbone for controllable talking-avatar generation with body and head motion control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39273)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Max Ku, Jiaojiao Fan, Zekun Hao, Francesco Ferroni, Heng Wang, Wenhu Chen, Ming-Yu Liu, Prithvijit Chattopadhyay

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a lightweight physical-consistency evaluator for generated videos trained with a unified ranking/regression/calibration objective, offering a reusable signal for improving physical plausibility in video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38377)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Wei Xue, Keliang Liu, Mingzhang Cui, Jinhua Xie, Jinjie Wei, Jianan Hou, Jingcheng Lu, Lintao Wang, Kaixiang Qiu, Yizhou Liu, Xinghai Ye, Jinghang Han, Mingcheng Li, Jie Gu, Shunli Wang, Lihua Zhang, Dingkang Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Mixed-stream world-action model with shared backbone and manipulation anchor pose supervision for unified mobile manipulation, offering a modest world-model-flavored policy learning idea.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39388)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Yansong Shi, Jiange Yang, Xijie Yang, Shaowei Zhang, Yuhan Zhu, Tao Lu, Limin Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark and memory-augmentation framework for partially observable robotic manipulation that highlights the need for internal representations of hidden task states, indirectly relevant to world-model memory and state abstraction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38886)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Haoran Xu, Xingzhuo Guo, Yuchen Zhang, Jincheng Zhong, Jianmin Wang, Mingsheng Long

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows a standard Diffusion Transformer with a dynamics-aware noise prior and timestep-aware RL rewards improves spatiotemporal precipitation nowcasting, a domain-specific but transferable video-prediction insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.37038)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Yizhao Li, Pusen Gao, Ming Wang, Shaojie Shen, Shuo Yang, Hao Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates full-body co-speech humanoid motion via a speech-grounded diffusion transformer with rectified flow matching, offering a narrow but plausible motion-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39575)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Shu Yu, Chaochao Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents an RL fine-tuning method for diffusion models with causal scene graph rewards and spatially grounded advantages; image-only but the compositional/spatial grounding ideas may transfer to video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39441)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yulong Liu, Xiaotian Han, Junyuan Shang, Yuchen Ding, Zhenyu Zhang, Shuohuan Wang, Guibo Zhu, Sirui Han, Dianhai Yu

**机构**: Baidu (ERNIE Research)

**💡 亮点 (Highlight)**: Codec-native vision encoder with native token compression for long-video understanding; relevant mainly as an efficient video representation rather than a generative or dynamics contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39924)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Luca Bricarello, Jo\~ao Carlos Virgolino Soares, Alberto Sanchez-Delgado, Fulvio Mastrogiovanni, Claudio Semini

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns pre-contact terrain-interaction dynamics from locomotion experience with uncertainty-aware continual learning, a narrow but genuine learned-dynamics model for embodied prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39755)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Shuang Liang, Lejun Liao, Shiyuan Zhang, Max C. Zhang, Xiaolong Luo, Han Wang, Stefano Anzellotti, Yuan Yuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns salient factors in a frozen autoencoder latent to condition a diffusion transformer, offering a transferable representation-conditioning idea though demonstrated only on images rather than video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39635)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Linrui Qian, Jiajia Zhang, Gan He, Bohan Sun, Zhiwei Lin, Qianhao Wang, Zewu Cai, Nianyu Yi, Mengdi Zhao, Kai Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Embeds a biophysically detailed C. elegans circuit as a fixed dynamical core for visuomotor policies, providing a dynamics-core insight for robust embodied control but no learned world model or video generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39322)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Hung-Jen Chen, Yu-Hsun Hou, Yan-Hong Chen, Yan-Fu Chen, Binghua Cai, Min Sun, Chun-Yi Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses instruction-action binding failures in VLA policies and proposes Equivariant Counterfactual Training, a weakly related embodied-control insight with only indirect connection to learned dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39971)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Galbot Team, Xuchuan Chen, Xiaoqian Cheng, Yu Deng, Lihe Ding, Shaocong Dong, Xiangjun Gao, Haozhe Jia, Zekai Li, Zhoujian Li, Yunrui Lian, Sikai Liang, Chenghuai Lin, Dairu Liu, Jiahang Liu, Qingtao Liu, Yuxuan Ma, Zekun Qi, Jiayi Su, He Wang, Ruochen Xu, Tianyu Xu, Xudong Xu, Zhe Xu, Mi Yan, Siming Yan, Li Yi, Ruixi Yu, Jinlu Zhang, Yintianrun Zhang, Zhikai Zhang, Zhizheng Zhang, Yixin Zheng, Weiyi Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Evaluates a frontier multimodal model as an embodied policy across manipulation, navigation, and locomotion, offering empirical insight into the gap between high-level task decisions and reliable physical control relevant to embodied world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38537)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu, Tommi Jaakkola, Yang Zhang, Shiyu Chang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents an interactive 3D world auditing benchmark probing how multimodal agents couple action and visual reasoning for anomaly detection, providing a testbed relevant to interactive world-model evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.40325)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Ruiqi Li, Xuanyi Liu, Sijia Li, Haofeng Wang, Yuxin Liu, Feng Xie, Songchao Tan, Shiqi Wang, Hanwei Zhu, Yizong Wang, Chuanmin Jia, Siwei Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark revealing that image-to-video models fail to align behavior with latent mental states, exposing an omniscient bias relevant to world-model reasoning in video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39147)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Shaohong Zhong, Marco Pontin, Joe Watson, Perla Maiolino, Ingmar Posner

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unifies MPM dynamics with 3D Gaussian splatting for soft-robot and tactile simulation, providing a differentiable-ish dynamics-plus-rendering simulator relevant to learned dynamics and embodied world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38418)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zaijing Li, Rui Shao, Bing Hu, Haoyu Zhang, Dongmei Jiang, Liqiang Nie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a memory-centric VLA framework with query-skill memory banks for data-efficient adaptation, offering a memory/state-abstraction mechanism relevant to embodied world-model-style skill reuse.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39794)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Kowndinya Boyalakuntla, Ajinkya Pawar, Abdeslam Boularias, Jingjin Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a digital-twin nominal rollout with a recurrent plan-conditioned student to correct deviations under self-occlusion, contributing a predictive-rollout-plus-correction scheme relevant to learned dynamics for manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38857)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Heejae Suh, Jongwook Han, Zahra Gholami, Yohan Jo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes physical failure modes of VLA policies under camera blackout/freezing and tests mitigations, offering embodied-robustness insight adjacent to world-model-based control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39145)

---

## 47. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Amir-Hossein Shahidzadeh, Seungjae Lee, Eadom Dessalene, Shanthosh Raaj Mohanram Mageswari, Soroush Etemad, Furong Huang, Cornelia Ferm\"uller, Yiannis Aloimonos

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a skill-conditioned visuotactile representation with sparse event memory that improves contact-rich manipulation progress estimation, offering a weakly related insight into temporal memory for embodied dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38494)

---

## 48. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Hyunjoon Lee, Haebeom Jung, Eunsung Cha, Daeun Lee, Yu-Chiang Frank Wang, Jaesung Choe, Jaesik Park

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses event history priors plus current geometry for active view selection in event-referential grasping, a weakly related embodied memory/occlusion-reasoning system without a learned dynamics or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39375)

---

## 49. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Di Wu, Rongtian Shen, Ping Liu, Yan Shen, Zhenhan Yin, Shun Zuo, Xuhua Chen, He Zheng, Lingfeng Zhang, Jianglin Zhang, Tao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Stage-aware two-step flow denoising for VLA inference could transfer to faster action-conditioned video/world-model generation, though the paper targets robot execution latency rather than visual dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.39822)

---

## 50. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jiaheng Hu, Roberto Martin-Martin, Peter Stone, Rocky Duan, Zhenyu Jiang, Guanya Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses simulation as a corrective laboratory for coding agents to acquire robot skills, offering a weakly related sim-to-real dynamics insight but no learned visual world model or video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.38982)

---

