# 💡 今日研究速览 (Daily Summary)

### World Models for Video Generation and Prediction

Today's papers reveal a decisive shift toward **internalizing world-model capabilities directly into generative architectures**rather than treating them as external modules. The dominant theme is the unification of memory, action, and physical reasoning within a single latent space: rather than retrieving from external buffers or post-hoc simulators, models like the camera-conditioned retrieval gate in video world models and the reconstruction-free JEPA formulation (which provably disentangles invariant from variant dynamics) bake persistent state and identifiability into the representation itself. A second major thrust is**action-faithfulness and embodiment**: multi-view cross-embodiment models with counterfactual post-training, joint state-action generation for humanoids, and latent action spaces that scale positively across pretraining embodiments all point toward world models that are not merely predictive but *controllable* and physically grounded. Third, we see the emergence of **closed-loop procedural execution and planning-oriented foresight**—goal-directed video generation framed as task execution, planning-shaped latent representations for autonomous driving, and intent-conditioned 3D world evolution—signaling that the field is moving from passive video synthesis toward interactive, decision-coupled world simulation. Notably, several works (e.g., WOVEN, SplitJEPA, cross-embodiment latent actions) frame their contributions as *reusable training primitives or representation insights*, suggesting the community is converging on shared abstractions for visual world modeling rather than isolated architectures.

### Efficient World-Action Models and Inference Optimization

A focused cluster of work addresses the **inference cost of world-action models**, which is emerging as a critical bottleneck as these systems scale. The central insight is that world models exhibit substantial redundancy across timesteps and candidate trajectories: staleness-bounded KV reuse exploits action-expert cross-attention to selectively refresh tokens, latent navigation models share visual encoding across candidate futures, and streaming-aware diffusion with cross-step attention couples scheduling to trajectory. Together these methods demonstrate that**training-free or minimally invasive efficiency gains**are achievable without sacrificing closed-loop control fidelity—an important practical signal as world-action models move toward real-time robotic deployment. The convergence on attention-reuse and cross-step coupling suggests a maturing understanding of where temporal redundancy lives in these architectures.

### Multimodal LLMs and Visual Reasoning

The integration of world modeling into MLLMs is proceeding through**structured supervision recipes rather than architectural overhaul**. The most notable development is the treatment of visual transition reasoning as a reusable training primitive, organized by reasoning operation and validated across a broad benchmark suite—a sign that the community is beginning to systematize *what* world-modeling capabilities MLLMs should acquire, not just *that* they should acquire them. This complements the broader trend of using pretrained prediction-oriented latent spaces to condition downstream generation, indicating that MLLMs and world models are converging on shared representational substrates.

### Video Editing, Generation, and Streaming

Video generation research today is characterized by **transfer and control rather than from-scratch synthesis**. In-context visual demonstrations transfer image editing to video without paired data; expression-diverse reference galleries improve identity preservation under expressive motion; and acausal noise shaping enables single-pass real-time talking heads by eliminating distillation entirely. On the streaming front, the reconnection of cross-chunk gradients via shortcut gradient replay addresses the fundamental tension between autoregressive locality and long-horizon coherence. The through-line is**controllability under real-time constraints**: methods increasingly target drift-free, low-latency generation with fine-grained spatial and temporal control, often by repurposing pretrained image or video priors rather than training new generative stacks.

### Physical Dynamics, Simulation, and Contact Reasoning

A distinct thread advances**physics-grounded dynamics modeling** through local and phase-aware representations. Sparse local contact-surface reasoning for rigid-body interactions, phase-aware dual-branch generators for coupled solid-gas dynamics, and egocentric contact-force estimation all share a commitment to modeling *interaction structure* rather than holistic scene appearance. The frequency-guided and canonical-consistent optimization for head avatars, while application-specific, reinforces this theme of decomposing dynamics into structured components. These works collectively suggest that physical plausibility in generative video will increasingly depend on **explicit contact and phase representations**rather than implicit scaling alone.

### Benchmarks, Diagnostics, and Identifiability

