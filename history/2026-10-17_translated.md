# 💡 今日研究速览 (Daily Summary)

### World Models & Predictive Dynamics

Today's papers reveal a striking convergence around **world-action models**—architectures that jointly learn perception, action-conditioned future prediction, and planning within shared backbones. The dominant design pattern couples latent world models with policy learning, whether through mixture-of-transformers video diffusion (Perceive-Predict-Plan), view-decoupled geometry states (GeoState), or JEPA-based latent ranking for VLA verification (VeriVLA). A key emerging insight is**reciprocity**: unified causal training shows world modeling and action modeling mutually reinforce each other, while VLA-Δ and "What Should Robot Policies Learn to Predict?" systematically probe which supervision targets—action, latent-action, or future-vision—yield the best dynamics representations. Test-time adaptation is also maturing: T2-z optimizes environment latents for unseen physical configurations, and Plans-Are-Not-Executions closes the planning-execution gap by adapting frozen planners to controller-specific characteristics rather than substituting executed trajectories.

### Robot Learning & Vision-Language-Action Models

The VLA landscape is shifting from pure action imitation toward**dynamics-aware learning targets**. Several works now supervise explicit physical state transitions (VLA-Δ) or temporal latent actions (TS-WAM) to guide action generation, enabling learning from action-free videos. EgoJEPA pushes cross-embodiment transfer further by decoupling human priors from robot-specific control via effect-aware latent actions learned from egocentric video. Verification is becoming a first-class citizen: VeriVLA demonstrates that test-time action-chunk ranking via latent world models improves manipulation success without pixel reconstruction. Meanwhile, MAIA anticipates contact-rich manipulation anomalies by predicting future visual and force consequences—moving beyond reactive monitoring. Together, these papers suggest the field is converging on a recipe where policies learn *what to predict* (state transitions, latent actions, future features) rather than merely *what to do*.

### Multimodal Reasoning & Agentic Systems

A notable trend is the **repurposing of video generators as general-purpose perception and reasoning engines**. Gen4P shows that pretrained video generators transfer to feed-forward 4D perception with continuous-time queries, while CoWorld Reasoner embeds a video world model as a visual imagination engine within an agentic harness featuring co-evolving tools and skills. Intern Lumina U2 extends this with a multi-codebook diffusion LLM supporting video and 3D inputs. On the agentic front, the Gemini 4 Argon Minecraft run demonstrates sustained coherent planning over thousands of steps, and the proactive video assistant benchmark introduces risk prediction and intervention timing—both offering plausible, if indirect, evidence for long-horizon memory and anticipatory dynamics in agentic systems. "Can Visual Generation Expand What Unified Multimodal Models Know?" probes whether generation training transfers new knowledge to text-only QA, with alignment strategies relevant to unified generation-understanding training.

### Efficient Video & World Model Architectures

Efficiency and memory are being tackled through**spatial and temporal abstraction**. Velox introduces a training-free frustum-slab attention router that selects region-level historical context, accelerating long-horizon video world-model rollouts while preserving visual memory. Memory-as-Weights takes a complementary approach, internalizing long-term streaming history into evolving LoRA weights via a recurrent HyperNetwork—a transferable mechanism for long-horizon video and world models. ReState identifies a noise-level temporal mismatch in few-step diffusion and corrects masked predictions toward background evidence, a training-free insight applicable to efficient video diffusion editing. Constrained multi-agent RL in imagination moves constrained policy updates into learned rollouts, reducing environment interactions—another sign that learned simulators are becoming the default substrate for both training and evaluation.

### Representation Learning & Physical Understanding

