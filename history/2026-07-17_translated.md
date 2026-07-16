# 💡 今日研究速览 (Daily Summary)

### RL for LLMs
A significant cluster of papers today pushes the boundaries of reinforcement learning for language models, moving beyond traditional PPO-based fine-tuning. The scaling of verifiable-reward RL to trillion-parameter models in "Ring-Zero" demonstrates that emergent reasoning behaviors can be unlocked at massive scale, while "Where Should RL Post-Training Compute Go?" provides a crucial FLOP-accounting framework to guide resource allocation between model size, search, and learning. Several works introduce novel reward mechanisms: "SIVA-RL" and "CARE-PPO" propose outcome-conditioned visual alignment and confidence-aligned rewards respectively, while "LAPO" and "TRACE" tackle the critical challenge of dense credit assignment in long-horizon and multi-turn settings. "Groc-PO" and the OvisOCR2 technical report further enrich this landscape with grounded preference optimization and multi-component reward designs, collectively indicating a shift toward more sophisticated, task-specific reward structures that can drive pure RL improvement without reliance on SFT.

### Reasoning and Latent Computation
Research on reasoning mechanisms shows a bifurcation between explicit chain-of-thought and latent approaches. "DeepLoop" addresses a fundamental architectural challenge by enabling stable recurrent depth in looped transformers, a key enabler for implicit CoT through residual scaling. "GeoAnchor" advances latent reasoning for 3D spatial understanding with interleaved text-latent representations. On the process supervision front, "Consensus as Privileged Context" introduces label-free self-distillation that converts consensus among reasoning paths into token-level supervision, offering a practical alternative to expensive human annotation. "LAPO" complements this by providing self-generated process rewards for multi-turn search reasoning, collectively suggesting that the field is converging on methods to extract rich supervisory signals from the model's own outputs.

### Distillation and Compression
The theme of efficient model improvement through distillation emerges strongly, particularly in the context of on-policy methods. "ShortOPD" directly addresses a critical gap by proposing a short-to-long on-policy distillation schedule that recovers pruned LLMs, training on the model's own rollouts with a frozen teacher. This approach is mirrored in the OvisOCR2 work, which combines RL with on-policy distillation into a smaller model for document parsing. The "Consensus as Privileged Context" paper further extends distillation to a label-free setting, converting multiple reasoning solutions into dense supervision. These works collectively indicate a growing recognition that on-policy distillation—where the student generates its own training trajectories—provides superior capability recovery compared to traditional static distillation, especially when combined with reinforcement learning signals.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Qingyu Zhang, Qianhao Yuan, Hongyu Lin, Yaojie Lu, Xianpei Han, Le Sun, Xiang Li, Ming Xu, Jiarui Li, Xiuyin Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ShortOPD, a short-to-long on-policy distillation schedule that recovers pruned LLMs by training on the model's own on-policy rollouts with a frozen teacher, directly addressing on-policy distillation for LLM capability improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13124)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xinyu Tang, Gangqiang Cao, Yurou Liu, Yuliang Zhan, Xiaochong Lan, Yifan Li, Yuchen Yan, Han Peng, Zican Dong, Zhenduo Zhang, Tianshu Wang, Xinyu Kong, Zujie Wen, Wayne Xin Zhao, Zhiqiang Zhang, Jun Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Scales verifiable-reward RL (zero RL) to 1T parameters, revealing emergent reasoning behaviors and proposing a structured CoT quality evaluation framework.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.12395)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Leitian Tao, Baolin Peng, Wenlin Yao, Tao Ge, Hao Cheng, Mike Hang Wang, Jianfeng Gao, Sharon Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dense credit-assignment method for agentic RL that derives per-action rewards from frozen reference model log-probabilities, enabling pure RL improvement on long-horizon tool-use tasks without SFT.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13988)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Cheng Tang, Junzhi Ning, Min Cen, Wei Li, Xinyi Zeng, Pinxian Zeng, Rongbin Li, Qiming Zhu, Yuqiang Li, Junjun He, Yirong Chen, Ming Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RLVR framework with sample-wise, outcome-conditioned visual alignment that improves multimodal reasoning, directly contributing to RL for LLMs with a new reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13931)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Shuzhen Li, Yifan Zhang, Jiacheng Guo, Quanquan Gu, Mengdi Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DeepLoop, a residual scaling method for looped transformers that enables stable recurrent depth for latent reasoning, directly addressing a key architectural challenge for implicit CoT.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13491)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiang Zhu, Jiajun Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces LAPO, a self-generated process reward method for multi-turn search reasoning that uses leave-one-turn attribution to provide process supervision without external reward models, directly contributing to RL for LLMs via reward design.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13501)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mehak Dhaliwal, Rasta Tadayon, Andong Hua, Haewon Jeong, Yao Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CARE-PPO, a novel RL framework that repurposes the PPO critic as a confidence estimator via a confidence-aligned reward, directly improving LLM quantitative prediction and uncertainty estimation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.12687)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhixiao Zheng, Zheren Fu, Zhiyuan Yao, Chunxiao Liu, Dongming Zhang, Zhendong Mao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Groc-PO, a grounded preference optimization framework with stage-specific supervision for multimodal LLMs, directly addressing RL-for-LLMs via a new reward design and training pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13712)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hao Li, Han Fang, Zixin Pan, Xin Wei, Hongbo Sun, Jinglin Xu, Zhiyu Lin, Ye Yuan, Zhongjiang He, Yu Yu, Hao Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces GeoAnchor, a latent reasoning framework with interleaved text-latent representations for 3D spatial understanding, directly contributing to latent CoT/reasoning.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13454)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Patrick Wilhelm, Odej Kao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a FLOP-accounting framework for RL post-training that studies compute allocation trade-offs between model size, search, learning, and feedback, directly relevant to RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13389)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shiyin Lu, Yinglun Li, Yu Xia, Yuhui Chen, An-Yang Ji, Jun-Peng Jiang, Qing-Guo Chen, Jianshan Zhao, En Lin, Haijun Li, Cheng Qin, Zhao Xu, Weihua Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training recipe combining RL with a multi-component reward design and on-policy distillation into a smaller model for document parsing, directly matching RL-for-LLMs and on-policy distillation criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13639)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: John Gkountouras, Josip Juki\'c, Ivan Titov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CANON, a label-free self-distillation method that converts consensus among multiple reasoning solutions into dense token-level supervision, improving reasoning accuracy without gold labels.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.13643)

---

