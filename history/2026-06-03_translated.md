# 💡 今日研究速览 (Daily Summary)

# 潜在推理和解释性
大量论文超越了思维链的黑匣子，专注于潜在的推理操纵和理解内部模型计算。作品提出了由机械解释性指导的免训练解码时干预，并引入了诸如几何潜在推理（GLR）等新颖架构，这些架构可以学习嵌入空间中的连续轨迹以提高效率。然而，该领域也在进行批判性的自我反思;机械诊断表明，潜在视觉推理中的性能提高可能来自格式标记，而不是真正的潜在“插槽”，这挑战了核心假设。推进新的潜在架构与严格验证其潜在机制之间的紧张关系定义了当前的前沿。并行框架将这一范式扩展到多模式领域，包括视觉-语言-动作和语音识别，这表明了推理过程内化的广泛趋势。

# LLM的RL：理论、优化和对齐
该领域正在经历理论和方法论严谨性的复兴。一个关键的理论贡献提供了因果信息理论界限，解释了为什么基于结果的RL会导致推理捷径，正式证明过程奖励模型是一个拓扑过滤器。这还辅之以一系列解决关键瓶颈的实用创新：信用分配（通过LoRA的适配器剩余、阶梯级优势）、熵崩溃（通过作为“政策再加热器”的政策上自蒸馏）和样本低效率（通过优先级组重播）。混合中等长度策略优化（HMPO）等新优化食谱直接解决CoT压缩问题，而纳什偏好优化和语义校准自玩（S-SPPO）的框架则细化了一致性。趋势是朝着更细、理论上更有依据、更高效的RL训练食谱发展，超越简单的结果奖励。

# 自我改进和自我进化的代理人
代理格局正在从静态工具使用转向动态、闭环的自我改进。核心主题是代理组件的共同进化-世界模型和政策（COMAP）、技能和工具（SkillSmith）或技能和记忆（MemPro）。这些框架利用自我提炼、车间级信用分配和故障模式引导的修订来创建一个没有外部监督的持续改进循环。ExpWeaver等新颖方法使用隐藏状态的潜在检索增强生成，而其他方法则专注于通过RL（SIRI）或提炼野外指南（MMG 2 Skill）内化技能。这代表了从简单的RL微调到从自己的经验中学习的复杂、多组件进化系统的成熟。

# 使用RL进行视觉和多模式推理
强化学习正在积极应用于视觉和多模式领域，超越静态基准。TRON的引入为视觉推理RL提供了一个可控、可验证的在线环境，实现无限课程学习。它与DeepLatent等新颖架构搭配使用，用于并行潜在视觉推理，以及使用GRPO进行主动3D视角控制的框架。重点是减轻多模式模型特有的偏见，例如通过DPO的空间词汇偏见和通过基于GRPO的奖励建模的MLLM作为法官中的感知判断偏见。趋势是创建可验证的交互式训练循环，以在感知数据中进行推理，其应用范围从航空导航到放射学报告生成。

# 培训效率和数据合成
大规模RL培训的实用性正在取得重大工程和算法进展。创新解决了具有动态组规模的同步按策略RL中的落后问题，并提出了无日志按策略蒸馏（OmniOPD）以实现更快、更可扩展的训练。在数据方面，“数据飞跃”概念正在变得可操作化，正如HomeFlow对智能家居代理的可验证模拟以及使用代理深度研究来构建GRPO的细粒度规则（DR-rubric）中所示。从静态数据集到动态生成的、可验证的训练数据的转变是扩展基于RL的推理和代理训练的关键推动因素。

---

## 1. 解锁潜在推理的黑匣子：解释性引导的干预方法

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Shuochen Chang, Tong Bai, Xiaofeng Zhang, Qianli Ma, Qingyang Liu, Zhaohe Liao, Yibo Miao, Li Niu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes training-free, decode-time interventions on latent reasoning vectors guided by mechanistic interpretability, directly addressing latent reasoning control.

**摘要**: arXiv：2606.01243v1公告类型：新摘要：潜在推理使大型语言模型（LLM）能够在连续的隐藏状态中执行多步推理，从而比显式思想链（CoT）提供效率提升。然而，这些连续的思想载体的不透明性阻碍了它们的可靠性和可控性。本文弥合了机械解释性和可操作控制之间的差距。我们首先使用结构、因果和几何探针进行系统分析，揭示潜在载体编码推理步骤的压缩、忠实表示，早期载体充当关键的因果中心。在此基础上，我们将这些可解释性见解实施为一套免训练、解码时干预措施，这些干预措施通过强加已识别的几何和语义先验来完善潜在推理过程。跨多个模型尺度和不同任务领域的广泛实验表明，我们的方法能够持续提高推理准确性。我们的可解释性引导干预可持续释放潜在能力并提高推理准确性，无需任何参数更新。

