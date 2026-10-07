# 💡 今日研究速览 (Daily Summary)

### World Models & Latent Dynamics

The dominant thread across today's submissions is the maturation of world models from passive predictors into controllable, verifiable components of decision-making loops. A clear convergence is emerging around **latent world models with explicit geometric or physical structure**: HLA-WM addresses long-range forgetting in linear-attention recurrent state by adding geometry-guided retrieval over cached states (12x memory reduction), while EpicWorldModel pairs stochastic JEPA latents with a flow-matching predictor and repurposes predictive variance as an exploration signal for CEM planning. ChronoWorld and Keepsake both attack long-horizon consistency from complementary angles—epipolar causal attention with geometric reflection for 4D free-view control, versus a training-free relational memory controller that reassesses stored observations under a fixed budget. Notably, the field is beginning to**audit its own simulators**: the response-theory probe on Lorenz-63 shows learned stochastic simulators can match invariant statistics while misrepresenting slow relaxation modes, and "Considering Context" formalizes predictive sufficiency to determine when external context is actually needed versus history-recoverable. This diagnostic turn is healthy and suggests the community is moving past aggregate-likelihood benchmarks toward mode-resolved evaluation of learned dynamics.

### Predictive Control & Closed-Loop Robotics

A strong cluster of work treats world models as the substrate for**predictive control rather than generation for its own sake**. The laser melt pool paper demonstrates differentiable rollouts enabling amortized policy distillation; SimForcing distills simulation motion priors into an action-conditioned robot world model to bridge sim-to-real and initialize VLAs; and Future Anchored Verification uses predicted future frames as anchors for VLM-guided recovery during execution—a concrete mechanism for detecting drift from predicted dynamics. The disturbance-observer extension to learned world models via state-rollout and cost-query interfaces offers a broadly reusable recipe for sim-to-real compensation. Perhaps most sobering is "Encoded but Not in Control," which reveals a grounding gap where VLA and world-action models encode instructions that fail to steer action selection—a controllability limit that the rest of this cluster implicitly assumes away. TAPDreamer's transferable adversarial patches further expose the shared visual encoders of these models as a robustness liability. Together these papers suggest that**verification and adversarial auditing of world-model control loops is becoming as important as the models themselves**.

### Video Generation & Spatiotemporal Consistency

Video generation research today is converging on**structured inductive biases over brute-force scale**. S2PD's serial-to-parallel diffusion uses autoregressive denoising at high noise to enforce physical and logical state transitions; Prism's dynamic sparse attention adapts block shapes to spatiotemporal content and audio-visual coupling for 2.5x faster native 2K joint video-audio training; and WaveGSSM introduces second-order graph state-space models that explicitly represent motion rate-of-change in the latent state. Efficiency work is equally active: Hybrid-Basis Feature Forecasting provides training-free multi-basis feature forecasting demonstrated on HunyuanVideo, and "Video Encoders Built on Image Representations" builds compact video encoders on frozen image backbones with question-aware token allocation. A cautionary note comes from the causal decomposition of test-time training, showing self-generated feedback destabilizes long-horizon adaptation—directly relevant to any iterative video or world-model training regime. The compression/editing framework using a frozen generator as generative prior rounds out a picture of the video stack being**factorized into reusable frozen components with lightweight, task-specific adapters**.

### Agents, Reasoning & Embodied Interaction

Agentic work today spans GUI, video, and physical interaction. Imagine to Act builds a pixel-level image-editing world model of GUI transitions to synthesize multi-step imaginary trajectories for scalable agent training—an elegant reuse of action-conditioned visual dynamics for data generation. VepAgent bridges causal transitions via tool-augmented RL for video event prediction, and Long-Horizon Textual World Modeling casts multi-step transitions as structured reasoning over sparse state changes with predictive-gain rewards. On the embodied side, I-BFM learns shared latent representations of humanoid-object-contact dynamics via forward-backward representations and unsupervised RL, while InterMimicGen scales humanoid loco-manipulation through a self-evolving motion-imitation flywheel. The ultrasound guidance paper is a notable non-robotics application, formulating operator guidance as retrieval-induced latent transition planning in a V-JEPA world model without probe-tracking hardware. A recurring theme is**nonparametric or retrieval-based dynamics**as a lightweight alternative to fully learned transition models, and the growing use of predictive-gain or variance signals as intrinsic rewards for exploration.

