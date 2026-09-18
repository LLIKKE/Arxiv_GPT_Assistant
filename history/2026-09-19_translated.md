# 💡 今日研究速览 (Daily Summary)

### World Models and Action-Conditioned Dynamics

The dominant theme across today's submissions is the maturation of *world-action models* (WAMs) — systems that jointly predict future scene dynamics and the actions that drive them. A clear architectural consensus is emerging around replacing expensive pixel-level video generation with compact, structured latent predictions: MoWAM substitutes explicit future motion for full video synthesis, JEPA-WAM grounds generated visual instructions in JEPA-encoded latent goal references, and LIFD maintains a persistent 3D-aware scene-token memory completed by rectified flow. Equally notable is the rapid infusion of *touch* into this paradigm — DexTouch-WM, Agile-WAM, and TacSushi all learn action-conditioned tactile world models, with Agile-WAM emphasizing multi-horizon asymmetric contact dynamics and TacSushi demonstrating human-to-robot transfer for dexterous tasks. What unifies these efforts is a shift from passive video prediction toward *interactive, intervention-aware* modeling: JEPA-Anything's orthogonal predictive factorization explicitly targets intervention prediction and out-of-distribution generalization across seven domains, while MM-Future co-evolves paired scene-action hypotheses for closed-loop driving. The field appears to be converging on the view that world models are only as useful as the action-conditioned counterfactuals they can generate.

### Efficiency, Quantization, and Deployment of Generative World Models

As video-generation-based world models grow more capable, a parallel line of work is confronting their practical deployment costs. Predict Before You Deploy offers a pragmatic contribution by predicting quantization-induced task degradation directly from offline action deviations, enabling practitioners to anticipate failure modes before committing to a compressed model. This complements the broader efficiency thrust seen in MoWAM and Agile-WAM, both of which explicitly optimize for low inference latency and efficient inference-time scaling. The emerging picture is that the community is no longer treating efficiency as an afterthought to capability — rather, the architecture choices themselves (motion prediction over video generation, latent rather than pixel-space rollouts, multi-horizon latent prediction) are being designed with deployability in mind. The next frontier will likely be standardized robustness metrics that couple compression decisions to downstream task performance, an area where today's work provides an early template.

### Object-Centric and Structured Representations for Dynamics

A third cluster of papers pushes toward *structured, object-centric* representations as an alternative to monolithic latent spaces. ParticleSplat learns self-supervised object-centric latent particle splatting with controllable scene editing, FAMOS performs feed-forward articulation modeling from sparse observations to recover joint dynamics, and SnapPhysics infers per-object physical properties — mass, friction, center of gravity — from a single image via a physics-aware scene graph. These contributions share the intuition that dynamics models generalize better when they operate over disentangled entities with explicit physical priors rather than entangled feature maps. This connects naturally to the persistent-memory concerns raised by LIFD and the JEPA factorization in JEPA-Anything: if a model can maintain stable object identities across time, it can reason about permanence, contact, and articulation more robustly. The convergence of object-centric perception with world-action modeling strikes me as one of the most promising under-explored intersections in today's batch.

### Embodied Perception, Benchmarks, and the Permanence Problem

Today's evaluation-focused work delivers a sobering corrective to world-model enthusiasm. "Can 4D Foundation Models Remember?" introduces PersistBench, revealing that 4D and video world models systematically lose object permanence, motion continuity, and appearance once objects exit the field of view — a fundamental failure that undermines long-horizon embodied reasoning. VABench similarly probes embodied spatial intelligence through active perception and metric control, testing observe-reason-act loops rather than raw generation quality. These benchmarks are valuable precisely because they target capabilities that current architectures implicitly assume but rarely verify. Supporting this thread, BinoGen scales egocentric binocular data with dense multimodal supervision, AnyViewDex achieves view-invariant dexterous manipulation via multi-view contrastive alignment, and ReShoot demonstrates generative visual domain randomization of recorded demonstrations. Together they suggest that the field's data and evaluation infrastructure is beginning to catch up to its modeling ambitions — though the permanence failures documented in PersistBench indicate that memory and persistence, not raw generative fidelity, may be the binding constraint on the next generation of embodied systems.

### Simulation, Control, and Cross-Embodiment Transfer

