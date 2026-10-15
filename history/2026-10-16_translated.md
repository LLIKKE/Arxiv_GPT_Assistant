# 💡 今日研究速览 (Daily Summary)

### World Models & Predictive Dynamics

The dominant theme today is the maturation of world models from passive video predictors into controllable, action-conditioned simulators with persistent internal state. A clear architectural convergence is emerging around **decoupling abstract state from visual state**: StateCraft maintains an editable symbolic state to condition a video diffusion model, while Thinker-WM and Atomic-WAM jointly evolve RGB, depth, and action within shared dynamics transformers, and RepForcing shows that supervising the *representation* trajectory—rather than intermediate teacher outputs—yields better few-step autoregressive distillation. Equally notable is the turn toward **execution-grounded and weakness-targeted training**: Atomic-WAM uses GRPO rewards to force motion descriptions to be executable, and work on policy-conditioned environment generation synthesizes worlds aimed specifically at a policy's validated failure modes. Several papers attack the long-horizon consistency problem from complementary angles—decoupled drift-diffusion with heteroscedastic uncertainty gating, order-consistent latent geometry that proves acute bends in interpolated latent trajectories cause planning-order reversals, and occupancy modeling via one-step drifting that enables direct policy extraction through differentiation. Finally, the field is beginning to police itself: WorldMemBench reveals that static memory retention does not imply reliable state evolution, and PhyMetric supplies a scene-level QA protocol for diagnosing physical plausibility—together signaling that evaluation rigor is catching up to generation capability.

### Embodied Agents & Vision-Language-Action Models

World modeling is being aggressively absorbed into the VLA stack, with today's papers converging on the question of *where* and *how* future prediction should enter the policy. A systematic disentanglement study of world-representation, integration-paradigm, and backbone choices provides transferable guidance, while ObjDream pushes toward object-centric temporal slots with action-conditioned future object-state prediction to improve manipulation generalization under distribution shift. In autonomous driving, SafeDriveVLA decouples conflict reasoning from action generation by rolling out strict navigation-following futures, and KinoGen uses kinematically grounded video generation to synthesize customizable humanoid loco-manipulation references with keyframe-level goal-pose control. A parallel thread targets sim-to-real transfer: Contact-UAN proposes a residual world model that corrects actuator dynamics while preserving simulator priors, and meta-learning approaches now actively select *what* to simulate for policy co-training. Complementing these methods, a survey on agentic robots organizes world models and world-action models into a broader taxonomy, and ASIWorld introduces a persistent survival sandbox for benchmarking sustained goal execution—evidence that the community is building both the conceptual map and the stress tests for embodied world-action systems.

### Multimodal & Interactive Generation

Interactive generation is diversifying beyond RGB video into richer physical and perceptual modalities. SonoWorld brings pose-controllable ultrasound world models trained from freehand clinical video via latent-action pretraining and EM-based pose grounding, while PAWA targets multi-agent settings with a synchronized POV-plus-panoramic Minecraft dataset and cross-view token alignment. Physical fidelity is a recurring concern: interactive 4D volumetric liquid forecasting under moving-solid interaction introduces transport-aware coupling for long-horizon rollouts, and cardiac dynamic synthesis from sparse observations demonstrates a focus-align-diffuse keyframe paradigm for temporally coherent generation under weak temporal cues. On the efficiency and memory front, Kandinsky S2V 1.0 combines reference-aware multi-scale visual memory with pi-Flow distillation for long-form audio-driven avatars, and a world-state-centric framework improves cross-shot spatial and temporal consistency in agentic video generation. An intriguing cross-cutting insight comes from casting captioning and text-to-image generation as successive refinement with language as the low-rate code—a rate-distortion framing that may transfer directly to video generation objectives.

### Evaluation, Benchmarks & Reliable Dynamics

