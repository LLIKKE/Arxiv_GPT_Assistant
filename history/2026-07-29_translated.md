# 💡 今日研究速览 (Daily Summary)

### SFT and Distillation
The field is seeing a significant push toward more sophisticated distillation methods that go beyond simple imitation. **Masked Distillation**introduces a novel on-policy framework that internalizes Chain-of-Thought reasoning into latent computation, directly targeting the gap between observed reasoning traces and the model's internal processing. This is complemented by a unified study of on-policy distillation (OPD) for multi-turn planning, which demonstrates clear methodological advances over standard approaches. The concept of "noisy student" on-policy self-distillation for VLMs is also gaining traction, using prediction discrepancies between clean and corrupted inputs as a form of self-supervision that eliminates the need for external models or ground-truth answers. Furthermore, a diagnostic analysis of outcome-confounded local supervision in on-policy distillation reveals a critical insight: agreement-on-failure often dominates, and local divergence alone cannot pinpoint where a trajectory becomes unrecoverable, highlighting a fundamental challenge in current distillation practices.

### RL for LLMs (Post-Training and Optimization)
Reinforcement learning for LLMs is undergoing a rapid maturation, with several key themes emerging. First, there is a strong focus on addressing the fundamental limitations of current algorithms, as evidenced by the impossibility theorem proving a tradeoff between gradient unbiasedness and length invariance in GRPO. In response, new methods like**ACRL**propose adaptive control of training-inference discrepancy for stable RL training, while**Progress-conditioned Group Policy Optimization (ProGPO)**tackles credit assignment in long-horizon agentic tasks by using first-visit observation coverage to break credit traps. Second, the community is moving toward more structured and task-specific reward design. This includes the**SeekJudge**framework for computer-use agents,**SyRuP**for system-prompt following via a learned reward head, and the use of heuristic rewards for aligning LLMs as Socratic tutors. Third, the integration of RL with inference-time reasoning is a clear trend, with frameworks like**CALM**combining multi-task RL with controller-aware post-training, and stage-wise optimization (**STAIF**) that decouples soft and hard constraints. The release of large-scale models like**Kimi K3**, which employs million-token agentic RL with persistent rollouts, signals that these techniques are now being deployed at an industrial scale.

### Agents and Multi-Turn Planning
Agentic systems are benefiting from a convergence of distillation and reinforcement learning. The key challenge being addressed is the distribution gap between proprietary and open-source models, with**Multi-Agent Protocol Distillation (MAPD)**proposing a joint distillation and RL framework that uses a structured protocol as an intermediate representation to bridge this gap for agentic search. For tool-use coding agents, a two-stage post-training recipe combining schema-stripped SFT with execution-shaped RL (CRAFT) is proving effective. In the multimodal agentic space, novel actor-critic frameworks like**HyGAE**are being developed, which use hybrid advantage estimation and a unified critic to handle both token- and turn-level RL optimization. The "spy game" environment introduced in**RLSVR**is a creative approach to generating self-verifiable rewards for open-ended tasks, enabling RL-based self-improvement beyond traditional math and code domains. This direction is also seeing practical infrastructure advances, such as**DynaResize**, a runtime GPU reallocation system designed to mitigate pipeline bubbles in the disaggregated RL training loop for agentic models.

### Reasoning and Invisible Computation
A landmark finding this week challenges the very nature of how we perceive reasoning in LLMs. Research demonstrates that frontier LLMs perform consequential reasoning within semantically irrelevant filler tokens, revealing a form of "invisible computation" that evades standard Chain-of-Thought monitoring. This has profound implications for both AI safety and the design of distillation and reward methods, as it suggests that faithful reasoning may not be fully observable. Complementing this, a theoretical and empirical analysis shows that in-context learning with score-conditioned examples is equivalent to implicit policy gradient optimization, offering a new and powerful perspective on how LLMs can self-improve without explicit parameter updates. For more structured reasoning tasks, frameworks like**LaRec**are exploring latent reasoning for generative recommendation, using step-level alignment and personalized RL-tuning to enable efficient exploration in latent space. Similarly, the concept of "learning when to reason" is being applied to Text-to-SQL, where models are trained via SFT and DPO to dynamically decide whether to engage in explicit reasoning or bypass it.

