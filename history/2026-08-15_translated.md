# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
Reinforcement learning for language models is rapidly evolving beyond simple outcome-based rewards. A clear trend is the move toward *denser* and *more granular* supervision signals. Papers like CrEST and SSPO (Step-Level Self-Distilled Policy Optimization) shift credit assignment from sparse, trajectory-level outcomes to step-level advantages, directly addressing the temporal credit assignment problem in multi-turn tool-use and deep search agents. Concurrently, reward design is being refined; the "Reasoning Jury" proposes a multi-model consensus mechanism for evaluating reasoning traces, while "From Refuse to Richness" introduces rubric-based rewards that decompose long-form generation quality into grounding and coverage components, mitigating the pitfalls of monolithic reward models. This collective focus on signal fidelity—whether through step-level granularity or rubric decomposition—marks a significant maturation of the RLHF/RLVR pipeline.

### On-Policy Distillation & Self-Improvement
A dominant theme today is the convergence of RL and self-distillation, where a frozen or privileged teacher provides supervision on the student's own (on-policy) rollouts. LOPD (Latent On-Policy Self-Distillation) makes the teacher's privileged context learnable end-to-end, while CROP introduces a counterfactual criterion to selectively allocate token-level supervision where it matters most. This paradigm is extending beyond text LLMs into multimodal and embodied domains: HPSD adapts the concept for text-to-video diffusion, and FIRE-VLA applies it to vision-language-action models for autonomous driving. Furthermore, the self-improvement loop is becoming more autonomous and diversity-aware. DIVE and SkillEvo push frozen or evolving models to generate their own training data through verifier feedback and multi-turn interaction gradients, while "Beyond the Best Guess" offers a complementary approach using evolution strategies on weights to explicitly preserve solution diversity, directly countering the coverage collapse often seen in standard RL.

### Agents & World Models
Agentic systems are tackling the scalability bottleneck of environment interaction. WMRL (World Model RL) is a standout contribution, proposing to replace costly real-world execution with a learned world model for AutoResearch agents, complete with debiasing and denoising techniques to mitigate the inherent inaccuracies of simulated environments. This represents a critical step toward training agents that can reason and plan over long horizons without prohibitive computational costs. Complementing this, the Intern-S2-Preview model demonstrates a practical, unified post-training pipeline that integrates multi-task and agentic RL with on-policy distillation, offering a blueprint for stable, large-scale agent training. The synergy between learned simulators (WMRL) and robust training recipes (Intern-S2) suggests that the field is converging on a scalable recipe for complex, multi-step agentic reasoning.

### Multimodal & Safety Alignment
Multimodal research is moving from capability-focused training to behavioral alignment. The paper on hybrid-thinking MLLMs is particularly noteworthy, introducing a response-pattern reward model to explicitly align the model's thinking and non-thinking modes, ensuring that the new reasoning capabilities don't degrade conversational quality. In safety, HiRoute offers a parameter-efficient alternative to full fine-tuning by using a hierarchical prompt-tuning framework with a router and preference optimization, providing a more targeted approach to safety alignment. This shift towards fine-grained behavioral control—managing *how* a model responds, not just *what* it answers—indicates a maturing understanding of the post-training landscape.