### Multimodal Generation, Avatars & Applications

A final cluster applies generative dynamics to human-centric and domain-specific synthesis. CoDance learns reactive, compliant human-humanoid interaction from video via multi-link compliance augmentation; Talk, Render, Act integrates streaming speech, audio-driven facial animation, and semantically planned body motion; and UltraDub unifies visually-steered flow learning with trajectory guidance for authentic dubbing. Generating the Wild adds frequency-aware identity conditioning for individual-consistent wildlife image-to-video, and the pedestrian risky-motion generator combines trajectory-level conflict synthesis with text-conditioned motion diffusion and animatable 3DGS avatars for driving safety evaluation. Mobile-4DGS contributes a compact explicit 4D Gaussian representation with second-order motion for continuous-time dynamic rendering. While several of these are narrow applications, they collectively signal that**controllable, identity- and physics-preserving generation is becoming the default expectation**, and that domain-specific datasets (wildlife, driving, dubbing) are increasingly paired with targeted conditioning mechanisms rather than generic text prompts.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 7/10

**作者**: Zhuokun Chen, Feng Chen, Xi Lin, Xiyu Wu, Jiahao He, Jianfei Cai, Bohan Zhuang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies long-range forgetting in Gated DeltaNet and introduces geometry-guided retrieval over cached recurrent states, improving long-horizon video world-model revisit consistency and camera control with 12x memory reduction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05739v1)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jeffrey Hu, Daniel Olmeda Reino, Ayush Tewari

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes serial-to-parallel diffusion that uses autoregressive denoising at high noise to enforce physical and logical state transitions, improving rule consistency and temporal stability in video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06847v1)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bowen Feng, Julian Ost, May Mei, Anirudha Majumdar, Felix Heide

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains stochastic JEPA latent world models with a flow-matching predictor and uses predictive variance as an exploration signal for CEM planning under partial observability.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05996v1)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuyuan Tu, Qi Tian, Yinming Huang, Yue Wu, Xintong Han, Kaihang Pan, Weijie Kong, Jiangfeng Xiong, Jian-Wei Zhang, Zuxuan Wu, Yu-Gang Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a dynamic sparse attention framework that adapts block shapes to spatiotemporal content and audio-visual coupling, enabling 2.5x faster native 2K joint video-audio generation training with better quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05416v1)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Abdul Mohaimen Al Radi, Kunyang Li, Yuzhang Shang, Mubarak Shah, Yu Tian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free relational memory controller that reassesses stored observations via pose-appearance graphs, improving long-horizon camera-controlled video consistency under a fixed memory budget.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06588v1)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Fangxin Wang, Xiang Gao, Yuguang Yao, Kaiwen Dong, Nikash Walia, Kamalika Das

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Casts multi-step textual world-model transitions as structured reasoning over sparse state changes with predictive-gain and intermediate rewards, improving long-horizon prediction and counterfactual action sensitivity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06637v1)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yiyang Yan, Markus Bambach, Mohamadreza Afrasiabi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a generative latent world model for laser melt pool dynamics whose differentiable rollouts enable predictive control and amortized policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06250v1)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaoyu Zhou, Dingwei Xian, Zhenyu Wang, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Camera-controllable 4D world generation with spatiotemporal epipolar causal attention and a reconstruction-driven geometric reflection pipeline improves global spatiotemporal consistency and free-view controllability in generated video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06687v1)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaodong Wang, Tianle Li, Chuanxin Song, Junliang Xie, Zhanmi Zhong, Suiying Wu, Peixi Peng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces latent-motion distillation from a simulation teacher plus multi-block simulation conditioning and classifier-free guidance to build an action-conditioned robot world model with better real-domain video dynamics and downstream VLA initialization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06598v1)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Noortje I. P. Schueler, Hans van Gorp, Ruud J. G. van Sloun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates ultrasound operator guidance as retrieval-induced latent transition planning in a V-JEPA-based world model, showing a nonparametric dynamics model can support closed-loop goal-reaching without probe tracking hardware.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06008v1)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 6/10

