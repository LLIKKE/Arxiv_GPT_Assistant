# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
The field is experiencing a surge in methodological refinements aimed at overcoming fundamental bottlenecks in policy optimization. A critical theoretical advance demonstrates the impossibility of achieving both unbiased and length-invariant optimization under outcome-reward GRPO, formalizing a core tradeoff between GRPO and its length-normalized variant. To address practical credit assignment, several works propose novel reward mechanisms: turn-level credit signals derived from game solvers, token-level rubric-guided weighting via counterfactual replay, and episode-wise rewards for long-horizon agentic reasoning. For long-horizon tasks specifically, a new method uses first-visit observation coverage to break credit traps, while another stabilizes training by adaptively controlling the discrepancy between training and inference. A particularly notable trend is the coupling of RL with game-theoretic concepts, including swap-regret losses that yield equilibrium guarantees and interactive reward agents that verify environment state for GUI tasks. Finally, critical practical insights emerge regarding the impact of final pretraining data on post-training RL responsiveness and the identification of reproducible failure modes in small-scale agent training.

### On-Policy Distillation
On-policy distillation (OPD) is rapidly maturing into a robust paradigm for improving student models through teacher guidance, with a strong focus on handling temporally extended and reasoning-heavy tasks. A key development is the use of teacher handoff at detected prefix failures, enabling efficient trajectory-relayed distillation that reduces training length while improving reasoning. For continuous-time models, a novel objective matches student and reference trajectories from student-visited states, deriving a temporally weighted velocity-matching objective that outperforms standard KL-based approaches. The role of outcome-confounded local supervision is critically examined, revealing that agreement-on-failure dominates token-level divergence and that current probes cannot fix this issue, pointing to a fundamental limitation. Several works also explore self-distillation and data synthesis, including a time-truncation harness for temporal reasoning data, noisy student self-distillation for VLMs using prediction discrepancies, and rollout-conditioned distillation for knowledge injection with retention guarantees. A unifying theme is the shift from simple imitation to more nuanced, credit-aware, and failure-informed forms of supervision.

### Agents
Agentic research is increasingly focused on improving the reliability and efficiency of long-horizon tool-use and reasoning. A prominent direction is the unification of agent and speculative decoding through joint RL, where a single model learns to predict its next tool call during rollout, directly reducing inference latency. For complex, multi-step tasks, progress-conditioned group policy optimization breaks credit traps by assigning advantages based on first-visit observation coverage, enabling effective learning in environments with sparse rewards. Personalized agentic reasoning is tackled by optimizing over long action horizons with episode-level rewards, moving beyond per-step or per-turn credit assignment. The interactive reward agent paradigm introduces environment-state verification as a reward signal for GUI agents, demonstrating a principled way to automate reward design for real-world tasks. A common thread is the need for more sophisticated credit assignment and reward structures that go beyond simple outcome rewards, especially as agents are deployed in increasingly open-ended and long-horizon settings.

