# 💡 今日研究速览 (Daily Summary)

# LLC和政策优化的RL

今天的研究表明，我们正在共同努力完善和稳定大型语言模型强化学习的核心机制，超越简单的回报最大化。中心主题是解决推理任务中稀疏和延迟奖励的根本挑战。KnowRL和代币级政策优化（TEPO）等新型框架引入了机制--例如最低限度的知识指导和代币级奖励聚合--以提供更密集、信息更丰富的学习信号。与此同时，我们非常注重确保这些优化流程产生经过良好校准和稳健的模型，正如校准感知政策优化（CAPO）中所示，并致力于通过针对相关代理的稳健优化来减轻奖励黑客攻击。对按政策蒸馏（OPD）动态的系统性调查进一步强调了这种成熟，提供了从失败的蒸馏中恢复过来并加强教师一致性的食谱，例如Lightning OPD。

# 自我进化和统计系统

人工智能代理的前沿正在迅速向能够真正、长期自我改进和自主运营的系统发展。一项关键创新是集成复杂的存储器架构，使代理能够从经验中学习并将成功的策略提炼成可重复使用的知识。MolMem和Reight-Retriever等框架明确构建持久的、不断发展的记忆系统--无论是用于分子优化还是一般代理任务--这些系统通过相互作用变得更有能力。这还得到了针对长期挑战的自治系统的研究的补充，例如用于ML研究工程的AiScientist和用于神经架构发现的HypoExplore，它们具有分层编排和假设生成和评估的自我改进循环。基准Frontier-Eng通过为现实世界工程任务中的生成式优化提供测试平台，进一步巩固了这一方向。

# 潜在推理和模型架构

在理解和构建LLM的内部计算流程方面正在取得重大进展，特别是在隐式推理和规划方面。一个主要目标涉及设计具有潜在、反复或可控内部状态的模型，以提高效率和应急能力。Parcae的稳定循环架构和EVE具有代理内部控制的变分模型等提案旨在实现更强大、更高效的潜在计算。理论和机制研究为此提供了基础，分析显示了思维链监督如何降低样本复杂性，并证明潜在的规划表示自然会随着模型规模而出现。对多标记预测如何诱导鲁棒推理电路的探索进一步加深了我们对这些能力如何在Transformer架构中学习和表示的机械理解。

# 多模式和专业代理对齐

关于对齐人工智能系统的研究正在扩展到复杂的多模式领域，需要超越简单人类偏好的新颖奖励设计和优化技术。一个明显的趋势是开发可扩展和细粒度的无注释或自我监督的奖励机制。EntEcho直接从视觉语言模型为文本到图像模型构建奖励，而视觉偏好优化（rDPO）则利用特定于实例的标题奖励。对于在长文档或网络等结构化环境中操作的代理，正在开发证据感知群体相对政策优化（DocSeeker）和使用ORPO/GRPO（从模仿到歧视）的渐进课程等方法，以联合优化任务成功和稳健的、基于证据的行为。周期一致搜索的工作也体现了这一趋势，从问题可重建性中创建代理奖励，以在没有黄金监督的情况下培训搜索代理。

# 去中心化和跨语言适应

最后，今天的论文讨论了在不同的现实世界限制中部署和调整高级LLM能力的实际挑战。其中一项工作是解决跨去中心化的私有数据孤岛调整模型的问题，正如PubSwap通过公共数据进行协调的联邦WLVR框架所示。另一个解决了推理中语言包容性的迫切需求，ReasonXL展示了一个使用SFT和RL的管道，并具有可验证的奖励，可以在不牺牲性能的情况下成功转变LLM的推理语言。这些努力凸显了人们日益关注使最先进的RL和推理技术在各种部署场景中可操作且公平。

---

## 1. KnowRL：通过强化学习和最少足够知识指导来增强LLM推理

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Linhao Yu, Tianmeng Yang, Siyu Ding, Renren Jin, Naibin Gu, Xiangzhao Hao, Shuaiyi Nie, Deyi Xiong, Weichong Yin, Yu Sun, Hua Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces KnowRL, a reinforcement learning framework for LLMs that uses minimal-sufficient knowledge guidance to address reward sparsity in reasoning tasks.

**摘要**: arXiv：2604.12627v1宣布类型：新摘要：WLVR改进了大型语言模型中的推理，但其有效性通常受到困难问题上严重奖励稀疏性的限制。最近的基于提示的RL方法通过注入部分解决方案或抽象模板来减轻稀疏性，但它们通常通过添加更多令牌来扩展指导，这会带来冗余、不一致和额外的训练费用。我们提出了\textBF{KnowRL}（知识引导的强化学习），这是一个RL训练框架，将提示设计视为最小充分引导问题。在RL训练期间，KnowRL将指导分解为原子知识点（KP），并使用约束子集搜索（CSS）来构建紧凑的交互感知子集以进行训练。我们进一步确定了一个修剪交互悖论--删除一个KP可能会有所帮助，而删除多个此类KP可能会造成伤害--并在此依赖结构下明确优化稳健的子集策展。我们从OpenMath-Nemotron-1.5B训练KnowRL-1.5B。在1.5B规模的八个推理基准中，KnowRL-Nemotron-1.5B的表现始终优于强RL和暗示基线。在没有KP暗示推理的情况下，KnowRL-Nemotron-1.5B的平均准确率达到70.08，已经超过Nemotron-1.5B +9.63分;在选定的KP下，性能提高到74.16，建立了这种规模的新技术水平。该模型、精心策划的训练数据和代码可在https://github.com/Hasuer/KnowRL上公开获取。