Finally, several papers address the pipeline from simulation to real-world control. REARL uses real-data clusters and an LLM to correct rollout distribution drift in closed-loop driving simulation — a transferable insight for keeping learned simulators aligned with real dynamics over long horizons. Improving Cross-embodiment Transfer in Latent Action Models introduces action-similarity supervision to better transfer latent dynamics learned from action-free video across embodiments, directly tackling a persistent bottleneck in robot learning. On the control side, Accelerating Visual Policy Learning couples sampling-based MPC with first-order policy gradients, while OmniMimic augments directionally limited animal motion via temporal reversal and constrained dynamics completion for multi-gait quadruped locomotion. TADreamer and PACE round out the batch by grounding video imagination into metrically consistent 3D waypoints and typed cinematic specifications respectively. The through-line here is *grounding*: whether through LLM-corrected simulation, action-similarity supervision, or metric calibration of imagined video, today's work consistently seeks to anchor generative and latent representations to physically executable control.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuai Liu, Hechangle Gong, Hao Jiang, Runlin He, Junxiang Zhan, Kai Huang, Sheng Yang, Shaoqing Ren

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a multi-mode joint world-action model that co-evolves paired scene-action hypotheses via a modality-aware diffusion Transformer for closed-loop driving rollout.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20377)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiayu Wang, Bin Zhu, Yue Yu, Jingjing Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replaces future video generation with explicit compact future motion prediction in a world-action model, retaining future dynamics for efficient inference-time scaling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20709)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yan Qin, Yue Chen, Wenwei Lin, Shujia Liu, Chuqiao Lyu, Kailun Su, Chenze Yu, Ping Luo, Wenbo Ding, Tianxing Chen, Renjing Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns an action-conditioned tactile world model from scalable human touch that jointly predicts future RGB and tactile dynamics, enabling human-to-robot transfer and surrogate policy evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20649)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Taoyong Cui, Zhongyao Wang, Xinyue Xu, Weiyang Liu, Zhaochen Yu, Yuying Zhang, Qiang Gao, Mengyue Yang, Wanli Ouyang, Pheng Ann Heng, Yingcheng Wu, Zhenfei Yin, Ling Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends JEPA world modeling with orthogonal predictive factorization of latent targets, yielding a domain-agnostic predictive framework that improves long-horizon dynamics, intervention prediction, and out-of-distribution generalization across seven domains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20800)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Caoliwen Wang, Mengdi Wang, Heng Zhang, Shixun Huang, Siyuan Chen, Chao Liu, Anpei Chen, Zhendong Wang, Peter Yichen Chen, Huamin Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Contact-centric world model for deformable-object manipulation that predicts dynamics at larger time steps than the source simulator, enabling 10x faster data generation and improved real-robot policy success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19600)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hanchu Zhou, Brendan Lynch, Raman Goyal, Dechen Gao, Begum Kasap, Boqi Zhao, Junshan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Tactile world action model with multi-horizon multimodal prediction that jointly generates action chunks and future visual/tactile latents, capturing asymmetric contact dynamics at low inference latency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20761)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tianbin Liu, Jian Zhu, Taiyi Su, Jianjun Zhang, Chong Ma, Zitai Huang, Yi Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments a video-generative World Action Model with JEPA-encoded visual goal references to improve instruction grounding and action-conditioned rollout.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20277)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Maxime Alvarez, Renzo Caballero, Tatsuya Matsushima, Yusuke Iwasawa, Yutaka Matsuo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces action-similarity supervision for latent action models, improving cross-embodiment transfer of learned latent dynamics from action-free video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19846)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Haodi Hu, Kaen Kogashi, Toshiaki Koike-Akino

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains a tactile-grounded world-action model with training-only future-consequence prediction and gated tactile fusion, improving dexterous manipulation success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19613)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Wenbo Li, Yiteng Chen, Wenhao Li, Qingyao Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a persistent 3D-aware scene-token memory completed by a rectified-flow generative model with anchor-guided cross-attention, offering a generative latent scene representation for partially observable manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19796)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Chiyoung Kim, Min Sung Choi, Jinho Ju, Chanhoe Gu, Donghwan Hwang, Wonseok Choi, Woongsun Jeon, Minhyeok Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses an edge-conditioned video generator to re-render recorded robot demonstrations under altered appearances, providing a video-generation-based data augmentation insight for visuomotor policy learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19661)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Lyuxing He, Daniel Guo, Elizabeth Terveen, Deepak Pathak, David Held, Tal Daniel

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Self-supervised object-centric latent particle splatting learns a 3D object-centric representation with controllable scene editing, relevant to object-centric dynamics representations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19463)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jiuyi Xu, Jinjia Guo, Meida Chen, Jing Du, Yangming Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Predicts quantization-induced task degradation for video-generation-based world action models from offline action deviations, giving a practical efficiency/robustness insight for deploying video world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19441)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Bing Duan, Qiang Guo, Linpu Li, Zhijian Mao, Min Zhu, Zhirui Ren, Yiwei Yan, Xi Chu, Xiaoding Li

