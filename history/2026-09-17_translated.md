# 💡 今日研究速览 (Daily Summary)

### World Models & Learned Dynamics

A clear theme across today's submissions is the maturation of *world-action models* (WAMs) from single-domain curiosity into a general-purpose substrate for embodied control. The strongest work pushes toward physics-grounded, interactive, and long-horizon fidelity: **PhysStream**enables mid-generation manipulation of rigid-body dynamics through structured scene memory and sparse velocity-increment control, while**WholeBodyWAM** generalizes pre-trained world-action priors to humanoid loco-manipulation by jointly predicting visual dynamics, actions, and whole-body control intents. A parallel thread concerns *where action representations come from*: **GeoLAM**learns geometry-grounded latent actions from unlabeled human video via a 4D geometry teacher, and**ProxiDex**couples forward and inverse proximity dynamics to stabilize dexterous manipulation. Perhaps the most conceptually important contribution is**World Model Science**, which reframes long-horizon LLM agent reliability through the lens of self-organized criticality and metastable belief dynamics—diagnosing error avalanches and stress accumulation at the trajectory level rather than treating them as isolated failures. Complementing this,**Stable by Construction** introduces variational latent Markov operators that stabilize long-horizon autoregressive PDE rollouts, an insight that transfers directly to any learned dynamics model suffering from compounding error. Together, these papers suggest the field is converging on a shared agenda: grounding latent dynamics in geometry and physics, controlling them interactively, and rigorously characterizing their failure modes over long horizons.

### Robotics, VLA & Embodied Manipulation

Today's embodied-intelligence papers show a pronounced shift toward *spatially-grounded, demonstration-driven* policies that unify perception, language, and action. **sensVLA**exemplifies this with a VLA architecture for autonomous wheel loaders that routes BEV lidar features to a flow-matching action expert—an unusually concrete industrial instantiation. On the manipulation side,**UniDex-ViTac**and**Weave**both leverage human video or human-object interaction data, driving simulation and contact-aware retargeting respectively to learn dexterous and whole-body loco-manipulation policies.**Seeing What Matters**takes a notably different route, using a generative video model as a navigation planner augmented with BEV visual cues and an inverse-dynamics model to ground predicted video flow into embodiment-specific actions—a clean bridge between the video-generation and robotics communities.**EgoPathBench**and**MEgoVista**provide the evaluation and supervision infrastructure this ecosystem needs: the former probes zero-shot egocentric waypoint decision-making in VLMs, the latter reconstructs metric 4D hand and head motion from egocentric video with motion-capture-validated accuracy. Finally,**FluxVLA Engine** addresses a growing pain point by standardizing interfaces across VLA, world-action models, and embodied policy training—infrastructure that, while not a methodological advance, may materially accelerate reproducibility in the subfield.

### Video Generation, Editing & Neural Codecs

Work on controllable and temporally coherent video continues to diversify along two axes: *interactive control* and *robust streaming*. **MDN-Control**offers a training-free multi-subject editing framework that combines mask localization, depth-aware occlusion control, and noise latent prompting to reduce attribute leakage—an increasingly important capability as generative video moves toward practical editing workflows. On the representation side,**DecoGS**adaptively decouples static and dynamic 3D Gaussians for free-viewpoint video streaming, improving temporal coherence and reducing flicker; the decoupling principle here is likely transferable to temporally consistent dynamic scene generation more broadly.**Semantic-Aware Neural Video Codec**partitions latent representations by importance for error-resilient low-latency transmission, a representation-prioritization idea with clear relevance to robust generation pipelines under bandwidth or channel constraints.**OmniHarness**sits at the periphery of this cluster, applying symbolic policy learning to generalizable visual generation; its compositional policy reuse is suggestive for controllable generative pipelines, though the connection to video dynamics is currently weak.

### Scientific & Domain-Specific Dynamics