### Multimodal and Spatial Reasoning
Multimodal reasoning is benefiting from curriculum-based and privileged-information approaches. A curriculum RL framework with offline-online critical-step awareness is being used to improve multimodal reasoning through step-level rewards and progressive training. A novel on-policy self-distillation method,**RP-OPSD**, leverages resolution differences as privileged information, achieving both training speedup and performance gains in multimodal LLMs. In the spatial reasoning domain, a hierarchical diagnostic framework (**Spatial-IQ**) decomposes spatial intelligence into sub-tasks, and the combination of CoT supervision with RL and verifiable rewards is shown to significantly improve performance. Finally,**FlowCTS** introduces a novel on-policy distillation method for flow models that uses continuous trajectory supervision, outperforming vanilla KL-based OPD and mixed-reward RL baselines, indicating that these techniques are also being adapted for generative models beyond autoregressive transformers.

---

## 1. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Durgesh Kalwar, Vardhan Palod, Subbarao Kambhampati

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces masked distillation, a novel on-policy distillation framework that internalizes CoT reasoning into latent computation, directly targeting both latent reasoning and on-policy distillation.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22629)

---

## 2. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Qinsi Wang, Jing Shi, Huazheng Wang, Kun Wan, Yiran Wu, Bo Liu, Qingyun Wu, Hai Helen Li, Yiran Chen, Handong Zhao, Wentian Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RLSVR, a task-transformation paradigm that creates self-verifiable rewards for open-ended tasks, enabling RLVR-style self-improvement beyond math/code via a multi-agent spy game environment.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23802)

---

## 3. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Tianyi Men, Zhuoran Jin, Kang Liu, Jun Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a unified study of on-policy distillation (OPD and multi-teacher OPD) for multi-turn planning, directly advancing on-policy distillation for LLMs with clear methodological contributions.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24720)

---

## 4. [Translation Failed]

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Fei Ding, Yongkang Zhang, Yuhao Liao, Zijian Zeng, Huiming Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proves an impossibility theorem for unbiased and length-invariant policy optimization in GRPO, characterizing a fundamental tradeoff between gradient unbiasedness and length invariance.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23364)

---

## 5. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Vatsal Baherwani, Tom Goldstein, Ashwinee Panda

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Demonstrates that frontier LLMs perform consequential reasoning in semantically irrelevant filler tokens, revealing invisible computation that evades CoT monitoring and has direct implications for latent reasoning and AI safety.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22925)

---

## 6. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ofek I. Cohen, Lior Shani, Aviv Rosenberg, Ankur Samanta, Tal Wagner, Yonathan Efroni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a black-box method to learn a logit-bias vector via a KL-regularized RL objective for adapting LLMs without weight modification, directly contributing to RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22837)

---

## 7. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Masahiro Kaneko, Timothy Baldwin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical and empirical demonstration that in-context learning with score-conditioned examples corresponds to implicit policy gradient optimization, offering a new perspective on LLM self-improvement.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23153)

---

## 8. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Moumita Choudhury, Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ankush Chakrabarty, Shlomo Zilberstein, Ye Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CALM, a controller-aware post-training framework using multi-task RL (GRPO) over inference-time reasoning modules, directly addressing RL for LLMs with a novel training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23771)

---

## 9. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tzu-Heng Huang, Shengqi Qiu, Frederic Sala

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces program distillation to replace LLM-as-a-judge, producing transparent, low-cost programmatic judges and reward signals, directly relevant to scalable reward design for RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22561)

---

## 10. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Kaiyang Ye, Yuan Ge, Junxiang Zhang, Bei Li, Ziming Zhu, Haishu Zhao, Xiaoqian Liu, Chenglong Wang, Jingbo Zhu, Zhengtao Yu, Tong Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FlowCTS, a novel on-policy distillation method for flow models that uses continuous trajectory supervision and outperforms vanilla KL-based OPD and mixed-reward RL baselines.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24522)

