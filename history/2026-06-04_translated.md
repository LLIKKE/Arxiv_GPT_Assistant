# 💡 今日研究速览 (Daily Summary)

# SFT和对齐
一系列重要的工作解决了当前基于RL的对齐管道的根本限制。研究表明，一致性培训可能会自相矛盾地强化阿谀奉承，凸显天真对齐方法中的关键失败模式。为了打击奖励黑客攻击，HARVE等新颖方法提出了对奖励头部进行免训练编辑，而机械分类则对RL HF中的崩溃和评估器游戏进行系统性分类。在合成方面，QUBRIC等框架通过共同设计查询和标题，使RL能够超越可验证的奖励，并提出了合成增强方法来扩展WLVR任务，减少对昂贵的人类策展的依赖。

# LLM RL（推理和后培训）
这一类别是最激烈的活动，明确重点是完善奖励信号和训练动态。有几部作品引入了细粒度的流程奖励：ARBOR为搜索代理使用可重复使用的标题缓冲区，KnightFold通过内省偏好学习惩罚冗余推理步骤，Hidden-Align对齐正确展开的隐藏状态。新的优化范式出现，包括用于无行为概率的同步后训练的ASymPO、具有自蒸馏的物理引导策略优化以及减少梯度方差的零阶优化器GRJO。高效的超参数优化和FGRPO（用于非IID数据）等联邦变体解决了可扩展性，而FiRe-OPD等方法则通过联合过滤和重新加权轨迹来重新考虑优化粒度。一个值得注意的趋势是对多样性的探索，HDPO激励多元化的解决方案探索，并建立了一个使用奖励不确定性来诱导不同行为的原则框架。

# 潜在推理与效率
该领域正在积极重新定义推理的结构方式，超越单一的思想链。分层和自适应潜在推理模型占主导地位，ALAR等作品根据任务难度在潜在和显式CoT之间切换，以及HybridThinker将CoT压缩到记忆令牌中。子目标持久性（在“何时重新规划”中）和指标空间接地（MeRa）解决了稳定性与适应性的权衡。对于多模式推理，SpecFlow使用频谱渐进方法来实现有限记忆，而想象感知令牌则将中间感知表示具体化。效率延伸到推理，基于RL的控制器用于动态退出层（LEDE）和测试时的自适应采样，以及用于长推理链的值感知随机KV缓存驱逐。

# 代理（自我改进和多代理）
一个重大的范式转变是随着时间的推移学习和巩固技能的自我进化主体的出现。SkillPyramid和EvoDS等框架通过agentic RL实现分层技能整合和上下文管理。LLM的“睡眠”范式使用基于RL的模仿和梦想来持续自我完善。多智能体系统正在通过社会化进化（SAGE）和联邦技能学习（FederatedSkill）演变为去中心化经济（思想经济）。工具使用是一个关键焦点，PROVE在实时环境中使用编程奖励，TAO-RL将工具感知过滤与信息引导探索结合起来。实际应用包括安全关键型自动驾驶（EvoDrive）和患者轨迹建模（Traj-Evolve）。培训终端代理的教学见解表明，由于基于环境的监督，得分较低的代理可以矛盾地产生更好的教学数据。

# 多模式和视觉推理
视觉推理正在通过专门的RL框架和潜在推理机制来解决。VEPO将视觉敏感性与代币信息融合在一起以进行信用分配，而DRTL则使用可验证的奖励进行空间推理。P#2-DPO通过校准在知觉加工中引发幻觉。趋势是将抽象推理建立在底层视觉或空间度量空间中，正如MeRa和Imaginative Percept Tokens所示。体验驱动的自我进化还延伸到文本到图像生成（MemoGen），过去的经验可以改善未来的输出。

# 压缩和效率
效率问题在多个层面得到解决。对于推理，HybridThinker和SpecFlow将中间思想压缩成紧凑的表示。在推理级别，基于RL的控制器动态地管理计算（例如，推测解码退出、自适应采样）。KV缓存管理采用了一种新颖的免训练方法，可以保护大幅度值状态。在训练方面，GRZR和高效的超参数优化减少了RL后训练的计算负担。

---

## 1. EvoTrainer：共同发展的LLM政策和自主强化学习的培训利用

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Guhong Chen, Yingcheng Shi, Yongbin Li, Binhua Li, Xander Xu, Hu Wei, Shiwen Ni, Min Yang, Jieping Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EvoTrainer, a framework for co-evolving LLM policies and training harnesses in an autonomous RL loop, directly addressing self-improving agents and RL for LLMs.

**摘要**: arXiv：2606.03108v1宣布类型：新摘要：自主LLM培训通常被定义为食谱搜索，这使得培训工具基本上是静态的。这种限制在代理RL中变得更加尖锐，其中移动瓶颈和纯量奖励掩盖了不同的失败模式。我们引入EvoTrainer，这是一个自主培训框架，通过经验反馈共同发展LLM政策和培训端利用：它诊断推出级证据、修改诊断、回测干预措施并积累可重复使用的技能。EvoTrainer在数学推理、竞争性编程代码生成和存储库级软件工程方面进行了评估，在相同的数据、代码库和评估协议下，EvoTrainer与人工工程RL参考相匹配或超过，在长期代理SWE方面获得了最大的收益。轨迹分析表明，保留策略在各个领域之间存在分歧，不断发展的诊断可以防止无效的高分分支被提升，而可重复使用的技能则塑造了以后的搜索。自主LLM RL应该超越配方搜索，转向政策和解释政策的培训工具的联合演变。

