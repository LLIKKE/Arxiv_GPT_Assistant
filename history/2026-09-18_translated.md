# 💡 今日研究速览 (Daily Summary)

### World Models & Physical Dynamics

The dominant thread today is the maturation of *world-action models* (WAMs) into structured, causally-grounded systems rather than monolithic video predictors. StrucPhysVideo exemplifies the push toward physics-focused structured-caption data paired with a MoE text-image-to-video backbone, extended into an interactive image-action-to-video model with causal autoregressive few-step robot rollouts—signaling a convergence of world modeling and low-latency control. CSWAM and WholeBodyWAM both attack the representation problem from complementary angles: the former injects a V-JEPA-based causal semantic expert with history-conditioned attention to improve out-of-distribution generalization, while the latter pretrains language-conditioned whole-body motion priors on heterogeneous human/humanoid data and fuses them with video and action experts via asymmetric Mixture-of-Transformers. A notable shift is the treatment of *dynamics shifts as first-class problems*: Changepoint-Aware World Models detect abrupt regime changes via CUSUM on prediction error and forget stale replay, while Causal-History Test-Time Scaling offers a training-free mechanism to detect non-progress and recover reliable history prefixes. Together these papers suggest the field is moving from "predict the next frame" toward "know when your model is wrong, and repair it."

### Generative Dynamics for Embodied & Multimodal Systems

A second cluster extends generative video and flow models into physically grounded, multi-sensory territory. Dreaming the Sound of Contact is particularly striking: it derives force-aware manipulation trajectories from *generated* video plus *generated* contact audio, closing the loop between world models and physically meaningful data generation. DiT-Garment applies a 2D diffusion transformer over UV-space to learn distributions of 3D garment deformations conditioned on motion and physical parameters, a template likely to transfer to broader motion-conditioned deformation. Beyond Random Couplings introduces contrastive noise alignment for flow matching, reducing transport curvature and improving few-step generation—a training-time trick with clear downstream value for video diffusion and flow-based world models. VibeAvatar combines a phonetic-kinematics adapter with GRPO-optimized aesthetic motion policy, illustrating how narrow conditioning-plus-post-training recipes can sharpen motion quality. GenStream takes a different tack entirely, transmitting skeletal keypoints, camera parameters, and static 3D backgrounds, then reconstructing photorealistic humans generatively—a structured-metadata alternative to dense video transmission with implications for bandwidth-efficient human-centric media.

### Navigation, Planning & Multi-Agent Interaction

Navigation and planning papers today share a focus on *adaptive execution under uncertainty*. WAVE-Go couples a world-model action predictor with adaptive interruptible execution for wheel-legged robots, directly confronting the failure mode where predicted action sequences become invalid under dynamic observations. Risk-Aware World Modeling with Flow-Guided Occupancy Evolution forecasts evolving traffic via signed residual correction to support selective trajectory planning in automated driving. TRACER learns probabilistic per-entity response models of how other agents react to robot actions, with persistent identity-bound beliefs updated online—a transferable interaction-dynamics insight for multi-agent world models. VLM-MPPI uses a VLM to select among behaviorally diverse MPPI candidates rendered onto FPV frames, a pragmatic language-grounded action-selection scheme. HAP predicts future 6-DoF head motion from hand motion and a dynamic target-centric occlusion graph, contributing an intention-driven, object-centric dynamics model for egocentric forecasting.

### Humanoid & Whole-Body Control

Humanoid and whole-body control research is increasingly data- and prior-driven. PASSAGE scales scene-aligned motion learning with a perception-conditioned flow-matching planner and whole-body tracker, demonstrating that data scaling improves closed-loop humanoid dynamics prediction and control. Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator combines Transformer encoding, GRU memory, and auxiliary dynamics prediction via a temporal context estimator. ActiveScale augments a VLA with historical video observations and per-frame camera-pose tokens plus a pose prediction head, offering a temporal/spatial representation insight for active-perception policies. DeformSmith generates physically credible deformable assets through a hierarchical agentic pipeline with a physics-grounded harness and robot-interaction feedback—a contribution to simulation-ready dynamics assets rather than video generation per se.