---

## 11. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wendi Deng, Hang Du, Guoshun Nan, Haokun Tian, Jiaqi Yu, Xinlei Cao, Jaile Li, Jingfeng Chen, Ling Deng, Ting Li, Hao Yang, Jun Liu, Xudong Jiang, Sicong Leng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a curriculum RL framework with offline-online critical-step awareness for multimodal reasoning, directly improving LLM reasoning via step-level reward and progressive training.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23700)

---

## 12. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Aakash Kolekar, Sahika Genc, Shahriar Shariat, Bunyamin Sisman, Tibor Mezi, Barbara Poblete, Shree Vandana Kachroo, Calvin Chi, Parth Parmar, Ari Singer, Prayaas Jain, Cindy Barker, Benoit Dumoulin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage post-training recipe combining schema-stripped SFT and execution-shaped RL for tool-use coding agents, directly improving LLM behavior via RL.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22642)

---

## 13. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zing Team, Ao Xiang, Bi Jingping, Chen Jiahui, Chen Lehan, Chen Yilin, Cheng Xueqi, Fan Yixing, Gan Kairong, Gao Haowen, Gao Jinhua, Gao Shuxuan, Gong Chang, Guo Jiafeng, Guo Ruijie, Han Zhouyu, He Guangfu, He Yichun, Jiang Shuo, Jing Shaoling, Jing Ya, Lei Chenhao, Lei Yan, Li Anqi, Li Chengao, Li Haoyu, Li Shitian, Liang Xinjian, Liu Zhaoge, Lyu Xingyu, Nie Zhuwei, Pang Liang, Quan Zeping, Shan Shiguang, Shen Huawei, Tang Xinran, Tian Feng, Wang Qian, Wang Ruiping, Wang Xiaohong, Xia Zaiyu, Xiao Yi, Xu Jiayuan, Xu Kehan, Xu Qianqian, Xu Tianyu, Xu Yongjun, Yang Haoming, Yang Jun, Yao Di, Yu Xiaoming, Zhang Futong, Zhang Jie, Zhang Shixuan, Zhang Yuxuan, Zhao Xinyu, Zhao Zhuoran, Zhong Yunfei, Zhu Shengyu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Zing, a diagnosis-driven training recipe combining SFT, on-policy distillation, and rubric-based RL for social intelligence, directly matching RL-for-LLMs and on-policy distillation criteria.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23740)

---