**机构**: StudioPiLabs

**💡 亮点 (Highlight)**: Typed script-grounded specification and camera solver that compiles cinematic plans into diffusion prompts and 3D scenes, offering a controllability mechanism for spatial framing in generated video previsualization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19853)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xiangyu Li, Tiancheng Lai, Xijie Huang, Ruitian Pang, Siqi Shen, Juncheng Chen, Zaisheng Pan, Chao Xu, Fei Gao, Yanjun Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses generated video as an imagined navigation plan and calibrates it into metrically consistent 3D waypoints, showing how video imagination can be grounded for embodied control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19824)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Xiaojun Bi (Minzu University of China, Beijing, China), Jun Jiang (Minzu University of China, Beijing, China), Yiwen Sun (Peking University, Beijing, China, BIGAI, Beijing, China), Quanyi Ou (Minzu University of China, Beijing, China), Ke Cheng (Beihang University, Beijing, China), Mingjie Bi (BIGAI, Beijing, China), Yexin Li (BIGAI, Beijing, China)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Closed-loop traffic simulation that uses real-data clusters and an LLM to correct rollout distribution drift, offering a transferable insight for keeping learned environment simulators aligned with real dynamics over long horizons.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19903)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Chunpeng Li, Ya-tang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates large-scale embodiment-aware egocentric binocular video data with dense multimodal supervision, offering a dataset contribution relevant to embodied visual dynamics but without a new generative method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19881)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Kevin Qu, Tao Sun, Massimiliano Viola, Liyuan Zhu, Zhizhuo Zhou, Sayan Deb Sarkar, Konrad Schindler, Iro Armeni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Feed-forward articulation modeling from sparse observations learns object-centric motion and joint dynamics, offering a transferable representation for dynamics-aware world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20817)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Soham Patil, Om Sanjay Gunjal, Sourabh Bhosale, Arhan Chavare, Ramandeep Singh Hora, Spandan Roy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: View-invariant dexterous manipulation via multi-view contrastive alignment and privileged 3D geometric supervision, offering a weakly related representation-learning insight for embodied visual dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20107)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Guangzhao He, Hadar Averbuch-Elor, Wei-Chiu Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces PersistBench, a 360-degree-video-grounded benchmark and metric suite revealing that 4D/video world models lose object permanence, motion continuity, and appearance once objects leave the field of view.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20819)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Noura Fady, Farah Khaled, Catherine M. Elias

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates safety-critical driving scenarios via LLM-guided AR augmentation, offering a weakly related data-generation pipeline for testing learned driving dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20318)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Suji Kang, Seok-Young Kim, Young Bin Kim, Taewook Ha, Dieter Schmalstieg, Shohei Mori, Woontack Woo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Infers per-object physical properties (mass, friction, center of gravity) from a single image via a physics-aware scene graph, providing structured physical priors that could inform physically plausible dynamics or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19815)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Amirhossein Mollaei Khass, Athanasios Cosse, Nader Motee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds semantic risk-weighted control barrier functions over 3D Gaussian maps with active perception, a weakly related spatial-uncertainty representation rather than a learned dynamics or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19330)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Sheng Wu, Guoqiang Zhao, Zhe Yang, Fei Teng, Zhikun Zhou, Yanlin Yang, Zheng Fang, Hong Zheng, Yaonan Wang, Kailun Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments directionally limited animal motion demonstrations via temporal reversal and constrained dynamics completion to train a multi-gait locomotion policy, a narrow dynamics-augmentation insight with limited transfer to world models or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20566)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Yilang Liu, Haoxiang You, Qian Wang, Daniel Rakita, Ian Abraham

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Couples sampling-based MPC with first-order policy gradients for visual policy learning, offering a weakly related model-based control insight but no explicit world-model or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.20575)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Zhongbo Zhang, Jiayi Jin, Yifan Wang, Zaibin Zhang, Haiwen Diao, Lijun Wang, Huchuan Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for embodied spatial intelligence with active perception and metric control; relevant mainly as an evaluation of observe-reason-act loops rather than a world-model or video-generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19554)

---

