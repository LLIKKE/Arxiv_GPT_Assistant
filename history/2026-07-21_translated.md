# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
The field is experiencing a surge in methodological innovations aimed at stabilizing and scaling reinforcement learning for large language models. A key trend is the focus on practical training bottlenecks: one paper introduces QUADS, which addresses the instability of low-precision (NVFP4) rollout generation during RL training for Mixture-of-Experts models by aligning quantization errors from both forward and backward passes. Concurrently, work on optimizer choice shows that Muon significantly outperforms AdamW in sparse-reward agentic settings when combined with the GiGPO algorithm. To improve exploration efficiency in complex multi-turn scenarios, a new framework uses process reward models to guide tree rollouts, enabling more targeted exploration for agentic tasks. These contributions collectively push toward more robust, efficient, and scalable RL pipelines for post-training.

### Reasoning (Latent & Chain-of-Thought)
A major breakthrough is the emergence of *latent reasoning* as a concrete architectural paradigm, moving beyond traditional token-by-token chain-of-thought. One technical report details a model that uses compact, learnable latent tokens for internal reasoning, achieving a 200x reduction in output tokens while maintaining performance. Complementing this, a novel method for looped transformers compresses the recurrent KV cache via low-rank latents, with on-policy refinement yielding improved math reasoning. Additionally, a bootstrapped iterative distillation method (BIRD) improves the quality of reasoning rollouts before on-policy training, achieving a strong accuracy-efficiency trade-off. These works signal a shift toward more compressed and efficient internal reasoning processes.

### Understanding & Scaling Laws of Reasoning
A deeper, more systematic understanding of the pretraining-to-post-training pipeline is emerging. A controlled study using chess as a testbed quantitatively characterizes how pretraining choices—such as model size and data volume—directly shape the returns from RL post-training. The key finding is that RL reward curves improve linearly with pretraining tokens, and that RL is capable of surfacing novel correct moves on hard puzzles that were not present in the pretraining data. This work provides foundational insights into the scaling behavior of reasoning, linking the data and compute invested during pretraining to the ultimate effectiveness of subsequent RL fine-tuning.

### Multimodal & Tool-Augmented RL
The application of RL to multimodal reasoning is advancing through the integration of external tools. A new framework for scientific claim verification trains a vision-language model using GRPO with a composite reward signal, augmented by visual tools to improve verification accuracy. This work demonstrates how tool use can be seamlessly incorporated into the RL training loop for complex, domain-specific multimodal tasks, offering a blueprint for combining visual perception, tool invocation, and reinforcement learning for rigorous reasoning.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Leichao Dong, Dongxu Zhang, Yiding Sun, Qirui Wang, Yuhan Wang, Lin Chen, Jihua Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes BIRD, a two-stage bootstrapped iterative self-reasoning distillation method that improves the rollout distribution before on-policy training, achieving strong accuracy-efficiency trade-offs on reasoning benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15736)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum, Matus Telgarsky, Pavel Izmailov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a controlled testbed (chess) to quantitatively study how pretraining choices (model size, data) shape returns to RL post-training, revealing that RL reward curves improve linearly with pretraining tokens and that RL surfaces novel correct moves on hard puzzles.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16097)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: James O' Neill, Fergal Reid

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a post-training cache codec for looped transformers that compresses the recurrent KV cache via low-rank latents, with on-policy refinement improving math reasoning, directly relevant to latent reasoning and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15456)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bowen Zheng, Chao Yi, Dian Chen, Gaoyang Guo, Han Zhu, Jiakai Tang, Jian Wu, Mao Zhang, Wen Chen, Yifan Lu, Yujie Luo, Yuning Jiang, Zhujin Gao, Bo Zheng, Dixuan Wang, Hao Fang, Jiancai Liu, Jing Yu, Ke Chen, Kewei Zhu, Mingke Xu, Wenjun Yang, Xunke Xi, Zile Zhou

**机构**: Alibaba Group (Taobao)

**💡 亮点 (Highlight)**: Introduces Latent Intent Reasoning with compact learnable latent tokens for internal reasoning, directly addressing latent CoT/reasoning with a new architecture and 200x output token reduction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15591)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhengyang Zhuge, Hao Yu, Xin Wang, Zheng Li, Yizhong Cao, Dayiheng Liu, Jianwei Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes QUADS, a quantization-error alignment method to stabilize NVFP4 low-precision rollout generation for RL training of MoE LLMs, directly addressing a key bottleneck in RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15810)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Binglin Zhou, Peng Shi, Ryo Kamoi, Nan Zhang, Rui Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a tool-augmented VLM framework trained with GRPO under a composite reward for scientific claim verification, directly contributing a new RL pipeline and reward design for LLM reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16131)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kai Ruan, Jinghao Lin, Zihe Huang, Ziqi Zhou, Qianshan Wei, Xuan Wang, Hao Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates Muon optimizer for agentic RL post-training of LLMs, showing significant gains over AdamW in sparse-reward settings with GiGPO.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.16169)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xintong Li, Sha Li, Yuwei Zhang, Changlong Yu, Rongmei Lin, Hongye Jin, Shuyi Guan, Xin Liu, Linwei Li, Qingyu Yin, Jingbo Shang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PATR, a process-reward-guided tree rollout framework for multi-turn RL that improves exploration efficiency in agentic tasks, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15610)

---