A substantial cluster of work focuses on diagnosing rather than generating. IsoVRBench constructs isolated-intervention video preference pairs to train reward models without human feedback, improving both generation quality and temporal-order discrimination. Beyond video, VaryST extends spatio-temporal forecasting to open-world distribution shift via dynamic context construction and masking, RAN-JEPA separates representation learning from intervention learning to handle observation-intervention asymmetry in mobile network control, and dynamic graph world modeling predicts future latent node/relation states from temporal context—offering non-visual but transferable dynamics-prediction insights. Two papers probe the boundaries of what current systems can capture: an analysis of why 3D reconstruction breaks down on under-ice AUV video proposes fast failure detection, and work on physical time as a missing dimension of robot policy memory argues that memory states should evolve over measured time intervals rather than step counts. The throughline is a shift from benchmark scores toward *mechanistic* understanding of when and why learned dynamics models fail.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zefan Yang, Zheyuan Zhang, Boris Maihe, Yikang Liu, Hang Yu, Ankush Mukherjee, Xiao Chen, Pingkun Yan, Terrence Chen, Shanhui Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a causal, pose-controllable ultrasound video world model trained from freehand clinical video with latent-action pretraining, EM-based pose grounding, and distillation for long-horizon autoregressive rollout.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19327)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Lorenzo Venturoli, Nedko Savov, Xi Wang, Marc Pollefeys, Luc Van Gool

**机构**: INSAIT Institute