### Action Representation & Data Augmentation

Two papers address the lower-level plumbing of embodied learning. ActionPiece rethinks action tokenization for autoregressive VLAs by introducing physical rank consistency and joint representation-quantization supervision, indirectly relevant to action-conditioned world-model tokenization fidelity. DetAug uses obstacle-blind trajectory augmentation with explicit conditioning labels to enable zero-shot obstacle avoidance, a controllable-policy-rollout data-augmentation idea. SVMemAgent learns a query-agnostic streaming video memory policy via GRPO for online keyframe selection, offering indirect relevance to video generation and learned dynamics.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: WM Team, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds physics-focused structured-caption data and a MoE text-image-to-video world model, then extends it to an interactive image-action-to-video model with causal autoregressive few-step robot rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18430)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tianbin Liu, Jian Zhu, Taiyi Su, Jianjun Zhang, Chong Ma, Zitai Huang, Yi Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments a world action model with a V-JEPA-based causal semantic expert and history-conditioned causal attention, improving out-of-distribution generalization of learned visual dynamics for action prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18462)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Everest Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a changepoint-aware DreamerV3 world model that detects abrupt dynamics shifts via CUSUM on prediction error and forgets stale replay, yielding faster recovery after environment change.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18950)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bowei Zhang, Qiyao Zhang, Shuanghao Bai, Xinhua Wang, Meng Li, Yilei Wang, Leiwang Zhang, Jian Tang, Lu Zhou, Lei Sun, Zhengping Che

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Pretrains a language-conditioned whole-body motion expert on heterogeneous human/humanoid motion as a transferable predictive prior, then fuses it with video and action experts via asymmetric Mixture-of-Transformers for humanoid world-action modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18197)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lin Li (Edwin), Long Chen (Edwin), Kwunhang (Edwin), Wong (Tim), Jiaming Lei (Tim), Song Jin (Tim), Shucheng Du (Tim), Chuhan Zhang (Tim), Songchen Ma (Tim), Weihao Zhang (Tim), Jun Xiao (Tim), Kwang-Ting (Tim), Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free test-time scaling over causal histories for autoregressive world-action models, detecting non-progress, recovering reliable history prefixes, and verifying hypotheses to recover from execution failures.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18016)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Guanhua Ji, Tianyu Li, Dayoon Suh, Yuqian Zhang, Boyan Zhang, Nadia Figueroa

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses generated video plus generated contact audio to derive force-aware manipulation trajectories, extending video world models toward physically grounded contact dynamics and data generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.19137)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Mingyi Li, Ji Li, Zhihao Ouyang, Yage He, B\"orje F. Karlsson

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Couples a world-model action predictor with adaptive interruptible execution for wheel-legged navigation, addressing how predicted action sequences become invalid under dynamic observations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18193)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Rongxiang Zeng, Linsen Cai, Jiafu Zhang, Yijie Zhong, Yide Tao, Shuai Wang, Nan Zheng, Hai L. Vu, Alvaro Garcia Hernandez, Yongqi Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a risk-aware world model with flow-guided occupancy evolution and signed residual correction for forecasting evolving traffic dynamics to support selective trajectory planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18442)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Lennart Wittke, Vinicius Azevedo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces contrastive noise alignment for flow-matching that reduces transport curvature and improves few-step generation quality, a training-time idea transferable to video diffusion/flow models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18488)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Lan Hu, Minghui Liwang, Wenbo Zhu, Xinlei Yi, Wei Gong, Yiguang Hong, Seyyedali Hosseinalipour

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a probabilistic per-entity response model of how other agents react to robot actions, with persistent identity-bound beliefs updated online, offering a transferable interaction-dynamics insight for multi-agent world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18776)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yunji Feng, Junyi Ma, Guanzhong Sun, Chenyang Xu, Hesheng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Predicts future 6-DoF head motion from hand motion and a dynamic target-centric occlusion graph, contributing an object-centric, intention-driven dynamics model for egocentric motion forecasting.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18548)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Yuxuan Ma, Zicheng Zeng, Chunlin Peng, Zhoujian Li, Zetong Zhao, Zhikai Zhang, Yunrui Lian, Han Xue, Sikai Liang, Weiyi Zhu, Mulin Chen, Chenghuai Lin, Jiayu Zeng, Yanwei An, Songan Zhang, Jiayuan Gu, Jilong Wang, Jingbo Wang, He Wang, Li Yi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: A perception-conditioned flow-matching planner with a whole-body tracker that composes traversal behaviors from scene-aligned motion data, showing data scaling improves closed-loop humanoid dynamics prediction and control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18732)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Antoine Dumoulin, Laurence Boissieux, Joao Regateiro, Pierre Hellier, Stefanie Wuhrer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a 2D diffusion transformer over UV-space to learn a generative distribution of 3D garment deformations conditioned on body motion and physical parameters, a transferable approach to motion-conditioned dynamic deformation modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18510)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Qilin Wang, Mingyu Li, Hao Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Talking-avatar video generation with a phonetic-kinematics adapter and GRPO-optimized aesthetic motion policy, offering a narrow but transferable conditioning-plus-post-training recipe for motion quality and efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18632)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Shuai Zhou, Kaisheng Pang, Wenxuan Song, Wenjie Zhang, Xinhu Zheng, Haoang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Augments a VLA with historical video observations and per-frame camera-pose tokens plus a pose prediction head, giving a modest temporal/spatial representation insight for active-perception robot policies.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18514)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Can Li, Jie Gu, Zishun Deng, Jingmin Chen, Lei Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Generates physically credible deformable assets via a hierarchical agentic pipeline with a physics-grounded harness and robot-interaction feedback, contributing to simulation-ready dynamics assets rather than video generation itself.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18620)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Emanuele Artioli, Daniele Lorenzi, Shivi Vats, Farzad Tashtarian, Christian Timmerer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Semantic streaming framework that transmits skeletal keypoints, camera parameters, and a static 3D background, then uses a generative model to reconstruct photorealistic humans, offering a structured-metadata alternative to dense video transmission.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18634)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Reece O'Mahoney, Moritz Zoellner, Ioannis Havoutis

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Obstacle-blind trajectory augmentation with explicit conditioning labels enables zero-shot obstacle avoidance, a weakly related data-augmentation idea for controllable policy rollouts rather than a world model or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18395)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Shijie Lian, Bin Yu, Zhaolong Shen, Xiaopeng Lin, Yichao Du, Zhirui Zhang, Laurence T. Yang, Kai Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces physical rank consistency and joint representation-quantization supervision for action tokenization in autoregressive VLA models, indirectly relevant to action-conditioned world-model tokenization fidelity.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18487)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Zhongyu Chen, Yuxuan Nai, Qian Chen, Yidong Zhu, Chen Jing, Qihan Wang, Xudong Li, Zhizhan Li, Leixin Chang, Liangjing Yang, Hua Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a whole-body loco-manipulation controller with a temporal context estimator that combines Transformer encoding, GRU memory, and auxiliary dynamics prediction, offering a modest dynamics-modeling insight for embodied control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18930)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Hanbing Zhang, Fangguo Zhao, Zerui Li, Xin Guan, Peng Cheng, Shuo Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a VLM to select among behavior-diverse MPPI trajectory candidates rendered onto FPV frames, a weakly related language-grounded action-selection scheme with only indirect world-model or video-generation relevance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18451)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Dohwan Ko, Ji Soo Lee, Pierce Chuang, Debojeet Chatterjee, Ashish Shenoy, Yichao Lu, Seungwhan Moon, Xin Luna Dong, Vikas Bhardwaj, Hyunwoo J. Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a query-agnostic streaming video memory policy via GRPO for online keyframe selection, offering only indirect relevance to video generation or learned dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.18540)

---

