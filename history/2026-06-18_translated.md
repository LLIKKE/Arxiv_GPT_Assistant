# 💡 今日研究速览 (Daily Summary)

# LLM的按政策蒸馏
多篇论文将政策蒸馏（OPD）作为改进LLM的核心方法论，出现了一个明显的趋势。该领域正在从简单的模仿学习转向更复杂的技术，以解决基本的训练与推理不匹配问题。PowerOPD引入了有界的权力转换奖励，与普通OPD相比，可以稳定训练动态并提高推理准确性。近端政策优化区（ZPPO）采取了一种新颖的方法，让教师保持在提示而不是梯度中，重新制定提示来指导学生学习，而不会产生直接的梯度干扰。对于扩散语言模型，从自我未来学习（d-OPSD）提供了第一个具有步骤级监督的政策上自我提炼框架，而自生成错误训练使令牌编辑器能够修复自己的草稿错误。用于图形用户界面基础的质量感知自我提炼方法演示了正确性感知门控如何提高教师信号质量。这些工作共同表明，OPD正在成熟为一系列原则性技术，可以稳定训练、提高样本效率并在没有外部监督的情况下实现持续自我改进。

# 推理和效率的强化学习
强化学习继续推动LLM推理的突破，几篇论文解决了当前方法的根本局限性。动态认识论熵描述的Ericycle Reinstructive Learning（E3 RL）通过使用动态熵阈值来实现自我修复推理，直接对抗自回归诅咒-消除早期逻辑缺陷并重新使用KV缓存来进行长期任务。SuCo引入了一个两阶段框架，将对齐微调与服务感知策略优化相结合，以动态控制推理长度，直接针对效率-可靠性的权衡。动态推出编辑（DRE）通过在GRPO式训练期间编辑推出轨迹来改善信用分配，来解决RL训练模型中的过度思考问题。在无批判的WLVR中重新思考组提出了负令牌过滤以实现稳定的单次推出训练，消除了组同步带来的数据效率低下。从推理轨迹到可重用模块中的理论框架提供了重要的基础，展示了SFT和RL如何在组合概括中发挥补充作用。这些进步共同表明，RL方法正在向更适应、更高效、更有理论依据的RL方法转变，这些方法可以应对语言模型推理的独特挑战。

# 潜在推理和深循环架构
一种新兴的范式专注于Transformer架构内的潜在推理，超越显式的思想链。LoopCoder-v2引入了用于潜在推理的并行循环Transformer，仔细研究循环计数的收益成本权衡，并实现强大的代码推理结果。定点推理者提出了一种具有保证定点收敛的环路Transformer作为端到端停止机制，直接解决深度环路架构中的信号传播挑战。学习细化隐藏状态（Relar）使用动态引导的潜在细化来在解码之前迭代更新隐藏表示，在表示级别而不是令牌级别应用策略梯度。这些方法有一个共同的见解：推理可以发生在Transformer层的潜在空间中，从而可能提供比自回归令牌生成更高效、更可控的计算。收敛保证和自适应停止机制表明这个方向正在朝着实用、稳定的实施方向发展。

# 多模式和统计系统
RL与多模式和代理系统的集成取得了重大进展。请参阅First，Answer Later引入了敏捷驱动的RL（通过GRPO），用于MLLM中的视觉证据预对齐，通过确保模型在生成答案之前关注相关的视觉证据来直接改善视觉基础和推理。MaineCoon将加强在线策略蒸馏（ROPD）作为核心技术，推动实时视听世界模型，展示了OPD如何适应多模式自回归模型。STAR为文本到图像RL训练后提供时空自适应奖励分配，使用注意力图将政策更新集中在相关潜在区域上--这是扩散模型微调的关键进步。在agentic方面，EnvRL通过辅助环境动态学习目标（状态预测和逆动力学）增强了agentic RL，通过帮助模型理解环境转变，显示出对长期任务的明显改进。OPD-Evolver提出了一个慢-快协同进化框架，使用政策上的自我提炼来培养整体的代理进化者，这表明OPD可以作为跨多个维度的代理改进的统一机制。

---

## 1. 通过轻量级的体验式潜在记忆持续自我完善

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 9/10

**作者**: Vaggelis Dorovatas, Nancy Kalaj, Rahaf Aljundi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an online method that distills inference-time reasoning traces into compact latent memories using self-generated rewards, enabling continual self-improvement without external supervision.