## 14. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, M. C., Jianfeng Cai, Xinyuan Cai, Peizhou Cao, Yuxuan Cao, Ziwei Chai, Y. Charles, H. S. Che, Guanduo Chen, Guangyu Chen, Guanzheng Chen, Huarong Chen, Jia Chen, Jianlong Chen, Jun Chen, Kexin Chen, Peng Chen, Ruijue Chen, Wentao Chen, Xin Chen, Yang Chen, Yanru Chen, Yifei Chen, Yingjiang Chen, Yuankun Chen, Yujie Chen, Yutian Chen, Zhirong Chen, Dazhi Cheng, Yean Cheng, Jialei Cui, Jingbing Cui, Anqi Dai, Jiaqi Deng, Hao Ding, Rui Ding, Shaofeng Ding, Mengfan Dong, Mengnan Dong, Yuhao Dong, Yuxin Dong, Angang Du, Chenzhuang Du, Dikang Du, Jusen Du, Yulun Du, Yu Fan, Jing Feng, Qiulin Feng, Yichen Feng, Kelin Fu, Qiang Fu, Fuxuan Gao, Hongcheng Gao, Jingyue Gao, Tong Gao, Weijia Gao, Shangyi Geng, Jie Gong, Linhu Gong, Shengao Gong, Xiaochen Gong, Qizheng Gu, Yicheng Gu, Shuhao Guan, Haiqing Guo, Shiqi Guo, Xiang Guo, Zhengyan Guo, Beixi Hao, Wenxin Hao, Xiaoru Hao, Dailan He, Haotian He, Lehan He, Qi He, Weiran He, Xinran He, Xinyi He, Yibo He, Yunjia He, Chao Hong, Tiange Hong, Hao Hu, Jiaxi Hu, Ruikun Hu, Weiming Hu, Yangyang Hu, Zhenxing Hu, Liang Hua, Jinbin Huang, Ke Huang, Ruiyuan Huang, Siying Huang, Weixiao Huang, Yan Huang, Zhengjie Huang, Zhiqi Huang, Yulong Hui, Chaobo Jia, Yutong Jiang, Zhejun Jiang, Zuoyou Jiang, Wenyi Jin, Xinyi Jin, Yu Jing, Huanjun Kong, Guokun Lai, Aidi Li, Cheng Li, Chengyuan Li, Cong Li, Fang Li, Guanyu Li, Haoyang Li, Jia Li, Junxiong Li, Lei Li, Letian Li, Lincan Li, Weihong Li, Wentao Li, Xintong Li, Yang Li, Yishen Li, Yiwei Li, Yuxiao Li, Zhaowei Li, Zhaoxi Li, Zheming Li, Zhengxiao Li, Zhiyuan Li, Jiawei Lin, Xiaohan Lin, Yibo Lin, Zichao Lin, Ziyan Lin, Bill Liu, Boxiao Liu, Chuan Liu, Liang Liu, Shaowei Liu, Shudong Liu, Shuran Liu, Tianwei Liu, Weizhou Liu, Yangyang Liu, Yanming Liu, Yibo Liu, Yipeng Liu, Zhengying Liu, Zhiheng Liu, Enzhe Lu, Haoyu Lu, Linqiang Lu, Tingzhan Lu, Zhiyuan Lu, Aotian Luo, G. Luo, Junyu Luo, Yifan Luo, B. Lyu, Wenzhou Lyu, Shaoguang Mao, Yuan Mei, Xin Men, Minqing Ni, Yixuan Niu, Siyuan Pan, Shujun Peng, Zhangyang Qi, Ruoyu Qin, ZeChao Qin, Zeyu Qin, Haiquan Qiu, Jianxin Qiu, Jiezhong Qiu, Bowen Qu, Yuhao Qu, Zeyu Shang, Youbo Shao, Han Shen, Jincheng Shi, Juanfeng Shi, Lidong Shi, Shengyuan Shi, Wingchun Siu, Pengwei Song, Xiaoxi Song, Jianlin Su, Yunfeng Su, Zhaochen Su, Lin Sui, Jingsong Sun, Junyao Sun, Shaoning Sun, Shuzhe Sun, Tongyu Sun, Yujun Sun, Yunpeng Tai, Chuning Tang, Heyi Tang, Sirui Tang, Zecheng Tang, Chaoran Tian, Rongpeng Tian, Yu Tian, Wei Tu, Chensi Wang, Chuang Wang, Chunjie Wang, Dinglu Wang, Feng Wang, Hailong Wang, Haiming Wang, Hao Wang, Hao Wang, Huaqing Wang, Hui Wang, Jiayi Wang, Jinglong Wang, Jinhong Wang, Jiuzheng Wang, Linian Wang, Shaobo Wang, Shenzhi Wang, Shuyi Wang, Si Wang, Siyuan Wang, Tianfu Wang, Wenjue Wang, Xingran Wang, Xinmei Wang, Xinyuan Wang, Xusheng Wang, Yalin Wang, Yangkun Wang, Yao Wang, Yaoyu Wang, Yejie Wang, Yiqin Wang, Yucheng Wang, Yuzhi Wang, Zhaoji Wang, Zhaowei Wang, Zhengtao Wang, Zhenhao Wang, Zhongsheng Wang, Zifan Wang, Chu Wei, Ming Wei, Shouxin Wei, Zichen Wen, Fan Wu, Haoning Wu, Rucong Wu, Wenhao Wu, Xiaoxue Wu, Yingcong Wu, Yongqi Wu, Yuxin Wu, Zijian Wu, Xinglang Xian, Chenxuan Xiang, Yuye Xiang, Bocheng Xiao, Chenjun Xiao, Xin Xiao, Jin Xie, Xiaotong Xie, Yifeng Xie, Zhe Xie, Bowei Xing, Yiming Xiong, Baosheng Xu, Boyu Xu, Jiale Xu, Jianfan Xu, Jing Xu, Jinjing Xu, L. H. Xu, Qingtao Xu, Shuyao Xu, Suting Xu, Tiantian Xu, Tianxiang Xu, Weixin Xu, Xinran Xu, Yangchuan Xu, Ye Xu, Yueni Xu, Ziyao Xu, Haonan Xue, Junjie Yan, Yaoyao Yan, Fan Yang, Guangyao Yang, Hao Yang, Junwei Yang, Ruoyu Yang, Wenjie Yang, Xiaofei Yang, Xinyu Yang, Yi Yang, Yiling Yang, Ying Yang, Yuchen Yang, Zhen Yang, Zhilin Yang, Zian Yang, Zuhao Yang, Haotian Yao, Dan Ye, Haoran Ye, Wenjie Ye, Zhanbo Ye, Bohong Yin, Haoxiang Yin, Xietong Yin, Chengzhen Yu, Haozhen Yu, Longhui Yu, Shengnan Yu, Shuying Yu, Tianxiang Yu, Enming Yuan, Mengjie Yuan, Tongtian Yue, Wei Yue, Yang Yue, Dunyuan Zha, Haobing Zhan, B. H. Zhang, Dehao Zhang, Fei Zhang, Hao Zhang, Haoyuan Zhang, Huanyu Zhang, Jiapei Zhang, Jiaxuan Zhang, Jin Zhang, Kaiyi Zhang, Miaozhen Zhang, Puqi Zhang, Qinglei Zhang, Rong Zhang, Rui Zhang, Shaoshuai Zhang, Shiyi Zhang, Xiaobin Zhang, Xiaoyun Zhang, Y. Zhang, Yangkun Zhang, Ye Zhang, Yichi Zhang, Yikun Zhang, Yizhi Zhang, Yongting Zhang, Yu Zhang, Yutao Zhang, Yutong Zhang, Zheng Zhang, Zijing Zhang, Bin Zhao, Chenguang Zhao, Feifan Zhao, Jinglun Zhao, Jinxiang Zhao, Shuai Zhao, Wenshuo Zhao, Xiangyu Zhao, Xuanle Zhao, Yikai Zhao, Zijia Zhao, Haozhi Zheng, Huabin Zheng, Ruihan Zheng, Shaojie Zheng, Tengyang Zheng, Haofeng Zhong, Lei Zhong, Longguang Zhong, M. Zhou, Qiankang Zhou, Runjie Zhou, Ruozhang Zhou, Xinyu Zhou, Yiqiao Zhou, Zaida Zhou, Jinguo Zhu, Liya Zhu, Xinhao Zhu, Yangjunfeng Zhu, Yuxuan Zhu, Zhen Zhu, Chen Zhuang, Weiyu Zhuang, Xinxing Zu

