# 💡 今日研究速览 (Daily Summary)

# LLC和统计政策优化的RL
当今研究的一个重要重点是完善和扩展LLM的强化学习，特别是对于代理和推理任务。一个关键主题是解决传统RL管道的不稳定性和效率低下问题。**T-STAR**和**Android Coach**等新型框架引入了分层和外科手术式优化方法，利用认知树或单状态多动作等结构来提高学分分配和培训效率。与此同时，**RAgen-2**和**难度缩放极限**等论文提供了关键诊断，分析推理崩溃等故障模式以及GRPO等方法中硬样本的递减回报。这项集体工作超越了简单的政策更新，转向了更结构化、更高效且可诊断的RL流程，这些流程对于开发稳健的多步骤代理至关重要。

# 潜在推理和模型架构
对推理内部机制的研究看到了理解极限和提出新架构的双重关注。基础研究，如**深度天花板**和**叠加的错觉？**直接探测现有模型中潜在的多步规划和叠加的边界，为该领域建立原则性基线。与此同时，新的架构正在被提出来超越这些限制。神经计算机**引入了学习运行时状态的范式转换概念，有效地将计算移动到动态模型状态，而**多目标进化合并** 提供了一种基于压缩的方法，使推理跟踪更有效。这一方向凸显了从仅仅使用潜在推理到从根本上重新设计其实施和理解方式的成熟转变。

# 多模式和排队代理对齐
多模式大型语言模型（MLLM）与具体化的、面向任务的动作的结合是一个不断发展的前沿。核心挑战是弥合“推理与行动差距”，即语义理解无法转化为有效的政策。**Walk the Talk**通过多模式统计政策优化（MAPO）直接解决了这个问题，MAPO是一种新型RL方法，将视觉语义对齐与任务奖励结合起来。闭合感知、推理和行动之间循环的主题进一步得到了模拟环境中的工作的支持，例如**TwinLoop**，它使用数字双胞胎在环境变化后加速多智能体RL政策改进。这些进步对于在复杂的现实世界场景中部署有能力的代理至关重要。

# 生成模型RL和微调
强化学习技术正在针对标准语言模型之外的多样化生成模型家族进行专业化和优化。对于扩散模型，**FP 4 Explore、BF 16 Train** 提出了一个高效的两阶段RL框架，该框架使用积极的量化来进行可扩展的部署。同样，对于混合自回归-扩散图像模型，**MAR-GRPO**引入了具有新颖梯度降噪功能的稳定RL变体。该领域还看到了统一的理论框架，正如**离散流匹配政策优化** 所证明的那样，它提供了适用于离散流匹配模型的新政策梯度公式。这种专业化表明RL作为协调和改进各种最先进生成式架构的核心工具的成熟。

# 自我改进和持续学习系统
一个复杂的研究路线探讨了如何设计系统以进行持续的适应和自我完善。这超越了单一的训练运行，转向了持续进化的框架。**自学习诊断代理**通过双记忆模块和强化训练来实现推理和记忆的联合优化，体现了这一点。迭代、相互增强的概念也是**话语一致性和响应引导的上下文重写**的核心，其中重写器和响应器模型在循环中相互改进。此外，** 自我修改代理实际需要多少LLM？**采取元视角，外部化代理状态来批判性地分析LLM本身的边缘作用，推动更高效、更透明的自我改进架构。

# SFT、泛化和奖励建模
研究继续完善模型对齐的基础阶段，重点是理解泛化和改善奖励信号。SFT**提供了一个比较SFT和RL的关键条件分析，根据优化、数据和模型能力，直接告知每种方法何时以及为什么成功。在奖励建模方面，**Personalized RewardBench** 通过引入个性化人类偏好的基准来解决关键限制，展示其与下游RL性能的相关性。这项工作确保了驱动WLHF和相关方法的偏好数据更加细致、可扩展和可评估，为高级优化奠定了更可靠的基础。

---

## 1. SHADE：通过LLM推理潜力估计的阶段感知分层优势

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhengyang Ai, Zikang Shan, Xiaodong Ai, Jingxian Tang, Hangkai Hu, Pinyan Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SHAPE, a hierarchical credit assignment method using stage-aware advantage and entropy-driven redistribution for RL-based process supervision of LLM reasoning.

**摘要**: arXiv：2604.06636v1宣布类型：新摘要：流程监督已成为增强LLM推理的一种有希望的方法，但现有方法无法区分有意义的进展与纯粹的冗长，导致推理能力有限和未解决的代币效率低下。为了解决这个问题，我们提出了通过潜力估计的阶段感知分层优势（SHADE），这是一个将推理形式化为通过经验可解性状态空间的轨迹的框架。SHADE引入了分层信用分配机制：在细分层面，它采用阶段感知优势功能，优先考虑低潜力状态的高效突破;在代币层面，它利用了信息量驱动的再分配来尖锐执行信号。跨三个基本模型和五个基准进行的数学推理的广泛实验表明，SHADE实现了3%的平均准确性提高，代币消耗减少了30%。

