# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
A significant cluster of papers today focuses on improving reinforcement learning (RL) for large language models, particularly by addressing the quality and efficiency of training signals. A key theme is the refinement of on-policy distillation. Several works analyze the failure modes of naive self-distillation, attributing them to privileged information bias and token-level supervision issues, and propose novel corrections. For instance, **SPOT**introduces sparse probing with outcome-calibrated targets from verifier-scored rollouts, while**OCSD**contrasts replay views to calibrate token rewards. A unifying theoretical insight is proposed by the concept of "counterfactual recoverability," which serves as a principled, outcome-grounded criterion for selectively intervening in or supervising rollouts, showing strong empirical gains. Beyond distillation, other works tackle the core RL loop:**ABSeeker**converts sparse trajectory outcomes into dense step-level rewards for long-horizon tasks, and a recoverability-aware framework proposes adaptive rollout intervention for online RL. Efficiency is also a major focus, with**SpecRoll**accelerating rollout generation via fast-slow verifier feedback and**Fewer Tokens, Smaller Cache**using process rewards to jointly drive KV-cache compression and early stopping. Finally, novel reward designs are emerging, such as a skill-entropy reward for long-horizon reasoning and the**RAD-GRPO**algorithm used in**ToolArtist**to jointly optimize reasoning, tool use, and generation in a unified multimodal policy.

### Agents
Research on LLM agents is increasingly focusing on scalable and cost-effective training paradigms that integrate environment feedback and memory management. A notable trend is the use of environment-derived signals to create verifiable training objectives, as seen in**State2State**, which proposes a mid-training phase that generates objectives from explored states, effectively serving as a scalable initialization for downstream RL. Complementing this,**MemoryCPT**introduces an end-to-end trainable memory pipeline optimized with GRPO to explicitly balance performance against inference cost in long-horizon tasks. Meanwhile,**ABSeeker**provides a fine-grained credit assignment mechanism that is particularly well-suited for training search agents, converting sparse outcomes into dense step-level rewards. Collectively, these works push toward more autonomous and sample-efficient agent training, moving beyond simple imitation to leverage the structure of the environment itself.