**摘要**: arXiv：2606.17803v1宣布类型：新摘要：大型语言模型通过扩展推理时计算来实现强大的推理性能，但从根本上保持无状态，丢弃了在此过程中生成的丰富、自创的推理痕迹。我们调查模型是否可以从这种经验中在线学习，将瞬时计算（推理痕迹）转化为持久的可重复使用的知识，并且无需外部监督或访问未来数据。我们表明，原始推理轨迹的内上下文学习（ICL）无法概括，反映了代币级重用的根本局限性：即使在细化（例如自我反思）之后，单个轨迹也缺乏传输所需的抽象。相比之下，我们从最近关于无监督强化学习的工作中汲取灵感，发现以自我生成的测试时信号（多数投票）作为奖励的轻量级每实例训练会产生巨大的收益，通常超过全数据集离线训练，激发了从原始痕迹到学习的潜在代表的转变。基于这一见解，我们提出了一种在线方法，该方法将用于遇到问题的推理时计算提炼成紧凑的模块化潜在记忆，以捕获底层推理结构。这些记忆被存储和检索以供未来输入，通过模块化设计实现持续改进，同时避免灾难性的遗忘。重要的是，我们的方法高效、参数化为极其轻量级的软提示记忆（~模型参数的0.001%），并且仅用几个梯度步骤进行训练，但通过完整参数更新和离线训练即可实现具有竞争力的性能。在具有挑战性的数学推理基准中，我们的方法显着优于零触发和原始数据ICL基线，同时在数据集之间有效传输。