[阅读原文](https://arxiv.org/abs/2604.06636)

---

## 2. 链条中的理性，树木中的学习：多回合代理政策优化的自我纠正和嫁接

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu Li, Sizhe Tang, Tian Lan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (T-STAR) for LLM agents that recovers latent reward structure via a Cognitive Tree and performs surgical policy optimization at critical reasoning steps.

**摘要**: arXiv：2604.07165v1宣布类型：新摘要：大型语言模型代理的强化学习通常会受到多步推理任务中的稀疏奖励的阻碍。群相对政策优化等现有方法将采样轨迹视为独立链，为每个链中的所有步骤分配统一的信用度，并忽略可能影响推理结果的关键步骤的存在。在本文中，我们提出了T-STAR（树结构自学代理纠正），这是一个跨越看似独立的轨迹恢复潜在相关奖励结构的框架。具体来说，我们通过识别和合并功能相似的步骤/节点将轨迹整合到统一的认知树中。它实现了内省估值机制，通过树反向传播个体级奖励，以获得阶梯级方差降低相对优势的新概念。使用认知树，我们还开发了上下文思维移植，通过在关键分歧点/步骤对比成功和失败的分支来综合纠正推理。然后，我们提出的手术政策优化利用集中在这些关键点/步骤的丰富政策梯度信息，通过Bradley-Terry类型的手术损失。针对具体化、交互式、推理和规划基准的广泛实验表明，T-STAR在强基线上实现了一致的改进，在需要扩展推理链的任务上，其收益最为明显。

[阅读原文](https://arxiv.org/abs/2604.07165)

---

## 3. RAgen-2：超级RL中的推理崩溃

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zihan Wang, Chi Gui, Xing Jin, Qineng Wang, Licheng Liu, Kangrui Wang, Shiqi Chen, Linjie Li, Zhengyuan Yang, Pingyue Zhang, Yiping Lu, Jiajun Wu, Li Fei-Fei, Lijuan Wang, Yejin Choi, Manling Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a diagnosis and mitigation method for reasoning collapse in RL-trained LLM agents, introducing mutual information as a key metric and SNR-aware filtering.

**摘要**: arXiv：2604.06268v1宣布类型：新摘要：多回合LLM代理的RL训练本质上是不稳定的，推理质量直接决定任务性能。熵被广泛用于跟踪推理稳定性。然而，信息量仅测量同一输入内的多样性，而无法判断推理是否实际上响应不同的输入。在RAgen-2中，我们发现即使有稳定的熵，模型也可以依赖于固定模板，这些模板看起来多样化但与输入不可知有关。我们称这种模板崩溃，这是一种对信息量和所有现有指标来说不可见的失败模式。为了诊断这种故障，我们将推理质量分解为输入内多样性（Entropy）和交叉输入互换性（互信息，MI），并引入一系列互信息代理用于在线诊断。在不同的任务中，互信息与最终性能的相关性比信息量强得多，使其成为推理质量的更可靠的代理。我们进一步用信噪比（SNR）机制解释模板崩溃。低回报方差会削弱任务梯度，让正规化项占主导地位并消除交叉输入推理差异。为了解决这个问题，我们提出SNR-Aware过滤，使用奖励方差作为轻量级代理，在每次迭代中选择高信号提示。在规划、数学推理、网络导航和代码执行中，该方法持续改善了输入依赖性和任务性能。

[阅读原文](https://arxiv.org/abs/2604.06268)

---

## 4. 深度上限：大型语言模型在发现潜在规划方面的局限性

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yi Xu, Philipp Jettkant, Laura Ruis

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies the limits of latent multi-step planning in LLMs, a core topic for latent CoT/reasoning research.

**摘要**: arXiv：2604.06427v1宣布类型：新摘要：思想链（CoT）监控的可行性取决于模型无法在其潜在表示中有效推理。然而，人们对LLM中这种潜在推理的局限性知之甚少。我们通过研究模型是否可以在没有中间步骤监督的情况下发现多步骤规划策略并在一次向前传递内潜伏执行它们来测试这些限制。使用精确控制所需潜在规划步骤数量的图寻路任务，我们发现了一个大规模扩展无法解决的惊人限制：从头开始训练的微型变形金刚发现需要多达三个潜在步骤的策略，微调的GPT-4 o和Qwen 3 - 32 B达到五个，GPT-5.4在几次提示下达到七个。尽管训练期间可以学习的最大潜在规划深度模型是五个，但所发现的策略在测试时概括了多达八个潜在步骤。这揭示了仅在最终答案监督下发现潜在策略的能力与一旦发现就执行潜在策略的能力之间存在脱节。如果类似的限制更广泛地存在，那么需要多个协调的潜在规划步骤的策略可能需要明确教授或外部化，从而为CoT监控提供可信度。

[阅读原文](https://arxiv.org/abs/2604.06427)

---

## 5. Android Coach：通过单状态多动作提高在线统计训练效率

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guo Gan, Yuxuan Ding, Cong Chen, Yuwei Ren, Yin Huang, Hong Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel online RL framework (Android Coach) for agent training using a Single State Multiple Actions paradigm with a learned critic, directly improving agent capabilities through a scalable RL pipeline.

**摘要**: arXiv：2604.07277v1宣布类型：新摘要：在线强化学习（RL）是增强Android代理能力的有效方法。然而，由于模拟器的高延迟和现有RL算法的样本效率低下，引导代理通过在线交互进行学习的成本极其昂贵。我们发现了当前方法中的一个根本局限性：单状态单动作范式，该范式通过在线单向推出的一对一状态动作对更新策略，而无需充分探索每个昂贵的模拟器状态。在本文中，我们提出了Android Coach，这是一个新颖的框架，它将训练范式转变为单状态多个动作，允许代理为单个在线状态采样和利用多个动作。我们通过学习估计动作值的评论家来实现这一目标，而无需额外的模拟器负载。为了确保批评者成为可靠的教练，我们集成了流程奖励模型，并根据平均批评者输出引入了分组优势估计器。大量实验证明了Android Coach的有效性和效率：与UI-TARS-1.5- 7 B相比，它在AndroidLab和AndroidWorld上实现了7.5%和8.3%的成功率提高，并在匹配的成功率下实现了比单状态单动作方法PPO和GRPO高1.4倍的训练效率。

[阅读原文](https://arxiv.org/abs/2604.07277)

---

## 6. 叠加幻觉？语言模型中潜在思维的原则性分析

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Michael Rizvi-Martel, Guillaume Rabusseau, Marius Mosbach

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly investigates latent reasoning (Latent CoT) and superposition in language models, a core topic of latent CoT/reasoning research.

**摘要**: arXiv：2604.06374v1宣布类型：新摘要：通过连续思想链的潜在推理（潜在CoT）已成为离散CoT推理的一种有希望的替代方案。在连续空间中操作可以提高表达力，并被假设可以实现叠加：在单个表示中同时维护多个候选解决方案的能力。尽管存在理论上的争论，但目前尚不清楚语言模型在使用潜在CoT进行推理时是否真的利用了叠加。我们在三个机制中研究这个问题：一个无训练机制，将潜在思想构建为代币嵌入的凸组合;一个微调机制，其中基础模型适合产生潜在思想;以及一个从头开始机制，其中模型完全用潜在思想训练以解决给定任务。使用Logit Lens和实体级探测来分析内部表示，我们发现只有从头开始训练的模型才会表现出使用叠加的迹象。在无需训练和微调的机制中，我们发现叠加要么崩溃，要么根本不被使用，而模型反而发现捷径解决方案。我们认为，这是由于两个互补现象造成的：i）对自然语言数据的预训练会使模型偏向于在最后一层中承诺代币ii）容量对模型青睐的解决方案产生巨大影响。总的来说，我们的结果为连续思想链推理中何时以及为何出现叠加提供了统一的解释，并确定了叠加崩溃的条件。

[阅读原文](https://arxiv.org/abs/2604.06374)

---

## 7. 自学习诊断代理的推理和双记忆联合优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bingxuan Li, Simo Du, Yue Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-learning diagnostic agent with a dual-memory module and a reinforcement training framework for joint optimization of reasoning and memory, enabling continual adaptation.

**摘要**: arXiv：2604.07269v1宣布类型：新摘要：临床专业知识不仅通过获取医学知识来提高，还通过积累产生可重复使用的诊断模式的经验来提高。最近基于LLM的诊断试剂在决策支持的临床推理方面显示出有希望的进展。然而，大多数方法都独立处理病例，限制了经验的重复使用和持续适应。我们提出SEA，一种具有认知启发双记忆模块的自学习诊断试剂。我们设计了一个针对我们设计的代理量身定制的强化训练框架，用于联合优化推理和内存管理。我们在两种补充的环境中评估SEA。在MedCaseReasoning数据集的标准评估中，SEA的准确率达到了92.46%，比最强基线高出+19.6%，证明了联合优化推理和记忆的好处。在ER-Reason数据集的长期范围内，SEA获得了最好的最终准确性（0.7214）和最大的改进（+0.35 Acc@100），而基线方法显示出有限或不稳定的收益。专家评估进一步表明，从SEA中合并的规则显示出较强的临床正确性、有用性和信任度，表明双记忆模块中的推导规则可靠且具有实际意义。总体而言，SEA通过有效地将经验转化为可重复使用的知识，提高了诊断推理能力和持续学习。

[阅读原文](https://arxiv.org/abs/2604.07269)

---

## 8. 神经计算机

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Mingchen Zhuge, Changsheng Zhao, Haozhe Liu, Zijian Zhou, Shuming Liu, Wenyi Wang, Ernie Chang, Gael Le Lan, Junjie Fei, Wenxuan Zhang, Yasheng Sun, Zhipeng Cai, Zechun Liu, Yunyang Xiong, Yining Yang, Yuandong Tian, Yangyang Shi, Vikas Chandra, J\"urgen Schmidhuber

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Neural Computers, a new frontier for learned runtime states, which is a novel latent reasoning architecture that moves computation into a learned model state.

**摘要**: arXiv：2604.06425v1宣布类型：新摘要：我们提出了一个新的前沿：神经计算机（NC）--一种新兴的机器形式，将计算、存储器和I/O统一在学习的运行时状态中。与执行显式程序的传统计算机、在外部执行环境中作用的代理以及学习环境动态的世界模型不同，NC的目标是使模型本身成为正在运行的计算机。我们的长期目标是完全神经计算机（NC）：这种新兴机器形式的成熟、通用实现，具有稳定的执行、显式的重编程和持久的能力重复使用。作为第一步，我们研究是否可以仅从收集的I/O轨迹中学习早期NC基元，而无需插装程序状态。具体来说，我们将NC实例化为视频模型，可以根据CLI和图形用户设置中的指令、像素和用户操作（如果可用）推出屏幕框架。这些实现表明，学习的运行时可以获取早期的接口基元，尤其是I/O对齐和短期控制，而例行重用、受控更新和符号稳定性保持开放。我们围绕这些挑战概述了CNCs的路线图。如果克服这一问题，CNCs可以建立一种超越当今代理、世界模型和传统计算机的新计算范式。

[阅读原文](https://arxiv.org/abs/2604.06425)

---

## 9. FP 4探索、BF 16训练：通过高效推出缩放进行扩散强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yitong Li, Junsong Chen, Shuchen Xue, Pengcuo Zeren, Siyuan Fu, Dinghao Yang, Yangyang Tang, Junjie Bai, Ping Luo, Song Han, Enze Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel two-stage RL framework (Sol-RL) for diffusion model alignment, using FP4 quantization for efficient rollout scaling and BF16 for policy optimization.

**摘要**: arXiv：2604.06916v1宣布类型：新摘要：基于强化学习的后训练最近已成为将文本到图像扩散模型与人类偏好保持一致的一种有前途的范式。在最近的研究中，增加推出组规模会带来显着的性能改进，这表明进一步对齐的巨大空间。然而，大规模基础扩散模型的扩展（例如，FLOX.1 - 12 B）带来了沉重的计算负担。为了缓解这一瓶颈，我们探索将FP 4量化集成到扩散RL部署中。然而，我们发现天真的量化管道本质上会带来性能下降的风险。为了克服效率和训练完整性之间的困境，我们提出了Sol-RL（光速RL），这是一种新型的FP 4授权的两阶段强化学习框架。首先，我们利用高吞吐量NVFP 4部署来生成庞大的候选池并提取高度对比的子集。其次，我们以BF 16精度重新生成这些选定的样本，并专门针对它们优化策略。通过将候选探索与政策优化脱钩，Sol-RL将部署扩展的算法机制与NVFP 4的系统级吞吐量收益集成在一起。这种协同算法-硬件设计有效地加速了推出阶段，同时保留了高保真样本用于优化。我们的经验表明，我们的框架保持了BF 16精度流水线的训练完整性，同时充分利用了FP 4算法实现的吞吐量增益。在SANA、FLUX.1和SD3.5-L上进行的大量实验证实，我们的方法在多个指标上提供了卓越的对齐性能，同时将训练收敛速度加快了4.64倍，以一小部分成本释放了大规模部署扩展的能力。

[阅读原文](https://arxiv.org/abs/2604.06916)

---

## 10. 离散流匹配政策优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Maojiang Su, Po-Chung Hsieh, Weimin Wu, Mingcheng Lu, Jiunhau Chen, Jerry Yao-Chieh Hu, Han Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified RL fine-tuning framework (DoMinO) for Discrete Flow Matching models, directly addressing RL for LLMs with a new policy gradient formulation and regularization.

**摘要**: arXiv：2604.06491v1宣布类型：新摘要：我们引入了离散流匹配策略优化（DoMinO），这是一个在广泛的政策梯度方法下进行强化学习（RL）微调离散流匹配（DFM）模型的统一框架。我们的关键想法是将DFM采样过程视为多步马尔科夫决策过程。该观点提供了将微调回报最大化作为稳健的RL目标的简单而透明的重新表述。因此，它不仅保留了原始的DFM采样器，而且还避免了许多先前RL微调方法使用的有偏辅助估计器和似然代理。为了防止政策崩溃，我们还引入了新的总变异调节器，以保持微调后的分布接近预先训练的分布。从理论上讲，我们建立了DoMinO的离散化误差的上界和正规化器的易于处理的上界。通过实验，我们评估了DoMinO的调节DNA序列设计。与之前的最佳奖励驱动基线相比，DoMinO实现了更强的预测增强子活性和更好的序列自然性。正规化进一步改善了与自然序列分布的一致性，同时保留了强大的功能性能。这些结果使DoMinO成为可控离散序列生成的有用框架。

[阅读原文](https://arxiv.org/abs/2604.06491)

---

## 11. 第一个猜测很少是最终答案：学习搜索旅行推销员问题

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Andoni Irazusta Garmendia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a neural improvement framework for TSP using a two-stage RL pipeline (imitation learning + critic-free RL) to learn a policy for local search, directly aligning with RL for agent improvement.

**摘要**: arXiv：2604.06940v1公告类型：新摘要：旅行推销员问题（TSP）的大多数神经求解器都被训练成输出单个解决方案，尽管从业者很少停在那里：在测试时，他们通常会在采样或事后搜索上花费额外的计算。这就提出了一个自然的问题：搜索过程本身可以学习吗？神经改进方法通过学习将局部修改应用于候选解决方案的策略，从而在改进轨迹上积累收益。然而，对TPS的学习改进仍然相对不成熟，现有的方法仍然达不到稳健、可扩展的性能。我们认为，一个关键原因是设计不匹配：许多方法重复使用从单一解决方案方法继承的状态表示、架构选择和训练食谱，而不是围绕本地搜索的机制构建。这种不匹配激发了NICO-TBC（组合优化神经改进）：一个2-选项的DSP改进框架。NICO-TPS代表当前的巡回赛，其中$n$边缘令牌与邻居操作符对齐，直接对2-opp移动进行评分，无需巡回位置编码，并通过两阶段过程进行训练：模仿学习到短期最佳轨迹，然后在较长时间内进行无批评的基于群体的强化学习。在计算匹配的评估下，将改进作为搜索步骤和时钟时间的函数来衡量，NICO-TPS提供比之前的学习和启发式搜索基线更强、明显更高效的改进，更可靠地推广到更大的分布外实例，并且既可以作为经典本地搜索的竞争替代品，又可以作为建设性求解器的强大测试时细化模块。

[阅读原文](https://arxiv.org/abs/2604.06940)

---

## 12. 步骤流程中断时推理失败

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xiaoyu Xu, Yulan Pan, Xiaosong Yuan, Zhihong Shen, Minghao Su, Yuanhao Su, Xiaofeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes StepFlow, a test-time intervention that repairs information flow failures in large reasoning models to improve accuracy without retraining.

**摘要**: arXiv：2604.06695v1宣布类型：新摘要：生成长思想链的大型推理模型（LRM）现在在多步骤数学、科学和编码任务中表现良好。然而，他们的行为仍然不稳定且难以解释，并且现有的分析工具难以应对如此长的结构化推理痕迹。我们引入了Step-Saliency，它将注意力梯度分数集中到沿着问题-思考-总结轨迹的分步地图中。在多个模型中，Step-Spentiency揭示了两种反复出现的信息流失败：浅锁定（Shallow Lock-in），其中浅层过度关注当前步骤，几乎不使用早期的上下文;和深度衰退（Deep Decay），其中深层逐渐失去对思维部分的显着性，摘要越来越注重自身和最后几个步骤。受这些模式的激励，我们提出了StepFlow，这是一种受显着性启发的测试时干预措施，通过奇等桥调整通过分步显着性测量的浅层显着性模式，并通过分步动量注入在深层添加小的分步水平剩余。StepFlow无需重新培训即可提高多个LRM之间数学、科学和编码任务的准确性，这表明修复信息流可以恢复部分缺失的推理性能。

[阅读原文](https://arxiv.org/abs/2604.06695)

---

## 13. 用于移动边缘计算中任务卸载的多轮推理LLM

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ning Yang, Chuangxin Cheng, Haijun Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes COMLLM, a generative framework using Group Relative Policy Optimization (GRPO) for foresighted decision-making in MEC, directly applying RL for LLM policy improvement.

**摘要**: arXiv：2604.07148v1公告类型：新摘要：新兴的计算密集型应用对资源受限的移动设备提出了严格的延迟要求。移动边缘计算（MEC）通过任务卸载解决了这一挑战。然而，由于动态任务到达、时变通道以及服务器队列的时空耦合，设计有效的策略仍然很困难。传统的启发式方法缺乏适应性，而深度强化学习（DRL）的概括性和架构僵化性有限，当网络布局发生变化时需要重新训练。尽管大型语言模型（LLM）提供语义推理能力，但标准的监督微调（SFT）会产生短视的策略，这些策略贪婪地最小化即时延迟，而不考虑长期系统进化。为了解决这些限制，我们提出了COMLLM，这是一个生成式框架，可以在MEC系统中进行有预见性的决策。COMLLM将组相对策略优化（GRPO）与前瞻协作模拟（LACS）机制集成，该机制在联合建模服务器队列动态的同时执行多步蒙特卡洛部署。通过将这些推出纳入奖励设计中，该框架捕捉了当前决策对未来系统状态的长期影响。实验结果表明，COMLLM实现了接近最优的延迟和改进的负载平衡公平性。值得注意的是，它展现出零触发的拓扑可扩展性，允许在小规模网络上训练的模型在无需重新训练的情况下推广到更大的、不可见的拓扑，表现优于SFT、DRL和启发式基线。

[阅读原文](https://arxiv.org/abs/2604.07148)

---

## 14. TwinLoop：用于在线多智能体强化学习的环仿真数字双胞胎

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Nan Zhang, Zishuo Wang, Shuyu Huang, Georgios Diamantopoulos, Nikos Tziritas, Panagiotis Oikonomou, Georgios Theodoropoulos

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TwinLoop, a simulation-in-the-loop digital twin framework for online multi-agent reinforcement learning, enabling accelerated policy improvement after context shifts.

**摘要**: arXiv：2604.06610v1公告类型：新摘要：分散式在线学习使网络物理多智能体系统的运行时适应成为可能，但当运行条件发生变化时，学习到的策略通常需要大量的试错交互才能恢复性能。为了解决这个问题，我们提出了TwinLoop，这是一个用于在线多智能体强化学习的模拟在环数字孪生框架。当上下文发生变化时，数字孪生被触发以重建当前系统状态，根据最新的代理策略进行初始化，并在将更新的参数同步回物理系统中的代理之前通过模拟假设分析执行加速策略改进。我们在工作负载和基础设施条件不断变化的车辆边缘计算任务卸载场景中评估TwinLoop。结果表明，数字双胞胎可以提高轮班后适应效率，并减少对昂贵的在线试错的依赖。

[阅读原文](https://arxiv.org/abs/2604.06610)

---

## 15. 多党对话生成的话语连贯性和响应引导的语境重写

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhiyu Cao, Peifeng Li, Qiaoming Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dynamic self-evolution learning method where a rewriter and responder continuously enhance capabilities through mutual interaction in an iterative training loop.

**摘要**: arXiv：2604.06784v1宣布类型：新摘要：之前关于多方对话生成的研究主要利用对话固有的结构信息来直接告知生成过程。然而，对话中口语化表达和不完整话语的盛行往往会阻碍理解并削弱对话结构表现的忠实性，这在多党对话中尤其明显。在这项工作中，我们提出了一个新颖的框架DRCR（话语连贯性和响应引导的上下文重写），通过对话上下文重写来改善多方对话的生成。具体来说，DRCR采用两种补充的反馈信号：话语连贯性和响应质量，来构建用于上下文重写和响应生成的偏好数据。此外，我们提出了一种动态自进化学习方法，允许重写者和响应者通过迭代训练循环中的相互交互来不断增强他们的能力。对四个多方对话数据集进行的全面实验证实了DRCR的有效性。

[阅读原文](https://arxiv.org/abs/2604.06784)

---

## 16. 自我修改代理实际需要多少LLM？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Seongwoo Jeong, Seonil Son

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a declared reflective runtime protocol to externalize agent state and study the marginal role of LLM intervention in self-revising agents, directly aligning with self-improving agent frameworks.

**摘要**: arXiv：2604.07236v1宣布类型：新摘要：最近基于LLM的代理通常将世界建模、规划和反射置于单一语言模型循环中。这可以产生有能力的行为，但这使得一个基本的科学问题难以回答：代理人的能力的哪一部分实际上来自LLM，哪一部分来自其周围的显式结构？   我们研究这个问题，不是通过要求一个普遍的答案，而是通过使它在经验上易于处理。我们引入了一个声明的反射运行时协议，具体化代理状态，信心信号，守卫行动，并假设转换到可检查的运行时结构。我们在声明式运行时中实例化该协议，并在嘈杂的协作战舰[4]上使用四个渐进结构的代理在54场比赛（18个板$\times $3个种子）中对其进行评估。   由此产生的分解隔离了四个组成部分：后验信念跟踪，明确的世界模型规划，象征性的情节反射，稀疏LLM为基础的修订。在此分解中，显式世界模型规划比贪婪的后验基线（+24.1pp获胜率，+0.017 F1）有了显着的改善。符号反射作为一种真正的运行时机制运行--具有预测跟踪、置信度门控和受保护的修订操作--尽管其当前的修订收件箱总体上尚未达到净正值。在约4.3%的回合数处添加有条件的LLM修订只会产生较小且非单调的变化：F1平均水平略有上升（+0.005），而胜率下降（31 $\rightarrow 29（满分54））。   这些结果表明了方法论的贡献，而不是排行榜的主张：外部化反射将潜在的代理行为转变为可检查的运行时结构，从而允许直接研究LLM干预的边缘作用。

[阅读原文](https://arxiv.org/abs/2604.07236)

---

## 17. 重新思考推理SFT中的概括：优化、数据和模型能力的条件分析

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qihan Ren, Peng Wang, Ruikun Cai, Shuai Shao, Dadi Guo, Yuejin Xie, Yafu Li, Quanshi Zhang, Xia Hu, Jing Shao, Dongrui Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Revisits the generalization of reasoning SFT vs. RL, providing a conditional analysis of optimization, data, and model capability that directly informs RL for LLMs.

**摘要**: arXiv：2604.06628v1宣布类型：新摘要：LLM后培训中的一种流行说法认为，监督微调（SFT）是记忆的，而强化学习（RL）是概括的。我们重新审视了用长思想链（CoT）监督推理SFT的主张，发现跨域概括并非不存在，而是有条件的，由优化动态、训练数据和基本模型能力共同塑造。一些报告的失败是优化不足的产物：跨域性能首先下降，然后再通过扩展训练（一种浸入和恢复模式）进行恢复和改进，因此短期训练检查点可能会低估一般性。数据质量和结构都很重要：低质量的解决方案广泛损害了概括性，而经过验证的长CoT痕迹会产生一致的跨域收益。模型能力至关重要：更强大的模型将可转移的程序模式内化（例如，回溯）甚至是从玩具算术游戏中，而较弱的则模仿表面冗长。然而，这种概括是不对称的：推理得到改善，而安全性却下降，从推理SFT是否推广到在什么条件下以什么代价重新构建了问题。

[阅读原文](https://arxiv.org/abs/2604.06628)

---

## 18. 多目标进化合并实现高效推理模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mario Iacobelli, Adrian Robert Minut, Tommaso Mencattini, Donato Crisostomi, Andrea Santilli, Iacopo Masi, Emanuele Rodol\`a

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a multi-objective evolutionary model merging framework to compress reasoning traces (Long-to-Short), directly targeting latent reasoning efficiency.

**摘要**: arXiv：2604.06465v1宣布类型：新摘要：推理模型在通过利用长思维链来解决复杂问题方面表现出了非凡的能力。然而，这种更深思熟虑的推理在推理时会带来大量的计算负担。长到短（L2 S）推理问题寻求使用更少的令牌来保持高准确性，但当前的免训练模型合并方法依赖于分层的固定超参数算术方法，这些方法高度脆弱，并迫使次优妥协。为了解决这一差距，我们引入了Evo-L2 S，这是一个新颖的框架，将L2 S推理制定为多目标优化挑战。通过利用进化模型合并，Evo-L2 S显式优化了准确性和输出长度之间的权衡，以产生合并模型的稳健帕累托前沿。为了使这种搜索对于大型语言模型在计算上易于处理，我们提出了一种基于信息量的子集采样技术，该技术可以大幅减少适应度估计的负担。在六个数学推理基准上进行的1.5B、7 B和14 B参数尺度的综合实验表明，Evo-L2 S可以将生成的推理轨迹的长度减少50%以上，同时保持甚至提高原始推理模型的问题解决精度。

[阅读原文](https://arxiv.org/abs/2604.06465)

---

## 19. 言行一致：通过多模式统计政策优化弥合图像思维的推理与行动差距

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wenhao Yang, Yu Xia, Jinlong Huang, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Yuchen Zhou, Xiaobo Xia, Yuanyu Wan, Lijun Zhang, Tat-Seng Chua

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Multimodal Agentic Policy Optimization (MAPO), a novel RL method for MLLMs that couples semantic alignment of visual observations with task reward to bridge the reasoning-action gap.

**摘要**: arXiv：2604.06777v1公告类型：新摘要：多模态大型语言模型（MLLM）的最新进展激励模型通过在多轮推理期间积极调用视觉工具来“用图像思考”。依赖于基于结果的奖励的常见强化学习（RL）实践忽略了这样一个事实，即文本可解释性通常掩盖了执行失败，这意味着模型可能会表现出直观的文本推理，同时在其代理推理轨迹中执行不精确或不相关的视觉动作。这种推理-动作差异引入了在多轮推理过程中积累的噪音，严重降低了模型的多模式推理能力，并可能导致训练崩溃。在本文中，我们引入了多模式统计政策优化（MAPO），弥合文本推理和模型在其多模式思想链（MCoT）中生成的视觉动作之间的差距。具体来说，MAPO要求模型为通过工具使用获得的视觉内容生成显式文本描述。然后，我们采用一种新颖的优势估计，将这些描述和实际观察之间的语义一致与任务奖励相结合。我们提供了理论研究结果来证明MAPO背后的原理，MAPO本质上减少了梯度的方差，大量的实验表明我们的方法在多个视觉推理基准上实现了卓越的性能。

[阅读原文](https://arxiv.org/abs/2604.06777)

---

## 20. 难度缩放的局限性：硬样本在GRPO调谐的SLC中产生的回报不断减少

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Suraj Yadav, Siddharth Yadav, Parth Goyal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies GRPO (a preference optimization/RL method) for improving LLM reasoning, analyzing its limits and scaling with difficulty.

**摘要**: arXiv：2604.06298v1宣布类型：新摘要：最近关于大型语言模型（LLM）的对齐工作表明，偏好优化可以通过将概率质量转向更好的解决方案来改善推理。我们在资源有限的环境中测试了这一说法，方法是将GRPO和LoRA应用于SLS（最高3B），在GSM 8 K和MAT数据集上进行数学推理，并进行困难分层分析。随着问题难度的增加，准确性趋于平稳，揭示了能力边界：GRPO主要重塑输出偏好，而不可靠地改进最难层的解决方案。与此一致，仅在较低难度的问题上训练GRPO可与跨难度层的全数据集准确性相匹配，同时仅使用约45%的训练步骤，这表明在该方案中，较硬样本的回报递减。我们还发现了一种跨数据集的概括效应：经过GSM 8 K训练的GRPO在MAT的数字子集上实现了比经过Mathh训练的GRPO更高的准确性，在1.5B时比它高出约5%，在3B时比它高出约3%。我们表明，最佳可实现的收益在很大程度上取决于基本模型的先验推理能力和数据集的难度概况。

[阅读原文](https://arxiv.org/abs/2604.06298)

---

## 21. MAR-GRPO：用于AR扩散混合图像生成的稳定GRPO

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Xiaoxiao Ma, Jiachen Lei, Tianfei Ren, Jie Huang, Siming Fu, Aiming Hao, Jiahong Wu, Xiangxiang Chu, Feng Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a stabilized RL framework (MAR-GRPO) for hybrid autoregressive-diffusion models, directly addressing RL for generative models with novel gradient noise reduction techniques.

**摘要**: arXiv：2604.06966v1公告类型：新摘要：强化学习（RL）已成功应用于自回归（AR）和扩散模型。然而，由于交错推理和噪声对数概率估计，将RL扩展到混合AR扩散框架仍然具有挑战性。在这项工作中，我们研究了掩蔽自回归模型（VAR），并表明扩散头在训练动态中发挥着关键作用，通常引入噪音梯度，导致不稳定和早期性能饱和。为了解决这个问题，我们提出了一个稳定的VAR RL框架。我们引入了多轨迹期望（MTE），它通过对多个扩散轨迹进行平均来估计优化方向，从而减少扩散引起的梯度噪音。为了避免过度平滑，我们进一步估计多个轨迹的代币不确定性，并仅对前k %的不确定代币应用多轨迹优化。此外，我们还引入了一种一致性感知代币选择策略，该策略可以过滤掉与最终生成的内容不太一致的AR代币。跨多个基准的广泛实验表明，与基线GRPO和RL前模型相比，我们的方法持续提高了视觉质量、训练稳定性和空间结构理解。代码可访问：https://github.com/AMAP-ML/mar-grpo。

[阅读原文](https://arxiv.org/abs/2604.06966)

---

## 22. 个性化奖励平台：通过人性化个性化评估奖励模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Qiyao Ma, Dechen Gao, Rui Cai, Boqi Zhao, Hanchu Zhou, Junshan Zhang, Zhe Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a benchmark for evaluating reward models on personalized human preferences, with demonstrated correlation to downstream RL (PPO) performance.

**摘要**: arXiv：2604.07343v1宣布类型：新摘要：多元对齐已成为大型语言模型（LLM）开发的一个关键前沿，奖励模型（RM）是捕捉多样化人类价值观的核心机制。虽然一般响应质量的基准很普遍，但评估奖励模型如何很好地考虑个人用户偏好仍然是一个悬而未决的挑战。为了弥合这一差距，我们引入了个性化奖励长凳，这是一个新颖的基准，旨在严格评估奖励模型对个性化偏好进行建模的能力。我们根据严格遵守（或违反）用户特定的主题来构建选择和拒绝的响应对，确保偏好区分是针对个人独特的。特别是，人类评估证实，配对之间的主要区别因素严格是个人偏好，两种反应都保持高的总体质量（例如，正确性、相关性和有用性）。广泛的测试表明，现有的最先进的奖励模型在个性化方面遇到了严重困难，准确率峰值仅为75.94%。至关重要的是，由于有效的奖励模型基准应该预测奖励模型在下游任务上的性能，因此我们进行了实验，证明与现有基线相比，我们的基准在N最佳（BoN）采样和近端策略优化（PPO）中与下游性能表现出显着更高的相关性。这些发现使个性化奖励平台成为评估奖励模型在下游应用程序中性能的强大而准确的代理。

[阅读原文](https://arxiv.org/abs/2604.07343)

---

## 23. 基于强化学习和监督微调的开源LLM应用驱动教学知识优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Navan Preet Singh, Xiaokun Wang, Anurag Garikipati, Madalina Ciobanu, Qingqing Mao, Ritankar Das

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-stage RL and SFT optimization strategy for LLMs, focusing on progressive difficulty training and data synthesis, directly matching RL for LLMs criteria.

**摘要**: arXiv：2604.06385v1宣布类型：新摘要：我们提出了一种结合强化学习（RL）和监督式微调（SFT）的创新多阶段优化策略，以增强大型语言模型（LLM）的教学知识，如EduQwen 32 B-RL 1、EduQwen 32 B-SFT和可选的第三阶段模型EduQwen 32 B-SFT-RL 2所示：（1）RL优化，实现渐进难度训练，专注于具有挑战性的示例，并采用扩展推理展开;（2）随后的SFT阶段，利用RL训练的模型来合成具有难度加权采样的高质量训练数据;以及（3）可选的第二轮RL优化。EduQwen 32 B-RL 1、EduQwen 32 B-SFT和EduQwen 32 B-SFT-RL 2是一个应用程序驱动的开源教学LLM系列，构建在密集的Qwen 3 - 32 B主干网上。这些模型在跨领域教学知识（CDPK）基准上显着实现了足够高的准确性，可以在交互式教学基准排行榜上建立新的最先进（SOTA）结果，并超越了显着更大的专有系统，例如之前的基准领导者Gemini-3 Pro。这些密集的320亿参数模型表明，领域专业化优化可以将中型开源LLM转变为真正的教学领域专家，其表现优于大型通用系统，同时保留负责任的教育人工智能部署所需的透明度、可定制性和成本效率。

[阅读原文](https://arxiv.org/abs/2604.06385)

---

## 24. SEARCH DE-ED：同理心对话系统的基于战略的逐步推理框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Hongru Ji, Yuyin Fan, Meng Zhao, Xianghua Li, Lianwei Wu, Chao Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage training paradigm combining supervised fine-tuning with multi-objective reinforcement learning to align LLM behaviors with empathetic strategies.

**摘要**: arXiv：2604.07100v1宣布类型：新摘要：同理心对话不仅需要识别用户的情绪状态，还需要在整个响应生成过程中做出具有策略意识、上下文敏感的决策。然而，缺乏全面的同理心策略框架、明确的与任务一致的多阶段推理和高质量的策略感知数据从根本上限制了现有的方法，使它们无法有效地将同理心对话建模为一个复杂的、多阶段的认知和决策过程。为了应对这些挑战，我们提出了SEARCH DE-ED，这是一个基于STRategy的、可解释的和深度的推理框架，通过结构化的、受策略条件的推理来建模同理心对话。为了支持有效的学习，我们开发了一个策略感知的数据细化管道，集成了基于LLM的注释、多模型一致性加权评估和动态采样，以构建与同理心策略一致的高质量训练数据。此外，我们采用两阶段训练范式，将监督微调与多目标强化学习相结合，以更好地将模型行为与目标情绪、同理心策略和响应格式保持一致。大量实验表明，CLARDE-ED在各种开源LLM上进行了推广，并且在自动指标和人工评估方面始终优于现有方法。

[阅读原文](https://arxiv.org/abs/2604.07100)

---