### Multimodal & Reasoning
Advancements in multimodal models and reasoning are converging on two fronts: enhancing latent reasoning capabilities and integrating external tools. For video understanding,**DyLaR**introduces a dynamic latent reasoning framework with perception and rationale-supervised latents, using RL-based routing to achieve strong efficiency gains. In parallel, the community is actively probing the fundamental properties of latent reasoning.**Protoreasoning**demonstrates that simple latent-like chain-of-thought mechanisms in tiny transformers can exhibit step-by-step generalization, while a direct study on CoT monitorability asks whether "out-of-sight" reasoning is truly "out-of-mind" by comparing explicit and latent chains under intervention. On the application side,**ToolArtist**presents a fully agentic image generation model that unifies reasoning, tool use, and generation within a single policy, while**Teaching MLLMs to Say No**introduces a calibrated RL strategy to balance a model's refusal ability with its localization accuracy. Complementing these,**OPD-V** extends on-policy self-distillation to the visual domain with modality-balance trust regions, improving reasoning while reducing training costs.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yi Yang, Cong Qin, Xiaodan Liu, Chishui Chen, Qing Dong, Yan Zhang, Cao Liu, Zhao Yang, Lu Pan, Jiaye Lin, Yi Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Observation-Calibrated Self-Distillation (OCSD), an on-policy distillation method that contrasts replay views to calibrate token-level rewards for LLM agent RL training, directly addressing the confounding in privileged replay support.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04788)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Haotian Xia, Zilin Xiao, Junbo Zou, Vicente Ordonez, Hanjie Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Dynamic Latent Reasoning (DyLaR) with perception latents, rationale-supervised reasoning latents, and RL-based adaptive routing, directly advancing latent reasoning with strong efficiency gains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04124)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Sarthak Harne, Chinmay Karkar, Yash Pandya, Ahmed Awadallah, Akshay Nambi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly analyzes and explains the failure of self-distillation (a form of on-policy distillation) as a lone objective, identifying PI bias and token-level supervision issues, with a causal chain and diagnostic metric.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04794)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zikun Qu, Min Zhang, Mingze Kong, Zhiwei Shang, Yikun Ban, Shuang Qiu, Zhongxiang Dai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces SPOT, a novel on-policy distillation method with sparse probing and outcome-calibrated targets, directly improving LLM reasoning via verifier-scored student rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04419)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: De Jiang, Zhengyang Zhang, Kehong Yuan, Shaohua Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces counterfactual recoverability as an outcome-grounded decision variable for selective supervision in on-policy distillation, with strong empirical gains on AIME and GPQA.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04408)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yijun Lu, Rui Ye, Jiajun Wang, Yuwen Du, Tian Jin, Songhua Liu, Siheng Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a fine-grained credit assignment framework (ABC) that converts sparse trajectory outcomes into dense step-level rewards for RL training of long-horizon search agents, directly advancing RL-for-LLMs with a new reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05102)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zheyuan Zhang, Manqing Mao, Hong Wang, Zhuoer Wang, Samson Koelle, Jie Yuan, Yanjun Lin, James Feng, Nikki Lijing Kuang, Yanfang Ye, Wei Niu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a recoverability-aware online contextual-bandit framework for adaptive rollout intervention in critic-free group-based RL, directly improving RL-for-LLM training efficiency and signal quality.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05080)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Qiyuan Zhu, Dezhi Li, Pengyu Cheng, Tianle Chen, Jiacheng Wang, Ruijie Shen, Hao Gu, Sida Lin, Zirui Liu, Jiacheng Liu, Sirui Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a reward-coordinated framework that uses process rewards to jointly drive KV-cache compression, reflection-token penalties, and early stopping, directly improving reasoning efficiency while preserving accuracy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04771)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Nhat Minh Pham, Duy Tung Doan, Thi Duyen Ngo, Vinh Van Nguyen, Khac-Hoai Nam Bui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a speculative rollout engine with fast-slow verifier-feedback adaptation that accelerates RL post-training while preserving the target distribution, directly improving RL-for-LLM efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04962)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Eduardo Valle, Fergal Reid

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces protoreasoning, a simple latent-like CoT mechanism in tiny transformers, directly studying step-by-step reasoning and its generalization, which is highly relevant to latent reasoning research.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04980)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jiahao Zhao, Xiaomin Yu, Zhongxiang Sun, Fengwei Teng, Chengwei Qin, Xiaobin Hu, Jun Xu, Shuicheng Yan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a fully agentic image generation model post-trained with a novel RL algorithm (RAD-GRPO) that jointly optimizes reasoning, tool use, and generation within a unified policy, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04436)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xuanyu Lei, Yiqi Zhu, Chenliang Li, Kaiming Liu, Peng Li, Ming Yan, Jieping Ye, Ya-Qin Zhang, Yang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an environment-derived mid-training method that generates verifiable training objectives from explored states, directly improving LLM agent capabilities and serving as a scalable RL initialization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04934)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yinghui He, Ling Yang, Jiarui Liu, Yongjin Yang, Lechen Zhang, Yingcheng Wu, Zhenfei Yin, Mengdi Wang, Sanjeev Arora

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel RL framework with a skill-entropy reward that directly improves long-horizon cross-skill reasoning, matching the RL-for-LLMs criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05139)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Songxin Lei, Kun Ouyang, Weilin Ruan, Yuqian Wu, Zhijiang Guo, Yushi Sun, Fugee Tsung

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an end-to-end trainable memory pipeline with GRPO-based reward optimization for cost-performance trade-offs in long-horizon LLM agents, directly relevant to RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04843)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pedro Ferreira, Wilker Aziz, Ivan Titov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly investigates monitorability of latent CoT reasoning, a central concern for latent reasoning architectures, comparing explicit vs latent CoT under a hint-based intervention setup.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04928)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Aniri, Jinhe Bi, Peng Liao, Zengjie Jin, Volker Tresp, Fei Shen, Yunpu Ma, Tat-Seng Chua

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces OPD-V, a visual on-policy self-distillation paradigm that uses modality-balance trust regions to select on-policy tokens, directly improving MLLM reasoning and reducing training cost.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.05131)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xuzheng Yang, Jun Ling, Tao Huang, Caiyan Qin, Peng Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a calibrated RL strategy (RC-GRPO) that balances refusal ability and localization accuracy in MLLMs, directly advancing RL-for-LLMs with a novel reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.04698)

---

