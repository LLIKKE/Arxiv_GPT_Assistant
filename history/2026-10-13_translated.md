# 💡 今日研究速览 (Daily Summary)

### World Models & Action-Conditioned Dynamics

The dominant thread today is the maturation of world models from passive predictors into actively controllable, transferable substrates for embodied decision-making. A cluster of work converges on the idea that the *representation* underlying a world model, not merely its predictive accuracy, determines downstream utility: LeWAM shows that jointly training next-latent-state prediction with action flow matching under an isotropic Gaussian constraint yields a model that directly executes policies and plans, while "What Visual Representations Do World Action Models Need?" systematically distills a representation recipe for manipulation. Complementing this, RoleWorld introduces functional role abstractions as reusable symbolic knowledge that transfers across environments with altered object behavior, and "When Generative Models Act as Simulators" probes the editability of generative latents as simulator states, learning explicit latent-to-state mappings. A second theme concerns *grounding* synthetic rollouts in physical reality: Grounded-Dreamer fuses video world models with simulator physics to filter implausible action-labeled data, SimVTA renders trajectory-matched futures via 3DGS for driving, and CASTER formalizes synthetic-video-to-trajectory transfer as constrained optimization, exposing precisely what video generators must satisfy for physical plausibility. Continual and belief-consistent dynamics also feature prominently—Dream to Remember steers a frozen generalist policy via imagined rehearsal to avoid catastrophic forgetting, while Belief-Overlap Partial Inversion performs object-centric belief estimation with partial flow inversion for replanning under uncertainty.

### Video Diffusion: Efficiency, Control, and Generation Quality

Video diffusion research today bifurcates into accelerating inference and imposing finer-grained control. On efficiency, ForcingBooster cuts denoising steps roughly in half via adaptive patch-wise denoising, CORAL-KV compresses autoregressive KV caches through cross-layer prediction and residual coding to enable long-video generation, and Unified Generative Video Compression unifies bidirectional and autoregressive decoding from a shared bitstream with teacher-student distillation for low-latency streaming. On control and fidelity, HorizonNav couples video diffusion with geometry-guided depth alignment for anticipatory 3D robot navigation, GLIMPSE introduces a global-local memory interface with multi-precision spectral encoding to suppress ghosting under revisited viewpoints, and Destination-Conditioned Adaptation improves target-frame faithfulness for large-motion inbetweening. Generation quality itself is addressed from two angles: GraftOOD grafts out-of-distribution exemplars into advantage-weighted rectification to combat motion collapse in video reward optimization, while "Learning Representations to Guide Pixel Diffusion Transformers" introduces Representation Guidance, a low-dimensional bottleneck that improves image generation and scaling efficiency with plausible transfer to video. Together these works suggest the field is shifting from raw sample quality toward controllable, memory-consistent, and compute-efficient generative video.

### Robot Learning & Manipulation Policies

A substantial body of work targets the transfer of pretrained generative and multimodal models into executable manipulation. VLMs are Native Action Models grounds continuous actions in a VLM's text interface for zero-shot control without explicit dynamics prediction, Evo-World augments a lightweight VLA with optical-flow-supervised future motion prediction, and ATHLETE learns reactive humanoid tennis policies by matching trajectories derived from ordinary videos. Closed-loop self-improvement is a recurring motif: EndoRSI drives endoscopic policy improvement from physical rollout evidence, Fly-by-Code equips embodied coding agents with active "View and Probe" diagnostics to gather missing evidence under partial observability, and JoyInside-VLM-Agent performs product-conditioned multimodal policy learning via sandbox trajectory generation. In autonomous driving, ManeuverFlow leverages a world model's predicted future features as evidence for maneuver-conditioned trajectory generation and refinement. The unifying trend is the migration of generative priors into control loops, with physical evidence and closed-loop rollout increasingly serving as the corrective signal.

### Continual Learning, Memory & Embodied Benchmarks

Evaluation infrastructure is catching up to the ambitions of embodied agents. EmbodiedCLBench probes compositional generalization and skill recombination under continual learning, MAGMA-Bench stress-tests long-horizon multi-robot reasoning under dynamic tasks and execution failures, and "What Should Embodied Agents Remember?" benchmarks memory modalities—frames, scene graphs, generated descriptions—for spatial-temporal retention. JitterVBench isolates controller effects on motion quality in VLA-driven manipulation, and TextVBench provides diagnostics for text rendering fidelity in video generation. These benchmarks collectively argue that persistent state tracking, memory representation choice, and execution robustness are now first-class research targets rather than afterthoughts.