**作者**: Zhibin Qin, Zhenxiong Tan, Xinchao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a world action model's predicted future frames as anchors for verification and VLM-guided recovery during robotic execution, a concrete closed-loop mechanism for detecting and correcting drift from predicted dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06280v1)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junyou Zhu, Fenying Cai, Ping Xiong, Christian Nauck, Langzhou He, Chao Gao, Jürgen Kurths, Frank Hellmann

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a second-order graph state-space model that explicitly represents motion/rate-of-change in the latent state, improving spatio-temporal propagation prediction and weather forecasting dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06540v1)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: João Böger, Simon Driscoll, Niccolò Zagli, Valerio Lucarini, Francisco Camara Pereira

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a mode-resolved linear-response test that reveals learned stochastic simulators can match invariant statistics yet misrepresent slow relaxation modes, a broadly useful diagnostic for learned dynamics models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06798v1)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Oleg Smirnov, Sofiane Ennadir, John Pertoft, Bjartur Hjaltason, Sara Karimi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formalizes predictive sufficiency to quantify when world models actually need externally supplied context versus history-recoverable information, offering a practical criterion for matching context-aware mechanisms to available information.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06651v1)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Tianqi Zhu, Jun Yang, Jianliang Mao, Cong Li, Shihua Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends disturbance observers to learned world models via state-rollout and cost-query interfaces, offering a broadly useful insight for compensating sim-to-real mismatch in learned dynamics models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.04896v1)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Siyuan Liu, Miao Li, Haibao Yu, Haohong Lin, Qing Zhou, Bingbing Nie, Ding Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Combines trajectory-level conflict synthesis with text-conditioned motion diffusion and animatable 3DGS avatars to generate photorealistic, motion-controllable safety-critical driving scenarios, advancing controllable video/world simulation for driving evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06171v1)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Ziqi Han, Yitang Li, Junhan Sun, Fanrong Dong, Yaojie Shen, Lei Ye, Zetong Jing, Yongqi Zhang, Yiming Zhang, Xue Wang, Hao Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a shared latent representation of humanoid-object-contact coupled dynamics via forward-backward representations and unsupervised RL, providing a dynamics-model insight for closed-loop interaction and recovery.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06129v1)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yongxin Ning, Runliang Niu, Qianli Xing, Zhiyi Duan, Qingzu He, Pan Wang, Qi Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a pixel-level image-editing world model of GUI transitions to synthesize multi-step imaginary trajectories for agent training, offering a controllable action-conditioned visual dynamics approach.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05861v1)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Compact explicit 4D Gaussian representation with second-order motion and temporal support enables continuous-time dynamic scene rendering, relevant to temporal dynamics modeling though focused on mobile rendering efficiency rather than generative video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05289v1)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Qiutong Chen, Yuchan Guo, Zhenlong Yuan, Haobo Yang, Fangfang Lin, Xinyi Long, Yin Wang, Zijian Song, Rui Lan, Shi Qiu, Boyuan Pan, Yang Luo, Yuyin Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Agentic tool-augmented RL framework explicitly models causal transitions from observed to future events for video event prediction, providing a weakly supervised dynamics-reasoning angle relevant to future prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06293v1)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Shaohan Jiang, Jiahang Cao, Qiduo He, Fengting Deng, Kun Wu, Jingkai Sun, Jiaxu Wang, Qiang Zhang, Qihao Zheng, Chunfeng Song, Ping Luo, Andrew F. Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnostic analysis of vision-language-action and world-action models revealing a grounding gap where encoded instructions fail to control action selection, offering insight into controllability limits of world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06235v1)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng, Yichen Feng, Yaorui Ding, Yuetai Li, Zhen Xiang, Bhaskar Ramasubramanian, Basel Alomair, Luyao Niu, Radha Poovendran

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that transferable adversarial patches corrupt shared visual encoders of world action models, exposing a vulnerability relevant to robustness of world-model representations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06814v1)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xihua Sheng, Dong Liu, Chang Wen Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a spatiotemporal semantic-importance-guided compression and editing framework that uses a frozen video generator as a generative prior, offering transferable insight into which spatiotemporal latents matter for AI-generated video reconstruction and prompt-based editing.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05779v1)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Yuzhuo Li, Di Zhao, Xinyu Zhang, Daniel Wilson, Yun Sing Koh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds a frequency-aware identity conditioning branch to a frozen image-to-video model to preserve fine-grained individual appearance cues, with a wildlife video dataset for training and evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05587v1)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Kai-Liang Cheng, Yuan-Yuan Cheng, Yu-fan Jin, Xiao-Ming Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free multi-basis feature forecasting accelerates diffusion sampling and is demonstrated on HunyuanVideo, offering a transferable efficiency technique for video diffusion generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05254v1)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Cheng Luo, Bing Li, Bernard Ghanem

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Causally decomposes how self-generated feedback destabilizes test-time training over long horizons, offering transferable insight into error accumulation and update validation relevant to long-horizon world-model and video generation training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05076v1)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Yucheng Zhang, Sirui Xu, Jinhong Li, Liuyu Bian, Anatulya Nandi, Derek Zhang, Xiangchen Liu, Xueting Li, Umar Iqbal, Yu-Xiong Wang, Liang-Yan Gui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Self-evolving motion-imitation data flywheel for humanoid loco-manipulation offers only indirect relevance to world models or video generation, as it concerns robot motion data scaling rather than learned visual dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06850v1)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Di Wu, Ping Liu, Xuhua Chen, He Zheng, Lingfeng Zhang, Tao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Execution-aligned progressive noise improves temporal consistency across asynchronously replanned action chunks in generative robot policies, a weakly transferable idea for temporally coherent generative rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06090v1)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jin Jiang, Kun Li, Jiancong Ma, Shengcai Liao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Integrates streaming speech, audio-driven facial animation, and semantically planned body motion for a humanoid, offering a narrow but plausible multimodal generative-dynamics pipeline relevant to controllable embodied video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06153v1)

---

## 30. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Baiqin Wang, Zhixing Ding, Jijie Li, Jiankuo Zhao, Zhen Lei, Xiangyu Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Improves person-specific speaking-habit imitation in real-time talking-head generation via motion-space flow matching, a narrow avatar application with limited transferable video-generation insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06658v1)

---

## 31. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jusheng Zhang, Wenhao Wang, Longqi Cai, Liangzhe Yuan, Yuxiao Wang, Ming-Hsuan Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds compact video encoders on frozen image representations with question-aware token allocation and lightweight temporal refinement, relevant to video-generation tokenizer and efficiency design though framed for video-language understanding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.06616v1)

---

## 32. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zhuoqun Chen, Shucheng Jia, Boyuan Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns reactive, compliant human-humanoid interaction from video via multi-link compliance augmentation, providing a narrow but plausible connection to learning dynamics from video for embodied control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05324v1)

---

## 33. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Gaoxiang Cong, Liang Li, Jianwei Wen, Zhedong Zhang, Zheng-Jun Zha, Qingming Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a visually-steered flow-learning and trajectory-guidance dubbing framework that improves lip-sync and speaker consistency, with limited but plausible transferable relevance to controllable video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.05932v1)

---

