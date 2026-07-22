# 💡 今日研究速览 (Daily Summary)

### Reinforcement Learning for LLMs
A major cluster of papers today pushes the boundaries of RL for LLMs, addressing foundational challenges in reward design, credit assignment, and training stability. **ISO**introduces a novel RLVR-native optimization framework that improves reasoning and coding by optimizing spectral frames, offering a principled alternative to standard policy optimization.**RRPO**generalizes GRPO to non-verifiable tasks by using reference-relative contrastive advantages from stratified rollouts, broadening the applicability of RL.**S2T-RLHF**tackles credit assignment in preference-based RLHF with a hierarchical sentence-to-token reward decomposition, while**Off-Context GRPO**leverages privileged information to provide learning signals on hard problems where standard RLVR fails.**GEAR**addresses repetitive copying in long-context reasoning by augmenting accuracy rewards with grounding and distractor penalties.**Measuring Reward-Seeking**reveals a critical insight: RL training can inadvertently increase alignment with grader preferences over user intentions, a finding with significant implications for alignment research. The**Parallel Shapley**framework offers a principled method for path-level reward attribution in multi-path reasoning, and**Stale but Stable**proposes staleness-adaptive trust regions to stabilize asynchronous RL training. Together, these works signal a maturation of RL for LLMs, moving beyond simple reward functions toward more sophisticated, robust, and generalizable training paradigms.

### On-Policy Distillation
On-policy distillation (OPD) emerges as a major theme, with several papers proposing novel frameworks that go beyond simple imitation.**AdaFlash**introduces OPD using reverse-KL divergence for diffusion drafters in speculative decoding, directly addressing the distribution mismatch problem.**One Student, Many Teachers**proposes a multi-task OPD method using soft-prompt teachers that preserves student geometry and avoids catastrophic forgetting.**Contrastive On-Policy Distillation (COPD)**uses token-level advantage signals from contrasting instructions to encourage concise reasoning, offering a fine-grained distillation signal.**H²SD**proposes a hybrid hindsight self-distillation framework that switches between teacher-conditioned objectives based on trajectory correctness, eliminating the need for an external teacher. These works collectively demonstrate that OPD is evolving from a simple knowledge transfer technique into a powerful tool for shaping model behavior with precise, on-policy signals.

### Reasoning with Latent and Continuous Representations
A fascinating trend is the exploration of latent and continuous reasoning mechanisms.**MUX**proposes lossless multiplexed tokens for continuous reasoning, providing a strong theoretical foundation for latent Chain-of-Thought (CoT).**LatentMT**presents the first systematic study of latent-reasoning looped language models for machine translation, showing strong performance with compact models.**Reasoning Fine-Tuning Induces Persistent Latent Policy States**models reasoning as a switching dynamical system, revealing that fine-tuning globally reorganizes latent dynamics, with practical applications in causal interventions and pruning. These papers suggest a paradigm shift away from discrete token-by-token reasoning toward more efficient, continuous latent reasoning spaces, potentially unlocking new capabilities in compact models.

### RL for Specialized Domains
The application of RL to specialized domains continues to expand with principled frameworks.**Adopting RLVR for Molecular Generation**provides a clean instantiation of GRPO for molecule generation, directly matching the verifiable reward criterion.**DobicVLM**applies GRPO with clinically-grounded programmatic rewards for chest X-ray report generation, demonstrating how domain-specific rewards can align VLMs with medical requirements.**Search-on-Graph-R1**trains a compact 8B model for knowledge graph navigation using an SFT+RL pipeline with frontier teacher scaffolding.**OPD-IAD**proposes an on-policy self-distillation framework for industrial anomaly detection, distilling privileged defect evidence onto the model's judgment trajectory.**Beyond Score Prediction**introduces a unified RL framework for essay scoring and feedback generation with rubric-based rewards. These works illustrate the versatility of RL frameworks when paired with carefully designed, domain-specific reward functions.

