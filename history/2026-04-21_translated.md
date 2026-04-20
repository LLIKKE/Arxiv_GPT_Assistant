# 💡 今日研究速览 (Daily Summary)

# LLC和对齐的RL
当今的主导主题是超越来自人类反馈的基本强化学习（RL HF），向LLM更稳健、可验证和高效的RL范式的复杂推动。一个关键突破是专注于打击奖励黑客攻击并确保忠实的推理。GRift等方法使用梯度指纹来检测欺骗性优化，而AtManRL利用可区分注意力显着性来训练模型，以产生真正影响输出的推理痕迹。与此同时，CPO++和CiPO等框架通过高级反事实和迭代偏好优化来解决推理模型中非平稳性和取消学习的挑战。集体方向强调RL，它不仅是奖励驱动的，而且具有推理意识，并且对分布漂移和对抗性游戏具有鲁棒性。

# 代理和自我改进系统
代理系统的研究正在向通过交互实现自主闭环进化的架构融合。核心创新是从静态的、提示的代理转向具有动态的、可学习的内部状态的系统。CoEvolve和Policy Bank等框架引入了代理及其训练数据之间相互进化的机制，以及在内存中进化政策理解的机制。通过MCTS对代理技能进行二层优化等工作是补充的，该工作将技能改进形式化为优化问题。趋势很明显：下一代智能体将不仅使用工具，还将拥有可更新的内部“装备”或记忆，使他们能够根据经验学习和调整自己的能力和世界模型，正如Milkyway等系统中所见，以进行未来预测。

# 潜在推理与效率
一个重要的概念和工程线索质疑推理本身的本质，认为它是一个潜伏状态轨迹，而不是显式的思想链标记。这一观点直接推动了效率创新。为了支持复杂的潜在推理，使用概率尝试的顺序KV缓存压缩等新方法旨在打破压缩限制，而STOP等技术则学习尽早修剪并行架构的推理路径。其目标是使潜在推理的计算密集型过程大规模易于处理，确保推理质量的进步不会因推理期间令人望而却步的记忆或计算要求而受到阻碍。

# 多模式和专业应用RL
RL技术正在成功定制以解决特定、具有挑战性的领域，展示了该框架的多功能性。在多模式推理中，提出了一种具有鲁棒改进奖励（GRPO）的师生RL管道用于视频上下文修复。在科学领域，基于RL的后训练在缩小小分子药物设计中的能力差距方面表现出了巨大的希望。对于事件预测等开放式任务，精心设计了新颖的RL奖励设计（SCATTER）来生成多样化且包容性的假设。这一方向凸显了从通用一致转向开发专门的RL目标和培训方案的转变，这些目标和培训方案直接优化复杂的特定领域任务的性能。

# SFT和偏好优化
虽然RL占主导地位，但通常先于它的监督和偏好优化基础正在持续完善。输出多样性崩溃的分析追踪了SFT、DPO和CoT蒸馏对模型权重的影响，为后训练提供重要的诊断。为了解决可扩展性问题，GroupDPO引入了一种内存高效的分组偏好优化算法。此外，提示注入等方法战略性地增加了训练数据，以提供关键的推理步骤，提高了后续RL的样本效率。这项工作确保了基础模型和初始对齐阶段更加有效和高效，为高级RL训练创造了更强大的起点。

---

## 1. 利用梯度指纹检测和抑制奖励黑客

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Songtao Wang, Quang Hieu Pham, Fangcong Yin, Xinpeng Wang, Jocelyn Qiaochu Chen, Greg Durrett, Xi Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GRIFT, a method using gradient fingerprints to detect and suppress reward hacking in LLM reasoning, directly relevant to RL for LLMs with verifiable rewards.

**摘要**: arXiv：2604.16242v1公告类型：新摘要：具有可验证奖励的强化学习（WLVR）通常会优化结果奖励，而不会对中间推理施加限制。这使得训练容易受到奖励黑客攻击，模型利用漏洞（例如，训练数据中的虚假模式）在奖励函数中实现高分而无需解决预期任务。这些奖励黑客行为通常是隐性的，因为中间思想链（CoT）表面上可能看似合理，从而限制了纯粹基于文本的监控的有效性。我们提出了梯度指纹（GRFT），这是一种使用模型内部计算检测奖励黑客攻击的方法。给定提示和模型生成的CoT，GRFT计算以提示为条件的CoT的梯度，并将其压缩成紧凑的表示，然后用于评估CoT是否反映了奖励黑客行为。在涵盖数学、代码和逻辑推理的可验证推理基准中，GRFT的表现大大优于包括CoT Monitor和TRACE在内的强大基线，在检测奖励黑客行为方面实现了超过25%的相对改进。此外，将GRFT集成到推理任务的拒绝微调管道中可以减少奖励黑客攻击并提高真实任务目标的性能。我们的结果强调了利用梯度水平表示来评估CoT推理痕迹质量的一个有前途的方向。我们的代码可访问：https://github.com/songtao-x/reward_hack。