Finally, the field is investing in**rigorous diagnostics and identifiability analysis**. The multi-view shared-world benchmark exposes a critical failure mode—independently controlled views fail to maintain shared-state persistence—that strikes at the heart of interactive world modeling. Identifiability-driven experimental agents introduce a three-way plateau verdict distinguishing capability limits from fundamentally non-identifiable dynamics, a methodological contribution with broad implications. Memorization analysis via diffusion energy-landscape basin geometry offers a complementary lens on data curation and training dynamics. Together, these papers signal a maturing field that is increasingly asking *whether* world models actually capture shared, identifiable structure—not merely whether they generate plausible outputs. The emergence of such diagnostics alongside capability papers is a healthy sign that the community is building the evaluative infrastructure needed to distinguish genuine world understanding from sophisticated pattern matching.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: JiaKui Hu, Tailai Chen, Yuqi Pan, Xuerui Qiu, Jialun Liu, Xiao Cao, Zhenxin Zhu, Guang Chen, Hangjun Ye, Bing Wang, Yanye Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Internalizes memory retrieval into a video world model's persistent state with a camera-conditioned retrieval gate and 3D re-visibility trigger, improving long-horizon scene consistency without external memory.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11444)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates multi-agent egocentric world modeling with synchronized ego-stream generation and fine-grained embodied interaction, improving cross-view and shared-environment consistency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12299)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates procedural video generation as closed-loop task execution in visual world space, jointly training a planner and executor with hierarchical visual memory and a 59K step-annotated benchmark.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12459)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang

**机构**: BRAVE Group / AgiBot (project page brave-eai.github.io)

**💡 亮点 (Highlight)**: Multi-view cross-embodiment robot world model with image-space action rendering, offline geometric calibration, and counterfactual post-training guided by an embodied video reward model for action-faithful, physically plausible video prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12468)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ruijin Hua, Zichuan Liu, Zhuokai Zhao, Yujia Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reconstruction-free JEPA that provably identifies invariant and variant latent subspaces of predictive dynamics, a broadly useful world-model representation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12349)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Establishes visual transition reasoning as a reusable training primitive for world modeling in MLLMs, with a supervision recipe organized by reasoning operation and validated transfer across 26 benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12417)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Prince Jha, Nils Lukas, Kun Zhang, Salem Lahlou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a controllability- and reward-relevance-factored latent representation for a pretrained video world model, improving planning and generalization to manipulated variants.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12016)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu Liu, Hetian Guo, Tianlv Huang, Ziyi Cai, Wudi Chen, Hantang Wang, Qiutong Liu, Yingzhi Peng, Wei Han, Peijun Tang, Jianan Wang, Zipei Fan, Zhiyuan Zha, Xuan Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Predicts task-relevant future states in a pretrained prediction-oriented latent space to condition VLA action generation, yielding a lightweight latent world model with parallel future prediction and low inference latency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12285)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a lifting-free learned view synthesizer that supplies structural conditions to a video diffusion model for exocentric-to-egocentric generation, with a confidence-guided denoising scheme.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12442)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Dongbin Zhang, Chaoda Zheng, Kangjie Chen, Xiangyu Li, Shijia Chen, Jinhao Deng, Yuqi Zhang, Guangfeng Jiang, Hongbin Lin, Choo Sin Wai, Minqi Wang, Puyi Wang, Jingye Zhang, Yu Zhang, Xianming Liu, Boyang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reconnects cross-chunk gradients in autoregressive video generation via shortcut gradient replay, improving long-horizon visual quality and temporal consistency without changing inference.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12156)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Turns static 3D Gaussian Splatting scenes into seamlessly looping 3D cinemagraphs via a Fourier-series periodic deformation field and a grounded drift field that absorbs cross-view inconsistency from imperfect video-model supervision.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12461)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jinchang Xu, Hongda Yu, Fengwei Dong, Wenhui Huang, Xi Wei, Yongzhi Liu, Sunan Zhang, Jirao Wang, Chen Lv, Bingbing Li, Guodong Yin, Weichao Zhuang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shapes a latent world model's future representation with trajectory-planning objectives and distills it into a history-only prior, yielding planning-oriented foresight for end-to-end driving.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11382)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ruixiang Ouyang, Guanren Qiao, Fansen Meng, Yueci Deng, Ruixing Jin, Kui Jia, Guiliang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Models rigid-body dynamics through sparse local contact-surface neighborhoods, improving long-horizon position/orientation accuracy and contact fidelity for predictive physical world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12333)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Linkai Liu, Yuntian Zhang, Zhenshan Bing, Chen Chen, Lingjuan Lyu, Shangguang Wang, Mengwei Xu, Dongqi Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Latent navigation world model that shares visual encoding across candidate trajectories and jointly predicts action-conditioned future representations at multiple horizons, enabling fast future-aware closed-loop planning on a real robot.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12368)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jingfeng Ou, Kun Wang, Rui Zhao, Jingwei Guan, Limin Wang, Chao Dong, Xingyu Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Phase-aware dual-branch video generator with spatiotemporal cross-attention that improves physical plausibility and motion adherence for coupled solid-gas dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11791)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kai Ding, Yang He, Ruijie Quan, Yi Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free KV reuse for world action models that selects refresh tokens via action-expert cross-attention plus latent surprise, cutting video DiT prefill FLOPs while preserving closed-loop control accuracy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11401)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yan Yang, Jikun Rong, Minzhao Zhu, Zheyi Zhao, Qirui Hu, Zihan Lan, Weixin Mao, Yinhao Li, Zhen Fu, Hua Chen