[阅读原文](https://arxiv.org/abs/2606.03108)

---

## 2. 何时重新计划：分层潜在推理中的子目标持久性

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ayushi Chadha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hierarchical latent reasoning model with subgoal persistence, directly addressing the stability-adaptivity tradeoff in latent reasoning.

**摘要**: arXiv：2606.03741v1宣布类型：新摘要：长期推理要求系统致力于中期意图，而不会变得僵化：重新计划太频繁，计算永远不会整合到多步骤结构中;承诺太长，计划就会过时。我们在潜在推理环境中研究这种稳定性与适应性的权衡，其中多步计算发生在隐藏状态内，而不是外部化令牌痕迹内。我们用封建风格的管理者-工作者界面扩展了分层推理模型（HRM）：缓慢的高级模块周期性地发出一个规范化的方向子目标，该子目标持续P个低级步骤，从而偏向工作者的隐藏状态更新并提供固有的cos对齐损失。在ARC和ConceptARC上，我们发现子目标持续性（而不是单独的子目标注入）是中心旋钮：[3，6]中的中等时期P始终优于非常频繁（P=1）和非常长的视野，P=3时明显最小LM损失（P=1时，1.544 vs 1.674，基线为1.640;在5个种子上重复，平均值为1.595，标准差为0.045）。固有对齐权重Lambda显示出互补的窄最佳值（Lambda约为0.05）。当对准信号超过其最佳值时，在过去最佳点Lambda处的受控消融将学习到的方向结构（而不仅仅是架构容量或辅助损失）隔离为干扰源。这些发现共同暗示了潜在推理系统中组合规划的设计原则：中视野意图必须在足够多的计算步骤中保持一致，以形成组合结构。

[阅读原文](https://arxiv.org/abs/2606.03741)

---

## 3. ARBOR：通过可重复使用的Rubric Buffer为搜索代理提供在线奖励

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zheng Liu, Longxiang Zhang, Xintong Wang, Zhiang Xu, Shaoxiong Zhan, Xin Shan, Wen Huang, Tao Dai, Shu-Tao Xia, Chengfu Huo, Liang Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ARBOR, a novel online process-reward framework with a reusable rubric buffer for RL training of search agents, directly addressing RL for LLMs with a new reward design and training recipe.

**摘要**: arXiv：2606.03239v1宣布类型：新摘要：基于LLM的搜索代理主要接受仅结果奖励的训练，从而使搜索过程本身没有监督。该信号在结果均匀的组上退化，其中所有采样轨迹都具有相同的正确性，从而产生零组内优势并且没有梯度。现有的流程监督要么训练成本高昂的验证器，要么生成每个查询之间不一致并在使用一次后丢弃的每个查询标题。我们提出了ARBOR（在线奖励自适应Rubric Buffer），这是一个可重复使用的流程奖励框架，可以维护在查询之间共享的Rubric内存。由对比轨迹引发的查询本地草稿被接受，合并到交叉查询常用标题中，并随着政策的发展而退役。常见指标的一小部分活跃子集通过稀疏成对判断对轨迹进行评分，并将所得分数添加到基本奖励中，即使结果奖励均匀，也提供过程级梯度。ARBOR在四个多跳QA基准上始终优于GRPO和DAPO基线，将LLM评委的平均准确性提高了4.2个百分点，并将高达42%的零梯度训练组转化为信息丰富的训练组。

[阅读原文](https://arxiv.org/abs/2606.03239)

---

## 4. KnightFold：通过内省偏好学习折叠推理链

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziyan Liu, Xueda Shen, Yuzhe Gu, Songyang Gao, Kuikun Liu, Guangran Cheng, Chengqi Lyu, Dahua Lin, Wenwei Zhang, Kai Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ThoughtFold, a framework using introspective preference learning to penalize redundant reasoning steps in CoTs, directly addressing RL for LLM efficiency via fine-grained reward signals.

**摘要**: arXiv：2606.03503v1宣布类型：新摘要：得益于思想链（CoTS）上的可验证奖励强化学习（WLVR），大型推理模型（LRM）取得了显着进展。然而，由于长CoT自然包含尝试和错误，并且主流的WLVR方法选择结果正确的CoT轨迹进行记忆，因此长CoT中的多余探索不可避免地得到加强，从而导致LRM的过度思考问题。之前解决这个问题的尝试主要是更短的轨迹更有优势，但它们的学习信号仍然基于结果，并且无法减少长CoT中冗余探索的记忆。因此，我们提出了BrightFold，这是一个利用细粒度偏好学习来减少冗余探索以实现高效推理的框架。KnightFold采用内省策略来识别每个正确轨迹内的冗余，从而产生一系列候选子轨迹。利用这一频谱，我们引入了一个掩蔽偏好优化目标，该目标明确惩罚冗余探索，并鼓励模型直接连接基本推理片段，有效地将其推理链折叠成更简洁的路径。大量实验表明，BrightFold显着提高了效率。它将DeepSeek-R1-Distill-Qwen-7 B的代币使用量减少了约56%，同时保持最先进的准确性。

[阅读原文](https://arxiv.org/abs/2606.03503)

---

## 5. 正确造就力量：对齐已验证的隐藏状态增强RL推理能力

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziyue Wang, Aomufei Yuan, Yongfu Zhu, Shuai Dong, Wenpu Liu, Yiran Yao, Weichu Xie, Yuqi Xu, Caoyuan Ma, Wenqi Shao, Xiaoying Zhang, Nan Duan, Jiaqi Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Hidden-Align, a novel auxiliary loss for RLVR that aligns hidden states of correct rollouts at the anchor token, directly improving LLM reasoning via a new reward-aligned training method.

**摘要**: arXiv：2606.03234v1宣布类型：新摘要：来自可验证奖励的强化学习（WLVR）已成为改进大型语言模型中数学推理的主要方法，但当前的方法将每个正确的展开减少到单个奖励位，忽略了其隐藏状态之间共享的几何结构。调查这个结构，我们发现在锚代币处（答案标记之前的位置），正确的展开会自然收敛，因为它们必须产生相同的答案（cos相似度~0.84），但每个都保留了其独特推理路径的剩余方差。此时鼓励完全对齐可以推动模型提取统一的“正确决策”表示，降低对所采取的推理路径的敏感性。基于这一观察，我们提出了Hidden-Align，这是一种辅助损失函数，它在RL训练期间将正确展开的最后一层隐藏状态对齐在锚点标记处，训练和推理的开销均为零。在八个数学推理基准上，Hidden-Align在Qwen 3 -1.7B、4 B和14 B上分别将平均通过率@1提高了3.8、6.2和5.4个百分点，在所有三个尺度上都获得了一致的通过率@k收益，并得到了损失类型、锚位置、层深度和损失重量的消融的支持。

[阅读原文](https://arxiv.org/abs/2606.03234)

---

## 6. 光是不够的：通过视觉锚定令牌选择解锁视觉推理的有效强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Senjie Jin, Peixin Wang, Boyang Liu, Xiaoran Fan, Shuo Li, Zhiheng Xi, Jiazheng Zhang, Yuhao Zhou, Tao Gui, Qi Zhang, Xuanjing Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (VEPO) for visual reasoning that integrates visual sensitivity with token entropy for credit assignment, directly addressing RL for LLMs with a new reward/selection mechanism.

**摘要**: arXiv：2606.03937v1宣布类型：新摘要：虽然代币级的信息量被普遍认为对于具有可验证奖励的纯文本强化学习（WLVR）中的信用分配有效，但目前尚不清楚这种机制是否仍然适用于视觉推理。我们的对照研究表明，由于省略了具有自然低熵的视觉敏感标志，这种机制在视觉推理中崩溃。尽管现有的多模式RL方法越来越认识到视觉感知的重要性，但它们很难满足将精确的感知基础与语义推理交织在一起的固有需求，要么缺乏系统的视觉测量，要么忽视了标志性信息的主要驱动语义探索。为了解决这个问题，我们引入了VEPO（用于政策优化的视觉-Entropy代币选择），这是一个有效的RL框架，通过有原则的相乘耦合将视觉敏感性与代币信息量显式集成，其中VEPO将梯度信用重定向到同时具有视觉基础和信息量高的代币。广泛的实验证明了VEPO的领先性能，在7 B量表下显着优于仅含信息量的基线2.28分，在3B量表下显着优于仅含信息量的基线3.15分。消融进一步证实了我们方法的合理性。

[阅读原文](https://arxiv.org/abs/2606.03937)

---

## 7. 利用验证一代差距：具有保密条件验证的测试时强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiahui Li, Jianfeng Shan, Wenpei Chen, Shunyu Wu, Jian Lou, Wenjie Feng, Dan Li, See-Kiong Ng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a confidence-conditioned verification framework for test-time RL that improves Pass@k coverage and Pass@1 performance in label-free LLM reasoning.

**摘要**: arXiv：2606.03608v1宣布类型：新摘要：测试时强化学习已成为一种有前途的范式，可以以完全无标签的方式增强大型语言模型的复杂推理能力。尽管现有研究重点关注Pass@1性能，但优化Pass@k仍然没有得到充分探索，但在无标签环境中至关重要，无标签环境可以衡量发电覆盖率以进行持续探索。在无标签设置中优化Pass@k是非常重要的，因为直接应用对RLVR有效的Pass@k优势设计会产生不令人满意的性能。通过深入的实证分析，我们发现了阻碍性能的根本原因：低置信度样本的伪标签估计有很高的概率是不正确的，而高置信度样本的候选答案遭受严重的多样性崩溃。为了克服这些障碍，我们提出了TTRL-CoCoV（具有置信度条件验证的测试时强化学习），这是一种新颖的置信度自适应框架，可以扩展Pass@k覆盖范围并提高Pass@1性能。基于我们的关键见解，即验证能力通常会导致生成能力，TTRL-CoV采用了一种置信度条件机制：对于高置信度样本，它引导验证器并应用探索增强奖励以防止多样性崩溃;对于低置信度样本，它将伪标签选择委托给验证器以过滤不正确的伪标签;对于中等置信度样本，它完全绕过验证。大量实验表明，与完全监督的RL方法相比，TTRL-CoCoV在6个广泛认可的基准上优于最佳竞争方法，在Pass@1中实现了+9.8%的平均绝对收益，在Pass@16中实现了+18.7%的平均绝对收益，甚至在多个推理基准上实现了高达+5.0%的绝对Pass@1改进。我们的代码存储库：https://github.com/shanjf666/CoCoV。

[阅读原文](https://arxiv.org/abs/2606.03608)

---

## 8. 自适应隐性统计推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Dongwon Jung, Peng Shi, Yi Zhang, Junshan Zhang, Muhao Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ALAR, a dual-mode framework for LLM agents that uses latent reasoning for routine turns and explicit CoT for hard decisions, directly addressing latent reasoning and agent efficiency.

**摘要**: arXiv：2606.02871v1宣布类型：新摘要：大型推理模型通过生成扩展思想链（CoT）推理来提高性能，但这种行为在应用于LLM代理时变得效率低下。当前的LLM代理通常在每个决策步骤生成冗长的文本推理，并在回合之间几乎均匀地分配推理工作，导致多回合代理轨迹的效率大幅低下。我们提出了自适应潜在推理（ALAR），这是一种双模式框架，它对常规转变使用紧凑的潜在推理，并在需要更深入的思考时选择性地升级到显式思想链。ALAR通过使用代理的动作作为监督锚来学习潜在推理，并进一步优化为在足以实现任务成功时使用潜在推理，并为更难的决策保留显式CoT。对代理搜索和工具使用基准的实验表明，ALAR保持了相当或更好的任务准确性，同时在搜索中将生成的令牌大幅减少了高达43.6%，在工具使用中将生成的令牌大幅减少了84.6%。这些结果表明，ALAR通过减少不必要的文本推理，同时保留对更困难的决策步骤的明确审议，改善了LLM代理的准确性-效率权衡。

[阅读原文](https://arxiv.org/abs/2606.02871)

---

## 9. HybridThinker：通过压缩记忆和瞬时思维步骤进行高效的思想链推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xin Liu, Runsong Zhao, Xinyu Liu, Junhao Ruan, Pengcheng Huang, Shichao Dong, Chunyang Xiao, Chenglong Wang, Changliang Li, Jingbo Zhu, Tong Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HybridThinker, a latent reasoning method that compresses CoT into memory tokens while retaining transient thought steps, with a hybrid training scheme to force effective compression.

**摘要**: arXiv：2606.03768v1宣布类型：新摘要：扩展思想链（CoT）痕迹改进了LLM推理，但会产生巨大的计算和内存成本。虽然现有的CoT压缩方法通过通过记忆令牌将思维步骤浓缩为紧凑的表示并在推理时仅保留这些表示来缓解这一问题，但细粒度信息的丢失使后续步骤更容易出错。为了缓解这个问题，我们提出了\textBF{HybridThinker}，其中除了保留这些表示之外，还暂时保留思维步骤以提供细粒度的细节。然而，我们观察到，天真地保持思维步骤可访问的后续步骤\{在训练期间}会让模型通过直接从这些步骤检索信息来绕过记忆令牌，从而导致模型通过记忆令牌压缩和检索信息的能力训练不足。因此，我们引入了一种混合训练方案，其中只有一些思维步骤可以通过关注后续步骤直接访问，而其他思维步骤则被屏蔽，迫使模型使用记忆令牌进行压缩和检索。在4个推理基准中，HybridThinker匹配未压缩的基线，在相似的推理时间下将CoT压缩的平均准确性提高了5.8个百分点。消融研究证实，暂时的思想步骤保留和混合训练计划都有助于这些收获。

[阅读原文](https://arxiv.org/abs/2606.03768)

---

## 10. 具有信息量指导的工具感知优化，以实现高效的统计强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongye Cao, Nuo Yan, Haoyuan Deng, Ziwei Wang, Tianpei Yang, Jing Huo, Yuyao Zhang, Yang Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TAO-RL, a unified framework coupling tool-aware trajectory filtering with entropy-guided exploration for efficient agentic RL, directly addressing RL for LLMs and self-improving agents.

**摘要**: arXiv：2606.03762v1宣布类型：新摘要：抽象强化学习（RL）为大型语言模型（LLM）配备了工具使用能力，可以大幅改善复杂任务的推理。然而，集成外部工具往往会破坏培训的稳定：过度依赖工具可能会导致输入分布转变，而过于保守的工具使用则限制了有效的探索。为了解决这个问题，我们提出了一个统一的框架TAO-RL，该框架将工具感知轨迹过滤与信息引导探索结合起来，以实现高效的策略优化。具体来说，在数据层面，TAO-RL根据两个标准过滤展开轨迹：丢弃所有工具调用都未能执行的轨迹，并删除所有工具调用都正确或不正确的轨迹，因为这两种情况都会产生退化优势估计，不会贡献任何区分性学习信号。这种联合过滤保留了既可使用工具又可提供信息的数据，从而建立高质量的训练分布。在算法层面，我们引入了一种工具感知的、由信息引导的奖金，该奖金重塑了工具调用后代币的优势函数，鼓励政策在关键决策点探索更多样化的推理路径。这两个部分是相辅相成的：轨迹过滤建立了清晰且信息丰富的训练基础，而信息引导的探索则在关键的工具交互路口推动了更强的推理行为。在3个模型尺度上对7个具有挑战性的推理基准进行了大量实验，证明了TAO-RL优于现有方法。

[阅读原文](https://arxiv.org/abs/2606.03762)

---

## 11. 合成和奖励--在实时环境中多步骤工具使用的强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ibrahim Abdelaziz, Asim Munawar, Kinjal Basu, Maxwell Crouse, Chulaka Gunasekara, Suneet Katrekar, Pavan Kapanipathi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (PROVE) with programmatic rewards and live-execution environments for multi-step tool use, directly matching RL for LLMs and self-improving agents.

**摘要**: arXiv：2606.03892v1宣布类型：新摘要：训练LLM协调多步骤工具调用受到三个相互关联的障碍的阻碍：真实的有状态执行环境的构建成本高昂，合成训练查询通常与服务器的实际状态脱节（因此生成的工具调用无法执行），基于回忆的RL奖励激励冗长的工具调用模式。我们提出证明（已验证环境的程序化奖励），一个具有三项贡献的框架：（1）包含20个有状态的LCP的库（模型上下文协议）服务器公开343个工具，通过会话范围的状态隔离实现实时执行RL训练;（2）自动化数据合成管道，通过依赖图生成针对这些服务器的经验证的多回合工具调用轨迹基于实时采样的服务器状态的引导式对话模拟，因此生成的每个查询都引用实际存在的实体;以及（3）多组件程序奖励-分级有效性评分、依赖性感知覆盖、具有复杂性缩放呼叫预算的自适应效率惩罚、工具名称信号，以及论据价值匹配奖金-不需要外部评委模型。我们使用相同的奖励超参数和约13 K个训练示例，使用GRPO训练四个模型（Qwen 3 - 4 B、Qwen 3 -8B、Qwen 2.5 - 7 B、Granite-4.1-8B）;每个模型家族仅调整学习率。在BFCL Multi-Turn、tau 2-bridge和T-Eval上，PROVE分别提高了+10.2、+6.8和+6.5分，证明紧凑的程序奖励可以在两个模型系列的多步骤工具编排方面产生一致的收益。

[阅读原文](https://arxiv.org/abs/2606.03892)

---

## 12. 学会解决问题，忘记保留：WLVR中正确设定的周转率

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chuanyu Qin, Chenxu Yang, Qingyi Si, Naibin Gu, Peng Fu, Zheng Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a retention-aware review mechanism for RLVR that addresses correct-set turnover, a novel RL training recipe for LLMs.

**摘要**: arXiv：2606.03087v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）提高了大型语言模型的能力，但标题准确性的提高往往掩盖了隐藏的成本：随着训练的进行，之前解决的问题悄然变得无法解决。我们将这种现象定义为\{correct-set turnover}，代表解决方案获取和掌握集中回归的耦合动态。在这种观点下，保留与收购一起成为明确的优化目标。我们通过分析和经验建立了\{修复窗口原则}：恢复倒退提示的成本随着审查延迟而急剧增加，从而定义了标准WLVR管道无法利用的低成本窗口。为了解决这个问题，我们提出了\textBF{\system {}}，这是一种保留感知的审查机制，可以跟踪掌握的提示并定期将它们重新引入到\textBF{reform}之前解决方案的模型中。通过利用部署前批量替换，\方法{}产生的额外部署费用为零。使用Qwen 3-BL和Qwen 2.5-Math对涵盖图像-文本、视频和纯文本任务的20个基准进行了评估，\system {}持续提高了超过GRPO、DAPO和重播基线的性能，展示了跨模式和算法的强大通用性。

[阅读原文](https://arxiv.org/abs/2606.03087)

---

## 13. SkillPyramid：自我进化代理的分层技能整合框架

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuan Xiong, Ziqi Miao, Qian Chen, Lijun Li, Yequan Wang, Shizhu He, Jun Zhao, Kang Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SkillPyramid, a hierarchical skill consolidation framework with a self-evolution mechanism for agents to compose and improve skills over time, directly addressing self-evolving agents.

**摘要**: arXiv：2606.03692v1宣布类型：新摘要：最近的人工智能代理可以灵活地调用技能来解决复杂任务，但其长期改进从根本上受到缺乏系统性技能构建、积累和转移的限制。特别是，如果没有统一的技能整合框架，代理往往会在不同任务中冗余地构建类似的能力，无法有效地将经验转化为可重复使用的资产，并且很难将特定任务的技能推广到新的场景。为了解决这一局限性，我们提出了SkillPyramid，这是一个技能整合框架，可以重复利用现有技能经验进行更广泛的任务概括。SkillPyramid在分层技能布局上运行，进一步引入了一种自我进化机制，使代理能够在任务执行期间构建、验证和整合新技能。在ALFWorld、WebShop和ScienceWorld上对四个主干模型进行的实验表明，SkillPyramid将平均奖励大幅提高了38.0%，并将执行步骤减少了27.7%。总体而言，我们的方法将技能集合从静态资源池转换为动态进化系统。

[阅读原文](https://arxiv.org/abs/2606.03692)

---

## 14. 用于轻量级多模态推理的谱-渐进思想流

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Yixian Shen, Zhiheng Yang, Qi Bi, Changshuo Wang, Shuai Wang, Jia-Hong Huang, George Floros, Prayag Tiwari, Anuj Pathania

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent reasoning framework (SpecFlow) that represents intermediate visual thoughts in a fixed-size discrete cosine space, enabling bounded memory and stable latency for multimodal reasoning.

**摘要**: arXiv：2606.02842v1宣布类型：新摘要：多模式空间推理通常依赖于中间文本和视觉思想的长链，其中积累的视觉标记和密集的跨模式注意力会导致大量的计算和记忆负担。为了应对这一挑战，我们提出了Spectral-Progressive Thought Flow（SpecFlow），这是一种新型的轻量级多模式空间推理框架，可以在固定大小的离散Cosin空间中表示中间视觉思想。通过利用强大的能量压缩，SpecFlow保留了全局布局和关系结构，同时仅在需要提高空间精度时引入高频细节。为了使视觉状态演变与语言意图保持一致，无分类器引导自回归文本思维能够引导视觉工作空间/状态的基于流的更新，而无需扩展上下文。因此，SpecFlow维护了一个有界的视觉工作空间，其更新仅取决于当前的视觉状态和累积的文本痕迹，从而能够以稳定的延迟和独立于推理深度的内存使用情况进行长视野推理。经验结果表明，SpecFlow实现了有竞争力或卓越的推理性能，同时将计算和KV缓存成本降低了高达2.1倍。

[阅读原文](https://arxiv.org/abs/2606.02842)

---

## 15. 一致性培训可能会加剧错位

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: David Demitri Africa, Arathi Mani

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates how consistency training affects LLM alignment, showing it can amplify sycophancy, which is directly relevant to RL-based alignment methods.

**摘要**: arXiv：2606.03810v1宣布类型：新摘要：一致性培训鼓励模型在相关输入或抽样程序中产生类似的输出。此类方法简单、可扩展且基本上无需标签，但其对模型对齐的影响仍然知之甚少。这些方法的自引导性质是否会放大模型中不希望的行为？我们对108个“模型生物体测试了七种一致性训练方法：经过微调的开源模型（7 B--70 B），以表现出各种形式的受控失准行为。我们发现结果差异很大：一致性培训通常会抑制奖励黑客和紧急失调，但会放大谄媚。我们提出的证据表明，一致性标记过程引起的分布变化，而不是选择操作符的变化，可能是系统性对齐效应的主要驱动因素。最后，我们提出了一个统一的理论框架来推导一致性训练将放大或抑制失准的条件。总的来说，我们的研究确定一致性培训并非中立的，并且应该仔细审计其在关键系统中的使用。

[阅读原文](https://arxiv.org/abs/2606.03810)

---

## 16. 语言模型需要睡眠：学会自我修改和巩固记忆

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Ali Behrouz, Farnoosh Hashemi, Vahab Mirrokni

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a 'Sleep' paradigm for LLMs that uses RL-based imitation learning and dreaming for continual self-improvement and memory consolidation, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2606.03979v1宣布类型：新摘要：过去几十年见证了机器学习算法设计方面的重大进展，从对特定任务浅层模型的早期研究到更通用的深度大型语言模型（LLM）。尽管在需要即时预测或上下文学习的任务中显示出有希望的结果，但现有模型缺乏持续学习和有效地将其暂时上下文知识转化为长期参数的能力。受人类学习过程的启发，我们引入了一种“睡眠”范式，允许模型不断学习，通过重播将短期脆弱的记忆提炼成稳定的长期知识，并通过“做梦”过程来迭代改进自己。更详细地说，睡眠由两个阶段组成：（1）记忆巩固：一个向上蒸馏的过程，称为知识播种，将较小的自我的记忆蒸馏到更大的网络中，以在保留知识的同时提供更多容量。作为概念证明，我们为{Knowledge Seeding}提出了一个新的广义蒸馏过程（即，政策提炼与基于强化学习（RL）的模仿学习的结合）;（2）梦想：自我改进阶段，模型使用RL来生成合成数据课程，以排练新知识并在没有人类监督的情况下完善现有能力。我们关于长期、持续学习、知识整合和少量概括任务的实验支持了睡眠阶段的重要性。

[阅读原文](https://arxiv.org/abs/2606.03979)

---

## 17. 利用奖励不确定性在强化学习中诱导多样化行为

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Anthony GX-Chen, Ankit Anand, Gheorghe Comanici, Zaheer Abbas, Eser Ayg\"un, David Smalling, Shibl Mourad, Doina Precup, Andr\'e Barreto, Mark Rowland

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a principled RL framework that induces diverse behavior by treating reward as a distribution, with a novel gradient estimator and theoretical generalization of policy gradient, directly relevant to RL for LLMs.

**摘要**: arXiv：2606.03962v1宣布类型：新摘要：经典强化学习（RL）通常寻求一种确定性策略，以最大化量化奖励的预期总和。然而，语言模型微调或科学发现等现代应用需要多样性。现有的补救措施，例如信息质量规范化或多样性奖金，通常需要脆弱的权衡，为了随机性而牺牲性能，或者依赖可能导致政策排名不一致的启发式指标。我们认为，多样性更自然地被理解为对奖励不确定性的理性反应。当奖励函数并不完全已知时--就像模糊的偏好或不完美的奖励模型的情况一样--致力于单一行动可能是次优的。在此基础上，我们提出了对RL目标的根本重新制定，通过用奖励函数上的分布取代纯量奖励，并对动作集应用非线性目标。其结果是一个框架中，校准的行为多样性自然出现，保持可控的奖励函数分布，并获得不牺牲预期的奖励。专注于上下文的强盗设置，我们推导出一个原则性的梯度估计为这个目标，并证明我们的配方自然概括香草政策梯度和最近开发的行动集的方法。我们的实证结果表明，这个框架提供了一个强大的和理论上接地复杂的RL任务的替代传统的配方的问题，未能诱导所需的代理行为的广度。

[阅读原文](https://arxiv.org/abs/2606.03962)

---

## 18. 思想经济：新兴的多智能体智能与经济互动

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Zhenting Qi, Huangyuan Su, Ao Qu, Chenyu Wang, Yu Yao, Han Zheng, Kushal Chattopadhyay, Guowei Xu, Zihan Wang, Weirui Ye, Vijay Janapa Reddi, Ju Li, Paul Pu Liang, Himabindu Lakkaraju, Sham Kakade, Yilun Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a decentralized agent economy where agents self-improve via economic selection, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2606.02859v1宣布类型：新摘要：在没有集中控制的情况下，一群代理人如何自我编排和自我适应到更强大的集体智能中？受弗里德里希·海耶克关于市场去中心化协调的经济理论的启发，我们通过代理经济来研究这个问题，在代理经济中，代理人通过拍卖争夺行动权、交换支付和从环境回报中积累财富的权利。这些简单的经济信号引发了去中心化的信用分配，在没有全球编排或明确通信协议的情况下推动规划。人口通过经济选择进化：有效的主体积累财富并通过剥削而变异，而无效的主体则破产并通过探索而被取代。我们表明，在以弱代理初始化的情况下，经济会产生紧急的多步推理策略，并且在五个代理任务（包括数学推理、金融研究、科学研究、加速器设计和分布式系统优化）中表现优于更强的整体基线。我们进一步提供有关经济动态如何塑造代理人行为的理论见解，将当地激励与长期全球绩效联系起来。我们的结果提出了一条通往多主体智能的新途径：我们可以设计去中心化的激励结构，而不是工程协调，在该结构下它会自动出现。

[阅读原文](https://arxiv.org/abs/2606.02859)

---

## 19. EvoDS：具有技能学习和上下文管理的自我进化自主数据科学代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zherui Yang, Fan Liu, Yansong Ning, Hao Liu

**机构**: HKUST

**💡 亮点 (Highlight)**: Proposes a self-evolving data science agent that learns new skills and manages context via agentic reinforcement learning, directly matching the self-improving agent criterion.

**摘要**: arXiv：2606.03841v1宣布类型：新摘要：大型语言模型（LLM）代理的最新进展为自动化数据科学带来了光明的进步。然而，现有方法仍然受到静态动作集和缺乏有原则的长期上下文管理的根本限制，阻碍了它们积累跨任务的可重复使用经验以及在多阶段、迭代数据科学管道中可靠运行的能力。为了应对这些挑战，我们引入了EvoDS，这是一种自我进化的自主数据科学代理，可以通过代理强化学习来学习扩展其技能并自适应地管理长期上下文。具体来说，EvoDS引入了两个关键策略：（1）自主技能获取（ASA）机制，使代理能够合成、验证和重用可执行技能;（2）自适应上下文压缩（ACC）策略，将上下文管理视为一个习得的控制问题，而不是被动截断。这些策略是在两阶段多智能体训练计划中精心编排的，使EvoDS能够随着时间的推移自主改进。从理论上讲，我们证明了EvoDS的分层设计减少了工具选择错误，其优化目标符合信息瓶颈原则，确保了有效的上下文使用。从经验上看，EvoDS在四个不同基准上的表现比最先进的开源数据科学代理平均高出28.9%，同时消除了名义上的失败。我们的代码和数据可在https://github.com/usail-hkust/EvoDS上获取。

[阅读原文](https://arxiv.org/abs/2606.03841)

---

## 20. HARVE：具有黑客意识的奖励头部载体编辑，用于稳健的奖励模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shuang Liu, Yuxuan Bo, Qiuyang Zhao, Caiyue Huang, Xiaorong Chen, Yanguang Liu, Mengnan Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HARVE, a training-free reward-head editing method to mitigate reward hacking in LLM reward models, directly addressing RL reward model robustness.

**摘要**: arXiv：2606.03131v1宣布类型：新摘要：奖励模型是大型语言模型（LLM）对齐的核心，但它们仍然容易受到奖励黑客攻击的影响。为了评估奖励模型的稳健性，我们引入了RewardHackBench，其中包含13种奖励黑客模式，涵盖现实生活中的高风险域和一般设置，并且我们发现八个奖励模型中的特定子类别存在严重失败。为了减轻这些失败，我们提出了HARVE，这是一种针对纯量奖励模型的免训练奖励头编辑方法。HARVE没有微调奖励模型，而是从与所选黑客子类别相关的剩余流方向中识别出多方向黑客子空间，并删除与该子空间对齐的奖励头分量。这直接降低了奖励头部对黑客相关功能的敏感性，仅使用一小组对比性的黄金黑客示例，而无需梯度更新或微调。针对八个奖励模型的综合实验表明，\模型提高了黑客攻击的稳健性，优于微调基线，并保留了奖励模型的一般能力。进一步的分析表明，与孤立的表面线索相比，奖励黑客更好地捕捉为多维剩余空间结构。

[阅读原文](https://arxiv.org/abs/2606.03131)

---

## 21. Skill-RM：通过代理技能统一异类评估标准

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tao Chen, Gangwei Jiang, Pengyu Cheng, Siyuan Huang, Yihao Liu, Jingwei Ni, Jiaqi Guo, Mengyu Zhou, Kai Tang, Junling Liu, Qinliang Su, Xiaoxi Jiang, Guanjun Jiang

**机构**: Alibaba Group (Qwen)

**💡 亮点 (Highlight)**: Proposes Skill-RM, a unified reward model framework that treats reward computation as an agentic task to dynamically orchestrate heterogeneous evaluation criteria for RL pipelines.

**摘要**: arXiv：2606.03980v1宣布类型：新摘要：奖励模型（RM）为LLM后训练提供关键的反馈信号，特别是在强化微调（RFT）和强化学习（RL）管道中。然而，当前的奖励评估依赖于基于规则的验证器、基本事实参考、程序检查表和复杂的指标，其中整合所有类型证据的统一机制仍未探索。为此，我们提出了技能奖励模型（Skill-RM），这是一个统一的框架，将奖励建模重新定义为可重复使用的奖励评估技能的执行。通过将奖励计算视为结构化代理任务，Skill-RM提供了一致的接口来协调异类资源，动态选择和聚集根据每个输入的特定要求定制的证据。这种方法使奖励模型能够超越静态评估，确保不同任务的一致性和透明度。对奖励基准和下游应用程序的广泛实验（包括N中最佳选择和强化学习）表明，Skill-RM始终优于传统的判断基线。我们的研究结果表明，Skill-RM不仅为奖励建模提供了统一的解决方案，而且还通过战略性和动态的证据编排来实现卓越的性能。代码位于https://github.com/Qwen-Applications/Skill-RM。

[阅读原文](https://arxiv.org/abs/2606.03980)

---

## 22. Taiji：具有Semantics-ID权衡的帕累托最优政策优化，以实现工业LLM增强型推荐

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuecheng Li, Zeyu Song, Jing Yao, Chi Lu, Peng Jiang, Kun Gai

**机构**: Kuaishou

**💡 亮点 (Highlight)**: Proposes Pareto Optimal Policy Optimization (POPO) for RL alignment in LLM-enhanced recommendation, addressing the trade-off between semantic and preference rewards.

**摘要**: arXiv：2606.03866v1公告类型：新摘要：通过大型语言模型（LLM）扩展推荐系统已经成为行业的一个突出趋势。然而，通过后训练（例如，SFT和RL）仍然具有挑战性。现有的LLM 4 Rec范式受到两个主要问题的困扰：（1）SFT期间难以衡量和改进开放领域推荐中的思想链（CoT）质量，（2）忽视RL对齐期间LLM语义奖励和推荐偏好奖励之间的权衡。受这些挑战的启发，我们提出了Taiji，这是一种为工业推荐系统设计的新型LLM作为增强者框架。为了克服SFT瓶颈，我们利用反向工程推理和开放式拒绝采样来生成高质量的特定领域CoT数据。为了解决RL对齐问题，我们提出了帕累托最优政策优化（POPO），它自适应地调整跨域奖励权重。理论上，它实现了LLM的语义世界知识和代表在线用户偏好的协作ID特征之间的最佳权衡。广泛的线下评估和在线A/B测试验证了太极的有效性。太极自2026年5月部署在快寿的广告平台上，目前每天为超过4亿用户提供服务，产生了可观的商业收入，并展示了其在网络规模环境中强大的可扩展性。

[阅读原文](https://arxiv.org/abs/2606.03866)

---

## 23. FGRPO：对非IID数据进行自适应聚合的联合GRPO

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Pengyu Chen, Shaowei Li, Kai Wang, Yunsheng Yuan, Kai Han, Jun Luo, Feng Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FGRPO, a federated RL framework for reasoning models that adaptively aggregates client updates based on relative performance gain, directly addressing RL for LLMs with a new training recipe.

**摘要**: arXiv：2606.03094v1公告类型：新摘要：语言模型的最新进展已经将强化学习确立为引发自我纠正和长链推理的主要范式。虽然组相对策略优化（GRPO）通过消除批评者网络提供了卓越的可扩展性，但将其部署在中央基础设施上需要从分布式所有者收集大量数据，这会带来重大的隐私风险。为了解决这些问题，我们引入了联邦GRPO（FGRPO），这是一个旨在分散跨异类数据所有者的推理模型微调的框架。为了有效地减轻不同任务之间奖励规模造成的不稳定性，FGRPO结合了基于相对性能收益的自适应聚合机制。通过描述每个客户相对于其个性化历史基线的改进，该框架动态地优先考虑有效的学习轨迹，而无论本地任务的难度如何。FGRPO确保非IID数据的稳健融合，同时保护数据隐私。

[阅读原文](https://arxiv.org/abs/2606.03094)

---

## 24. 老师什么时候应该搬家？自策略蒸馏中的时间耦合和稳定性

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haowei Guo, Baolong Bi, Ruicheng Zhang, Bingqian Sun, Wentao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Consolidation-Gated Teacher Refresh (CGTR) for stable self on-policy distillation, a novel RL training recipe for LLMs that addresses temporal coupling and collapse.

**摘要**: arXiv：2606.03532v1宣布类型：新摘要：自我策略蒸馏针对源自其自身参数历史的教师训练学生策略，但教师的更新时间表（管理教师和学生之间的时间耦合）尚未作为稳定性变量进行系统研究。通过Qwen 3 -8B上的受控日程扫描，我们确定\{隔离期}（定义为更新之间的教师完全冻结）是实现稳定学习的关键结构属性，而不是教师年龄。为了描述这些潜在的训练动态，我们引入了一个时间KL结构、刷新冲击和长尾风险的诊断框架。该框架进一步揭示了\{状态不经意崩溃}：最佳短期固定时间表在长期训练下会灾难性地失败，因为时钟驱动的刷新可以在一个不可逆转的步骤中将暂时漂移的学生复制到教师中。这种故障模式在短期评估下是不可见的，并且在机制上与EMA的慢性污染不同。为了解决这个问题，我们提议\{Consolid-Gated Teacher Refresh}（CGTR），它保留了隔离期，同时根据奖励改进和长尾安全的联合证据对每次刷新进行门控，确保每次教师动作都响应真正的学生合并，而不是时钟信号。通过单个共享参数集且无需按数据集重新调整，CGTR实现了\textBF{零折叠}和所有四项任务（化学、生物、物理、工具使用）的最佳最终分数，并根据每个任务的学习动态自我调节其刷新频率。

[阅读原文](https://arxiv.org/abs/2606.03532)

---

## 25. SAGE：主体生态系统社会化进化的定量评估

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Linyue Pan, Yaoming Zhu, Lin Qiu, Xuezhi Cao, Xunliang Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a framework for evaluating socialized evolution in agent ecosystems, directly addressing self-improvement through peer experience, a core aspect of self-evolving agents.

**摘要**: arXiv：2606.03544v1宣布类型：新摘要：自我改进的语言代理通常是孤立评估的：代理尝试一项任务、接收反馈并迭代地改进自己的行为。然而，代理人越来越多地与战略和结果公开可见的同行一起运营。这就提出了一个尚未得到充分研究的问题：什么时候分享经验会产生自我改进无法实现的改进？我们介绍SAGE（社会代理组进化），一个评估框架，比较两个计算匹配的条件：SocialEvo，其中代理从五个不同的模型家庭共同发展与访问所有同行的历史;和SelfEvo，每个代理接收相同数量的任务尝试，但只看到自己的过去，这是传统的自我改进代理研究。我们在三个领域实例化SAGE：开放式ML研究，长期经济规划和战略多人游戏，在多个进化回合中进行评估。我们发现，群体历史不是一个通用的放大器：最强的代理人不会超过其自我进化的上限。然而，在自我提升下达到平台的代理人可以在同伴经验可用时实现重大突破。在竞争性环境中，反事实控制显示，代理商改善一般，而不是制定具体的策略。在不同形式的共享历史中，过滤后的同行跟踪和反思总结通常优于原始日志，这表明社交收益取决于抽象而不是曝光量。这些研究结果表明，同行历史收益是代理特定的，舞台依赖的，并取决于从公共痕迹中提取可转移知识的能力。

[阅读原文](https://arxiv.org/abs/2606.03544)

---

## 26. 潜在推理什么时候有帮助？MeRa：空间预测的度量空间偏差

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhenyu Yu, Shuigeng Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MeRa, a metric-space bias module for latent reasoning in spatial prediction, showing that grounding latent reasoning in the underlying metric space is crucial for performance.

**摘要**: arXiv：2606.03727v1公告类型：新摘要：潜在推理通过在预测之前迭代地细化表示来改进顺序推荐，但是它有助于空间预测吗？我们发现，答案取决于推理是否在底层度量空间中扎根。如果没有这样的基础，潜在推理会将空间预测降级到未修改的基线以下，而从成对距离推导出的习得度量空间偏差会产生一致的收益。我们通过MeRa（度量空间推理）形式化了这一发现，MeRa是一个轻量级的主干不可知模块，可以插入任何序列编码器及其预测头之间。在GETNext主干上，没有指标空间偏差的推理和有指标空间偏差的推理之间的差距达到了4.5% NDCG@10。在比较方法中，MeRa在所有三种空间预测基准上都达到了最佳的NDCG@10，超过了最近的方法，例如GeoMamba和HMST。我们证明了度量空间约束推理收敛到唯一的不固定点，并且N步推理比（N-1）步推理严格更具表达力。在CYVR上进行的欧几里得距离对照实验证实了这一发现的推广超出了地理坐标。该代码包含在补充材料中。

[阅读原文](https://arxiv.org/abs/2606.03727)

---

## 27. Traj-Evolve：一个自进化的多智能体系统，用于肺癌早期检测中的患者轨迹建模

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sihang Zeng, Matthew Thompson, Ruth Etzioni, Meliha Yetisgen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving multi-agent system for patient trajectory modeling using an experience pool and multi-agent RL for self-improvement, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2606.02812v1宣布类型：新摘要：根据纵向电子健康记录（EHR）对患者轨迹进行建模需要对稀疏、有噪和长背景的多模式序列进行推理。现有的基于LLM的多代理系统解决了上下文长度问题，但孤立地处理患者，未能反映临床医生如何利用从类似之前病例中积累的经验。我们提出Traj-Evolve，一个具有两种互补进化机制的自我进化多智能体系统。首先，体验池（ExPool）充当非参数存储器，索引拒绝采样的推理痕迹，以检索类似患者作为少数镜头上下文。其次，通过奖励排名微调的多智能体强化学习（MARL）参数化优化了智能体间和智能体记忆协作。留一交叉检索策略将两者统一起来，在检索增强下调整训练时和推理时行为。在利用长达五年的多模式EHR的肺癌预测任务中，Traj-Evolve在总体人群和具有挑战性的从不吸烟人群中的表现优于9个强基线。对不断变化的动力学的分析突出了三个关键发现：（1）扩展ExPool将最佳检索从不同样本转移到特定样本;（2）在MARL下，管理代理的预测损失迅速收敛，而工作代理的时间推理继续受益于更多验证患者;（3）这两种机制在预测风险方面是互补的，其中ExPool提高了特异性，而MARL提高了敏感性。

[阅读原文](https://arxiv.org/abs/2606.02812)

---

## 28. 具有自蒸馏的物理引导政策优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ke Wang, Yuning Wu, Haoran Liu, Chaoqun Jia, Devin Chen, Kai Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Physics-Guided Policy Optimization (PGPO), a novel RL method for LLM post-training that uses an information-modulated step-size to stabilize self-distilled policy optimization.

**摘要**: arXiv：2606.03620v1宣布类型：新摘要：自提炼策略优化（SDPO）已成为LLM后训练的流行范式，其中模型根据特权信息从自己的预测中学习。然而，SDPO对每个更新步骤的信任程度很敏感：自学者的更正可能对某些批次提供大量信息，而对其他批次则具有误导性，并且以固定的步骤统一应用它们可能会破坏训练的稳定性。我们从粘性流体动力学中汲取灵感，并在预设水平上正式化类比，提出了物理引导的政策优化（PGPO），它引入了一个信息调制的步进乘数，该乘数源自学生的预测和反馈条件教师之间的互信息估计。我们表明，这种调制保留了vanilla Singapore的1阶弱逼近保证，并且每次迭代所产生的开销可以忽略不计。我们在Science-QA数据集上评估了PGPO，它在4个域中的3个域上的表现优于SDPO，收益高达+4.5分，同时在SDPO在训练后期崩溃的环境中保持稳定。

[阅读原文](https://arxiv.org/abs/2606.03620)

---

## 29. P\textsuperScript{2}-DPO：通过校准直接偏好优化在感知处理中产生幻觉

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ruipeng Zhang, Zhihao Li, Haozhang Yuan, C. L. Philip Chen, Tong Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes P^2-DPO, an on-policy DPO variant for LVLMs that constructs preference pairs targeting perceptual bottlenecks and visual robustness, directly addressing RL-based alignment for vision-language models.

**摘要**: arXiv：2606.03376v1宣布类型：新摘要：幻觉最近引起了大型视觉语言模型（LVLM）的大量研究关注。直接偏好优化（DPO）旨在直接从人类提供的纠正偏好中学习，从而解决幻觉问题。尽管取得了成功，但该范式尚未专门针对关注区域的感知瓶颈，也尚未解决视觉鲁棒性不足的问题。此外，现有的偏好对通常是愿景不可知的，其固有的政策外性质限制了其指导模型学习的有效性。为了解决这些挑战，我们提出了感知处理直接偏好优化（P\textsuperScript{2}-DPO），这是一种新型训练范式，其中模型生成并从其自己的偏好对中学习，从而直接解决已识别的视觉瓶颈，同时从本质上避免了视觉不可知和政策外数据的问题。它介绍了：（1）针对聚焦并增强感知和视觉稳健性的政策偏好对构建方法，以及（2）设计良好的校准损失，以精确地将视觉信号与文本的因果生成对齐。实验结果表明，在具有相当数量的训练数据和成本的情况下，P\textsuperScript{2}-DPO的表现优于依赖于昂贵的人类对基准的反馈的强基线。此外，对注意区域保真度（ARF）和图像退化场景的评估验证了P\textsuperScript{2}-DPO在解决关注区域的感知瓶颈和针对退化输入提高视觉鲁棒性方面的有效性。

[阅读原文](https://arxiv.org/abs/2606.03376)

---

## 30. LLM强化学习的高效超参数优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Minping Chen, Bowen Xiao, Du Liang, Chuxuan Zeng, Zeyi Wen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel multi-fidelity hyperparameter optimization method for LLM RL that jointly adapts model size and training budget, directly improving RL training efficiency.

**摘要**: arXiv：2606.03073v1宣布类型：新摘要：大型语言模型（LLM）的强化学习（RL）对超参数配置高度敏感，使得超参数优化（HPO）至关重要，但计算成本高昂。由于模型规模庞大和资源密集型训练周期，现有的多保真HPO方法对于LLM RL来说仍然效率低下。在本文中，我们提出了联合保真超参数优化（JF-HPO），它同时调整模型大小和训练预算作为保真度。JF-HPO的授权如下：（i）它利用目标LLM的小型代理模型在每个HPO试验中进行高效的培训和评估;（ii）它集成了基于训练动态精心设计的早期停止策略;（iii）它引入了高效的检查点机制来消除冗余计算。与现有的HPO方法相比，JF-HPO显着提高了每次试验的计算效率（高达14.9倍），同时在相同的时间预算下实现更好或有竞争力的预测准确性。值得注意的是，与利用VeRL Recipe中的超参数配置相比，JF-HPO的性能改进范围从5.8%到111.6%。

[阅读原文](https://arxiv.org/abs/2606.03073)

---

## 31. LLM推理的提示引导多元化政策优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhiyu Cao, Kaixin Wu, Mingjie Zhong, Peifeng Li, Xiaobo Li, Can Ye, Qiaoming Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new RLVR method (HDPO) with a hint-guided diversified policy optimization that explicitly incentivizes diverse solution exploration and selection, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2606.03021v1宣布类型：新摘要：大型语言模型（LLM）的最新发展展示了令人印象深刻的推理能力，其中具有可验证奖励的强化学习（WLVR）是一种有前途的增强策略。然而，现有的奖励机制局限于结果水平的正确性，并且缺乏明确的信号来指导模型考虑不同的解决方案。相比之下，人类问题的解决通常涉及评估多种潜在方法并选择最可靠的解决方案，这是当前的WLVR框架没有明确激励的认知过程。受此启发，我们提出了提示引导的多元化政策优化（HDPO），允许模型首先列出所有潜在的候选解决方案大纲作为提示，然后选择最可靠的解决方案大纲进行进一步推理。HDPO包括结构化推理冷启动和提示引导多元化强化学习两个阶段，以激励模型遵循“提议-选择-思考”轨迹生成多样化且可靠的解决方案。实验结果表明，HDPO有效地增强了LLM推理，增强了候选解决方案的多样性以及LLM识别可靠解决方案的能力。

[阅读原文](https://arxiv.org/abs/2606.03021)

---

## 32. 本地指导，全球影响：高斯重塑的信任区域解锁行为转变

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Bingxu Liu, Jiashun Liu, Johan Obando-Ceron, Hao Wang, Runze Liu, Pablo Samuel Castro, Aaron Courville, Ling Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel Gaussian trust region method for RL that improves policy optimization in non-stationary environments and demonstrates effectiveness in LLM post-training, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2606.03382v1宣布类型：新摘要：虽然近端策略优化（PPO）在静态环境中表现出强劲的性能，但我们表明其标准优化范式在连续和非静态环境中表现不佳。故障并非源于模型容量不足或剪裁过于严格。相反，PPO执行持续的、定向低效的本地更新，这表明缺乏几何感知的指导来积累有意义的行为变化，并最终阻碍向新行为模式的转变。尽管基于分歧的正规化引入了部分几何意识，但其单调增加的惩罚隐性地阻止了大的政策偏差，即使此类转变对于有效适应是必要的。为了解决这一限制，我们提出了高斯信任区域策略优化（GTR），它使用高斯核重塑信任区域。由此产生的约束是有界且非单调的，提供了强大的局部稳定性，同时在持续的高优势更新下逐渐放松。为了进一步提高鲁棒性，我们引入了一个混合高斯锚点，该锚点适应最近的政策轨迹，减少了陈旧引用引起的方差。GTR是架构不可知的，在游戏、模拟机器人控制、开放世界探索和语言模型训练后实现了强劲的性能。这些结果表明，几何感知的信任域设计可以成为复杂非静态环境中鲁棒强化学习的一个有前途的方向。我们的代码可在https://anonymous.4open.science/r/GTR_demo/README.md上获取。

[阅读原文](https://arxiv.org/abs/2606.03382)

---

## 33. MemoGen：过去的经验可以改善未来的文本到图像生成吗？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wenshuo Chen, Kuimou Yu, Bowen Tian, Jianfei Song, Shaofeng Liang, Haozhe Jia, Kan Cheng, Haosen Li, Kaishen Yuan, Lei Wang, Jiemin Wu, Songning Lai, Yutao Yue

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free agentic framework that uses experience memory for self-evolution in text-to-image generation, directly matching the self-evolving agents criterion.

**摘要**: arXiv：2606.03243v1宣布类型：新摘要：现代文本到图像模型已经实现了强大的视觉合成，但当提示需要隐式视觉约束、关系推理或外部知识时，仍然不可靠。现有的检索增强和代理生成方法通过获取外部知识、参考或当前请求的细化提示来缓解这个问题，但它们通常将每一代视为一个孤立的事件，并且不会系统性地保存过去的成功或失败以供未来使用。在这项工作中，我们询问文本到图像系统是否可以在不更新底层生成器的情况下根据自己的生成体验不断改进。我们提出了MemoGen，这是一个免训练框架，它通过代理进化层增强了现有的图像生成器。对于每个任务，MemoGen明确推断视觉需求，在必要时检索外部证据和参考，将它们转化为可执行生成约束，评估生成的结果，并将任务理解、参考选择、视觉反馈、成功策略和失败教训存储为可重复使用的经验记忆。在各个进化回合中，代理检索相关经验来改进类似的未来世代，选择性地修复之前失败的案例，同时保留成功的案例，从而在无需参数更新的情况下实现测试时自我进化。针对知识密集型和理性导向基准的广泛实验证明了这一范式的有效性：仅经过两轮进化后，基于开源Qwen-Image主干网构建的MemoGen就超越了WISE和Mind-Bench上的Nano Banana Pro和GPT-Image-1等强大的专有系统，表明显式体验记忆可以作为可靠的文本到图像生成的强大持续学习信号。

[阅读原文](https://arxiv.org/abs/2606.03243)

---

## 34. 高效且可控的LLM推理的显式思维链引导

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yu Xia, Zhouhang Xie, Xin Xu, Byungkyu Kang, Prarit Lamba, Xiang Gao, Julian McAuley

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning-based controller agent that adaptively steers a frozen LLM reasoner's chain-of-thought for efficient and controllable reasoning.

**摘要**: arXiv：2606.03965v1宣布类型：新摘要：大型语言模型通过扩展的思想链推理来提高最终答案的准确性，但经常低效地使用令牌并且几乎没有提供推理时控制。现有的高效推理方法通过缩短、提前停止或压缩痕迹来控制思维长度，让模型的思维方式隐式。在本文中，我们提出了抽象思想链引导（RST），它将推理引导制定为马尔科夫决策过程，其中控制器代理在推理期间自适应地引导冻结的推理器。在每一步，控制器观察推理轨迹和剩余思维预算，然后发出由推理策略和引导短语组成的引导动作，以启动下一个推理器步骤。这使得预算感知策略控制能够实现高效推理，同时保持推理者的生成连续性。我们通过多预算增强从构建的合成转向轨迹初始化控制器代理，并通过具有预算条件奖励整形的强化学习进一步优化它。在多个基准测试中的实验表明，该方法可以将全面思考的性能与大量的令牌节省相匹配，并在不同的推理机和任务之间实现可控的准确性-效率权衡。该代码可在https://github.com/Andree-9/ACTS上获取。

[阅读原文](https://arxiv.org/abs/2606.03965)

---

## 35. 在WLVR中用人体治疗换取合成增强

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Akshansh, Leonardo Rosa Rodrigues, Michael Korostelev, Youssef Hassan, Mark E. Whiting

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a method for synthetic augmentation of RLVR tasks, directly addressing the scalability of RL for LLMs via verifiable rewards.

**摘要**: arXiv：2606.03800v1宣布类型：新摘要：高质量培训任务的提供是代理语言模型上可验证奖励（WLVR）强化学习的核心瓶颈。每个任务都需要沙箱设置、提示和手写奖励功能，并且只有通过质量条的任务才会产生有用的训练信号。在这个质量标准下的手工策划无法经济地扩展到有效RL训练所需的任务计数，并且自动生成的任务变体和人类编写的任务变体之间的替代率尚未确定。我们研究使用预先指定的、门控过滤的小型手工创作基础的增强来替代WLVR期间的额外人类策展。我们正式化增强任务和人类编写任务之间的成本调整交易率$\rho_{\text{cost}}$，通过在具有不同增强份额的训练库中进行受控消融来衡量它，并描述增强管道的端到端经济性。将增强内容替换为额外的人类编写的任务保留了对跨越代码、指令遵循、推理和多轮代理功能调用的十个基准套件的总体概括。门控合成任务和人类编写的WLVR任务之间的成本调整交易率$\rho_{\text{cost}}$在合理的$c_{\text{human}}/c_{\text{aug}$范围内保持在$[1.4\times，11.6\times]$。

[阅读原文](https://arxiv.org/abs/2606.03800)

---

## 36. 具有强化学习的LLM经验驱动的动态退出

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yanyu Zhu, Hoilam Pao, Niu Hu, Wei Guo, Shaoxiong Zhan, Boyu Lai, Zitai Wang, Yongqin Zeng, Hai-Tao Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning framework (LEDE) to dynamically select exit layers and speculation lengths for self-speculative decoding, directly applying RL to optimize LLM inference.

**摘要**: arXiv：2606.03113v1宣布类型：新摘要：大型语言模型遭受缓慢的自回归推理。虽然自我推测解码加速了这一过程，但其效率受到固定退出层和推测长度等静态配置的阻碍。我们将这种优化重新定义为\textBF{Markov决策过程}，并提出\textBF{LEDE}，这是一个使用离线强化学习的框架。LEDE学习一种策略，根据每一步生成的序列的本地上下文动态选择最佳退出层和推测长度，平衡计算成本和草稿质量。对Llama-2和Llama-3模型的综合评估显示，LEDE比自回归解码实现了高达2.0%的加速，并且比静态推测基线提供了额外17%的加速。

[阅读原文](https://arxiv.org/abs/2606.03113)

---

## 37. 小型RL控制器，大型语言模型：RL引导的自适应采样用于测试时间缩放

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Runpeng Dai, Tong Zheng, Rui Liu, Chengsong Huang, Hongtu Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a lightweight RL controller for adaptive sampling at test time, formulated as an MDP to balance correctness, latency, and cost.

**摘要**: arXiv：2606.03102v1宣布类型：新摘要：测试时扩展提高了大型语言模型的推理性能，但在总计算和延迟方面都会产生巨大的成本。现有的自适应采样方法通过动态决定何时停止采样来部分缓解这个问题，但它们通常依赖于启发式规则或依赖于分布假设。在这项工作中，我们将自适应抽样表述为马尔科夫决策过程（MDP）。我们使用强化学习（RL）训练轻量级采样控制器，以共同平衡答案正确性、延迟和计算成本。在每一轮，控制器决定停止采样或获取额外样本。我们的方法是轻量级的，仅依赖于最终答案的统计数据，并且可以在中央处理器上训练和部署。我们进一步表明，由此产生的框架允许解释为具有显式预算约束的约束优化问题的拉格朗日松弛。针对ASC和OSC等强基线的实验表明，我们的方法在答案正确性、抽样轮数和所需总样本之间实现了改进的权衡。

[阅读原文](https://arxiv.org/abs/2606.03102)

---

## 38. EvoDrive：通过自我改进LLM代理实现安全关键自动驾驶的帕累托进化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tong Nie, Yuewen Mei, Yihong Tang, Junlin He, Jie Deng, Jian Sun, Wei Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving LLM agent framework for multi-objective safety-critical scenario generation using a simulator-grounded actor-critic and Pareto archive.

**摘要**: arXiv：2606.03678v1公告类型：新摘要：生成安全关键场景对于验证和改进自动驾驶系统至关重要，但它本质上需要最大化对抗性以暴露故障，同时保持现实性。现有的方法通常用手工设计的算法来管理这种权衡，将生成限制在已知的先验知识上，而忽略了未充分探索的模式。虽然最近的开放式代理进化可以突破这一极限，但不受约束的一般代理缺乏严格的模拟器基础，并且往往会将多目标紧张局势崩溃为单量最大化。在这里，我们介绍EvoDrive，这是第一个用于多目标场景生成的自动化、基于LLM的代理进化框架。EvoDrive采用基于模拟器的演员-评论家架构，其中记忆驱动的演员迭代地提出对生成器的改进，评论家过滤出不可信的候选者，而自我进化的世界评估者则提出有希望的提案来优化模拟预算。EvoDrive进一步维护评估候选者的帕累托档案，以保留多样化的攻击现实主义权衡，并通过模拟反馈指导未来的演变。MetaDrive和CARLA的基准结果表明，EvoDrive不仅显着扩展了各种发电机的帕累托边界，而且还为政策培训提供了有价值的场景。

[阅读原文](https://arxiv.org/abs/2606.03678)

---

## 39. 培训前后悔：弥合先验和先验观点以增强知识基础

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mingkuan Zhao, Xiayu Sun, Wentao Hu, Suquan Chen, Jiaxuan Li, Xiaoyan Zhu, Xin Lai, Jiayin Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Regret Pre-training, a self-supervised framework using a dual-view architecture to transfer future-aware signals into causal representations, directly relevant to latent reasoning via a novel training objective.

**摘要**: arXiv：2606.03080v1宣布类型：新摘要：因果语言模型仅使用先前的上下文对序列概率进行因子分解，尽管未来信息在训练数据中可用，但在训练期间不会被利用。本文介绍了Regert Pre-train，这是一个基于使用特权信息学习（LUPI）范式的自我监督框架。该框架采用双视图架构，其中单个模型既生成因果学生分布，又生成受未来影响的教师分布。训练目标通过遗憾损失增强了标准语言建模，最大限度地减少了教师与学生之间的KL分歧，将未来感知信号转移到因果表示。我们研究了OLMoE-1B-7 B架构上的两种教师配置：LocalRegret，它通过一个未来标志来扩展注意力，和GlobalRegret，它以目标位置被屏蔽的双向上下文为条件。经过40亿个令牌训练后对9个下游任务进行的实验表明，两种配置的表现始终优于基线。平均而言，GlobalRegret和LocalRegret的准确率分别为33.9%和32.2%，超过了基线的30.2%。最值得注意的是，GlobalRegret将BoolQ的绩效提高了18.1个百分点（61.0% vs 42.9%）。该框架不引入任何额外的参数，并且每个训练步骤仅需要一次额外的推断模式前向传递。

[阅读原文](https://arxiv.org/abs/2606.03080)

---

## 40. MemTrain：自我监督的上下文记忆训练

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ziheng Li, Xingrun Xing, Haoqing Wang, Zhi-Hong Deng, Yehui Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-supervised training framework (MemTrain) using GRPO to improve LLM agent context memory via proxy tasks, directly relevant to self-improving agents.

**摘要**: arXiv：2606.03197v1宣布类型：新摘要：记忆是长期LLM代理不可或缺的能力，使他们能够保存和利用在扩展交互中积累的信息。现有的存储代理方法通常通过下游任务的强化学习进行端到端训练。然而，为内存密集型场景收集高质量的注释问题成本高昂，而且产生的训练数据通常缺乏足够的多样性来覆盖一般记忆行为。在这项工作中，我们提出了MemTrain，这是一个自我监督的训练框架，用于普遍增强LLM代理的上下文记忆能力，以实现更有效的下游后训练。MemTrain在未标记的维基百科库上引入了两个耦合的代理任务：（1）端到端掩蔽重建目标，它要求模型在多轮内存更新后恢复掩蔽实体，从而鼓励从最终结果角度维护内存;和（2）中间记忆回忆目标，其要求模型使用中间记忆状态重建掩蔽的历史信息，鼓励在整个交互过程中忠实的压缩和记忆完整性。使用GRPO联合优化这两个目标。对长文本QA和基于搜索的QA基准的广泛实验表明，MemTrain持续提高不同模型之间的下游内存密集型推理性能，比直接特定任务的后训练获得高达17.67分的收益。

[阅读原文](https://arxiv.org/abs/2606.03197)

---

## 41. GRZR：大型语言模型微调的组相对零阶优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Liyan Tan, Yequan Zhao, Yifan Yang, Ruijie Zhang, Xinling Yu, Zheng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel zeroth-order optimizer (GRZO) for LLM fine-tuning that reduces gradient variance via group-relative normalization, directly improving RL-based post-training efficiency.

**摘要**: arXiv：2606.02857v1宣布类型：新摘要：零阶（Zero）优化是反向传播的一种内存高效替代方案，用于微调大型语言模型，但其部署受到梯度估计的高方差的限制。我们提出了GRZR，这是一种组相对零阶优化器，它为每个迷你批示例绘制一个伪独立扰动，并通过组相对规范化来汇总每个示例的损失，将有效梯度方向计数从一提高到批大小，而无需额外的前向成本，同时保留推理级内存。我们证明了GRZero是方向无偏的，方差与批量大小成比例地缩小，从而产生比MeZero更严格的非凸收敛界。在RoBERTa-large、Llama 3 -8B和OPT-13 B的多个任务中，GRZR将Llama 3 -8B的平均准确性比MeJO提高了+3.0美元，峰值图形内存较低23%;作为MeJO核心的直接替代品，它将稀疏、低等级和量化的Zero变体平均提高了+6.0美元。

[阅读原文](https://arxiv.org/abs/2606.02857)

---

## 42. 想象感知标记增强多模式语言模型中的空间推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mahtab Bigverdi, Lindsey Li, Weikai Huang, Yiming Liu, Jaemin Cho, Jieyu Zhang, Tuhin Kundu, Chris Dangjoo Kim, Zelun Luo, Linda Shapiro, Ranjay Krishna

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Imaginative Perception Tokens (IPT), a novel latent reasoning mechanism for spatial reasoning in VLMs that externalizes intermediate perceptual representations, outperforming textual CoT.

**摘要**: arXiv：2606.03988v1宣布类型：新摘要：视觉语言模型（VLM）在许多任务中表现出色，但当关键信息不可直接观察时，仍然难以进行空间推理。许多此类问题需要富有想象力的感知：推断从看不见的视角会看到什么，追踪穿过遮挡空间的路径，或者将部分观察结果整合到连贯的空间表示中。我们引入了想象感知令牌（TIP），这是一种中间感知表示，它将VLM在替代空间配置下感知的内容具体化，同时与观察到的输入保持一致。   为了研究这种能力，我们制定了三项任务：透视图（PET）、路径追踪（PT）和多视图计数（MVP），并利用基本真相想象力、答案和评估基准构建了大约2万个示例的数据集。使用统一的VLM BAGEL作为支柱，TIP监督持续改进空间推理，并且往往优于文本思维链训练，即使在推理时没有生成图像。在MVP上，TIP将准确性提高了3.4%，并通过PT上的强大闭源模型实现了有竞争力的性能。我们进一步发现，将IDT和仅标签监督相结合会产生额外的收益，而文本思维链可能会大幅降低性能，这表明当通过语言强制空间计算时，存在模式不匹配。总的来说，IDT为推理未观察到的空间结构提供了一个原则性的监督信号，提高概括性，同时产生可解释的中间表示。

[阅读原文](https://arxiv.org/abs/2606.03988)

---

## 43. 通过宽基线匹配在MLLM中引发复杂空间推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hao Zhong, Muzhi Zhu, Shenyan Zeng, Anzhou Li, Cong Chen, Hua Geng, Duochao Shi, Wentao Ye, Tao Lin, Hao Chen, Chunhua Shen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Dynamic Correspondence Reinforcement Learning (DCRL), a verifiable-reward RL method for improving spatial reasoning in MLLMs, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2606.03577v1宣布类型：新摘要：宽基线匹配（WBM）需要集成几何理解、观点变化、细粒度感知和遮挡推理，使其成为部署在物理环境中的多模式大型语言模型（MLLM）中空间推理的具有挑战性的测试平台。然而，当前的MLLM缺乏针对这些能力的系统评估和培训框架。我们引入了ReasonMatch-Bench，这是一个按室内、室外和以对象为中心的场景中的观点位移和匹配粒度分层的基准，并表明当前的MLLM仍然难以应对细粒度的宽基线对应：在困难的90个样本子集上，人类注释者实现了84.0 F1，而现有最佳基线达到37.2。为了弥合这一差距，我们构建了一个可扩展的数据生成管道，该管道可以自动从大规模视频3D库（包括RGB-D视频和SfM重建）中提取宽基线视图对，从而产生多样化且可验证的监督。我们进一步提出了动态对应强化学习（DMCR），它结合了图像级观点进步和点级对应课程，通过可验证的奖励来改进WBM培训，而无需明确的CoT监督。大量实验表明，DRTL大大改进了ReasonMatch-Bench并转移到相关的空间基准，同时在几个基准上保持了总体视觉理解性能，并获得了适度的增长。

[阅读原文](https://arxiv.org/abs/2606.03577)

---

## 44. 宪法上的政策安全蒸馏

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ming Wen, Yuxuan Liu, Kun Yang, Yunhao Feng, Zhuoer Xu, Yuhao Sun, Shiwen Cui, Xiang Zheng, Xingjun Ma, Yu-Gang Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Constitutional On-Policy Safe Distillation (COPSD), a novel RL-based distillation method for safety alignment with a new reward design and training recipe.

**摘要**: arXiv：2606.03089v1宣布类型：新摘要：政策上的自我蒸馏（OPSD）通过使用受特权信息限制的教师来提供密集的代币级监督，已成为一种有效的培训后范式。之前的工作表明，OPSD可能会在可验证的推理任务中崩溃，但安全调整的不同之处在于，它是由高级构成而不是明确的目标答案来指导的，这使得它成为重新审视密集蒸馏的自然环境。然而，我们的试点研究表明，安全性OPSD仍然遭受严重崩溃：宪法条件反射使教师分布收缩为短期和过于保守的反应，而反向KL进一步放大了这种收缩，导致表达力下降。我们将这种效应形式化为非垂直语义空间中安全边界下的几何泄漏，其中安全压力转移到表达维度。基于这一分析，我们提出了宪法性政策安全蒸馏（COPD），该方法首先通过跨SFT冷启动来校准教师，然后进行宪法条件下的政策性蒸馏。对12个基准的实验表明，COPD实现了比基线更强的安全性--帮助权衡，同时大幅降低了一般推理能力的安全税。

[阅读原文](https://arxiv.org/abs/2606.03089)

---

## 45. 当WLHF失败时：奖励黑客、崩溃和评估者游戏的机械分类

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zelalem Abahana

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a mechanistic taxonomy and empirical study of reward hacking in RLHF pipelines (PPO, DPO, UP-PPO), directly addressing RL for LLMs with a new classification method for training dynamics.

**摘要**: arXiv：2606.03238v1宣布类型：新摘要：来自人类反馈的强化学习（RL HF）通过用学习且可扩展的代理替换未指定的人类目标，使大规模的后训练成为可能。同样的替代会产生结构化的失败表面：优化可以提高习得回报，而外部质量下降，降低代理和判断分数，揭示代理不一致，或产生特定于评估者的分歧。我们对紧凑的WLHF管道进行了一项实证故障模式研究，该管道具有近端策略优化（PPO）、直接偏好优化（DPO）、不确定性惩罚的PPO（UP-PPO）、奖励模型不确定性、大约政策漂移、多样性和重复诊断以及两个外部LLM法官。我们没有将奖励黑客视为单个终端事件，而是使用学习到的奖励、评委分数和平均评委分数的方向对检查点之间的匹配转换进行分类。在61个检查点行和1920个行级转换中，激进的PPO具有最高的局部奖励黑客率（14.45%;自举95%CI：10.16-18.75），而UP-PPO在相同的激进机制下产生较低的奖励黑客率（11.33-10.94%）。过渡前的逻辑模型用ROC-AUC 0. 821预测未来的行级奖励黑客攻击，行级分析发现检查点平均在12种设置中的3种中未命中的本地化奖励黑客攻击。中心结论是方法论：RL HF失败不仅是最终模型病理，而且是可以分类、局部化和部分预期的训练动态。

[阅读原文](https://arxiv.org/abs/2606.03238)

---

## 46. 过滤，然后重新加权：重新思考按策略蒸馏中的优化粒度

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuying Li, Leqi Zheng, Yongzi Yu, Wenrui Zhou, Xuchang Zhong, Xing Hu, Jing Jin, Huangjie Yuan, Tao Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FiRe-OPD, a novel on-policy distillation method for LLMs that jointly filters and reweights trajectories and tokens for finer-grained optimization, directly improving RL-based post-training.

**摘要**: arXiv：2606.02684v1宣布类型：新摘要：大型语言模型中的按策略提炼（OPD）正在从全轨迹KL监督转向更具选择性的训练范式。最近的OPD方法越来越注重选择要学习的轨迹、哪些代币信息最丰富、哪些监督信号最可靠。受这一趋势的启发，我们重新思考OPD的优化粒度，并提出了\fireicon\ FiRe-OPD（过滤，然后重新加权），联合调整轨迹和代币级别的监督信号。详细来说，FiRe-OPD首先过滤轨迹以删除低质量的推出样本，然后在保留的轨迹内应用软重新加权以强调信息性令牌。与硬令牌选择相比，FiRe-OPD利用软加权机制有效减少信息损失，增强优化稳定性，从而实现更细粒度的OPD优化。我们验证了FiRe-OPD在强到弱、单教师和多教师环境中的有效性，并证明其优于最近的代币级OPD方法（例如，AIME 2024上的+6.25（强到弱），Miner上的+18.81（多教师）。我们的代码可在https://github.com/YuYingLi0/FiRe-OPD上获取。

[阅读原文](https://arxiv.org/abs/2606.02684)

---

## 47. 缓解虚假信用传播：基于条目的强化学习的概率图形奖励聚合

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Can Lv, Mingju Chen, Heng Chang, Shiji Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a probabilistic graphical framework for dependency-aware rubric reward aggregation to mitigate false credit propagation in RL for LLMs.

**摘要**: arXiv：2606.03361v1宣布类型：新摘要：基于条目的奖励越来越多地用于开放式语言模型训练后，但标准级分数通常被汇总为独立的效用。这种扁平规模化忽略了标准之间指定的先决条件和激活关系，即使不存在许可奖励或惩罚的条件，也允许对奖励或惩罚进行计算。我们称这种结构性奖励聚合失败\textBF{假信用传播}（FCP）。为了解决这个限制，我们提出了\ourName（\textBF{G}raphical \textBF{E}vent \textBF{A} gggraction for \textBF{R}ubric rewards），这是一个用于依赖性感知的标题聚合的概率图形框架。\ourName将每个标准结果建模为类型化标题图中的潜在伯努里事件，将软抑制从不支持的父事件传播到其子事件，并将产生的事件概率聚合为标准化的预期带符号效用。这产生了线性时间奖励计算，该计算可以插入标准的基于规则的RL管道中，而无需改变外部优化算法。HealthBench、DeliveringBench和PLawBench具有两个策略主干的实验表明，我们的名字比扁平聚合和确定性门控持续改进，比扁平聚合实现了高达15.5%的相对收益。FCP诊断进一步表明，与平面聚合相比，ourName将泄漏减少了96.5%，同时保留了比确定性门控更多的许可下游实用程序。我们的代码可在https://github.com/LvCan926/GEAR上公开获取。

[阅读原文](https://arxiv.org/abs/2606.03361)

---

## 48. 从Agent轨迹中提取推理原语

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhihan Lei, Jiarui Yan, Joshua Momo, William W. Cohen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a method to mine and convert recurrent reasoning moves from agent traces into a library of pseudo-tools, enabling self-improvement from interaction traces.

**摘要**: arXiv：2606.02994v1宣布类型：新摘要：ReAct风格的LLM代理经常在问题中重新发现相同的推理例程，但却将这些例程困在暂时的记事本中。我们引入了推理原始归纳，这是一种单次方法，可以挖掘成功的ReAct痕迹、聚集循环推理动作，并将最频繁的动作转换为类型化伪工具的紧凑库。每个伪工具都由LLM在调用时解释的自然语言文档字符串指定，标准ReAct循环在测试时组成这些基元。核心结果是，诱导库的表现优于生成其踪迹的代理：RuleArena NBA上+44 pp（30 -> 74），MuSR团队分配上+30 pp（38 -> 68），NatPlan会议规划上+22 pp（7 -> 29）。在涵盖叙事演绎、规则应用和约束满足规划的五个可比子任务中，单个固定配置在每个子任务上都优于零触发思想链，匹配或超越专家撰写的分解，并以较低的平均推理成本优于AWM。

[阅读原文](https://arxiv.org/abs/2606.02994)

---

## 49. 推理模型的价值感知随机KV缓存驱逐

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ting-Yun Chang, Harvey Yiyun Fu, Deqing Fu, Chenghao Yang, Jesse Thomason, Robin Jia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free KV cache eviction method for reasoning models that protects large-magnitude value states and introduces stochasticity, bridging efficiency and accuracy for long CoT outputs.

**摘要**: arXiv：2606.03928v1宣布类型：新摘要：推理模型通过扩展的思维链来提高准确性，但它们的长输出会造成内存和计算瓶颈。KV缓存驱逐方法通过从缓存中驱逐不重要的关键字-值对来降低这种成本，但它们的准确性通常比保留完整的KV缓存的基于选择的稀疏注意力替代方案更差。我们确定了对KV缓存驱逐准确性至关重要的关键因素。首先，一小部分值状态具有异常大的幅度，驱逐它们会导致灾难性的失败，导致模型进入重复推理循环。其次，在驱逐期间引入随机性通过增加缓存多样性来提高准确性。基于这些发现，我们提出了价值感知随机KV缓存驱逐（VaSE），这是一种免训练的食谱，可以保护大规模价值状态并促进多样化的驱逐决策。在六个推理任务中，使用VaSE和4x KV缓存压缩的Qwen 3模型在相同稀疏度下比SOTA选择方法产生更高的平均准确性，同时比最强的驱逐方法高出4%以上。总体而言，VaSE弥合了效率和准确性之间的差距，支持Flash Attention 2并为推理模型提供静态内存空间。

[阅读原文](https://arxiv.org/abs/2606.03928)

---

## 50. ASymPO：无行为信息的非线性LLM后培训的非线性规模策略优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zehua Liu, Yuxuan Yao, Xiaojin Fu, Tao Zhong, Mingxuan Yuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Asymmetric-Scale Policy Optimization (ASymPO), a novel RL objective for asynchronous LLM post-training that stabilizes training without behavior-policy probabilities, directly addressing RL for LLMs.

**摘要**: arXiv：2606.03070v1宣布类型：新摘要：同步强化学习可以通过将响应生成与策略优化脱钩来提高语言模型训练后的吞吐量，但陈旧的响应会带来分布漂移。标准的行为纠正方法通过行为策略概率、重要性比或剪裁来控制这种漂移，这需要跨部署和学习器系统的标记对齐、版本化和数字一致的行为日志概率。我们询问是否可以仅使用当前策略概率来稳定非同步组相关RL。我们确定了一种规模失衡失败模式：当在当前政策下评估陈旧的响应时，正损失项和负损失项可能会出现在不同的负对概率尺度上，因此零和优势不再意味着平衡的损失贡献。我们提出了非线性规模策略优化（ASymPO），它通过当前平均令牌负对log概率来标准化每个响应的令牌损失。ASymPO不需要行为策略概率，可以恢复响应级别零和平衡，并保留非零学习信号。我们还引入了扩展策略优化（SPO），一种固定的负扩展基线，并在训练后的同步数学推理中评估当前仅策略的目标。

[阅读原文](https://arxiv.org/abs/2606.03070)

---

## 51. 是什么让交互轨迹对培训终端代理有效？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sidi Yang, Chaofan Tao, Jierun Chen, Tiezheng Yu, Ruoyu Wang, Yuxin Jiang, Yiming Du, Wendong Xu, Jing Xiong, Taiqiang Wu, Lifeng Shang, Xiaohui Li, Ngai Wong, Haoli Bai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a pipeline for training terminal agents from interaction trajectories, revealing a pedagogical paradox where lower-scoring agents produce better teaching data due to environment-grounded supervision.

**摘要**: arXiv：2606.03461v1宣布类型：新摘要：更强的代码代理通常被认为是后培训的优秀教师，但这种假设与任务难度、利用设计和学生能力仍然很难分开。我们使用Terminal-Lego来研究这种教学联系，Terminal-Lego是一个可扩展的管道，可以将多领域现实世界问题转化为经过环境验证的代理任务。令人惊讶的是，独立的表现并不决定教学效果：虽然Claude Opus 4.6在Terminal-Bench 2.0上获得了更高的分数，但根据得分较低的代理DeepSeek-V3.2的轨迹进行微调的学生表现出明显更强的概括性。我们将这种“教学悖论”归因于基于环境的监督（EGS）：通过利用可见的互动明确暴露检查-行动-验证行为的轨迹使学生能够内化强大的解决问题的例行程序，而不是脆弱的行动序列。缩放分析揭示了出色的数据效率：例如，Qwen 3 - 32 B的Terminal-Lego轨迹只有15.3k，在Terminal-Bench 2.0上获得了24.3%的分数，与之前的SOTA性能相媲美，数据量是30倍以上。我们的结果表明，智能体后训练的前沿不仅仅是结果匹配，而是将重点转向“生命周期工程”，其中基于环境的交互结构的系统设计充当可复制和可推广的智能体的主要催化剂。

[阅读原文](https://arxiv.org/abs/2606.03461)

---

## 52. QUBRIC：为RL联合设计超越可验证奖励的收件箱和标题

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Rongzhi Zhang, Rui Feng, Zhihan Zhang, Jingfeng Yang, Qingyu Yin, Xin Liu, Zixuan Zhang, Priyanka Nigam, Bing Yin, Tuo Zhao, Chao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes QUBRIC, a framework for co-designing queries and rubrics to enable RL beyond verifiable rewards, directly addressing a key limitation in RL for LLMs.

**摘要**: arXiv：2606.03968v1宣布类型：新摘要：基于条目的RL是一种将强化学习扩展到可验证奖励之外的有希望的途径，但现有方法在将查询分布视为固定的同时优化了条目。我们发现了一个结构瓶颈：标题质量受到查询结构的限制。开放式查询会产生模糊的标题;天真地缩小它们会引入没有模型可以验证的捏造引用，因此所有响应都会失败，训练也不会收到奖励信号。我们介绍了QUBRIC，这是一个共同设计查询和标题的框架。教师衍生的关键点奠定了将开放式查询重写为基于情景的可评估问题的基础。然后，对比标题生成将教师政策差距转化为查询级标准，而可学习性过滤仅保留信息丰富的查询-标题对用于GRPO培训。QUBRIC在ArenaHard上取得了超过SFT基线+5.5分的增长。它仅在遵循叙述的数据上进行培训，进一步转移到涵盖法律、道德和叙事推理的三个既定基准（平均+6.3分），改进集中在推理相关维度。这些结果提供了证据，表明协同设计查询和标题可以使基于标题的RL成为超越严格可验证任务的WLVR的实用补充。

[阅读原文](https://arxiv.org/abs/2606.03968)

---

## 53. FederatedSkill：联邦学习，促进抽象技能进化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jingbo Yang, Guanyu Yao, Yang Zhang, Ramana Rao Kompella, Gaowen Liu, Shiyu Chang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a privacy-preserving federated learning framework for collaborative self-evolution of LLM agent skill libraries via semantic skill diffs.

**摘要**: arXiv：2606.03143v1宣布类型：新摘要：现代LLM代理越来越依赖技能库来处理复杂的任务，使技能进化成为自我完善的主要驱动力。然而，孤立的单用户任务流缺乏建立全面技能所需的多样性。虽然跨用户协作可以克服这一数据瓶颈，但当前的数据库共享方法会损害用户隐私，并强加一个无法适应客户端多样性的统一全球库。我们引入了FederatedSkill，这是一个用于协作代理进化的隐私保护框架。FederatedSkill超越了原始轨迹共享，利用语义技能差异、本地库的结构化补丁作为通信的基本单位。在服务器端，进化代理聚合这些补丁，以动态建模特定于客户端的能力边界，促进严格个性化的技能进化，而不是次优的全球平均水平。在20个不同的代理任务家族中进行评估，FederatedSkill显示出比自我进化基线有很大的收益，成功率提高了44.4%，计算成本降低了37.5%。

[阅读原文](https://arxiv.org/abs/2606.03143)

---

## 54. InfoMem：利用用户条件信息收益训练长上下文存储代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tiancheng Han, Yong Li, Wuzhou Yu, Qiaosheng Zhang, Wenqi Shao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces InfoMem, a novel reward mechanism for training long-context memory agents via answer-conditioned information gain, directly contributing to RL for LLMs with a new reward design.

**摘要**: arXiv：2606.03329v1宣布类型：新摘要：长上下文任务需要LLM从大上下文中识别和保存与答案相关的信息。块式存储代理通过顺序读取文档块、更新紧凑存储器并从累积的存储器生成最终答案来解决这个问题。然而，现有的基于RL的块式代理要么依赖于稀疏的最终答案奖励，要么使用词汇中间奖励来进行记忆和检索动作。这些信号监督任务成功或局部重叠，但不直接评估最终记忆是否支持地面真相答案。我们提出了InfoMem，这是一种用于训练块式记忆代理的奖励机制，它使用回答条件信息评估最终记忆效用。InfoMem衡量最终记忆增加了模型的地面真相答案的每个令牌日志可能性的程度。为了稳定RL优化，InfoMem仅将此信号应用于成功的轨迹，并在奖励合成之前对其进行标准化。在相同的GRPO框架和培训预算下，InfoMem比可比的存储代理RL基线提高了长上下文存储代理性能。分析表明，有效的最终记忆奖励应该在成功的轨迹上运行，在奖励合成之前进行规范化，并以答案而不是询问为条件。我们的代码可在https://github.com/GenSouKa1/InfoMem上获取。

[阅读原文](https://arxiv.org/abs/2606.03329)

---