[阅读原文](https://arxiv.org/abs/2604.16242)

---

## 2. 超越分配精简：任务奖励的重要性

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sarthak Mittal, Leo Gagnon, Guillaume Lajoie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly analyzes and advocates for task-reward-based RL for LLMs, demonstrating its superiority over distribution sharpening for robust performance improvement.

**摘要**: arXiv：2604.16259v1宣布类型：新摘要：在将基于任务奖励的强化学习（RL）集成到其训练管道中后，前沿模型展示了非凡的能力，使系统能够从纯推理模型发展为复杂的代理。然而，关于RL是否真正在基础模型中灌输新技能，还是仅仅简化其现有分布以激发潜在能力的争论仍然存在。为了解决这种二分法，我们对分布细化和基于任务奖励的学习进行了明确的比较，利用RL作为实现这两种范式的工具。我们的分析揭示了分布尖锐化的固有局限性，从第一原则出发证明了最优值如何以及为什么会是不利的，并且该方法从根本上不稳定。此外，我们在数学数据集上使用Llama-3.2- 3B-Direct、Qwen 2.5 - 3B-Direct和Qwen 3 - 4 B-Direct-2507的实验证实，细化的收益有限，而结合基于任务的奖励信号可以极大地帮助实现稳健的性能改进和稳定的学习。

[阅读原文](https://arxiv.org/abs/2604.16259)

---

## 3. CoEvolve：通过代理数据相互进化培训LLM代理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shidong Yang, Ziyu Ma, Tongwen Huang, Yiming Hu, Yong Wang, Xiangxiang Chu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CoEvolve, an agent-data mutual evolution framework enabling LLM agents to improve through closed-loop, interaction-driven training, directly matching self-evolving agent criteria.

**摘要**: arXiv：2604.15840v1宣布类型：新摘要：LLM代理的强化学习通常是在静态数据分布上进行的，这无法适应代理不断变化的行为，并导致复杂环境交互的覆盖率较差。为了应对这些挑战，我们提出了CoEvolve，这是一个代理-数据相互进化框架，使LLM代理能够通过闭环、交互驱动的培训进行改进。具体来说，CoEvolve从推出轨迹中提取遗忘和不确定性等反馈信号，以识别容易失败的交互模式，并利用它们来指导基于LLM的任务合成。合成的任务通过环境交互进行验证，并用于更新数据分布，从而实现代理及其数据的联合适应。在Qwen 2.5 - 7 B、Qwen 3 - 4 B和Qwen 3 - 30 B-A3 B上对AppWorld和BFCL进行的广泛实验表明，与强基础模型相比，取得了一致且显着的改进，绝对收益分别为19.43%、15.58%和18.14%。

[阅读原文](https://arxiv.org/abs/2604.15840)

---

## 4. AgentV-RL：带验证器的标度报酬模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiazheng Zhang, Ziche Fu, Zhiheng Xi, Wenqing Jing, Mingxu Chai, Wei He, Guoqiang Zhang, Chenghao Fan, Chenxin An, Wenxiang Chen, Zhicheng Liu, Haojie Pan, Dingwei Zhu, Tao Gui, Qi Zhang, Xuanjing Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes AgentV-RL, a novel RL-based framework for agentic reward modeling where a verifier autonomously interleaves tool-use with reasoning via proactive exploration and reinforcement learning.

**摘要**: arXiv：2604.16004v1宣布类型：新摘要：验证器已被证明可以通过测试时间缩放（TTC）增强LLM推理。然而，他们在复杂领域面临着重大挑战。不正确的中间推理造成的错误传播可能会导致看似合理的解决方案出现假阳性，而缺乏外部基础会使验证器在计算或知识密集型任务中不可靠。为了应对这些挑战，我们提出了抽象验证器，这是一个将奖励建模转化为多回合、工具增强的审议过程的框架。我们引入了互补的前向和后向代理：一个从前提到结论追踪解决方案，而另一个则根据其基本前提重新检查结论。这个双向过程可以对解决方案进行全面、可靠且可解释的评估。为了促进实际部署，我们提出了AgentV-RL。通过主动探索和强化学习，验证者自主地将工具使用与内部推理交织在一起。大量实验表明，Atlanttic Verification在并行和顺序TTC下都能产生一致的性能提升。值得注意的是，我们的4 B变体比最先进的ORM高出25.2%，使其成为代理奖励建模的一个有前途的范式。

[阅读原文](https://arxiv.org/abs/2604.16004)

---

## 5. Policy Bank：LLM代理人不断发展的政策理解

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jihye Choi, Jinsung Yoon, Long T. Le, Somesh Jha, Tomas Pfister

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PolicyBank, a memory mechanism for LLM agents that evolves policy understanding through interaction and feedback, directly aligning with self-improving agent frameworks.

**摘要**: arXiv：2604.15505v1宣布类型：新摘要：根据组织政策运作的LLM代理必须遵守通常以自然语言指定的授权约束。在实践中，此类规范不可避免地包含歧义和逻辑或语义差距，导致代理的行为系统性地偏离真实需求。我们问：通过让代理通过来自部署前测试的交互和纠正反馈来发展其政策理解，它能否自主完善其解释以缩小规范差距？我们提出了Policy Bank，这是一种记忆机制，可以维护结构化的工具级政策见解，并迭代地完善它们--与现有的记忆机制不同，将政策视为不可变的基本真相，强化“顺从但错误”的行为。我们还通过扩展流行的工具调用基准来提供一个系统性测试平台，其中具有可控的政策差距，将对齐失败与执行失败隔离开来。虽然现有的记忆机制在政策缺口场景中取得了接近零的成功，但Policy Bank缩小了与人类先知的差距高达82%。

[阅读原文](https://arxiv.org/abs/2604.15505)

---

## 6. LLM推理是潜在的，而不是思想链

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wenshuo Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Position paper arguing that LLM reasoning is primarily latent-state trajectory formation, directly aligning with the latent CoT/reasoning research interest.

**摘要**: arXiv：2604.15726v1公告类型：新摘要：这份立场文件认为，大语言模型（LLM）推理应该作为潜在状态轨迹形成而不是作为忠实的表面思想链（CoT）进行研究。这一点很重要，因为关于忠实性、可解释性、推理基准和推理时间干预的主张都取决于该领域认为推理的主要对象是什么。我们问，一旦将三个经常混淆的因素分开并形式化三个相互竞争的假设，该对象应该是什么：H1，推理主要由潜伏状态轨迹介导; H2，推理主要由显式表面CoT介导;和H 0，最明显的推理收益可以更好地解释通用序列计算比任何特权代表对象。在这个框架下重新组织最近的经验、机械和调查工作，并添加计算机审计的工作样本，这些样本将表面痕迹、潜在干预措施和匹配的预算扩张分解，我们发现当前的证据最强烈地支持H1作为默认工作假设，而不是作为一个独立于任务的判断。因此，我们提出两项建议：该领域应将潜伏状态动力学视为LLM推理的默认研究对象，并且应使用明确区分表面痕迹、潜伏状态和序列计算的设计来评估推理。

[阅读原文](https://arxiv.org/abs/2604.15726)

---

## 7. 通过概率语言尝试的顺序KV缓存压缩：超越每载体香农限制

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Gregory Magarshak

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel sequential KV cache compression method using probabilistic language tries and predictive delta coding, directly targeting latent reasoning efficiency.

**摘要**: arXiv：2604.15356v1宣布类型：新摘要：最近关于KV缓存量化的工作（最终以TurboQuant为高潮）已经接近了Transformer关键字-值缓存的每载体压缩的Shannon熵限制。我们观察到，这个限制适用于一个比实际重要的问题严格弱的问题：将KV缓存压缩为序列。存储在KV缓存中的令牌不是任意的浮点数据--它们是来自模型训练所依据的确切形式语言的样本，并且该模型是通过构建该语言的近乎最优的预测器来实现的。我们引入了顺序KV压缩，这是一种利用这种结构的两层架构。第一层，概率前置数据删除，使用来自概率语言Tries（PLT）的trie度量d_T（s，s '）= -log_2 P_M（s '）来识别会话之间语义等效的共享前置。第二层（预测增量编码）仅存储模型自己对其预测的每个新KV载体的残余，从而实现H（KV_{i+1}）的每令牌的熵界限|KV_{<=i}）<= H（token_{i+1}| token_{<=i}）。我们证明，在典型的语言模型困惑度下（对于流利的英语文本来说大约为10-20），这个界限平均为每个符号位置3.3-4.3位，而TurboQuant的每个载体分量3位（典型的注意力头具有64-128个组件）。在香农极限下，TurboQuant的理论压缩比约为914，000 x。即使在比最低密度高1000倍（故意悲观的最坏情况下的费用，比实际源代码器典型的2- 5倍高出两个数量级），该比率仍然大约是TurboQuant的914倍，随着上下文长度的增长，压缩率会提高而不是下降。这两个层是垂直的，并与包括TurboQuant在内的现有每载体量化方法组成。

[阅读原文](https://arxiv.org/abs/2604.15356)

---

## 8. 发现和证明：在Lean 4中进行硬模式自动定理证明的开源抽象框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chengwu Liu, Yichun Yin, Ye Yuan, Jiaxuan Xie, Botao Li, Siqi Li, Jianhao Shen, Yan Xu, Lifeng Shang, Ming Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an agentic framework (DAP) that uses LLM reasoning with explicit self-reflection to discover answers for automated theorem proving, aligning with self-improving agent criteria.

**摘要**: arXiv：2604.15839v1宣布类型：新摘要：大多数ATP基准将最终答案嵌入到正式声明中--我们称之为“简单模式”的惯例--这种设计相对于人类竞争对手面临的任务简化了任务，并可能导致对模型能力的乐观估计。我们将更严格、更现实的设置称为“硬模式”：系统必须在构建正式证明之前独立发现答案。为了实现硬模式研究，我们做出了两项贡献。首先，我们发布了MiniF 2F-Hard和FIMO-Hard，这是两个广泛使用的ATP基准测试的专家重新注释的Hard模式变体。其次，我们引入了Discover And Prove（DAB），这是一个代理框架，使用LLM自然语言推理和显式自我反思来发现答案，然后将硬模式陈述重写为现有ATP证明者的简单模式陈述。DPA设定了最新水平：在CombiBench上，它提出了7个已解决的问题（之前的SOTA，Pass@16）至10;在PutnamBench上，它是第一个以Hard Mode正式证明36个定理的系统，同时揭示了最先进的LLM在相同问题上的回答准确率超过80%，而正式证明者的回答准确率低于10%，暴露了硬模式基准唯一适合衡量的巨大差距。

[阅读原文](https://arxiv.org/abs/2604.15839)

---

## 9. 奖励加权无分类指导作为自回归模型中的政策改进

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Alexander Peysakhovich, William Berman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Reward Weighted Classifier-Free Guidance (RCFG) as a policy improvement operator for autoregressive models, enabling test-time reward optimization without retraining.

**摘要**: arXiv：2604.15577v1宣布类型：新摘要：考虑产生输出x的自回归模型（例如，问题的答案、分子），其中每一个都可以通过属性载体y来概括（例如，有益与无害，或生物利用度与亲脂性）。任意奖励函数r（y）编码这些属性之间的权衡。通常，倾斜模型的抽样分布以增加此奖励是在训练时通过强化学习完成的。然而，如果奖励功能发生变化，重新调整需要重新训练。在本文中，我们表明，奖励加权无分类器指导（RCGM）可以在这种环境下充当政策改进操作员，通过Q函数逼近抽样分布的倾斜。我们将RCGM应用于分子生成，证明它可以在测试时优化新型奖励功能。最后，我们表明，使用RCGM作为老师并融入基本政策作为热开始，可以显着加快标准RL的融合。

[阅读原文](https://arxiv.org/abs/2604.15577)

---

## 10. 世界泄露未来：未来预测代理的进化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chuyang Wei (University of Science and Technology of China, Zhongguancun Academy, Beijing, China), Maohang Gao (University of Science and Technology of China, Zhongguancun Academy, Beijing, China), Zhixin Han (Zhongguancun Academy, Beijing, China), Kefei Chen (Zhongguancun Academy, Beijing, China, Tsinghua University), Yu Zhuang (Zhongguancun Academy, Beijing, China), Haoxiang Guan (University of Science and Technology of China, Zhongguancun Academy, Beijing, China), Yanzhi Zhang (Zhongguancun Academy, Beijing, China), Yilin Cheng (Zhongguancun Academy, Beijing, China), Jiyan He (Zhongguancun Academy, Beijing, China), Huanhuan Chen (University of Science and Technology of China), Jian Li (Tsinghua University), Yu Shi (Zhongguancun Academy, Beijing, China), Yitong Duan (Zhongguancun Academy, Beijing, China), Shuxin Zheng (Zhongguancun Academy, Beijing, China)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving agent system (Milkyway) that improves future predictions via internal feedback and a persistent, updatable harness.

**摘要**: arXiv：2604.15719v1宣布类型：新摘要：在得知相关结果之前，必须做出许多重要决定。此类问题通常被定义为\{未来预测}，其中LLM代理必须仅使用预测时可用的公共信息对未解决的问题做出预测。这种设置很困难，因为公开证据会不断发展，而有用的监督只有在问题解决后才会到来，因此大多数现有的方法仍然主要从最终结果中改进。然而，最终结果过于粗略，无法指导早期的因素跟踪、证据收集和解释或不确定性处理。当同一个未解决的问题随着时间的推移被重新审视时，早期和晚期预测之间的时间对比可以暴露早期预测过程中的遗漏;我们称之为信号\emdash内部反馈。我们介绍了一个自我进化的代理系统，它保持基本模型不变，而是更新一个持久的未来预测工具，用于因素跟踪、证据收集和解释以及不确定性处理。在对同一个未解决的问题进行重复预测时，\n {Milkyway}会提取内部反馈，并将可重复使用的指导写回线束中，这样以后对该问题的预测就可以在结果已知之前得到改进。问题解决后，在更新的线束被带入后续问题之前，最终结果将提供\n {回顾检查}。在FutureX和FutureWorld上，Milkyway获得了比较方法中最好的总分，将FutureX从44.07提高到60.90，将FutureWorld从62.22提高到77.96。

[阅读原文](https://arxiv.org/abs/2604.15719)

---

## 11. 减少你的损失！学习尽早修剪路径以实现高效并行推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiaxi Bi, Tongxu Luo, Wenyu Du, Zhengyang Tang, Benyou Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes STOP, a learnable internal method for early path pruning in parallel reasoning, directly addressing efficiency in latent reasoning architectures.

**摘要**: arXiv：2604.16029v1公告类型：新摘要：并行推理增强了大型推理模型（LRM），但由于早期错误导致的无效路径而导致了高昂的成本。为了缓解这一问题，在前缀级的路径修剪是必不可少的，但现有的研究仍然支离破碎，没有一个标准化的框架。在这项工作中，我们提出了第一个系统性的路径修剪分类，根据其信号源（内部与外部）和可学习性（可学习与不可学习）对方法进行分类。这种分类揭示了可学习的内部方法未经开发的潜力，激发了我们提出STOP（Super TOken for Pruning）的动机。对1.5B至20 B参数范围内的LRM进行广泛评估表明，与现有基线相比，STOP实现了卓越的有效性和效率。此外，我们还严格验证了STOP在不同计算预算下的可扩展性-例如，在固定计算预算下，将AIM 25上的GPT-OSS-20 B准确性从84%提高到近90%。最后，我们将我们的研究结果提炼成正式的经验指南，以促进最佳的现实世界部署。代码、数据和模型可访问https://bijiaxihh.github.io/STOP

[阅读原文](https://arxiv.org/abs/2604.16029)

---

## 12. 走向稳健的内生推理：统一非平稳调整中的漂移适应

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xiaoyu Yang, En Yu, Wei Duan, Jie Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Counterfactual Preference Optimization++ (CPO++), a comprehensive RL fine-tuning framework to adapt to endogenous reasoning drift in MLLMs, directly targeting reward design for robust alignment.

**摘要**: arXiv：2604.15705v1宣布类型：新摘要：强化微调（RFT）已成为将多模式大型语言模型（MLLM）与复杂的人类价值观和特定领域要求保持一致的重要范式。尽管如此，目前的研究主要集中在减轻以数据为中心的因素引起的外生分布变化上，内生推理中固有的非平稳性在很大程度上仍未被探索。在这项工作中，MLLM中揭示了一个关键的弱点：它们在思维和感知角度上都高度容易受到内生推理漂移的影响。它表现为自回归生成过程中自发出现的不可预测的分布变化，独立于外部环境扰动。为了适应它，我们首先从理论上将MLLM RFT内的内生推理漂移定义为多模式概念漂移。在此背景下，本文提出了反事实偏好优化++（CPO++），这是一个适应多模式概念漂移的全面且自治的框架。它将反事实推理与领域知识集成，以在思维和感知中执行受控扰动，采用偏好优化来解开虚假相关性。对两个高度动态和安全关键领域进行了广泛的实证评估：医疗诊断和自动驾驶。他们证明，所提出的框架在推理一致性、决策精度和针对极端干扰的固有鲁棒性方面实现了卓越的性能。该方法还展现出出色的零镜头跨域概括，为安全关键应用中可靠的多模式推理提供了原则性基础。

[阅读原文](https://arxiv.org/abs/2604.15705)

---

## 13. 培训后产出多样性在哪里崩溃？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Constantinos Karouzos, Xingwei Tan, Nikolaos Aletras

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly analyzes output diversity collapse in post-training LLMs, tracing effects of SFT, DPO, and CoT distillation on model weights and reasoning.

**摘要**: arXiv：2604.16027v1宣布类型：新摘要：后训练语言模型产生的输出比基本模型变化较少。这种输出多样性崩溃破坏了依赖不同样本的推理时缩放方法，并有可能导致模型输出在创造性和充满价值的任务上的风险。先前的工作属性崩溃到特定的训练后方法，而没有将训练数据合成的角色与方法分开，或者将生成格式与模型权重分开。我们通过Olmo 3、Think（思想链蒸馏）、Direct（广泛的多源数据）和RL零这三个并行的训练后谱系来跟踪输出多样性，涵盖15个任务和4个文本多样性指标。我们发现崩溃的位置与数据组成相互变化：Think谱系在监督微调中失去了大部分语义多样性，并且DPO在Direct中的影响比Think中的影响更大。在Think模型中抑制推理时的思想链推理会降低硬任务的准确性，但答案级别的多样性保持不变，这表明崩溃是通过训练数据嵌入模型权重中的，而不是由生成格式强加的。将六个可验证任务的多样性损失分解为质量控制组件（删除不正确的输出）和剩余组件（正确输出之间的真正缩小）揭示了这种分裂是依赖于任务的，并且Think模型比Direcht保留了更多的正确答案多样性，尽管总体上崩溃了更多。我们的结果表明，多样性崩溃是在训练期间通过数据合成确定的，并且无法仅在推理时解决。

[阅读原文](https://arxiv.org/abs/2604.16027)

---

## 14. CiPO：通过迭代偏好优化进行大型推理模型的反事实反学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junyi Li, Yongqiang Chen, Ningning Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CiPO, an iterative preference optimization framework for unlearning in Large Reasoning Models by generating counterfactual reasoning traces, directly targeting the reasoning process.

**摘要**: arXiv：2604.15847v1宣布类型：新摘要：近年来，机器去学习越来越受到关注，它是一种有前途的技术，可以从在大规模人类数据上训练的大型语言模型中选择性地删除不需要的隐私或受版权保护的信息。然而，大型推理模型（LRM）的出现强调长思想链（CoT）推理来解决复杂问题，给取消学习带来了困境：现有方法要么难以从CoT痕迹中完全消除不需要的知识，要么由于干扰推理过程而降低推理性能。为此，我们通过迭代偏好优化（CiPO）引入了反事实去学习，这是一个新颖的框架，将去学习重新定义为LRM中CoT推理的有针对性干预。更具体地，给定所需的取消学习目标答案，CiPO指示LRM生成逻辑上有效的反事实推理轨迹以进行偏好调整。当LRM调整到反事实痕迹时，CiPO迭代更新偏好学习数据，以增加与原始模型的差异。这个迭代循环确保了理想的取消学习和顺利优化，有效地缓解了困境。具有挑战性的基准测试的实验表明，CiPO擅长取消学习，从中间CoT步骤和最终答案中完全删除知识，同时保留LRM的推理能力。

[阅读原文](https://arxiv.org/abs/2604.15847)

---

## 15. AtManRL：通过区分注意力显着性实现忠实推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Max Henning H\"oth, Kristian Kersting, Bj\"orn Deiseroth, Letitia Parcalabescu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes AtManRL, an RL method using differentiable attention saliency to train LLMs to generate more faithful and influential reasoning traces.

**摘要**: arXiv：2604.16158v1公告类型：新摘要：大型语言模型（LLM）越来越依赖思想链（CoT）推理来解决复杂任务。然而，确保推理轨迹既有助于又忠实地反映模型最终答案的基本过程，而不仅仅是伴随它，仍然具有挑战性。我们引入AtManRL，这是一种利用可区分注意力操纵通过强化学习学习更忠实的推理的方法。通过训练添加性注意力面具，该面具识别CoT中对产生正确答案至关重要的标记，我们获得了显着奖励信号，该信号鼓励模型生成真正影响其最终预测的推理痕迹。我们将这种显着性奖励与GRPO框架内基于结果的奖励集成在一起，以共同优化正确性和可解释性。使用Llama-3.2- 3B-Direct在GSM 8 K和MMLU上进行的实验表明，我们的方法可以识别有影响力的推理标记，并能够训练更透明的推理模型。

[阅读原文](https://arxiv.org/abs/2604.16158)

---

## 16. 人工智能主体蒸馏中不安全行为的潜意识转移

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jacob Dang, Brian Y. Xie, Omar G. Younis

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Demonstrates subliminal transfer of unsafe behavioral biases through model distillation of agent trajectories, directly relevant to RL/alignment for LLM agents.

**摘要**: arXiv：2604.15559v1宣布类型：新摘要：最近关于潜意识学习的工作表明，语言模型可以通过与这些特征语义无关的数据传输语义特征。然而，目前尚不清楚行为特征是否可以在代理系统中转移，其中政策是从轨迹而不是静态文本中学习的。在这项工作中，我们提供了第一个经验证据，表明不安全的代理行为可以通过模型提炼在两个互补的实验环境中潜意识地转移。在我们的主要环境中，我们构建了一个表现出强烈的删除偏见的教师代理，倾向于通过API风格的工具界面执行破坏性的文件系统操作，并仅使用表面上安全的任务的轨迹将其提取到学生中，所有显式删除关键字都经过严格过滤。在我们的次要设置中，我们在本地Bash环境中复制威胁模型，用shell命令替换API工具调用，并将偏差操作为优先选择，优先发布chmodd作为第一个与权限相关的命令，而不是语义等效的替代方案（例如chown或setfacl）。尽管在这两种环境中都有充分的关键词卫生，但学生们继承了可衡量的行为偏见。在API设置中，学生的删除率在均相蒸馏下达到100%（相对于5%的基线）;在Bash设置中，学生的chmod优先率达到30%-55%（相对于0%-10%的基线），在大到小蒸馏中观察到最强的转移。我们的研究结果表明，明确的数据卫生是一个不够的防御，和行为偏见的编码隐含在轨迹动态，无论工具接口。

[阅读原文](https://arxiv.org/abs/2604.15559)

---

## 17. 基于蒙特卡罗树搜索的智能体技能二层优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chenyi Huang, Haoting Zhang, Jingxu Xu, Zeyu Zheng, Yunduan Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a bilevel optimization framework using MCTS and LLMs to improve agent skills, directly aligning with self-improving agent frameworks.

**摘要**: arXiv：2604.15709v1宣布类型：新摘要：Agent \textttt {skills}是指令、工具和支持资源的结构化集合，可帮助大型语言模型（LLM）代理执行特定类别的任务。经验证据表明，\textttt {skills}的设计可以极大地影响代理任务绩效，但系统性地优化\textttt {skills}仍然具有挑战性。由于\textttt {skill}以结构化的方式包括指令、工具和支持资源，因此优化它需要联合确定这些组件的结构以及每个组件包含的内容。这产生了一个复杂的决策空间，结构和组件之间具有很强的相互依赖性。因此，我们将这两个耦合的决策表示为\textttt {skill}结构和组件内容，并将\textttt {skill}优化公式化为二层优化问题。我们提出了一个双层优化框架，其中外循环使用蒙特卡罗树搜索来确定\textttt {skill}结构，而内循环则细化外循环选择的结构内的组件内容。在这两个循环中，我们都使用LLM来协助优化过程。我们在开源Operations Research Question Ensemering数据集上评估了所提出的框架，实验结果表明，双层优化框架通过优化的\textttt {skill}提高了代理的性能。

[阅读原文](https://arxiv.org/abs/2604.15709)

---

## 18. 开放式事件预测的分散假设生成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: He Chang, Zhulin Tao, Lifang Yang, Xianglin Huang, Yunshan Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning framework (SCATTER) for generating diverse and inclusive future event hypotheses, directly matching RL for LLMs via novel reward design.

**摘要**: arXiv：2604.15788v1宣布类型：新摘要：尽管开放式事件预测对于风险管理很重要，但目前基于LLM的方法主要只针对最可能的结果，忽视了现实世界事件固有的不确定性。为了弥合这一差距，我们通过引入假设生成的代理任务，将开放式事件预测从精确预测推进到分散预测。该范式旨在生成一套包容性且多样化的假设，广泛涵盖看似合理的未来事件的空间。为此，我们提出了SCATTER，这是一个强化学习框架，可以共同优化假设的包容性和多样性。具体来说，我们设计了一种新颖的混合奖励，它由三个部分组成：1）有效性奖励，衡量与观察到的事件的语义一致性，2）组内多样性奖励，以鼓励采样响应内的变化，以及3）组间多样性奖励，以促进不同模式的探索。通过将有效性门控分数集成到总体目标中，我们将对广泛多元化结果的探索限制在上下文合理的未来，防止模式崩溃问题。对两个现实世界基准数据集进行实验，即OpenForecast和OpenEP证明SCATTER的表现显着优于强基线。我们的代码可以在www.example.com上找到。

[阅读原文](https://arxiv.org/abs/2604.15788)

---

## 19. GroupDPO：内存高效的分组直接偏好优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Jixuan Leng, Si Si, Hsiang-Fu Yu, Vinod Raman, Inderjit S. Dhillon

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a memory-efficient group-wise preference optimization algorithm for LLM alignment, directly relevant to scalable RL/feedback mechanisms.

**摘要**: arXiv：2604.15602v1宣布类型：新摘要：偏好优化被广泛用于将大型语言模型（LLM）与偏好反馈保持一致。然而，大多数现有的方法每次提示都会训练一个正负对，从而放弃了通常包含多个候选响应的偏好数据集中可用的额外监督。受这一限制的激励，最近的工作探索了分组偏好优化，该优化联合对比同一提示的多个响应，但由于分组耦合目标的内存负担，其经验行为和可扩展性仍然未充分研究。在这项工作中，我们引入了一种内存高效的分组偏好优化算法，该算法在反向传播期间保留梯度，同时将样本脱钩，从而大幅减少峰值内存使用，从而实现了更大组规模的可扩展训练。在离线和在线对齐设置中，我们表明利用多个响应始终优于单对训练。此外，在积极反应中纳入负对似然（NLL）项对于绩效提高和训练稳定性至关重要。

[阅读原文](https://arxiv.org/abs/2604.15602)

---

## 20. 评估小分子药物设计大语言模型能力的进展

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Shriram Chennakesavalu, Kirill Shmilovich, Hayley Weir, Colin Grambow, John Bradshaw, Patricia Suriana, Chen Cheng, Kangway Chuang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces RL-based post-training for LLMs on chemical tasks, showing substantial improvement and a practical route to close capability gaps.

**摘要**: arXiv：2604.16279v1宣布类型：新摘要：大型语言模型（LLM）具有加速小分子药物设计的潜力，因为它们能够推理来自不同来源和格式的信息。然而，由于缺乏反映现实世界场景的基准，它们的实际用途仍然不清楚。在这项工作中，我们介绍了一系列基于化学的任务，涵盖分子性质预测、分子表示转换和分子设计。重要的是，我们将这些任务制定为强化学习（RL）环境，从而实现统一的评估和后培训方法。在三个模型家族中，我们发现前沿模型在化学任务上越来越熟练，但仍有很大的改进空间，特别是在数据较少的实验环境中。至关重要的是，我们表明基于RL的后训练可以大幅提高性能。尽管基础模型明显较弱，但在我们的环境上进行后训练的较小模型仍能与最先进的前沿模型竞争。这为在药物发现中使用LLM提供了一条实用的途径;通过将精心设计的评估任务与有针对性的后培训相结合，我们可以阐明并缩小关键的能力差距。

[阅读原文](https://arxiv.org/abs/2604.16279)

---

## 21. 查找、修复、原因：用于视频推理的上下文修复

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Haojian Huang, Chuanyu Qin, Yinchuan Li, Yingcong Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a teacher-student RL pipeline (GRPO) with a Robust Improvement Reward for video reasoning, directly aligning with RL for LLMs via reward design and on-policy optimization.

**摘要**: arXiv：2604.16243v1宣布类型：新摘要：强化学习先进了大型多模式模型中的视频推理，但占主导地位的管道要么依赖于政策上的自我探索（在模型的知识边界趋于稳定），要么依赖于混合政策并需要仔细规则化的混合回放。动态上下文方法放大了有针对性的证据，但通常需要精心策划的预训练和两阶段调整，并且它们的上下文仍然受到小模型能力的限制。相比之下，较大的模型擅长指令遵循和多模式理解，可以为较小的模型提供更丰富的上下文，并通过简单的工具快速放大目标区域。在此能力的基础上，我们引入了观察级干预：一位冻结的、工具集成的教师识别缺失的时空依赖性并提供最少的证据补丁（例如，时间戳、地区等）来自原始视频，而问题保持不变。学生使用添加的上下文再次回答，并使用集成到组相对政策优化（GRPO）中的选择推出计划进行培训更新。我们进一步提出了稳健改进奖励（RIR），将优化与两个目标保持一致：通过正确答案来确定结果有效性，以及通过反映引用证据的原理来确定依赖性。优势在批次中进行分组标准化，保留政策探索，同时将其引导到具有因果意义的方向，并对训练栈进行最小的更改。各种相关基准的实验显示出一致的准确性收益和较强的概括性。网页和源代码可在https://github.com/JethroJames/FFR.git上获取。

[阅读原文](https://arxiv.org/abs/2604.16243)

---

## 22. 将谜题放在重要的地方：强化学习的问题增强框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yangyi Fang, Jiaye Lin, Xiaoliang Fu, Cong Qin, Haolin Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hint injection framework for RL-based LLM reasoning that strategically identifies and provides critical reasoning steps to improve training.

**摘要**: arXiv：2604.15830v1宣布类型：新摘要：强化学习已成为增强大型语言模型推理的有力方法，但面临着一个根本性的困境：对简单问题进行训练可能会导致过度匹配和传递@k降级，而对困难问题进行训练通常会导致稀疏回报。最近的问题增强方法通过预先添加部分解决方案作为提示来解决这个问题。然而，统一提示提供可能会引入冗余信息，同时错过关键推理瓶颈，过多的提示会降低推理多样性，导致传递@k降级。我们提出了\textBF{PieceHint}，这是一个提示注入框架，可以在训练期间战略性地识别并提供关键推理步骤。通过评分不同推理步骤的重要性、根据问题难度选择性地分配提示以及逐步撤回支架，PieceHint使模型能够从引导学习过渡到独立推理。对六个数学推理基准的实验表明，我们的1.5B模型实现了与32 B基线相当的平均性能，同时在所有$k$值中保留了Pass@k多样性。

[阅读原文](https://arxiv.org/abs/2604.15830)

---

