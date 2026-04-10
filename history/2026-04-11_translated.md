# 💡 今日研究速览 (Daily Summary)

# 自我改进的代理人和人工智能
人工智能领域正在果断地走向闭环、自我进化系统。一个明显的趋势是开发框架，使代理能够通过交互自主改进，通常无需外部监督。通过变分合成（TTVS）的测试时自我进化、使用成对比较的迭代细化（3DrawAgent）以及体现系统中的模块化能力进化（不失去身份的学习）来说明这一点。这些方法通过专注于创建能够在连续循环中执行、自我评估和完善政策的代理来统一，有效培养元认知能力并超越静态的一次性培训。

# LLM的强化学习
LLM RL的研究正在超越基础算法，以解决对齐大型模型所固有的关键稳定性和效率挑战。主要焦点是减轻训练与推理的不匹配，采用QaRL调整量化展开和StableOPD等新颖方法稳定按政策蒸馏以防止失败模式。与此同时，奖励设计也有重大创新，从简单的基于结果的信号转向指导中间推理（SubSearch）和强制逻辑一致性（Faithful GRPO）的复杂过程奖励。这反映了对样本效率更高、稳定且理论上立足的RL训练方案的更广泛推动，正如后训练统一框架中所分析的那样。

# 隐性推理
一种强大的范式正在出现，它将复杂的推理从代币空间转移到习得的潜在表示，旨在提高效率和组合概括。Pearl和SeLaR等框架通过学习预测嵌入或选择性地激活软嵌入以进行多步推理来证明了这一点，从而有效地创建“潜在的思想链”。“这个方向与效率方面的架构创新密切相关，例如用于隐式多跳推理（循环、思考和概括）的回归深度转换器，以及通过计算阶段转换实现恒定推理缓存的新颖状态空间模型（MIPT-RSM）。目标是压缩推理轨迹并实现更复杂的内部计算。

# 多模式和领域专业化RL
RL技术正在积极定制，以解决多模式和专业领域中的具体挑战，特别是在高风险的准确性和忠实基础至关重要的领域。在视觉领域，方法是强制视觉空间一致性（忠实GRPO）和为VLM（分解、外观和推理）开发潜在推理策略。对于科学和医学应用，例如眼底阅读（Fundus-R1）或药物发现（LLM引导行动空间），框架集成了可验证的奖励和过程监督，以确保可靠、无注释的学习。这一趋势凸显了RL不仅作为通用对齐工具的作用，而且作为灌输特定领域推理能力和可信度的精确工具。

# 工具使用和长期规划
代理框架在外部工具的编排和长期任务的管理方面越来越复杂。研究的重点是元认知仲裁、将工具使用效率取决于任务成功（机智地行动），以及使用课程RL来发展使用工具的CAD代理（TOOLCAD）。对于规划，GIRL等新方法引入了潜在世界模型，并通过控制来防止想象力漂移，从而实现更可靠的长期推理。这还得到了对主动存储系统（MemReader）的研究的补充，该系统使用RL来优化选择性存储器写入，创建了一个自我改进循环，用于管理复杂任务中的长期上下文和信息。

---

## 1. TTVS：通过测试时变分合成增强自我探索强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sikai Bai, Haoxi Li, Jie Zhang, Yongjiang Liu, Song Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TTVS, a test-time self-evolution framework for LRMs that uses variational synthesis and hybrid exploration to improve via unlabeled test queries, directly matching self-improving agent criteria.

**摘要**: arXiv：2604.08468v1宣布类型：新摘要：尽管在具有可验证奖励的强化学习（RLVR）驱动下，大型推理模型（LRM）取得了重大进展，但这种范式在专业或新颖领域中从根本上受到限制，这些领域的监督成本高得令人望而却步或不可用，这对测试时间适应构成了关键挑战。虽然现有的测试时方法提供了潜在的解决方案，但它们受到从静态查询集学习的限制，存在过度适合文本模式的风险。为了解决这一差距，我们引入了测试时变分合成（TTVS），这是一种新颖的框架，它使LRM能够通过动态地扩展来自未标记测试查询的训练流来自我进化。TTVS由两个协同模块组成：（1）在线变分合成，它将静态测试查询转换为多样化、语义等效的变化的动态流，强制模型来学习底层问题逻辑而不是表面模式;（2）测试时混合探索，它平衡了准确性驱动的开发与合成变体的一致性驱动的探索。大量实验表明，TTVS在八种模型架构中具有卓越的性能。值得注意的是，TTVS仅使用未标记的测试时数据，不仅优于其他测试时自适应方法，而且还优于在大量、高质量的标记数据上训练的最先进的基于监督RL的技术。

