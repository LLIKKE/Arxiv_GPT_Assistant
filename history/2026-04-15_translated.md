# 💡 今日研究速览 (Daily Summary)

# LLM的强化学习
今天的研究表明，使用强化学习（RL）作为引导和改进LLM行为的主要引擎是一种强大的融合，并且明显倾向于更复杂、高效和可验证的奖励机制。一个关键突破是从简单的基于结果的奖励转向密集的、面向过程的信号。* * OOM-RL **等方法引入了不可破解的、市场驱动的目标，而**CPMI**和**MISE**则专注于可扩展的、自动标记步骤级奖励和校准的事后自我评估。为了解决长推理链中信用分配的核心挑战，提出了**Entropy-Aware Policy Optimism（EAPO）**、**Rollout-Tree Monte Carlo（RTMC）**和**SCOPE** 的信号校准监督等新颖技术。此外，效率是一个主要问题，**低等级优化轨迹建模**旨在加速RL训练，而**你只能判断一次** 实现高效的多响应奖励建模。共同的方向是走向更具可解释性、稳定性并能够优化复杂的多步骤行为（例如谈判、工具使用和结构化生成）的RL框架。

# 自我改进和进化的代理人
该领域正在迅速发展为能够在无需人类干预的情况下迭代自我改进的完全自主系统。该范式正在从静态代理转向通过经验进化的动态学习实体。* * ReflectiChain **、**EE-HCP**和**Mem$#392$Evolve**等框架通过整合自动化环境生成、体验银行和协同进化能力扩展的机制来实现这一目标。至关重要的是，这种自我改进通常是由RL循环驱动的，正如用于自主医学研究的**Camyla**和用于生产中持续模型细化的**Pioneer Agent**系统所示。该能力的最终测试由**Agent ' 2 RL-Bench** 进行基准测试，该测试评估LLM代理是否可以自主设计RL管道以改进基础模型。这个方向指向的未来，代理不仅仅是工具，而且是有弹性的、自适应的系统，可以从交互中学习、诊断故障并在闭环中管理自己的训练数据。

# 潜在推理和计算效率
一个重要的目标是将明确、冗长的思想链推理转变为更紧凑、潜在和高效的计算形式。目标是保留或提高推理质量，同时大幅减少内存和计算负担。* * 循环推理语言模型 **和**内省扩散语言模型** 等架构从根本上改变了模型的计算图，以实现潜在空间中的迭代细化。* * MEMEMENTO **等补充方法教LLM将推理块压缩为密集状态摘要，**ZoomR**和**CASK** 提出了复杂的KV缓存压缩技术，可以保护核心推理痕迹。* * 变形金刚在上下文中学习潜在混合模型 ** 等工作强化了理论基础，该工作揭示了注意力层中已经存在的潜在计算机制。这种集体努力旨在通过内化该过程，从代币级叙事转向潜伏状态进化来解锁更深层次、更有效的推理。

# 多模式和条件推理
研究将RL和潜在推理范式扩展到多模式和体现领域，重点关注视觉、物理和交互环境中的模型行为。核心挑战是将模型决策锚定到感官输入以减轻幻觉。* * MedLVR **和**Visual Enhanced Depth Scaling**等框架采用潜在状态细化来进行视觉问题回答，而**V-STAR** 使用分层视觉注意力奖励来显式地将推理与像素联系起来。在具体化环境中，**OOWM**通过使用基于结果的RL优化的面向对象的编程世界模型来构建规划，而**AIM**利用自提炼的RL来生成机器人动作。趋势是走向统一的政策，可以在复杂的多模式状态空间内推理和行动，使用RL将代理人的内部推理过程与物理或视觉世界的外部可验证约束保持一致。

# 专业RL框架和应用程序
今天的产出包括大量为小众但关键的应用程序设计的高度专业化的RL框架，展示了RL作为微调工具的多功能性。这些方法通常引入新颖的奖励设计来解决特定领域的模糊性或优化挑战。例如，**CSPO**为结构化LaTeX生成理清了特定于组件的奖励，**ASPIRin**通过动作空间投影优化语音LM中的回合转换，**Policy Split**使用双模式信息量规则化来鼓励在开放式任务中进行多元化探索。其他作品，例如用于终身模型编辑的**HiEdit**和用于物理一致3D生成的**PhyMix** 的Scene-GRPO，展示了RL对模型行为执行精确、自适应控制的能力。这种专业化标志着该领域的成熟，RL不再是一种钝器，而是一种用于将LLM与复杂的现实世界目标保持一致的精确工具。

---

## 1. OOM-RL：基于LLM的多智能体系统的资金外强化学习市场驱动的调整

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Kun Liu, Liqun Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces OOM-RL, a novel RL alignment paradigm for LLM-based multi-agent systems using financial market penalties as an objective, un-hackable reward signal.

**摘要**: arXiv：2604.11477v1宣布类型：新摘要：用于自主软件工程的多智能体系统（MAS）的对齐受到评估者认识不确定性的限制。当前的范式，例如来自人类反馈的强化学习（RL HF）和人工智能反馈（RLAIF），经常会导致模型谄媚，而基于执行的环境则会遭受不受约束的代理的对抗性“测试逃避”。在本文中，我们引入了一种客观对齐范式：\textBF{超出金钱的强化学习（OOM-RL）}。通过将代理人部署到实时金融市场的非稳定、高摩擦现实中，我们将临界资本枯竭作为不可破解的负梯度。我们为期20个月的纵向实证研究（2024年7月至2026年2月）记录了该系统从高周转率、阿谀奉承的基线到强大、流动性意识的架构的演变。我们证明，财务损失的不可否认的实体论后果迫使MAS放弃过度匹配的幻觉，转而采用\textBF{严格测试驱动统计工作流程（STSYS）}，该流程强制执行受拜占庭启发的单向状态锁（RO-Lock），锚定到确定性验证的$\geq 95\%$代码覆盖约束矩阵。我们的结果表明，虽然早期迭代遭受了严重的执行衰退，但最终的OOM-RL对齐系统在其成熟阶段实现了稳定的平衡，年化夏普率为2.06。我们的结论是，用严格的经济惩罚取代主观的人类偏好，为在高风险的现实世界环境中协调自治代理提供了一种稳健的方法论，为计算计费充当客观物理约束的广义范式奠定了基础

