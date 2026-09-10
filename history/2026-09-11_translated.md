# 💡 今日研究速览 (Daily Summary)

### World Models & Latent Dynamics

Today's contributions converge on a maturing understanding of what makes latent world models *work*—and where they silently fail. The most striking result is ARC-Bench, which demonstrates that latent-distance action ranking in frozen JEPA world models is structurally broken, with closed-loop replanning merely masking the defect; this is a cautionary finding that should prompt the community to audit action-selection mechanisms rather than benchmark end-task success alone. Complementing this diagnostic turn, several papers push toward causally grounded and counterfactually identifiable world models: InfluenceField introduces an intervention-aware latent influence field with identifiable causal structure for multimodal rollouts, Counterfactual Latent World Models use a contrastive objective to separate perceptually aliased interventions, and Compiling VGDL into Causal Models shows that symbolic environment descriptions can be lifted into dynamic structural causal models for faithful counterfactual reasoning. A parallel thread emphasizes *action-conditioned* and *multi-view* modeling: Earth System World Model brings transition-action pretraining and masked response learning to terrestrial ecosystem what-if simulation, while DUET-DINO jointly predicts side- and wrist-camera representations for full 7-DoF latent planning and analyzes which visual encoders best capture action-induced dynamics. Domain-specific instantiations—radiological world models for evidence generation and compact visuotactile models for force-constrained lifting—suggest the paradigm is generalizing beyond navigation and manipulation into medicine and contact-rich control. The through-line is a shift from "can we predict the future?" to "is our latent state causally and interventionally faithful?"

### Embodied Agents & Robotic Manipulation

The embodied thread today is defined by benchmarks and representation choices that stress-test long-horizon, contact-rich, and deformable manipulation. FolDeX contributes a real-robot benchmark with 2000+ hours of data for long-horizon deformable object manipulation, filling a conspicuous gap in world-action model training and evaluation. On the control side, the UAV visual servoing work shows that compact target-centric cues plus curriculum RL can stabilize long-horizon vision-guided servoing, reinforcing a recurring theme that representation compactness matters more than raw perceptual richness for embodied policies. The visuotactile lifting paper adds trajectory-level uncertainty calibration and imagination-based actor-critic learning, pointing toward force-constrained control where contact prediction—not just geometry—drives success. Field Converter's geometry-initialized temporal residual refinement for soccer pose estimation is only weakly related but illustrates the same temporal-dynamics toolkit applied to real-world tracking. Collectively, these papers suggest the field is moving past single-task demos toward standardized, physically demanding evaluation regimes.

### Generative Modeling & Video Synthesis