### Latent Reasoning & Efficiency
Efficiency and architectural innovation are being driven by the need to handle long reasoning traces. Thought-Aware KV Cache Compaction and ReconSpan both tackle the computational cost of latent reasoning from complementary angles. The former exploits the structure of chain-of-thought (CoT) to adaptively prune the KV cache, while the latter learns a reconstruction-guided, input-dependent tokenization scheme to compress text into denser latent representations. StateBridge offers a novel, training-free method for aligning hidden states across models in multi-agent latent communication, bypassing the need for expensive fine-tuning. These works collectively point toward a future where reasoning is not only deeper but also more computationally efficient and structurally communicative.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Guibin Zhang, Jiayang Lyu, Ran Sun, Xinlei Yu, Haoyu Zhao, Qibing Ren, Shuicheng Yan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Latent On-Policy Self-Distillation (LOPD), making the teacher's privileged context learnable end-to-end and providing dense token-level supervision on the student's own trajectories, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13040)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li, Huiyuan Chen, Haiyang Zhang, Chenlei Guo, Jingrui He, Zhenyu Liao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes World Model RL (WMRL) to replace environment execution with a learned world model for AutoResearch agents, addressing a key RL scaling bottleneck with debiasing and denoising mitigations.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12564)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zechuan Wang, Siyuan Lu, Hongxuan Zhang, Linjian Mo, Chenyi Zhuang, Leilei Gan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CrEST, a hierarchical credit assignment framework combining verifier-bounded RL with on-policy self-teacher distillation for multi-turn tool-use agents, directly advancing both RL-for-LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13179)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yubo Zhang, Xinhong Ma, Zezhong Tan, Ziqiang Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an instance-level adaptive routing between GRPO and privileged self-distillation, directly addressing a core RL-for-LLMs training recipe with a novel capability-dependent teacher-reliance mechanism.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12957)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Enhan Li, Junhao He, Hongyang Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a counterfactual relevance criterion for selective on-policy distillation, directly improving token-level supervision allocation in LLM post-training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13387)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Haoze Wu, Chuqiao Kuang, Tianyi Zhuang, Xiaoguang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Step-Level Self-Distilled Policy Optimization (SSPO) with Evidence Anchors, a novel on-policy distillation method that converts teacher-student disagreement into step-level advantage weights within GRPO for deep search agents, directly advancing on-policy distillation for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12764)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yang Liu, Bin Chong, Chongyang Zhang, Hao Zheng, Jiayu Liang, Xu Kefu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a thought-aware KV cache compaction method that exploits CoT structure for adaptive budget allocation, directly addressing latent reasoning efficiency.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12331)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jiazi Bu, Pengyang Ling, Yujie Zhou, Yibin Wang, Yuhang Zang, Xuanlang Dai, Shengyuan Ding, Tianyi Wei, Xiaohang Zhan, Jiaqi Wang, Tong Wu, Dahua Lin, Xingang Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Hybrid-Policy Self-Distillation, an on-policy distillation framework for TI2V diffusion models that combines off-policy teacher anchors with on-policy student rollouts to improve base generation ability.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13205)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Siheng Xiong, Ali Payani, Oguzhan Gungordu, Faramarz Fekri

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a diversity-driven skill evolution framework for frozen LLMs, using verifier feedback and on-policy self-improvement loops, directly relevant to on-policy distillation and RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12486)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Qianxi Yan, Chunrong Chen, Jiuzhou Zhao, Min Zhang, Yongzhou Xu, Xiaochuan Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-renewing evolution loop for agent skills driven by multi-turn interaction feedback, with a governance layer to repair degradation, directly addressing on-policy distillation and self-improvement from model-generated trajectories.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13120)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Conor F. Hayes, Elliot Meyerson, Kajetan Schweighofer, Roberto Dailey, Babak Hodjat, Risto Miikkulainen, Xin Qiu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes evolution strategies as a post-training method that directly optimizes weight-space perturbations to preserve solution diversity and improve pass@k, contrasting with RL's coverage collapse.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12679)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Hao Dou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a failure-informed self-evolution framework combining GRPO with on-policy self-distillation from a frozen teacher copy, directly targeting RL for LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13395)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lixing Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a reconstruction-guided adaptive latent tokenization method that directly advances latent reasoning by compressing text into compact continuous representations with input-dependent spans.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12756)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lei Bai, Jiaqi Cao, Chiyu Chen, Guanzhou Chen, Kai Chen, Guangran Cheng, Erfei Cui, Xuanlang Dai, Shengyuan Ding, Shangheng Du, Yanhui Duan, Yue Fan, Youqing Fang, Quan Gan, Yuanyuan Gao, Jiaye Ge, Lixin Gu, Yuzhe Gu, Qipeng Guo, Junjun He, Xin Hong, Ming Hu, Zhouqi Hua, Haian Huang, Junhao Huang, Zixian Huang, Minxi Jin, Lingkai Kong, Alexander Lam, Zehao Li, Zonglin Li, Tianhao Liang, Dahua Lin, Junyao Lin, Tianyang Lin, Zhouhan Lin, Jiangning Liu, Jin Liu, Kuikun Liu, Wenran Liu, Yifei Liu, Yuhong Liu, Yuhong Liu, Zhoumianze Liu, Ziyan Liu, Ziyu Liu, Haijun Lv, Han Lv, Chengqi Lyu, Le Ma, Ningsheng Ma, Zerun Ma, Haoyang Peng, Runyu Peng, Jifei Shan, Zixin Shang, Kou Shi, Xiang Shi, Qisheng Su, Xuerui Su, Hao Sun, Xiao Sun, Yanan Sun, Yu Sun, Huanze Tang, Yinghao Tang, Wenhui Tian, Zhongbo Tian, Bingli Wang, Haomin Wang, Jiarui Wang, Jingzhi Wang, Rui Wang, Xiquan Wang, Yi Wang, Zhecan Wang, Ziyi Wang, Zun Wang, Rubin Wei, Lianyi Wu, Wen Wu, Yue Wu, Yuhan Wu, Zhenyu Wu, Zijian Wu, Shuhao Xing, Jun Xu, Xingle Xu, Xuenan Xu, Xiangchao Yan, Ziang Yan, Bowen Yang, Danni Yang, Lin Yang, Zhiqi Yang, Qian Yao, Haochen Ye, Peng Ye, Jinhui Yin, Jiashuo Yu, Dingbo Yuan, Fei Yuan, Yuhang Zang, Bo Zhang, Chao Zhang, Chen Zhang, Hongjie Zhang, Junming Zhang, Wenlong Zhang, Wenwei Zhang, Yiming Zhang, Zhuo Zhang, Ziyang Zhang, Haiteng Zhao, Penghao Zhao, Yibo Zhao, Zhonghan Zhao, Zhihang Zhong, Bowen Zhou, Peiheng Zhou, Xin Zhou, Xinyu Zhou, Yunhua Zhou, Dongsheng Zhu, Yicheng Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a unified post-training pipeline combining multi-task RL, agentic RL, and on-policy distillation with practical stability techniques, directly advancing RL-for-LLMs and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13505)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinming Wang, Weinong Wang, Hongming Yang, Yansong Lin, Zheng Ruan, Shangpin Peng, Qiming Peng, Nan Qiao, Fengyuan Lu, Guoqing Ma, Marito Li, Songyang Zhang, Saiyong Yang, Han Hu, Yonglong Tian, Xu-Yao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a response-pattern reward model and RL training with pattern-specific penalties to align thinking and non-thinking modes in hybrid-thinking MLLMs, directly contributing to RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12781)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Fangzhou Chen, Shiji Zhao, Mengyang Wang, Qihui Zhu, Ranjie Duan, Maoxun Yuan, Xingxing Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a hierarchical prompt-tuning framework with a router and preference optimization for safety alignment, directly improving LLM behavior through a new training recipe.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12821)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yudong Wang, Zhe Yang, Wenhan Ma, Rang Li, Qibin Yang, Weimin Xiong, Jiangshan Duo, Liang Zhao, Zhifang Sui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces rubric-based reward design for long-form hallucination RL, directly addressing reward design for RLHF-style training with a novel soft combination of grounding and coverage rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12337)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Congchao Wang, Diwakar Singh, Qiaozi Gao, Spyros Matsoukas, Yang Liu, Mahdi Namazifar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a multi-model jury with moderated consensus to judge reasoning traces, directly improving reward signals for RL and data curation for reasoning LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.12585)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free hidden-state alignment method for latent communication in multi-agent systems, directly advancing latent reasoning/communication with a novel orthogonal transformation approach.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2608.13317)

---