### Video-Language Models & Temporal Understanding

Several papers interrogate whether video-language models genuinely model temporal dynamics or merely recognize frames. "Mind the Temporal Gap" empirically demonstrates that video models in driving behave as frame-level bias-driven recognizers, with motion cues recoverable via probes but unused by the video-to-language pathway—a sobering diagnostic. OWLET redistributes token-level credit using privileged spatiotemporal evidence during post-training, and Redirecting Teacher Supervision employs temporal-response-guided latent distillation to steer teacher supervision toward temporal understanding. "What Egocentric Video Embeddings Encode" further shows inertial signals capture complementary dynamics to video embeddings. The emerging consensus is that temporal reasoning must be explicitly supervised rather than assumed to emerge from scale.

### Foundations & Cross-Cutting Architectures

Two contributions push toward unified substrates for world modeling. Kairos proposes a byte-level multimodal foundation model with a shared codec and denoising objective spanning video and control streams, offering a plausible architecture for unified world-model training—though only convergence sanity checks are reported. Robot-WATCHDOG contributes an object-centric spatio-temporal graph world model for failure detection via future state prediction, exemplifying the broader trend toward object-centric dynamics representations. Finally, Make It Flow lifts 2D optical flow into a consistent 3D Eulerian motion field to animate water in static 3D Gaussian Splatting scenes, a reminder that temporally coherent dynamics can be achieved without full physical simulation—an insight with implications for efficient world-model rendering.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Minghao Fu, Tavis Siebert, Eryk Halicki, Randall Balestriero

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents an end-to-end JEPA world model jointly trained on next latent state prediction and action flow matching with an isotropic Gaussian latent constraint, enabling direct policy execution and fast planning with large gains on contact-rich and long-horizon tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12818)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bahey Tharwat, Iman Nematollahi, Marvin Alles, Xingyuan Zhang, Akshay L Chandra, Abhinav Valada

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Continually steers a frozen generalist robot policy using a pretrained world model for imagined rehearsal of prior tasks, avoiding catastrophic forgetting without replay data.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13816)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Boyuan Xiao, Pu Wang, Ji Feng, Yao-Xiang Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces functional role abstractions as reusable symbolic world-model knowledge that transfers across environments with altered object behavior, improving generalization of learned dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13172)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zheming Fu, Ruizhe He, Wenbin Ning, Xiaoxiao Ma, Xuan Yang, Lianrui Mu, Haoyang Huang, Chang Liu, Lei Wang, Siming Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Addresses motion collapse in video reward optimization by grafting out-of-distribution exemplars into advantage-weighted rectification, improving generated video dynamics without sacrificing reward.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13470)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hajira Amjad, Valerii Serpiva, Viacheslav Liubimov, Didar Seyidov, Dzmitry Tsetserukou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses video diffusion to generate plausible future observations for anticipatory robot navigation, with a geometry-guided depth alignment stage that improves 3D consistency of the imagined environment beyond temporal video coherence.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13849)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Albert Ge, Akash Haridas, Utkarsh Saxena, Ruijing Yang, Ian Colbert, Frederic Sala, Vikram Appia, Emad Barsoum

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces cross-layer prediction and residual coding to compress autoregressive video diffusion KV caches, reducing memory for long-video generation while preserving reconstruction fidelity and temporal consistency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12514)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhiyu Xu (Tianjin University), Wei Shang (Singapore Management University), Yushen Xu (Tianjin University), Wenwen Li (Tianjin Medical University), Zhiyan Xu (Southeast University), Pengfei Zhu (Tianjin University), Dongwei Ren (Tianjin University)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Destination-conditioned adaptation plus semantic-geometric alignment of a pretrained latent video diffusion model improves target-frame faithfulness and temporal stability for large-motion generative inbetweening.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13187)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Feng Jiang, Shu Chen, Yuanfei Wang, Yuan Li, Zhenhao Shen, Jiaqi Liang, Yang Chen, Lei Wei, Chen Xie, Ruihai Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Combines a video world model with simulator physics to synthesize physically grounded, action-labeled robot manipulation data, using simulation replay to filter implausible rollouts without human teleoperation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13164)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zekai Gu, Peng Wang, Jiahao Lu, Yongsen Mao, Cheng Lin, Yuan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adaptive patch-wise denoising allocates variable steps across spatial regions in autoregressive video diffusion, cutting denoising steps roughly in half while preserving quality for real-time interactive video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12625)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhufeng Xu, Henglei Lv, Bailin Deng, Yikang Ding, Xiaoqiang Liu, Guoxin Zhang, Hongbo Fu, Lin Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a global-local memory interface with multi-precision spectral encoding for camera-controlled video world models, improving scene consistency and reducing ghosting under revisited viewpoints.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13706)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sevan Brodjian, Michael Hobley, Pietro Perona

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates editability of generative model latents as simulator states, learning mappings between latent representations and environment state to enable controllable next-step prediction in Othello and a continuous video-like world.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12847)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Changhui Jing, Haochen Tian, Hongchen Li, Tianyu Li, Caojun Wang, Zihao Zhang, Yanhao Liu, Chengen Xie, Bailin Li, Hao Zhao, Zhenjie Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a simulation-grounded post-training framework that renders trajectory-matched future videos with 3DGS and uses flow-matching video supervision to improve driving world action model planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13781)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zihao Pan, Mengting Chen, Cheng Shi, Taihang Hu, Zhengrong Yue, Zikang Wang, Yuan Wang, Wei Li, Sibei Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Representation Guidance, a low-dimensional bottleneck that forms and exploits internal representations to guide pixel diffusion transformers, improving image generation quality and scaling efficiency with potential transfer to video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12978)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tianyu Zhang, Shuai Huo, Dengchao Jin, Hewei Liu, Meng Lei, Tianwen Wu, Jiawen Gu, Chao Zhou, Li Li, Dong Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified generative video codec combining bidirectional and autoregressive diffusion decoding from a shared bitstream, with teacher-student distillation for low-latency streaming video reconstruction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13023)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yinlong Dai, Homanga Bharadhwaj, Dylan P. Losey

