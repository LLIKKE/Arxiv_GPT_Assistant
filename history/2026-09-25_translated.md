# 💡 今日研究速览 (Daily Summary)

### World Models for Embodied Manipulation

The dominant thread today is the rapid maturation of world models as the central substrate for embodied control, with a clear shift from visual prediction toward topology-agnostic, action-conditioned dynamics. PointCast exemplifies this by abandoning mesh- or category-specific state representations in favor of per-point diffusion-transformer trajectory prediction, unifying rigid, articulated, and deformable manipulation under a single model and enabling MPC-style planning. AWM-VLA pushes in a complementary direction by embedding aligned latent future-observation modeling directly inside a VLA policy, using object-centric semantic alignment to make long-horizon anticipation both more accurate and more interpretable. Taken together, these works suggest the field is converging on a recipe where generative future prediction is not a separate module but an intrinsic component of the policy itself.

### Asynchronous and Hierarchical Dynamics for Dexterous Control

A second theme concerns the temporal structure of world-action models, particularly the tension between long-horizon intent and high-frequency reactivity. LiMA addresses this directly by decoupling intent generation from reactive refinement through asynchronous diffusion and a Latent Schrödinger Bridge coupling, yielding measurable gains in both latency and success for dexterous manipulation. CereVLA offers a biologically inspired analogue, using a recurrent state-space model to predict the consequences of residual corrective actions, effectively governing action-conditioned rollouts through learned consequence prediction. Both papers point toward architectures that explicitly separate slow deliberative dynamics from fast corrective loops, a distinction that appears increasingly necessary as policies move into contact-rich, high-frequency regimes.

### Agent World Modeling Beyond Vision

Notably, world modeling is expanding beyond visual and physical domains into the cognitive space of LLM agents. Agent-Editing World Model reframes the problem entirely: rather than predicting pixels, it predicts how reasoning and actions shape future task progress and can edit contaminated state, yielding a transferable dynamics-modeling insight for long-horizon agent rollouts. This is a meaningful conceptual departure, suggesting that the world-model paradigm generalizes to abstract task-state dynamics where visual prediction is neither available nor useful. The result hints at a future where agent planning and embodied world models share formal machinery despite operating over radically different state spaces.

### Memory and State Abstraction for Long-Horizon Embodiment

Several papers converge on memory as the bottleneck for long-horizon embodied tasks. MemBodied introduces a fixed-size recurrent associative episodic memory into VLA policies, improving history-dependent manipulation without the context bloat that plagues naive sequence extension. EmbodiedMemory-Bench complements this with a benchmark and external memory system for world-state tracking, providing reusable infrastructure even if its primary contribution is evaluative. Read alongside Kairos, which extends 3D scene graphs into a 4D predictive directional-flow memory for spatial-temporal forecasting, the trend is clear: persistent, structured, and compact state representations are becoming as important as the generative models that consume them.

### Generative Priors and Negative Results in Behavior Modeling

Two papers offer valuable corrective signals. The Gaussian Is Enough reports that non-Gaussian flow-matching priors fail to improve fine-tuning of large behavior models, a useful negative result cautioning against assuming that richer generative priors translate into better action modeling. Banana Kick, meanwhile, identifies first-order learning starvation in response-informed skill evolution for humanoid soccer, a dynamics-adaptation insight that generalizes to contact-rich policy learning. Both papers are methodologically modest but epistemically important, reminding the community that architectural sophistication does not automatically yield capability gains.

### Simulation and Cross-Modal Generation Infrastructure