**💡 亮点 (Highlight)**: Decouples a persistent, editable abstract state from the visual state to condition a video diffusion world model, improving long-horizon consistency and controllability in interactive generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19795)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Thinker Team, Peng Gao, Jichao Jiao, Chen Liao, Daqin Luo, Yiming Ma, Baiyu Pan, Hailin Shi, Jiyuan Wang, Xiangming Xu, Xiongwei Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified multimodal world model jointly evolving RGB, metric depth, and robot action in a shared dynamics transformer, supporting joint video-action generation, world prediction, and inverse dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18447)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Anton Arapin, Aditya Singh, Yixin Wang, Jun Gao, Bernadette Bucher

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a decoupled drift-diffusion world model that regresses deterministic next-state predictions plus a heteroscedastic uncertainty map to spatially gate a conditional diffusion process, improving action-conditioned future frame prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19212)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shijun Shi, Zhe Liu, Zhi Hou, Yinan Chen, Tao Zhang, Kai Hu, Yong Liu, Jiangning Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a world action model that couples atomic-motion reasoning with joint future-video and action-chunk prediction, using execution-grounded GRPO rewards to make motion descriptions executable.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20157)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shaoyuan Xie, Zihan Zhang, Jingxuan Wang, Jiashu Qu, Xiaoqing Liang, Lingdong Kong, Junchi Lu, Henrik I. Christensen, Qi Alfred Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces navigation-conditioned world model dreaming that rolls out strict navigation-following futures to decouple conflict reasoning from action generation in driving VLAs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20609)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qi Wu, Lulu Zhao, Sanghyun Hahn, Rishi Yennu, Emmy Yang, Dingqi Zhang, Tao Pang, Jiuguang Wang, Kuan Fang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses kinematically grounded video generation to synthesize customizable humanoid loco-manipulation references, with keyframe editing enabling goal-pose control and improved contact preservation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20552)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Binghan Wu, Kai Zeng, Kai Yang, Ya-Qin Zhang, Joseph Sifakis, Ye Ouyang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Action-conditioned latent world model for RAN control that separates representation learning from intervention learning to handle observation-intervention asymmetry, with coherent what-if rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17584)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Siming Fu, Zheming Fu, Lianrui Mu, Haoyang Huang, Chaojie Gu, Ruizhe He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replaces intermediate-teacher trajectory regression with representation-space supervision for few-step autoregressive video distillation, improving generation quality at four sampling steps.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20111)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Siqi Yang, Yimu Wang, Ziqi Cai, Chengxuan Zhu, Shuchen Weng, Erwin Wu, Zhaofei Yu, Kaipeng Zhang, Boxin Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a synchronized POV-plus-panoramic multiplayer Minecraft dataset and a dual-tower action-conditioned world model with cross-view token alignment and quadratic-phase player encoding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20240)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuanpeng He, Ceyao Zhang, Fangjing Li, Kefei Zhu, Lijian Li, Yueheng Li, Tianjia He, Wenpin Jiao, Zhi Jin, Yaodong Yang, Yuanpei Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns world-action models via predictive rehearsal and action perturbations, using action-response credit assignment to allocate visual supervision for policy learning from video priors.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16443)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Weijie Wang, Haomin Zhang, Ye Li, Akide Liu, Zeyu Zhang, Haoyu Zhao, Yefei He, Donny Y. Chen, Feng Chen, Bohan Zhuang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a world-state-centric scene/event memory framework that improves cross-shot spatial and temporal consistency in long-form agentic video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20571)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jongwon Ryu, Sunjae Yoon, Junyeong Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates interactive 4D volumetric liquid forecasting conditioned on moving solids and introduces a two-level recurrent framework with transport-aware coupling and stabilization for long-horizon physical rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16167)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang, Kai Wang, Jianhua Yang, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically disentangles world-representation, integration-paradigm, and backbone choices for world modeling in VLA policies, yielding transferable insights on future prediction for embodied dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19825)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junlin Wu, Wen Fan, Dandan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a self-approaching (no-reversal) condition for latent-space planning in visual world models and proves that acute bends in interpolated latent trajectories cause candidate-order reversals, offering a broadly useful insight for latent world-model representations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18570)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Bo Li, Yue Yang, Yujin Huang, Siao Liu, David Lemphers, Sara E Rodriguez Gomez, Luke Borgnolo, Can Wang, Xin Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a dynamic-graph world-modeling framework that predicts future latent node/relation states from temporal context, offering a non-visual but transferable dynamics-prediction insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19364)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Shuyue Stella Li, Jacqueline He, Jiahui Chen, Sreya Dutta Roy, Yulia Tsvetkov, Luke Zettlemoyer, Marjan Ghazvininejad, Xiaochuang Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds isolated-intervention video preference pairs to train a reward model that improves video generation quality and temporal-order discrimination without human feedback.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.17234)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Huailiang Ma, Yuxuan Li, Ziyi Zhao, Xinkai Wang, Mingyu Li, Xinyu Guo, Lifeng Zhu, Aiguo Song, Cewu Lu, Jianhua Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds object-centric temporal slots and action-conditioned future object-state prediction to a VLA model, improving manipulation generalization under distribution shift.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20223)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Robin Uhrich, Marco Bagatella, N\'uria Armengol Urp\'i, Pavel Kolev, Georg Martius

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Models discounted state-visitation occupancies with a one-step drifting generative sampler, enabling direct policy extraction via differentiation as a latent dynamics/occupancy world-model insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19883)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Haoyuan Li, Qihang Cao, Huanyuan Zhou, Xin Hu, Sijia Chen, Zihan Guo, Kun Xiang, Yunshuang Nie, Tao Tang, Xinlong Zheng, Jia-Wang Bian, Xianming Liu, Xiaodan Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Internalizes predictive latent world representations and next-frame semantic targets into an MLLM, providing a lightweight predictive-dynamics idea relevant to world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20592)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yue Zhang, Han Lin, Zun Wang, Yidong Huang, Zaid Khan, Mohit Bansal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates training environments targeted at a pretrained navigation policy's validated failure modes, offering a weakness-guided environment-generation loop relevant to embodied dynamics learning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19420)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Jahyeok Koo, Hyeonseo Yu, Seungho Jang, Jaewoo Jung, Jiwon Kang, Seokju Cho, Seungryong Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses 3D language understanding as complementary supervision for novel-view generation, improving cross-view correspondence in VAE representations, which is adjacent to view-consistent video/world generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20610)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Nolan Fey, Khai Nguyen, Yash Prabhu, Gabriel B. Margolis, Pulkit Agrawal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a residual world model that corrects actuator dynamics while preserving simulator physics priors, with contact-consistent replay for humanoid control, contributing a dynamics-modeling insight for sim-to-real transfer.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.18991)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Junkai Liu, Haofan Wu, Nay Aung, Joao A. C. Lima, Steffen E. Petersen, Le Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a focus-align-diffuse keyframe diffusion paradigm for synthesizing dense cardiac dynamics from sparse observations, with transferable ideas for temporally coherent video generation under weak temporal cues.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19050)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 7/10