**机构**: Virginia Tech

**💡 亮点 (Highlight)**: Formalizes synthetic-video-to-robot-trajectory transfer as constrained optimization, yielding concrete insights into what video generation models must satisfy for physically grounded manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12567)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Kai Liu, Jiangran Lyu, Tingyu Deng, Yixin Zheng, Jingtian Wan, Wenbo Cui, Mi Yan, Yizhou Zhou, Haoran Li, Dongbin Zhao, Zhizheng Zhang, He Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically studies which visual representations and integration mechanisms best support world action models built on pretrained video generators, yielding a representation recipe that improves manipulation success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13024)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Zile Zhong, Yuxin Du, Tao Lin, Haoxiao Wang, Wei Dai, Binhua Zuo, Bo Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments a lightweight VLA with future motion prediction via optical-flow supervision, providing a task-relevant predictive dynamics signal that improves manipulation control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12936)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yuhao Wei, Yong Chen, Chen Yang, Yingchen Wang, Delin Ouyang, Lingfeng Qi, Qi Lan, Zhanhua Zhang, Jie Li, Guofa Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a world model's predicted future features as evidence for maneuver-conditioned trajectory generation and refinement in end-to-end driving, a concrete action-conditioned dynamics application.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13409)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Chen Yu, Sudarshan S Harithas, Juan Borbon, Dingqi Zhang, Jiuguang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Object-centric online belief estimation with partial flow inversion for replanning under uncertain object dynamics, offering a transferable insight for belief-consistent dynamics revision.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13087)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Kjell Keune, Florian Hahlbohm, Jannis M\"oller, Susana Castillo, Martin Eisemann, Marcus Magnor

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Lifts 2D optical flow into a consistent 3D Eulerian motion field to animate water in static 3D Gaussian Splatting scenes, yielding temporally seamless looping dynamics without physical simulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13860)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Quentin Rolland, Fabrice Mayran de Chamisso, Jean-Baptiste Mouret

**机构**: CEA-List