**机构**: Moonshot AI

**💡 亮点 (Highlight)**: Introduces a large-scale MoE model with RL post-training across general, agentic, and coding domains, including million-token agentic RL with persistent rollout, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24653)

---

## 15. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL pipeline (GRPO) with a heuristic reward for aligning LLMs as Socratic tutors, directly improving educational alignment via on-policy optimization.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22996)

---

## 16. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junlin Liu, Jiangwang Chen, Zixin Song, Shuaiyu Zhou, Chunji Lv, Hank Wu, Kailin Jiang, Jinyang Wu, Bohan Yu, Chenxi Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Multi-Agent Protocol Distillation (MAPD), a joint distillation and RL framework using a structured protocol as intermediate representation to bridge distribution gap from proprietary to open-source LLMs for agentic search.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24280)

---

## 17. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenxuan Zhang, Yuhui Wang, Donggang Jia, Xiaoqian Shen, Jian Ding, Ivan Viola, J\"urgen Schmidhuber, Mohamed Elhoseiny

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HyGAE, a novel actor-critic framework with hybrid advantage estimation and a unified critic for token- and turn-level RL optimization of VLMs in agentic environments.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23605)

---

## 18. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu Xia, Zihan Lin, Wei Yang, Rui Zhong, Cheng Chen, Huan Ren, Yao Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LaRec, a latent reasoning framework for generative recommendation that uses step-level alignment and personalized RL-tuning with Gaussian mixture distributions to enable efficient latent-space reasoning and exploration of user interests.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24617)