### Step-Level and Fine-Grained Credit Assignment
Improving credit assignment at the token and step level is a key focus.**SSC-GRPO**assigns step-level rewards via self-consistency scores across rollouts to mitigate reasoning hallucinations, directly targeting the problem of incorrect intermediate steps.**S2T-RLHF**decomposes sentence-level rewards into token-level contributions for stable RLHF.**Parallel Shapley**provides fine-grained path-level reward attribution in multi-path reasoning. The**RFE** component in RLAES offers rubric-based feedback evaluation at a granular level. This collective emphasis on finer-grained credit assignment signals a move away from monolithic reward signals toward more interpretable and effective training signals.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ayhan Suleymanzade, Halil Alperen Gozeten, Michael Bronstein, \.Ismail \.Ilkan Ceylan, Jinwoo Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MUX, a novel method for latent continuous reasoning via lossless multiplexed tokens, directly addressing latent CoT/reasoning with strong theoretical grounding and empirical results.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18264)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Wei-Rui Chen, Samar M. Magdy, Chiyu Zhang, Wenhui Zhu, Zhipeng Wang, Muhammad Abdul-Mageed

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: First systematic study of latent-reasoning looped language models for machine translation, showing strong performance with compact models and analyzing recurrent computation scaling.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18618)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junyao Yang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Ruhan Wang, Xiangxin Zhou, Kishan Panaganti, Haitao Mi, Leowei Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a staleness-adaptive trust region method for stabilizing asynchronous RL for LLMs, directly addressing a key challenge in scalable RL training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18722)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Abir Harrasse, Michael Lan, Hunar Batra, Fateme Hashemi Chaleshtori, Chaithanya Bandi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Models reasoning as a switching dynamical system to discover latent policy states, revealing that reasoning fine-tuning globally reorganizes latent dynamics, with causal interventions and pruning applications.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18532)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hanqing Zhu, Wenyan Cong, Zhizhou Sha, Sagnik Mukherjee, Xinyuan Song, David Gonz\'alez-Mart\'inez, Xiaoxia Wu, Yuandong Tian, Shiwei Liu, David Z. Pan, Zhangyang "Atlas" Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Isospectral Optimization (ISO), a novel RLVR-native optimization framework with offline and online instantiations that improves reasoning and coding accuracy by optimizing spectral frames while keeping base spectra fixed.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19331)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Wentao Zhang, Haoyu Zhang, Xinke Jiang, Yuxuan Cheng, Yuhan Pan, Miao Li, Zhipeng Qiao, Tao Feng, Zhen Tao, Dengji Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Parallel Shapley, a novel RL framework using Shapley values for fine-grained path-level reward attribution in multi-path reasoning, directly improving RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18979)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Axel H{\o}jmark, J\'er\'emy Scheurer, Evgenia Nitishinskaya, Felix Hofst\"atter, Jason Wolfe, Theodore Ehrenborg, Bronson Schoen, Alexander Meinke

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel method (Contrastive Synthetic Document Finetuning) to measure reward-seeking behavior in RL-trained LLMs, revealing that RL training can increase alignment with grader preferences over user/developer intentions.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18966)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuimu Chen, Jing Jin, Nan Su, Hongbo Xu, Zebang Cheng, Wenming Yang, Fei Ma, Guijin Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an on-policy self-distillation framework for LVLM-based industrial anomaly detection, distilling privileged defect evidence onto the model's own judgment trajectory.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18850)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lizhe Fang, Weizhou Shen, Tianyi Tang, Yisen Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GEAR, a reward shaping method that augments accuracy with grounding and distractor penalties to reduce repetitive copying in long-context LLM reasoning, validated via RL training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19345)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mingxuan Ouyang, Hao Lan, Wanyu Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a principled RLVR framework with GRPO for molecular generation, directly matching the RL-for-LLMs criterion with a verifiable reward design and on-policy optimization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19044)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiye Cai, Yichuan Ma, Linyang Li, Peiji Li, Yongkang Chen, Qipeng Guo, Yicheng Zou, Tao Gui, Xiaocheng Feng, Bing Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hybrid hindsight self-distillation framework that uses trajectory correctness to switch between two teacher-conditioned objectives, improving reasoning via on-policy distillation without an external teacher.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18955)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xuefeng Jin, Jiashuo Zhang, Teng Cao, Bin Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RLAES, a unified RL framework for essay scoring and feedback generation with a novel rubric-based reward design (RFE) and adaptive gated feedback optimization (AGFO), directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19219)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu-Yang Qian, Hao-Cong Wu, Chen Chen, Jiacheng Sun, Zhenhua Dong, Peng Zhao, Zhi-Hua Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces AdaFlash with on-policy distillation (OPD) using reverse-KL divergence for diffusion drafters in speculative decoding, directly addressing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19223)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Priyank Agrawal, Ankur Samanta, Shervin Ghasemlou, Jalaj Bhandari, Kavosh Asadi, Daniel Jiang, Aditya Modi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Off-Context GRPO, a new RLVR variant that uses privileged guidance to provide learning signal on hard problems where standard RLVR fails, with an importance-corrected objective.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19313)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Thanni Adewuyi, Angelica Obayi, Andem Aniekan, Samuel Okoko, Angel Ezendu, Ephraim Usani, Ademide Animasaun, Philip Chibundu, Christian Maurice, Mary Donald Essien, Oluwaseun Odunsi, Oluwasegun Oguntuase, Abiodun Adereni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO with clinically-grounded programmatic rewards for VLM alignment in medical report generation, directly contributing a new RL reward design and training pipeline for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18988)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wei Chen, Guanghui Zhu, Yafei Li, Limin Wang, Yihua Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hierarchical sentence-to-token reward decomposition framework for stable RLHF, directly addressing credit assignment in preference-based RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18258)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaomeng Hu, Jiaqi Hu, Hao Chen, Qi Zhang, Zhanming Shen, Wentao Ye, Junbo Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SSC-GRPO, a new RL method that assigns step-level rewards via self-consistency scores across rollouts to mitigate reasoning hallucinations, directly advancing RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18915)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jia Ao Sun, Hao Yu, Fengran Mo, Zhan Su, Yuchen Hui, Bang Liu, Jian-Yun Nie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL pipeline (SFT+RL) to train a compact 8B model for knowledge graph navigation, using a frontier teacher scaffolded with gold SPARQL queries to generate grounded on-policy trajectories.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18481)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yingzi Ma, Zichen Zhu, Ming Jiang, Chaowei Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-task on-policy distillation method using soft-prompt teachers that preserves student geometry and avoids forgetting, directly matching the on-policy distillation criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18293)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuxin Xiong, Xunyi Jiang, Rohan Surana, Xintong Li, Sheldon Yu, Nikki Lijing Kuang, Ryan A. Rossi, Jingbo Shang, Tong Yu, Julian McAuley, Junda Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RRPO, a new RL method for LLMs that generalizes GRPO to non-verifiable tasks using reference-relative contrastive advantages from stratified conditional rollouts.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.18470)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiacheng Ruan, Jun Tang, Wenzhen Yuan, Ting Liu, Shuai Bai, Dayiheng Liu, Zhibo Yang, Yuzhuo Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes COPD, a contrastive on-policy distillation framework that uses token-level advantage signals from contrasting instructions to encourage concise reasoning, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.19046)

---

