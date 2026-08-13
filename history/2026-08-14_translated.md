# 💡 今日研究速览 (Daily Summary)

### On-Policy Distillation & Self-Improvement
A significant cluster of work this week focuses on refining on-policy distillation (OPD) beyond simple imitation. Key insights reveal that while OPD boosts sampling efficiency, it may not inherently expand reasoning capability, prompting new designs like reliability-adaptive reward extrapolation (REOPD) and hybrid-policy self-editing that combine on-policy signals with off-policy rollouts for better composability. The field is also seeing a shift toward test-time alternatives, such as strong-to-weak capability transfer via harnesses, which offers a compelling inference-time substitute for traditional distillation loops.

### RL for LLMs: Reward Design & Stability
Reinforcement learning for LLMs is maturing with a focus on principled reward engineering and training stability. Novel approaches include multi-objective process rewards for spatial reasoning (SCOUT), context-calibrated preference optimization to mitigate hallucination, and simple yet effective tricks like Rubric Dropout to prevent reward hacking. A critical theme is addressing capability degradation during rollout RL, with new geometric constraints (GCPO) and subspace-projection methods providing a principled way to maintain model integrity while optimizing for specific objectives.

### Agents & Long-Horizon Reasoning
Agentic systems are advancing toward more sophisticated reflection and knowledge management. The introduction of global-perspective distillation (LoongReflect) for search agents demonstrates how to boost long-horizon reflection by leveraging outcome-based RL (GRPO) with a global view. Complementing this, training-free self-reflection loops for code-based reasoning and uncertainty-driven active clarification frameworks (CLAIM) are pushing agents toward more autonomous and reliable decision-making in complex, multi-step tasks.

### Multimodal & Specialized Reasoning
Multimodal and domain-specific applications are seeing targeted RL innovations. For MLLMs, context-calibrated DPO directly tackles object hallucination, while structured chain-of-thought with multi-objective process rewards unlocks enhanced spatial reasoning. The application of GRPO with task-aligned structured rewards is also yielding impressive results in specialized domains, such as financial advice generation and European real estate analysis, where specialist-decomposed agent frameworks are outperforming commercial LLMs under rigorous causal evaluation.

### Architecture & Efficiency
A notable architectural contribution retrofits recurrent depth into pretrained LLMs, offering a latent reasoning pathway that extrapolates more efficiently than scratchpad-based models. This work, alongside on-policy self-distillation for multi-dialect ASR, highlights a broader trend toward efficiency and parameter-economical training. The ASR work specifically addresses train-test mismatch by training on the model's own decoded prefixes, a clever approach that preserves performance on the source domain while mastering new ones.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 9/10