**机构**: LimX Dynamics

**💡 亮点 (Highlight)**: Humanoid world action model that jointly generates reference actions and post-execution proprioceptive states, closing the action-execution gap for more accurate future visual prediction and manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12026)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junpeng Yue, Boyuan Li, Yuxuan Wang, Zepeng Wang, Yuhui Fu, Feiyang Xie, Yu Zhang, Jing Zhang, Xianqi Zhang, Weibo Li, Xiaofei Zheng, Yuming Fang, Jiangxing Wang, Zongqing Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Latent world-action model pretrained on mixed-modality human video and motion data jointly predicts future latent visual states and motion to ground humanoid loco-manipulation control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11283)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Huang Huang, Sriram Yenamandra, Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan, Tsung-Yen Yang, Akshara Rai, Michael Rabbat, Li Fei-Fei, Jiajun Wu, Tingfan Wu, Franziska Meier

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified latent action space for cross-embodiment robot world models shows that shared latent actions scale positively with pretraining embodiments, a broadly useful world-model representation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10846)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Zhaoyang Liu, Kun Jiang, Ziying Song, Diange Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces action- and semantic-conditioned future 3D geometry prediction on a VGGT-based world model, enabling controllable action-dependent world evolution for driving.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11161)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Leigang Qu, Feng Cheng, Ziyan Yang, Bangbang Yang, Zhaoyang Huang, Wei Chow, Yicong Li, Wenjie Wang, Tat-Seng Chua, Yan Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Transfers image editing to video via in-context visual demonstrations and a shared spatial position encoding that propagates appearance edits across frames, improving controllable video generation without paired video-editing data.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12104)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Harris Partaourides, Sotirios Chatzis

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Streaming-aware diffusion with cross-step attention and trajectory-coupled scheduling enables real-time video super-resolution with improved temporal coherence at reduced complexity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11746)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Minye Wu, Zehao Wang, Tinne Tuytelaars

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unifies action generation and action-conditioned future-state prediction in one autoregressive spatial-language model over discrete coordinate and semantic tokens, with random-play transition pretraining.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12172)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Jiuming Liu, Jianing Li, Mengmeng Liu, Hongyang He, Hesheng Wang, Per Ola Kristensson

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Memory-buffer autoregressive scene flow forecasting with uncertainty-aware reweighting improves long-horizon 3D motion prediction, offering transferable insights for temporal dynamics modeling in world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10759)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Yu Han, Dejan Markovic, Alexander Richard, Wojciech Zielonka, Akshay Venkatesh, Cheng-hsin Wuu, Michael Zollhoefer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces acausal noise shaping for single-pass feed-forward talking-head generation, a broadly reusable insight for real-time, drift-free streaming video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11070)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Surya Shetty, Ulisses Braga-Neto

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifiability-driven LLM agent for closed-loop discovery of mechanistic world models, contributing a three-way plateau verdict that distinguishes capability limits from non-identifiable dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11253)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Joel-Pascal Ntwali N'konzi, Feliks N\"{u}ske, Stefan Klus

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Kernel-based Koopman embedding learning via bilevel optimization offers a data-driven dynamics model applicable to video and spatiotemporal forecasting, relevant to learned visual dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12370)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jing Xu, Cunjian Chen, Qiuhong Ke

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Chain-of-Dancers sequential decomposition enables scalable group dance generation with per-dancer identity preservation and spatial coordination, offering a transferable conditional video-generation strategy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11237)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yuqi Li, Xiaoqin Feng, Fan Xu, Weilun Feng, Chuanguang Yang, Yingli Tian, Hao Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Task-aware memory distillation organizes teacher knowledge into retrievable historical references to improve spatiotemporal video prediction and forecasting without extra inference cost.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11617)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Lipeng Zhuang, Yingdong Ru, Shiyu Fan, Edmond S. L. Ho, Gerardo Aragon Camarasa, Paul Henderson

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Masked generative transformer over discrete trajectory tokens with geometry-guided token search enables structural trajectory repair, a dynamics/planning-adjacent generative approach.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10646)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 7/10