Several papers probe the**geometric and physical structure latent in learned representations**. Local Temporal Contrasts on human motion data induce a latent geometry with coherent structure, while "How Much Physics Can Vision Learn from Audio?" distills audio-derived damping structure into vision encoders, showing multi-frame visual dynamics recover material properties. FutureLift refines multimodal motion forecasts via bidirectional future graphs, offering a transferable relational dynamics representation. GRASE closes the loop between real and simulated geometry through agentic render-vs-capture feedback, directly relevant to world-model construction. Collectively, these works suggest that self-supervised objectives over temporal and multimodal signals are uncovering physically meaningful latent structure—a foundation for more sample-efficient and generalizable dynamics models.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang, Ping Tan, Jie Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified world-action model that jointly learns 3D perception, action-conditioned visual future prediction, and goal-directed planning via a mixture-of-transformers video diffusion backbone with shared weights.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22363)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a view-decoupled geometry state representation for predictive 3D world models, separating scene dynamics from camera-induced variation to enable geometrically consistent cross-view rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22343)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chenyuan Zhou, Yining Hong, Huang Huang, Yunfan Jiang, Wenlong Huang, David Held, Vitor Campagnolo Guizilini, Yue Wang, Li Fei-Fei, Jiajun Wu, Leonidas Guibas, Yejin Choi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces test-time optimization of unsupervised environment latents that condition a robotic world model, enabling adaptation to unseen physical configurations and improving action-conditioned prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22364)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yi Qiao, Maolin Zheng, Haoran Sun, Lujia Dong, Wenzhao Lian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Builds a vision-action-force world model that predicts future visual and force consequences of planned actions to anticipate contact-rich manipulation anomalies earlier than reactive monitors.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21686)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Menghao Yin, Jiaju Yin, Xiyue Dong, Lixin Xu, Zhenhui Zhang, Ke Zhang, Yating Feng, Renjing Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Couples a self-supervised temporal latent-action model with a latent world model to predict future visual features that guide robot action generation, enabling learning from action-free videos.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21922)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, Zhe Liu, Hengshuang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a JEPA-based latent world model to rank action chunks by predicting action-conditioned future latents and task-progress changes, improving VLA manipulation success without pixel reconstruction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21985)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiuhong Shen, Shizun Wang, Xinchao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Training-free frustum-slab attention router that selects region-level historical context to accelerate long-horizon interactive video world-model rollouts while preserving visual memory.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22311)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Meng Cao, Can Zhao, Jinjie Wei, Haonan Zhao, Yulong Zhang, Duo Han, Xiaofan Li, Ziwu Song, Rongtao Xu, Ruyi Gan, Hao Wang, Qian Wang, Daolin Ma, Ian Reid, Xiaodan Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns effect-aware latent actions and a latent-action world model from egocentric human video, decoupling human priors from robot-specific control for cross-embodiment manipulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20904)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yue Su, Bokai Lin, Xinkai Wang, Chubin Zhang, Xiangnan Wu, Kuan Zhang, Weiyang Jin, Jiwen Yu, Yiming Li, Cewu Lu, Lixin Yang, Xihui Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Unified causal training framework showing reciprocal benefits between action-conditioned video world modeling and policy learning in a shared video-action architecture.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21095)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yitong Xia, Zeren Jiang, Chuanxia Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Repurposes a pretrained video generator as a feed-forward 4D perceiver with continuous-time on-demand queries, showing video generative pretraining transfers to geometry and motion understanding.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22371)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses a video world model as a unified visual imagination engine within an agentic reasoning harness, with co-evolution of tools and skills for flexible spatiotemporal reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21910)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Danqi Zhao, Keyu Chen, Wenchao Sun, Minglei Huang, Jianhe Zhang, Yan Zhu, Hao Cheng, Zifan Cao, Sifa Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that adapting a frozen world-model planner's latent rollout to controller-specific execution characteristics, rather than substituting executed trajectories, closes the planning-execution gap.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22041)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Raz Shmueli, Shahaf S. Shperberg

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a multi-agent world model that predicts cost in imagination, moving constrained policy updates into learned rollouts and reducing environment interactions.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21319)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 7/10