[阅读原文](https://arxiv.org/abs/2606.17803)

---

## 2. 向自我未来学习：DLLM的政策上自我蒸馏

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yifu Luo, Zeyu Chen, Haoyu Wang, Xinhao Hu, Yuxuan Zhang, Zhizhou Sha, Shiwei Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces d-OPSD, the first on-policy self-distillation framework for diffusion LLMs, with a novel suffix-conditioning teacher and step-level supervision.

**摘要**: arXiv：2606.18195v1宣布类型：新摘要：基于策略的自蒸馏（OPSD）已被证明对训练后的大型语言模型（LLM）有效，但其在扩散LLM（dLLM）中的应用尚未探索。现有的OPSD方法本质上是自回归中心的。他们通过从左到右的前缀条件与令牌级发散监督注入特权信息，这种设计从根本上与dLLM的任意顺序生成相冲突。我们介绍d-OPSD，第一个OPSD框架dLLMs量身定制。我们的方法做出了两个核心贡献。首先，我们通过使用自我生成的答案作为后缀条件反射来重新构建自学者的构建，使学生模型能够从“自我未来经验”而不是特权前置中学习。其次，我们将监督从符号级转移到步骤级，使训练与dLLM的迭代去噪过程保持一致。四个推理基准的实验表明，d-OPSD始终优于WLVR和SFT基线，具有卓越的样本效率，仅需要WLVR大约10%的优化步骤，并为dLLM后训练开辟了一条有希望的途径。该代码可在https://github.com/xingzhejun/d-OPSD上获取。

[阅读原文](https://arxiv.org/abs/2606.18195)

---

## 3. PowerOPD：通过有限电力转型稳定政策内蒸馏

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Anhao Zhao, Junlong Tong, Yingqi Fan, Ping Nie, Wenjie Li, Xiaoyu Shen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PowerOPD, a bounded power-transformation reward for on-policy distillation that stabilizes training and improves reasoning accuracy over vanilla OPD.

**摘要**: arXiv：2606.17199v1公告类型：新摘要：大型语言模型的标准策略蒸馏（OPD）使用学生样本标记来估计反向KL目标，产生无偏的单样本蒙特卡罗估计器，避免了词汇范围的计算。然而，我们发现，这种估计在实践中受到严重的训练病理：样本效率低下，不稳定的生成动态，以及与精确的全词汇OPD相比，存在很大的性能差距。奖励水平诊断将这些病理追溯到对数比奖励，它不受结构限制，产生集中在早期位置并在整个训练过程中持续存在的极高方差梯度;标准的事后缩放失败，因为它们只有在这种扭曲发生后才起作用。为了解决这个问题，我们提出了PowerOPD：来自Box-Cox功率变换的一系列本机有界、符号一致的奖励，参数为Alpha > 0，其中对数比是退化Alpha -> 0限制。在六个数学推理基准和四个Qwen 3师生对中，PowerOPD的基准平均Avg@8/Pass@8比普通OPD提高高达+6.37/+5.71，比事后稳定提高+3.01/+3.54，比全词汇OPD提高+2.59/+8.90，同时将壁挂时间减少59.2%，峰值图形内存减少23.1%。较大的Alpha通常会提高准确性，持续缩短响应，并使梯度规范比普通OPD小3，000倍以上。

[阅读原文](https://arxiv.org/abs/2606.17199)

---

## 4. LoopCoder-v2：仅循环一次，以实现高效的测试时计算扩展

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jian Yang, Shawn Guo, Wei Zhang, Tianyu Zheng, Yaxin Du, Haau-Sing Li, Jiajun Wu, Yue Song, Yan Xing, Qingsong Cai, Zelong Huang, Chuan Hao, Ran Tao, Xianglong Liu, Wayne Xin Zhao, Mingjie Tang, Weifeng Lv, Ming Zhou, Bryan Dai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a parallel loop Transformer architecture for latent reasoning and studies the gain-cost trade-off of loop count, achieving strong code reasoning results.

**摘要**: arXiv：2606.18023v1宣布类型：新摘要：循环变形金刚通过重复应用共享块来扩展潜在计算，但顺序循环会随着循环计数而增加延迟和KV缓存内存。并行回路变压器（PLT）通过跨回路位置补偿（LCC）和共享KV门控滑动窗关注度来减轻这一成本，使回路计数成为一种实用的设计选择。因此，我们通过收益-成本观点研究PLT循环计数选择：额外的循环可能会细化表示，但opp也会在每个循环边界引入位置不匹配。我们通过在18 T令牌上从头开始训练LoopCoder-v2（一个具有不同循环计数的7 B PLT编码器家族）来实例化这项研究，然后进行匹配的指令调优和评估。从经验上看，双循环变体在代码生成、代码推理、代理软件工程和工具使用基准测试方面比非循环基线提供了广泛的收益，将SWE-Benefit从43.0提高到64.4分，将Multi-SWE从14.0提高到31.0分。相比之下，具有三个或更多循环的变体会回归，揭示出强烈的非单调循环计数效应。我们的诊断表明，循环2提供了主要的生产性细化，而后面的循环会产生递减的、振荡的更新和减少的代表多样性。由于随着细化收益的缩小，MPP引发的不匹配仍然大致固定，因此抵消成本日益占据主导地位。这种收益-成本权衡解释了PLT在两个环路上的饱和，并为环路计数选择提供了诊断。

[阅读原文](https://arxiv.org/abs/2606.18023)

---

## 5. 最接近的政策优化区：教师是先知，而不是学生

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Byung-Kwan Lee, Ximing Lu, Shizhe Diao, Minki Kang, Saurav Muralidharan, Karan Sapra, Andrew Tao, Pavlo Molchanov, Yejin Choi, Yu-Chiang Frank Wang, Ryo Hachiuma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ZPPO, a novel on-policy distillation method that keeps the teacher in the prompt rather than the gradient, using reformulated prompts and a replay buffer to improve small student models.

**摘要**: arXiv：2606.18216v1宣布类型：新摘要：知识蒸馏将教师的能力转移给小学生，但在小学生制度中是脆弱的：强迫学生模仿大得多的老师的逻辑，将知识集中在老师最尖锐的模式上，损害了对培训主体以外基准家庭的概括。强化学习（RL）通过对学生自己的展开进行训练来避免logit模仿。然而，在每次推出都失败的问题上--产生零优势并被默默地忽视--将更强的教师反应注入政策梯度中打破了政策假设并导致漂移。我们引入了近端政策优化区（ZPPO），其灵感来自维果茨基的近端发展区，它使教师处于提示而不是政策梯度内。在困难问题上，ZPPO构建了两个重新制定的提示：包含二元预测的问题（BCQ）将一个正确的老师回答与一个不正确的学生回答配对，作为学生必须区分的匿名候选人，而包含负预测的问题（NCQ）将学生的错误提问汇总到一个提示中，以暴露他们共同的失败模式。即时重播缓冲区重新循环每个难题，直到它毕业（学生的平均推出准确率达到一半）或在有限容量下被FIFO驱逐，放大学生当前最近发展区域内的BCQ和NCQ。在Qwen 3.5系列中，在四个学生规模（0.8B-9 B）和一名27 B教师的情况下，接受视觉语言模型后培训，并在31个基准套件（16 VLM、10 LLM、5 Video）上进行评估，ZPPO的表现优于政策外/政策内蒸馏和GRPO，在最小规模下收益最大。

[阅读原文](https://arxiv.org/abs/2606.18216)

---

## 6. 先看，后回答：通过充分性驱动RL进行视觉证据预对齐

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yilian Liu, Sicong Leng, Guoshun Nan, Junyi Zhu, Jiayu Huang, Minghao Sun, Xuancheng Zhu, Yisong Chen, Zexian Wei, Xiaofeng Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel sufficiency-driven RL objective (GRPO) for visual evidence pre-alignment in MLLMs, directly improving visual grounding and reasoning.

**摘要**: arXiv：2606.17678v1宣布类型：新摘要：多模式大型语言模型（MLLM）将强大的文本推理与视觉输入集成在一起，但它们的响应可能与底层图像不一致，这表明推理过程中视觉证据的利用效率低下。流行的训练范式依赖于大规模基于字幕的预训练来进行一般对齐，然后是有监督的微调和强化学习，以实现指令遵循和复杂推理。然而，这种预训练只提供了薄弱的视觉基础：简短、粗略的字幕使模型偏向突出的对象，而忽略了细粒度的视觉证据。在本文中，我们介绍了视觉证据预对齐（VEPA），这是训练前和训练后之间的中间阶段，通过群体相对政策优化（GRPO）探索一种新型的视觉驱动目标，以优化受问题影响的视觉证据描述。跨不同基准的广泛实验表明，我们的VEPA持续提高了视觉要求高的评估的性能，并补充了标准的监督后培训。进一步的分析表明，收入来自强化的、可转移的视觉基础，而不是来自额外的特定任务培训。

[阅读原文](https://arxiv.org/abs/2606.17678)

---

## 7. 打破自回归诅咒：LLM的动态认识论熵描述的可擦除强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ziliang Wang, Kang An, Faqiang Qian, Jialu Cai, Cijun Ouyang, Yuhang Wang, Qibing Ren, Yichao Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes E3RL, a novel RL method that uses dynamic epistemic entropy thresholds to enable self-healing reasoning in LLMs by excising early logical defects and reusing KV cache, directly addressing the autoregressive curse in long-horizon reasoning.

**摘要**: arXiv:2606.17735v1 Announce Type: new  Abstract: Although reinforcement learning (RL) has expanded the cognitive boundaries of large language models (LLMs), it often remains vulnerable to the autoregressive curse in long-horizon logical reasoning: small epistemic perturbations introduced early in generation can propagate irreversibly along the Markov decision process flow, triggering cascading failures that drive the reasoning trajectory toward collapse. To overcome this autoregressive cascade, in which a single early mistake can compromise all subsequent reasoning steps, we propose dynamic epistemic entropy orchestrated erasable reinforcement learning ($\text{E}^3\text{RL}$). $\text{E}^3\text{RL}$ eliminates reliance on external signals by grounding the model's endogenous local autoregressive cross-entropy as an intrinsic coordinate of epistemic uncertainty. By introducing segment-level adaptive dynamic thresholds and advantage allocation, $\text{E}^3\text{RL}$ enables the model to precisely excise localized logical defects while reusing historical key-value (KV) cache streams, thereby endowing the reasoning process with a self-healing capability. We train $\text{E}^3\text{RL}$ on the DeepMath-103k dataset. Experimental results show that $\text{E}^3\text{RL}$ reshapes the exploration efficiency of long-sequence reasoning and improves sample efficiency while maintaining linear memory overhead. On mathematical reasoning benchmarks such as AIME, $\text{E}^3\text{RL}$ achieves substantial performance gains, with the 4B and 8B parameter models surpassing previous state-of-the-art (SOTA) results by 5.349\% and 6.514\%, respectively. These findings suggest that $\text{E}^3\text{RL}$ shatters the autoregressive curse in long-sequence reasoning and establishes a theoretical and systems-level foundation for the next generation of self-healing artificial general intelligence (AGI).

[阅读原文](https://arxiv.org/abs/2606.17735)

---

## 8. MaineCoon：追求实时视听社交世界模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lichen Bai, Tianhao Zhang, Shitong Shao, Dingwei Tan, Qiyu Zhong, Zhengpeng Xie, Haopeng Li, Qinghao Huang, Dandan Shen, Tengjiao Ji, Wei Wang, Peicheng Wu, Yuxuan Zhao, Xiangyu Zhu, Welly Luo, Shurui Yang, Zeke Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces reinforced online-policy distillation (ROPD) as a core technique for training a real-time audio-visual autoregressive model, directly matching the on-policy distillation criterion.

**摘要**: arXiv：2606.17800v1宣布类型：新摘要：随着越来越多的全球视频内容是在社交平台上消费的，用于互动社交目的，为社交世界构建的视频生成模型很重要，但在很大程度上被之前的研究忽视了。在这项工作中，我们定义了社交世界模型的位置，并构建了原型模型，作为实现这一目标的第一步。虽然以前的世界模型成功地模拟了物理环境或游戏世界探索，但它们从根本上脱离了以人为本的社会动态。为了弥合这一差距，作为社交世界模型的第一步，我们推出了MaineCoon，这是第一个实时视听自回归模型，具有22 B参数，能够实时流媒体生成和亚秒交互，在单个图形处理器上具有创纪录的帧率高达47.5 FPS。据我们所知，MaineCoon也是第一个专门针对社交互动应用程序优化的实时视听生成模型。为了实现高效、稳定的训练，我们在MaineCoon中引入了几种新颖技术，包括自重采样、跨模式表示对齐、领域感知偏好优化和强化在线策略蒸馏（ROPD）。我们还设计了第一个代理流推理框架，该框架支持千秒规模甚至更长的生成，同时通过代理缓存管理和即时规划来减轻漂移。这些创新显着加速了训练，同时优化了实时推理性能。我们相信，这项工作不仅为高质量、低延迟和长视野视听自回归模型设定了新的最先进（SOTA）性能基准，而且指出了下一代人工智能原生社交平台所需的范式转变。

[阅读原文](https://arxiv.org/abs/2606.17800)

---

## 9. 从推理痕迹到可重用模块：理解语言模型推理中的组合概括

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lingjing Kong, Xin Liu, Guangyi Chen, Martin Q. Ma, Xiangchen Song, Yuekai Sun, Mikhail Yurochkin, Taylor W. Killian, Ruslan Salakhutdinov, Kun Zhang, Eric P. Xing, Zhengzhong Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical framework and controlled experiments showing how SFT and RL play complementary roles in compositional generalization for LLM reasoning, directly relevant to RL-for-LLMs.

**摘要**: arXiv：2606.18089v1宣布类型：新摘要：将监督微调（SFT）与强化学习（RL）相结合的后训练管道已成为将大型语言模型（LLM）转化为稳健推理器的关键配方。我们认为，这种综合成功是由成分概括驱动的，我们通过分层潜在选择模型将其形式化。在该框架中，推理痕迹是由与可重复使用的原子模块相对应的一系列离散潜在选择变量生成的，包括技能（本地操作）和路由机制（如何选择、重复使用和组成中间信息）。在这个模型中，我们从理论上表明SFT和RL发挥着不对称的互补作用：SFT在组成痕迹中提供原始模块材料，而RL分解这些痕迹以识别潜在的原子模块并实现组成概括。我们设计控制实验来验证这一理论。我们的结果表明，RL可以从SFT提供的复合轨迹中提取原子模块，并将它们重新组合以解决新的配置。此外，我们发现对复合轨迹进行训练比对孤立原子模块进行训练能产生更强的概括性。最后，我们研究SFT和RL数据之间的关系，并确定一种有效的协议，其中SFT通过组合痕迹确保覆盖所有原子模块，而RL则专注于SFT支持之外的新型组合以推动探索。

[阅读原文](https://arxiv.org/abs/2606.18089)

---

## 10. 动态推出编辑以减少RL训练推理模型中的过度思考

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zihao Wei, Wenjie Shi, Liang Pang, Jingcheng Deng, Shicheng Xu, Shasha Guo, Zenghao Duan, Jiahao Liu, Jingang Wang, Huawei Shen, Xueqi Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Dynamic Rollout Editing (DRE), a training-time intervention for GRPO-style RL that edits overthinking rollouts to improve credit assignment and reduce unnecessary reasoning.

**摘要**: arXiv：2606.17890v1宣布类型：新摘要：长形式思维链推理可以提高复杂任务的LLM性能，但在出现正确答案后，模型通常会继续生成不必要的推理。我们将这种行为称为过度思考。我们从训练后的GRPO式强化学习（RL）的角度研究这种现象，将其框架为训练时的学分分配问题，而不仅仅是解码时的停止问题。在GRPO训练开始时抽样的展开中，我们观察到，对于相同提示，成功的轨迹可能比不成功的轨迹表现出稍微高一些的过度思考程度。这种早期不平衡为不良反馈循环提供了起点：由于GRPO分配序列级信用，因此它无法区分达到解决方案的前置符与延长成功轨迹的不必要延续。两者都收到积极的更新信号，使最初的不平衡在训练期间发展为更严重的过度思考。为了解决这个问题，我们引入了动态滚动编辑（DRE），这是一种针对成功轨迹的训练时干预，在答案出现后继续思考。DRE保留了已接受的已验证的前置，编辑剩余的思维，并更喜欢同一RL组内编辑的轨迹，削弱了不必要思维的偏好信号，而不会惩罚得出答案所需的推理。不同任务的实验表明了DRE的有效性。

[阅读原文](https://arxiv.org/abs/2606.17890)

---

## 11. 重新思考无批评的WLVR中的群体

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yihong Wu, Liheng Ma, Lingfeng Xiao, Muzhi Li, Xinyu Wang, Yingxue Zhang, Jian-Yun Nie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes negative token filtering, a novel method enabling stable single-rollout training in critic-free RL for LLMs, directly addressing data inefficiency and group synchronization issues.

**摘要**: arXiv：2606.17250v1宣布类型：新摘要：强化学习（RL）已成为训练后大型语言模型的核心范式。现有的无批评RL方法通常会为同一问题生成一组展开，以估计优势计算的价值基线。然而，这种设计存在数据效率低下、组同步障碍以及结构化部署的不灵活性。在这项工作中，我们重新审视了“群体”的作用，并表明其基本功能不仅是估计基线，而且是防止对阴性样本的虚假处罚。基于这一见解，我们提出了负令牌过滤，这是一种简单有效的策略，可以实现稳定的单次推出训练。我们将其应用于两种批级优势方法，相对于基于群组的RL技术，在推理任务上实现了相当的性能，在代理任务上实现了更强的性能。

[阅读原文](https://arxiv.org/abs/2606.17250)

---

## 12. OPD-Evolver：通过按政策蒸馏培养整体Agent Evolver

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guibin Zhang, Xun Xu, Yanwei Yue, Zikun Su, Wangchunshu Zhou, Xiaobin Hu, Shuicheng Yan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a slow-fast co-evolution framework using on-policy self-distillation to cultivate holistic agent evolvers, directly matching the on-policy distillation criterion.

**摘要**: arXiv：2606.17628v1宣布类型：新摘要：记忆已成为自我进化主体的标准基础，但保留经验并不等同于学习如何通过它进化。现有的记忆主体可以存储轨迹、检索反射或积累技能，但通常缺乏选择有用经验、采取行动、编写可重复使用的知识并维护不断增长的知识库的整体能力。我们引入了OPD-Evolver，这是一个慢-快协同进化框架，通过政策上的自我提炼来培养这样的代理进化器。在快速循环中，OPD-Evolver与四级内存层次结构交互，以读取、使用、写入和维护体验，以实现测试时的快速发展。在慢循环中，结果校准的记忆归因和特权事后诸葛亮将这四种能力提炼到可部署政策中。在多域基准测试中，OPD-Evolver超过ReasoningBank等内存系统高达11.5%，超过Skill 0等基于训练的方法约5.8%。进一步的分析表明，OPD-Evolver内化了高价值体验和内存管理，使OPD-Evolver-9 B能够挑战Qwen 3.5 - 397 B-A17 B和Step-3.5-Flash等大型同行，超越内存增强代理，走向真正合格的代理进化者。

[阅读原文](https://arxiv.org/abs/2606.17628)

---

## 13. 扩散语言模型中标记编辑的自生成错误训练

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lin Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes self-generated T2T, an on-policy distillation method that trains a token editor on the model's own draft errors to fix training-inference mismatch in diffusion LMs.

**摘要**: arXiv：2606.17175v1宣布类型：新摘要：令牌到令牌（T2 T）编辑允许LLaDA 2.1在块扩散解码期间修改已提交的令牌。发布的食谱对编辑进行了随机词汇损坏的培训，但推断编辑会看到模型自己流畅、高可信度的草稿错误。我们研究这种训练-推理不匹配，并提出自生成的T2 T，它执行无梯度草稿传递，用预测的令牌填充掩蔽位置，并在这些自生成的破坏下监督第二次传递中的恢复。我们在LLaDA2.1-mini上将更新实施为简短的LoRA连续预训练传递，并在官方Q-Mode T2 T程序下对多个基准进行评估，其中推理参数不变。该方法通常可以提高准确性，同时降低T2 T编辑强度，减轻失败模式，例如在正确推理后的最终数字转录错误以及在简短的事实答案之前的过度自我纠正。

[阅读原文](https://arxiv.org/abs/2606.17175)

---

## 14. EnvRL：在抽象强化学习中从环境动力学中学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhitong Wang, Songze Li, Hao Peng, Shuzheng Si, Yi Wang, Maosong Sun, Juanzi Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EnvRL, a framework that augments agentic RL for LLMs with auxiliary environment dynamics learning objectives (state prediction and inverse dynamics), showing clear improvements on long-horizon tasks.

**摘要**: arXiv：2606.17680v1宣布类型：新摘要：强化学习（RL）已成为将大型语言模型（LLM）训练为代理的强大范式。然而，用于长期代理任务的传统RL方法通常难以应对稀疏的结果奖励。直觉上，这忽略了展示交互轨迹中包含的丰富环境动态信息。我们认为，交互体验本质上是一种隐性监督信号，揭示了环境的潜在转变机制，并使代理能够构建更准确的环境内部模型。因此，在这项工作中，我们研究如何利用这个额外的信号来改善政策学习。具体来说，我们提出了EnvRL，这是一个通过两个辅助目标（状态预测和逆动力学）将环境动力学学习纳入代理RL的框架。通过与主要RL目标联合优化，我们鼓励代理从自己的交互体验中内化环境动态。对两个长期代理基准的广泛实验表明，EnvRL比仅RL基线在成功率方面实现了显着提高，例如，接受GRPO培训时，ALFWorld上的Qwen-2.5-1. 5 B-Direcct从72.8%提高到77.4%，WebShop上的Qwen-2.5 - 1. 5 B-Direcct从56.8%提高到67.0%。

[阅读原文](https://arxiv.org/abs/2606.17680)

---

## 15. 信任合适的老师：GUI基础的质量意识自我升华

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jingyuan Huang, Zuming Huang, Yucheng Shi, Tianze Yang, Xiaoming Zhai, Wei Chu, Ninghao Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a quality-aware on-policy self-distillation method for GUI grounding that uses correctness-aware gating and teacher-probability scaling to improve coordinate-token teacher signals, directly advancing on-policy distillation for LLMs.

**摘要**: arXiv：2606.18101v1宣布类型：新摘要：图形用户界面（图形用户界面）基础需要视觉语言模型（VLM）来识别高分辨率屏幕截图中的小目标元素并预测精确的屏幕坐标。政策上的自我蒸馏（OPSD）对于这项坐标敏感任务来说是一种有前途的训练后方法，因为它提供了超出硬坐标标签的密集代币级教师信号。然而，天真的OPSD并不太适合图形用户界面接地：OPSD根据学生生成的前置来评估教师，当前置已经偏离目标坐标时，坐标令牌教师信号的质量可能会下降，从而导致教师信号不可靠。为了缓解这一问题，我们提出了基于VLM的图形用户界面接地的质量感知自蒸馏，通过软正确性感知门控和教师概率缩放来提高协调令牌教师信号质量。软正确性感知门检查教师当前的坐标令牌预测是否仍然可以完成到学生生成的前置码下的地面真值框中。如果不是，则相应的老师信号被向下加权。然后，教师概率缩放使用教师的信心作为轻量级因素来进一步校准门控监督的强度。一个关键的经验发现是，两个组成部分都无法单独提高总体绩效，而将它们结合起来持续提高绩效。这表明这两种机制发挥着互补作用：正确性感知门控抑制不可靠的协调令牌监督，而教师概率缩放则校准剩余信号的强度。六个图形用户界面基础基准测试的实验表明，我们的方法持续改进了基本模型，并优于强基线。

[阅读原文](https://arxiv.org/abs/2606.18101)

---

## 16. 学习精炼隐藏状态以实现可靠的LLM推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chia-Hsuan Hsu, Jui-Ming Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ReLAR, a reinforcement-guided latent refinement framework that iteratively updates hidden representations before decoding, directly addressing latent reasoning with a policy gradient objective.

**摘要**: arXiv：2606.17524v1宣布类型：新摘要：大型语言模型表现出强大的推理能力，但其内部推理过程在复杂的多步骤设置中可能保持不稳定，早期隐藏状态错误可能会传播到错误的预测。我们提出了Relar，这是一个动态引导的潜在细化框架，可以在解码之前迭代更新隐藏的表示。Relar保持紧凑的潜在推理状态，并使用学习的深度和动作控制器来自适应地确定细化步骤的数量和方向。控制器采用基于逐步似然改进的策略梯度目标进行训练，从而在无需显式思维链生成的情况下实现高效的输入相关推理。医学、数学、多跳推理和开放式生成基准的实验表明，Relar提高了准确性、生成质量和推理稳定性，并且比显式推理基线低得多。

[阅读原文](https://arxiv.org/abs/2606.17524)

---

## 17. SuCo：充分性引导的连续自适应推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiahao Wang, Bingyu Liang, Chenhao Hu, Longhui Zhang, Xuebo Liu, Min zhang, Jing Li, Xuelong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SuCo, a two-stage training framework with MSC-Aligned Fine-Tuning and Sufficiency-Aware Policy Optimization (RL) to dynamically control reasoning length, directly targeting reasoning efficiency via RL and latent reasoning control.

**摘要**: arXiv：2606.17687v1宣布类型：新摘要：尽管大型推理模型（LRM）在复杂任务上表现出色，但通常会生成过长的思想链（CoT），甚至会增加简单查询的计算成本。缓解这种低效率的现有努力通常依赖于离散推理模式或固定预算层，缺乏推理何时充分的原则性标准。在这项工作中，我们引入了最小充分CoT（MSC），其定义为足以产生正确答案的CoT轨迹的最短前置。我们经验表明，MSC不仅减少了推理令牌，而且还提高了跨难度级别的准确性。在MSC的基础上，我们提出了充分性引导的连续自适应推理（SuCo），这是一个用于沿着连续频谱进行自主推理控制的两阶段训练框架。在第一阶段，MSC对齐微调（NSX）使用问题自适应充分性阈值来构建MSC数据，该阈值随着问题难度自然扩展，然后微调模型以内化简洁但充分的推理模式。在第二阶段，充分性意识政策优化（SPP）通过具有动态复杂性跟踪和有效性意识奖励的强化学习进一步优化模型，惩罚过度思考和不足思考。跨越数学、代码和科学基准的广泛实验表明，SuCo在准确性和推理效率方面不断提高。

[阅读原文](https://arxiv.org/abs/2606.17687)

---

## 18. 定点推理器：稳定且自适应的深环变形金刚

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sajad Movahedi, Vera Milovanovi\'c, Shlomo Libo Feigin, Alexander Theus, Thomas Hofmann, Valentina Boeva, T. Konstantin Rusch, Antonio Orvieto

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a looped Transformer with fixed-point convergence as an end-to-end halting mechanism for adaptive latent reasoning, directly addressing signal propagation in deep looped architectures.

**摘要**: arXiv：2606.18206v1宣布类型：新摘要：循环体系结构提供了一种归纳偏见，即学习需要组合推理的任务的分步过程。循环达到的有效层数量决定了这些模型找到的解决方案的质量。与深度架构一样，当暂停决策被推迟时，环形架构容易出现深度引发的信号传播问题。在本文中，我们使用预规范层和剩余缩放来解决这个信号传播问题。在这些架构修改的基础上，我们提出了FPRM，这是一种基于转换器的定点推理模型，它使用定点收敛作为循环架构中的端到端停止机制。我们表明，定点停止允许FPRM调整其计算以适应任务难度。FPRM对常见推理基准（即数独、迷宫、状态跟踪和ARC-AGI）有效。

[阅读原文](https://arxiv.org/abs/2606.18206)

---

## 19. STAR：用于文本到图像RL后训练的时空自适应奖励分配

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jinjie Shen, Wei Deng, Xian Hu, Daiguo Zhou, Jian Luan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a spatiotemporally adaptive reward allocation method for RL post-training of text-to-image diffusion models, using attention maps to focus policy updates on relevant latent regions.

**摘要**: arXiv：2606.17979v1宣布类型：新摘要：用于文本到图像生成的现有RL后训练方法通常将最终图像奖励转换为单个纯量优势，并将其以相同的强度应用于整个生成轨迹。然而，文本到图像的生成自然具有时间和空间结构：不同的去噪步骤负责不同的生成阶段，而真正决定文本对齐的内容往往只出现在图像的一部分中。这种粒度不匹配使得策略更新很难专注于实际影响回报的生成性组件。为了解决这个问题，我们提出\textBF{SpatioTemporal Adaptive Reward（STAR）Allocation}用于文本到图像扩散和流模型的RL后训练。STAR在生成模型中使用文本图像关注，并从用户在提示中真正关心的核心内容开始。它构建了在去噪步骤和展开中动态变化的空间分配地图，并将相同的组相对优势分配给更相关的潜在区域，几乎没有额外的计算负担。然后，STAR通过空间分解的政策目标对这些地区进行更强有力的政策更新。我们使用Stable Distance 3.5 Medium作为基本模型，并评估三项任务：GenEval、OCR文本渲染和PickScore。实验结果表明，STAR在不改变外部奖励来源的情况下改进了合成语义对齐、文本渲染和偏好优化，分别在GenEval、OCR和PickScore上实现了$\mathBF {0.9759}$、$\mathBF{0.9757}$和$\mathBF{23.60}$。

[阅读原文](https://arxiv.org/abs/2606.17979)

---