### Compression & Efficiency
Efficiency-focused research is making strides in reducing both training and inference costs without sacrificing capability. A lightweight black-box adaptation method learns a logit-bias vector via a KL-regularized RL objective, enabling model customization without any weight modification, which is particularly valuable for API-accessed models. For structured reasoning, a latent-reasoning framework localizes recurrent computation to a narrow decoder interval, significantly reducing inference latency while maintaining accuracy on complex reasoning tasks. In the data domain, a data-centric preference optimization method uses multi-evaluator agreement and process-critic correction to achieve strong alignment with a fraction of the typical training data, demonstrating that careful data selection can dramatically improve efficiency. These approaches collectively emphasize that efficiency gains are being achieved not just through architectural changes, but through smarter optimization objectives and data utilization strategies.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yu Wang, Yi-Kai Zhang, Wentao Shi, Ziang Ye, Yuchun Miao, Yueqing Sun, Qi Gu, Xunliang Cai, Lan-Zhe Guo, Han-Jia Ye, Fuli Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CAST, which converts game solver state value changes into turn-level credit signals for RLVR, and shows equivalence to on-policy distillation from the solver, directly contributing to both RL for LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25308)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Fei Ding, Yongkang Zhang, Yuhao Liao, Zijian Zeng, Huiming Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proves an impossibility theorem for unbiased and length-invariant policy optimization under outcome-reward GRPO, revealing a fundamental tradeoff between GRPO and Dr. GRPO.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23364)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Haolei Xu, Xiaowen Xu, Haiwen Hong, Zixuan Ni, Hongxing Li, Yiwen Qiu, Weiming Lu, Yongliang Shen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Relay-OPD, a novel on-policy distillation method that uses teacher handoff at detected prefix failures to improve reasoning and reduce training length.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.26057)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Kaiyang Ye, Yuan Ge, Junxiang Zhang, Bei Li, Ziming Zhu, Haishu Zhao, Xiaoqian Liu, Chenglong Wang, Jingbo Zhu, Zhengtao Yu, Tong Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FlowCTS, a novel on-policy distillation method for flow models that matches student and reference trajectories from student-visited states, deriving a temporally weighted velocity-matching objective and demonstrating clear improvements over vanilla KL-based OPD.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24522)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jiabao Ji, Yujian Liu, Li An, Rohit Jain, Gungor Polatkan, Siyu Zhu, Shiyu Chang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a joint agent-speculator RL method that unifies agent and speculator in a single model, using on-policy rollouts to improve next tool-call prediction latency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25816)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chanwoo Park, Asuman Ozdaglar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a swap-regret loss for training self-attention models, directly connecting RL-for-LLMs via regret-based objectives that yield game-theoretic equilibrium guarantees.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23333)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ofek I. Cohen, Lior Shani, Aviv Rosenberg, Ankur Samanta, Tal Wagner, Yonathan Efroni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a black-box method to learn a logit-bias vector via a KL-regularized RL objective, enabling lightweight LLM adaptation without weight modification.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22837)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zibin Meng, Zhenyu Zhao, Chunqiang Run

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes AdaKP, an online adaptive knowledge-point selection method for reasoning-oriented RL with verifiable rewards, introducing an entropy proxy and lightweight mechanisms to dynamically select which hints to inject during RL training, directly improving competition math benchmarks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24833)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Cen Lu, Yung-Chen Tang, Andrea Cavallaro

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that the final pretraining data window strongly shapes how a model responds to subsequent RL/DPO post-training, revealing a critical and overlooked factor for alignment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25063)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Bo-Wen Zhang, Junwei He, Wen Wang, Song-Lin Lv, Wentao Ma, Rongyi Lin, Shuhan Zhong, Lan-Zhe Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CoRT, a token-level credit weighting method for rubric-conditioned GRPO using counterfactual replay, directly improving RL for LLMs with a novel reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25659)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kaibing Yang, Guangfeng Cai, Shengtian Yang, Shuo He, Yu Li, Mengyi Liu, Pengwei Chen, Jun Xu, Lei Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ProGPO, a new group-based policy optimization method for LLM agents that uses first-visit observation coverage to assign advantages and break credit traps in long-horizon tasks, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22724)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wanxu Cai, Zhengyu Chen, Huaisheng Zhu, Wei Wang, Jingang Wang, Qiang Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a time-truncation harness for on-policy distillation of temporal search and reasoning data, enabling efficient self-improvement of LLMs for future prediction.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25554)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies and fixes three reproducible failure modes in PPO-based RL for small LLMs, proposing a capacity-headroom hypothesis and a robust training pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25091)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiaqi Zhang, Tong Chen, Junliang Yu, Quoc Viet Hung Nguyen, Hongzhi Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Episode-wise GRPO (ESPO), a novel RL method for personalized agentic reasoning that optimizes over long action horizons with episode-level rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25369)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yan Hong, Wei Li, Kedong Xiu, Jun Lan, Shuheng Zhou, Zhongcai Lyu, Huijia Zhu, Weiqiang Wang, Jianfu Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a rollout-conditioned online distillation objective (RoCo-ACE) for knowledge injection that uses likelihood contrast and anchored correction to improve retention while injecting new knowledge.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24771)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yutong Chen, Shouqian Shi, Xinran Liu, Haochen Wang, Jiaying Wang, Tianxing Xu, Yuanxi Wang, Zirui Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Penelope, a latent-reasoning framework that localizes recurrent computation to a narrow decoder interval, reducing inference latency while maintaining accuracy on structured reasoning tasks.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25915)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chenrui Shi, Yuwei Wu, Yang Liu, Ruining Feng, Zirui Shang, Zhi Gao, Lifeng Fan, Che Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an interactive reward agent (IRA) for GUI task evaluation that verifies environment state, and demonstrates its use as a reward signal for RL training of GUI agents, directly matching RL-for-LLMs criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25904)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenwu Fan, Qihong Lin, Zhijie Xia, Zhuo Zheng, Sihao Wang, Qiang Chen, Liangsheng Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ACRL, an adaptive control method to stabilize RL training for LLMs by managing training-inference discrepancy, directly addressing a core RL-for-LLMs challenge.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24062)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuai Wang, Daoan Zhang, Zhe Tang, Hao Cheng, Jiaheng Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes NOPD, a novel on-policy self-distillation method for VLMs that uses prediction discrepancies between clean and corrupted inputs as a self-supervision signal, directly matching the on-policy distillation criterion.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23125)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guoqing Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a diagnostic analysis of outcome-confounded local supervision in on-policy distillation, revealing that agreement-on-failure dominates student-teacher token-level divergence and that current training probes cannot fix it.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23731)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhengtao Yao, Runhao Li, Xupeng Chen, Jiayi Cheng, Chenqian Le, Michael Yue, Siheng Wang, Haoyan Xu, Yuqi Li, Chenhao Wei, Zhengdao Li, Rongchao Zhang, Guang Yang, Yidong Wang, Junhao Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a data-centric on-policy preference optimization method (DMAPO) that uses multi-evaluator agreement and process-critic correction to select high-confidence training examples, directly improving alignment with a small curated set.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.25136)

---