[阅读原文](https://arxiv.org/abs/2606.01243)

---

## 2. Deep潜伏：通过并行潜伏视觉推理思考图像

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Dongchen Lu, Zhimo Li, Mao Shu, Huo Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DeepLatent, a parallel latent visual reasoning framework with a novel LatentFormer and continuous-space RL for optimizing latent representations, directly targeting latent reasoning.

**摘要**: arXiv：2606.00562v1宣布类型：新摘要：新兴的“用图像思考”范式将视觉状态嵌入到中间推理步骤中，定义了视觉语言模型的新前沿。现有的方法有两条路线。工具辅助方法应用显式视觉操作，但存在高延迟和限制操作类型的问题。潜在推理方法自回归产生隐式视觉状态，但表现不佳工具辅助方法，而且它们的潜在标记无法捕获有效的视觉信息。在这项工作中，我们提出了DeepLatent，这是一个潜在视觉推理的并行框架。首先，我们介绍LatentFormer。它使用可学习的2D令牌并行生成受上下文影响的潜在状态，将每个视觉更新直接锚定在原始图像特征中。其次，我们设计了连续空间强化学习算法。它直接在嵌入空间中优化潜在调制参数，显着提高潜在表示质量。该框架是通过知识提炼和连续空间RL算法来训练的。此外，我们还提供了DeepLatent-180 K，这是一个为潜在视觉推理量身定制的大规模数据集。对多个基准的广泛评估表明DeepLatent实现了最先进的性能。

[阅读原文](https://arxiv.org/abs/2606.00562)

---

## 3. TRON：视觉推理RL的有针对性的规则可验证在线环境

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianze Yang, Yucheng Shi, Ruitong Sun, Jingyuan Huang, Ninghao Liu, Jin Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces TRON, a controllable online environment generator for visual reasoning RL, enabling unbounded verifiable training rollouts and curriculum learning.

**摘要**: arXiv：2606.01599v1宣布类型：新摘要：视觉推理的强化学习（RL）需要可扩展、可验证和可控的训练信号。现有的视觉RL后训练在静态策划的数据集上进行训练，固定的图像问答样本受其收集预算限制。在这项工作中，我们引入了TRON（有针对性的、规则可验证的在线电子设备），这是一种在线环境基础：由可控的生成器验证程序按需生成训练部署，该程序对新鲜的潜在视觉状态进行采样，渲染图像，提出问题，并准确验证答案。因此，一次运行可以在当前课程要求的难度水平上绘制无限的新实例流。当前的TRON套件包含520个环境，组织为五个能力桶（空间、数学、图表、模式/逻辑和计数）;相同的底层支持在所有桶上训练的单个完整模型和每桶能力专家模型，无需额外的数据收集。我们还引入了一种底层分析，涵盖生成可靠性、实例和级别多样性、跨环境近乎重复以及按难度级别划分的基本模型通过率。使用METHOD的RL后训练持续提高了Qwen 3-BL-4 B、Qwen 2.5-BL-7 B和MiMo-BL-7 B-SFT的十个外部多模式推理基准的性能。

[阅读原文](https://arxiv.org/abs/2606.01599)

---

## 4. 结果优化的悖论：LLM中推理捷径的因果信息理论界限

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zihan Chen, Yiming Zhang, Wenxiang Geng, Zenghui Ding, Yining Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical framework (SCM+IB) explaining why outcome-based RL leads to reasoning shortcuts in LLMs and formally justifies process reward models as topological filters, directly addressing RL for LLMs.

**摘要**: arXiv：2606.00674v1宣布类型：新摘要：通过基于结果的强化学习（RL）对齐的大型语言模型（LLM）经常表现出严重的失败模式：它们在分布内基准上实现了高性能，同时在分布外（OOD）任务上表现出脆弱的推理能力。我们将这种现象称为奖励诱导的汇管崩溃。我们建立了一个连接结构因果模型和信息瓶颈原理的理论框架来解释这一悖论。我们将推理定义为一个高复杂度的因果过程，将捷径学习定义为利用低复杂度的虚假相关性。在随机梯度下降（SGD）的隐式归纳偏差下，为结果奖励优化的模型偏向于捷径解决方案，只要训练分布允许真正因果机制的“马尔可夫筛选”。我们推导出一个新的泛化范围的基础上语义覆盖测度（$\eta$），而不是样本大小，显示为什么数据缩放均匀分布可能无法纠正推理缺陷。我们还表明，流程奖励模型（PRM）的作用是Topological Filters，强制实施逐步的互信息约束，使低复杂性捷径多管齐下。这些结果为流程监督的作用提供了数学基础，超出了简单的信用分配。

[阅读原文](https://arxiv.org/abs/2606.00674)

---

## 5. 抽象变形金刚可以通过强化学习搜索

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tong Yang, Yu Huang, Yingbin Liang, Yuejie Chi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical analysis of how transformer-based agents learn to search via RL training dynamics, directly addressing RL for LLMs and self-improving agents.

**摘要**: arXiv：2606.00183v1宣布类型：新摘要：树搜索是许多语言代理推理和决策任务背后的核心抽象：代理必须探索行动、记住失败并回溯到有希望的替代方案。然而，我们缺乏对基于转换器的策略如何从强化学习（RL）的训练动态中获得此类搜索能力的理论了解。我们在随机$k$-元树环境中研究这个问题，其中代理Transformer仅通过交互观察其轨迹历史，并因到达隐藏叶目标节点而接收最终奖励。我们首先构建一个双头Transformer，实现随机深度优先搜索（DFS）：一个头跟踪之前的操作，而另一个头检测失败结果并触发回溯。然后，我们分析了深度课程下政策梯度的训练动态，表明这种相同的DFS机制是在没有专家演示的情况下从稀疏强化反馈分阶段出现的。由此产生的策略表现出深度概括：仅在深度-1美元和深度-2美元的树上进行训练后，它在更深的全树上取得了成功。我们进一步表明，在不平衡的目标分布下，贴现回报会导致分级的DFS策略，该策略优先考虑高概率分支。总的来说，我们的结果确定了基于变换器的搜索的机械范式，其中注意力头专业化并合作从上下文中提取与决策相关的痕迹，并通过RL训练将它们转换为代理动作选择。

[阅读原文](https://arxiv.org/abs/2606.00183)

---

## 6. 超越视觉记忆：潜在视觉推理的机械诊断

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Garvin Guo, Yu Chen, Xiang Wang, Shuai Li, Xinpei Zhao, Huaxing Liu, Shuai Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Mechanistically decomposes latent visual reasoning tokens, revealing gains come from boundary markers and format rather than latent slots, challenging assumptions in latent reasoning.

**摘要**: arXiv：2606.01287v1宣布类型：新摘要：最近的潜在视觉推理方法通过将连续的潜在标记插入到多模式语言模型中来获得实质性收益。这些收益通常归因于编码视觉证据的代币;然而，最近的分析揭示了一个悖论：代币与图像松散地联系在一起，对答案贡献不大。至关重要的是，这些分析将潜在代币视为一个单位，模糊了收益的真正来源。因此，我们将潜在代币分解为三个可测试的组件：潜在槽位、边界标记和格式，并开发出一种最先进的方法作为有利条件下的探测器。在六个方法阶段设置和四个感知量很大的基准中，潜在槽无法通过视觉记忆帐户的每一项预测。引人注目的是，仅保留边界标记在几种设置中可以保留78%至100%的收益，而模型在潜在位置比在答案位置更窄地关注图像。因此，收益来自边界标记、格式和这种注意力模式，而不是来自潜在的位置。每种方法如何使用该机制取决于其训练监督：在匹配的准确性下，机制仍然可能存在显着差异。因此，潜在的视觉推理不仅需要准确性进行评估，还需要模型实际依赖的内容。

[阅读原文](https://arxiv.org/abs/2606.01287)

---

## 7. COMAP：LLM代理的共同演变世界模型和代理政策

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Youwei Liu, Jian Wang, Hanlin Wang, Wenjie Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel co-evolutionary framework for LLM agents that jointly updates a world model and agent policy via closed-loop interaction and self-distillation, directly matching the self-improving agent criterion.

**摘要**: arXiv：2606.02372v1宣布类型：新摘要：为语言代理配备世界模型使它们能够预测环境动态并在执行之前评估候选动作。然而，现有的文本世界模型通常在训练后是固定的，从而阻止它们适应由不断发展的代理人引发的政策上的状态动作分布。与此同时，代理改进方法通常依赖于外部奖励或验证者，限制了它们在现实交互环境中的适用性。在本文中，我们提出了COMAP，这是一个新颖的框架，通过闭环交互共同进化文本世界模型和代理策略。在每个决策步骤，世界模型预测候选动作的未来状态反馈，代理通过估计此反馈的可靠性并相应地改进其动作来执行未来感知反射。然后使用由此产生的政策轨迹通过自我提炼来更新世界模型，使其能够更好地匹配代理不断变化的交互分布。在具体任务规划、Web导航和工具使用基准方面，COMAP始终优于竞争基准，例如，Qwen 3 - 4 B相对提高+16.75%。进一步的分析表明，协同进化循环随着时间的推移提高了世界模型的预测准确性，并导致更有效的长期决策。我们的代码可访问：https://github.com/loyiv/CoMAP。

[阅读原文](https://arxiv.org/abs/2606.02372)

---

## 8. ReSkill：在大型RL中将技能创造与政策优化相结合

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zelin He, Haotian Lin, Boran Han, Wei Zhu, Haoyang Fang, Bernie Wang, Xuan Zhu, Runze Li, Matthew Reimherr

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ReSkill, an RL-in-the-loop skill creation framework that reconciles skill evolution with policy learning for LLM agents, directly matching the RL for LLMs and self-evolving agents criteria.

**摘要**: arXiv：2606.01619v1宣布类型：新摘要：抽象强化学习（RL）使LLM代理能够从环境奖励中不断改进，但由此产生的策略并没有系统地积累可重复使用的策略，这些策略可以在任务中推广。模块化技能可以提供此类可重复使用的策略，但现有的技能增强RL方法将技能创建与政策优化脱钩，从而冒着采用与不断变化的政策相冲突的技能的风险。受Anthropic的Skill Creator的启发，我们引入了ReSkill，这是一个RL在环技能创建框架，可协调技能进化与政策学习。ReSkill利用GRPO的分组结构，自然嵌入三种机制，仅需边际额外负担：（1）主张驱动的技能创建者，根据过去的经验诊断失败，并提出有条件的、基于操作员的技能修订;（2）组内推出采样，能够对技能版本进行受控比较，捕捉哪个版本最能支持政策的持续学习;和（3）随着政策的发展，具有适应性折扣的汤普森抽样，以平衡技能版本选择中的探索和利用。在多个领域，ReSkill的性能始终优于现有的记忆和基于技能的RL方法，在不可见的任务上获得了最大的收益。对技能生命周期的分析显示，随着政策的改进，技能会自动创建、测试、完善和修剪，从而证明了协调的技能与政策协同演变。

[阅读原文](https://arxiv.org/abs/2606.01619)

---

## 9. HomeFlow：具有可验证模拟的智能家居代理培训的数据飞轮

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yi Gu, Huacan Wang, Shuo Zhang, Yuqing Hou, Lei Xue, Weipeng Ming, Chen Liu, Fangzhou Yu, Kuan Li, Ronghao Chen, Sen Hu, Xiaofeng Mou, Yi Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a verifiable data flywheel for smart home agent training with MCTS-Flow for trajectory synthesis and step-wise RLVE, demonstrating strong task success rates.

**摘要**: arXiv：2606.01230v1宣布类型：新摘要：大型语言模型代理正在从纯文本交互转向物理世界控制，智能家居作为代表领域。真正的家庭互动需要理解模糊的意图、在动态环境中操作并进行多轮推理。然而，现有方法很难为智能家居代理生成高质量的培训数据。我们提出HomeFlow，这是该领域的一种可验证的数据陀螺。HomeFlow使用HomeEnv作为统一的模拟环境，并使用HomeMaker以程序方式生成多样化的家庭设置。随后，Blueprint将开放式用户意图汇编成可执行的基于状态的成功条件，而MCTS-Flow则通过环境引导的树搜索合成多样化、可验证的多转弯轨迹。然后，我们通过有监督的微调和逐步的RNVE来优化代理，这有助于通过真实的物理反馈进行迭代改进。我们进一步构建SmartHome-Bench来评估各种智能家居任务中的代理。在此基准上，HomeFlow-RL-4 B和HomeFlow-RL-8B的任务成功率分别为84.60%和87.03%。值得注意的是，HomeFlow-RL-8B甚至超越领先的GPT-5.5 1.23个百分点。

[阅读原文](https://arxiv.org/abs/2606.01230)

---

## 10. OpenWebRL：揭开可视化Web代理的在线多轮强化学习的神秘面纱

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Rui Yang, Qianhui Wu, Yuxi Chen, Hao Bai, Wenlin Yao, Hao Cheng, Baolin Peng, Huan Zhang, Tong Zhang, Jianfeng Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an open framework for training visual web agents with online multi-turn RL on live websites, achieving strong results with minimal data.

**摘要**: arXiv：2606.02031v1宣布类型：新摘要：构建有能力的视觉网络代理需要长期推理、精确的基础以及与动态现实世界网站的强大交互。尽管进展迅速，但最强大的系统在很大程度上仍然是专有的，而开放代理仍然严重依赖对大量策划网络轨迹的监督后训练。这种依赖性造成了一个主要的可扩展性瓶颈：高质量的演示的收集成本高昂，而静态数据集对多样化、不断变化的开放网络的覆盖范围有限。尽管在线RL已经展示出了基于文本的代理的前景，但其直接在实时网站上训练视觉网络代理的潜力仍然没有得到充分的开发。本文介绍了OpenWebRL，这是一个开放框架，用于在真实网站上通过在线多回合RL训练视觉Web代理。OpenWebRL涵盖完整的培训管道，包括可扩展的实时浏览器基础设施、监督初始化、多模式上下文管理、车间级成功判断和高效的多回合策略优化。使用这个框架，我们训练OpenWebRL-4 B，它在具有挑战性的实时网络基准测试方面建立了新的开源技术水平。OpenWebRL-4 B仅采用0.4K初始化轨迹和2.2K开放式RL训练任务，在Online-Mind 2 Web上取得了67.0%的成功率，在DeepShop上取得了64.0%的成功率，优于之前类似或更大规模的开放代理，并与OpenAI CUA和Gemini CUA等专有系统保持竞争力。除了强大的基准性能之外，我们还系统地研究了使在线RL对视觉网络代理有效的关键设计选择，并分析RL如何改进代理推理。总的来说，我们的工作为构建更有能力、可重复性和更具成本效益的开放Web代理提供了一条实用途径。我们将发布我们的训练数据、模型和代码来支持未来的研究。

[阅读原文](https://arxiv.org/abs/2606.02031)

---

## 11. ExpWeaver：LLM代理通过Latent RAG从经验中学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tao Feng, Tianyang Luo, Jingjun Xu, Zhigang Hua, Yan Xie, Shuang Yang, Ge Liu, Jiaxuan You

**机构**: University of Illinois Urbana-Champaign

**💡 亮点 (Highlight)**: Proposes ExpWeaver, a framework for LLM agents to learn from experience via latent retrieval-augmented generation, using hidden states and RL optimization, directly addressing self-improving agents and latent reasoning.

**摘要**: arXiv：2606.01041v1宣布类型：新摘要：通过将过去的交互集成为可重复使用的知识，体验学习在增强LLM代理规划和推理方面取得了可喜的成果。然而，现有的方法仍然局限于显式文本空间，通过语义相似性来检索体验并将它们连接到上下文窗口中，从而导致大量的令牌负担和将检索与生成分离的脱钩架构。为了解决这些限制，我们提出了ExpWeaver，这是一个框架，使LLM代理能够通过潜在的检索增强生成从经验中学习，而不需要单独的RAG模块。ExpWeaver使用LLM自己的隐藏状态对体验进行编码，在每个解码步骤直接在潜在空间中检索相关体验，并通过交叉注意聚集和门控剩余机制将它们集成。整个管道通过强化学习进行端到端优化，支持生成任务和排名任务。我们评估ExpWeaver的13项不同任务，涵盖问答、推理、编码、科学预测和推荐。结果表明，ExpWeaver在13项任务中的12项中实现了最先进的性能，比最强基线高出6.8%以上;保持与非检索基线相当的令牌效率，而基于文本的检索方法需要多出1.5至2倍的令牌;并表现出出色的跨域概括性，在零镜头传输下比最强基线高出16.32%，在少镜头传输下比最强基线高出15.21%。我们的ExpWeaver代码在https://github.com/ulab-uiuc/ExpWeaver上发布。

[阅读原文](https://arxiv.org/abs/2606.01041)

---

## 12. 几何潜在推理导致LLM中的一代更短

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Shashi Kumar, Yacouba Kaloga, Petr Motlicek, Ina Kodrasi, Andrea Cavallaro

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Geometric Latent Reasoning (GLR), a novel latent reasoning architecture that learns continuous trajectories in embedding space, directly matching the latent CoT/reasoning criterion.

**摘要**: arXiv：2606.02248v1宣布类型：新摘要：大型语言模型通过生成显式推理标记的冗长链来解决复杂问题。虽然有效，但这使得推理成本高昂、对长度敏感且仅限于（离散）自然语言。虽然潜在推理提供了一个连续的替代方案，但确定中间潜在状态的有用结构是一个开放的挑战。在本文中，我们将潜在推理表述为模型预训练的标记嵌入空间内的几何路径逼近问题。我们引入了几何潜在推理（GLR），它使用轻量级的过渡头来预测嵌入空间中的迭代方向更新。使用文本思想链痕迹作为锚，GLR学习逼近离散推理轨迹，同时允许与精确的令牌嵌入的持续偏差。使用Qwen 3模型对数学推理基准的评估揭示了一种新现象：几何潜在推理在没有明确的长度目标的情况下导致了显着更短的世代。通过用连续的潜在步骤取代早期的显式推理，模型通常只需少得多的总生成步骤即可得出正确的答案。这些发现表明，连续轨迹充当紧凑的中间推理状态，暴露了潜在计算预算、输出长度和准确性之间的新权衡。

[阅读原文](https://arxiv.org/abs/2606.02248)

---

## 13. SkillSmith：自我改进Agent系统的共同进化技能和工具

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yangbo Wei, Zhen Huang, Shaoqiang Lu, Junhong Qian, Qifan Wang, Chen Wu, Lei He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-improving agent framework that co-evolves skills and tools via a synergy-aware ecological utility model, directly addressing self-evolving agents.

**摘要**: arXiv：2606.01314v1宣布类型：新摘要：最近的自我进化代理人表明，技能可以通过执行来发现、完善和积累。然而，现有的技能进化框架通常假设固定的工具层并独立评估每项技能，从而限制了它们修复工具级故障或推理技能之间相互作用的能力。我们提出SkillSmith，一个协同意识的技能工具协同进化框架。SkillSmith引入了一个统一的提案空间，其中反射产生原子束，这些束联合修改技能和工具，允许在技能进化识别可重复使用的能力差距时包装、编辑、合成、拆分或退役工具。为了指导这种联合搜索，SkillSmith维护了一种受Lotka-Volterra动力学启发的生态效用模型，其中从执行轨迹估计的交互矩阵捕捉技能之间的成对互补性和冲突，并为检索、突变优先级和退休提供压力信号。此外，SkillSmith记录反模式，包括失败签名、因果归因和补救措施，以加速诊断和否决重复已知错误的提案。对包括WildClawBench在内的三个基准和五个Qwen 3.5模型量表的实验表明，SkillSmith的表现始终优于强基线，并且随着任务复杂性和多技能协同激活的增加，收益会放大。

[阅读原文](https://arxiv.org/abs/2606.01314)

---

## 14. 深入研究作为强化学习的主题

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Wangyi Mei, Zhouhong Gu, Zhenhan Bai, Yin Cai, Lefan Zhang, Zhenxin Ding, Bo Chen, Yan Gao, Yi Wu, Yao Hu, Jiaqing Liang, Deqing Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces DR-rubric, a two-stage framework that uses agentic deep research to construct fine-grained rubrics for GRPO-based RL, enabling scalable reward signals for open-ended reasoning tasks.

**摘要**: arXiv：2606.01091v1宣布类型：新摘要：开放式推理和长篇生成任务缺乏可靠的自动验证信号来进行基于奖励的政策优化。标题提供了一个有希望的替代方案，但现有的方法将它们视为给定的文物--要么手工制作，要么预算生成--并且经常错过最重要的特定任务、知识密集型维度，从而扭曲了奖励信号。我们的主要观察是，标题构建本身就是一个研究问题：确定是什么使反应正确或有洞察力需要发现和综合外部知识。我们提出了深度研究作为Rubric（DR-rubric），这是一个用于构建此类主题的两阶段框架。第一阶段通过迭代多轮代理搜索来引出领域事实、结构约束和故障模式;第二阶段将这些证据提炼成原子的、可独立验证的约束，用于基于GRPO的政策优化。由于正在训练的模型可以充当其自己的标题生成器，因此DR-rubric-8B支持自举标题生成，无需前沿模型帮助。我们对涵盖代理研究和专家推理的6个基准进行评估。实验表明，DR-Rubric只需1 K-3 K训练实例即可实现强大的竞争性能，其中GPT-5生成的标题特别有利于对代理任务的广泛覆盖，Gemini生成的标题在代理和专家推理任务中产生最平衡的性能，而引导标题表现出专业化到再平衡的演变，在第三次迭代中实现最佳的总体性能。结果表明，将标题结构从静态评估模板重新构建到证据驱动的研究过程中，可以为开放式任务产生更可扩展、更细粒度的奖励信号。

[阅读原文](https://arxiv.org/abs/2606.01091)

---

## 15. OmniOPD：通过推测验证进行无Logit政策蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuhang Zhou, Lizhu Zhang, Yifan Wu, Mingyi Wang, Peng Bo, Jiayi Liu, Xiangjun Fan, Zhuokai Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes OmniOPD, a logit-free on-policy distillation framework using chunk-level semantic verification and peak-entropy scheduling, directly improving LLM behavior via a novel RL-like training recipe.

**摘要**: arXiv：2606.01476v1宣布类型：新摘要：按政策蒸馏（OPD）在来自更强教师的密集代币级反馈下，根据自己的生成轨迹训练学生模型，减轻监督微调（SFT）的政策外分布转变和强化学习（RL）的稀疏学分分配。然而，标准OPD面临两个相互关联的限制。首先，它要求直接访问教师的代币级日志，排除了广泛一类有能力的专有模型担任教师。其次，代币级logit信号本身很脆弱，这取决于老师和学生之间看似合理的下一个代币的狭窄重叠，并且容易放大重复循环等退化模式。在本文中，我们介绍了OmniOPD，这是一个新颖的框架，通过无逻辑的块级监督信号来解决这两种限制。OmniOPD用蒙特卡洛推出取代了确定性logit匹配，蒙特卡洛推出通过对多令牌块的连续语义相似性指标来逼近教师的本地偏好，并通过峰值熵调度器集中这种监督，该调度器仅在其高不确定性推理叉处审计学生。Dirichlet-Multinomic Bayesian先验和基本模型KL锚进一步限制了离散抽样的方差，并防止未经审计的代币中的政策崩溃。在竞争基准中，OmniOPD在数学上超过标准OPD方法高达+28.64%，这证实了块级语义验证比标记级logit匹配提取更可靠的学习信号，后者的高信息密度被显着的噪音和脆性所抵消。此外，当与Claude-4.5-Haiku和Gemini-2.5-Flash等更强的黑匣子教师搭配使用时，OmniOPD的数学相对率比开重量教师额外增加了+9.54%，使学生超越了自我探索性RL的表现。

[阅读原文](https://arxiv.org/abs/2606.01476)

---

## 16. 迭代纳什偏好优化的有效探索

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tianlong Nan, Xiaopeng Li, Christian Kroer, Tianyi Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel explicitly exploratory iterative NLHF algorithm with regret guarantees, directly addressing RL for LLMs under general preference models.

**摘要**: arXiv：2606.01382v1宣布类型：新摘要：偏好对齐是改进大型语言模型的核心，但当人类偏好是循环性的、非传递性的或无法用纯量奖励来表示时，标准的基于奖励的公式可能会受到限制。人类反馈纳什学习（NLHF）通过将一致建模为偏好游戏并以纳什均衡而不是回报最大化器为目标来解决这一局限性。然而，可扩展NLHF的学习理论基础仍然有限。现有的遗憾保证依赖于基于Oracle的方法，这些方法估计一般偏好模型并解决KL-正规化极小极大问题，而迭代NLHF方法直接优化政策级偏好损失，并且更容易实现，但缺乏遗憾保证。我们在一般偏好模型下研究在线迭代NLHF，并将探索确定为关键障碍。首先，我们表明标准迭代NLHF可能会对KL-正规化参数呈指数级依赖，这表明通过策略更新的隐式探索不足以控制后悔。其次，我们提出了一种显式探索性迭代NLHF算法，该算法将基于SFT的正规化与对抗性政策探索相结合。所得方法保留了迭代NLHF的直接策略优化结构，避免了显式偏好模型估计，并实现了$O（\squtt {T}）$后悔界，而不对KL-正规化参数有指数依赖。我们表明，通过访问极小极大Oracle，遗憾可以改进为$O（\log（T））$，澄清了学习一般偏好游戏中的计算-统计权衡。最后，我们实例化了LLM微调的方法，并在\textttt {Llama-3- 8B-Direcct}上跨多个基准对其进行评估，其中显式探索会在现有NLHF基线上产生一致的改进。

[阅读原文](https://arxiv.org/abs/2606.01382)

---

## 17. 学习何时不采取行动：缓解抽象强化学习中的工具滥用

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Liuji Chen, Dianxing Tang, Xing Shi, Dingshuo Chen, Qiang Liu, Shu Wu, Liang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EAPO, a novel RL framework for LLM agents that learns selective tool use via difficulty-aware reward shaping and confidence-aware token reweighting, directly addressing tool abuse in agentic RL.

**摘要**: arXiv：2606.02132v1宣布类型：新摘要：抽象的强化学习可能会导致工具滥用，即模型过度使用外部工具，即使对于可通过内部推理解决的查询也是如此。现有的方法通过统一的工具使用惩罚或硬限制来缓解这个问题，这会减少工具频率，但也可能抑制有用的工具辅助勘探。我们提出EAPO，这是一个高效的统计政策优化框架，可以学习选择性工具的使用。EAPO将无工具轨迹引入到每个推出组中，应用困难感知奖励整形来惩罚主要针对更简单的查询的冗余工具调用，并使用信任感知代币重新加权来改善政策学习。在九个数学和知识密集型推理基准中，EAPO一致改善了Qwen 2.5 -3B、Qwen 2.5 - 7 B和Llama3.1-8B的准确性效率权衡。与GRPO相比，EAPO将平均性能提高了10.45%、7.27%和9.69%，同时将平均工具调用量分别降低了18.33%、18.33%和24.59%。这些结果表明，代理可以学习何时不使用工具，而不会损害工具集成推理。

[阅读原文](https://arxiv.org/abs/2606.02132)

---

## 18. 没有无效样本的WLVR：LLM推理的组优先非策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yixiu Mao, Yun Qu, Qi Wang, Heming Zou, Xiangyang Ji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new RLVR framework (POPO) with prioritized group replay and decoupled off-policy optimization to address ineffective samples in LLM reasoning, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2606.01281v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）已成为增强大型语言模型（LLM）推理能力的强大范式。然而，无效训练数据的普遍存在极大地阻碍了其有效性：许多抽样提示产生的响应组要么完全正确，要么完全不正确，导致零方差奖励和有限的学习信号。最近最先进的方法通过广泛推出LLM来过滤无效样本来解决这个问题，但代价是相当大的计算费用。替代方法，包括预测采样和轨迹回放，旨在提高数据效率，但通常仍然不足，并且可能会引入系统偏差或次优约束等额外问题。为了解决这些限制，我们提出了组优先级非策略优化（POPO），这是一个简单而有效的框架，可以充分利用有效的训练批次，而无需额外的推出费用。POPO包括两个关键组件：优先级组重播和脱钩的脱离策略优化。前者通过基于最近度的重播机制，将无效的政策上群体替换为有效的政策外群体，该机制共同考虑样本质量和政策外程度。为了进一步缩小政策外差距，POPO采用脱钩重要性抽样来纠正政策外偏差，同时在一致的信任区域约束下保持稳定的政策更新。对数学、规划和视觉几何等各种推理任务的经验评估表明，POPO大大加速了RL微调，并以显着减少的部署量实现了强大的推理性能。

[阅读原文](https://arxiv.org/abs/2606.01281)

---

## 19. HMPO：思想链压缩的混合中等长度政策优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Minghui Zheng, Hongxu Chen, Huimin Ren, Hongsheng Xin, Xiaoyang Qu, Ze Wang, Shuling Yang, Ziyu Peng, Kaike Zhang, Pan Zhou, Kun Zhan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HMPO, a single-stage RL framework for compressing CoT reasoning tokens via a median-based budget and multiplicative reward, directly addressing RL for LLMs and latent reasoning efficiency.

**摘要**: arXiv：2606.01934v1公告类型：新摘要：大型语言模型通过扩展的思想链（CoT）推理实现了卓越的性能，但这个漫长的过程会产生大量的推理开销。现有的CoT压缩方法与不灵活的手动长度预算、计算昂贵的多阶段训练管道以及受限于小模型的脆弱可扩展性作斗争。我们提出了HMPO（混合中等长度策略优化），这是一种经济高效的单阶段强化学习框架。HMPO通过三个协同组件有效压缩CoT：从成功推出中获得的基于媒体的自适应预算以消除手动调整、用于平滑长度惩罚的cos衰变令牌奖励，以及通过严格优先考虑答案正确性来大幅减轻琐碎奖励黑客行为的相乘奖励公式。HMPO专门接受数学数据培训，可无缝概括数学、代码、科学和描述遵循任务。跨密集和专家混合（MoE）架构从9 B扩展到122 B参数的广泛实验表明，HMPO实现了19%-46%的令牌压缩，准确性下降可以忽略不计，同时与现有的多阶段基线相比大幅降低了训练成本。

[阅读原文](https://arxiv.org/abs/2606.01934)

---

## 20. S-SPPO：语义校准的自玩偏好优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiwen Chen, Wenhui Zhu, Jingjing Wang, Peijie Qiu, Zhipeng Wang, Huayu Li, ZhengXiao He, Xuanzhao Dong, Prayag Tiwari, Mingkun Xu, Yujian Xiong, Feng Luo, Abolfazl Razi, Brendan Hogan Rappazzo, Anderson Schneider, Yuriy Nevmyvaka

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes S-SPPO, a novel self-play preference optimization method with semantic calibration for LLM alignment, directly matching RL for LLMs criteria with a new training recipe.

**摘要**: arXiv：2606.01561v1宣布类型：新摘要：将大型语言模型（LLM）与人类偏好保持一致通常通过直接偏好优化（DPO）来制定。然而，DPO的标准Bradley-Terry实例在建模人类偏好中与传递性的常见偏离方面受到限制。为了解决这个问题，最近的工作引入了自玩偏好优化（SPPO），它通过训练自生成的赢输对来迭代地完善策略。然而，我们的调查揭示了SPPO中的一个关键不稳定性：当偏好预言者将过于自信的胜利分配给语义难以区分的响应时，优化很容易出现策略退化。为了缓解这一问题，我们提出了S-SPPO，这是一个双空间语义校准框架，包括：i）通过语义门控进行监督校准，随着语义重叠的增加，它将获胜率目标向最大熵基线进行退变;和ii）通过潜在排斥进行表示校准，以强制执行几何多样性，以防止多管齐溃缩并保持所选样本和拒绝样本之间的潜在多样性。从理论上讲，我们表明校准保留了恒和博弈结构，有助于收敛到纳什均衡。从经验上看，S-SPPO避免了现有方法中出现的性能下降，在配备Llama-3-8B的AlpacaEval 2.0上实现了52.19%的获胜率和47.46%的长度控制获胜率，而无需在训练期间使用额外的人类注释偏好。该代码可在https://github.com/xiwenc1/s-sppo上获取。

[阅读原文](https://arxiv.org/abs/2606.01561)

---

## 21. SIRI：具有内在技能的自我内化强化学习，用于LLM代理培训

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhongyu He, Yuanfan Li, Fei Huang, Tianyu Chen, Siyuan Chen, Xingyang Li, Meng Hsuan Yu, Xiangrong Liu, Leyi Wei, Lu Pan, Ke Zeng, Xunliang Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a three-phase RL framework for LLM agents to self-discover, validate, and internalize skills without external generators, showing clear self-improvement via trajectory-level utility and action-level advantage.

**摘要**: arXiv：2606.02355v1公告类型：新摘要：长期LLM代理可以从可重用技能中受益，但现有的基于技能的方法通常在训练期间依赖于外部技能生成器或在推理时持续的技能检索，从而增加了工程复杂性，上下文长度和部署延迟。我们提出了具有内在技能的自我内化强化学习（SIRI），这是一个三阶段框架，使代理能够在没有外部技能生成器或推理时间技能库的情况下发现，验证和内化技能。SIRI首先与Giovel一起预热政策，以获得基本互动能力并收集成功的无技能轨迹。然后，它执行自我技能挖掘，当前政策总结其成功的普通部署中的紧凑技能，并通过配对的技能增强和无技能部署来验证它们。最后，SIRI使用个体级效用和行动级优势，仅将有益的技能引导行动代币提炼到简单的政策中。推断时，代理仅在原始提示下运行。在配备Qwen 2.5 - 7 B-Direcct的ALFWorld和WebShop上，SIRI将ALFWorld上的Giulty从0.908提高到0.930，将WebShop上的Giulty从0.728提高到0.813，优于基于预算、基于RL和内存增强的基线。进一步分析表明，我们的自挖掘策略可以实现与闭源大型模型蒸馏相当的性能。我们的代码可在https://github.com/kirito618/SIRI上获取。

[阅读原文](https://arxiv.org/abs/2606.02355)

---

## 22. 内化温度：政策上的自我蒸馏作为强化学习的政策加热器

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xuewei Yang, Jiachen Yu, Jie Wu, Shaoning Sun, Junjie Wang, Yujiu Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TS-OPSD, a novel on-policy self-distillation method that internalizes temperature scaling to restore entropy in RL for LLMs, directly addressing entropy collapse in reasoning-oriented RL.

**摘要**: arXiv：2606.00755v1宣布类型：新摘要：来自可验证奖励的强化学习提高了大型语言模型的推理能力，但通常会受到信息量崩溃的影响，其中越来越集中的策略会减少推出多样性和有用的学习信号。现有的补救措施要么限制RL目标（例如，熵正规化）或在推出收集期间调整采样温度，但这些干预仍然在模型参数之外。我们提出了温度缩放的按策略自蒸馏（TS-OPSD），这是一种轻量级的策略重新加热方法，可以将温度的探索性效应内化为模型参数。TS-OPSD从一个信息量崩溃的RL检查点开始，通过对模型自己的日志应用高温缩放来构建一个自学者，然后将产生的更平稳的分布提取回学生中。此政策重新加热不需要外部教师、特权数据或额外的推断成本。Qwen 3 - 4 B-Base和Qwen 3 - 8 B-Base的实验表明，策略重新加热对连续RL产生的初始化比标准连续RL和滚动级别温度重新加热更强。进一步的分析表明，TS-OPSD主要降低了输出清晰度，同时保留了中间表示、顶级候选集和推理能力。这些结果表明，熵恢复可以作为扩展面向推理的RL的简单崩溃后干预。

[阅读原文](https://arxiv.org/abs/2606.00755)

---

## 23. CAPF：用信用衰减的反馈引导搜索代理的推出

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bin Chen, Xinye Liao, Yiming Liu, Xin Liao, Chonghan Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CAPF, a training-time mechanism that uses verifier-side privileged feedback to guide LLM search-agent rollouts, improving RLVR on hard problems.

**摘要**: arXiv：2606.01830v1宣布类型：新摘要：最近的LLM搜索代理使用具有可验证奖励的强化学习（WLVR）来从结果奖励中学习搜索增强推理。在困难问题上，这些代理很少对端到端的成功推出进行抽样，从而导致仅结果的WLVR几乎没有正回报轨迹。我们认为，改善此类问题的学习需要在培训期间提供额外的指导，而WLVR已经包含可以提供该指导的验证器端信息。该信息可以识别代理提交的答案中的错误或遗漏，并在推出期间指导修订。我们提出了一种名为\textBF{Credit-Attenuated特权反馈}（CAPF）的训练时机制，它使验证器端信息通过训练期间的特权反馈调用可用。CAPF允许该政策将零奖励尝试修改为正奖励修复轨迹，并削弱反馈电话和早期行动的信用度，以适应没有此电话的部署。实证研究表明，CAPF将Qwen 3 - 4 B的平均精确匹配分数从仅结果WLVR下的44.7%提高到七个开放领域QA基准上的48.5%。

[阅读原文](https://arxiv.org/abs/2606.01830)

---

## 24. 超越一次：现场实验中学习的人工智能代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Junjie Luo, Ritu Agarwal, Gordon Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a tool-augmented agentic AI that learns from experimental data to autonomously generate improved interventions, demonstrating a self-improving agent loop.

**摘要**: arXiv：2606.02458v1宣布类型：新摘要：组织定期运行A/B测试实验，但一项实验生成的数据没有充分利用来为后续干预设计提供信息。从之前的实验数据中提取可操作的知识来为新的干预措施提供信息存在重大障碍。我们研究工具增强的人工智能是否可以自动从实验数据中学习，以在后续实验中生成新的干预措施。通过医疗保健处方信息传递的两阶段现场实验（693，139名患者就诊），我们比较了Human + Chatbot方法（第1阶段：行为专家与对话人工智能共同设计13个消息变体，444，691名患者就诊）针对工具增强的统计人工智能方法（第二阶段：人工智能从第一阶段数据中自主提取原理，生成17个新变体，248，448名患者就诊）。统计人工智能方法配备了分析工具、结构化数据-信息-知识-智慧（DIKW）推理代理和透明证据链，可以产生卓越的干预措施：最好的人工智能生成的消息达到了69.8%的TLR（比基线+6.5个百分点）。至关重要的是，我们的结果表明，该值来自特定领域的实验数据，而不是来自一般推理能力：在没有实验数据的情况下运行的前沿LLM未能预测哪些干预措施会成功。现场实验还表明，用于干预设计的通用行为理论并不统一扩展到特定的医疗保健环境，从而激发了在现场实验规模上采用代理人工智能方法进行理论审计。我们的研究表明，工具增强的人工智能可以从实验数据中学习并生成改进的领域相关干预措施，将行为实验从一次性评估转变为可扩展的累积设计学习系统。

[阅读原文](https://arxiv.org/abs/2606.02458)

---

## 25. 人工理性之谜：调查大型推理模型中的生产与评估差距

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Mingzhong Sun, Teresa Yeo, Armando Solar-Lezama, Tan Zhi-Xuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a production-evaluation gap in LRMs and provides causal evidence of answer confirmation bias, directly relevant to RL for LLMs by revealing a limitation in current reasoning training approaches.

**摘要**: arXiv：2606.01462v1宣布类型：新摘要：对人类推理的研究表明，人们通常更擅长评估推理，而不是从头开始产生推理。相比之下，大型推理模型（LRM）经过训练，善于产生长推理链来解决复杂问题。那么LRM在评估原因方面表现如何？我们使用有效-答案-无效-推理（VEIR）数据集来研究这一点：具有琐碎推理缺陷但答案有效的数学问题和解决方案，旨在将推理评估与推理产生的混淆区分开来。与人类不同，我们发现人类在评分方面只比解决此类问题差6%，我们发现LRM中存在巨大的生产评估差距：尽管解决方案生产近乎完美，但前沿模型在评估VAir解决方案时得分低至48%。   为什么是这个谜？通过思想链（CoT）分析，我们发现了答案确认偏差的证据：LRM经常产生然后检查正确答案，而不是仔细验证每一步，即使在注意到异常推理时也会编造合理化。线性探测证实了这一点，表明虽然LRM激活编码了有效推理的一些表示，但它们无法稳健地将VAir解决方案表示为无效。最终答案表示的因果修补导致LRM判决和激活翻转，证明答案有效性是模型确认偏差的原因。这些发现表明，推理训练的主流方法存在明显的局限性，这些方法激励LRM产生和确认正确答案的推理，但不能强有力地评估潜在原因。

[阅读原文](https://arxiv.org/abs/2606.01462)

---

## 26. 自玩定理证明算法的理论框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Thomas Chen, Zhiyuan Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical framework for self-play theorem proving with LLMs, analyzing self-improvement dynamics and proposing a diversity-maximizing conjecturing algorithm, directly relevant to self-evolving agents.

**摘要**: arXiv：2606.01861v1宣布类型：新摘要：自玩是一种使模型能够自我改进的训练算法，最近在使用大型语言模型（LLM）进行形式定理证明的背景下显示出有希望的经验结果。(Dong& Ma，2025）通过两个合作的代理实例化自我游戏：一个证明者，证明定理，和一个假设者，生成新的定理作为证明者的课程。在本文中，我们提供了一个理论框架来理解自玩算法的自我改进能力，以实现定理证明。首先，我们将定理集形式化为一个图，其中节点为定理，两对具有相似语义的定理之间的边。我们引入了一组原始假设，这些假设描述了训练有素的证明者的保证以及证明者如何访问图的结构。其次，我们表明，如果基本的定理图是良好连通的，那么证明者-假设者系统（其中假设算法基于可逆随机游走）足以指数增长已证明的定理集。第三，激发了经验上遇到的问题，自我发挥算法，其中的deleturer往往会产生人为的复杂和非基本定理，我们提出了一个多样性措施的训练分布的定理产生的deleturer和改进的deleturer算法，局部最大化这种多样性措施，通过计算相邻定理之间的扩散相似性的定理图。最后，我们描述了一种计算扩散相似度的方法，通过使用对比学习将节点嵌入到欧氏空间中，然后计算嵌入之间的内积。

[阅读原文](https://arxiv.org/abs/2606.01861)

---

## 27. 摆脱模式抽奖：多响应训练提高语言模型泛化能力

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Hasan Amin, Kian Ahrabian, Ming Yin, Rajiv Khanna

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes multi-response training (MRT) as a principled RL-like data allocation method for fine-tuning LLMs, directly addressing the mode lottery problem with a variance-budget tradeoff and novel selection strategies.

**摘要**: arXiv：2606.00544v1宣布类型：新摘要：现代语言模型微调通常会将每个提示与单个响应配对，尽管许多提示承认多个有效完成。这有效地将多模式条件分布简化为单样本视图，我们将这种现象称为“模式彩票”，其中训练强调看似合理的模式的子集，而使其他模式的代表性不足。我们研究多响应训练（BRT），该训练在每个提示中保留多个响应，并对何时以及为何有帮助制定原则性的说明。我们的主要见解是，提示和响应是不同的统计资源：额外的提示可以减少输入分布的不确定性，而额外的响应可以减少条件输出分布的不确定性。这产生了方差-预算权衡，可以预测何时保留多个响应是值得的，显示出预算水平不确定性占主导地位时的回报递减，并解释了为什么大型冗余库可以表现出隐性的多响应效应。我们进一步分析了响应选择，并表明Random-K-of-N是分布式微调的无偏默认，基于奖励的选择可能会导致模式崩溃，而亚模块质量多样性目标提供了一种具有理论保障的有效替代方案。受控模拟验证了预测的方差和选择效应，包括一种引人注目的失败模式，即只奖励的选择会产生与真实目标不一致的梯度。在结构化和现实世界的数据集中，包括新的多提示、多响应基准，BRT持续改进了分布概括，在高响应多样性、低预算冗余机制中获得了最大的收益。BRT将响应多样性重新定义为一个具有明确指导的数据分配问题：当响应便宜且多样化时，保留多个响应不是启发式的，而是基于统计学的选择。

[阅读原文](https://arxiv.org/abs/2606.00544)

---

## 28. 视觉-语言-动作的连续推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Yueh-Hua Wu, Tatsuya Matsushima, Kei Ota

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel latent reasoning architecture for VLA that uses a shared Gaussian latent interface and self-verification objective, directly addressing latent reasoning for action.

**摘要**: arXiv：2606.00229v1宣布类型：新摘要：自然语言是语言和视觉语言模型的强大推理媒介，但它与连续控制的粒度不匹配。文本和显式子目标以任务级别的粒度运行，而视觉-语言-动作（VLA）策略必须选择更细的时间尺度的动作;因此，单个推理步骤可以跨越许多动作块，同时仅与现在所需的动作保持弱耦合。这对VLA提出了一个不同的问题：语言应该扮演什么角色？我们认为，有用的VLA推理媒体必须可在模型实例之间共享，通过下游动作改进进行验证，并与时间扩展的控制结构保持一致。   基于这一观点，我们提出了视觉-语言-动作的连续推理。我们的模型首先以结构化的连续思想集的形式预测连续推理，然后重新使用它们作为块结构化动作生成的共享上下文。仅靠更好的动作预测并不能证明良好的推理：如果相同的内部媒体无法在模型实例之间共享并通过改进的下游控制进行独立验证，那么添加的潜在可能只是成为模型专用捷径，帮助观察到的行为，而不支持可推广的控制。因此，我们将连续推理实例化为共享高斯潜在界面，并通过自我验证目标对其进行训练，其中指数移动平均值的教师在预测目标动作时必须成功地消化学生的推理。   从经验上看，连续推理提高了LIBERO-PRO的鲁棒性，并在真实机器人上表现出色，在与AgiBot G2兼容的变体TX-G2上将{\pi}0.5的平均子任务成功率提高了40.4%，在HSR上提高了26.3%。这表明VLA中的推理与其说是关于额外的令牌，不如说是关于可共享的、可验证的内部行动语言。

[阅读原文](https://arxiv.org/abs/2606.00229)

---

## 29. MindZero：用零注释学习在线心理推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Shunchi Zhang, Jin Lu, Chuanyang Jin, Yichao Zhou, Zhining Zhang, Tianmin Shu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-supervised RL framework for training MLLMs to perform online mental reasoning (Theory of Mind) without annotations, directly matching RL for LLMs and self-improving agent criteria.

**摘要**: arXiv：2606.00240v1宣布类型：新摘要：有效的现实世界援助需要具有强大的心理理论（ToM）的人工智能代理：从人类的行为推断人类的心理状态。尽管最近取得了进展，但仍然存在几个关键挑战，包括（1）在线推理，具有多个假设的稳健不确定性更新;（2）适合实时协助的高效推理;（3）现实世界领域中缺乏地面真相心理状态注释。我们通过引入MindZero来应对这些挑战，MindZero是一个自我监督的强化学习框架，可以训练多模式大型语言模型（MLLM）以实现高效且稳健的在线心理推理。在训练期间，模型因生成心理状态假设而受到奖励，这些假设最大化了由规划者估计的观察到的动作的可能性，类似于基于模型的ToM推理。因此，这种方法消除了对显式心理状态注释的需要。训练后，MindZero将基于模型的推理内化为快速单程推理。我们根据网格世界和家庭领域中具有挑战性的心理推理和人工智能辅助任务的基线来评估MindZero。我们发现仅靠LLM是不够的;基于模型的方法可以提高准确性，但速度慢、成本高，并且受到主干MLLM容量的限制。相比之下，MindZero增强了MLLM固有的ToM能力，并且在准确性和效率方面显着优于基于模型的方法，这表明心理推理可以作为一种自我监督技能有效学习。

[阅读原文](https://arxiv.org/abs/2606.00240)

---

## 30. LaSR：通过潜在推理的上下文感知语音识别

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Heyang Liu, Ziyang Cheng, Jiayi Huang, Wenyang Xiao, Ronghua Wu, Qunshan Gu, Yanfeng Wang, Yu Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LaSR, a novel training paradigm using latent reasoning for context-aware speech recognition, directly aligning with latent CoT/reasoning criteria.

**摘要**: arXiv：2606.00507v1宣布类型：新摘要：语音大型语言模型（Speech LLM）的最新进展显着增强了口语理解和推理。然而，他们的上下文意识有限，难以执行有效反映说话者意图和话题上下文的语音识别。在本文中，我们提出了LaSR（潜在语音推理），这是一种新颖的训练范式，具有利用潜在推理过程的上下文感知推理轨迹。LaSR不是生成显式的中间令牌，而是围绕目标词的声学特征区域调整思想链（CoT）监督，并引入上下文信息基础和转录转换的潜在推理期。此外，为了有效地根据专业词汇对上下文识别进行基准测试，我们提出了Spoken Darwin-Science，这是一个专注于学术术语的大型数据库。Fun-Audio-Chat上的初步实验表明，LaSR在不引入额外延迟的情况下显着提高了术语识别，并且始终优于标准的监督微调基线。我们的研究结果强调了潜在推理在构建高效、上下文感知的语音助手方面的潜力。

[阅读原文](https://arxiv.org/abs/2606.00507)

---

## 31. 论抽象工具调用和RL培训的有效性和效率

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tong Liu, Cheng Qian, Matej Cief, Yuan He, Daniele Dan, Nikolaos Aletras, Gabriella Kazai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes techniques to accelerate RL-based tool-calling training, directly addressing efficiency in RL for LLM agents.

**摘要**: arXiv：2606.00135v1宣布类型：新摘要：工具调用是现代大型语言模型（LLM）代理的核心组件，为它们提供超出参数知识的技能。本文沿着两个互补的轴研究工具调用：有效性，即如何衡量这种能力，以及效率，即它是如何学习的。在有效性方面，我们系统地分析了工具调用评估管道，并表明结果可能对看似微小、通常未记录的实施选择高度敏感，包括随机种子、系统提示、多回合模板构建以及如何继承先前的交互/推理历史。这些选择可能会导致报告的性能出现巨大差异，特别是在多回合环境中，如果没有严格的标准化，排行榜排名就不可靠。在效率方面，我们检查了用于工具调用的标准强化学习（RL），并确定了两个计算浪费的来源：（i）在推出期间，许多提示不产生学习信号，（ii）在策略更新期间，优化会产生很高的计算成本。在这些发现的指导下，我们引入了两种加速基于RL的工具调用训练的技术，在不降低性能的情况下实现大幅的时钟加速。

[阅读原文](https://arxiv.org/abs/2606.00135)

---

## 32. 视觉语言推理的分解政策蒸馏：视觉基础的指导要素

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hee Suk Yoon, Eunseop Yoon, Jaehyun Jang, SooHwan Eom, Ji Woo Hong, Mark Hasegawa-Johnson, Qi Dai, Chong Luo, Chang D. Yoo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-like on-policy distillation method with gradient steering for VLM reasoning, directly addressing visual grounding as a bottleneck.

**摘要**: arXiv：2606.00564v1宣布类型：新摘要：虽然按策略蒸馏为训练小型推理模型提供了密集的监督，但其在多模式领域的优化动态仍然没有得到充分的探索。在这项工作中，我们通过将损失从数学上分解为两个不同的部分：语言先验和视觉基础，挑战视觉语言模型（VLM）蒸馏的标准整体视图。我们的分析发现，这些分量的梯度载体几乎是垂直的，这表明与教师语言分布保持一致的目标在几何上与匹配其视觉感知的目标独立。因此，标准优化被动地遵循次优妥协轨迹，隐含地平衡了这两个目标。假设视觉基础构成视觉语言推理的主要瓶颈，我们引入了视觉梯度转向（VGS），这是一种动态重新定位更新载体以确定视觉子空间优先顺序的方法。多个蒸馏设置和复杂多模式基准的实验结果表明，VGS显着优于按政策蒸馏的标准整体公式，以最少的训练费用实现了卓越的基础。

[阅读原文](https://arxiv.org/abs/2606.00564)

---

## 33. 哪里看：基金会模型能否通过积极探索达到目标观点？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Liyang Li, Muzhi Zhu, Zhiyue Zhao, Hengyu Zhao, Ke Liu, Linhao Zhong, Hao Chen, Chunhua Shen

**机构**: University of Alberta

**💡 亮点 (Highlight)**: Proposes a new RL-based post-training framework (GRPO) for active 3D viewpoint control, directly matching RL for LLMs with a verifiable reward and online RL pipeline.

**摘要**: arXiv：2606.01247v1宣布类型：新摘要：人类可以通过主动的头部和身体运动再现目标图像指定的观点，但基础模型中的空间智能在很大程度上被研究为对预先收集的观察结果的被动理解。我们引入了目标观点再现（TVR）--一项主动任务，其中代理在3D环境中调整其观点，直到其观察与给定的目标图像相匹配--以及TVRBench，一个跨越场景规模和目标视图视觉丰富性的室内模拟基准。TVR还远未解决：在评估拆分上，最强的开源和闭源模型的成功率仅为7.8%和12.0%。细粒度分析确定了两个一致的瓶颈：现成的模型难以应对多圈视觉历史，而当观点复制需要身体平移而不是原地旋转时，性能急剧下降，从而暴露了将空间差异映射到具体运动方面的差距。为了研究缩小这一差距，我们构建了一个统一的TVR训练后框架，涵盖来自实时模拟器部署的专家轨迹SFT、理性监督的CoT-SFT、离线单圈GRPO和政策上的多圈GRPO。视觉动作SFT提供了主要收益，将9 B开源模型的成功率提高到了50.8%;多圈GRPO提供了有针对性的多房间细化，总体达到了51.4%，而CoT监督和单圈GRPO降低了闭环性能。这些结果使TVRBench成为测量和训练在3D环境中主动感知和行动的基础模型的测试平台。我们的代码、数据和模型可在https://github.com/aim-uofa/TVRBench上获取。

[阅读原文](https://arxiv.org/abs/2606.01247)

---

## 34. ResMerge：大型语言模型的基于剩余的谱合并

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yandu Sun, Zhiyan Hou, Haokai Ma, Yuheng Jia, Junfeng Fang, Haiyun Guo, Hongyan An, weizhen wang, Jinqiao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel spectral merging method (ResMerge) specifically designed for RL-trained expert models, addressing a key challenge in combining RL-finetuned LLMs.

**摘要**: arXiv：2606.02252v1宣布类型：新摘要：模型合并提供了一种无需训练的方式来组合多个训练后的专家模型，但合并通过强化学习（RL）获得的专家仍然具有挑战性。现有的频谱合并方法通常假设领先奇异方向包含主任务信号，而可以压缩、选择或衰减较低能量的残余分量以减少干扰。我们发现，这个假设对于RL任务载体并不成立：在将每个任务载体分解成领先谱头和剩余分量后，这两个部分都可以独立地恢复大量行为知识，同时表现出不同的合并属性。头部高度集中且信息丰富，但更容易出现尖锐的跨专家冲突，而剩余部分更加分散，为聚合提供了更稳定的基础。基于这一观察，我们提出了ResMerge，这是一个针对RL专家的基于剩余的频谱合并框架。ResMerge首先利用球形剩余共识自适应构建稳定的剩余主干，该主干估计弗罗贝尼乌斯球体上的可靠性加权共识方向。然后，它通过由积极的跨专家协议门控的轻量级头部纠正模块重新引入领先头部信息。跨多个RL专家组和能力域的实验表明，ResMerge比代表性任务载体和频谱合并基线更好地保留了专家能力。ResMerge的实现可在https://github.com/sunyd0303-cpu/ResMerge-release上公开获取。

[阅读原文](https://arxiv.org/abs/2606.02252)

---

## 35. 能力自我评估：教法学硕士了解自己的极限

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haoyan Yang, Reza Shirkavand, Yukai Jin, Jiawei Zhou, Shangqian Gao, Heng Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning approach for teaching LLMs capability self-assessment, directly improving alignment and delegation behavior.

**摘要**: arXiv：2606.00251v1宣布类型：新摘要：认识到自己的局限性并决定是否解决问题或委托的能力是可靠智能系统的基础。然而，我们表明现代大型语言模型系统性地缺乏这种能力：在不同的模型家族和规模中，它们高估了自己的能力，并尝试无法解决的查询。我们将这种能力称为能力自我评估（CSA），并将其描述为一个政策学习问题，旨在改善自我评估，同时保留模型的原始能力。我们的结果表明，强化学习可以有效地教授CSA，在保留原始能力的同时显着优于监督微调。相比之下，有监督的微调会严重降低模型要评估的能力。此外，习得的自我评估行为可以很好地脱离分布，这表明CSA是一种可转移的模型特征。最后，CSA实际上很有用：它改进了推理时的本地云决策，并为训练期间有针对性的数据选择提供信号。

[阅读原文](https://arxiv.org/abs/2606.00251)

---

## 36. 通过专家指导的GRPO实现精确的意向对准VLA空中导航

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tianyang Chen, Wenjun Li, Xin zhou, Yuze Wu, Fei Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EG-GRPO, a novel RL framework for VLA-based UAV navigation that augments online rollouts with expert data to improve intent alignment, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2606.02313v1公告类型：新摘要：视觉-语言-动作（VLA）模型为无人机（UAV）完成由细粒度指令指定的复杂任务提供了一个有前途的端到端范例。然而，标准监督微调（SFT）遭受数据稀缺，有限的推广，以及对细微而复杂的人类意图的监督不力。强化微调提供了一种自然的方法来缓解这些挑战，并通过可设计的反馈使政策行为与人类意图保持一致，但由于在广阔的连续空间中探索效率低下，将其应用于空中导航仍然具有挑战性。为了应对这些挑战，我们为基于VLA的空中导航引入了一个高效的强化学习（RL）框架。其核心是，我们提出EG-GRPO（专家引导的群体相对政策优化），以利用少量专家数据来增强在线部署。此外，我们设计了一个能够并行模拟和推理的异类管道，从而将推出时间缩短了43.5%。在复杂人类意图指定的多项任务中，EG-GRPO将成功率提高到SFT基线的2.13倍，同时将意图对齐性能提高60.9%。这些结果表明，我们的框架可以将空中导航转向精确的意图对准飞行。

[阅读原文](https://arxiv.org/abs/2606.02313)

---

## 37. 经济思考：LLM中适应性复杂性推理的分层框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yubo Gao, Haotian Wu, Hong Chen, Junquan Huang, Yibo Yan, Jungang Li, Zihao Dongfang, Sicheng Tao, Puay Siew Tan, Jie Zhang, Xuming Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hierarchical training framework (HAB) for adaptive-complexity reasoning in LLMs, directly addressing latent reasoning efficiency via step-level token budgeting.

**摘要**: arXiv：2606.01168v1宣布类型：新摘要：思想链（CoT）显着增强了LLM推理，但由于“过度思考”，通常会产生大量计算负担：生成过长的理由而没有相应的准确性提高。现有的效率方法通常应用均匀压缩，这忽视了一个关键观察，即推理复杂性在两个不同的粒度上是异类的：跨不同的问题和单个推理步骤。这激发了我们经济思考的原则：根据内在任务和步骤需求智能地分配计算资源，而不是追求统一的简洁性。我们提出了分层自适应预算（HAB），这是一个通过从粗到细的预算来操作这一原则的训练框架。在步骤间层面，HAB预测每个问题的最佳推理深度。在步骤内级别，HAB从PPL衍生的步骤比较和捕获本地质量效率权衡的自适应帕累托优化目标中学习步骤特定的代币预算信号，而基于Fisher信息的修剪器进一步提供细粒度的训练时间指导，从而鼓励生成器内化更经济的推理模式。GSM 8K和PATH 500上的实验表明，HAB不仅在准确性上超过了标准CoT，而且还减少了代币的使用，实现了比比较基线更强的性能效率权衡。

[阅读原文](https://arxiv.org/abs/2606.01168)

---

## 38. 量化推理模型认为他们需要思考更长时间，但事实并非如此

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sanae Lotfi, Polina Kirichenko, Steven Li, Zechun Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies and mitigates overthinking errors in quantized reasoning models via a training-free logit penalty, directly addressing reasoning efficiency in LLMs.

**摘要**: arXiv：2606.00206v1宣布类型：新摘要：训练后量化（PTQ）被广泛用于高效部署大型语言模型，但其对推理模型的影响尚未得到很好的理解。在数学、编码和科学QA中，我们发现激进的PTQ会降低准确性，同时增加思想链（CoT）长度。令人惊讶的是，我们表明，在高达52%的量化模型失败中，模型在中间推理步骤中得到了正确的答案，但不会将其输出为最终答案。为了理解量化为何会导致过度思考错误的增加，我们测量了量化和全精度输出分布之间的符号级KL偏差。具有高KL分歧的位置与高下一个令牌的熵密切相关，并且在这些位置，量化模型不成比例地采样过度思考的标记，例如“等待”、“但是”和“替代”。我们表明，简单地对一组精心策划的过度思考标记引入免训练的logit惩罚就可以将CoT长度减少12- 23%，同时保留或提高5个模型（1.5B-32 B参数）、3种量化方法和5个基准的准确性，与惩罚其他令牌集相比，产生了有利的帕累托边界。量化模型产生的过度思考错误尤其减少了高达58%。

[阅读原文](https://arxiv.org/abs/2606.00206)

---

## 39. SafeSteer：本地化政策蒸馏，实现高效安全调整

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hao Li, Jingkun An, Zijun Song, Pengyu Zhu, Rui Li, Hao Wang, Wendi Feng, Yesheng Liu, Lijun Li, Jin-Ge Yao, Lei Sha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SafeSteer, a novel RL-based safety alignment method using on-policy distillation confined to safety tokens, achieving strong safety with minimal general capability degradation.

**摘要**: arXiv：2606.02530v1宣布类型：新摘要：将大型语言模型（LLM）与人类价值观保持一致通常会降低它们的一般能力，称为调整税。现有的方法通过平衡双重目标来缓解这种情况，双重目标严重依赖于大量通用数据或辅助奖励模型。   在本文中，我们认为，由于安全特征在输出分布中本质上是稀疏的，因此对齐需要局部修改而不是全局权衡。为此，我们提出了SafeSteer，它只对安全令牌执行政策上的提炼。首先，我们通过激活引导来构建一名安全老师。基于这位老师，我们开发了一种安全令牌选择算法。因此，SafeSteer在训练期间将反向KL惩罚限制在这些代币上，以保留一般能力。   不同模型的实验结果表明，与现有方法相比，我们的SafeSteer在安全性和一般能力之间实现了更好的权衡，在七个安全基准上实现了强大的安全性能，而在五个一般能力基准上的降级仅最小。值得注意的是，SafeSteer仅需要100个有害样本，而不使用任何通用数据，不到之前基线使用的1%，大大降低了对齐成本。更多详细信息请访问我们的项目页面https://anjingkun.github.io/SafeSteer。

[阅读原文](https://arxiv.org/abs/2606.02530)

---

## 40. 通过感知扰动和奖励建模缓解多模式LLM作为法官中的感知判断偏差

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Seojeong Park, Jiho Choi, Junyong Kang, Seonho Lee, Jaeyo Shin, Hyunjung Shim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a GRPO-based reward modeling framework to mitigate perceptual judgment bias in MLLM judges, directly contributing to RL for LLM alignment.

**摘要**: arXiv：2606.02578v1宣布类型：新摘要：最近的多模式大型语言模型已经表现出强大的推理能力，但它们作为自动评估器的可靠性仍然受到一个关键弱点的限制：当视觉证据与文本线索发生冲突时，MLLM法官倾向于奖励合理的叙述而不是感知上正确的答案。我们识别并系统分析这种现象，我们称之为知觉判断偏差。通过受控的视觉扰动，现有的多模式法官经常锚定在响应文本上，而不是他们自己的视觉感知上，导致不一致和不可验证的评估。为了解决这个问题，我们引入了感知受干扰的判断数据集，它构建了最低限度编辑的反事实响应，以隔离感知错误并实现可验证的监督。在此数据集的基础上，我们开发了一个统一的训练框架，该框架将基于GRPO的结构化奖励与批排序目标相结合，在没有明确的成对标签的情况下实现连贯的全球排序。跨各种MLLM作为评委基准的实验表明，我们的方法大大提高了感知保真度、排名一致性以及与人类评估的一致性。我们的结果建立了一种可扩展和可推广的途径，用于训练基于感知、可解释且对视觉推理冲突具有鲁棒性的多模式法官。

[阅读原文](https://arxiv.org/abs/2606.02578)

---

## 41. MemPro：作为可进化程序的大型存储系统

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qingshan Liu, Guoqing Wang, Wen Wu, Jingqi Huang, Xinqi Tao, Dejia Song, Jie Zhou, Liang He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MemPro, a system-level evolution framework for agentic memory that treats the entire memory pipeline as an evolvable program, enabling self-improvement through failure-mode-guided refinement.

**摘要**: arXiv：2606.00619v1宣布类型：新摘要：长视野自治代理需要内存系统保留历史信息、跟踪不断发展的状态并在有限上下文窗口之外重复使用相关知识。现有的代理内存系统通常遵循内存构造-检索（MCR）流水线，但通常主要调整内存库，同时在部署后保持周围流水线固定。这种固定管道设计难以处理异类特定任务的故障模式，并且可能与规模和结构随着时间的推移而演变的存储库不一致。为了解决这些限制，我们提出了MemPro，这是一个系统级进化框架，它将整个MCR管道视为可进化程序，而不是仅调整内存库或提示文本。MemPro维护可运行存储系统实现的版本树，其中进化代理迭代地选择有希望的版本、诊断重复出现的故障，并通过故障模式引导的编辑调试细化创建改进的子版本。LongMemEval、LoCoMo、HotpotQA和NarrativeQA上的实验表明，MemPro在几次迭代内始终优于强大的静态和预算级进化基线，并随着进化而继续改进，并实现了有利的性能成本权衡。代码可在https://github.com/wanghai673/MemPro上获取。

[阅读原文](https://arxiv.org/abs/2606.00619)

---

## 42. 通过约束策略优化进行检测器规避LLM解释

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mingyi Wang, Zhuoer Shen, Yuheng Bu, Shaofeng Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DEPO, a constrained RL algorithm for LLM paraphrasing that uses Lagrangian primal-dual optimization and a GRPO-style update to balance detector evasion with semantic preservation.

**摘要**: arXiv：2606.00392v1宣布类型：新摘要：AI文本检测器很容易受到重述和检测器引导的重述攻击，但现有的检测器规避方法通常缺乏对语义保留的精确控制。特别是，直接优化检测器规避可能会降低细粒度语义，而分级奖励设计仅提供对规避-语义权衡的间接、权重敏感的控制。我们通过将检测器规避LLM解释制定为受约束的马尔科夫决策过程来解决这一局限性，其中检测器规避是主要目标，而语义保留作为显式约束强制执行。我们提出了检测器规避策略优化（DEPO），这是一种拉格朗日原始二元强化学习算法，具有新型的GRPO式基于组的策略更新。DEPO在训练期间自适应地平衡了语义保留和检测器规避，使该策略能够提高规定的语义保留区域内的攻击成功率。针对MAGE、RoBERTa、RADART、双筒望远镜和Fast-DetectGPT检测器进行的MAGE、M4、RADID和同行评审数据集的实验表明，DEPO在精确满足语义保留约束的同时实现了强大的检测器规避。DEPO还展现出跨域、跨检测器和预算级稳健性。

[阅读原文](https://arxiv.org/abs/2606.00392)

---

## 43. 多模态大型语言模型的注意力引导微调改善了思维链推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sanchit Sinha, Guangzhi Xiong, Bohan Liu, Zhenghao He, Aidong Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel attention-guided fine-tuning objective (Att-CoT) that improves CoT reasoning in MLLMs by addressing failure modes like premature answer commitment, directly relevant to RL for LLMs via a new training objective.

**摘要**: arXiv：2606.01558v1宣布类型：新摘要：多模式大型语言模型（MLLM）中思想链（CoT）提示的有效性仍然不确定：在多个视觉推理基准中，与直接提示相比，CoT提示通常会降低性能。在本文中，我们在需要分步视觉证据的数据集上对三个现代MLLM家族的CoT行为进行了系统分析。我们的分析确定了两种反复出现的失败模式：过早的答案承诺和原理生成期间的直接视觉令牌访问有限。我们进一步发现，标准的CoT风格监督微调（CoT-SFT）只能部分缓解这些问题，同时通常增加对文本先验的依赖并减少反事实视觉依赖。受这些发现的激励，我们提出了Attentive-CoT（Attentive-CoT），这是一个注意力引导的微调目标，鼓励CoT轨迹推迟答案承诺，同时保持持续的视觉令牌访问。Att-CoT可以插入任何CoT-SFT培训运行，无需进行架构更改。针对六个MLLM的三个视觉推理基准进行的实验表明，Att-CoT比标准微调增强了CoT的性能。

[阅读原文](https://arxiv.org/abs/2606.01558)

---

## 44. ARCA：代币信号退化时的适配器剩余信用分配

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Rodney Lafuente-Mercado

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ARCA, a novel credit assignment method for LLM RL with LoRA that uses adapter hidden-state residuals to avoid degenerate token signals, directly addressing a structural failure mode in RL for LLMs.

**摘要**: arXiv：2606.00257v1宣布类型：新摘要：语言模型强化学习的令牌级信用分配通常被制定为好像策略是完全可训练的，而实际的LLM-RL管道通常依赖于参数高效的微调，尤其是LoRA。我们认为这种分离隐藏了结构性失效模式。在LoRA下，政策被限制在参考模型的低等级邻居，因此常见的内在信用信号、附加值、熵约减和政策分歧使用的每代币输出分布差异可能会在轨迹内正规化后退化，要么接近统一的权重，要么集中在一小群任务不可知的位置上。我们将这种行为形式化，并建议通过体重基尼和有效代币比率等浓度诊断直接测量它。然后，我们引入\{Adapter-Residential Credit Assign}（ARCA），这是一种轻量级替代方案，它从适配器自己的隐藏状态剩余中推导出令牌显着性，$\|h^{\text{base}}_t\|_2$。ARCA询问适配器实际改变模型的位置，而不是输出分布在哪里看起来不确定或发生变化，并且不需要学习奖励模型、价值头或树构建。在紧凑的MAT/Qwen 3 -1.7B GRPO扫描中，ARCA在匹配的推出预算下展示了预测的非退化中间制度信用分布，并且与排名匹配的基线保持竞争力。

[阅读原文](https://arxiv.org/abs/2606.00257)

---

## 45. 多模式大语言模型空间推理中空间词汇偏差的机械诊断

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chuang Ma, Qianying Liu, Tomoyuki Obuchi, Fei Cheng, Wang Yang, Sudong Cai, Shuyuan Zheng, Akiko Aizawa, Sadao Kurohashi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a DPO-based LLM-only update to mitigate spatial lexical bias in MLLMs, directly aligning with RL for LLMs via preference optimization.

**摘要**: arXiv：2606.01914v1宣布类型：新摘要：多模式大型语言模型（MLLM）在空间多项选择题上仍然不可靠，其失败通常归因于视觉信息关注不足。在这项工作中，我们确定了一种补充的失败模式，即空间词汇偏见：在答案选项中添加空间关系词可以吸引模型的决策，并使新添加的选项有可能被选择。使用九个开重MLLM，我们表明这种现象被广泛观察到。特别是，模型可以正确回答二元空间问题，但一旦将其添加到答案集中，就会始终选择错误的第三个空间选项。我们将此类二元稳定但二元脆弱的病例隔离为诊断示例，并利用机械解释工具，揭示了很大一部分失败源于语言方面而不是视觉方面：视觉注意力分析和剩余流探测表明，在这些故障中，正确的空间关系仍然在内部可用，而不相关的选项控制、激活补丁、稀疏成分干预追踪对特定LLM侧通道和神经元的偏见。基于这一发现，我们表明，对微小的单对象对合成数据进行轻量级的仅LLM DPO更新可以减轻偏差，将合成数据上的四向鲁棒准确性提高了多达100个点，在更广泛的评估数据集上提高了68.0、32.6和20.1个点WhatsUp、SpatialMQA-Direct和VSR。

[阅读原文](https://arxiv.org/abs/2606.01914)

---

## 46. 演员：GRPO优势翻转的非特权剪辑不对称自学

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yang Li, Gongle Xue, Yijia Guo, Yuheng Yuan, Liwen Hu, Lei Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CAST, a novel self-distillation method for GRPO-style RLVR that provides dense token-level advantages and addresses zero-variance group issues, directly improving RL for LLM reasoning.

**摘要**: arXiv：2606.00172v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR），特别是组相对策略优化（GRPO），已被广泛用于改进大型语言模型中的推理。然而，结果级奖励仅提供稀疏的监督，当提示的所有采样轨迹正确或不正确时，群体相对优势就会消失。按政策自蒸馏（OPSD）提供密集的代币级指导，但其代币偏好不一定与轨迹正确性一致;经验诊断表明，OPSD信号在正确和不正确的推出时表现不同，教师积极和教师消极的差距信号表现出不同的噪音轮廓。这些诊断是在OPSD风格的特权教师环境下进行的，仅用于分析，而AST培训使用无答案的自学评分。在这些观察的启发下，这项工作提出了AST，这是一种用于GRPO风格WLVR的无答案自我提炼方法。AST保留了基于验证者的GRPO目标，但使用停止梯度自学来根据轨迹正确性塑造代币级优势。与之前的自我提炼的RL VR方法不同，AST不需要参考解决方案条件的教师评分，在整个培训过程中保持自我教师的日志概率差距，并应用双向局部优势符号逆转：正确轨迹中的教师负代币可以获得负代币水平优势，而错误轨迹中的教师正代币可以获得有限的正局部优势。对于零方差全正确和全错误的组，AST分配有界符号约束的基本优势，因此这些原本为零梯度的组可以贡献验证者签名的令牌反馈。数学推理实验表明，AST改进了WLVR训练，同时保留了轻量级、基于验证器的实验室级目标。

[阅读原文](https://arxiv.org/abs/2606.00172)

---

## 47. CARE-RL：用于缓解跨领域冲突的能力感知强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Rui Zhang, Xinle Wu, Yao Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CARE-RL, a novel RL framework combining a protocol-aware generative reward model for non-verifiable tasks and a capability-aware optimization method to mitigate cross-domain conflicts in multi-domain LLM training.

**摘要**: arXiv：2606.00609v1宣布类型：新摘要：具有可验证奖励的强化学习（RL）在面向推理的LLM中取得了强劲进展，但由于不可验证任务中的奖励不可靠性和跨领域的能力干扰，将其扩展到多领域RL仍然具有挑战性。我们提出CARE-RL将协议感知奖励生成与功能感知优化相结合，以减轻跨域冲突。对于不可验证的任务，协议感知生成奖励模型（PA-GRM）在产生轨迹条件奖励之前构建预算级评估协议和模式，从而能够对开放式响应进行任务自适应但具有可比性的评估。对于多域优化，方向感知能力子空间投影（DACSP）从之前的RL阶段中提取历史能力方向，并通过放大对齐分量、抑制冲突分量和保留垂直更新来调制后续更新。数学、聊天和描述遵循基准的实验表明，CARE-RL始终优于标准的多领域RL基线，在Qwen 2.5 - 7 B和Qwen 3 - 4 B上分别实现了47.9和50.7的总平均得分。

[阅读原文](https://arxiv.org/abs/2606.00609)

---

## 48. RDA：强化学习的奖励设计代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hojoon Lee, Ajay Subramanian, Ben Abbatematteo, Vijay Veerabadran, Pedro Matias, Karl Ridgeway, Nitin Kamra

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a VLM-based agentic framework (RDA) that iteratively designs and refines reward functions for RL, directly matching the RL for LLMs criterion on reward design.

**摘要**: arXiv：2606.01672v1宣布类型：新摘要：强化学习使人们能够获得令人印象深刻的机器人技能，但通常需要手工制作的奖励功能，这些功能设计缓慢且难以与人类意图保持一致。最近的工作（例如Eureka）通过使用LLM从任务描述中迭代生成和完善奖励代码来自动化奖励设计。然而，它们依赖于成功率等粗略的反馈信号，而这些信号几乎没有对学习行为提供语义洞察。因此，他们训练有素的政策实现了最终目标，但通常与任务指令不一致。我们引入了奖励设计代理（RDA），这是一个基于LMA的代理框架，可以将语义理解注入到奖励设计中。RDA分解任务、可视化评估轨迹、总结失败模式并迭代修改奖励代码以更好地与任务指令保持一致。在ManiSkill的12项桌面操作任务和HumanoidBench的4项全身操作任务中，RDA生成的策略比其他基线的策略更加符合预期，同时实现了相当的任务成功率。视频和生成的奖励代码可在https://nitinkamra1992.github.io/reward-design-agent上获取。

[阅读原文](https://arxiv.org/abs/2606.01672)

---

## 49. SkillRevise：通过跟踪条件技能修订提高法学硕士作者的代理技能

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuxuan Liu, Zhaochen Su, Lingyun Xie, Yuhao Zhang, Qing Zong, Jiahe Guo, Zhongwei Xie, Yiyan Ji, Yauwai Yim, Hongyu Luo, Xiyu Ren, Ruan Chenyu, Haoran Li, Yangqiu Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SkillRevise, a self-improving agent framework that iteratively refines agent skills using execution traces and a repair memory, showing measurable capability gain.

**摘要**: arXiv：2606.01139v1宣布类型：新摘要：代理技能是程序性产品，使LLM代理能够执行工作流程、验证约束并从故障中恢复。现有的自我进化方法使用积累的轨迹来完善技能。然而，他们在冷启动环境中挣扎，那里只有一个初始的，不完美的技能。因此，技能构建默认为专家创作或一次性LLM生成。专家编写的技能成本很高，可能与LLM代理实际执行任务的方式不一致，而一次性生成的技能可能在语法上很好，但在行为上很弱。为了弥合这一差距，我们提出了SkillRevise，这是一个基于执行的框架，旨在迭代地完善这些初始技能。SkillRevise根据执行证据诊断技能缺陷，从通用记忆中检索相关修复原则，并应用执行锚定编辑。通过重新执行候选人并衡量经验效用，它系统性地保留最佳技能版本。经过三个基准和五个LLM的评估，SkillRevise的表现大大优于一次性基线，将基本代理在SkillsBench上的成功率从36.05%提高到61.63%。此外，修改后的技能表现出强大的跨模型可移植性，可以捕获一般化的程序知识而不是特定于模型的工件。

[阅读原文](https://arxiv.org/abs/2606.01139)

---

## 50. 形式数学验证中生成性奖励模型的期望值对齐

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shihao Ji, Haotao Tan, Zihui Song, Mingyu Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Expected Value Alignment (EVA), a novel generative reward modeling procedure that extracts continuous scores from token logits for process reward models in formal math verification, directly addressing RL reward design.

**摘要**: arXiv：2606.01160v1宣布类型：新摘要：大型语言模型（LLM）越来越多地与Lean 4等正式交互式定理证明器一起使用。使用强化学习或搜索方法扩展这些系统需要能够评估中间推理步骤的流程奖励模型（PRM）。现有的奖励模式设计暴露了实际的权衡。价值头部模型提供连续分数，但修改了生成模型界面，而生成奖励模型保留了文本原理，但与连续浮点回归的匹配性较差，因为数字值在代币之间分裂。我们引入了期望值对齐（伊娃），这是一种奖励建模过程，可以保持表面输出的离散性，同时从模型的代币分布中提取连续分数。该模型以结构化的SON格式发出整分数，而伊娃计算连续分数作为对相应锚令牌logits的期望。训练将因果语言建模目标与这些预期值的辅助均方误差损失相结合。我们在\textit{Leibniz}（Lean 4正式验证的奖励模型）中实例化了伊娃，并根据零射击和奖励建模基线对其进行评估。评估表明，基于日志的连续评分显着减少了离散化伪影，同时保留了生成性批评的可解释性。

[阅读原文](https://arxiv.org/abs/2606.01160)

---

## 51. 经验更好：自我发展的LLM代理，以循证健康社区笔记

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zihang Fu, Fanxiao Li, Jianyang Gu, Haonan Wang, Preslav Nakov, Bryan Hooi, Min-Yen Kan, Jiaying Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving LLM agent framework (EvoNote) that improves health Community Notes generation via an evolving experience memory and fine-grained credit assignment.

**摘要**: arXiv：2606.02215v1宣布类型：新摘要：大型语言模型（LLM）-增强的社区注释提供了一种可扩展的路径，用于及时、基于证据的纠正社交平台上的健康错误信息。然而，它们仍然在每个职位上重置，留下了之前案例中有用的纠正经验。我们引入EvoNote，这是一个代理框架，使健康社区注释的生成能够通过先前错误信息纠正事件的不断发展的经验记忆来自我发展。其核心是细粒度的信用分配：EvoNote将专家级反馈纳入特定健康的笔记质量，并将其提炼为行动级记忆，以进行主张分析、证据获取和笔记撰写。我们在MM-HealthCN上评估了EvoNote，MM-HealthCN是一个1.2K实例的多模式基准，包含用户标记的健康帖子，带有人工编写的社区注释和人群衍生的帮助标签。在经过人类验证的分层效用判断下，在89.6%的案件中，EvoNote生成的笔记比相应的人类书写的笔记更受青睐;在一组单独的、没有群体帮助判断的“需要更多评级”帖子中，EvoNote为82.0%的案件生成有用的笔记。它还将生成候选修正所需的平均时间从人类笔记管道中的13小时以上减少到2分钟以下。分析将这些成果与更强有力的证据使用和可重复使用的纠正策略联系起来，将自我进化的笔记生成定位为健康错误信息治理的一个有希望的范式。

[阅读原文](https://arxiv.org/abs/2606.02215)

---

## 52. 沙盒编码代理是有竞争力的全模式任务解决器

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dongping Chen, Xuanao Huang, Zhihan Hu, Qingyuan Shi, Dianqi Li, Tianyi Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Code-X, a training recipe with verifiable reward for coding agents, directly matching RL for LLMs via verifier-driven optimization and self-improvement.

**摘要**: arXiv：2606.00579v1宣布类型：新摘要：随着多模式LLM越来越多地针对视频和音频，人们通常认为此类任务需要原生的多模式模型。我们表明，情况并非总是如此：仅具有文本+图像访问和沙箱工具使用界面的编码代理可以匹配，并且在某些设置中优于跨多个音频-视频基准的SOTA原生全模式模型和预定义的多模式代理支架。我们的轨迹分析表明，它们的优势来自编写代码和编排工具，从笔录、帧和其他形态信号中提取相关证据，从而将全模式任务转化为检索和信息处理问题，而不是吞下整个媒体流。我们通过故障分类和流程级跟踪分析进一步描述了它们的局限性，并表明简单的技能注入（包括人工编写和自我提炼的技能）可以极大地提高性能。为了探索开源启发，我们引入了Code-X，这是一种具有OmniCoding轨迹数据集和可验证奖励的训练食谱，并提供了Qwen-3.5- 9 B和Qwen-3.6- 27 B的基线。最后，我们认为下一个前沿是多模式处理，并引入TerminalBench-O，这是一个用于现实世界全模式处理任务的流程级基准。代码可在https://github.com/Dongping-Chen/OmniCoding上获取。

[阅读原文](https://arxiv.org/abs/2606.00579)

---

## 53. 通过意识落后的组规模调整更快的同步政策RL

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Azal Ahmad Khan, Ammar Ahmed, Zeshan Fayyaz, Sheng Di, Mingyi Hong, Ali Anwar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dynamic group-size controller for synchronous on-policy RL (GRPO/DAPO) that mitigates straggler issues, directly improving RL training efficiency for LLMs.

**摘要**: arXiv：2606.02218v1宣布类型：新摘要：群相对政策优化（GRPO）等同步强化学习方法提供稳定且可重复的政策训练，但它们极易受到掉队者的影响，单一异常长的推出可能会延迟整个群体的奖励计算和参数更新。随着群组规模的增加，这个问题变得更加严重，导致更大群组的好处与同步的时钟成本之间出现紧张关系。我们提出了离散感知组控制（SAGC），一个动态的组大小控制器，适应训练组在线观察到的推出行为的基础上。SAGC制定组大小选择作为一个在线约束优化问题，寻求保留较大的群体的好处，同时控制长期率的掉队事件。在同步GRPO和DAPO培训中，以及在常规和强大的工程基线之上，SAGC始终降低了掉队者的发生率，提高了挂钟效率，同时实现了有竞争力或更好的培训回报。我们进一步表明，这些收益转移到最终的模型质量：SAGC是竞争力或优于最强的静态组大小基线下游推理基准，并经常产生较短的输出没有任何显式的长度惩罚。这些结果将动态组控制定位为使同步按策略RL更加高效和稳健的实用方法。

[阅读原文](https://arxiv.org/abs/2606.02218)

---

## 54. SDR：放射学报告生成的设定距离奖励

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Halil Ibrahim Gulluk, Max Van Puyvelde, Wim Van Criekinge, Olivier Gevaert

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes set-distance rewards for RL-based post-training of VLMs for radiology report generation, directly matching the RL for LLMs criterion with a novel reward design.

**摘要**: arXiv：2606.00440v1宣布类型：新摘要：具有可验证奖励的强化学习迅速推进了视觉推理--语言模型。然而，对于胸部X光报告生成来说，标准奖励（即精确匹配准确性和分步过程）是不兼容的，因为报告由无序和垂直的发现组成，而不是因果推理链。我们通过基于集合的视图来解决这个差距：每个报告都被拆分成句子，并通过冻结句子Transformer嵌入，从而产生无序的嵌入集。我们建议使用生成的嵌入和引用嵌入之间的集到集距离作为连续的、排列不变的奖励。在两个数据集和三个视觉语言模型（Qwen 3-BL-2B/4 B、Gemma 3 - 4 B）中，通过GRPO进行基于集到集距离的奖励的后训练在所有标题指标上始终优于监督式微调和精确匹配GRPO（BERTScore、RadShape F1和CheXbert F1分别平均相对提高了6.80、7.82和4.45）。相同的设置距离还可以实现测试时最佳N$选择：根据候选人与训练报告嵌入的距离对候选人进行评分优于我们训练模型以及三个闭源LLM（Mistral-Small、Gemini-2.5 Flash-Lite、GPT-4 o-mini）的随机选择，BERTScore平均相对提高16.4。用作流媒体信号，它们支持一种更有效的测试时间扩展形式：在中代修剪低评分候选项将生成的令牌减少了50%以上，同时保留了完全N$中最佳选择的结果质量。这些结果共同建立了设定距离奖励作为胸部X射线报告生成中训练后和测试时间缩放的统一信号。我们的代码是公开的\href{https：//anonymous.4open.science/r/Set-Distance-Rewards-CXR-BFDA}{可用}。

[阅读原文](https://arxiv.org/abs/2606.00440)

---

## 55. MMG 2技能：特工能否将野外向导提炼为自我进化的技能？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xinyu Che, Junqi Xiong, Yunfei Ge, Xinping Lei, Shihao Li, Hang Yan, Han Li, Yuanxing Zhang, Zhiqi Bai, Jinhua Hao, Ming Sun, Han Li, Jiaheng Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a closed-loop framework for self-evolving agents that distill in-the-wild guides into executable skills and improve them via trajectory-driven revision.

**摘要**: arXiv：2606.01993v1宣布类型：新摘要：Web上丰富的程序知识对于帮助代理解决长期任务具有巨大潜力。然而，此类知识通常是多模式、异类、嘈杂的，并且隐含地假设为人类执行者，因此很难直接用作代理所需的技能。为了弥合以人为本的向导和代理可执行技能之间的差距，我们将这个问题形式化为向导到技能学习：将野外向导转化为可执行技能，并从代理可观察的轨迹不断改进它们。为了评估现有代理在此任务上的能力，我们引入了MMG 2 Skill-Bench，这是为此问题设计的第一个基准。我们进一步提出MMG 2 Skill，这是一个闭环框架，可以将指南编译为可编辑技能，在执行期间对这些技能进行固定的视觉语言模型（VLM）代理进行条件，并在不使用基准分数的情况下根据专家级根本原因反馈修改技能。在图形用户界面控制、开放式游戏玩法和具有六个VLM主干的战略卡牌玩法方面，MMG 2 Skill在每个模型域设置中始终优于普通基线代理，在主干之间实现了+12.8至+25.3个百分点的宏观平均收益。消融研究表明，用原始指南直接提示代理可能会降低性能，而结构化技能构建和教师驱动的修订对于观察到的改进来说都是必要的。在可成功推断的任务中，基于分析器的早期停止可以进一步防止后期性能退化，并在成功信号得到正确校准时节省25%-53%的尝试。

[阅读原文](https://arxiv.org/abs/2606.01993)

---

## 56. 像鸽子一样主动探索：通过抽象视觉语言模型加强空间推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wei Deng, Xianlin Zhang, Mengshi Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel agentic pipeline for spatial reasoning in VLMs using dynamic cognitive maps and Spatial Assertion Codes for dense reward signals, optimized via RL finetuning.

**摘要**: arXiv：2606.02459v1 Announce Type：new摘要：使视觉语言模型（VLM）能够执行空间推理仍然具有挑战性。现有的方法处理VLMs作为被动的观察者，这是很难在现实世界中的应用。此外，强化学习方法依赖于稀疏奖励，限制了它们在复杂推理任务中的有效性。受鸽子构建和利用认知地图进行导航的启发，我们提出了一种新的空间推理代理管道。首先，我们引入了一个新的动态认知地图参数化场景布局的对象的位置和方向，作为新的观察持久的记忆。其次，我们提出了一种新的\n {空间断言代码（SAC）}，Python表达式编程描述空间关系。通过与动态认知地图合作，SAC能够验证中间推理步骤，提供密集的奖励信号。我们通过监督和强化微调来优化模型。MindCube基准测试上的实验证明了最先进的性能，具有总体准确性，在具有挑战性的\ttexc {Rotation}子集上比当前最佳方法高出\ttexc {29.5}个准确度点（相对改进\ttexc {53.2\%}）。我们的代码和数据在https://github.com/dw-dengwei/active-spatial-reasoning.git上开源。

[阅读原文](https://arxiv.org/abs/2606.02459)

---

## 57. 通过近未来指导弥合政策上蒸馏中的推理轨迹

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuxuan Jiang, Francis Ferraro

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new on-policy distillation method for LLM reasoning that uses near-future trajectory information to improve token-level supervision, directly addressing a core limitation in RL-based reasoning training.

**摘要**: arXiv：2606.00305v1宣布类型：新摘要：政策上蒸馏（OPD）通过在教师监督下根据自己的政策采样的轨迹训练学生模型来改进大型语言模型推理。尽管OPD按照轨迹运行，但其学习信号仍然是代币级别的：它通过高损失代币识别偏差，并通过本地反向KL修正修复它们。我们表明，这种“随机抽样但符号学习”的机制无法可靠地将学生轨迹与教师轨迹联系起来。大约30%的高损失代币属于低分歧机制，这表明许多代币是表面形式的错配，而不是真正的推理叉。此外，即使是真正不同的代币也很难通过孤立的代币级监督来修复，因为推理失败通常表现为短期分布漂移。我们提出了轨迹感知OPD（TOPD），它使用近未来轨迹信息来识别真实的不同状态并在多个未来代币之间分发指导。实验表明，抑制非分歧高损失代币将标准OPD的平均准确率从47.8%提高到48.2%，而TOPD将性能进一步提高到52.2%，AIME 24的平均准确率从60.0%提高到63.3%，AIME 25的平均准确率从46.7%提高到53.3%。

[阅读原文](https://arxiv.org/abs/2606.00305)

---

## 58. SPADER：分步同行优势，具有多元化意识的探索奖励，多答案问题解答

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qiming Shi, Zhaolu Kang, Yunfan Zhou, Di Weng, Yingcai Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SPADER, an RL framework with step-level credit assignment and diversity-aware rewards for multi-answer QA, directly matching RL for LLMs and agent self-improvement criteria.

**摘要**: arXiv：2606.00593v1宣布类型：新摘要：大型语言模型越来越多地被部署为工具增强代理，以获取参数知识之外的信息。虽然最近的工作改进了长期工具使用推理，但大多数方法都专注于具有单一正确答案的任务。相比之下，许多现实世界的查询需要发现一组全面的有效答案，这种设置称为多答案QA。这种设置提出了两个挑战：长搜索轨迹上的细粒度信用分配，以及在简单高频实体之外进行持续探索的奖励一致。我们提出SPADER，这是一个强化学习框架，用于在多答案QA中长期使用工具。SPADER包括分步同行优势（SPA），这是一种无批评的分步级信用分配机制，可通过决策步骤对齐平行轨迹，并估计同行回报的优势。它还包括具有多样性意识的探索奖励，通过提高罕见发现的权重和降低冗余发现的权重来促进长尾实体的发现。QAMPARI、Mintaka、WebQSP和QUEST的实验表明，SPADER总体上比基于预测的代理、结果监督的RL方法和最近的分步监督方法提高了召回率和总体F1。我们的代码和模型权重可在https://github.com/KhanCold/spader上获取。

[阅读原文](https://arxiv.org/abs/2606.00593)

---

## 59. AgentPLM：具有用于蛋白质序列设计的推理增强解码的抽象蛋白质语言模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sahil Rahman, Maxx Richard Rahman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving agentic protein language model that uses reasoning-augmented decoding and trajectory-level RL (CAPO) to learn from biophysical oracle feedback.

**摘要**: arXiv：2606.02386v1宣布类型：新摘要：蛋白质语言模型（PLM）是被动的预言：它们在单次正向传递中生成序列，没有机制在候选者违反热力学或结构约束时咨询外部生物物理反馈或重定向生成。我们引入了AgentPLM，它通过为预训练的PLM配备i）推理增强解码（RAD）来解决这个问题，它将自回归生成与工具调用交织在一起（ESFold、FoudX、AutoDock Vina），以及ii）对比代理策略优化（CAPO），直接偏好优化的子公司级扩展，可以端到端训练策略来学习Oracle反馈何时提供信息，而不仅仅是模仿高-健身序列。我们评估AgentPLM的基准任务，涵盖从头酶设计、抗体优化、热稳定性、PPI界面设计以及使用标准化Oracle API和受控序列身份分裂的零射击适应度预测。AgentPLM实现了最先进的结果，抗体命中率比最强的被动基线提高了10%，提供了无需明确回溯的在线错误纠正的机械证据。

[阅读原文](https://arxiv.org/abs/2606.02386)

---

## 60. MT-EditFlow：通过流匹配进行多圈图像编辑的强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiahui Huang, Yasi Zhang, Tianyu Chen, Shu Wang, Jianwen Xie, Oscar Leong, Mingyuan Zhou, Nanzhu Wang, Ying Nian Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning framework (GRPO/NFT-based) with multi-reward formulation for multi-turn image editing, directly addressing RL for LLM-like generative models.

**摘要**: arXiv：2606.01985v1宣布类型：新摘要：基于描述的图像编辑最近的突破引起了人们的广泛关注，因为模型现在能够以日常用户所需的实用性来处理现实世界的编辑需求。然而，主要为单轮编辑而训练的编辑模型经常在多轮编辑中崩溃--这是一种自然的交互式设置，用户根据模型自己之前的输出迭代地细化图像。这种失败源于全有或全无要求，即一次失败的转弯会损害整个序列，以及错误传播，即曝光偏差会导致复合编辑错误。为了应对这些挑战，我们引入了MT-EditFlow，这是一个流匹配强化学习框架，旨在优化顺序图像编辑的奖励信号。MT-EditFlow将多回合视角与多回报公式集成，以提供适用于GRPO和基于NFT的强化学习方法的统一结构。我们通过研究回合级聚合的有效评分策略、权衡奖励偏差和方差的VLM推理模式以及防止奖励黑客攻击的优势融合水平来系统地分析和优化奖励信号。我们的研究结果表明，在整个编辑轨迹中传播聚合优势有效地弥合了本地规划和全球多回合任务成功之间的差距。大量实验表明，MT-EditFlow显着提高了不同基本模型的性能。值得注意的是，它将FLOX.1-Kontext-dev的整体性能提升了6.85分-3，超越了Qwen-Image-Edit等最先进的开源模型。通过保持高的边际成功率和减少曝光偏差，MT-EditFlow为视觉内容创建中更可靠、更自然的人机协作提供了基础。

[阅读原文](https://arxiv.org/abs/2606.01985)

---