---

## 19. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Soohyuk Jang, Jiheum Yeom, Nohil Park, Sang Hun Kim, Yoonyoung Choi, Kiwook Bae, Sungroh Yoon

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a framework integrating auto-thinking (dynamic reasoning bypass) into SFT and DPO for Text-to-SQL, directly addressing on-policy distillation and RL for LLMs by training the model to decide when to reason.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22622)

---

## 20. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jian Hong, Chen Cheng, Quan Liu, Yuhao Chen, Enhong Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a stage-wise RL framework (STAIF) that decouples soft and hard constraint optimization using preference optimization and RL with verifiable rewards, directly advancing RL-for-LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22649)

---

## 21. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yang Wan, Zhenhao Zhang, Jierui Wang, Linchao Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a practical model-based reward framework (SeekJudge) for RL in computer-use agents, matching rule-based supervision with a novel multi-agent judge and distillation pipeline.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23263)

---

## 22. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Patrick Rim, Tom Long, Ekta Prashnani, Ruth Rosenholtz, Ben Boudaoud, Peter Xenopoulos, Alex Wong, Joohwan Kim, Jae-Hyun Jung

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hierarchical diagnostic framework for spatial reasoning and demonstrates that training with CoT supervision over sub-tasks combined with RL with verifiable rewards improves performance, directly contributing to RL for LLMs.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22864)

---

## 23. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenwu Fan, Qihong Lin, Zhijie Xia, Zhuo Zheng, Sihao Wang, Qiang Chen, Liangsheng Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ACRL, a method to adaptively control training-inference discrepancy for stable RL training of LLMs, directly addressing a core RL-for-LLMs challenge.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24062)

---

## 24. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuai Wang, Daoan Zhang, Zhe Tang, Hao Cheng, Jiaheng Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes NOPD, a noisy student on-policy self-distillation method for VLMs that uses prediction discrepancies between clean and corrupted inputs as self-supervision, improving reasoning without external models or ground-truth answers.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23125)

---

## 25. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kaibing Yang, Guangfeng Cai, Shengtian Yang, Shuo He, Yu Li, Mengyi Liu, Pengwei Chen, Jun Xu, Lei Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Progress-conditioned Group Policy Optimization (ProGPO), a new RL method for LLM agents that uses first-visit observation coverage to assign advantages and break credit traps in long-horizon tasks with sparse outcome rewards.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22724)

---

## 26. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guoqing Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a diagnostic analysis of outcome-confounded local supervision in on-policy distillation for LLM reasoning, revealing that agreement-on-failure dominates and that local divergence alone cannot identify where a trajectory becomes unrecoverable.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23731)

---

## 27. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hanlin Du, Zhiyuan Yan, Haiquan Chen, Jiarui Fang, Yungang Bao, Sa wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a runtime GPU reallocation system for disaggregated RL-based LLM post-training, directly addressing pipeline bubbles in the RL training loop.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.22614)

---

## 28. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Seoyeon Kim, Minjae Kang, Jaehyung Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SyRuP, a decoding-time framework with a learned reward head for system-prompt adherence, directly contributing a new reward-guided method for LLM behavior control.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.23991)

---

## 29. [Translation Failed]

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qihui Zhu, Yuchen Wang, Zijian Wen, Tao Zhang, Mengjie Zhang, Yang Liu, Shuangwu Chen, Siying Wu, Jian Yang, Xiaofeng Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel on-policy self-distillation method for multimodal LLMs that uses resolution differences as privileged information, achieving training speedup and performance gains.

**摘要**: [Translation Failed]

[阅读原文](https://arxiv.org/abs/2607.24447)

---

