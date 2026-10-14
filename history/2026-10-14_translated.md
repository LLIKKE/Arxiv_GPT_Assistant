# 💡 今日研究速览 (Daily Summary)

### Agents

Today's work on long-horizon agents reflects a growing emphasis on how agents manage and reuse their own interaction history rather than treating each episode as an isolated rollout. The standout contribution introduces retrospective exploration: agents deliberately rewind to earlier environment states and evolve their policies using accumulated experience, effectively turning trajectory data into a reusable substrate for future decisions. This reframes exploration as a bidirectional process—moving backward to consolidate knowledge before advancing—and connects naturally to broader themes in world-model planning and persistent memory. While the reported gains are characterized as weakly transferable, the underlying insight is significant: for long-horizon tasks, the bottleneck is often not raw capability but the ability to revisit, re-evaluate, and build upon prior states. This aligns with a wider trend this period toward treating agent memory and state management as first-class research problems, distinct from and complementary to improvements in base reasoning or tool use. As agents are deployed on increasingly extended tasks, mechanisms that let them exploit their own past experience—rather than merely accumulating it—are likely to become a central design axis.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 5/10, 创新性 (Nov): 6/10

**作者**: Ziang Ye, Wentao Shi, Lei Chen, Zhengzhou Cai, Yu Wang, Zhiyuan Yao, Zihan Wang, Xierui Song, Fuli Feng, Yixin Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces environment rewinding with experience reuse for long-horizon LLM agents, offering a weakly transferable insight about state revisiting and knowledge accumulation relevant to world-model planning and memory.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2610.13058)

---

