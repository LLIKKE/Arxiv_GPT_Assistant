# 💡 今日研究速览 (Daily Summary)

### RL for LLMs and Agents
A significant cluster of papers today focuses on advancing reinforcement learning (RL) for large language models (LLMs) and agents, moving beyond standard policy gradient methods. Several works address the critical challenge of credit assignment and reward shaping. **Contrastive Policy Optimization (CPO)**introduces a token-level contrastive disagreement signal for correctness-aware advantage estimation in RLVR, theoretically and empirically outperforming entropy-based methods. Complementing this,**Branching Policy Optimization (BPO)**tackles high variance in agentic RL by leveraging deterministic sandbox snapshots to construct a shared-prefix rollout tree, improving success rates on complex agent benchmarks. On the reward design front, a**Pairwise Validator**is proposed as a drop-in replacement for scalar rewards in self-evolving agent loops, offering a more robust training signal. Finally,**Step-Level Preference Learning**applies DPO to generative agents for social simulations, improving long-horizon decision quality by learning from step-by-step human preferences.

### On-Policy Distillation and Generalization
On-policy distillation emerges as a powerful theme for transferring capabilities and ensuring generalization. The**Progressive RLVR**framework establishes the first non-vacuous generalization bounds for RL fine-tuning by integrating on-policy distillation with TinyLoRA and quantization. A novel**On-Policy Delta Distillation**method efficiently transfers reasoning capabilities by using the delta between teacher and base model outputs. The**SEED**framework directly addresses the supervision gap in outcome-based RL for agents by converting completed on-policy trajectories into hindsight skills, which are then distilled back into the policy, creating a self-evolving loop.

### Latent Reasoning Architectures
A new wave of architectures is exploring more efficient and persistent internal reasoning. The**T2MLR (Transformer with Temporal Middle-Layer Recurrence)**fuses cached middle-layer representations across tokens, enabling persistent intermediate computation with minimal overhead and strong gains on math reasoning. Similarly, a**training-free per-token halting rule**for depth-recurrent transformers exploits fixed-point convergence, allowing variable-depth internal computation without explicit chain-of-thought, directly advancing the field of latent reasoning.

### Diffusion Models and Multimodal Reasoning
Reinforcement learning is being systematically applied to new domains. A**Continuous-Time RL framework**is proposed for fine-tuning discrete diffusion models, enabling reward-driven optimization with intermediate rewards, which provides a unified perspective on policy optimization for masked diffusion LLMs. This is complemented by**Mask-Aware Policy Gradients**, which introduces a novel two-stage action MDP for these models. In the multimodal space,**SD-MAR**combines synthetic data generation with a new RL method (GRPO-lite with BDA) for multi-image analytical reasoning in VLMs, specifically strengthening later reasoning steps via a novel reward allocation scheme.

### Understanding and Improving Reasoning Distillation
Critical insights into the data generation process for reasoning are provided.**Answer-Conditioned Chains of Thought**are shown to degrade verifiable-reasoning distillation, with a clear mechanism explaining why answer-blind data generation is superior. Furthermore, applying GRPO to multimodal document QA**without intermediate reasoning tokens** reveals surprising phenomena like reasoning suppression and grounding divergence, highlighting the need for careful reward design and training recipes in this setting.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Weiwen Xu, Jia Liu, Hou Pong Chan, Long Li, Deng Cai, Min Chen, Hao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Contrastive Policy Optimization (CPO) using token-level contrastive disagreement for correctness-aware advantage shaping in RLVR, with theoretical and empirical results showing strong improvements over entropy-based methods.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14614)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yuxuan Zhu, Rohan Alur, Daniel Kang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Establishes first non-vacuous generalization bounds for RLVR fine-tuning of LLMs via a Progressive RLVR framework integrating on-policy distillation, TinyLoRA, and quantization, directly advancing RL-for-LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14506)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jinyang Wu, Shuo Yang, Zhengxi Lu, Fan Zhang, Yuhao Shen, Lang Feng, Haoran Luo, Zheng Lian, Shuai Zhang, Zhengqi Wen, Jianhua Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SEED, a self-evolving on-policy distillation framework that converts completed on-policy trajectories into hindsight skills and distills them back into the policy, directly addressing the supervision gap in outcome-based RL for LLM agents.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14777)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han

**机构**: NAVER AI

**💡 亮点 (Highlight)**: Proposes a novel on-policy distillation method using a delta signal (difference between teacher and base model) to transfer reasoning capabilities, showing strong empirical gains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15161)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ziyang Cai, Xingyu Zhu, Yihe Dong, Yinghui He, Sanjeev Arora

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel latent reasoning architecture (T2MLR) that fuses cached middle-layer representations across tokens, enabling persistent intermediate computation with minimal overhead and strong math reasoning gains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15178)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Bowei He, Yankai Chen, Xiaokun Zhang, Xue Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Branching Policy Optimization (BPO), a novel RL algorithm for LLM agents that leverages deterministic sandbox snapshots to construct a shared-prefix rollout tree, achieving lower variance and improved success rates on agent benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14171)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a continuous-time RL framework for fine-tuning discrete diffusion models, enabling reward-driven optimization with intermediate rewards and a unified perspective on policy optimization in masked diffusion LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14522)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haran Raajesh, Kulin Shah, Adam Klivans, Philipp Kr\"ahenb\"uhl

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel two-stage action MDP and policy gradient for masked diffusion language models, directly advancing RL for LLMs with a new training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.15200)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Joe Logan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free per-token halting rule for depth-recurrent transformers that exploits fixed-point convergence, directly advancing latent reasoning by enabling variable-depth internal computation without explicit CoT.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14427)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jungseob Lee, Seungyoon Lee, Suhyune Son, Dongyub Jude Lee, Sungbin Han, Sugyeong Eo, Heuiseok Lim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that answer-conditioned chain-of-thought generation degrades verifiable-reasoning distillation, with a clear mechanism and practical takeaway for generating answer-blind data.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14552)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Harikrishnan P M, Goutham Vignesh, Ganesh Parab, Saisubramaniam Gopalakrishnan, Vishal Vaddina, Varun V, Rohit Agrawal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO to multimodal document QA without intermediate reasoning tokens, revealing reasoning suppression and grounding divergence, which is a strong match for RL-for-LLMs with a novel reward design and training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14682)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Minghao Liu, Yu Wang, Jiayun Wang, Wei Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a pairwise validator as a drop-in replacement for scalar reward in self-evolving agent loops, directly relevant to RL for LLMs via reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14408)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenchang Gao, Pingyue Sheng, Lanlan Qiu, Yunfei Ma, Jian Zhao, Baicheng Chen, Kangda Wang, Yuyang Tian, Shunqiang Mao, Tianxing He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces step-level human preference learning via DPO for LLM-based generative agents, directly improving long-horizon decision quality with a new training signal.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14485)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shiyu Yuan, Sourav Sanjukta Bhabesh, Zhe Wang, Dmitriy Bespalov, Wesley Rose, Huzefa Rangwala

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new RL method (GRPO-lite with BDA) for multi-image analytical reasoning in VLMs, combining synthetic data generation with a reward allocation scheme that strengthens later reasoning steps.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.14333)

---