Generative work today splits between physical plausibility and controllability. PhysMAS introduces a physics-grounded multi-agent framework for compositional 4D Gaussian scene synthesis, binding part-wise materials and running MPM simulation to improve the physical realism of generated dynamics—an important step toward generators whose outputs obey contact and material constraints. Geodesic-informed diffusion injects topology-preserving deformation dynamics into generation, offering a geometry-aware formulation that could transfer to structure-preserving video and world-model synthesis. On the controllability front, AgenticGen decomposes advertising video generation into strategy selection and draft generation, using online business feedback with DPO/GRPO to close the loop between generation and reward—an early example of agentic, reward-guided video pipelines. The "Beyond Coherence" benchmark sharpens the critique: professional editing techniques like J-cuts, L-cuts, and transition timing remain poorly controlled in multi-shot audio-video generation, and the proposed agentic baseline exposes these gaps. The emerging picture is that raw visual fidelity is no longer the bottleneck; physical grounding, causal structure, and fine-grained editorial control are.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhihao Wang, Ruichen Wang, Ruohan Li, Lei Ma, George Hurtt, Xiaowei Jia, Gengchen Mai, Shaowen Wang, Yiqun Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an action-conditioned Earth-system world model with transition-action pretraining and masked response learning, enabling controllable what-if interventions and long-horizon dynamics emulation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.08855)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhengshu Zhang, Zhiyuan Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Audits frozen JEPA latent world models and shows latent-distance action ranking is structurally broken, with closed-loop replanning masking the defect—an important insight for latent world-model planning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.05461)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Todd Y. Zhou, Daniel Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Counterfactual Latent World Models with a contrastive counterfactual objective that separates perceptually aliased interventions, plus a representation-agnostic counterfactual separability metric tied to planning success.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.05834)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Nisarga Nilavadi, Ralf R\"omer, Moritz Reuss, Michael Krawez, Tobias J\"ulg, Angela P. Schoellig, Rudolf Lioutikov, Wolfram Burgard

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Cross-view action-conditioned latent world model that jointly predicts side- and wrist-camera representations to enable full 7-DoF latent planning, with analysis of which visual encoders best capture action-induced dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.10506)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiang Qin, Chunji Lv, Yangguang Wei, Yang Gao, Ming Liu, Lizhong Ding, Ye Yuan, Yinjie Lei, Changsheng Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Physics-grounded multi-agent framework for compositional 4D Gaussian dynamic scene synthesis with part-wise material binding and MPM simulation, improving physical plausibility of generated dynamics.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.07174)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zihao Yang, Zijia Wang, Zhiqiu Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an intervention-aware latent influence field with identifiable causal structure for multimodal world modeling, enabling counterfactual rollout and improved propagation prediction of local visual interventions.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.07874)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Nian Wu, Nivetha Jayakumar, Jiarui Xing, Miaomiao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Integrates topology-preserving geodesic deformation dynamics into diffusion generation, offering a geometry-aware generative formulation that could inform structure-preserving video/world-model generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.08153)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Mohit Jiwatode, Bodo Rosenhahn, Alexander Dockhorn

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Compiles VGDL game descriptions into dynamic structural causal models, giving causally faithful environment dynamics for counterfactual reasoning and model-based agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.05459)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Suyang Xi, Songtao Hu, Shansong Wang, Mojtaba Safari, Luke del Balzo, Ehsan Ul Karim, Mingzhe Hu, Kuo Zhang, Tonghe Wang, Ralph R. Weichselbaum, Xiaofeng Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Learns a shared latent radiographic state supporting both diagnostic readout and report-conditioned image generation, a domain-specific world-model formulation with targeted evidence construction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.07719)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 6/10

**作者**: Xingyuan Bu, Chengru Song, Hao Zhou, Tao Zhou, Dong Li, Wei Li, Shilong Li, Hao Shi, Yongxin Guo, Donghao Zhou, Qiangpeng Yang, Shilei Wen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Reward-guided agentic framework that decomposes advertising video generation into strategy selection and draft generation, using online business feedback and DPO/GRPO to improve generated video content.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.09187)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin

**机构**: Alibaba Research

**💡 亮点 (Highlight)**: Benchmark and agentic baseline for editing-technique execution (J-cuts, L-cuts, transition timing) in multi-shot audio-video generation, exposing controllability gaps relevant to controllable video generation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.08275)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Qinzhen Ma (Rice University), Sida Peng (Zhejiang University)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Compact visuotactile world model for robotic lifting with trajectory-level uncertainty calibration and imagination-based actor-critic learning, offering insights on contact prediction and force-constrained control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.09597)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Simon Khan, Laurent Gajny, Jennyfer Lecompte, S\'ebastien Laporte

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses geometry-initialized temporal residual refinement for world-grounded 3D player pose estimation, a weakly related temporal-dynamics method with no generative or world-model contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.10498)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Saurbh Singh Jamwal, Nived Chebrolu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies compact target-centric visual representations and curriculum training for long-horizon UAV visual servoing, weakly relevant to learned dynamics and embodied control but without a world model or video-generation contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.09234)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: Chenhuan Liu, Yi Xu, Feng Wu, Hanyang Wang, Wenxiao Kuai, Weihao Ding, Shan Wang, Yang Liu, Shuyong Gao, Wenqiang Zhang

**机构**: Midea Group (ai.midea.com)

**💡 亮点 (Highlight)**: Real-robot long-horizon deformable manipulation benchmark with 2000+ hours of data that could inform world-action model training and evaluation, though it offers no new dynamics or generative method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2609.10243)

---