Finally, foundational infrastructure continues to advance. BladeMaster introduces persistent online-generated discontinuities in a GPU-accelerated cutting simulator, providing physically plausible dynamics for environment modeling in contact-rich tasks. All modalities are equal, but video is more equal diagnoses and corrects a reciprocal cross-modal attention gap in joint video-motion and video-audio diffusion transformers, improving anatomical fidelity and synchronization. Generalizable Robotic Insertion demonstrates that a single visual-proprioceptive world model can zero-shot generalize across many insertion tasks, reinforcing the data-efficiency case for model-based assembly. Collectively, these works strengthen the simulation and generation backbone on which the more ambitious world-model and agent systems above ultimately depend.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hantao Ye, Ross Worobel, Zhuoli Xie, Mingen Li, Houjian Yu, Youngjin Hong, Changhyun Choi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a point-set diffusion-transformer world model that predicts per-point future trajectories for rigid, articulated, and deformable manipulation, with a topology-agnostic state and MPC planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28393)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: An Lanji, Dawei Liu, Jin Li, Haoran Xu, Mei Chen, Yu Tian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Embeds aligned latent future-observation world modeling inside a diffusion-transformer VLA policy, adding object-centric future-semantics alignment for long-horizon anticipation and interpretability.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27753)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ohad Rahamim, Dvir Samuel, Idan Schwartz, Gal Chechik

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies and corrects a reciprocal cross-modal attention gap in joint video-motion and video-audio diffusion transformers, improving anatomical fidelity and audio-video synchronization in generated video.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27901)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ning Chen, Yankai Fu, Junkai Zhao, Qianpu Sun, Guocai Yao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Decouples long-horizon world-action intent generation from high-frequency reactive refinement via asynchronous diffusion and a Latent Schrödinger Bridge coupling, improving dexterous manipulation latency and success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28431)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shuang Sun, Guoxin Chen, Fanzhe Meng, Jia Deng, Huatong Song, Jinhao Jiang, Wayne Xin Zhao, Hongteng Xu, Ji-Rong Wen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an LLM-agent world model that predicts how reasoning and actions shape future task progress and edits contaminated state, offering a non-visual but transferable dynamics-modeling insight for long-horizon agent rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28416)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Iacopo Catalano, Julio A. Placed, Javier Civera, Jorge Pe\~na Queralta

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Extends 3D scene graphs to a 4D predictive directional-flow memory that forecasts presence and motion distributions for planning, a substantive spatial-temporal dynamics representation relevant to world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27467)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Nicklas Hansen, Iretiayo Akinola, Yijie Guo, Jie Xu, Bingjie Tang, Hao Su, Xiaolong Wang, Abhishek Gupta, Dieter Fox, Yashraj Narang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains a single visual-proprioceptive world model across many insertion tasks, showing zero-shot generalization and data-efficiency gains for model-based robotic assembly.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28258)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Shuai Zeng, Yuxuan Liang, Hangmiao Hu, Fobao Zhou, Zixiang Wang, Wenxi Hong, Hang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a recurrent state-space model to predict consequences of residual corrective actions in VLA execution, offering a learned-dynamics insight for action-conditioned rollout governance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27468)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Ziheng Guo, Yang Bu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a state-continuation framework with explicit learned evolution and reuse boundaries, mapped to electromagnetic world-model studies and inverse design, giving a broadly transferable latent-dynamics modeling insight.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27621)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Tej Deep Pala, Navonil Majumder, Bryce Goh, Raphael Yee, Jianfei Yang, Liming Chen, Soujanya Poria

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Adds a fixed-size recurrent associative episodic memory to VLA policies, improving history-dependent manipulation without bloated context, a memory/state-abstraction insight relevant to embodied world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28256)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Lizhou Liang, Xinyu Zhong, Miao Pan, Xiaohe Zhou, Xuanyu Liu, Qinfeng Li, Peng Li, Jintao Chen, Xuhong Zhang, Wenqi Zhang

**机构**: Zhejiang University

**💡 亮点 (Highlight)**: Introduces a benchmark and external memory system for long-horizon embodied memory and world-state tracking, offering a reusable memory mechanism but primarily a benchmark contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28236)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Zhanyu Yang, Yunuo Chen, Yanjia Huang, Joseph Masterjohn, Yin Yang, Chenfanfu Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces persistent online-generated discontinuities in a GPU-accelerated TLMPM cutting simulator, providing a physically plausible dynamics simulation relevant to world-model environment modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27342)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Hao E. Zhang, Ruize Geng, Raihan Haque, Khalil Zbiss, Guanyang Luo, Hui-ping Wang, H. Eric Tseng, Ding Zhao

**机构**: Tsinghua University

**💡 亮点 (Highlight)**: Introduces response-informed skill evolution for adapting a humanoid kicking policy to a contact-rich spin-generating skill, offering a dynamics-adaptation insight (first-order learning starvation) relevant to learned action-conditioned dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27269)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Chen Xu, Rishi Shah, Hadas Kress-Gazit, Haruki Nishimura, Masha Itkina

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Empirically shows that non-Gaussian flow-matching priors do not improve fine-tuning of large behavior models, a useful negative insight for generative action/dynamics modeling though only weakly tied to video or visual world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.27070)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Jichuan Yu, Zhenyu Xiao, Ze Wang, Ruixuan Liu, Changliu Liu, Chuxiong Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Modular dual-arm skill learning and composition for long-horizon assembly is only weakly connected to learned world models or video generation, with no explicit dynamics-model or generative-video contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.28281)

---