[阅读原文](https://arxiv.org/abs/2604.11477)

---

## 2. ClawGUI：用于培训、评估和部署GUI代理的统一框架

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Fei Tang, Zhiqiong Lu, Boxuan Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a unified GUI agent framework with ClawGUI-RL, featuring an open-source RL infrastructure with a Process Reward Model for dense step-level supervision, directly contributing to RL for LLMs and self-improving agents.

**摘要**: arXiv：2604.11784v1宣布类型：新摘要：图形界面代理通过其视觉界面而不是编程API驱动应用程序，通过点击、滑动和击键与任意软件交互，到达基于CLI的代理无法到达的应用程序长尾。然而，这一领域的进展与其说是建模容量的阻碍，不如说是缺乏一致的全栈基础设施：在线RL训练受到环境不稳定和封闭管道的影响，评估协议在工作中悄然漂移，训练有素的代理很少接触到真实设备上的真实用户。我们介绍了\textBF{ClawGUI}，这是一个开源框架，可以在单个工具中解决这三个差距。\textBF{ClawGUI-RL}提供了第一个开源图形用户界面代理RL基础设施，对并行虚拟环境和真实物理设备都有经过验证的支持，将Giovel与流程奖励模型集成，以实现密集的步骤级监督。\textBF{ClawGUI-Eval}在6个基准和11个以上型号中强制执行完全标准化的评估管道，相对于官方基线实现了95.8%的复制率。\textBF{ClawGUI-Agent}通过12个以上具有混合CLI-GUI-GUI-Agent控制和持久个性化内存的聊天平台将训练有素的代理带到Android、HarmonyOS和iOS中。经过此管道内的端到端培训，\textBF{ClawGUI-2B}在ALEWorld GUI-Only上实现了17.1%的成功率，比同规模MAI-UI-2B基线高出6.0%。

[阅读原文](https://arxiv.org/abs/2604.11784)

---

## 3. 从布局到轨迹：LLM驱动的供应链弹性世界模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jia Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-improving agent framework (ReflectiChain) with a Retrospective Agentic RL mechanism for autonomous policy evolution, directly matching self-evolving agents.

**摘要**: arXiv：2604.11041v1公告类型：新摘要：在全球地缘政治动荡中，半导体供应链面临前所未有的弹性挑战。传统的大语言模型（LLM）规划者在面对这种非平稳的“政策黑天鹅”事件时，由于缺乏物理环境建模，经常遭受决策瘫痪或严重的接地间隙。本文介绍了ReflectiChain，这是一个为弹性宏观经济供应链规划量身定制的认知代理框架。核心创新在于由生成世界模型驱动的潜在轨迹排练的集成，该模型将行动中的反思（系统2审议）与延迟的行动反思结合起来。此外，我们利用回顾性抽象RL机制来实现部署阶段（测试时）的自主策略演变。对我们的高保真基准Semi-Sim进行的评估表明，在出口禁令和材料短缺等极端情况下，ReflectiChain的平均步距奖励比最强的LLM基线提高了250%。它成功地将可操作率（OR）从不足的13.3%恢复到88.5%以上，同时确保稳健的梯度收敛。消融研究进一步强调，物理基础约束和双环学习之间的协同作用对于弥合语义推理和物理现实之间的差距以实现长期战略规划至关重要。

[阅读原文](https://arxiv.org/abs/2604.11041)

---

## 4. EE-HCP：通过自动环境生成和体验学习进行自我进化的MCP-图形界面代理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tiantian He, Yihang Chen, Keyue Jiang, Ka Yiu Lee, Kaiwen Zhou, Kun Shao, Shuai Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving agent framework with automated environment generation and an experience bank for iterative improvement across GUI and MCP modalities.

**摘要**: arXiv：2604.09815v1公告类型：新摘要：通过模型上下文协议（MCP）将GUI交互与结构化API调用相结合的计算机使用代理显示出自动化软件任务的前景。然而，现有的方法缺乏对代理应该如何平衡这两种模式以及如何在不同的应用程序中实现迭代自我改进的原则性理解。我们将MCP-图形用户界面相互作用描述为一个统一的混合策略学习问题，其中代理在每个模式提供互补优势时进行学习，并表明提炼和体验增强针对的是根本不同的故障模式--需要应用程序感知机制选择。在此公式的基础上，我们提出了一个具有全自动管道的自我进化框架，该管道协调自动环境生成和验证、轨迹收集、差距驱动的任务合成和质量过滤训练-所有这些都无需手动干预。一项关键创新是我们的经验库，它从轨迹比较中积累LLM学到的规则，无需微调即可实现推理时改进。跨三个桌面应用程序的系统\textBF{跨应用程序分析}表明，最佳策略取决于MCP-图形用户界面的组成：蒸馏在以CP为主的任务上达到了77.8%的通过率（+17.8pp），而体验银行在图形用户界面密集型任务上表现出色（+10.0pp）。

[阅读原文](https://arxiv.org/abs/2604.09815)

---

## 5. 多轮同理心对话中的话语多样性

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongli Zhan, Emma S. Gueorguieva, Javier Hernandez, Jina Suh, Desmond C. Ong, Junyi Jessy Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces MINT, a reinforcement learning framework to optimize discourse move diversity across multi-turn empathic dialogue, directly improving LLM behavior via a novel reward design.

**摘要**: arXiv：2604.11742v1宣布类型：新摘要：大型语言模型（LLM）在单轮环境中产生被评为高度同理心的响应（Ayers等人，2023年; Lee等人，2024），但它们也被认为是公式化生成器，在任务中重复使用相同的词汇模式、语法模板和话语结构（Jiang等人，2025年; Shaib等人，2024年; Namuduri等人，2025年）。人们较少关注这种公式化是否延伸到话语动作的水平，即，回应对其所针对的人有何作用。这个问题对于同理心对话尤其重要，有效的支持不仅需要一时的善意回应，还需要随着对话的展开而采取不同的策略（Stiles等人，1998年）。事实上，之前的工作表明，LLM在单回合环境中比人类支持者更多地重复使用相同的策略序列（Gueorguieva等人，2026年）。我们将这种分析扩展到多回合对话，发现僵化现象加剧：一旦一种策略出现在支持者回合中，LLM在下一轮中重复使用它的比例几乎是人类的两倍（0.50-0.56 vs. 0.27）。这种模式适用于在真正的情感支持对话中充当支持者的LLM，并且对于标准相似性指标来说是不可见的。为了解决这一差距，我们引入了MNT（多回合策略间新颖性训练），这是第一个强化学习框架，用于优化多回合同理心对话中的话语移动多样性。最好的MNT变体将同理心质量奖励与交叉转向策略新颖信号相结合，在1.7B和4 B模型中将总同理心比香草提高了25.3%，同时在4 B模型上将交叉转向话语移动重复减少了26.3%，超过了所有基线，包括两种指标上的纯质量和代币级别的多样性方法。这些结果表明，当前模型缺乏的不是同理心本身，而是在整个对话中改变话语的能力。

[阅读原文](https://arxiv.org/abs/2604.11742)

---

## 6. 临时奖励：推理奖励量表视觉生成培训和测试时间

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haozhe Wang, Cong Wei, Weiming Ren, Jiaming Liu, Fangzhen Lin, Wenhu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RationalRewards, a reward model that generates structured rationales for fine-grained RL training and test-time critique-refine loops, directly matching RL for LLMs.

**摘要**: arXiv：2604.11626v1宣布类型：新摘要：大多数视觉生成的奖励模型都将丰富的人类判断简化为一个无法解释的分数，放弃了构成偏好的推理。我们表明，在评分之前教授奖励模型产生显式、多维的批评，可以将它们从被动评估者转变为主动优化工具，以两种补充的方式改进生成器：在训练时，结构化原理为强化学习提供可解释的、细粒度的奖励;在测试时，Generate-Critique-Refine循环将批评转化为有针对性的提示修订，无需任何参数更新即可改善输出。为了在不需要昂贵的理由注释的情况下训练这样的奖励模型，我们引入了偏好锚定简化（PARROT），这是一个有原则的框架，通过锚定生成、一致性过滤和蒸馏从现成的偏好数据中恢复高质量的理由。由此产生的模型DeliveralRewards（8B）在开源奖励模型中实现了最先进的偏好预测，与Gemini-2.5-Pro竞争，同时使用的训练数据比可比基线少10- 20倍。作为RL奖励，它持续改进文本到图像和图像编辑生成器，超出了纯量替代方案。最引人注目的是，它的测试时批评和细化循环在几个基准上匹配或超过了基于RL的微调，这表明结构化推理可以释放现有生成器中次优提示无法激发的潜在能力。

[阅读原文](https://arxiv.org/abs/2604.11626)

---

## 7. Skill-SD：多回合LLM试剂的技能条件自蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hao Wang, Guozhi Wang, Han Xiao, Yufeng Zhou, Yue Pan, Jichao Wang, Ke Xu, Yafei Wen, Xiaohu Ruan, Xiaoxin Chen, Honggang Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Skill-SD, a novel RL-based self-distillation framework for multi-turn LLM agents that uses trajectory-derived skills as dynamic privileged supervision for agent improvement.

**摘要**: arXiv：2604.10674v1公告类型：新摘要：强化学习（RL）已被广泛用于训练LLM代理多轮交互式任务，但其样本效率受到稀疏奖励和长视野的严重限制。政策上的自我升华（OPSD）通过提供来自特权教师的密集令牌级监督来实现这一点，该教师可以访问地面真相答案。然而，这种固定的特权信息无法捕捉到代理任务中多样化的有效策略，天真地将OPSD与RL结合常常会导致训练崩溃。为了解决这些限制，我们引入了Skill-SD，这是一个将代理自己的轨迹转变为动态仅培训监督的框架。完成的轨迹被总结为紧凑的自然语言技能，描述成功的行为、错误和工作流程。这些技能仅作为教师的动态特权信息条件，而学生始终在简单的任务提示下行事，并学会通过蒸馏将指导内化。为了稳定训练，我们推导出重要性加权反向KL损失，以提供梯度正确的代币水平蒸馏，并动态同步教师与进步的学生。Agentic基准测试的实验结果表明，Skill-SD的表现大大优于标准RL基线，改善了vanilla GRPO（AppWorld/Sokoban上+14.0%/+10.9%）和vanilla OPD（+42.1%/+40.6%）。项目页面：https://k1xe.github.io/skill-sd/

[阅读原文](https://arxiv.org/abs/2604.10674)

---

## 8. 重新思考WLVR中的代币级信用分配：两极-熵分析

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuhang He, Haodong Wu, Siyi Liu, Hongyu Ge, Hange Zhou, Keyi Wu, Zhuo Zheng, Qihong Lin, Zixin Zhong, Yongqi Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Entropy-Aware Policy Optimization (EAPO), a new RL method for LLMs that addresses token-level credit assignment in RLVR, directly improving reasoning via reward design.

**摘要**: arXiv：2604.11056v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）极大地提高了大型语言模型（LLM）的推理能力。然而，其稀疏的基于结果的奖励构成了一个根本的信用分配问题。我们通过奖励两极和代币熵的联合镜头来分析这个问题。我们的诊断工具“四象限分解”通过极化和熵隔离令牌更新，受控消融表明推理改进集中在高熵象限。为了从理论上证明这一观察结果的合理性，我们将条件互信息适应自回归WLVR设置，并证明代币可以承载的信用度由其信息的信息量为上界。这种观点产生了可测试的预测，即推理收益主要来自高熵代币，并且对积极和消极更新具有独特的作用。GRPO的梯度分析进一步揭示了均匀奖励广播如何稀释高熵位置的信号，同时过度信用确定性代币。基于这些见解，我们提出了相应地调节代币级学习信号的熵感知策略优化（EAPO）。大量实验表明，EAPO的表现优于两个模型系列的强基线。

[阅读原文](https://arxiv.org/abs/2604.11056)

---

## 9. 政策分裂：通过双模式熵正规化激励LLM强化中的双模式探索

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiashu Yao, Heyan Huang, Chuwei Luo, Daiqing Wu, Zeming Liu, Yuhang Guo, Yangyang Kang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Policy Split, a novel RL method for LLMs that uses a dual-mode policy with entropy regularization to encourage diverse exploration.

**摘要**: arXiv：2604.11510v1宣布类型：新摘要：为了鼓励在大型语言模型（LLM）的强化学习（RL）中进行多样化探索，同时不影响准确性，我们提出了Policy Split，这是一种新颖的范式，它将策略分为正常模式和高熵模式，并具有高熵提示。在共享模型参数的同时，这两种模式会根据不同目标进行协作的双模式熵正规化。具体来说，正常模式针对任务正确性进行优化，而高熵模式则结合了探索偏好，并且两种模式协同学习。大量实验表明，在一般和创造性任务中，我们的方法在各种模型尺寸中始终优于既定的信息引导RL基线。进一步的分析表明，政策拆分促进了双模式探索，其中高熵模式生成与正常模式不同的行为模式，提供独特的学习信号。

[阅读原文](https://arxiv.org/abs/2604.11510)

---

## 10. 琐碎纠正内生回报

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinda Wang, Zhengxu Hou, Yangshijie Zhang, Bingren Yan, Jialin Liu, Chenzhuo Zhao, Zhibo Yang, Bin-Bin Yang, Feng Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TCER, a novel unsupervised RL method for LLMs that corrects triviality bias in endogenous reward design for open-ended generation.

**摘要**: arXiv：2604.11522v1宣布类型：新摘要：开放式文本生成的强化学习受到缺乏可验证奖励的限制，因此必须依赖需要注释数据或强大的闭源模型的判断模型。受最近关于使用基于信心的内生奖励进行数学推理的无监督强化学习研究的启发，我们研究了这一原则是否可以适用于开放式写作任务。我们发现，直接应用信心奖励会导致琐碎偏见：政策向高概率产出崩溃，减少多样性和有意义的内容。我们提出了TBER（琐碎纠正的内生奖励），它通过奖励专业政策和通才参考政策之间的相对信息收益来解决这种偏见，并由概率相关的纠正机制调节。在多个写作基准和模型架构中，TBER在没有外部监督的情况下实现了一致的改进。此外，TBER还有效地转移到数学推理，验证了我们方法在不同生成任务中的通用性。

[阅读原文](https://arxiv.org/abs/2604.11522)

---

## 11. 先锋代理：持续改进生产中的小型语言模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Dhruv Atreja, Julia White, Nikhil Nayak, Kelton Zhang, Henrijs Princis, George Hurn-Maloney, Ash Lewis, Urchade Zaratiana

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a closed-loop system for continual self-improvement of small language models via automated data curation, failure diagnosis, and retraining.

**摘要**: arXiv：2604.09791v1宣布类型：新摘要：小型语言模型因其低成本、快速推理和易于专业化而对生产部署具有吸引力。然而，使它们适应特定任务仍然是一个具有挑战性的工程循环，驱动的不是训练本身，而是周围决策：数据策展、故障诊断、回归避免和迭代控制。我们介绍了Pioneer Agent，这是一个使此生命周期自动化的闭环系统。在冷启动模式下，仅给定自然语言任务描述，代理会通过联合优化数据、超参数和学习策略来获取数据、构建评估集并迭代训练模型。在生产模式下，给定带有标记故障的已部署模型，它会诊断错误模式、构建有针对性的训练数据并在显式回归约束下进行重新训练。为了评估这种设置，我们引入了AdaptFT-Bench，这是一个具有逐渐增加的噪音的合成推理日志基准，旨在测试整个适应循环：诊断、课程合成、再培训和验证。在涵盖推理、数学、代码生成、总结和分类的八个冷启动基准中，Pioneer Agent比基本模型提高了1.6-83.8个百分点。在AdaptFT-Bench上，它可以提高或保留所有七种场景下的性能，而天真再培训则会降低高达43个百分点。在根据公共基准任务构建的两个生产式部署上，它将意图分类从84.9%提高到99.3%，将实体F1从0.345提高到0.810。除了性能提升之外，代理还经常纯粹从下游反馈中发现有效的培训策略，包括思想链监督、特定任务的优化和以质量为中心的数据策展。

[阅读原文](https://arxiv.org/abs/2604.09791)

---

## 12. 一起玩：学习通过心理理论引导信仰的双重主体捍卫者

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hanqi Xiao, Vaidehi Patil, Zaid Khan, Hyunji Lee, Elias Stengel-Eskin, Mohit Bansal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Trains AI Double Agents using reinforcement learning with ToM and fooling rewards, directly improving LLM behavior via an RL pipeline for belief steering.

**摘要**: arXiv：2604.11666v1宣布类型：新摘要：随着大型语言模型（LLM）成为对话系统背后的引擎，它们推理对话伙伴的意图和状态的能力（即，形成并使用心理理论（ToM）对于与潜在敌对伙伴的安全互动变得越来越重要。我们提出了一种新颖的以隐私为主题的ToM挑战，ToM引导信念（ToM-SB），其中防御者必须充当双重代理，以在共享宇宙中引导具有部分先验知识的攻击者的信念。为了在ToM-SB上取得成功，防御者必须与攻击者互动并形成攻击者的ToM，目标是欺骗攻击者相信他们已经成功提取敏感信息。我们发现，Gemini 3-Pro和GPT-5.4等强大的前沿模型在ToM-SB上很难使用部分攻击者先验知识在困难场景中欺骗攻击者，即使在提示推理攻击者的信念（ToM提示）时也是如此。为了缩小这一差距，我们在ToM-SB上训练模型，使用强化学习来充当人工智能双代理，测试愚弄和ToM奖励。值得注意的是，我们发现ToM和攻击者愚弄之间存在双向紧急关系：仅奖励愚弄成功可以改善ToM，而仅奖励ToM可以改善愚弄。在四种具有不同优势的攻击者、六种防御者方法以及内分布和外分布（OOD）评估中，我们发现ToM的收益和攻击者愚弄的收益密切相关，凸显了信念建模是ToM-SB成功的关键驱动力。结合了ToM和愚弄奖励的人工智能双代理产生了最强的愚弄和ToM性能，在困难场景下，ToM提示的性能优于Gemini 3-Pro和GPT-5.4。我们还表明，ToM-SB和AI双重代理可以扩展到更强大的攻击者，展示了对OOD设置的概括性和我们任务的可处理性。

[阅读原文](https://arxiv.org/abs/2604.11666)

---

## 13. 循环推理语言模型的机制分析

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hugh Blayney, \'Alvaro Arroyo, Johan Obando-Ceron, Pablo Samuel Castro, Aaron Courville, Michael M. Bronstein, Xiaowen Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Mechanistically analyzes looped reasoning language models, a latent reasoning architecture where layers are looped in the latent dimension, directly matching the latent CoT/reasoning criterion.

**摘要**: arXiv：2604.11791v1宣布类型：新摘要：推理已成为大型语言模型的核心能力。最近的研究表明，通过在潜在维度中循环LLM的层，从而产生循环推理语言模型，可以提高推理性能。尽管结果令人鼓舞，但很少有作品研究它们的内部动力学与标准前向模型的内部动力学有何不同。在本文中，我们对循环语言模型中的潜在状态进行了机械分析，特别关注在前向模型中观察到的推理阶段与在循环模型中观察到的推理阶段如何进行比较。为此，我们分析了循环循环，并表明对于许多研究的模型来说，循环中的每一层都收敛到一个不同的不稳定点;因此，循环块在潜在空间中遵循一致的循环轨迹。我们提供的证据表明，当达到这些固定点时，注意力头行为就会稳定下来，从而导致在循环过程中的持续行为。从经验上看，我们发现循环块学习的推理阶段与前向模型的推理阶段密切相似，并在每次迭代中深入重复这些阶段。我们研究循环块大小、输入注入和标准化如何影响这些循环不定点的出现和稳定性。我们相信这些发现有助于将机械见解转化为建筑设计的实际指导。

[阅读原文](https://arxiv.org/abs/2604.11791)

---

## 14. 通过互信息自我评估强化来利用和校准事后诸葛亮流程奖励

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiashu Yao, Heyan Huang, Zeming Liu, Yuhang Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MISE, a novel RL paradigm for LLMs that uses calibrated hindsight generative self-evaluation as dense reward signals, directly aligning with RL for LLMs.

**摘要**: arXiv：2604.11611v1宣布类型：新摘要：为了克服基于大型语言模型（LLM）的智能体强化学习（RL）中的稀疏奖励挑战，我们提出了互信息自我评估（MISE），这是一种RL范式，利用事后诸葛亮生成式自我评估作为密集奖励信号，同时根据环境反馈对其进行校准。从经验上看，MISE使代理能够从补充稀疏外部信号的密集内部奖励中自主学习。从理论上讲，我们的工作为生成性自我奖励范式提供了第一个正式基础。我们证明，利用事后诸葛亮的自我评估奖励相当于最小化将相互信息与政策和代理奖励政策之间的KL分歧项相结合的目标。然后，这种理论见解为我们的校准步骤提供了信息并证明了其合理性，该步骤将这些奖励与最佳政策积极地保持一致。大量实验表明，MISE的表现优于强基线，使大约7 B参数的开源LLM能够在无需专家监督的情况下在验证方面实现与GPT-4 o相当的性能。

[阅读原文](https://arxiv.org/abs/2604.11611)

---

## 15. Relax：一个用于全模式大规模训练后的同步强化学习引擎

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Liujie Zhang, Benzhe Ning, Rui Yang, Xiaoyan Yu, Jiaxing Li, Lumeng Wu, Jia Liu, Minghao Li, Weihang Chen, Weiqi Hu, Lei Zhang

**机构**: Rednote AI

**💡 亮点 (Highlight)**: Introduces a novel, scalable asynchronous RL training engine designed for omni-modal post-training of LLMs, directly addressing RL for LLMs.

**摘要**: arXiv：2604.11554v1宣布类型：新摘要：事实证明，强化学习（RL）后训练对于解锁大型语言模型中的推理、自我反思和工具使用能力是有效的。随着模型扩展到全模式输入和代理多回合工作流程，RL培训系统面临着三个相互依赖的挑战：异类数据流、大规模操作稳健性以及陈旧性--吞吐量权衡。我们介绍了\textBF{Relax}（利用统计X-modality的强化引擎），这是一个开源RL训练引擎，通过三个共同设计的架构层来解决这些挑战。首先，\{omni-原生架构}将多模式支持构建到整个堆栈中--从数据预处理和模式感知并行到推理生成--而不是将其改造到以文本为中心的管道上。其次，每个RL角色都作为独立的故障隔离服务运行，可以在无需全局协调的情况下扩展、恢复和升级。第三，服务级脱钩支持通过TransferQueue数据巴士进行同步训练，其中单个过时参数在政策上执行、近政策上执行和完全同步执行之间平滑地插入。Relax在Qwen 3 - 4 B政策培训上比veRL实现了1.20 $\times $的端到端加速。其完全Inbox模式在Qwen 3 - 4 B上比托管提供1.76 $\times $加速，在Qwen 3-Omni-30 B上提供2.00 $\times $加速，而所有模式都收敛到相同的奖励级别。Relax支持R3（推出路由重播）~\cite{ma 2025 r3}，用于MoE型号，仅需1.9%的管理，而相同配置下veRL的性能下降为32%。它进一步展示了Qwen 3-Omni上跨图像、文本和音频的稳定全模式RL收敛，在视频上持续超过2{，}000步而不会降级。Relax可在https://github.com/rednote-ai/Relax上获取。

[阅读原文](https://arxiv.org/abs/2604.11554)

---

## 16. 可控且可验证的工具使用数据合成进行统计强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Siyuan Xu, Shiyang Li, Xin Liu, Tianyi Liu, Yixiao Li, Zhan Shi, Zixuan Zhang, Zilong Wang, Qingyu Yin, Jianshu Chen, Tuo Zhao, Bing Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a pipeline for generating synthetic, reward-checkable tool-use environments to enable RL optimization of tool-calling policies, directly matching RL for LLMs and self-improving agent criteria.

**摘要**: arXiv：2604.09813v1宣布类型：新摘要：现有的合成工具使用库主要是为离线监督微调而设计的，但强化学习（RL）需要支持可奖励检查的在线部署的可执行环境。我们提出了COVERT，这是一个两阶段管道，首先通过具有多层验证的自进化合成来生成可靠的基本工具使用轨迹，然后应用Oracle保留增强来系统性地增加环境复杂性。这些增强引入了干扰工具、间接或模糊的用户查询以及嘈杂、多格式或错误的工具输出，同时严格保留Oracle工具调用和最终答案作为基本真相。该设计通过标准案例的引用匹配以及错误检测等特殊行为的轻量级判断辅助验证来实现自动奖励计算，支持工具调用策略的RL优化。在Qwen 2.5-Direct-14 B上，COVERT-RL将BFCL v3的总体准确性从56.5提高到59.9，将ACEBench的总体准确性从53.0提高到59.3，对一般能力基准的回归最小;当叠加在SFT上时，它进一步达到62.1和61.8，确认了相加性收益。这些结果表明，保留Oracle的合成环境提供了一个实用的RL细化阶段，补充SFT，用于在模糊性和不可靠的工具反馈下提高工具使用的鲁棒性。

[阅读原文](https://arxiv.org/abs/2604.09813)

---

## 17. 带回价值模型：LLM强化学习中价值模型的生成性批评者

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zikang Shan, Han Zhong, Liwei Wang, Li Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a generative critic with chain-of-thought reasoning for value modeling, directly improving credit assignment in LLM reinforcement learning.

**摘要**: arXiv：2604.10701v1宣布类型：新摘要：学分分配是强化学习（RL）的核心挑战。经典的演员-评论家方法通过基于习得价值函数的细粒度优势估计来解决这一挑战。然而，现代大语言模型（LLM）RL中通常会避免习得价值模型，因为传统的区分性批评者很难可靠地训练。我们重新审视价值建模，并认为这种困难部分是由于表达能力有限。特别是，表示复杂性理论表明，在现有价值模型使用的一次性预测范式下，价值函数可能很难逼近，而我们的缩放实验表明，此类批评者不会随着规模的增长而可靠地改进。受这一观察的启发，我们提出了生成性行为者-批评者（GenAC），它用生成性批评者取代一次性纯量值预测，生成性批评者在产生价值估计之前执行思想链推理。我们进一步引入了情境条件反射，这可以帮助批评者在整个培训过程中保持对当前演员的校准。GenAC改进了价值逼近、排名可靠性和分布外一般化，这些收益转化为比基于价值和无价值基线更强的下游RL性能。总的来说，我们的研究结果表明，更强的价值建模是改善LLM强化学习中信用分配的一个有希望的方向。

[阅读原文](https://arxiv.org/abs/2604.10701)

---

## 18. 指导LLM使用具有可验证奖励的强化学习进行谈判

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao, Lei Lei, Yuheng Zhang, Yisong Yue, David Simchi-Levi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Strong match for RL for LLMs: introduces RL with verifiable rewards to train an LLM agent for negotiation, showing strategic evolution and outperforming larger models.

**摘要**: arXiv：2604.09855v1宣布类型：新摘要：大型语言模型（LLM）的最近发展确立了它们作为自主交互代理的潜力。然而，他们经常在不完全信息的战略游戏中挣扎，例如双边价格谈判。在本文中，我们研究了来自可验证奖励的强化学习（WLVR）是否可以有效地教LLC谈判。具体来说，我们探索学习过程中出现的战略行为。我们引入了一个框架，针对现实世界产品的广泛分销中的受监管LLM卖家，培训中型买家代理。通过将奖励信号直接建立在经济盈余最大化和严格遵守私人预算约束之上，我们揭示了一种新颖的四阶段战略演变。代理人从天真的讨价还价发展到使用激进的起价，经历僵局阶段，并最终发展出复杂的说服技巧。我们的结果表明，这种可验证的训练允许30 B代理在提取盈余方面的表现显着优于其规模十倍以上的前沿模型。此外，经过训练的代理人会强有力地推广到培训期间看不到的更强大的交易对手，并且即使在面临敌对、敌对的卖家角色时仍然有效。

[阅读原文](https://arxiv.org/abs/2604.09855)

---

## 19. LLM WLVR加速的低级优化轨迹建模

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhipeng Chen, Tao Qian, Wayne Xin Zhao, Ji-Rong Wen

**机构**: RUCAIBox (likely Renmin University of China)

**💡 亮点 (Highlight)**: Proposes a novel method to accelerate RL with Verifiable Rewards (RLVR) for LLMs by modeling and nonlinearly extrapolating low-rank parameter trajectories.

**摘要**: arXiv：2604.11446v1宣布类型：新摘要：最近，针对大型语言模型（LLM）扩展具有可验证奖励的强化学习（WLVR）已成为显着提高模型能力的有效训练范式，这需要引导模型进行广泛的探索和学习，从而导致大量的计算费用并成为一个关键挑战。为了减少训练步骤的数量，先前的工作对模型参数进行线性外推。然而，人们对WLVR训练期间模型参数更新的动态性仍然不够了解。为了进一步研究LLM在WLVR训练期间的演变，我们进行了实证实验，发现模型的rank-1子空间并不是线性演变，并且其对原始参数的主导地位在LoRA训练期间进一步放大。基于上述见解，我们提出了低阶轨迹的\textBF{N}onlinear \textBF{Ext} Rapplation（\textBF{NExt}），这是一个以非线性方式建模和外推低阶参数轨迹的新型框架。具体来说，我们首先使用LoRA训练模型，并在多个训练步骤中提取参数差异的rank-1子空间，然后用于后续的非线性外推。然后，利用提取的秩1子空间训练预测器，对RLVR过程中参数更新的轨迹进行建模，并通过预测-扩展过程外推模型参数，实现RLVR的加速。为了进一步研究和理解NExt，我们进行了全面的实验，证明了该方法的有效性和鲁棒性。我们的方法减少了约37.5%的计算开销，同时保持兼容范围广泛的RLVR算法和任务。我们在https://github.com/RUCAIBox/NExt上发布代码。

[阅读原文](https://arxiv.org/abs/2604.11446)

---

## 20. 备忘录：教法学硕士管理自己的环境

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Vasilis Kontonis, Yuchen Zeng, Shivam Garg, Lingjiao Chen, Hao Tang, Ziyan Wang, Ahmed Awadallah, Eric Horvitz, John Langford, Dimitris Papailiopoulos

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MEMENTO, a method teaching LLMs to segment reasoning into blocks and compress them into dense state summaries (mementos), directly aligning with latent CoT/reasoning by moving computation to a compact latent form.

**摘要**: arXiv：2604.09852v1宣布类型：新摘要：推理模型以长的、非结构化的流进行思考，没有压缩或组织自己的中间状态的机制。我们引入MEMEMENTO：一种教模型将推理分割成块的方法，将每个块压缩成纪念品，即，密集的状态摘要，并通过仅关注纪念品、减少上下文、KV缓存和计算进行推理。为了训练MEMENTO模型，我们发布了OpenMementos，这是一个包含228 K推理痕迹的公共数据集，源自OpenKnights-v3，经过分段和注释，并使用中间摘要。我们表明，OpenMementos上的两阶段SFT食谱在不同的模型系列（Qwen 3、Phi-4、Olmo 3）和规模（8B--32 B参数）中有效。经过训练的模型在数学、科学和编码基准方面保持了很高的准确性，同时实现了${\sim} 2.5\x $峰值的KV缓存减少。我们扩展了vLLM来支持我们的推理方法，实现了${\sim} 1.75\times $吞吐量的提高，同时还使我们能够执行RL并进一步提高准确性。最后，我们识别了一个双重信息流：来自每个推理块的信息由纪念文本和相应的KV状态承载，这些状态保留了来自原始块的隐式信息。删除此通道会使AIME 24上的准确性降低15，pp。

[阅读原文](https://arxiv.org/abs/2604.09852)

---

## 21. 多模态潜在推理的视觉增强深度缩放

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yudong Han, Yong Wang, Zaiquan Yang, Zhen Qu, Liyuan Pan, Xiangxiang Chu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel framework for multimodal latent reasoning, replacing explicit CoT with implicit feature propagation and adaptive depth scaling.

**摘要**: arXiv：2604.10500v1宣布类型：新摘要：多模式潜在推理已成为一种有前途的范式，用隐式特征传播取代显式思想链（CoT）解码，同时增强表示信息性并减少推理延迟。通过分析潜伏训练期间的标记级梯度动态，我们揭示了两个关键观察结果：（1）由于固有的语言偏见，视觉标记表现出比文本对应物明显更高、更不稳定的梯度规范，导致系统性视觉优化不足;和（2）语义简单的标记快速收敛，而复杂的标记表现出受固定架构深度约束的持续梯度不稳定性。为了解决这些局限性，我们提出了一个视觉回放模块和路由深度缩放，以协作增强视觉感知并细化复杂的潜伏，以进行更深层次的上下文推理。前一个模块利用因果性自我注意力来估计代币显着性，通过空间一致的约束来加强细粒度的基础。补充地，后一种机制自适应地将额外的推理步骤分配给复杂令牌，从而实现更深层次的上下文细化。在逐步将显式CoT内化为紧凑的潜在表示的课程策略的指导下，我们的框架在不同基准上实现了最先进的性能，同时在显式CoT基线上提供了实质性的推理加速。

[阅读原文](https://arxiv.org/abs/2604.10500)

---

## 22. 基于对比互信息的高效流程奖励建模

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Nakyung Lee, Sangwoo Hong, Jungwoo Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel automatic reward labeling method (CPMI) for process reward models, directly addressing scalable reward design for RL in LLMs to improve reasoning verification.

**摘要**: arXiv：2604.10660v1宣布类型：新摘要：最近的研究投入了大量精力使用流程奖励模型（PRM）和其他验证者模型来验证思想链（CoT）轨迹的中间推理步骤。然而，训练PRM通常需要人类注释者为每个推理步骤分配奖励分数，这既昂贵又耗时。由于LLM的重复推出，现有的自动化方法，例如蒙特卡洛（MC）估计，也需要大量的计算资源。为了克服这些限制，我们提出了对比逐点互信息（CPMI），这是一种新型的自动奖励标签方法，它利用模型的内部概率来推断阶梯级监督，同时显着减少注释数据集的计算负担。CPMI量化推理步骤相对于硬否定替代方案增加了该步骤与正确目标答案之间的互信息的程度。这个对比信号可以代表该步骤对最终解决方案的贡献，并产生可靠的回报。实验结果表明，与MC估计相比，基于CPMI的标记将数据集构建时间减少了84%，令牌生成减少了98%，同时在流程级评估和数学推理基准方面实现了更高的准确性。

[阅读原文](https://arxiv.org/abs/2604.10660)

---

## 23. 环形Transformer内部状态的关系偏好编码

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jan Kirin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates how latent reasoning states in a looped transformer encode human preference, directly relevant to latent CoT/reasoning and RL for LLMs via internal reward modeling.

**摘要**: arXiv：2604.09870v1宣布类型：新摘要：我们研究循环转换器如何在其内部迭代状态中编码人类偏好。使用Ouro-2. 6 B-Thinking，一个具有迭代细化的2. 6 B参数循环Transformer，我们从每个循环迭代中提取隐藏状态，并训练轻量级评估头（约5 M参数）来预测人类HH-RLHF数据集上的人类偏好。我们的成对评估器在8，552个未见示例上实现了95.2%的测试准确率，超过了全批L-BFSG探针（84.5%），而基本模型保持完全冻结。   我们的中心发现是，循环状态主要以关系方式编码偏好：对成对差异的线性探测达到84.5%，最好的非线性独立评估器仅达到65%的测试准确率，线性独立分类得分为21.75%，低于机会并且具有相反的两极。经过精确解释，评估器充当模型内部一致性探测器，测量Ouro自己的习得价值系统组织其表示的稳定性，而不是它预测嘈杂的人类注释的能力。   我们还记录了一个系统性的架构搜索，该搜索为独立评分建立了真正的70%上限，并展示了防止退化的成对解决方案所需的50%参数交换协议如何在峰值时将成对训练指标缩小了约31个点，从而创造了成对和逐点评估者共享相同上限的假象。   最后，我们表明，第2个时期的cos学习率死区意外地充当了提前停止，在过度适应退化的测试准确性从95.2%下降到第5个时期的62.4%之前保留了概括峰值。跨时期翻转测试分析表明，反对称相关性保持稳定，而严格的符号翻转率主要跟踪得分者偏差。我们建议将翻转测试作为成对偏好评估者的强制诊断。

[阅读原文](https://arxiv.org/abs/2604.09870)

---

## 24. 变形金刚通过镜像下降在上下文中学习潜在混合模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Francesco D'Angelo, Nicolas Flammarion

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Strong match for latent reasoning: demonstrates transformers learn latent mixture models in-context via mirror descent, revealing a mechanism for latent computation in attention layers.

**摘要**: arXiv：2604.10848v1宣布类型：新摘要：序列建模需要确定哪些过去的代币与上下文及其重要性存在因果关系：这是变形金刚中注意力层固有的过程，但其潜在的学习机制仍然知之甚少。在这项工作中，我们通过引入基于过渡分布混合的框架，将估计代币重要性的任务形式化为一个背景学习问题，其中潜在变量确定过去代币对下一个代币的影响。这个潜在变量的分布由变形者必须在上下文中学习的未观察到的混合权重参数化。我们证明变形器可以实现Mirror Destent以从上下文中学习这些权重。具体来说，我们给出了三层变换器的显式构造，该变换器准确地实现了镜像下降的一步，并证明了所得估计器是Bayes最优预测器的一阶逼近。通过梯度下降证实了我们的构造及其可学习性，我们凭经验证明从头开始训练的transformers学习与我们的理论一致的解决方案：它们的预测分布，注意力模式和学习的转换矩阵与构造密切匹配，而更深的模型实现了与多步镜像下降相当的性能。

[阅读原文](https://arxiv.org/abs/2604.10848)

---

## 25. 协同进化统计推荐系统的自提炼强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zongwei Wang, Min Gao, Hongzhi Yin, Junliang Yu, Tong Chen, Shazia Sadiq, Tianrui Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-distilled RL framework for co-evolving agentic recommender systems, directly internalizing interaction experience into parameters via novel interaction reward and credit assignment.

**摘要**: arXiv：2604.10029v1宣布类型：新摘要：大型语言模型授权的代理推荐系统（ARS）将推荐重新定义为推荐代理和用户代理之间的多轮交互，实现了超越传统一次性预测的迭代偏好获取和细化。然而，现有的ARS主要在反射式范式中进行优化，其中过去的交互轨迹被存储为文本记忆，并作为提示上下文检索，以供以后推理。尽管这种设计允许代理人回忆之前的反馈和观察，但积累的经验仍然不受模型参数的影响，这使得代理人依赖于一般推理，而不是通过学习逐步获得特定于代理的决策能力。因此，强化学习（RL）提供了一种将此类交互体验内化为参数的自然方法。然而，现有的ARS RL方法仍然存在两个关键限制。首先，它们未能捕捉到ARS的交互性质，其中推荐代理和用户代理持续相互影响，并且可以通过交互反馈自然地产生内生监督。其次，他们将丰富的多回合互动过程简化为最终结果，忽略了贯穿整个轨迹的密集监督。为此，我们提出了CoARS，这是一个自提炼的强化学习框架，用于共同进化的代理推荐系统。CoARS引入了两种补充的学习方案：交互奖励，从相同的交互轨迹中为推荐者代理和用户代理推导出耦合的任务级监督，以及自提炼的学分分配，将历史轨迹转换为教师-学生条件反射下的代币级信用信号。多个数据集的实验表明，CoARS在推荐性能和用户对齐方面优于代表性ARS基线。

[阅读原文](https://arxiv.org/abs/2604.10029)

---

## 26. 代理' 2 RL-长凳：LLM代理可以进行大型RL后培训吗？

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Wanyi Chen, Xiao Yang, Xu Yang, Tianming Sha, Qizheng Li, Zhuo Wang, Bowen Xian, Fang Kong, Weiqing Liu, Jiang Bian

**机构**: Microsoft

**💡 亮点 (Highlight)**: Introduces a benchmark for evaluating whether LLM agents can autonomously design and run RL pipelines to improve foundation models, directly targeting self-improving agents and RL for LLMs.

**摘要**: arXiv：2604.10547v1宣布类型：新摘要：我们引入了Agent ' 2 RL-Bench，这是评估Agent RL训练后的基准--LLM代理是否可以自主设计、实施和运行改进基础模型的完整RL管道。这种能力很重要，因为RL后训练越来越多地推动模型对齐和专业化，但现有的基准在很大程度上仍然是静态的：单独监督微调就会产生强劲的结果，从而使交互式RL工程未经测试。Agent ' 2 RL-Bench通过三个级别的六项任务来解决这个问题--从基于规则的静态训练到具有轨迹收集的闭环在线RL--每个任务都添加了先前级别没有强加的结构性要求。该基准测试为隔离收件箱提供了分级API、记录每次提交和代码修订的运行时工具，以及生成结构化运行报告的自动化事后分析，从而实现对代理驱动的训练后行为的首次自动化诊断。在跨越五个代理系统和六个驱动程序LLM的多个代理堆栈中，我们发现代理实现了惊人的交互收益--在ALFWorld上，仅支持RL的代理通过SFT热身和GRPO在线推出从5.97提高到93.28--但在其他方面仅取得微弱进展（DeepSearchQA：评估噪音内+2.75），驱动程序选择对交互任务有很大影响--在同一框架内，切换驱动程序会将交互改进从接近零变为+78 pp。更广泛地说，该基准显示，在固定预算下，受监督的管道在代理驱动的后培训中占据主导地位，而在线RL仅在ALFWorld上成功成为最终的最佳路径。代码可在www.example.com上获取。

[阅读原文](https://arxiv.org/abs/2604.10547)

---

## 27. Mem $' 2 ' Evolve：通过协同进化能力扩展和体验提炼实现自我进化的代理人

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zihao Cheng, Zeming Liu, Yingyu Shan, Xinyi Wang, Xiangrong Zhu, Yunpu Ma, Hongru Wang, Yuhang Guo, Wei Lin, Yunhong Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving agent framework that co-evolves capabilities and experience via dynamic asset creation guided by accumulated experience.

**摘要**: arXiv：2604.10923v1宣布类型：新摘要：虽然大型语言模型--动力代理可以通过积累经验或动态创建新资产（即，工具或专家代理），现有框架通常会隔离处理这两个进化过程。这种分离忽视了它们内在的相互依赖性：前者本质上受到手动预定义的静态工具集的限制，而后者则在没有经验指导的情况下从头开始生成新资产，导致能力增长有限和不稳定的演变。为了解决这一局限性，我们引入了一种新的协同进化能力扩展和体验提炼范式。在此范式的指导下，我们提出了\textBF{Mem$^{\textBF{2}}$Evolve}，它集成了两个核心组件：\textBF{体验记忆}和\textBF{资产记忆}。具体来说，Mem$^{2}$Evolve利用积累的经验来指导资产的动态创建，从而扩大代理的能力空间，同时获得新的经验以实现协同进化。跨6个任务类别和8个基准的广泛实验表明，Mem$' s $Evolve比标准LLM提高了18.53%，比仅通过经验进化的代理提高了11.80%，比仅通过资产创建进化的代理提高了6.46%，使其成为一个更加有效和稳定的自我进化代理框架。代码可访问：https://buaa-irip-llm.github.io/Mem2Evolve。

[阅读原文](https://arxiv.org/abs/2604.10923)

---

## 28. HiEdit：使用分层强化学习的终身模型编辑

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yangfan Wang, Tianyang Sun, Chen Tang, Jie Liu, Wei Cai, Jingchi Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hierarchical reinforcement learning framework for lifelong model editing, directly using RL to adaptively select layers for precise, instance-aware updates.

**摘要**: arXiv：2604.11214v1宣布类型：新摘要：终身模型编辑（LME）旨在顺序纠正已部署的LLM中过时或不准确的知识，同时最大限度地减少对不相关输入的副作用。然而，现有方法通常将参数扰动应用于所有编辑实例的静态且密集的LLM层集。这种做法是违反直觉的，因为我们假设不同的知识存储在模型的不同层中。忽视这种分层的特殊性可能会阻碍整合新知识的适应性，并导致通用知识和之前编辑的知识的灾难性遗忘。为了解决这个问题，我们提出了HiEdit，这是一个分层强化学习框架，可以自适应地识别每个编辑实例与知识最相关的层。通过启用动态、实例感知的层选择并结合稀疏性的内在奖励，HiEdit实现了精确的本地化更新。对各种LLM的实验表明，HiEdit将竞争RLEdit的性能平均提高8.48%，每次编辑仅扰乱一半的层。我们的代码可访问：https://github.com/yangfanww/hiedit。

[阅读原文](https://arxiv.org/abs/2604.11214)

---

## 29. Camyla：医学图像分割中的缩放自主研究

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Yifan Gao, Haoyue Li, Feng Yuan, Xin Gao, Weiran Huang, Xiaosong Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a fully autonomous research agent system (Camyla) that demonstrates self-improvement through long-horizon experimentation, knowledge retention, and recovery mechanisms.

**摘要**: arXiv：2604.10696v1宣布类型：新摘要：我们介绍了Camyla，这是一个在医学图像分割科学领域进行完全自主研究的系统。卡米拉将原始数据集转换为基于文献的研究提案、可执行实验和完整手稿，无需人为干预。长期的自主实验提出了三个相互关联的挑战：搜索工作朝着没有希望的方向漂移，早期试验的知识随着背景的积累而退化，以及从失败中的恢复崩溃为重复的增量修复。为了应对这些挑战，该系统结合了三种耦合机制：用于在竞争提案之间分配工作的质量加权分支探索、用于以多个粒度保留和压缩交叉试验知识的分层反射记忆以及用于在表现不佳的试验后实现多样化的分歧诊断反馈。该系统是在CamylaBench上进行评估的，CamylaBench是一个由31个数据集完全根据2025年出版物构建的无污染基准，遵循严格的零干预协议，在8-图形处理器集群上在总共28天内进行两次独立运行。在两次运行中，Camyla生成了2，700多个新颖的模型实现和40份完整的手稿，并在相同的训练预算下分别超过了从包括nU-Net在内的14个已建立架构中选出的最强的每个数据集基线（union：24/31）。高级人类评论家对当代医学影像期刊的T1/T2边界生成的手稿进行评分。相对于自动化基线，Camyla在总体细分性能方面优于AutoML和NAS系统，并在任务完成和超越基线的频率方面超过了六个开放式研究代理。这些结果表明，在医学图像分割中可以实现领域规模的自主研究。

[阅读原文](https://arxiv.org/abs/2604.10696)

---

## 30. Multi-ORFT：协同驾驶中多智能体扩散规划的稳定在线强化微调

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haojie Bai, Aimin Li, Ruoyu Yao, Xiongwei Zhao, Tingting Zhang, Xing Zhang, Lin Gao, and Jun Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Multi-ORFT, a stable online reinforcement fine-tuning method for multi-agent diffusion planners, directly aligning with RL for LLMs via reward design and policy optimization.

**摘要**: arXiv：2604.11734v1宣布类型：新摘要：闭环合作驾驶需要规划者生成现实的多模式多智能体轨迹，同时提高安全性和交通效率。现有的扩散规划者可以通过演示对多模式行为进行建模，但它们通常表现出弱的场景一致性，并且与闭环目标保持不佳的一致性;与此同时，在反应式多智能体环境中进行稳定的在线后训练仍然困难。我们提出了Multi-ORFT，它将场景条件扩散预训练与稳定的在线强化训练后结合起来。在预训练中，规划者使用智能体间自我注意、交叉注意和基于AdaLN-Zero的场景条件反射来提高场景一致性和关节轨迹的道路依从性。在训练后，我们制定了一个两级MDP，它揭示了在线优化的分步反向核可能性，并将密集的假设级奖励与方差门控组相对政策优化（VG-GRPO）相结合以稳定训练。在WOMD闭环基准上，Multi-ORFT将碰撞率从2.04%降低到1.89%，越野率从1.68%降低到1.36%，同时将平均速度从8.36 m/s提高到8.61 m/s，相对于预培训的规划者，它在主要安全和效率指标方面优于强大的开源基线，包括SMART-large、SMART-tiny-CLSFT和VBD。这些结果表明，耦合场景一致性去噪与稳定的在线扩散策略优化提高了闭环协同驾驶的可靠性。

[阅读原文](https://arxiv.org/abs/2604.11734)

---

## 31. CSPO：缓解结构化表转LaTeX一代的奖励模糊性

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yunfan Yang, Cuiling Lan, Jitao Sang, Yan Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CSPO, a novel RL framework for LLMs that disentangles component-specific rewards to alleviate reward ambiguity in structured table-to-LaTeX generation.

**摘要**: arXiv：2604.10918v1宣布类型：新摘要：表格包含丰富的结构化信息，但当存储为图像时，它们的内容仍然“锁定”在像素内。将表格图像转换为LaTeX代码可以实现忠实的数字化和重用，但当前的多模式大型语言模型（MLLM）通常无法保持结构、风格或内容保真度。传统的强化学习（RL）后训练通常依赖于单一的聚合奖励，从而导致奖励模糊性，将多个行为方面混为一谈并阻碍有效优化。我们提出了特定于对象的策略优化（CSPO），这是一个RL框架，可以分解LaTeX表组件之间的优化--结构、风格和内容。特别是，CSPO分配特定于组件的奖励，并仅通过与其组件相关的令牌反向传播每个信号，从而减轻奖励的模糊性并实现有针对性的组件优化。为了全面评估绩效，我们引入了一组分层评估指标。大量实验证明了CSPO的有效性，强调了特定于组件的优化对于可靠的结构化生成的重要性。

[阅读原文](https://arxiv.org/abs/2604.10918)

---

## 32. 内省扩散语言模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yifan Yu, Yuqing Jian, Junxiong Wang, Zhongzhu Zhou, Donglin Zhuang, Xinyu Fang, Sri Yanamandra, Xiaoxia Wu, Qingyang Wu, Shuaiwen Leon Song, Tri Dao, Ben Athiwaratkun, James Zou, Fan Lai, Chenfeng Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel diffusion language model architecture with introspective strided decoding, directly addressing latent reasoning efficiency by enabling parallel verification of generated tokens.

**摘要**: arXiv：2604.11035v1宣布类型：新摘要：扩散语言模型承诺并行生成，但在质量上仍然落后于自回归（AR）模型。我们将这种差距缩小为内省一致性的失败：AR模型与自己的一代人意见一致，而DLC往往不一致。我们定义了内省接受率，它衡量模型是否接受其之前生成的代币。这揭示了为什么AR训练具有结构性优势：因果掩盖和逻辑比特转换隐性地强制了内省的一致性。受这一观察结果的启发，我们引入了内省扩散语言模型（I-DLM），这是一种保留扩散式并行解码的范式，同时继承AR训练的内省一致性。I-DLM使用一种新颖的内省分步解码（ISD）算法，该算法使模型能够验证之前生成的令牌，同时在同一向前传递中推进新令牌。从系统的角度来看，我们在AR继承的优化上构建I-DLM推理引擎，并使用静态批处理调度器进一步对其进行定制。据我们所知，I-DLM是第一款在15个基准测试中在模型质量和实际服务效率方面优于之前的DLC的DLM。AIME-24上达到69.6，LiveCodeBench-v6上达到45.7，分别比LLaDA-2.1-mini（16 B）高出26分和15分以上。除了质量之外，I-DLM还专为不断增长的大并发服务需求而设计，其吞吐量比之前最先进的DLC高出约3倍。

[阅读原文](https://arxiv.org/abs/2604.11035)

---

## 33. 从临床叙述中学习基于偏好的目标以进行顺序治疗决策

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Daniel J. Tan, Kay Choong See, Mengling Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL reward learning framework (CN-PR) that uses LLMs to derive trajectory-level preferences from clinical narratives for sequential treatment decision-making.

**摘要**: arXiv：2604.10783v1宣布类型：新摘要：设计奖励函数仍然是医疗保健强化学习（RL）的核心挑战，因为医疗保健的结果稀疏、延迟且难以指定。虽然结构化数据捕捉生理状态，但它们往往无法反映患者临床轨迹的整体质量，包括恢复动态、治疗负担和稳定性。相比之下，临床叙述总结了纵向推理，并隐含地编码了治疗有效性的评估。我们提出了临床叙事信息偏好奖励（CN-PR），这是一个直接从出院摘要学习奖励功能的框架，将其视为对教师级别偏好的可扩展监督。使用大型语言模型，我们推导出轨迹质量评分（TQS）并构建患者轨迹的成对偏好，从而通过结构化的基于偏好的目标实现奖励学习。为了考虑叙事信息量的变异性，我们引入了一个信心信号，该信号根据监督与决策任务的相关性来加权监督。习得的回报与轨迹质量高度一致（Spearman rho = 0.63），并使政策始终与改善恢复相关结果相关，包括增加无器官支持天数和更快的休克解决，同时保持相当的死亡率表现。这些影响在外部验证下持续存在。我们的结果表明，叙事衍生的监督为动态治疗方案的手工制作或基于结果的奖励设计提供了一种可扩展和富有表现力的替代方案。

[阅读原文](https://arxiv.org/abs/2604.10783)

---

## 34. 从对比中学习：从多样化搜索轨迹中合成推理路径

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Peiyang Liu, Zhirui Chen, Xi Wang, Di Liang, Youru Li, Zhi Cai, Wei Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Contrastive Reasoning Path Synthesis (CRPS), a method for synthesizing reasoning supervision from search trajectories, directly aligning with latent reasoning and self-improvement loops.

**摘要**: arXiv：2604.11365v1宣布类型：新摘要：蒙特卡洛树搜索（MCTS）已被广泛用于自动推理数据探索，但当前的监督提取方法仍然效率低下。标准方法只保留单一的最高回报轨迹，丢弃许多探索路径中存在的比较信号。在这里，我们介绍了\textBF{对比推理路径合成（CRPS）}，这是一个将监督提取从过滤过程转换为合成过程的框架。CRPS使用结构化反思过程来分析高质量和低质量搜索轨迹之间的差异，提取有关战略支点和局部故障模式的明确信息。这些见解指导推理链的合成，这些链融合了成功模式，同时避免已识别的陷阱。我们根据经验表明，仅对60 K个CPR合成示例进行微调的模型与在标准拒绝采样中获得的59万个示例上训练的基线的性能相匹配或超过，数据集大小减少了20 $\times $。此外，CRPS提高了对域外基准的概括性，证明从成功与失败之间的对比中学习比仅从成功中学习可以产生更多可转移的推理能力。

[阅读原文](https://arxiv.org/abs/2604.11365)

---

## 35. ASPIRin：用于全复式语音语言模型中交互优化强化学习的动作空间投影

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chi-Yuan Hsiao, Ke-Han Lu, Yu-Kuan Fu, Guan-Ting Lin, Hsiao-Tsung Hung, Hung-yi Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an RL framework (ASPIRin) with action space projection to optimize turn-taking in speech LMs, directly addressing RL for LLM behavior improvement.

**摘要**: arXiv：2604.10065v1宣布类型：新摘要：端到端双环语音语言模型（SLC）需要精确的轮流来实现自然交互。然而，通过标准原始令牌强化学习（RL）优化时间动态会降低语义质量，导致严重的生成崩溃和重复。我们提出了ASPIRin，这是一个交互式优化的RL框架，它显式地将何时说话与说什么分开。使用动作空间投影，ASPIRin将文本词汇映射到粗粒度的二进制状态（活动语音与非活动静音）。通过应用基于规则的奖励的组相对策略优化（GRPO），它平衡了用户中断和响应延迟。经验评估表明，ASPIRin优化了回合转换、反向引导和暂停处理的交互性。至关重要的是，与标准GRPO相比，将计时与标记选择隔离可以保留语义一致性，并将重复n元语法的部分减少了50%以上，有效地消除了退化性重复。

[阅读原文](https://arxiv.org/abs/2604.10065)

---

## 36. CASK：用于推理痕迹的核心感知选择性KV压缩

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Buseong Kim, Heejun Gwon

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel KV cache compression method (CASK) that preserves reasoning behavior by protecting a core reasoning trace and consolidating scratch space, directly targeting latent reasoning efficiency.

**摘要**: arXiv：2604.10900v1宣布类型：新摘要：在执行长式推理的大型语言模型中，KV缓存会随着解码长度的增长而迅速增长，从而在内存和推理稳定性方面造成瓶颈。现有的面向推理的KV压缩主要遵循以驱逐为中心的观点：更准确地估计代币重要性，然后丢弃排名较低的条目。我们的分析表明，单独的记分器细化通常无法实质上重新组织实际的保持集，因此可能不是保留推理行为的主要杠杆。相反，我们将推理KN压缩框架为一个保持行为的结构化合并问题。CASK将解码时推理轨迹划分为一个受保护的核心，该核心锚定答案形成和中间状态，以及具有高冗余度的可合并划痕。核心被保留，而选择性巩固仅应用于划痕。为了解决预算繁重的制度，即在解码级压缩变得活跃之前，前置代码可能会耗尽预算，CASK进一步使用两阶段设计：前置代码驱逐，然后是解码级合并。在H100推理门上，CASK在AIM 24和AIM 25上的预算匹配时表现出比TriAttention更高的全KV连续保真度，并且经常出现cask@384 > triattention@512交叉。在预算繁重的重播中，multi_news和vcsum充当解码活跃证人，而qmsum和gov_report暴露precise_budget_exhausted边界。总体证据支持一个简单的结论：有效的推理KV压缩与其说依赖于更复杂的评分器工程，不如说依赖于将核心保留与选择性划痕合并相结合以降低可用预算边界。

[阅读原文](https://arxiv.org/abs/2604.10900)

---

## 37. 强化学习中的熵控制方法的比较理论分析

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ming Lei, Christophe Baehr

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a comparative theoretical analysis of entropy control methods in RL, directly relevant to scalable RL training for LLMs and addressing policy collapse.

**摘要**: arXiv：2604.09676v1宣布类型：新摘要：强化学习（RL）已成为增强大型语言模型（LLM）推理的关键方法，但可扩展训练往往会受到策略信息量快速崩溃的阻碍，从而导致过早收敛和性能饱和。本文对两种信息量控制策略进行了比较理论分析：传统的信息量规则化和最近提出的基于协方差的机制。我们在softmax参数化下建立了一个统一的熵动力学框架，表明熵变化由log概率和logit更新之间的协方差决定。我们的分析表明，传统的熵正规化引入了密集、持续的偏差，该偏差会修改平稳条件，从而导致次优策略，而基于协方差的方法则选择性地正规化高协方差令牌的稀疏子集，并在正规化系数被调整时实现渐进无偏性。这些结果为LLM后训练中的信息量控制提供了原则性指南，并对将RL扩展到更大的模型和更复杂的推理任务具有影响。

[阅读原文](https://arxiv.org/abs/2604.09676)

---

## 38. 协同多Agent推理生成算法增强谋杀推理中的不完全信息推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Keyang Zhong, Junlin Xie, Hefeng Wu, Haofeng Li, Guanbin Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-agent framework with a GRPO-based RL training stage to enhance VLM reasoning under imperfect information, directly aligning with RL for LLMs and self-improving agent criteria.

**摘要**: arXiv：2604.11741v1宣布类型：新摘要：视觉语言模型（VLM）在感知任务中表现出了令人印象深刻的能力，但它们在具有不完美和欺骗性信息的多人游戏环境下的复杂多跳推理中会退化。本文研究了一个代表性的多人游戏任务--谋杀之谜游戏，它需要根据具有不同意图的角色提供的部分线索推断隐藏的真相。为了应对这一挑战，我们提出了一种协作多代理框架，用于评估和合成高质量、角色驱动的多人游戏脚本，从而实现针对角色身份定制的细粒度交互模式（即，凶手vs无辜者）。我们的系统通过协调的代理交互生成丰富的多模式上下文，包括角色背景故事、视觉和文本线索以及多跳推理链。我们设计了一种两阶段代理监控的训练策略来增强VLM的推理能力：（1）对模拟不确定性和欺骗的策划和合成数据集进行基于思想链的微调;（2）基于GRPO的强化学习，具有代理监控的奖励塑造，鼓励模型开发特定于角色的推理行为和有效的多模式多跳推理。大量实验表明，我们的方法显着提高了VLM在叙事推理、隐藏事实提取和欺骗弹性理解方面的性能。我们的贡献为在不确定、对抗和社会复杂条件下训练和评估VLM提供了可扩展的解决方案，为不完美信息下多模式多跳推理的未来基准奠定了基础。

[阅读原文](https://arxiv.org/abs/2604.11741)

---

## 39. 仅在需要时推理：通过模型内部不确定性进行高效生成奖励建模

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chao Xue, Yao Wang, Mengqiao Liu, Di Liang, Xingsheng Han, Peiyang Liu, Xianjie Wu, Chenyao Lu, Lei Jiang, Yu Lu, Haibo Shi, Shuang Liang, Minlong Peng, Flora D. Salim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an efficient generative reward modeling framework (E-GRM) that uses model-internal uncertainty to selectively trigger CoT reasoning, directly improving reasoning-aware reward design.

**摘要**: arXiv：2604.10072v1宣布类型：新摘要：生成奖励模型（GRM）的最新进展证明了其通过思想链（CoT）激励增强LLM推理能力的潜力。尽管取得了这些成果，但GRM的现有实现仍存在两个关键限制。首先，CoT提示不加区别地应用于所有输入，无论其固有的复杂性如何。这为适合快速、直接推理的任务带来了不必要的计算成本。其次，现有的方法主要依赖于基于投票的机制来评估CoT输出，而这种机制在评估推理质量方面往往缺乏粒度和精确性。在本文中，我们提出了E-GRM，这是一个基于模型内部不确定性的高效生成性回报建模框架。E-GRM利用并行模型生成的收敛行为来估计不确定性，并仅在需要时选择性地触发CoT推理，而不依赖于手工制作的特征或任务相关的信号。为了提高奖励保真度，我们引入了一个轻量级的区分评分器，该评分器经过混合回归-排名目标训练，以提供推理路径的细粒度评估。多个推理基准的实验表明，E-GRM大幅降低了推理成本，同时不断提高答案准确性，证明模型内部不确定性是高效推理感知奖励建模的有效且通用的信号。

[阅读原文](https://arxiv.org/abs/2604.10072)

---

## 40. ZoomR：通过多粒度关键值检索进行内存高效推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: David H. Yang, Yuxuan Zhu, Mohammad Mohammadi Amiri, Keerthiram Murugesan, Tejaswini Pedapati, Subhajit Chaudhury, Pin-Yu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ZoomR, a method for memory-efficient reasoning via multi-granularity KV cache retrieval and compression of verbose thoughts, directly targeting latent reasoning efficiency.

**摘要**: arXiv：2604.10898v1宣布类型：新摘要：大型语言模型（LLM）在复杂推理任务上表现出了出色的性能，但通常需要在得出最终答案之前生成长时间的中间想法。在生成过程中，LLM依赖于密钥-值（KV）缓存进行自回归解码。然而，KV缓存的内存占用随着输出长度的增加而增加。之前关于KV缓存优化的工作主要集中在压缩长输入上下文，同时保留完整的KV缓存以进行解码。对于需要长时间输出生成的任务，这会导致计算和存储成本增加。在本文中，我们介绍了ZoomR，这是一种新颖的方法，使LLM能够自适应地将冗长推理思想压缩到摘要中，并使用动态KV缓存选择策略，该策略利用这些摘要，同时还战略性地“放大”细粒度细节。通过在解码期间使用摘要键作为粗粒度索引，ZoomR使用查询仅检索最重要思想的详细信息。这种分层策略通过避免每一步的全缓存关注，显着减少了内存使用。数学和推理任务的实验表明，与基线相比，我们的方法实现了有竞争力的性能，同时将推理记忆需求减少了超过4美元。这些结果表明，多粒度KV选择可以实现更高的内存效率解码，尤其是对于长输出生成。

[阅读原文](https://arxiv.org/abs/2604.10898)

---

## 41. TInR：探索大型语言模型中的工具内化推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qiancheng Xu, Yongqi Li, Fan Liu, Hongru Wang, Min Yang, Wenjie Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a tool-internalized reasoning framework using a three-phase pipeline including reinforcement learning with specific rewards, directly aligning with RL for LLMs and latent reasoning.

**摘要**: arXiv：2604.10788v1宣布类型：新摘要：通过在推理期间使用外部工具扩展大型语言模型（LLM）的能力，工具集成推理（TLR）已成为一个有前途的方向。现有的TLR方法通常在推理过程中依赖于外部工具文档。然而，这会导致工具掌握困难、工具大小限制和推理效率低下。为了缓解这些问题，我们探索了工具内化推理（TInR），旨在通过内化到LLM中的工具知识来促进推理。实现这一目标提出了显着的要求，包括工具内化和工具推理协调。为了解决这些问题，我们提出了TInR-U，这是一个用于统一推理和工具使用的工具内化推理框架。TInR-U通过三个阶段的管道进行训练：1）具有双向知识对齐策略的工具内化; 2）使用高质量推理注释的监督微调预热，以及3）具有TInR特定奖励的强化学习。我们全面评估我们的方法跨域和域外设置。实验结果表明，TInR-U在两种设置下都取得了优异的性能，突出了其有效性和效率。

[阅读原文](https://arxiv.org/abs/2604.10788)

---

## 42. MedLVR：用于可靠医疗视觉问题回答的潜在视觉推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Suyang Xi, Songtao Hu, Yuxiang Lai, Wangyun Dan, Yaqi Liu, Shansong Wang, Xiaofeng Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MedLVR, a latent visual reasoning framework for medical VQA that uses iterative latent state refinement and Visual-Latent Policy Optimization (VLPO), aligning with latent CoT/reasoning.

**摘要**: arXiv：2604.09757v1宣布类型：新摘要：医学视觉语言模型（VLM）在医学视觉问答（VQA）方面表现出了强大的潜力，但它们的推理在很大程度上仍然以文本为中心：图像一旦被编码为静态上下文，随后的推理由语言主导。这种范式在临床场景中从根本上受到限制，其中准确的答案通常取决于微妙的局部视觉证据，而这些证据无法可靠地保存在静态嵌入中。我们提出了\textsk {MedLVR}，这是一个潜在视觉推理框架，它将显式视觉证据状态引入到自回归解码中。\textsk {MedLVR}不是仅仅依赖基于文本的中间推理，而是通过将隐藏状态重新用作连续的潜在步骤来在解码器内交织一个简短的潜在推理片段，从而能够在生成答案之前迭代地保存和细化与查询相关的视觉证据。为了支持有效的视觉监督，我们采用了两阶段训练策略：感兴趣区域（Investment）监督微调将潜在状态与临床相关图像证据对齐，视觉潜在政策优化（VLPO）进一步优化潜在推理和结果级别奖励下的答案生成。OmniMedVQA和五个外部医疗VQA基准的实验表明，\textsk {MedLVR}始终优于最近的推理基线，并将平均得分从Qwen 2.5-BL-7 B主干的48.3%提高到53.4%。这些结果表明，潜在视觉推理为保存诊断相关视觉证据和提高医学VQA的可靠性提供了有效机制。

[阅读原文](https://arxiv.org/abs/2604.09757)

---

## 43. 认知支点和视觉锚定：揭露和纠正多模式推理模型中的幻觉

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhe Qian, Yanbiao Ma, Zhuohan Ouyang, Zhonghua Wang, Zhongxing Xu, Fei Luo, Xinyu Liu, Zongyuan Ge, Yike Guo, Jungong Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes V-STAR, a training paradigm using a Hierarchical Visual Attention Reward (HVAR) within the GRPO framework to anchor multimodal reasoning to visual input, directly aligning with RL for LLMs via reward design.

**摘要**: arXiv：2604.10219v1宣布类型：新摘要：多模式大型推理模型（MLRM）通过测试时间计算缩放在视觉推理方面取得了显着的进步，但长链推理仍然容易产生幻觉。我们发现了一种令人担忧的现象，称为推理视觉真相脱节（RVTD）：幻觉与通常表现出高熵状态的认知分歧点密切相关。我们将这种漏洞归因于视觉语义锚定的崩溃，该锚定位于网络中间层内;具体来说，在这些高不确定性转变期间，模型无法查询视觉证据，而是恢复到语言先验。因此，我们主张从纯粹的结果层面监督转向通过细粒度的内部注意力指导来加强它。为此，我们提出了V-STAR（具有注意力强化的视觉结构训练），这是一种轻量级、整体的训练范式，旨在内化视觉感知推理能力。我们方法的核心是分层视觉注意力奖励（HCAR），集成在GRPO框架中。在检测到高熵状态后，该机制动态地激励关键中间层的视觉注意力，从而将推理过程锚定回视觉输入。此外，我们还引入了强制反射机制（FRM），这是一种轨迹编辑策略，通过触发高熵认知分歧点周围的反射并鼓励针对视觉输入验证后续步骤来破坏认知惯性，从而将外部去偏置干预转化为缓解幻觉的内在能力。

[阅读原文](https://arxiv.org/abs/2604.10219)

---

## 44. ExecButton：通过指南模型有效引导黑匣子LLM

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Vijay Lingam, Aditya Golatkar, Anwesan Pal, Ben Vo, Narayanan Sadagopan, Alessandro Achille, Jun Huan, Anoop Deoras, Stefano Soatto

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ExecTune, a training recipe using structure-aware reinforcement learning to optimize guide models for steering black-box LLMs, directly aligning with RL for LLMs.

**摘要**: arXiv：2604.09741v1宣布类型：新摘要：对于通过黑匣子API部署的大型语言模型，重复性推断成本通常超过一次性训练成本。这激励了组成的代理系统，将昂贵的推理摊销为可重复使用的中间表示。我们研究了一类广泛的此类系统，称为引导核心政策（GCoP），其中引导模型生成由黑匣子核心模型执行的结构化策略。这种抽象包含了基础、监督和指导者风格的方法，这些方法的主要区别在于指导的训练方式。我们在对成本敏感的效用目标下对GCoP进行了形式化，并表明端到端性能由指南平均可执行性决定：指南生成的策略能够被核心忠实执行的可能性。我们的分析表明，现有的GCoP实例化常常无法在部署约束下优化可执行性，从而导致策略脆弱和计算效率低下。受这些见解的启发，我们提出了ExecTune，这是一种有原则的培训食谱，它结合了教师指导的接受抽样、监督微调和结构感知强化学习，以直接优化语法有效性、执行成功和成本效率。在数学推理和代码生成基准测试中，采用ExecTune的GCoP将准确性比之前最先进的基线提高了高达9.2%，同时将推理成本降低了高达22.4%。它使Claude Haiku 3.5在数学和代码任务方面都优于十四行诗3.5，并且绝对准确率仅为十四行诗4的1.7%，成本低38%。除了效率之外，GCoP还通过更新指南而无需重新培训核心来支持模块化适应。

[阅读原文](https://arxiv.org/abs/2604.09741)

---

## 45. OOWM：通过面向对象的程序化世界建模来构建目标推理和规划

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hongyu Chen, Liang Lin, Guangrun Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes OOWM, a structured embodied reasoning framework that uses outcome-based rewards (GRPO) to implicitly optimize its object-oriented reasoning structure, aligning with RL for LLMs.

**摘要**: arXiv：2604.09580v1宣布类型：新摘要：标准思想链（CoT）激励使大型语言模型（LLM）具有推理能力，但其对线性自然语言的依赖本质上不足以在具体任务中进行有效的世界建模。虽然文本提供了灵活性，但它未能显式地表示稳健的机器人规划所需的状态空间、对象层次结构和因果依赖关系。为了解决这些限制，我们提出了面向对象的世界建模（OOWM），一个新的框架，结构体现推理通过镜头的软件工程形式主义。我们重新定义世界模型不是作为一个潜在的向量空间，而是作为一个显式的符号元组$W = \langle S，T \rangle$：一个实例化环境状态$S$的状态抽象（$G_\text{state}$），加上一个表示转换逻辑$T：S \times A \rightarrow S '$的控制策略（$G_\text{control}$）。OOWM利用统一建模语言（UML）来实现这一定义：它采用类图将视觉感知置于严格的对象层次结构中，并采用活动图将计划操作化为可执行的控制流。此外，我们引入了一个三阶段的训练管道相结合的监督微调（SFT）与组相对策略优化（GRPO）。至关重要的是，该方法利用最终计划中基于结果的奖励来隐式优化底层的面向对象推理结构，即使在稀疏注释的情况下也能实现有效的学习。对MUom-30 k基准的广泛评估表明，OOWM在规划一致性、执行成功和结构保真度方面显着优于非结构化文本基线，为结构化体现推理建立了新范式。

[阅读原文](https://arxiv.org/abs/2604.09580)

---

## 46. RTMC：通过推出树进行分步信用分配

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tao Wang, Suhang Zheng, Xiaoxiao Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Rollout-Tree Monte Carlo (RTMC), a novel critic-free credit assignment method for multi-step agentic RL, directly improving LLM-based code agents.

**摘要**: arXiv：2604.11037v1宣布类型：新摘要：多步代理强化学习受益于细粒度信用分配，但现有方法提供的选择有限：GRPO等无批评方法为轨迹中的每个动作分配统一的优势，而习得价值网络则引入了显着的额外费用，并且在稀疏奖励下可能很脆弱。我们观察到，针对同一问题的群组展开通常会穿越重叠的中间状态，隐含地形成一棵树，其分支在连续的决策点处分叉。基于这一见解，我们引入了卷取树蒙特卡洛（RTMC）优势估计，该估计汇总共享共同状态的卷取中的回报统计数据，以产生每一步的Q值和优势--无需任何有经验的批评者。状态动作签名系统将原始交互历史压缩为紧凑、可比较的表示，使交叉部署状态匹配变得易于处理。在SWE-based验证中，RTMC将pass@1比GRPO提高了3.2个百分点。

[阅读原文](https://arxiv.org/abs/2604.11037)

---

## 47. 通过可追溯细化实现意图一致的形式规范综合

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhe Ye, Aidan Z. H. Yang, Huangyuan Su, Zhenyu Liao, Samuel Tenka, Zhizhen Qin, Udaya Ghai, Dawn Song, Soonho Kong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a traceable refinement framework for formal specification synthesis that generates training data from refinement trajectories, enabling self-improvement for LLMs.

**摘要**: arXiv：2604.10392v1宣布类型：新摘要：大型语言模型越来越多地用于从自然语言生成代码，但确保正确性仍然具有挑战性。形式验证提供了一种原则性的方法来通过证明程序满足形式规范来获得此类保证。然而，规范在现实世界的代码库中经常缺失，编写高质量的规范仍然昂贵且需要专业知识。我们介绍了VeriSpecGen，这是一个可追溯的细化框架，通过需求级别归因和本地化修复在精益中合成意图一致的规范。VeriSpecGen将自然语言分解为原子需求，并生成具有显式可追溯性映射的针对需求的测试，以验证生成的规范。当验证失败时，可追溯性将失败归因于特定要求，从而实现有针对性的条款级修复。VeriSpecGen使用Claude Opus 4.5完成VERINA SpecGen任务的86.6%，在不同模型系列和规模中比基线提高了31.8个百分点。除了推理时间收益之外，我们还从VeriSpecGen细化轨迹生成343 K个训练示例，并证明对这些轨迹的训练可以相对地将规范合成提高62-106%，并将收益转移到一般推理能力。

[阅读原文](https://arxiv.org/abs/2604.10392)

---

## 48. PhyMix：通过隐式-显式优化实现物理一致的单图像3D室内场景生成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dongli Wu, Jingyu Hu, Ka-Hei Hui, Xiaobao Wei, Chengwen Luo, Jianqiang Li, Zhengzhe Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Scene-GRPO, a critic-free group-relative policy optimization method that uses a physics evaluator as a preference signal for RL, aligning with RL for LLMs via novel reward design and RL pipelines.

**摘要**: arXiv：2604.10125v1宣布类型：新摘要：现有的单图像3D室内场景生成器通常会产生视觉上看似合理的结果，但不符合现实世界的物理学，从而限制了它们在机器人、具体人工智能和设计方面的可靠性。为了检查这一差距，我们引入了一个统一的物理评估器，该评估器测量四个主要方面：几何先验、接触、稳定性和可部署性，并进一步分解为九个子约束，建立了第一个衡量物理一致性的基准。基于这位评估者，我们的分析表明，最先进的方法在很大程度上仍然不受物理影响。为了克服这一限制，我们进一步提出了一个框架，将物理评估者的反馈集成到训练和推理中，增强生成场景的物理可信度。具体来说，我们提出了PhyMix，它由两个补充组件组成：（i）通过Scene-GRPO进行隐式对齐，这是一种无批评的群体相对政策优化，利用物理评估器作为偏好信号，并将采样偏向物理可行的布局，以及（ii）通过即插即用测试时间优化器（TTO）进行显式细化，该优化器使用可区分的评估器信号来纠正生成期间的剩余违规。总的来说，我们的方法统一了评估、奖励塑造和推断时间纠正，产生视觉上忠实且物理上合理的3D室内场景。广泛的合成评估证实了视觉保真度和物理可信度方面的最新性能，而风格化和现实世界图像中的大量定性示例进一步展示了该方法的稳健性。我们将在发布后发布代码和模型。

[阅读原文](https://arxiv.org/abs/2604.10125)

---

## 49. Geoparing：使用统一形式语言进行平面和立体几何图形解析

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Peijie Wang, Ming-Liang Zhang, Jun Cao, Chao Deng, Dekang Ran, Hongda Sun, Pi Bu, Xuan Zhang, Yingyao Wang, Jun Song, Bo Zheng, Fei Yin, Cheng-Lin Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training paradigm combining Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards for geometry parsing, directly matching RL for LLMs with explicit reward design.

**摘要**: arXiv：2604.11600v1宣布类型：新摘要：多模式大型语言模型（MLLM）取得了显着的进展，但仍然在几何推理方面遇到困难，主要是由于细粒度视觉元素的感知瓶颈。虽然形式语言有助于理解平面几何，但需要空间理解的立体几何在很大程度上仍未被探索。在本文中，我们通过设计一种统一的形式语言来应对这一挑战，该语言集成了平面和立体几何，全面涵盖了几何结构和语义关系。我们构建GDP-29 K，这是一个大规模数据集，包括从不同的现实世界来源收集的20 k个平面和9 k个立体几何样本，每个样本都与其地面真相形式描述配对。为了确保语法正确性和几何一致性，我们提出了一种训练范式，将监督微调与通过可验证奖励的强化学习相结合。实验表明，我们的方法实现了最先进的解析性能。此外，我们证明，我们解析的形式描述可以作为关键的认知框架，显着增强MLLM执行下游几何推理任务的能力。我们的数据和代码可在Geoparsing上获取。

[阅读原文](https://arxiv.org/abs/2604.11600)

---

## 50. 代理规则会塑造还是扭曲？编码代理中的护栏击败指导

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xing Zhang, Guanghui Wang, Yanwei Cui, Wei Qiu, Ziyuan Li, Bing Zhu, Peiyang He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Empirically studies how natural language rules (guardrails) affect coding agent performance, analyzing effects through the lens of potential-based reward shaping (PBRS).

**摘要**: arXiv：2604.11088v1宣布类型：新摘要：开发人员越来越多地通过自然语言指令文件引导AI编码代理（例如，CLAUDE.md，.cursorrules），但还没有对照研究衡量这些规则是否真正提高了代理性能，或者哪些属性使规则有益。我们从GitHub中抓取了679个此类文件（25，532个规则），并进行了第一次大规模实证评估，在SWE平台上使用最先进的编码代理运行了5，000多个代理运行。规则将绩效提高7- 14个百分点，但随机规则的帮助与专家策划的规则一样大--这表明规则通过上下文启动而不是具体指令发挥作用。消极约束（“不重构不相关的代码”）是唯一对个人有利的规则类型，而积极指令（“遵循代码风格”）则积极有害--我们通过基于潜力的奖励塑造（PBRS）的视角分析了这一模式。此外，个别规则大多是孤立的，但集体来说是有益的，最多50条规则都不会降级。这些发现暴露了隐藏的可靠性风险--善意的规则通常会降低代理性能--并为安全代理配置提供了明确的原则：限制代理不能做的事情，而不是规定他们应该做的事情。

[阅读原文](https://arxiv.org/abs/2604.11088)

---

## 51. 具有轨迹诱导偏好优化的移动图形用户界面代理隐私个性化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhixin Lin, Jungang Li, Dongliang Xu, Shidong Pan, Yibo Shi, Yuchi Liu, Yuecong Min, Yue Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Trajectory Induced Preference Optimization (TIPO), a new preference optimization method for personalizing mobile GUI agents, directly aligning with self-improving agent frameworks.

**摘要**: arXiv：2604.11259v1宣布类型：新摘要：由多模式大型语言模型（MLLM）支持的移动图形用户界面代理可以在移动设备上执行复杂任务。尽管取得了这一进步，但大多数现有系统仍然优化任务成功或效率，忽视了用户的隐私个性化。本文研究了经常被忽视的代理个性化问题。我们观察到个性化会在执行轨迹中引发系统性结构性差异。例如，隐私第一的用户通常更喜欢保护行为，例如，拒绝权限、注销和最大限度地减少暴露，导致实用程序优先用户的执行轨迹在逻辑上不同。这种可变长度和结构上不同的轨迹使得标准偏好优化不稳定且信息较少。为了解决这个问题，我们提出了轨迹诱导偏好优化（TIPO），它使用偏好强度加权来强调与隐私相关的关键步骤，并使用填充门控来抑制对齐噪音。我们的隐私偏好数据集的结果显示，TIPO改善了角色一致性和区别性，同时保持了强大的任务可执行性，实现了65.60%的SR、46.22的合规性和66.67%的PD，超过了现有的各种图形用户界面任务的优化方法。该代码和数据集将在https://github.com/Zhixin-L/TIPO上公开发布。

[阅读原文](https://arxiv.org/abs/2604.11259)

---

## 52. 目标：具有空间价值地图的意图感知统一世界动作建模

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Liaoyuan Fan, Zetian Xu, Chen Cao, Wenyao Zhang, Mingqi Yuan, Jiayu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-distillation reinforcement learning stage for robot action generation, aligning with RL methods for improving agent behavior via reward design.

**摘要**: arXiv：2604.11135v1宣布类型：新摘要：预训练的视频生成模型为机器人控制提供了强大的先验，但如果没有大量的机器人特定训练，现有的统一世界动作模型仍然难以解码可靠的动作。我们将这种限制归因于结构不匹配：虽然视频模型捕捉场景如何演变，但动作生成需要明确地推理在哪里交互和底层操纵意图。我们引入AIM，这是一个意图感知的统一世界动作模型，通过显式的空间界面弥合这一差距。AIM不是直接从未来的视觉表示中解码动作，而是预测对齐的空间价值地图，该地图编码与任务相关的交互结构，从而实现对未来动态的面向控制的抽象。AIM基于预先训练的视频生成模型，在共享的混合变形器架构中联合建模未来观察和价值地图。它利用意图-因果注意力，专门通过价值表示将未来信息发送到行动分支。我们进一步提出了一个自我提炼强化学习阶段，该阶段冻结视频和价值分支，并使用从投影的价值地图响应以及稀疏任务级信号中衍生的密集奖励仅优化动作头部。为了支持训练和评估，我们构建了一个包含30 K操纵轨迹的模拟数据集，并具有同步的多视图观察、动作和值图注释。RoboTwin 2.0基准测试的实验表明，AIM的平均成功率为94.0%，显着优于之前的统一世界动作基线。值得注意的是，这种改进在长视野和接触敏感的操纵任务中更加明显，证明了显式空间意图建模作为视觉世界建模和机器人控制之间桥梁的有效性。

[阅读原文](https://arxiv.org/abs/2604.11135)

---

## 53. 巨人：来自科学文献的生成洞察力预测

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Joy He-Yueya, Anikait Singh, Ge Gao, Michael Y. Li, Sherry Yang, Chelsea Finn, Emma Brunskill, Noah D. Goodman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GIANTS-4B, an LM trained via RL to optimize a proxy reward for scientific insight anticipation, directly aligning with RL for LLMs.

**摘要**: arXiv：2604.09793v1宣布类型：新摘要：科学突破通常是从将先前的想法合成为新颖的贡献中产生的。虽然语言模型（LM）在科学发现方面表现出了希望，但它们执行这种有针对性的、基于文献的综合的能力仍然没有得到充分的探索。我们引入了洞察力预测，这是一项生成任务，其中模型从其基础母论文中预测下游论文的核心洞察力。为了评估这种能力，我们开发了GiantsBench，这是一个由八个科学领域的17，000个示例组成的基准，其中每个示例都由一组母论文与下游论文的核心见解相匹配。我们使用LM法官来评估模型，该法官对生成的洞察和地面真相洞察之间的相似性进行评分，并表明这些相似性得分与专家人类评级相关。最后，我们介绍了GIANTS-4 B，这是一种通过强化学习（RL）训练的LM，可使用这些相似性分数作为代理奖励来优化洞察预期。尽管其开源架构较小，但GIANTS-4 B的表现优于专有基线，并可推广到未见过的领域，与gemini-3-pro相比，相似性得分相对提高了34%。人类评估进一步表明，GIANTS-4 B产生的见解比基本模型在概念上更清晰。此外，SciJudge-30 B是一个经过训练的第三方模型，旨在通过可能的引用影响来比较研究摘要，该模型预测，GIANTS-4 B产生的见解更有可能导致更高的引用，在68%的成对比较中，他们更喜欢它们而不是基本模型。我们发布我们的代码、基准和模型来支持未来自动化科学发现的研究。

[阅读原文](https://arxiv.org/abs/2604.09793)

---

## 54. 摆脱上下文瓶颈：通过强化学习为LLM代理进行主动上下文治疗

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xiaozhe Li, Tianyi Lyu, Yizhao Yang, Liang Shan, Siyi Yang, Ligao Zhang, Zhuoyi Huang, Qingwen Liu, Yang Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a reinforcement learning-trained ContextCurator agent that actively prunes noise and preserves reasoning anchors to improve long-horizon agent performance.

**摘要**: arXiv：2604.11462v1宣布类型：新摘要：由于“上下文瓶颈”和“中间迷失”现象，大型语言模型（LLM）难以应对长期任务，即冗长环境累积的噪音会降低多轮交互的推理能力。为了解决这个问题，我们引入了一个共生框架，将上下文管理与任务执行分开。我们的架构将轻量级、专业的策略模型ContextCurator与强大的冻结基础模型TaskExecutor配对。通过强化学习训练，ContextCurator积极减少工作记忆中的信息熵。它积极修剪环境噪音，同时保留推理锚点，即对未来推论至关重要的稀疏数据点。在WebArena上，我们的框架将Gemini-3.0-Flash的成功率从36.4%提高到了41.2%，同时将代币消耗量减少了8.8%（从47.4K提高到43.3K）。在DeepSearch上，它的成功率为57.1%，而为53.9%，同时将代币消耗量减少了8倍。值得注意的是，7 B ContextCurator与GPT-4 o的上下文管理性能相匹配，为自主长期代理提供了可扩展且计算高效的范式。

[阅读原文](https://arxiv.org/abs/2604.11462)

---

## 55. 通过物理模拟器上的强化学习解决物理奥林匹克竞赛

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mihir Prabhudesai, Aryan Satpathy, Yangmin Li, Zheyang Qin, Nikash Bhardwaj, Amir Zadeh, Chuan Li, Katerina Fragkiadaki, Deepak Pathak

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes using physics simulators to generate synthetic QA data and training LLMs via reinforcement learning, directly aligning with RL for LLMs for scalable data generation and skill acquisition.

**摘要**: arXiv：2604.11805v1宣布类型：新摘要：随着DeepSeek-R1的出现，我们见证了LLM推理能力的显着进步。然而，这一进步的大部分是由大量的互联网问答（QA）对推动的，这是未来的一个主要瓶颈，因为此类数据规模有限，并且主要集中在数学等领域。相比之下，物理学等其他科学缺乏大规模QA数据集来有效训练具有推理能力的模型。在这项工作中，我们表明物理模拟器可以作为训练LLM物理推理的强大替代监督来源。我们在物理引擎中生成随机场景，从模拟交互中创建合成问答对，并在此合成数据上使用强化学习来训练LLM。我们的模型表现出了到现实世界物理基准的零射击从实时到真实的转换：例如，仅在合成模拟数据上进行训练可以在不同模型尺寸中将IPhO（国际物理奥林匹克竞赛）问题的性能提高5 - 10个百分点。这些结果表明，物理模拟器可以充当可扩展的数据生成器，使LLM能够获得超越互联网规模QA数据限制的深度物理推理技能。代码可访问：www.example.com。

[阅读原文](https://arxiv.org/abs/2604.11805)

---

## 56. 使用潜在基础模型进行参数化模拟的PDL空间的统计探索

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Abhijeet Vishwasrao, Francisco Giral, Mahmoud Golestanian, Federica Tonti, Andrea Arroyo Ramo, Adrian Lozano-Duran, Steven L. Brunton, Sergio Hoyas, Soledad Le Clainche, Hector Gomez, Ricardo Vinuesa

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hierarchical multi-agent LLM framework that orchestrates a closed loop of hypothesis, experimentation, and verification for autonomous scientific discovery, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2604.09584v1宣布类型：新摘要：流动物理学和由偏微方程（PDEs）控制的更广泛的物理现象本质上是连续的、多维的，并且往往是混乱的。传统上，研究人员使用实验室实验和/或计算成本高昂的数值模拟来探索这些丰富的时空PDL解空间。这严重限制了自动化和大规模探索，与药物发现或材料科学等领域不同，在这些领域，离散的、可标记化的表示自然地与大型语言模型交互。我们通过将多智能体LLM与潜在基础模型（LFM）相结合来解决这个问题，LFM是一种参数化模拟上的生成模型，可以学习流场的显式、紧凑且不纠缠的潜在表示，从而能够在管理PDL参数和边界条件方面进行持续探索。LFM充当按需代理模拟器，允许代理以可忽略的成本查询任意参数配置。分层代理架构通过假设、实验、分析和验证的闭环来协调探索，并具有不需要用户支持的工具模块化界面。该框架应用于Re = 500时流过串联圆柱体的流动，自主评估了超过1，600个参数位置对，并发现了不同的标度定律：用于最小位移厚度的与状态相关的双模式结构和用于最大动量厚度的稳健线性标度，两种景观都表现出双极端结构，出现在近尾流到共同脱落状态的转变。学习到的物理表示与代理推理的结合为在PDE管辖的系统中自动科学发现建立了一般范式。

[阅读原文](https://arxiv.org/abs/2604.09584)

---

## 57. 范围：采用双路径自适应加权的信号校准政策蒸馏增强

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Binbin Zheng, Xing Ma, Yiheng Liang, Jingqing Ruan, Xiaoliang Fu, Kepeng Lin, Benchang Zhu, Ke Zeng, Xunliang Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dual-path adaptive training framework (SCOPE) for on-policy RL in LLMs, introducing signal-calibrated token-level supervision to improve credit assignment in reasoning alignment.

**摘要**: arXiv：2604.10688v1宣布类型：新摘要：政策上的强化学习已成为大型语言模型中推理对齐的主要范式，但其稀疏的结果级奖励使得代币级信用分配变得臭名昭著。按政策蒸馏（OPD）通过从教师模型引入密集的、代币级KL监督来缓解这种情况，但通常在所有部署中统一应用这种监督，忽略信号质量的根本差异。我们提出了信号校准的政策上蒸馏增强（SCOPE），这是一种双路径自适应训练框架，它通过正确性将政策上的部署路由到两个补充的监督路径中。对于不正确的轨迹，SCOPE执行教师困惑加权KL蒸馏，以优先考虑教师表现出真正纠正能力的情况，同时降低不可靠指导的权重。为了正确的轨迹，它应用学生困惑加权MLE，将强化集中在能力边界的低置信度样本上，而不是过度强化已经掌握的样本。这两种路径都采用组级标准化来自适应地校准权重分布，考虑到提示之间的固有难度差异。对六个推理基准的广泛实验表明，与竞争基线相比，SCOPE在Avg@32和Pass@32中的平均相对改进分别为11.42%和7.30%，证明了其一致的有效性。

[阅读原文](https://arxiv.org/abs/2604.10688)

---

## 58. 教学语言模型如何像学习者一样编码：学生模拟的对话序列化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Charles Koutcheme, Arto Hellas, Juho Leinonen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training pipeline combining supervised fine-tuning with preference optimization to align models with authentic student debugging behavior, directly relevant to RL for LLMs via preference optimization.

**摘要**: arXiv：2604.10720v1宣布类型：新摘要：模拟学习者在教育系统内如何行为和反应的人工模型是大规模评估辅导策略和反馈机制的有前途的工具。然而，编程教育中的许多现有方法依赖于推动大型专有语言模型，从而引发了对隐私、成本和依赖性的担忧。在这项工作中，我们提出了一种使用真实的学生过程数据训练开权人工编程学习者的方法。我们的方法将时间日志跟踪序列化为对话格式，将每个学生的问题解决过程表示为学习者与其自动评估系统之间的对话。学生代码提交和环境反馈（例如测试结果、成绩和错误跟踪）形成交替的对话回合，使模型能够从迭代调试过程中学习。我们还引入了一个将监督微调与偏好优化相结合的训练管道，以使模型与真实的学生调试行为保持一致。我们通过在真实学生提交Python编程作业的大规模数据集中以4B和8B规模训练Qwen模型来评估我们的框架。我们的结果表明，结合环境反馈增强了模型复制学生调试行为的能力，比之前的纯代码方法有所改进，并提示了大型语言模型在功能对齐和代码相似性方面的基线。我们发布代码以支持可重复性。

[阅读原文](https://arxiv.org/abs/2604.10720)

---

## 59. 您只能判断一次：单次向前传递中的多响应奖励建模

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yinuo Yang, Zixian Ma, Manasi Ganti, Jieyu Zhang, Ranjay Krishna

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-response reward model for efficient N-way preference learning and demonstrates its use in RL (GRPO) to improve policy models, directly matching RL for LLMs criteria.

**摘要**: arXiv：2604.10966v1宣布类型：新摘要：我们提出了一个区分性多模式奖励模型，可以在一次向前传递中对所有候选响应进行评分。传统的区分奖励模型独立评估每个响应，需要多次向前传递，每个潜在响应一次。我们的方法将多个响应与分离符标记连接起来，并在它们的纯量分数上应用交叉熵，从而实现直接比较推理和高效的$N$方式偏好学习。与传统的单响应评分相比，多响应设计还可以产生高达N倍$的时钟加速和FLOP减少。为了使$N$的奖励评估超出现有的成对基准，我们构建了两个新的基准：（1）MR$#2$Bench-Image包含对8个不同模型的响应的人类注释排名;（2）MR$#2$Bench-Video是一个基于大规模视频的奖励基准，源自94 K众包的成对人类判断，跨越19个模型，通过偏好图集成去噪。这两个基准都提供了从完整排名中抽样的4个响应评估变体。我们的模型建立在具有LoRA微调和轻量级MLP值头部的4 B视觉语言主干之上，在六个多模式奖励基准上实现了最先进的结果，包括MR $2 $Bench-Image、MR $2 $Bench-Video和其他四个现有基准。我们的模型优于现有的更大的生成性和歧视性奖励模型。我们进一步证明，当我们的奖励模型用于与GRPO进行强化学习时，可以产生改进的政策模型，这些模型可以保持标准多模式基准的性能，同时大幅提高开放式生成质量，在训练稳定性和开放式生成质量方面都大大优于单响应区分奖励模型（RM）基线。

[阅读原文](https://arxiv.org/abs/2604.10966)

---

## 60. 无需询问即可提供帮助：部署的主动代理系统，用于随叫随到支持，并具有持续自我改进

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Fengrui Liu, Xiao He, Tieying Zhang

**机构**: ByteDance (Volcano Engine)

**💡 亮点 (Highlight)**: Introduces a proactive agent system with a continuous self-improvement mechanism that learns from human-resolved cases, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2604.09579v1宣布类型：新摘要：在大型云服务平台中，每天会产生数千张客户票据，通常通过随叫随到对话进行处理。这种大量随叫随到的交互给人力支持分析师带来了巨大的工作量。最近的研究探索了利用大型语言模型作为第一线支持的反应式代理，以直接与客户互动并解决问题。然而，当问题仍未解决并升级为人力支持时，这些代理通常会脱离接触。因此，他们无法协助后续调查、跟踪解决进展或从他们未能解决的案件中吸取教训。在本文中，我们介绍了Vigil，这是一种新型的主动代理系统，旨在在整个随叫随到的生命周期中运行。与反应性特工不同，Vigil专注于在已经涉及人类支持的阶段提供援助。它集成到客户和分析师之间的对话中，在无需明确用户调用的情况下主动提供帮助。此外，Vigil还结合了一种持续的自我改进机制，可以从人类解决的案例中提取知识，以自主更新其能力。Vigil已经在字节跳动的云平台Volcano Engine上部署了十多个月，基于此部署的综合评估证明了其有效性和实用性。该作品的开源版本可在https://github.com/volcengine/veaiops上公开获取。

[阅读原文](https://arxiv.org/abs/2604.09579)

---