**作者**: Zhuoming Liu, Jinhong Lin, Lin Zhang, Yiwu Zhong, Yin Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Internalizes long-term streaming video history into evolving LoRA weights via a recurrent HyperNetwork, offering a transferable memory mechanism for long-horizon video/world models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22070)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Daniel Grimm, J. Marius Z\"ollner

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Refines multimodal motion forecasts via bidirectional future graphs, offering a transferable relational dynamics representation for long-horizon trajectory prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22215)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Donghwan Lee, Sanghyun Jo, Sihyun Kim, Ziseok Lee, Kyungsu Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a noise-level temporal mismatch in few-step diffusion and corrects masked clean predictions toward background evidence, a training-free insight transferable to efficient video diffusion editing.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21287)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Zainab Afolabi, Vadim Selyutin, Zhao Gao, Babs Khalidson, Mohamed Ghoneim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Probes and distills audio-derived damping structure into vision encoders, showing multi-frame visual dynamics recover physical material properties relevant to learned dynamics representations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22221)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Haitao Shen, Hanyu Liu, Yihan Lin, Huiping Liu, Junbo Cui, Daoheng Li, Yang Li, Jing Zhang, Wenxin Li, Yuan Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically studies supervision-target allocation between action prediction, latent-action, and future-vision objectives in VLA learning, yielding insights on what dynamics policies should predict.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21915)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Zhaorui Lin, Haohan Liu, Zhen Chen, Xiangru Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Agentic real-to-sim pipeline that iteratively refines 3D scene geometry from video via render-vs-capture feedback, offering a closed-loop scene-modeling insight relevant to world-model construction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21498)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Qi Lu, Jiarun Li, Ce Zhang, Miao Pan, Yi Pan, Xu Wang, Wenqi Zhang, Xuhong Zhang

**机构**: ZJU-OmniAI

**💡 亮点 (Highlight)**: Supervises explicit physical state transitions between current and future states to improve VLA action generation, providing a dynamics-aware learning target relevant to world modeling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21306)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Wenkai Li, Wenyi Hong, Zhuoyi Yang, Jie Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Probes whether image-generation training transfers new knowledge to text-only QA in unified multimodal models, offering a controlled protocol and alignment strategies relevant to unified generation-understanding training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21459)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Louren\c{c}o A. Rodrigues, Felix Putze

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Temporal-neighborhood contrastive objective yields latent representation trajectories with coherent geometric structure, a potentially transferable representation insight for learned dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21630)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Qian Yu, Zongyang Qiu, Juncheng Yan, Hongliang Li, Qi Qin, Keqi Wang, Siqi Luo, Junkui Ju, Yapeng Mi, Tiantian Lu, Tian Liu, Pengyu Xie, Chenhao Ji, Minghui Zhang, Yiang Zhao, Siyu Yan, Haiying Xu, Yanbo Wang, Jianghan Shen, Yuandong Pu, Jiayi Lei, Borui Zhang, Jinxin Shi, Bo Zhang, Yuhang Zang, Shenglong Ye, Lixin Gu, Hongjie Zhang, Linghan Liu, Xinyuan Chen, Yuewen Cao, Lihe Zhang, Xiaohong Liu, Junjun He, Qiangwei Liu, Qi Zhang, Yu Cheng, Tianfan Xue, Hui Xiong, Chang Xu, Yu Qiao, Yihao Liu, Bin Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Multi-codebook discrete diffusion language model supporting video and 3D inputs, with a stability-aware sampling strategy that could transfer to video generation efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.20818)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Maxence Faldor, Satinder Singh, Roberta Raileanu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Long-horizon multi-agent Minecraft run demonstrates sustained coherent planning over thousands of steps, offering weak but plausible insight into long-horizon dynamics and memory for world-model agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22319)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Boyu Cui, Junhao Luo, Zhihao Wang, Linghan Chen, Zejun Li, Jiwen Zhang, Siyuan Wang, Zhongyu Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Benchmark for proactive video understanding with risk prediction and intervention timing, offering limited but plausible insight into anticipatory dynamics modeling for assistants.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.21568)

---