[阅读原文](https://arxiv.org/abs/2604.12627)

---

## 2. Lightning OPD：通过离线策略蒸馏对大型推理模型进行高效的后训练

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yecheng Wu, Song Han, Hai Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Lightning OPD, an efficient offline on-policy distillation framework for LLM post-training that enforces teacher consistency to match standard OPD performance.

**摘要**: arXiv：2604.13010v1宣布类型：新摘要：按策略提炼（OPD）已成为大型语言模型的一种有效的训练后范式。然而，标准OPD在整个培训过程中需要实时教师推理服务器，从而导致大量的基础设施费用。在这项工作中，我们研究政策上的蒸馏是否可以离线执行。一种自然的方法是在SFT推出期间预先计算教师日志概率一次，并在培训期间重复使用它们。然而，在实践中，这种离线变体无法可靠地匹配标准OPD的性能。为了理解这种差异，我们找出了一个以前被忽视的条件，该条件对任何OPD管道都至关重要，我们称之为教师一致性。这个条件要求相同的教师模型用于监督微调和OPD。我们发现，违反教师的一致性引入了一个不可约的梯度偏差，导致离线和在线OPD收敛到一个次优的固定点，无论训练时间。基于这一见解，我们提出了闪电OPD，一个离线的政策蒸馏框架，通过预先计算教师的日志概率在SFT推出，强制教师的一致性。这种设计完全消除了对实时教师服务器的需求。我们进一步表明，在教师一致性下，Lightning OPD与标准OPD具有相同的最优值，具有有限的梯度差异和有助于防止政策漂移的隐性正规化效应。数学推理和代码生成的大量实验表明，Lightning OPD实现了最先进的性能，效率显着提高。Lightning OPD从SFT初始化的Qwen 3 -8B-Base模型开始，仅需30个图形处理器小时即可在AIME 2024上达到69.9%，实现了标准OPD的4.0倍加速，并大幅降低了LLM后培训学术研究的入门门槛。

[阅读原文](https://arxiv.org/abs/2604.13010)

---

## 3. 推理LLM的校准感知策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziqi Wang, Xingzhou Lou, Meiqi Wu, Zhengqi Wen, Junge Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new RL-based policy optimization method (CAPO) for LLMs that jointly improves reasoning accuracy and calibration, directly addressing RL for LLMs.

**摘要**: arXiv：2604.12632v1宣布类型：新摘要：团体相对政策优化（GRPO）增强了LLM推理，但通常会导致过度自信，即不正确的响应比正确的响应产生的困惑度更低，从而降低了相对校准，如曲线下面积（AUR）所描述的。现有方法要么在校准方面产生有限的改进，要么牺牲推理准确性的收益。我们首先证明了GRPO式算法的这种退化源于其不确定性不可知的优势估计，这不可避免地使优化梯度与校准不一致。这导致以降级的校准为代价的改进的准确性。然后，我们提出了校准感知策略优化（CAPO）。它采用了逻辑AUC替代损失，理论上是一致的，并承认遗憾界，使不确定性意识的优势估计。通过进一步结合噪音掩蔽机制，CAPO实现了稳定的学习动态，共同优化校准和准确性。多个数学推理基准的实验表明，CAPO-1.5B将校准显着提高了高达15%，同时实现了与GRPO相当或更好的准确性，并进一步将下游推断时间缩放任务的准确性提高了高达5%。此外，当允许在低置信度条件下弃权时，CAPO实现了帕累托最优的精确度-覆盖率权衡，凸显了其在缓解幻觉方面的实际价值。

[阅读原文](https://arxiv.org/abs/2604.12632)

---

## 4. 安全培训在政策RL下调节了有害的错位，但方向取决于环境设计

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Leon Eshuijs, Shihan Wang, Antske Fokkens

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies on-policy RL for LLMs and its effect on harmful misalignment, analyzing reward design and environment features.

**摘要**: arXiv：2604.12500v1宣布类型：新摘要：众所周知，强化学习（RL）下的规范游戏会导致LLM出现谄媚、操纵或欺骗行为，但发生这种情况的条件仍不清楚。我们在3个环境中训练了11个经过描述调整的LLM（0.5B--14B），并发现模型大小在某些环境中充当安全缓冲区，但在其他环境中会导致更大的有害利用。控制消融将这种逆转追溯到特定环境的特征，例如角色框架和隐性可玩性线索。我们进一步表明，大多数安全基准并不能预测RL引起的失准，除非在Sycophancy评分的情况下，此时利用依赖于推断用户的偏好。最后，我们发现按策略RL保留了模型自己的发电分布中固有的安全缓冲区，该缓冲区在非策略设置期间被绕过。

[阅读原文](https://arxiv.org/abs/2604.12500)

---

## 5. 自我蒸馏归零：自我修正将二元奖励转化为密集监督

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yinghui He, Simran Kaur, Adithya Bhaskar, Yongjin Yang, Jiarui Liu, Narutatsu Ri, Liam Fowl, Abhishek Panigrahi, Danqi Chen, Sanjeev Arora

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel self-distillation method that uses binary rewards to generate dense token-level supervision for LLM self-improvement, aligning with RL for LLMs and self-evolving agents.

**摘要**: arXiv：2604.12002v1宣布类型：新摘要：当前可验证环境中的训练后方法分为两类。强化学习（WLVR）依赖于二元奖励，二元奖励具有广泛适用性且功能强大，但在训练期间仅提供稀疏的监督。蒸馏提供密集的代币级监督，通常从外部教师或使用高质量的演示获得。收集此类监督可能成本高昂或无法获得。我们提出了自蒸馏零（SD-Zero），这是一种比RL训练样本效率高得多的方法，并且不需要外部教师或高质量的演示。SD-Zero训练单个模型扮演两个角色：生成器（生成初始响应）和修订器（根据该响应及其二元奖励来产生改进的响应）。然后，我们执行政策上的自我提炼，将修订者提炼到生成器中，使用以生成器的响应及其奖励为条件的修订者的代币分布作为监督。实际上，SD-Zero训练模型将二元奖励转化为密集的代币级自我监督。在使用Qwen 3 - 4 B-Direct和Olmo-3- 7 B-Direct的数学和代码推理基准测试中，SD-Zero比基本模型提高了至少10%的性能，并且在相同的问题集和训练样本预算下优于强大的基线，包括拒绝微调（RFT）、GRPO和自蒸馏微调（SDFT）。广泛的消融研究显示了我们提出的算法的两个新颖特征：（a）令牌级自定位，其中修改者可以根据奖励识别生成器响应中需要修改的关键令牌，以及（b）迭代自进化，其中改进的修改答案的能力可以通过定期教师同步提炼回生成性能。

[阅读原文](https://arxiv.org/abs/2604.12002)

---

## 6. 令牌级策略优化：通过序列级Likestry将组级奖励链接到令牌级聚合

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xingyu Lin, Yilin Wen, Du Su, Jinchang Hou, En Wang, Wenbin Liu, Chenfu Bao, Zhonghou Lv

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TEPO, a novel token-level policy optimization framework for RL in LLMs that addresses sparse-reward challenges in CoT reasoning.

**摘要**: arXiv：2604.12736v1宣布类型：新摘要：组相对策略优化（GRPO）显着提高了大型语言模型（LLM）的推理能力，特别是在其数学推理性能方面。然而，GRPO和相关的熵正规化方法仍然难以应对代币级稀疏奖励，这是思想链（CoT）推理中固有的挑战。这些方法通常依赖于未经优化的代币级的熵正规化，这很容易导致稀疏代币奖励下的熵崩溃或模型退化。在这项工作中，我们提出了TEPO，这是一种新型的代币级框架，它（1）利用序列级可能性通过代币级聚合将组级奖励与个人代币联系起来，以及（2）引入代币级KL-分歧屏蔽约束，该约束针对具有积极优势的代币和减少的信息，以减轻突然的策略更新。实验表明，TEPO不仅在数学推理基准上实现了最先进的性能，而且显着增强了训练稳定性，与GRPO/DAPO相比，收敛时间缩短了50%。

[阅读原文](https://arxiv.org/abs/2604.12736)

---

## 7. MolMem：用于样本高效分子优化的内存增强强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ziqing Wang, Yibo Wen, Abhishek Pandy, Han Liu, Kaize Ding

**机构**: REAL-Lab-NU

**💡 亮点 (Highlight)**: Introduces MolMem, a multi-turn agentic RL framework with a dual-memory system for molecular optimization, explicitly focusing on self-improving agents that distill successful trajectories into reusable strategies.

**摘要**: arXiv：2604.12237v1宣布类型：新摘要：在药物发现中，分子优化旨在迭代精炼先导化合物，以改善分子性质，同时保持与原始分子的结构相似性。然而，每次Oracle评估都很昂贵，这使得样本效率成为有限Oracle预算下现有方法的关键挑战。试错法需要多次调用Oracle，而利用外部知识的方法往往会重复使用熟悉的模板，并在具有挑战性的目标上苦苦挣扎。一个关键缺失的部分是长期记忆，它可以为决策奠定基础并为未来的优化提供可重复使用的见解。为了解决这个问题，我们提出了MolMem（\textBF{Mol}分子优化与\textBF{Mem}ory），这是一个具有双存储系统的多轮代理强化学习（RL）框架。具体来说，MolMem使用静态示例记忆来检索冷启动接地的相关示例，并使用进化技能记忆将成功的轨迹提炼成可重复使用的策略。基于这种记忆增强的公式，我们通过密集的分步奖励来训练政策，将昂贵的推出转化为长期知识，以改善未来的优化。大量实验表明，MolMem仅使用500次Oracle调用即可在单属性任务上取得90%的成功（比最佳基线高1.5$x），在多属性任务上取得52%的成功。我们的代码可以在https://github.com/REAL-Lab-NU/MolMem上找到。

[阅读原文](https://arxiv.org/abs/2604.12237)

---

## 8. 迈向机器学习研究的自主长期工程

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guoxin Chen, Jie Chen, Lei Chen, Jiale Zhao, Fanzhe Meng, Wayne Xin Zhao, Ruihua Song, Cheng Chen, Ji-Rong Wen, Kai Jia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces AiScientist, an autonomous agent system for long-horizon ML research engineering, featuring a self-improving loop via durable state and hierarchical orchestration.

**摘要**: arXiv：2604.13018v1宣布类型：新摘要：自主人工智能研究取得了迅速发展，但长期ML研究工程仍然困难：代理必须在任务理解、环境设置、实施、实验和调试方面保持一致的进展。我们引入了AiScientist，这是一个用于ML研究的自主长期工程系统，其基础是一个简单的原则：强大的长期性能需要结构化编排和持久的状态连续性。为此，AiScientist将分层编排与权限范围的文件即巴士工作空间相结合：顶级编排器通过简洁的摘要和工作空间地图来维护阶段级控制，而专门的代理则反复重新构建持久的工件，例如分析、计划、代码和实验证据，而不是主要依赖于对话切换，从而对厚状态进行精简控制。在两个补充基准中，AiScientist将PaperBench得分平均比最佳匹配基线提高了10.54分，并在MLE-Bench Lite上实现了81.82 Any Medal%。消融研究进一步表明，File as-Bus协议是性能的关键驱动因素，删除后PaperBench降低了6.41分，MLE-Bench Lite降低了31.82分。这些结果表明，长期ML研究工程是一个在持久项目状态下协调专业工作的系统问题，而不是纯粹的局部推理问题。

[阅读原文](https://arxiv.org/abs/2604.13018)

---

## 9. 变分语言模型中的统计控制

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yves Ruffenach

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a variational language model with latent hidden computation (EVE) and a controller for agentic internal control, directly aligning with latent CoT/reasoning architectures.

**摘要**: arXiv：2604.12513v1宣布类型：新摘要：我们研究变分语言模型是否可以支持基于其自身内部证据的最小且可测量的代理控制形式。我们的模型结合了局部变分隐藏计算（EVE）、稳态潜在调节器、结构感知检查点保留以及在保留模型之上操作的校准的不确定性感知控制器。我们不是将不确定性视为预测后测量的被动诊断，而是将其视为可以调节训练、支持检查点保留和指导推理时间干预的操作信号。由此产生的框架是故意有重点的。它研究一种闭环形式的内部控制，其中结构性和预测性信号变得可操作。从经验上看，变分主干在语言建模任务上比匹配的确定性参考有所改进，同时还表现出更丰富、更可用的不确定性概况。在此主干之上，经过校准的控制器保持活跃，在完整的代理评估下使用多个动作，并产生积极的质量成本权衡。这些结果支持了一个精确的主张：内部不确定性不仅可以作为变分语言模型的描述属性，还可以作为监管、检查点保留和最小代理路由的实际控制界面。

[阅读原文](https://arxiv.org/abs/2604.12513)

---

## 10. Parcae：稳定循环语言模型的缩放定律

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Hayden Prairie, Zachary Novack, Taylor Berg-Kirkpatrick, Daniel Y. Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Parcae, a stable looped architecture for LLMs that enables latent recurrent computation, directly addressing latent reasoning efficiency.

**摘要**: arXiv：2604.12946v1宣布类型：新摘要：传统的固定深度架构通过增加训练FLOP（通常是通过增加参数化）来扩展质量，但以牺牲更高的内存占用或数据为代价。一个潜在的替代方案是循环架构，它通过循环中的一个层块发送激活来增加FLOP。虽然有希望，但用于训练循环架构的现有方案可能不稳定，会遭受残余爆炸和损失峰值的影响。我们通过将循环重铸为剩余流上的非线性时变动态系统来解决这些挑战。通过对该系统的线性逼近，我们发现由于注入参数中的谱规范大，现有的环路架构中出现了不稳定性。为了解决这些不稳定性问题，我们提出了Parcae，这是一种新型的稳定、循环架构，通过负对角线参数化的离散化来约束注入参数的谱规范。因此，与之前的大规模循环模型相比，Parcae的验证困惑度降低了高达6.3%。使用我们稳定的循环架构，我们研究了循环作为媒介的扩展属性，通过增加训练和测试时间中的FLOP来提高质量。对于训练，我们推导出可预测的功率定律来缩放FLOP，同时保持参数计数固定。我们最初的扩展定律表明，在固定的FLOP预算的情况下，循环和数据应该同时增加。在测试时，我们发现Parcae可以使用循环来扩展计算，遵循可预测的、饱和的指数衰减。当扩展到1.3B参数时，我们发现在固定参数和数据预算下，与强大的Transformer基线相比，Parcae将CORE和Core-Extended质量提高了2.99和1.18个点，实现了高达87.5%的Transformer相对质量。

[阅读原文](https://arxiv.org/abs/2604.12946)

---

## 11. EBER：混合LLM架构中来自习得尖峰神经网络动力学的自主认知行为

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: William Savage

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hybrid cognitive architecture where a persistent spiking neural network autonomously triggers and shapes LLM actions, enabling self-initiated behavior from learned associations.

**摘要**: arXiv：2604.12167v1宣布类型：新摘要：我们提出了（体验调制生物启发的紧急推理），一种混合认知架构，重新组织大型语言模型（LLM）和记忆之间的关系：我们不是用检索工具来增强LLM，而是将LLM作为持久的、基于生物学的关联性底层中的可替换推理引擎。   该架构以220，000个神经元的尖峰神经网络（SNN）为中心，具有尖峰时间相关可塑性（STDP）、四层分层组织（感觉/概念/类别/元模式）、抑制性E/I平衡和奖励调节学习。文本嵌入通过一种新的z分数标准化的top-k人口代码编码到SNN中，该代码通过构造而与维度无关，在嵌入维度上实现了82.2%的区分保留。   我们表明，STDP横向传播在空闲操作期间可以触发和塑造LLM动作，而无需外部提示或脚本触发器：SNN确定何时采取行动以及表面的关联，而LLM选择动作类型并生成内容。在一个实例中，系统在8小时的空闲时段期间横向激发学习到的人-主题关联之后自主地发起与用户的联系。从零学习权重的干净开始，第一个SNN触发的动作仅在7次会话交换（14条消息）后发生。

[阅读原文](https://arxiv.org/abs/2604.12167)

---

## 12. 自回归推理的复杂性示例：思想链与端到端

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Steve Hanneke, Idan Mehalel, Shay Moran

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical analysis showing Chain-of-Thought supervision eliminates sample complexity dependence on generation length, directly relevant to latent reasoning efficiency.

**摘要**: arXiv：2604.12013v1宣布类型：新摘要：现代大型语言模型自回归生成文本，一次生成一个令牌。为了研究此类系统的可学习性，Joshi等人（COLT 2025）为下一个令牌生成器（原始的基础自回归模型）引入了PAC学习框架。在此框架中，未知的下一个令牌生成器将一个令牌序列映射到下一个令牌，并迭代应用于$T$步骤，产生一个令牌链，其最终令牌构成模型的输出。学习任务是学习由这个自回归过程引起的输入-输出映射。根据可用的监督，训练示例可能仅揭示最终输出（端到端监督）或整个生成的链（思想链监督）。这引发了两个自然的问题：样本复杂性如何取决于世代长度$T$，以及多少思想链监督可以减少这种依赖性。   在这项工作中，我们通过揭示样本复杂性如何随$T$扩展的分类法，对这两个问题给出了几乎完整的答案。对于端到端学习，我们表明景观非常丰富：在温和的条件下，本质上恒定和线性之间的任何增长率$r（T）$都可能作为样本复杂性出现，并结合Joshi等人的线性上界，这产生了基本上完整的表征。相比之下，在思想链的监督下，我们表明，样本的复杂性是独立的$T$，表明访问中间推理步骤可以完全消除对生成长度的依赖。我们的分析引入了新的组合工具，作为推论，我们解决了Joshi等人提出的几个悬而未决的问题。关于可学习性对生成长度的依赖和思想链监督的作用。

[阅读原文](https://arxiv.org/abs/2604.12013)

---

## 13. 搜索检索：不要只是搜索原始数据，为记忆增强的搜索系统搜索想法

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tao Feng, Pengrui Han, Guanyu Lin, Ge Liu, Jiaxuan You

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving long-term memory for agents that grows more capable through continuous interaction, aligning with self-improving agent frameworks.

**摘要**: arXiv：2604.12231v1宣布类型：新摘要：大型语言模型（LLM）凭借其强大的内部能力和知识改变了人工智能研究。然而，现有的LLM在与世界互动时仍然未能有效地融入大量的外部知识。尽管提出了检索增强的LLM来缓解这个问题，但它们仍然从根本上受到LLM上下文长度的限制，因为它们只能从通常由数百万个数据块组成的外部知识库中检索前K个原始数据块。在这里，我们提出了一种新颖的模型不可知算法，它可以帮助LLM根据任意长的外部数据生成输出，而不受上下文长度或检索到的数据块数量的限制。我们的关键见解是让LLM充分利用解决过去的用户查询（想法）时产生的中间响应，过滤无意义和多余的想法，将它们组织在思想记忆中，并在解决新查询时检索相关想法。这有效地为基于LLM的代理提供了自我进化的长期记忆，该记忆通过持续的互动变得更有能力。除了算法创新之外，我们还精心准备了一个新颖的基准：AcademicEval，它要求法学硕士忠实地利用超长上下文来回答基于现实世界学术论文的查询。对AcademicEval和其他两个公共数据集的广泛实验证实，Right-Retriever的表现显着优于最先进的基线，在各种任务中实现了F1成绩平均至少7.6%和胜率平均增加16%。更重要的是，我们进一步展示了两个令人兴奋的发现：（1）Reight-Retriever确实可以帮助LLM在解决更多用户查询后自我进化;（2）Reight-Retriever学会利用更深层次的想法来回答更抽象的用户查询。

[阅读原文](https://arxiv.org/abs/2604.12231)

---

## 14. 潜在规划随着规模的扩大而出现

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Michael Hanna, Emmanuel Ameisen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies latent planning in LLMs, providing a framework and mechanistic evidence that internal planning representations emerge with scale, directly aligning with latent CoT/reasoning research.

**摘要**: arXiv：2604.12493v1宣布类型：新摘要：LLM可以执行看似计划密集型的任务，例如编写连贯的故事或运行代码，而无需明确表达计划;然而，他们隐含计划的程度尚不清楚。在本文中，我们将潜在规划定义为当LLM拥有内部规划表示时发生的，这些表示（1）导致特定未来代币或概念的生成，以及（2）塑造先前的上下文以许可所述未来代币或概念。我们研究了Qwen-3家族（0.6B-14 B）在简单计划任务上的表现，发现潜在的计划能力随着规模的增加而增加。计划模型具有代表计划词（如“会计师”）的特征，并使它们输出“an”而不是“a”;此外，即使是不太成功的Qwen-3 4 B-8B也有新生的计划机制。在完成押韵对句这一更复杂的任务时，我们发现模型通常会提前识别出一个押韵，但即使是大型模型也很少提前计划。然而，当我们将模型转向散文中的计划词时，我们可以引出一些随着规模而增加的计划。总而言之，我们提供了一个衡量规划的框架，以及模型规划能力如何随着规模而增长的机械证据。

[阅读原文](https://arxiv.org/abs/2604.12493)

---

## 15. 通过相关代理缓解奖励黑客的鲁棒优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zixuan Liu, Xiaolin Sun, Zizhan Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a robust optimization framework for RL agents to mitigate reward hacking by optimizing against worst-case correlated proxy rewards.

**摘要**: arXiv：2604.12086v1公告类型：新摘要：在存在不完美奖励信号的情况下设计鲁棒的强化学习（RL）代理仍然是一个核心挑战。在实践中，代理人经常接受代理奖励的训练，这些奖励只接近真实目标，使他们容易受到奖励黑客的攻击，其中高代理回报来自无意或剥削行为。最近的工作正式使用代理和真实奖励之间的r相关性来解决这个问题，但是现有的方法，如占用正则化策略优化（ORPO），针对固定代理进行优化，并且不能针对更广泛的相关代理类别提供强有力的保证。在这项工作中，我们制定奖励黑客作为一个强大的政策优化问题，在所有r相关的代理奖励的空间。我们推导出一个易于处理的最大-最小公式，在最坏情况下的代理一致的相关约束下，代理最大限度地提高性能。我们进一步表明，当奖励是已知特征的线性函数时，我们的方法可以适应于结合这种先验知识，从而产生改进的策略和可解释的最坏情况奖励。跨多种环境的实验表明，我们的算法在最坏情况下的回报方面始终优于ORPO，并在不同级别的代理与真实回报相关性之间提供了更好的鲁棒性和稳定性。这些结果表明，我们的方法在奖励设计本质上不确定的环境中提供了稳健性和透明度。该代码可在https://github.com/ZixuanLiu4869/reward_hacking上获取。

[阅读原文](https://arxiv.org/abs/2604.12086)

---

## 16. Frontier-Eng：通过生成式优化对现实世界工程任务的自我进化代理进行基准测试

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yizhe Chi, Deyao Hong, Dapeng Jiang, Tianwei Luo, Kaisen Yang, Boshi Zhang, Zhe Cao, Xiaoyan Fan, Bingxiang He, Han Hao, Weiyang Jin, Dianqiao Lei, Qingle Liu, Houde Qian, Bowen Wang, Situ Wang, Youjie Zheng, Yifan Zhou, Calvin Xiao, Eren Cai, Qinhuai Na

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a benchmark for generative optimization, a propose-execute-evaluate loop for agents, directly aligning with self-evolving agent frameworks that improve through iterative feedback.

**摘要**: arXiv：2604.12290v1宣布类型：新摘要：当前的LLM代理基准主要关注二进制通过/失败任务，例如代码生成或基于搜索的问答，通常忽视了现实世界工程的价值，而现实世界工程的价值通常是通过可行设计的迭代优化来捕捉的。为此，我们引入Frontier-Eng，这是一个经过人类验证的生成式优化基准--一个迭代的提议-执行-评估循环，其中代理生成候选工件，接收可执行验证者反馈，并在固定的交互预算下修改它们--跨越五个广泛的工程类别中的47美元任务。与以前的套件不同，Frontier-Eng任务基于工业级模拟器和验证器，这些模拟器和验证器提供连续的奖励信号，并在有限的预算下执行硬可行性约束。我们使用代表性的搜索框架评估了八种前沿语言模型，发现虽然Claude 4.6 Opus实现了最强大的性能，但基准测试对所有模型来说仍然具有挑战性。我们的分析表明，改善频率（$\sim $1/迭代）和幅度（$\sim $1/改善计数）的双幂律衰减。我们进一步表明，虽然宽度提高了并行性和多样性，深度仍然是在固定预算下来之不易的改进至关重要。Frontier-Eng建立了一个新标准，用于评估人工智能代理将领域知识与可执行反馈集成以解决复杂、开放式工程问题的能力。

[阅读原文](https://arxiv.org/abs/2604.12290)

---

## 17. 周期一致性搜索：问题可重建性作为搜索代理培训的代理奖励

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sohyun An (Meta Superintelligence Labs, UCLA), Shuibenyang Yuan (Meta Superintelligence Labs), Hayeon Lee (Meta Superintelligence Labs), Cho-Jui Hsieh (UCLA), Alexander Min (Meta Superintelligence Labs)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a gold-supervision-free RL framework (Cycle-Consistent Search) for training search agents using a novel cycle-consistency reward derived from question reconstructability.

**摘要**: arXiv：2604.12967v1宣布类型：新摘要：强化学习（RL）在优化复杂信息检索任务中的搜索代理方面表现出了强大的潜力。然而，现有的方法主要依赖于黄金监督，例如难以扩展的地面真相答案。为了解决这一局限性，我们提出了循环一致性搜索（CCS），这是一个用于训练搜索代理的无黄金监督框架，其灵感来自无监督机器翻译和图像到图像翻译的循环一致性技术。我们的关键假设是，与不充分或不相关的搜索轨迹不同，最佳搜索轨迹可以作为问题意图的无损编码。因此，高质量的轨迹应该保留准确重建原始问题所需的信息，从而引发政策优化的奖励信号。然而，天真的循环一致性目标很容易受到信息泄露的影响，因为重建可能依赖于表面的词汇线索而不是底层的搜索过程。为了减少这种影响，我们应用了信息瓶颈，包括排除最终响应和搜索查询的命名实体识别（NER）掩蔽。这些约束迫使重建依赖于检索到的观察结果以及结构支架，确保产生的奖励信号反映信息充分性而不是语言冗余。问答基准的实验表明，CCS的性能与监督基线相当，同时优于不依赖黄金监督的先前方法。这些结果表明，CCS提供了一种可扩展的训练范式，用于在无法获得黄金监督的环境中训练搜索代理。

[阅读原文](https://arxiv.org/abs/2604.12967)

---

## 18. SOAR：扩散模型中最佳对齐和细化的自我修正

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: You Qin, Linqing Wang, Hao Fei, Roger Zimmermann, Liefeng Bo, Qinglin Lu, Chunyu Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SOAR, a reward-free, on-policy self-correction method for diffusion models that provides dense per-timestep supervision, directly addressing the gap between SFT and RL alignment.

**摘要**: arXiv：2604.12617v1宣布类型：新摘要：扩散模型的后训练管道目前分为两个阶段：对策划数据的监督微调（SFT）和具有奖励模型的强化学习（RL）。他们之间存在着根本性的差距。SFT仅在从正向去噪过程中采样的地面真实状态上优化去噪器;一旦推断偏离这些理想状态，后续去噪依赖于分布外泛化而不是学习校正，表现出与自回归模型相同的暴露偏差，但沿着去噪轨迹而不是令牌序列积累。RL原则上可以解决这种不匹配，但其终端奖励信号是稀疏的，具有信用分配困难，并有奖励黑客的风险。我们提出了SOAR（Self-Correction for Optimal Alignment and Refinement），这是一种弥补这一空白的偏差校正后训练方法。从真实样本开始，SOAR对当前模型执行单个停止梯度卷展，重新噪化产生的偏离轨迹状态，并监督模型转向原始干净目标。该方法符合政策、免费奖励，并提供密集的逐时步监督，没有信用分配问题。在SD 3.5-Medium上，SOAR将GenEval从0.70提高到0.78，将OCR从0.64提高到0.67，同时提高了所有基于模型的偏好分数。在受控奖励特定实验中，尽管无法访问奖励模型，但SOAR在美学和文本图像对齐任务的最终指标值上都超过了Flow-GRPO。由于SOAR的基本损失包含了标准的SFT目标，因此它可以直接取代SFT作为预训练后更强的第一训练后阶段，同时保持与后续RL对齐完全兼容。

[阅读原文](https://arxiv.org/abs/2604.12617)

---

## 19. 重新思考大型语言模型的政策提炼：现象学、机制和配方

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yaxuan Li, Yuxin Zuo, Bingxiang He, Jinqian Zhang, Chaojun Xiao, Cheng Qian, Tianyu Yu, Huan-ang Gao, Wenkai Yang, Zhiyuan Liu, Ning Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically investigates the dynamics and mechanisms of On-Policy Distillation (OPD), a core post-training technique for LLMs, and proposes strategies to recover failing distillation.

**摘要**: arXiv：2604.13016v1宣布类型：新摘要：按策略提炼（OPD）已成为大型语言模型后训练的核心技术，但对其训练动态的了解仍然很少。本文对OPD的动力学和机制进行了系统研究。我们首先确定有两个条件决定OPD的成功或失败：（i）学生和教师应该共享兼容的思维模式;（ii）即使思维模式一致和分数更高，教师也必须提供超越学生在培训期间所看到的真正新的能力。我们通过弱到强的反向蒸馏来验证这些发现，表明从学生的角度来看，同一家庭1.5B和7 B教师在分布上没有区别。通过对代币级机制的探索，我们表明成功的OPD的特点是在学生访问的州对高概率代币进行渐进式对齐，这是一个集中了大部分概率质量（97%-99%）的小型共享代币集。我们进一步提出了两种实用的策略来恢复失败的OPD：政策外冷启动和教师一致的即时选择。最后，我们表明，OPD看似免费的密集代币级奖励午餐是有代价的，这引发了OPD是否可以扩展到长期蒸馏的问题。

[阅读原文](https://arxiv.org/abs/2604.13016)

---

## 20. 视觉识别的主动假设探索的统计发现

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jaywon Koo, Jefferson Hernandez, Ruozhen He, Hanjie Chen, Chen Wei, Vicente Ordonez

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an agentic framework (HypoExplore) for neural architecture discovery that uses LLM-guided hypothesis generation and a self-improving loop of evaluation and confidence updates.

**摘要**: arXiv：2604.12999v1宣布类型：新摘要：我们引入了HypoExplore，这是一个代理框架，将视觉识别的神经架构发现制定为假设驱动的科学探究。鉴于人类指定的高级研究方向，HypoExplore通过进化分支构思、实施、评估和改进神经架构。新假设是通过选择要建立的父假设，使用大型语言模型创建的，并在平衡利用已验证的原则与解决不确定原则的双重策略的指导下创建的。我们提出的框架维护了一个轨迹树，记录了所有提出的架构的谱系，以及一个假设记忆库，主动跟踪通过实验证据获得的置信度分数。每次实验结束后，多个反馈代理会从不同的角度分析结果，并将其发现整合到假设置信度更新中。我们的框架在CIFAR-10上进行了发现轻量级视觉架构的测试，最高达到94.11%的准确性是从18.91%开始的根节点基线演变而来的，并推广到CIFAR-100和Tiny-ImageNet。我们通过在MedMNIST上进行独立的架构发现运行，进一步证明了对专业领域的适用性，从而产生了最先进的性能。我们表明，随着证据的积累，假设置信度分数的预测性越来越强，并且学到的原则会在独立的进化谱系中转移，这表明HypoExplore不仅发现了更强大的架构，而且可以帮助建立对设计空间的真正理解。

[阅读原文](https://arxiv.org/abs/2604.12999)

---

## 21. EntEcho：来自视觉语言模型的无注释奖励，用于文本到图像强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jinlong Liu, Wanggui He, Peng Zhang, Mushui Liu, Hao Jiang, Pipei Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PromptEcho, a novel annotation-free reward construction method for RL-based improvement of text-to-image models, directly aligning with RL for LLMs via scalable reward design.

**摘要**: arXiv：2604.12652v1宣布类型：新摘要：强化学习（RL）可以提高文本到图像（T2 I）模型的提示跟随能力，但获得高质量的奖励信号仍然具有挑战性：CLIP Score粒度太粗，而基于PLM的奖励模型（例如，RewardDance）需要昂贵的人工注释偏好数据和额外的微调。我们提出了EntEcho，这是一种奖励构建方法，需要\{no}注释和\{no}奖励模型训练。给定生成的图像和引导查询，Inbox Echo计算以原始提示作为标签的冻结VLM的标记级交叉熵损失，直接提取VLM预训练期间编码的图像-文本对齐知识。回报是确定性的、计算效率高的，并且随着更强大的开源VLM的出现而自动改进。对于评估，我们开发了DenseAlignBench，这是一个概念丰富的密集字幕基准，用于严格测试提示跟随能力。在两个最先进的T2 I模型（Z-Image和QwenImage-2512）上的实验结果表明，在没有任何特定任务训练的情况下，AdmitEcho在DenseAlignBench上实现了实质性的改进（+26.8pp / +16.2pp净胜率），同时在GenEval、DPG-Bench和TIIFBench上实现了一致的增益。消融研究证实，在相同的VLM条件下，AktEcho的综合表现优于基于推理的评分，并且奖励质量随VLM大小而变化。我们将开源训练模型和DenseAlignBench。

[阅读原文](https://arxiv.org/abs/2604.12652)

---

## 22. DocSeeker：具有证据基础的结构化视觉推理，用于长文档理解

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hao Yan, Yuliang Liu, Xingchen Liu, Yuyi Zhang, Minghui Liao, Jihao Wu, Wei Chen, Xiang Bai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Evidence-aware Group Relative Policy Optimization, a novel RL method for joint optimization of evidence localization and answer accuracy in long-document agents.

**摘要**: arXiv：2604.12812v1宣布类型：新摘要：随着文档长度的增加，现有的多模式大型语言模型（MLLM）在长文档理解任务中的性能会显着下降。这源于两个基本挑战：1）低信噪比（SNR），关键证据隐藏在不相关的页面中; 2）监督稀缺，因为仅提供最终简短答案的数据集提供了弱的学习信号。在本文中，我们通过提出一个范式来解决这些挑战，该范式要求模型执行结构化的“\textBF{Analysing}、\textBF{Localism}和\textBF{Reasoning}”工作流程。为了灌输这种能力，我们设计了一个两阶段训练框架：我们首先对通过高效的知识提炼策略生成的高质量数据执行监督微调。随后，我们采用了证据感知组相对政策优化，该优化对证据本地化和答案准确性进行联合优化。此外，我们还引入了证据引导的解决方案分配策略，以减轻多页文档训练的内存限制。大量的实验表明，DocSeeker在域内和域外任务上都实现了卓越的性能。我们表明，它可以从短页面训练到超长文档进行强大的推广，并且与视觉检索增强生成系统自然协同，为其实现奠定了坚实的基础。

[阅读原文](https://arxiv.org/abs/2604.12812)

---

## 23. 从模仿到歧视：渐进式课程学习以实现稳健的网络导航

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chuang Peng, Wei Zhang, Renshuai Tao, Xinhao Zhang, Jian Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a progressive curriculum for web agents using ORPO and GRPO, directly aligning with RL for LLMs through novel preference optimization methods for robust discrimination and long-horizon consistency.

**摘要**: arXiv：2604.12666v1宣布类型：新摘要：基于文本的Web代理为自主Web导航提供了计算效率，但由于现实世界的HTML的噪音和多样性，开发稳健的代理仍然具有挑战性。标准监督微调（SFT）方法在两个关键方面失败：它们缺乏区分能力，无法拒绝人口稠密的页面中看似合理但不正确的元素，并且对未见的网站布局的概括有限。为了应对这些挑战，我们引入了Triton数据集（59万个实例）和渐进式培训课程。Triton是通过结构-语义硬负挖掘（显式地挖掘topological相似的干扰物）和双代理共识管道（Dual-Agent Consensus管道）构建的，该管道通过严格验证综合各种跨领域任务。在此基础上，我们的渐进课程产生了三个模型：Triton-SFT-32 B用于基本模仿，Triton-ORPO-32 B用于通过赔率比偏好优化实现稳健区分，以及Triton-GRPO-32 B用于通过群体相对政策优化实现长期一致性。对Mind 2 Web的实证评估表明，Triton-GRPO-32 B在开源模型中实现了最先进的性能，Step Success率为58.7%，超过GPT-4.5（42.4%）和Claude-4.5（41.4%）超过16%，验证了专业数据课程超过了网络导航的原始参数规模。

[阅读原文](https://arxiv.org/abs/2604.12666)

---

## 24. PubSwap：联邦WLVR的公共数据政策外协调

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Anupam Nayak, Baris Askin, Muhammed Ustaomeroglu, Carlee Joe-Wong, Gauri Joshi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a federated RLVR framework for reasoning post-training, combining LoRA-based local adaptation with public-data off-policy coordination to improve alignment across decentralized private data.

**摘要**: arXiv：2604.12160v1宣布类型：新摘要：通过来自可验证奖励的强化学习（WLVR）进行训练后推理通常是在集中式环境中研究的，但许多现实的应用涉及分布在组织中的去中心化私人数据。联合训练是一种自然的解决方案，但在此机制中扩展WLVR具有挑战性：全模型同步成本高昂，并且执行许多本地步骤可能会导致在异类数据下严重的客户端漂移。我们提出了一个联邦WLVR框架，该框架将基于LoRA的本地适应与基于公共数据的非政策步骤相结合，以提高通信效率和跨客户端协调。特别是，小型共享公共数据集用于定期交换和重复使用组织之间的响应级训练信号，为实现更加全球一致的目标提供轻量级锚点，而不会暴露私人数据。我们的方法在公共数据步骤中选择性地用全球正确的响应替换局部错误的响应，从而使培训更接近当地政策，同时仍然受益于跨客户协调。在数学和医学推理基准和模型中，我们的方法始终优于标准基线。我们的结果强调了训练后联邦推理的简单有效方法：将低级别通信与有限的公共数据协调相结合。

[阅读原文](https://arxiv.org/abs/2604.12160)

---

## 25. 变形金刚如何学习通过多代币预测进行计划

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jianhao Huang, Zhanpeng Zhou, Renqiu Xia, Baharan Mirzasoleiman, Weijie Su, Wei Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies how multi-token prediction objectives induce robust, interpretable reasoning circuits in Transformers, directly relevant to latent reasoning mechanisms.

**摘要**: arXiv：2604.11912v1宣布类型：新摘要：虽然下一个令牌预测（Norton）一直是训练语言模型的标准目标，但它常常难以捕捉推理任务中的全局结构。多令牌预测（STP）最近成为一种有前途的替代方案，但其潜在机制仍然知之甚少。在本文中，我们研究了MTA如何促进推理，重点关注规划。从经验上看，我们表明，在合成图寻路任务和更现实的推理基准（例如倒计时和布尔可满足性问题）方面，STP始终优于NP。从理论上讲，我们在星象任务上分析了简化的两层Transformer。我们证明了STP引入了两阶段的反向推理过程：模型首先关注端节点，然后通过向后跟踪中间节点来重建路径。这种行为源于STP的梯度去耦合特性，与NP相比，它提供了更干净的训练信号。最终，我们的结果凸显了多令牌目标如何本质上使优化偏向稳健且可解释的推理电路。

[阅读原文](https://arxiv.org/abs/2604.11912)

---

## 26. KG-Reasoner：一种端到端多跳知识图推理的增强模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Shuai Wang, Yinan Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces KG-Reasoner, an end-to-end LLM framework that uses Reinforcement Learning to internalize KG traversal for multi-hop reasoning.

**摘要**: arXiv：2604.12487v1宣布类型：新摘要：大型语言模型（LLM）在自然语言理解和生成方面表现出强大的能力，但它们在知识密集型推理方面遇到了困难。结构化知识图（KG）提供了一种有效的外部知识表示形式，并已广泛用于提高经典知识库问题解答（KBQA）任务的性能。然而，在KG上对复杂查询执行精确的多跳推理仍然极具挑战性。大多数现有的方法将推理过程分解为通过固定管道执行的一系列孤立步骤。虽然在某种程度上有效，但此类设计限制了推理的灵活性，并使整个决策过程支离破碎，通常导致不连贯以及早期步骤中关键中间信息的丢失。在本文中，我们介绍了KG-Reasoner，这是一个端到端框架，将多步骤推理集成到推理LLM的统一“思维”阶段。通过强化学习（RL），LLM被训练为内化KG穿越过程，使其能够动态探索推理路径，并在必要时执行回溯。对八个多跳和知识密集型推理基准的实验表明，与最先进的方法相比，KG-Reasoner实现了有竞争力或更优越的性能。代码可在存储库上获取：https://github.com/Wangshuaiia/KG-Reasoner。

[阅读原文](https://arxiv.org/abs/2604.12487)

---

## 27. ReasonXL：在不牺牲性能的情况下转变LLM推理语言

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Daniil Gurgurov, Tom R\"ohr, Sebastian von Rohrscheidt, Josef van Genabith, Alexander L\"oser, Simon Ostermann

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage pipeline (SFT + RL with verifiable rewards) to adapt LLMs to reason in non-English languages, directly matching RL for LLMs criteria.

**摘要**: arXiv：2604.12378v1宣布类型：新摘要：尽管多语言能力取得了进步，但大多数大型语言模型（LLM）在训练中以及最重要的是在推理痕迹的产生中仍然以英语为中心。即使在处理非英语问题时，这些模型也主要以英语推理，从而导致非英语使用场景的根本不匹配。   我们通过三项贡献直接解决了这种差异。(i)我们引入了ReasonXL，这是第一个跨越五种欧洲语言（英语、德语、法语、意大利语和西班牙语）的跨领域推理痕迹的大规模并行数据库，每种语言有超过200万个对齐样本，每个样本都包括提示、推理痕迹和最终输出，从而能够直接监督特定语言的推理。(ii)使用ReasonXL，我们证明了LLM可以完全以所需的目标语言进行推理，使用简单的两阶段监督微调（SFT）管道，然后是具有可验证奖励的强化学习（WLVR）。由此产生的模型符合或超过了基线性能，常识损失最小，跨语言迁移得到了广泛保留。(iii)我们对适应进行了广泛的代表性分析，并在模型深度上找到了明确的功能划分：早期层包含因果决定语言身份的激活瓶颈，而上层则集中了适应驱动的权重和激活变化。我们进一步发现，与SFT相比，RLVR通过更少的参数更新实现了与基本模型的更大的行为分歧，这表明尽管权重更新小得多，但代表性重路由更有效。

[阅读原文](https://arxiv.org/abs/2604.12378)

---

## 28. 使用Rubric Rewards优化视觉偏好

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Ya-Qi Yu, Fangyu Hong, Xiangyang Qu, Hao Wang, Gaojie Wu, Qiaoyu Luo, Nuo Xu, Huixin Wang, Wuheng Xu, Yongxin Liao, Zihao Chen, Haonan Li, Ziming Li, Dezhi Peng, Minghui Liao, Jihao Wu, Haoyu Ren, Dandan Tu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes rDPO, a preference optimization framework using instance-specific rubric rewards for fine-grained visual reasoning, directly aligning with RL for LLMs via novel reward design.

**摘要**: arXiv：2604.13029v1宣布类型：新摘要：直接偏好优化（DPO）的有效性取决于反映多模式任务中重要的质量差异的偏好数据。现有的管道通常依赖于政策外的扰动或基于结果的粗略信号，这些信号不太适合细粒度的视觉推理。我们提出了rDPO，这是一个基于特定实例主题的偏好优化框架。对于每个图像-指令对，我们创建一个包含基本和额外标准的清单式标题，以对任何可能策略的响应进行评分。描述规则池是离线构建的，并在构建政策上数据期间重复使用。在公共奖励建模基准上，基于标题的激励极大地改善了30 B-A3 B法官，使其接近GPT-5.4。在公共下游基准上，基于标题的过滤将宏观平均值提高到82.69，而基于结果的过滤将宏观平均值从81.14下降到75.82。在综合基准上评估可扩展性时，rDPO达到61.01，明显优于风格限制的基线（52.36）并超过59.48基本模型。总而言之，这些结果表明视觉偏好优化受益于将政策数据构建与特定实例的标准级反馈相结合。

[阅读原文](https://arxiv.org/abs/2604.13029)

---

## 29. 通过强化学习教授法学硕士对不适当论证进行类人编辑

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Timon Ziegenbein, Maja Stahl, Henning Wachsmuth

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning approach (group relative policy optimization) to teach LLMs human-like, self-contained editing strategies for improving argument appropriateness.

**摘要**: arXiv：2604.12770v1宣布类型：新摘要：编辑人类编写的文本已成为大型语言模型（LLM）的标准用例，例如，以使论点更适合讨论。然而，将人类与LLM生成的编辑进行比较，我们观察到编辑策略不匹配：虽然LLM经常执行多个分散的编辑，并且往往会显着改变意义，但人类宁愿将依赖改变封装在独立的、保留意义的编辑中。在本文中，我们提出了一种强化学习方法，教LLM进行类人编辑，以提高论点的适当性。我们的方法产生独立的业务级编辑建议，可以独立接受或拒绝。我们使用团体相对政策优化和多组件奖励功能来训练该方法，该功能联合优化编辑级语义相似性、流畅性和模式一致性以及论点级适当性。在自动和人工评估方面，它优于竞争基准和类人编辑的最新水平，多轮编辑实现了接近完全重写的适当性。

[阅读原文](https://arxiv.org/abs/2604.12770)

---

