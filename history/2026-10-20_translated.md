# 💡 今日研究速览 (Daily Summary)

### Video World Models & Generation

Today's video world model work converges on a shared diagnosis: the bottleneck is no longer raw generation quality but the *explicit state* a model carries forward. Two papers attack memory directly—one by making it structural, introducing persistent planar geometry jointly predicted with RGB to condition autoregressive chunks and hold cross-view coherence over hundreds of frames, and another by auditing it, with a new evaluation (MIST) that cleanly separates instruction execution from memory retention and shows that a targeted instruction-revision agent method substantially closes the memory gap. A parallel thread targets *physical and geometric fidelity* as a post-hoc or agentic correction layer rather than an emergent property: one line of work trains video-to-video correctors on synthetic paired supervision with optical-flow cues to disentangle camera from object motion, while another wraps generation in a generate-diagnose-repair agent with spatiotemporal causal constraints and experience-augmented in-context reasoning. Read together, the trend is a shift from "bigger video generators" toward modular world models with inspectable, repairable internal state—geometry as memory, agents as physics critics, and benchmarks that tell us which failure mode we are actually fixing.

### Controllable & 3D-Conditioned Generation

A smaller cluster explores bending strong video diffusion priors toward controllable 3D outputs, most notably fine-tuning a video diffusion model into a multi-view avatar with disentangled expression codes and camera-triplet training—delivering convincing hair dynamics and view consistency, though at the cost of narrow, avatar-specific applicability. The signal here is that video diffusion is proving to be a viable backbone for 3D-consistent controllable synthesis, but current instantiations remain point solutions rather than general controllable-3D engines.

### Representation Learning & Alignment

On the representation side, trajectory-level alignment emerges as a distinct granularity of text-video embedding: slow-fast encoding with mask-guided contrastive learning yields transferable spatiotemporal representations for object motion, though explicitly without generative or dynamics-modeling ambitions. This is complementary infrastructure—better motion-aware embeddings are precisely what the world-model and correction pipelines above will need as conditioning and evaluation substrates.

### World Models for Decision-Making & Robotics

One paper extends the world-model paradigm into policy: an action-conditioned graph dynamics model drives prediction-guided action selection, a sensible but auxiliary use of learned dynamics with modest reported gains. The takeaway is that graph-structured dynamics are a promising fit for relational robotic scenes, but the performance delta suggests prediction-guided selection is not yet a decisive advantage over strong model-free baselines.

**Cross-cutting observation:** Today's slate is dominated by *diagnosis and repair* over *scale*. Whether through explicit geometric memory, memory-vs-execution benchmarks, agentic physics critics, or post-hoc geometry correctors, the field is increasingly treating video world models as systems to be instrumented and patched—an encouraging maturation, provided the community converges on shared failure taxonomies rather than bespoke fixes.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yuze He, Bin Tan, Zelin Gao, Yujun Shen, Yong-Jin Liu, Nan Xue, Yinghao Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces persistent planar memory for video world models, jointly predicting RGB and planar geometry to condition autoregressive chunks and sustain cross-view coherence over hundreds of frames with compact explicit 3D memory.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.23795)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Weijie Lyu, Tiancheng Shen, Jason Li, Yujing Wang, Xiaoyuan Wang, Haobo Yuan, Yizhou Zhao, Ming-Hsuan Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a post-hoc video-to-video geometry corrector trained on synthetic paired supervision to fix camera-motion geometric inconsistency in generated videos, with optical-flow cues disentangling camera vs. object motion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.23856)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xikang Guan, Shaocong Yang, Yanqi Bao, Can Wang, Zheng Gu, Zhengqing Chen, Kai Chen, Jing Huo, Yang Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an agentic generate-diagnose-repair framework with spatiotemporal causal constraints and experience-augmented in-context learning to improve physical plausibility of generated videos.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.23677)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Weiyang Jin, Jiwen Yu, Sihan Xu, Yuwei Niu, Xihui Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces MIST evaluation that separates instruction execution from memory in video world models and an M3-Agent instruction-revision method that substantially improves memory reveal scores.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.23542)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 6/10, 创新性 (Nov): 5/10

**作者**: Simon Giebenhain, Tobias Kirschstein, Liam Schoneveld, Davide Davoli, Zhe Chen, Matthias Nie{\ss}ner

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Fine-tunes a video diffusion model into a controllable multi-view avatar with disentangled expression codes and camera-triplet training, yielding plausible hair dynamics and view consistency but narrow avatar application.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.23772)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 5/10

**作者**: Ruizhi Chen, Zining Fan, Yudi Guo, Jiang Liu, Zhiyu Lin, Zhongjiang He, Shouqian Shi, Hao Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes trajectory-level text-video embedding with slow-fast encoding and mask-guided contrastive learning, offering transferable spatiotemporal representations but no generative or dynamics-modeling contribution.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.22842)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 4/10

**作者**: TianLiang Ma, Ting Ma, ZhongYuan Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Uses an action-conditioned graph dynamics model for prediction-guided action selection in a robot policy, a plausible but auxiliary world-model use with modest reported gains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.23274)

---