A smaller but distinctive set of papers applies learned-dynamics machinery to scientific and industrial domains.**High-Fidelity Digital Twin Data Models**combines randomized dynamic mode decomposition with deep learning to build reduced-complexity surrogates that reproduce complex fluid dynamics—a transferable latent-dynamics approach for learned environment evolution.**Schema-Adaptive Action-Conditioned JEPA**studies cross-machine CNC dynamics transfer under partial sensor overlap, offering rare insight into industrial world-model transfer and, importantly, how to evaluate it. In the medical domain,**MUMINS**performs metadata-conditioned uncertainty-aware next-state synthesis to forecast anatomical evolution in a single diffusion pass with an uncertainty map—narrow in scope but methodologically aligned with the broader learned-dynamics agenda.**Driver Behavior Estimation** rounds out this cluster with a physics-constrained, decision-conditioned autoregressive transformer for predicting human longitudinal driving trajectories, a plausible if specialized contribution to behavior modeling. Collectively, these papers illustrate that the world-model toolkit is diffusing well beyond robotics and video into fluid dynamics, manufacturing, medicine, and transportation—domains where long-horizon stability and uncertainty quantification matter as much as raw predictive accuracy.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chuhao Chen, Peter Wonka, Chaoyang Wang, Chen Wang, Qiao Feng, Sergey Tulyakov, Lingjie Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Autoregressive physics-grounded image-to-video model with structured scene memory and sparse velocity-increment control enabling interactive mid-generation manipulation of rigid-body dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17521)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yifan Xie, Hekun Tian, Jinkun Liu, YuAn Wang, Qiao Sun, Wenbo Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns geometry-grounded latent actions from unlabeled human videos via a 4D geometry teacher and future-frame reconstruction, yielding transferable action representations for world-action models and robotic manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17099)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhuo Li, Yiming Yao, Jim Tan, Mengjie Jing, Zhipeng Dong, Fei Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends pre-trained world-action models to humanoid whole-body loco-manipulation by jointly predicting visual dynamics, actions, and whole-body control intents with structured WBC grounding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16644)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hojin Lee, Sizhe Lester Li, Maximilian Hilger, Susie Lu, Achim J. Lilienthal, Vincent Sitzmann, Daniel A. Duecker

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a generative video model as a navigation planner, adding BEV visual cues for global task context and an inverse-dynamics model to ground predicted video flow into embodiment-specific robot actions.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16737)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junyi Liao, Johann Guilleminot, Vahid Tarokh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces variational latent Markov operators with structured Gaussian perturbations and neural-operator transitions to stabilize long-horizon autoregressive PDE rollouts, a broadly useful insight for learned dynamics and error accumulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16621)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Xinyuan Song, Zekun Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trajectory-level dynamical diagnostics of LLM agent belief states provide conceptual insight into long-horizon world-model fidelity, stress accumulation, and error avalanches.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17419)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yushan Bai, Boyu Zheng, Zhiyang Mao, Hongzheng Sun, Yuchuang Tong, En Li, Zhengtao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns action-conditioned proximity dynamics with a coupled forward-inverse design, predicting future observation latents and decoding proximity changes to stabilize dexterous manipulation policies.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16586)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adaptive static-dynamic decoupling of 3D Gaussians for streaming free-viewpoint video improves temporal coherence and reduces flicker, offering transferable insights for temporally consistent dynamic scene generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17230)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Anna Oliveras, Roger Mar\'i, Rafael Redondo, Oriol Guardi\`a, Cynthia Ifeyinwa Ugwu, Ana Tost, Bhalaji Nagarajan, Carolina Migliorelli, Vicent Ribas, Petia Radeva

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Metadata-conditioned uncertainty-aware next-state synthesis forecasts anatomical evolution with a single-pass diffusion and uncertainty map, a narrow but relevant learned-dynamics contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17169)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Jiayi Yu, Xi Ye, Lina Wang, Yunkun Xia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free multi-subject video editing framework combining mask localization, depth-aware occlusion control, and noise latent prompting to reduce attribute leakage and improve temporal consistency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16475)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Ayoub Louaye Bouaziz, Matthieu Ostertag, Anton Demasles

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies schema-adaptive action-conditioned JEPA for cross-machine CNC dynamics transfer under partial sensor overlap, providing insight into industrial world-model transfer and evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16071)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Diana A. Bistrian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Combines randomized dynamic mode decomposition with deep learning to build reduced-complexity digital twin models that reproduce complex fluid dynamics, offering a transferable latent-dynamics surrogate relevant to learned environment evolution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17101)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Xu Xu (Beihang University), Jinxiu Liu (The Chinese University of Hong Kong), Zhangbo Qiao (Beihang University), Jiaxing Lu (Beihang University), Xiangyu Zhang (Beihang University), Yubin Gu (National University of Singapore), Fangwei Ning (Beihang University), Yan Shi (Beihang University)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Symbolic policy learning for generalizable visual generation is only weakly tied to video or world-model dynamics, but its compositional policy reuse could inform controllable generative pipelines.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16057)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Matin Mortaheb, Homa Esfahanizadeh, Jinfeng Du, Harish Viswanathan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Semantic-aware neural video codec that partitions latent representations by importance for error-resilient low-latency transmission, offering a transferable representation-prioritization idea for robust video generation pipelines.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16279)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Gopi Krishna Erabati, Bjarne Johannsen, Angus Stewart, Vardeep Singh Sandhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: VLA architecture for autonomous wheel loaders that routes BEV lidar features to a flow-matching action expert, offering spatially-grounded control relevant to embodied dynamics modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17021)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Mohammad Khoshkdahan, Pavel Laskov, Alexey Vinel

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decision-conditioned autoregressive transformer with physics constraints predicts human longitudinal driving trajectories, a narrow but plausible learned-dynamics contribution for behavior modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16058)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Hyesung Lee, Si-Hwan Heo, Sungwook Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses human video to drive simulation and learn a visuo-tactile dexterous manipulation policy, a weakly related embodied-dynamics contribution that leverages video demonstrations rather than advancing video generation or world modeling directly.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16504)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Liu Cao, Xingze Wu, Jingzhi Cui, Botian Xu, Mingzhi Pei, Ruoqu Chen, Mengdi Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns whole-body humanoid loco-manipulation from human-object interaction demonstrations with contact-aware retargeting, marginally relevant as embodied dynamics learning but not a world-model or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16683)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jiangong Xiao (Northwestern Polytechnical University), Zhihao Zhang (Xi'an Jiaotong University), Yifei Dong (Maniformer), Chao Ma (Maniformer), Zhouyi Jin (Maniformer), Zhiwen Hou (Maniformer), Li Liu (Maniformer), Weihuang Chen (Xi'an Jiaotong University), Hongbin Sun (Xi'an Jiaotong University), Maoqing Yao (Maniformer)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reconstructs metric 4D hand and head motion from egocentric video with calibrated stereo scale, providing motion-capture-validated supervision that could support dynamics learning but is primarily a reconstruction pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16684)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Yang Zhao, Zhuo Chen, Xubo Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Egocentric waypoint decision-making benchmark and training resource probing spatial and action-consequence reasoning in VLMs, weakly relevant to embodied world-model evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.16610)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Yinhao Li, Weixin Mao, Zihan Lan, Jikun Rong, Qirui Hu, Yiming Zhang, Weipeng Deng, Bowen Shen, Minzhao Zhu, Yiming Mao, Yan Yang, Chenguang Cui, Hongyuan Chen, Xu Huang, Zheyi Zhao, Pinxi Shen, Bozhen He, Zhen Fu, Yifan Wang, Zexin Zhang, Ang Gao, Haoyu Chen, Chengqi Shi, Hua Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Engineering platform standardizing interfaces for VLA, world-action models, and embodied policy training/deployment, offering infrastructure rather than a new world-model or video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.17210)

---