**作者**: Ruilin Gong, Hao Gong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Casts captioning and text-to-image generation as successive refinement with language as the low-rate code, offering a rate-distortion insight that may transfer to video generation objectives.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.16552)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Nikolay Semenov, Artem Riabinin, Sergey Bassenko, Anna Averchenkova, Julia Agafonova, Anastasia Aliaskina, Kirill Kozlov, Lev Novitskiy, Nikita Samsonov, Nikolai Gerasimenko, Denis Dimitrov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Speech-to-video avatar system with reference-aware three-scale visual memory and pi-Flow distillation for faster long-form generation, offering limited but transferable long-video memory and efficiency ideas.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19290)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Jincheng Zhang, Gy\"orgy Fazekas, Charalampos Saitis

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes self-representation alignment across noise levels in a diffusion U-Net, a training objective that could transfer to video diffusion but is demonstrated only on symbolic music generation conditioned on video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.15575)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Liqian Ma, Vaibhav Saxena, Utkarsh Aashu Mishra, Shuo Cheng, Yongxin Chen, Danfei Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Meta-learns a simulator's data-generation distribution via meta-gradients to improve sim-and-real policy co-training, a weakly related active simulation approach with limited direct world-model or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19479)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Shengnan Guo, Jinjun Cheng, Xiaowei Mao, Jianhao Zhang, Haochen Lv, Yang Jiang, YiHeng Huang, Yan Lin, Youfang Lin, Huaiyu Wan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a generalizable spatio-temporal forecasting model with dynamic context construction and masking, offering transferable ideas for dynamics modeling under distribution shift.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19813)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yushen Liang, Yue Peng, Baosheng Jin, Tianluo Zhang, Xinyu Zhang, Shuyi Zhou, Zhuoran Chen, Xinqi Liu, Shenji Wan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Treats physical time as a missing dimension of robot policy memory by evolving a memory state over measured time intervals, a weakly related dynamics/memory contribution without visual world modeling or video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20524)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Nan Zhou, Jianxiong Gao, Qiuyu Wang, Wen Wang, Jiahao Wang, Yufeng Yuan, Shuaiting Li, Hao Ouyang, Yujun Shen, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a benchmark for diagnosing static and dynamic memory failures in video world models, revealing that static retention does not imply reliable state evolution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19063)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 4/10

**作者**: Siwei Meng, Xuerou Cai, Rui Hu, Ping Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a scene-level QA benchmark with structured physical priors for diagnosing physical plausibility in text-to-video generation, providing a reusable evaluation protocol rather than a new generation method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19823)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Shaocheng Liu, Yuan Meng, Zhenshan Bing, Alois Knoll

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a predictive dynamics adapter that forces latent states to predict future transitions as a regularizer for collective robot manipulation, a weakly related learned-dynamics contribution without visual world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19141)

---

## 34. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Ana-\c{S}tefania Kog\u{a}lniceanu, Kl\'ara Orb\'an, Ashwin Nedungadi, Stefan L\"udtke, Kuderna-Iulian Ben\c{t}a

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes failure modes of 3D reconstruction from under-ice AUV video and proposes a fast failure-detection system, offering limited but plausible insight into video-based dynamics capture regimes.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.19993)

---

## 35. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 3/10

**作者**: Jianfeng Lin, Runze Wang, Haorong Hong, Yuxuan Xie, Zeno Zeng, Zhongyuan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Persistent survival sandbox benchmark for sustained agent goal execution; relevant to interactive environment simulation but contributes mainly evaluation rather than a new world-model method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.14807)

---

## 36. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 2/10

**作者**: Chonghan Qin, Dongming Wu, Kaituo Feng, Jiaxu Wang, Xinlei Yu, Peiwen Sun, Yijia Fan, Xilin He, Bingao Chen, Weitong Lian, Ryan Ji, Wenqi Ren, Xiaobin Hu, Dahua Lin, Yu-Gang Jiang, Xiangyu Yue

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Survey of agentic robots that organizes world models and world-action models within a broader taxonomy, useful for context but without a new method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20442)

---