**作者**: Mark Shapiro

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly introduces a latent reasoning architecture by retrofitting recurrent depth into a pretrained LLM, demonstrating extrapolation and efficiency gains over scratchpad models.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11233)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xinmu Ge, Zizhuo Zhang, Yu Huang, Jianing Zhu, Lin Yuan, Wanli Gu, Weichang Wu, Weiran Huang, Xiaolu Zhang, Bo Han, Jun Zhou, Jiangchao Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a critical analysis of on-policy distillation, showing it primarily improves sampling efficiency rather than expanding reasoning capability, with implications for distillation loop design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11829)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yang Sun, Lichao Ma, Houyuan Qin, Yuxin Liu, Hanyang Lu, Yao Zhu, Pinlong Cai, Guohang Yan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reliability-adaptive reward extrapolation framework for on-policy distillation, directly improving the target topic with a new token-level adaptive coefficient.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11698)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a pairwise-aware inclusion reweighting estimator for RLVR that corrects bias in adaptive rollout allocation, improving RL training efficiency and accuracy.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11368)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhixin Zhang, Xinke Jiang, Zhibang Yang, Weixuan Xu, Guohong Qiu, Xu Chu, Junfeng Zhao, Yasha Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training framework combining global-perspective distillation with outcome-based RL (GRPO) for reflection in search agents, directly addressing on-policy distillation and RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11967)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Kai Yang, Jingwei Xu, Wanyu Wang, Kai-Yuan Guo, Zhenbo Yu, Yi Wang, Yu Qiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel geometric constraint (GCPO) for on-policy RL post-training of LLMs, directly addressing stability and capability degradation with a principled subspace-projection method.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11674)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianci Liu, Zihan Dong, Tianchun Li, Yi-Chung Chen, Qiming Cao, Xingchen Wang, Shiyang Wang, Zichen Miao, Linjun Zhang, Haoyu Wang, Jing Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces hybrid-policy self-editing that combines on-policy distillation with off-policy rollouts to improve knowledge editing composability, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11660)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianze Yang, Liang Wu, Ruitong Sun, Yucheng Shi, Yanqiao Wang, Mayank Darbari, Ninghao Liu, Jin Sun, Liangjie Hong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free self-reflection loop where the model evolves its own code-based reasoning skills, directly improving reasoning via on-policy self-improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11292)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Po-Jen Ko, Che-Cheng Wu, Hung-Chun Hsu, Li-Yang Chang, Chuan-Ju Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel RL-trained polarizer that intervenes on prompt context to reduce confident misreading of misleading evidence, directly improving LLM reliability via a new reward design and training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11922)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Cheng Qian, Wenting Zhao, Liangwei Yang, Heng Wang, Jielin Qiu, Heng Ji, Silvio Savarese, Huan Wang, Shelby Heinecke

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces test-time strong-to-weak capability transfer via harnesses, a novel inference-time alternative to on-policy distillation that significantly boosts weaker model performance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12307)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Byungoh Ko, Jinyoung Park, Jongha Kim, Jeehye Na, Jaewon Cho, Hyunwoo J. Kim

**机构**: MLV Lab (likely Seoul National University)

**💡 亮点 (Highlight)**: Proposes a new DPO variant with a context-calibration objective that directly reduces object hallucination in MLLMs, a concrete reward/objective design for RL-based alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12158)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kuangzhao Yang, Ziliang Zhao, Zhicheng Dou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an uncertainty-driven framework for active clarification learning that combines entropy-based synthetic data generation with SFT and GRPO, directly contributing to RL-for-LLMs with a novel reward design and training pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11631)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zile Zhou, Huining Yuan, Weichen Zhang, Xinlei Chen, Xiao-ping Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a structured CoT framework with multi-objective process rewards and tailored advantage estimation for RL training, directly advancing RL-for-LLMs with a novel reward design and credit assignment method for spatial reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12220)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pardis Taghavi, Santosh Bhavani

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a specialist-decomposed LLM agent framework and uses GRPO with task-aligned structured rewards to improve financial judgment, directly contributing to RL-for-LLMs with a novel reward design and training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11381)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuiyuan Wang, Bingshen Mu, Pengshen Zhang, Chengyou Wang, Yujie Liao, Chengdong Liang, Binbin Zhang, Qiangze Feng, Lei Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an on-policy self-distillation loop for ASR that trains on the model's own decoded prefixes to improve dialect recognition while preserving Mandarin accuracy, directly addressing train-test mismatch.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11898)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haobo Zhang, Kelong Mao, Sulong Xu, Simiu Gu, Zhicheng Dou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a framework combining RL over verifiable outcomes with feedback-aware on-policy distillation to learn from real user interaction logs, directly advancing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11604)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Minglai Yang, Xinyu Guo, Utkarsh Tyagi, Mian Zhang, Razvan Dumitru, Sunjie Hou, Yunzhong He, Daniel Yue Zhang, Ying Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Rubric Dropout, a simple reward design modification that mitigates reward hacking in rubric-based RL for LLMs, directly improving RL-for-LLMs methodology.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11669)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ofir Ben Shoham, Shrutendra Harsola, Vignesh Subrahmaniam, Shravan Mohan, Yakov Gazman, Oded Vainas

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO with a novel LLM-as-a-judge reward and a causal audit to improve financial advice generation, directly advancing RL-for-LLMs with a new reward design and evaluation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11787)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Vu Duc Anh, Nhat M. Hoang, Do Xuan Long, Cong-Duy Nguyen, Ponhvoan Srey, Luu Anh Tuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage RL framework (SFS-DPO) that uses step-level preference optimization and explicit self-correction training, directly advancing RL-for-LLMs with a new training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.11573)

---