**作者**: Nikhil Verma, Siddharthan Dileep, Anoop Singh, Srikanth Sastry, Ramya Hebbalaguppe, Sayan Ranu, N. M. Anoop Krishnan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reveals latent memorization encoded in diffusion energy-landscape basin geometry via cyclic denoising, an analysis insight that could inform video diffusion training and data curation but is not itself a video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11670)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Tianwen Fu, Wenbin Teng, Gonglin Chen, Junyi Ouyang, Haolin Xiong, Yajie Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves identity preservation in video generation under expressive motion via expression-diverse reference galleries and a data-curation pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11023)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yun-Wei Song, Jinkai Tao, Jun-Dong Zhang, Rui Zhang, Yi-Min Wu, Qiang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Self-evolving agent that revises physical mechanisms and equations from experimental discrepancies, offering a weakly related learned-dynamics modeling insight rather than a visual world model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11344)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Filip Grigorov, Kourosh Darvish, Nandita Vijaykumar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Addresses the privileged-state to RGB-D modality gap in robotic RL via KL-driven rollout regulation and representation alignment, a weakly related embodied-dynamics contribution without a generative world model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11119)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yuxin Chen, Senqiao Yang, Zixuan Wang, Jinhui Ye, Changsheng Lu, Pengguang Chen, Shu Liu, Zhuotao Tian, Jiaya Jia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a V-JEPA video encoder for disagreement-triggered recovery in robot policies, offering a weakly related learned visual-dynamics signal for corrective control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12185)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Zhuo Dong, Jianhua Yang, Haohao Li, Yumeng Zhao, Keji He, Yan Huang, Liang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Estimates contact force and mechanical work from egocentric video, providing physically grounded interaction cues that could inform dynamics-aware video models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11347)

---

## 37. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Bohan Zhou, Xingbei Chen, Emily Huang, Weilin Ruan, Haojian Huang, Yehang Zhang, Zexi Li, Wenqian Li, Qize Yu, Zetian Song, Leyi Wu, Jinghao Li, Mingxuan Song, Xinrun Xu, Zongyang Qiu, Yangkai Wei, Tianyi Zhang, Kaiwen Zhou, Yinchuan Li, James Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a state-conditioned coordinator from counterfactual branch outcomes for composing robot skills, offering a weakly related predictive-dynamics insight for embodied control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11480)

---

## 38. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

**机构**: Zhejiang University (ZJU-REAL)

**💡 亮点 (Highlight)**: Visual-native skill cards for VLM agents encode spatial/action-state structure visually, offering a weakly transferable representation insight for dynamics and embodied control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12403)

---

## 39. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jusuk Lee, Sungha Kim, Yeonsoo Park, Jonguk Cheon, Yoonkyo Jung, Yongjun You, H. Jin Kim, Jia-Bin Huang, Furong Huang, Youngseok Jang, Seungjae Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Abstracts a single human video into sequential scene graphs that guide RL reset sampling and dense rewards, a weakly relevant structured-dynamics representation for manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12470)

---

## 40. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Qirui Wu, Stan Birchfield, Hesam Rabeti, Angel X. Chang, Bowen Wen

**机构**: NVIDIA Research

**💡 亮点 (Highlight)**: Generative agentic 3D object reconstruction from casual images with an edit-render-review loop; only weakly connected to temporal dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11215)

---

## 41. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Zhangbo Xu, Ruoxi Zhang, Rui Hu, Yisong Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnostic benchmark revealing that independently controlled views in multiplayer world models fail to maintain shared-state persistence and structural consistency, highlighting a key limitation for interactive world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11723)

---

## 42. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Shikun Zhang, Yong Li, Yiqun Wang, Qiuhong Ke, Cunjian Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Frequency-guided curriculum and canonical cross-view consensus improve fine-grained head avatar reconstruction, offering only narrow, application-specific relevance to video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11412)

---

## 43. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zoe Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provenance-aware world state representation with deterministic replay for robots is a symbolic state-tracking framework rather than a learned dynamics model, giving only indirect world-model relevance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12033)

---

## 44. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Changchuan Yang, Haoxuan Xu, Wenbo Chen, Shuai Ren, Jianlong Zheng, Huarui Zhang, Tianfu Li, Guanzhong Tian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Encodes bounded history of states and actions into a latent temporal sequence to resolve phase ambiguity in embodied policies, a weakly transferable memory/state-abstraction idea for world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11168)

---

## 45. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Qixiang Chen, Cheng Zhang, Fucai Ke, Chi-Wing Fu, Jianfei Cai, Jingwen Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free view-planning framework for multi-view spatial reasoning that improves cross-view spatial understanding, weakly relevant to world-model spatial representations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.11810)

---

## 46. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Ting Mao, Yanming Shao, Ziheng Wang, Haoyu Liu, Yiqun Wang, Xuanye Wu, Yao Mu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Video-to-dexterous-hand interaction pipeline with physics-in-the-loop refinement; relevant to learning manipulation dynamics from monocular video but not a world model or video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.10855)

---