**💡 亮点 (Highlight)**: Object-centric spatio-temporal graph world model that predicts future object states for failure detection, offering a transferable object-centric dynamics representation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13403)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jingkun Yi, Shujie Zhang, Zirui Zhou, Haoxiao Wang, Haiyang Sun, Yuhang Dong, Xudong Xu, Xing Shen, Tao Zhang, Yong Liu, Jiangning Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Grounds continuous robot actions in a VLM's native text interface for zero-shot manipulation, relevant to action-conditioned world modeling but without explicit dynamics or video prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12832)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jaewoo Lee, Jeongyeon Seo, Sihyun Cho, Gyeongrak Choe, Yutong Wang, Bavin Saravanan, Jia-Bin Huang, Furong Huang, Sebastian Scherer, Guanya Shi, H. Jin Kim, Seungjae Lee, Dongjae Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Active 'View and Probe' diagnostic programs let embodied coding agents gather missing visual/physical evidence, improving closed-loop policy refinement under partial observability in aerial manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12549)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Qitan Lv, Ke Fan, Hong Wang, Wen Wu, Yilin Wang, Bowen Zhou, Feng Wu, Chao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Video-LLM post-training method that redistributes token-level credit using privileged spatiotemporal visual evidence, offering a transferable insight for grounding video reasoning in temporal dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13272)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Chi Kit Ng, Yidong Zhang, Tianchun Wu, Siu Hing Lui, Hanlin Zhao, Huxin Gao, Hongliang Ren

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Closed-loop robot policy self-improvement driven by physical rollout evidence, relevant as an embodied dynamics/rollout insight though it does not learn a visual world model.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13376)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Zhihao Tian, Zifan Wang, Enzheng Zhu, Xun Yang, Jialong Qin, Mengbo Wang, Junwei Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns reactive humanoid tennis policies from locomotion data and ordinary tennis videos via trajectory-guided motion matching, a narrow but plausible video-derived dynamics contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13572)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Xinkai Lu, Junli Zha, Haolan Wei, Jiahui Wang, Chao Zhou, Xiang Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes temporal-response-guided latent distillation that uses representation responses to temporal perturbations to steer teacher supervision, improving temporal understanding in video-language models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13045)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Shiva Sreeram, Erfan Aasi, Tsun-Hsuan Wang, Alaa Maalouf, Daniela Rus

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Empirically shows video-language models behave as frame-level bias-driven recognizers rather than temporal world models in driving, with motion cues recoverable via probes but unused by the video-to-language pathway.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12575)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Gangyi Li, LuYao Wang, Jingfu Sun, Jingyi Yuan, Hang Liu, Hao Zong, Yujia Hu, Tingting Gao, Jianyong Wang, Xu Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Closed-loop sandbox trajectory generation and staged policy learning for embodied multimodal agents, weakly relevant to learned dynamics and interactive rollout.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12957)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Fabien Furfaro

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a byte-level multimodal foundation model with a shared codec and denoising objective over video and control streams, offering a plausible architecture for unified world-model training, though only convergence sanity checks are reported.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12495)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Kansuke Habano

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes what egocentric video embeddings encode and shows inertial signals capture complementary dynamics, providing insight into video representations of human dynamics relevant to world-model state abstraction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12926)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Jie Huang, Yanan Chen, Ruixun Liu, Kaichen He, Xinyi He, Rui Huang, Zilong Zheng, Zhenliang Zhang, Yiwu Zhong

**机构**: Peking University

**💡 亮点 (Highlight)**: Benchmark for continual learning in embodied simulation probing compositional generalization and skill recombination, indirectly relevant to world-model memory and self-evolving agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13021)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Loan Bernat (LAAS-GEPETTO), Matthieu Grard (LAAS-RAP), Ariane Herbulot (LAAS-RAP), Florent Lamiraux (LAAS-GEPETTO)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for long-horizon embodied multi-robot task reasoning under perturbations, offering insight into persistent state tracking and adaptation relevant to world-model planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13534)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Faith Ogunwoye, Didar Seyidov, Konstantin Gubernatorov, Dzmitry Tsetserukou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replay benchmark isolating controller effects on motion quality in VLA-driven manipulation, tangentially relevant to action-conditioned dynamics and smooth trajectory generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13628)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Ruiqiang Zhang, Hengyi Wang, Chang Liu, Guanjie Wang, Zehua Ma, Weiming Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a benchmark and evaluation framework for text rendering and preservation in video generation, offering diagnostics for spatial and temporal text fidelity that could inform video-generation method development.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13412)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Junxiang Wang, Yuchen Liu, Yi Wu, Guofei Chen, Nir Pechuk, Tao Chen, Zackory Erickson, Yuzhe Qin, Tianyu Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark study of memory modalities (frames, scene graphs, generated descriptions) for embodied agents, giving indirect insight into spatial-temporal memory representations for embodied dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.12561)

---