[阅读原文](https://arxiv.org/abs/2604.08468)

---

## 2. 针对任何差异目标的合成数据

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tristan Thrush, Sung Min Park, Herman Brunborg, Luke Bailey, Marcel Roed, Neil Band, Christopher Potts, Tatsunori Hashimoto

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Dataset Policy Gradient (DPG), a novel RL primitive for optimizing synthetic data generators to precisely shape LLM behavior via SFT, directly matching RL for LLMs.

**摘要**: arXiv：2604.08423v1宣布类型：新摘要：通过合成训练数据控制语言模型有哪些限制？我们开发了强化学习（RL）基元，即数据集策略梯度（DPG），它可以精确优化合成数据生成器，以生成目标示例的数据集。当用于目标模型的监督微调（SFT）时，这些示例会导致目标模型在我们选择的可微指标上表现良好。我们的方法通过通过更高阶梯度获取准确的数据属性并使用这些分数作为政策梯度奖励来实现这一目标。我们证明这个过程非常接近合成数据生成器的真实、棘手的梯度。为了说明DPG的潜力，我们表明，在生成的示例上仅使用SFT，我们可以使目标模型的LM头部权重（1）嵌入QR码，（2）嵌入模式$\textttt {67}$，以及（3）具有较低的$\ell ' 2 $规范。我们还表明，我们可以使生成器（4）用新语言重新表达输入，以及（5）产生特定的UID，即使生成器的输入提示中没有传达这两个目标。这些发现表明，DPG是一种强大且灵活的技术，可以仅使用合成训练示例来塑造模型属性。

[阅读原文](https://arxiv.org/abs/2604.08423)

---

## 3. 通过预测嵌入的多模式潜在推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ashutosh Adhikari, Mirella Lapata

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Pearl, a JEPA-inspired framework for latent reasoning that learns predictive embeddings from expert tool-use trajectories, directly aligning with latent CoT/reasoning research.

**摘要**: arXiv：2604.08065v1宣布类型：新摘要：工具增强的多模式推理使视觉语言模型（VLM）能够通过与外部工具（例如，裁剪、深度估计）。然而，此类方法会产生大量的推理负担，需要专门的监督，并且容易出现错误的工具调用。我们提出Pearl（潜在空间中推理的预测嵌入对齐），这是一个受JEPA启发的框架，可以完全在潜在空间中从专家工具使用轨迹中学习，从而消除了在推理时显式工具调用的需要。与基于重建的潜在推理方法不同，后者自回归生成潜在令牌，并遭受训练-推理不匹配和对多步骤工具使用的有限支持，Pearl直接从多模式轨迹学习预测嵌入，同时保留标准的视觉语言生成管道：它是模型不可知的，训练简单，并且自然支持具有多个工具调用的轨迹。多个感知基准的实验表明，Pearl与标准的监督微调和基于重建的潜在推理方法相匹配或优于。此外，我们提供了经验证据，表明基于重建的方法主要学习嵌入而不是潜在空间中的图像编辑，从而激励预测嵌入学习作为一种更有原则的替代方案。

[阅读原文](https://arxiv.org/abs/2604.08065)

---

## 4. QaRL：推出对齐量化感知RL，在训练中实现快速稳定的训练--推理不匹配

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hao Gu, Hao Wang, Jiacheng Liu, Lujun Li, Qiyuan Zhu, Bei Liu, Binxing Xu, Lei Wang, Xintong Yang, Sida Lin, Sirui Han, Yike Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes QaRL, a novel RL method for LLMs that aligns quantized rollouts with training to address the training-inference mismatch and stabilize optimization.

**摘要**: arXiv：2604.07853v1宣布类型：新摘要：大型语言模型（LLM）强化学习（RL）管道通常会被推出生成所干扰，从而导致端到端训练速度变慢。最近的工作通过运行带有量化的展开来加速解码（这是RL循环中最昂贵的阶段）来缓解这一问题。然而，这些设置通过放大训练-推理差距来破坏优化的稳定性：展开以低精度操作，而学习更新则以全精度计算。为了应对这一挑战，我们提出了QaRL（推出对齐量化感知RL），它将训练侧向前与量化推出对齐，以最大限度地减少不匹配。我们进一步识别量化展开中的失败模式：长式响应往往会产生重复的、混乱的标记（错误标记）。为了缓解这些问题，我们引入了TBPO（信任带政策优化），这是一个具有负样本双重剪裁的序列级目标，旨在在信任区域内保持更新。在Qwen 3 - 30 B-A3 B MoE上，QaRL的性能比量化推出训练高出+5.5，同时提高了稳定性并保留了低位吞吐量优势。

[阅读原文](https://arxiv.org/abs/2604.07853)

---

## 5. SeLaR：大型语言模型中的选择性潜在推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Renyu Fu, Guibo Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free latent reasoning framework (SeLaR) that selectively activates soft embeddings for low-confidence steps, directly addressing core challenges in latent CoT.

**摘要**: arXiv：2604.08299v1宣布类型：新摘要：思想链（CoT）已成为大型语言模型中推理的基石，但其有效性受到离散标记采样有限的表达能力的限制。最近的潜在推理方法试图通过用软嵌入取代离散令牌来缓解这一限制（令牌嵌入的概率加权混合）或隐藏状态，但它们通常存在两个问题：（1）全局激活将扰动注入高置信步骤，损害推理稳定性;以及（2）软嵌入迅速向最高概率的代币崩溃，限制了对替代轨迹的探索。为了应对这些挑战，我们提出了SeLaR（选择性潜在推理），这是一个轻量级且免训练的框架。SeLaR引入了一种信息量门控机制，该机制仅在低置信度步骤激活软嵌入，同时在高置信度步骤保留离散解码。此外，我们还提出了一种感知信息的对比正规化，可以将软嵌入推离主导（最高概率）代币的方向，鼓励对多个潜在推理路径的持续探索。五个推理基准的实验表明，SeLaR始终优于标准CoT和最先进的免训练方法。

[阅读原文](https://arxiv.org/abs/2604.08299)

---

## 6. 链条中的理性，树木中的学习：多回合代理政策优化的自我纠正和嫁接

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yu Li, Sizhe Tang, Tian Lan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (T-STAR) for LLM agents that constructs a cognitive tree to identify critical reasoning steps and perform surgical policy optimization, directly matching the self-improving agent and RL for LLM criteria.

**摘要**: arXiv：2604.07165v1宣布类型：新摘要：大型语言模型代理的强化学习通常会受到多步推理任务中的稀疏奖励的阻碍。群相对政策优化等现有方法将采样轨迹视为独立链，为每个链中的所有步骤分配统一的信用度，并忽略可能影响推理结果的关键步骤的存在。在本文中，我们提出了T-STAR（树结构自学代理纠正），这是一个跨越看似独立的轨迹恢复潜在相关奖励结构的框架。具体来说，我们通过识别和合并功能相似的步骤/节点将轨迹整合到统一的认知树中。它实现了内省估值机制，通过树反向传播个体级奖励，以获得阶梯级方差降低相对优势的新概念。使用认知树，我们还开发了上下文思维移植，通过在关键分歧点/步骤对比成功和失败的分支来综合纠正推理。然后，我们提出的手术政策优化利用集中在这些关键点/步骤的丰富政策梯度信息，通过Bradley-Terry类型的手术损失。针对具体化、交互式、推理和规划基准的广泛实验表明，T-STAR在强基线上实现了一致的改进，在需要扩展推理链的任务上，其收益最为明显。

[阅读原文](https://arxiv.org/abs/2604.07165)

---

## 7. 揭开OPD的神秘面纱：大型语言模型的长度膨胀和稳定策略

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Feng Luo, Yu-Neng Chuang, Guanchu Wang, Zicheng Xu, Xiaotian Han, Tianyi Zhang, Vladimir Braverman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes StableOPD, a stabilized on-policy distillation framework for LLMs that directly addresses a failure mode in RL-based training loops for math reasoning.

**摘要**: arXiv：2604.08527v1宣布类型：新摘要：按政策蒸馏（OPD）在自己的诱导分布下训练学生模型，同时利用更强大教师的监督。我们确定了OPD的一种失败模式：随着培训的进行，按政策推出可能会经历突然的长度膨胀，导致截断的轨迹主导训练数据。这种截断崩溃与突然的重复饱和相一致，并引起有偏的梯度信号，导致严重的训练不稳定性和验证性能的急剧下降。我们把这个问题归因于学生引起的数据收集和蒸馏目标之间的相互作用，这隐含地有利于长期和重复的推出。为了解决这个问题，我们提出了StableOPD，一个稳定的OPD框架，它结合了基于参考的发散约束和推出混合蒸馏。这些共同减轻了重复引起的长度膨胀，并进一步稳定OPD训练。在多个数学推理数据集中，我们的方法可以防止截断崩溃、稳定训练动态，并将性能平均提高7.2%。

[阅读原文](https://arxiv.org/abs/2604.08527)

---

## 8. 忠实的GRPO：通过约束策略优化改进多模式语言模型中的视觉空间推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sai Srinivas Kancheti, Aditya Kanade, Rohit Sinha, Vineeth N Balasubramanian, Tanuja Ganu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Faithful GRPO, a constrained RL method for multimodal LLMs that improves reasoning quality and answer accuracy by enforcing logical consistency and visual grounding.

**摘要**: arXiv：2604.08476v1宣布类型：新摘要：使用可验证奖励强化学习（WLVR）训练的多模式推理模型（MRM）在视觉推理基准上表现出更高的准确性。然而，我们观察到准确性的提高往往是以牺牲推理质量为代价的：生成的思想链（CoT）痕迹经常与最终答案不一致，并且视觉证据基础较差。我们在七个具有挑战性的现实世界空间推理基准上系统地研究了这一现象，并发现它会影响当代MRM，例如ViGoRL-Spatial、TreeVGR以及我们自己的用标准组相对政策优化（GRPO）训练的模型。我们沿着两个互补的轴来描述CoT推理质量：“逻辑一致性”（CoT是否需要最终答案？）和“视觉基础”（每个推理步骤是否准确地描述了图像中的对象、属性和空间关系？）。为了解决这个问题，我们提出了Faithful GRPO（FGRPO），这是GRPO的一种变体，通过拉格朗日双重上升来强制一致性和接地作为约束。FGRPO将批量级一致性和基础约束融入到组内的优势计算中，在优化期间自适应地调整约束的相对重要性。我们在七个空间数据集的Qwen 2.5-VL-7 B和3B主干上评估了FGRPO。我们的结果表明，FGRPO大幅提高了推理质量，将不一致率从24.5%降低到1.7%，并将视觉基础分数提高了+13%。它还比简单的GRPO提高了最终答案的准确性，证明忠实的推理可以提供更好的答案。

[阅读原文](https://arxiv.org/abs/2604.08476)

---

## 9. 循环、思考和概括：回归深度变形机中的隐式推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Harsh Kohli, Srinivasan Parthasarathy, Huan Sun, Yuekun Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes and analyzes recurrent-depth transformers for implicit multi-hop reasoning, directly addressing latent reasoning and compositional generalization.

**摘要**: arXiv：2604.07822v1宣布类型：新摘要：我们研究隐性推理，即在一次向前传递内结合知识或规则的能力。虽然基于转换器的大型语言模型存储了大量的事实知识和规则，但它们通常无法为隐式多跳推理组合这些知识，这表明它们的参数知识缺乏组合概括。为了解决这一限制，我们研究了回归深度变换器，它可以在相同的Transformer层上进行迭代计算。我们研究了隐式推理场景下的两个合成概括挑战：系统概括，即结合训练期间从未用于合成的知识，和深度外推，即从有限的推理深度（例如训练至5跳）推广到更深的合成（例如10跳）。通过从头开始训练的模型的对照研究，我们表明，虽然vanilla Transformer难以应对这两个概括挑战，但回归深度Transformer可以有效地进行这种概括。对于系统概括，我们发现这种能力是通过三阶段的摸索过程出现的，从记忆过渡到内分布概括，最后过渡到由机械分析支持的系统概括。对于深度外推，我们表明可以通过扩展推理时重现来解锁超出训练深度的概括，更多的迭代可以实现更深入的推理。我们进一步研究训练策略如何影响外推，为训练回归深度转换器提供指导，并找出一个关键限制，即过度思考，过度重复会降低预测并将概括限制到非常深的构图。

[阅读原文](https://arxiv.org/abs/2604.07822)

---

## 10. MIPT-RSM：通过阶段转换使用$O（1）$推理缓存扩展语言模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Yasong Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel sequence architecture (MIPT-SSM) that learns to route computation between wave and particle phases, achieving O(1) inference cache and latent state compression, aligning with latent reasoning efficiency goals.

**摘要**: arXiv：2604.07716v1宣布类型：新摘要：我们介绍了MIPT-RSM，这是一种基于测量诱导相转变（MTIP）物理学的神经序列架构。中心思想是学习测量速率$p_{t}\in（0，1）$，它在两个状态之间路由计算：波相$（p_{t}\rightarrow 0）$，其中信息以分布式复相干扰的形式传播;和粒子相$（p_{t}\rightarrow 1）$，其中状态塌陷到当前令牌上，从而实现精确的本地存储。这两个机制在单个线性运算符中是不相容的，这是序列建模中为数不多的“禁忌定理”之一，$p_{t}$是我们的解决方法。预测该模型将在关键序列长度$N &{*}\approx 1024 $处表现出相转变，其中信息密度比$N/D$与1相交，与我们的内存缩放观察结果一致。在AG News（四级分类）上，MTIP的准确率为0.905，而Transformer的准确率为0.736（+16.6%），在3个种子中稳定。$N=8192$MTIP需要810 MB，而Transformer的34，651 MB内存减少了42.8倍。在精确召回（“大海捞针”）上，我们的因果稀疏KV缓存实现了0.968的准确性。值得注意的是，在无限缓存容量下，$p_{t}$门会自动学习仅存储单个关键令牌（平均使用1.0美元/512美元插槽），过滤掉所有噪音并实现99.8%的稀疏率。在语言建模（Wikitext-103，31 M个参数）上，$K=64$缓存的MIPT-LM达到PPL 92.1，而Transformer的90.5（差距：1.8%），而推断KV缓存从$O（N）$缩小到$O（64）$。

[阅读原文](https://arxiv.org/abs/2604.07716)

---

## 11. 大型语言模型培训后：政策外和政策内学习的统一看法

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shiwan Zhao, Zhihu Wang, Xuyang Zhao, Jiaming Zhou, Caiyue Xu, Chenfei Liu, Liting Zhang, Yuhang Jia, Yanzhe Zhang, Hualong Yu, Zichen Xu, Qicheng Li, Yong Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a unified theoretical framework for LLM post-training, explicitly analyzing RL and on-policy/off-policy learning regimes central to RL for LLMs.

**摘要**: arXiv：2604.07941v1宣布类型：新摘要：后训练已成为将预训练的大型语言模型（LLM）转变为一致且可部署的系统的核心。最近的进展涵盖监督式微调（SFT）、偏好优化、强化学习（RL）、流程监督、验证器引导方法、蒸馏和多阶段管道。然而，这些方法通常以碎片化的方式讨论，由标签或客观家庭而不是由它们解决的行为瓶颈来组织。   这项调查认为，LLM后培训最好被理解为对模型行为的结构性干预。我们首先按照轨迹出处组织该领域，轨迹出处定义了两种主要学习制度：外部提供轨迹的政策外学习，以及学习者生成的推出的政策内学习。然后，我们通过两个重复出现的角色来解释方法--有效的支持扩展，使有用的行为更容易实现，政策重塑，改善已经可实现的区域内的行为--以及补充的系统级角色，行为巩固，它保存、转移和摊销跨阶段和模型转换的行为。   这种观点产生了对主要范式的统一解读。SFT可以用于扩大支持或重塑政策，而基于优惠的方法通常是政策外重塑。按策略RL通常会改善学习者生成状态的行为，尽管在更强有力的指导下，它也可以使难以到达的推理路径变得可用。蒸馏通常最好地理解为巩固而不是仅仅压缩，混合管道作为协调的多阶段组合物出现。   总体而言，该框架有助于诊断培训后瓶颈和阶段构成的原因，这表明LLM培训后的进展越来越依赖于协调的系统设计，而不是任何单一的主导目标。

[阅读原文](https://arxiv.org/abs/2604.07941)

---

## 12. 明智行事：在统计多模式模型中培养元认知工具的使用

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shilin Yan, Jintao Tong, Hongwei Xue, Xiaojun Tang, Yangyang Wang, Kunyu Shi, Guannan Zhang, Ruixuan Li, Yixiong Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HDPO, a decoupled RL framework for agentic multimodal models that conditions tool-use efficiency on task accuracy, directly addressing meta-cognitive tool arbitration.

**摘要**: arXiv：2604.08545v1宣布类型：新摘要：代理多模式模型的出现使系统能够主动与外部环境交互。然而，当前的代理人患有严重的元认知缺陷：他们很难在利用内部知识和查询外部效用之间进行仲裁。因此，它们经常成为盲目工具调用的牺牲品，即使查询可以从原始视觉上下文中解析，它们也会诉诸自反工具执行。这种病态行为会导致严重的延迟瓶颈，并注入外来噪音，从而破坏合理的推理。现有的强化学习协议试图通过惩罚工具使用的分级奖励来缓解这种情况。然而，这种结合的公式造成了一个不可调和的优化困境：激进的惩罚会抑制必要的工具使用，而温和的惩罚则完全被优势正常化期间准确性奖励的方差所包含，使其对工具过度使用无能为力。为了超越这一瓶颈，我们提出了HDPO，一个框架，从一个竞争的标量目标，严格有条件的工具效率。通过避免奖励标量化，HDPO保持了两个正交优化通道：一个是最大化任务正确性的准确性通道，另一个是通过条件优势估计在准确的轨迹内强制执行经济的效率通道。这种解耦的架构自然会引起认知障碍，迫使代理在完善其自力更生之前首先掌握任务解决方案。广泛的评估表明，我们得到的模型，Metis，减少工具调用的数量级，同时提高推理的准确性。

[阅读原文](https://arxiv.org/abs/2604.08545)

---

## 13. TOOLCAD：探索在文本到CAD生成中使用大型语言模型的工具，并通过强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yifei Gong, Xing Wu, Wenda Liu, Kang Tu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an online curriculum reinforcement learning strategy to evolve LLM-based CAD tool-using agents, directly matching RL for LLMs and self-improving agents.

**摘要**: arXiv：2604.07960v1宣布类型：新摘要：计算机辅助设计（CAD）是一项专家级任务，依赖于长期推理和连贯的建模动作。大型语言模型（LLM）在使语言代理能够处理现实世界的任务方面取得了显着的进步。值得注意的是，目前还没有研究使用工具的LLM如何与CAD引擎进行最佳交互，这阻碍了基于LLM的代理文本到CAD建模系统的出现。我们提出了Tools CAD，这是一种新型的代理CAD框架，将LLM部署为工具使用代理，用于文本到CAD生成。此外，我们还引入了一个交互式CAD建模健身房，以推出与CAD引擎的推理和工具增强交互轨迹，结合了混合反馈和人类监督。同时，提出了端到端的后培训策略，使LLM代理能够引出细化的CAD建模思想链（CAD-CoT），并通过在线课程强化学习发展为熟练的CAD工具使用代理。我们的研究结果表明，Tools CAD填补了为使用CAD工具的代理采用和培训开源LLM的空白，使它们能够执行对专有模型的复制，为更容易访问和更强大的自主文本到CAD建模系统铺平了道路。

[阅读原文](https://arxiv.org/abs/2604.07960)

---

## 14. GIRL：通过信息理论幻觉控制的生成想象强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Prakul Sunil Hiremath

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent world-model RL framework (GIRL) with grounding and trust-region components to control imagination drift, directly relevant to RL for long-horizon planning.

**摘要**: arXiv：2604.07426v1宣布类型：新摘要：基于模型的强化学习（MBRL）通过优化想象的展开内的策略来提高样本效率，但当模型错误复合并且想象的轨迹偏离训练集管时，长期规划就会降级。我们引入GIRL（生成想象力强化学习），这是一个潜在的世界模型框架，通过两个关键组件来解决这种失败模式。首先，从冻结基础模型（DINOv 2）推导出的跨模式接地信号将潜在的转变锚定在语义一致的嵌入空间之前，从而惩罚不一致或难以置信的预测。其次，不确定性自适应信任域瓶颈将KL正规化器解释为约束优化问题的拉格朗日乘数，限制了由预期信息收益和相对性能损失信号校准的学习区域内的想象力漂移。   我们使用性能差异引理和积分概率表重新推导出价值差距界限，从而产生一个界限，当折扣因子接近1时，该界限仍然具有信息性，并将目标与现实环境的遗憾联系起来。三个基准套件（包括DeepMind Control、Adroit Hand Manipulation和具有视觉干扰物的元世界）的实验表明，GIRL相对于DreamerV 3将任务中的潜在展开漂移减少了38%至61%，改善了渐进返回，并且在长视野任务中需要更少的环境交互。在标准评估指标下，GIRL在稀疏奖励和高接触设置方面的表现也优于TD-MPC 2。相对于完整模型，提炼先验变体减少了推理负担并提高了计算效率。

[阅读原文](https://arxiv.org/abs/2604.07426)

---

## 15. Fundus-R1：利用公共数据的知识感知推理训练基金阅读MLLM

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuchuan Deng, Qijie Wei, Kaiheng Qian, Jiazhen Liu, Zijie Xin, Bangxiang Lan, Jingyu Liu, Jianfeng Dong, Xirong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning with verifiable rewards (RLVR) method enhanced with a process reward for self-consistency, applied to training a fundus-reading MLLM.

**摘要**: arXiv：2604.08322v1宣布类型：新摘要：CFP、光学断层扫描和UWF等底部成像对于早期检测视网膜异常和疾病至关重要。由于其知识密集型性质，底部图像理解提出了一项具有挑战性的视觉语言任务。解决该任务的一种新兴方法是通过监督微调（SFT）或通过具有可验证奖励的强化学习（WLVR）对大量内部样本进行后训练通用多模式大型语言模型（MLLM），并与高质量的临床报告配对。然而，这些有价值的样本无法公开获取，这不仅阻碍了重复性，而且实际上将研究限制在少数参与者身上。为了克服这一障碍，我们进行了一次新颖的尝试，专门使用公共数据集来训练推理增强型基金阅读MLLM，我们将其称为Fundus-R1，其中超过94%的数据仅用图像级标签进行注释。我们的技术贡献是双重的。首先，我们提出了一种基于RAG的方法来组成特定于图像的、知识感知的推理痕迹。此类自动生成的痕迹将通用MLLM识别的视觉发现与眼科知识方面的图像标签联系起来。其次，我们通过流程奖励来增强WLVR，该奖励鼓励每次部署中生成的推理轨迹的自一致性。对三个基金阅读基准进行了广泛实验，即FunBench、Omni-Fundus和GMAI-Fundus表明，Fundus-R1的表现明显优于多个基线，包括其通用对应物（Qwen 2.5-BL）和无需使用生成的痕迹进行后训练的更强版本。这项工作为利用公开数据培训强大的基金阅读MLLM铺平了道路。

[阅读原文](https://arxiv.org/abs/2604.08322)

---

## 16. 自我修改代理实际需要多少LLM？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sungwoo Jung, Seonil Son

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a declared reflective runtime protocol to externalize agent state and study the marginal role of LLM intervention in self-revising agents, directly aligning with self-improving agent frameworks.

**摘要**: arXiv：2604.07236v2宣布类型：新摘要：最近基于LLM的代理通常将世界建模、规划和反射置于单一语言模型循环中。这可以产生有能力的行为，但这使得一个基本的科学问题难以回答：代理人的能力的哪一部分实际上来自LLM，哪一部分来自其周围的显式结构？   我们研究这个问题，不是通过要求一个普遍的答案，而是通过使它在经验上易于处理。我们引入了一个声明的反射运行时协议，具体化代理状态，信心信号，守卫行动，并假设转换到可检查的运行时结构。我们在声明式运行时中实例化该协议，并在嘈杂的协作战舰[4]上使用四个渐进结构的代理在54场比赛（18个板$\times $3个种子）中对其进行评估。   由此产生的分解隔离了四个组成部分：后验信念跟踪，明确的世界模型规划，象征性的情节反射，稀疏LLM为基础的修订。在此分解中，显式世界模型规划比贪婪的后验基线（+24.1pp获胜率，+0.017 F1）有了显着的改善。符号反射作为一种真正的运行时机制运行--具有预测跟踪、置信度门控和受保护的修订操作--尽管其当前的修订收件箱总体上尚未达到净正值。在约4.3%的回合数处添加有条件的LLM修订只会产生较小且非单调的变化：F1平均水平略有上升（+0.005），而胜率下降（31 $\rightarrow 29（满分54））。   这些结果表明了方法论的贡献，而不是排行榜的主张：外部化反射将潜在的代理行为转变为可检查的运行时结构，从而允许直接研究LLM干预的边缘作用。

[阅读原文](https://arxiv.org/abs/2604.07236)

---

## 17. 3DrawAgent：利用早期对比经验教授法学硕士绘制3D

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hongcan Xiao, Xinyue Xiao, Yilin Wang, Yue Zhang, Yonggang Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a training-free, self-improving agent framework using pairwise comparisons and a GRPO variant to iteratively refine 3D drawing capabilities.

**摘要**: arXiv：2604.08042v1宣布类型：新摘要：在3D空间中绘制草图可以对形状、结构和空间关系进行富有表达性的推理，但通过自然语言生成3D草图仍然是一个重大挑战。在这项工作中，我们引入了3DrawAgent，这是一个用于3D草图生成的免训练、语言驱动的框架，它利用大型语言模型（LLM）在几何反馈下顺序绘制3D贝塞尔曲线。与之前的2D草图代理不同，我们的方法引入了一种相对体验优化策略，该策略适应了最近提出的团体奖励政策优化（GRPO）范式。我们没有依赖于明确的基本事实监督，而是在生成的草图之间进行成对比较，每对都包括基于CLIP的感知奖励和基于LLM的细粒度定性评估的相对更好和更差的结果。然后使用这些经验迭代地完善3D绘图的先验知识，从而能够通过黑匣子加强模型的3D意识。这种设计使我们的模型能够自我提高其空间理解和绘制质量，而无需更新参数。实验表明，3DrawAgent可以从不同的文本提示中生成复杂、连贯的3D Bezier草图，表现出新兴的几何推理，并推广到新颖的形状，为推进免训练3D草图智能领域建立了新的范式。

[阅读原文](https://arxiv.org/abs/2604.08042)

---

## 18. AnomalyAgent：基于工具增强强化学习的工业异常综合

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiaming Su, Tengchao Yang, Ruikang Zhang, Zhengan Yan, Haoyu Sun, Linfeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an agentic anomaly synthesis framework with a two-stage training pipeline (SFT then RL) and a three-part reward mechanism for closed-loop optimization, directly matching RL for LLMs/Agents.

**摘要**: arXiv：2604.07900v1宣布类型：新摘要：工业异常生成是缓解异常检测任务中数据稀缺问题的重要方法。现有的异常合成方法大多依赖于一步生成机制，缺乏复杂的推理和迭代优化能力，难以生成具有高语义真实感的异常样本。我们提出了AnomalyAgent，一个异常合成代理与自我反思，知识检索和迭代细化能力，旨在产生现实和多样化的异常。具体来说，AnomalyAgent配备了五个工具：提示生成（PG），图像生成（IG），质量评估（QE），知识检索（KR）和掩码生成（MG），实现闭环优化。为了改善决策和自我反思，我们从真实的异常图像中构建结构化轨迹，并设计了一个两阶段的训练框架：监督微调，然后是强化学习。该过程由三部分奖励机制驱动：（1）任务奖励，以监督生成的异常的质量和位置合理性;（2）反射奖励，以训练模型提高异常合成提示的能力;（3）行为奖励，以确保遵守轨迹。在MMVTec-AD数据集上，AnomalyAgent在异常生成方面实现了2.10/0.33的IS/IC-L，使用ResNet 34实现了57.0%的分类准确率，使用简单的UNet在图像/像素级别实现了99.3%/74.2%的AP，超过了所有零镜头SOTA方法。代码和数据将公开。

[阅读原文](https://arxiv.org/abs/2604.07900)

---

## 19. FVD：通过Fleming-Viot重新分配扩散模型的推理时间对齐

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shivanshu Shekhar, Sagnik Mukherjee, Jia Yi Zhang, Tong Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FVD, an inference-time alignment method for diffusion models using a novel Fleming-Viot resampling mechanism, directly relevant to RL for generative models via reward-based trajectory selection.

**摘要**: arXiv：2604.06779v1宣布类型：新摘要：我们引入弗莱明-维奥特扩散（FVD），这是一种推理时间对齐方法，可以解决基于顺序蒙特卡罗（SMC）的扩散采样器中常见的多样性崩溃。现有的基于SMC的扩散采样器通常依赖于多项重采样或密切相关的重采样方案，这仍然会减少多样性并在强大的选择压力下导致谱系崩溃。受Fleming-Viot种群动力学的启发，FVD用专为扩散对齐而设计的专门生灭机制取代了多项再分配。为了处理奖励仅大致可用且天真重生会崩溃确定性轨迹的情况，FVD将独立的基于奖励的生存决策与随机重生噪音集成在一起。这产生了灵活的人口动态，可以保留更广泛的轨迹支持，同时有效地探索回报倾斜分布，而无需价值函数逼近或昂贵的推出。FVD是完全可并行的，并通过推理计算有效扩展。从经验上看，它在不同设置中取得了巨大的进步：在DrawBench上，它在Image Reward中的性能比以前的方法高出7%，而在类条件任务中，它在强基线上将DID提高了大约14-20%，并且比基于价值的方法快了66倍。

[阅读原文](https://arxiv.org/abs/2604.06779)

---

## 20. 子搜索：复杂检索中无监督引导推理的中间奖励

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Roxana Petcu, Evangelos Kanoulas, Maarten de Rijke

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SubSearch, a framework using intrinsic intermediate rewards to directly optimize LLM reasoning for complex retrieval, aligning with RL for LLMs by focusing on process reward design.

**摘要**: arXiv：2604.07415v1宣布类型：新摘要：大型语言模型（LLM）本质上是概率性的，并且在利用外部信息进行增强时执行得更可靠。由于复杂的查询通常需要对检索到的信息进行多步推理，并且没有明确或预定的推理路径，因此它们仍然具有挑战性。最近的方法使用强化学习来训练模型，以改善模型处理复杂信息的方式。我们引入了SubSearch，这是一个专门的框架，从仅结果的监督转变为激励规划高质量推理的中间奖励信号。与之前关于流程奖励建模的工作（专注于训练具有人类注释者或大型LLM法官注释轨迹的单独奖励模型）不同，SubSearch使用内在流程奖励（我们将其定义为内部衍生奖励）直接优化生成器，消除了对外部监督的需要，并转向自主信息密集型推理。七个基准测试的实验表明，与仅使用结果奖励相比，用内在奖励奖励中间推理步骤可以在QA和多跳QA数据集中产生更稳健的推理痕迹。SubSearch可以帮助构建推理痕迹，使代理能够更好地集成搜索引擎以进行复杂的查询回答，同时提供监督流程建模的数据高效替代方案。

[阅读原文](https://arxiv.org/abs/2604.07415)

---

## 21. 在不失去身份的情况下学习：有条件的代理人的能力进化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving embodied agent framework where modular capabilities evolve through a closed-loop process of execution and refinement.

**摘要**: arXiv：2604.07799v1公告类型：新摘要：智能体有望在动态物理环境中持续运行，随着时间的推移不断获得新的功能。现有的提高代理性能的方法通常依赖于修改代理本身-通过及时的工程，政策更新或结构重新设计-导致不稳定和长期存在的系统中的身份丢失。在这项工作中，我们提出了一种以能力为中心的具体代理进化范式。我们认为，机器人应该将持久的代理人作为其认知身份，同时通过其能力的进化实现持续改进。具体来说，我们引入了可调度能力模块（ECT）的概念，它表示模块化的、版本化的具体功能单元，可以随着时间的推移学习、细化和组成。我们提出了一个统一的框架，其中能力进化与代理身份脱钩。能力通过涉及任务执行、经验收集、模型细化和模块更新的闭环过程发展，而所有执行都由执行安全和策略约束的运行时层管理。我们通过模拟的具体任务证明，能力进化在20次迭代中将任务成功率从32.4%提高到91.3%，优于代理修改基线和既定技能学习方法（SPiRL、SkiMo），同时保持零政策漂移和零安全违规。我们的结果表明，将代理身份与能力进化分开为长期体现智能提供了可扩展和安全的基础。

[阅读原文](https://arxiv.org/abs/2604.07799)

---

## 22. 更少的接近更多：通过高风险任务的混合后培训协调绩效和信心忠诚度

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haokai Ma, Lee Yan Zhen, Gang Yang, Yunshan Ma, Ee-Chien Chang, Tat-Seng Chua

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hybrid post-training framework (HyTuning) that adaptively reweights unsupervised RL from Internal Feedback (RLIF) and reasoning distillation to improve accuracy and confidence faithfulness.

**摘要**: arXiv：2604.08454v1宣布类型：新摘要：大型语言模型越来越多地被部署在高风险任务中，自信但不正确的推断可能会对现实世界造成严重伤害，从而使以前被忽视的信心忠实性问题重新成为最重要的问题。一个有希望的解决方案是联合优化来自内部反馈的无监督强化学习（RLily）与推理跟踪引导的推理蒸馏（RD），这可能面临三个持续的挑战：高质量训练库的稀缺、事实上毫无根据的过度自信和放大错误更新的不加区别的融合。受人类从不确定性到确定性的信心积累的启发，我们提出了渐进推理收益（PRG）来衡量推理步骤是否逐渐增强对最终答案的支持。此外，我们还引入了HyTuning，这是一种混合训练后框架，它通过PRG风格的指标自适应地重新加权RD和RIIF，使用稀缺的监督推理轨迹作为稳定锚点，同时利用大量的未标记查询来实现可扩展性。对几个特定领域和通用基准的实验表明，HyTuning提高了准确性，同时在有限监督下实现了信心忠诚度，支持实用的“更少大约更多”效果。

[阅读原文](https://arxiv.org/abs/2604.08454)

---

## 23. 利用LLM引导的动作空间进行强化学习以实现可合成潜在客户优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tao Li, Kaiyuan Hou, Tuan Vinh, Monika Raj, Zhichun Guo, Carl Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an RL framework (GRPO) for LLM-guided lead optimization, directly matching RL for LLMs with a novel reward design and training pipeline.

**摘要**: arXiv：2604.07669v1宣布类型：新摘要：药物发现中的主导优化需要改善治疗性能，同时确保拟议的分子修饰符合可行的合成路线。现有的方法要么优先考虑属性分数而不强制执行可合成性，要么依赖于大型反应网络上的昂贵列举，而直接应用大型语言模型（LLM）经常会产生化学无效的结构。我们引入了MolReAct，这是一个框架，它将铅优化制定为由经过验证的反应模板定义的合成约束动作空间上的马尔科夫决策过程。工具增强的LLM代理充当动态反应环境，它调用专门的化学分析工具来识别反应位点并根据匹配的模板提出化学基础转换。通过团体相对政策优化（GRPO）训练的政策模型在这些受约束的动作中进行选择，以在多步反应轨迹中最大化长期Oracle奖励。基于SMILES的缓存机制进一步将端到端优化时间减少了约43%。在治疗数据共享资源的13项属性优化任务和一项基于结构的对接任务中，MolReAct的前10名平均得分为0.563，相对改进比最强的可合成基线高出10.4%，并在14项任务中的10项中实现了最佳样本效率。消融证实，工具增强的反应提案和专家级政策优化都有助于补充收益。通过以经过验证的反应模板为基础的每一步，MolReAct产生了性能改进且每个分子都伴随着明确的合成途径的分子。

[阅读原文](https://arxiv.org/abs/2604.07669)

---

## 24. OpenVLThinkerV2：用于多领域视觉任务的通用多模式推理模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wenbo Hu, Xin Chen, Yan Gao-Tian, Yihe Deng, Nanyun Peng, Kai-Wei Chang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Gaussian GRPO, a novel RL training objective for multimodal models, directly addressing reward scaling and gradient equity for RL-based LLM improvement.

**摘要**: arXiv：2604.08539v1宣布类型：新摘要：组相对策略优化（GRPO）已成为事实上的强化学习（RL）目标，推动了多模式大型语言模型的最新进展。然而，将这一成功扩展到开源多模式通才模型仍然受到两个主要挑战的严重限制：不同视觉任务中奖励布局的极端差异，以及平衡细粒度感知与多步推理能力的固有困难。为了解决这些问题，我们引入了高斯GRPO（G $& 2$LPO），这是一种新型RL训练目标，用非线性分布匹配取代标准线性缩放。通过在数学上迫使任何给定任务的优势分布严格收敛到标准正态分布，$\mathCal{N}（0，1）$，G $' 2$LPO理论上确保了任务间梯度公平性，减轻了对重尾异常值的脆弱性，并为正和负奖励提供对称更新。利用G $' 2$LPO提供的增强的训练稳定性，我们引入了两种任务级塑造机制，以无缝平衡感知和推理。首先，响应长度整形动态地为复杂查询引入扩展推理链，同时强制执行直接输出以增强视觉基础。其次，信息量整形严格限制了模型的探索区域，有效地防止了信息量崩溃和信息量爆炸。集成这些方法论，我们提出了OpenVLThinkerV 2，这是一个高度稳健的通用多模式模型。对18个不同基准的广泛评估表明，其优于强大的开源和领先的专有前沿模型。

[阅读原文](https://arxiv.org/abs/2604.08539)

---

## 25. MedVR：通过抽象强化学习进行无注释医学视觉推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zheng Jiang, Heng Guo, Chengyu Fang, Changchen Xiao, Xinyang Hu, Lifeng Sun, Minfeng Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel reinforcement learning framework (MedVR) for annotation-free visual reasoning in medical VLMs, aligning with RL for LLMs via reward design and self-improvement loops.

**摘要**: arXiv：2604.08203v1宣布类型：新摘要：医学视觉语言模型（VLM）对于复杂的临床任务具有巨大的前景，但它们的推理能力通常受到纯文本范式的限制，而纯文本范式无法将推理建立在视觉证据中。这种限制不仅会降低需要细粒度视觉分析的任务的性能，而且还会在安全关键型应用程序中引入幻视的风险。因此，我们引入MedVR，一种新的强化学习框架，可以为医学VLM提供无注释的视觉推理。它的核心创新在于两个协同机制：熵引导的视觉重接地（EVR）使用模型的不确定性来指导探索，而基于信任度的信用分配（CCA）从推出协议中提取伪监督。在中间步骤没有任何人工注释的情况下，MedVR在各种公共医疗VQA基准上实现了最先进的性能，显著优于现有模型。通过学习直接使用视觉证据进行推理，MedVR促进了加速医疗AI临床部署所必需的鲁棒性和透明度。

[阅读原文](https://arxiv.org/abs/2604.08203)

---

## 26. ReRec：通过强化微调的基于推理增强的LLM的推荐助手

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiani Huang, Shijie Wang, Liangbo Ning, Wenqi Fan, Qing Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement fine-tuning (RFT) framework with novel reward shaping and reasoning-aware advantage estimation to improve LLM reasoning for recommendation.

**摘要**: arXiv：2604.07851v1公告类型：新摘要：随着LLM的兴起，人们越来越需要智能推荐助手来处理复杂的查询，并提供个性化的、推理驱动的推荐。基于LLM的推理机显示出潜力，但在多步推理中面临挑战，强调了对推理增强系统的需求。为了解决这一差距，我们提出了ReRec，这是一种新型的强化微调（RFT）框架，旨在改进复杂推荐任务中的LLM推理。我们的框架引入了三个关键组件：（1）双图增强奖励整形，将NDCG@K等推荐指标与查询对齐和偏好对齐得分集成，为LLM优化提供细粒度的奖励信号;（2）推理感知优势估计，将LLM输出分解为推理段并惩罚不正确的步骤以增强推荐的推理;（3）在线课程设置，动态评估查询难度并组织培训课程，确保RFT期间的稳定学习。实验表明，ReRec的表现优于最先进的基线，并保留了遵循描述和常识等核心能力。我们的代码可在https://github.com/jiani-huang/ReRec上获取。

[阅读原文](https://arxiv.org/abs/2604.07851)

---

## 27. Policy Long：走向政策背景扩展

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junlong Jia, Ziyang Chen, Xing Wu, Chaochen Gao, TingHao Yu, Feng Zhang, Songlin Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PolicyLong, an on-policy data construction method for context extension that creates a self-curriculum by iteratively screening data with the current model.

**摘要**: arXiv：2604.07809v1宣布类型：新摘要：扩展LLM上下文窗口受到稀缺高质量长上下文数据的阻碍。最近的方法通过信息理论验证来合成具有真正长期依赖性的数据，选择降低基本模型预测性的上下文。然而，他们采用固定模型的单次离线构建造成了根本性的政策外差距：静态筛选环境与模型不断发展的能力不一致，导致训练分布漂移。我们提出Policy Long，将数据构建转向动态的政策范式。通过使用当前模型迭代重新执行数据筛选（信息量计算、检索和验证），Policy Long确保训练分布跟踪不断发展的能力，从而产生紧急的自我课程。至关重要的是，积极和消极的背景都源自当前模型的熵景观，共同进化模型学会利用和抵制的东西。RULER、HEMET和LongBench-v2（Qwen 2.5 -3B）上的实验表明，Policy Long的表现始终优于EntropyLong和NExtLong，收益在更长的环境下增长（例如，RULER上128 K时+2.54），证实了政策数据演变的价值。

[阅读原文](https://arxiv.org/abs/2604.07809)

---

## 28. 分解、观察和推理：VLM的强化潜在推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mengdan Zhu, Senhao Cheng, Liang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforced latent reasoning framework for VLMs, directly aligning with latent CoT/reasoning via a novel latent space policy.

**摘要**: arXiv：2604.07518v1宣布类型：新摘要：由于文本CoT中的视觉信息丢失，视觉语言模型经常难以应对复杂的视觉推理。现有的方法要么增加工具调用的成本，要么依赖于本地化的基于补丁的嵌入，而这些嵌入不足以在多步推理中提取语义。我们提出了\{“分解、外观和原因”（DLR）}，这是一个强化的潜在推理框架，它动态地将查询分解为文本前提，提取条件条件连续视觉潜伏，并通过基础原理推导答案。我们引入了三阶段训练管道，并提出了一种新型的球形高斯潜伏策略，以实现对潜在空间的有效探索。针对以视觉为中心的基准进行的大量实验表明，DLR始终优于强基线，包括纯文本、交织多模式CoT和潜在推理方法，同时提供出色的逐步解释性。

[阅读原文](https://arxiv.org/abs/2604.07518)

---

## 29. MemReader：从被动到主动提取长期代理记忆

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jingyi Kang, Chunyu Li, Ding Chen, Bo Tang, Feiyu Xiong, Zhiyu Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an active memory extractor agent (MemReader-4B) optimized with Group Relative Policy Optimization (GRPO) to make selective memory writing decisions, enabling a self-improving reasoning loop for long-term agent memory.

**摘要**: arXiv：2604.07877v1宣布类型：新摘要：长期记忆是个性化和自主代理的基础，但填充长期记忆仍然是一个瓶颈。现有系统将内存提取视为从上下文到结构化条目的一次性被动转录，它会与嘈杂的对话、缺失的引用和交叉转折依赖性作斗争，从而导致内存污染、低价值写入和不一致。本文中，我们介绍了用于代理系统中主动长期内存提取的MemReader系列：MemReader-0.6B，这是一个紧凑且经济高效的被动提取器，可提取准确且方案一致的结构化输出; MemReader-4 B，这是一个主动提取器，通过组相对策略优化（GRPO）进行优化，以做出内存写入决策。在ReAct风格的范式下，MemReader-4 B在行动之前明确评估信息价值、引用歧义和完整性，并且可以选择性地写入记忆、推迟不完整的输入、检索历史背景或丢弃不相关的喋喋不休。LOCOMO、LongMemEval和HaluMem上的实验表明，MemReader始终优于现有的基于提取的基线。特别是，MemReader-4 B在涉及知识更新、时态推理和幻觉减少的任务上实现了最先进的性能。这些结果表明，有效的主体记忆不仅需要提取更多信息，还需要执行推理驱动和选择性的记忆提取，以建立低噪音和动态演变的长期记忆。此外，MemReader已集成到MemOS中并部署在现实世界的应用程序中。为了支持未来的研究和采用，我们发布了模型并提供公共API访问。

[阅读原文](https://arxiv.org/abs/2604.07877)

---

## 30. HY-BASED-0.5：面向真实世界代理的BASED基础模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tencent Robotics X, HY Vision Team, :, Xumin Yu, Zuyan Liu, Ziyi Wang, He Zhang, Yongming Rao, Fangfu Liu, Yani Zhang, Ruowen Zhao, Oran Wang, Yves Liang, Haitao Lin, Minghui Wang, Yubo Dong, Kevin Cheng, Bolin Ni, Rui Huang, Han Hu, Zhengyou Zhang, Linus, Shunyu Yao

**机构**: Tencent Hunyuan

**💡 亮点 (Highlight)**: Introduces an iterative, self-evolving post-training paradigm for embodied foundation models, directly aligning with self-improving agent frameworks.

**摘要**: arXiv：2604.07430v1宣布类型：新摘要：我们引入了HY-propried-0.5，这是一系列专门为现实世界的具体化代理设计的基础模型。为了弥合一般视觉语言模型（VLM）和体现体主体需求之间的差距，我们的模型被开发为增强体现智能所需的核心能力：空间和时间视觉感知，以及用于预测、交互和规划的高级体现推理。HY-EQUIPED-0.5套件包括两个主要变体：一个是为边缘部署设计的具有2B激活参数的高效模型，另一个是针对复杂推理的具有32B激活参数的强大模型。为了支持对具体任务至关重要的细粒度视觉感知，我们采用了一种混合变形金刚（MoT）架构来实现特定于模态的计算。通过结合潜在标记，这种设计有效地增强了模型的感知表示。为了提高推理能力，我们引入了一个迭代的，自我进化的后训练范式。此外，我们采用按策略蒸馏将大型模型的高级功能转移到较小的变体，从而最大限度地提高紧凑模型的性能潜力。对22个基准（涵盖视觉感知、空间推理和体现理解）的广泛评估证明了我们方法的有效性。我们的MoT-2B型号在16个基准测试中的表现优于类似尺寸的最先进型号，而32 B的变体性能与Gemini 3.0 Pro等前沿型号相当。在下游机器人控制实验中，我们利用强大的VLM基础来训练有效的视觉-语言-动作（VLA）模型，在现实世界的物理评估中取得令人信服的结果。代码和模型在www.example.com上开放源代码。

[阅读原文](https://arxiv.org/abs/2604.07430)

---

## 31. LLM长上下文推理的分解视角

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Yanling Xiao, Huaibing Xie, Guoliang Zhao, Shihan Dou, Shaolei Wang, Yiting Liu, Nantao Zheng, Cheng Zhang, Pluto Zhou, Zhisong Zhang, Lemao Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Employs reinforcement learning on pseudo datasets targeting decomposed atomic skills to improve LLMs' long-context reasoning ability.

**摘要**: arXiv：2604.07981v1公告类型：新摘要：长上下文推理对于复杂的现实世界应用至关重要，但对于大型语言模型（LLM）仍然是一个重大挑战。尽管长上下文推理的发展迅速，但目前的研究往往忽视了长上下文推理任务本身的内部复杂性。在本文中，我们超越了这种整体观点，将长上下文推理分解为一组基本的原子技能，然后自动合成一套伪数据集，每个伪数据集都明确针对特定的原子技能。我们的实证分析证实，这些原子技能的熟练程度与一般长文本推理性能密切相关。基于这一见解，我们对这些伪数据集采用强化学习来提高模型的原子技能，希望增强其一般长上下文推理能力。跨多个基准的广泛实验证明了我们方法的有效性：在Loxit、Loong、LongBench-v2、BrowscompLong、Ruler-qa 2和MRCR中，它的平均利润率优于强基线7.7%（从46.3%提高到54.0%）。

[阅读原文](https://arxiv.org/abs/2604.07981)

---

## 32. 一个不完美的验证者就足够好了：在吵闹中学习奖励

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Andreas Plesner, Francisco Guzm\'an, Anish Athalye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates the robustness of RL with Verifiable Rewards (RLVR) for LLMs to noisy verifiers, a core RL for LLMs topic.

**摘要**: arXiv：2604.07666v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）已成为训练后大型语言模型（LLM）的一种重要方法。然而，验证器很少是没有错误的;即使是确定性检查也可能不准确，而且对基于模型的判断的日益依赖加剧了这个问题。WLVR对此类噪音的鲁棒性程度以及有效训练所需的验证器准确性仍然是未解决的问题。我们通过在RL训练中引入噪音来研究代码生成和科学推理领域的这些问题。噪音率高达15%，峰值验证准确度在清洁基线的2个百分点内。这些发现在受控和基于模型的噪音类型、三个模型系列（Qwen 3、GLM 4、Llama 3.1）和模型尺寸从4 B到9 B之间是一致的。总体而言，结果表明不完美的验证并不构成WLVR的根本障碍。此外，我们的研究结果表明，从业者应该优先考虑中等准确性和高精确度，而不是完美验证。

[阅读原文](https://arxiv.org/abs/2604.07666)

---

