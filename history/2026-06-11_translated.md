# 💡 今日研究速览 (Daily Summary)

# LLM的RL
一波主要的创新浪潮是针对大型语言模型强化学习（RL）的基本局限性，特别是在推理方面。有几项作品解决了多步推理中的信用分配问题。**FlowTracer**和**3SPO**等框架通过跟踪注意力引发的信息流或使用状态评分来提供分步、代币级信用，超越了量化奖励。第二个关键趋势是RL与潜在推理的集成，**Dropout-GRPO**引入结构化随机性，以在连续的潜在思想链上实现团体相对政策优化（GRPO）。此外，该领域正在积极解决训练稳定性和数据效率问题：**CPPO**提出了代币级信任区域来减轻累积的前置码漂移，而**TD-Grokking**和**TRACE**分别通过分解问题和树结构化分配来解决稀疏奖励和部署预算低效率问题。最后，关键漏洞正在暴露，例如一次性GRPO训练推翻对齐的能力（**需要一个人才能对所有人产生偏见**）以及RL后推理模型中观察到的系统对齐漂移（**推理是否保留对齐？**）。

# 按政策蒸馏和自我改进
一个主导主题是完善政策提炼，超越简单的模仿，转向更复杂、结构一致的反馈机制。**锚定剩余政策蒸馏（AR-OPD）**和**SocraticPO**都在学生自己的推出过程中利用特权教师指导来减轻事后诸葛亮偏见，而**反馈一致在自我蒸馏中的作用** 明确表明，逐步一致的批评反馈是有效性的关键驱动力，优于二元奖励。该原则适用于各种模式，从弥合语音模型中的非语言感知（**ParaBridge**）到使用视觉反馈进行代码生成（**Visual-SDPO**）。该方法还被扩展到培训专门的代理，正如从激励一致的竞技场轨迹中提取的管道（**Bittensor Agent Arenas**）和**跨模式多教师政策蒸馏（MOPD）**用于多模式LLM。一个新颖的框架**角色-代理** 通过让单个LLM同时充当代理和环境，使用预测的状态对齐作为流程奖励来引导这种自我改进。

# 大型RL和探索
代理RL的进步集中在改善复杂、多回合环境中的勘探和信用分配。**DiRL**引入了一种方向感知探索策略，该策略使用模型表示来区分推理与记忆，而**N-GRPO**则通过嵌入级邻居混合来促进语义多样性。对于实际的代理部署，**GUI-AC**通过使用基础确定性进行自适应优势估计，增强了图形用户界面代理的持续学习。通过零方差查询的**查询回收**来解决代理搜索中稀疏奖励的挑战，这提高了训练效率。统一框架**TRACE**专门针对推出预算分配问题，以增强多回合代理RL中的奖励对比。

# 对齐和安全
对对齐的研究正在从训练后扩展到数据选择和防御。一个新颖的**耦合任务引用选择** 框架使用极小最大视图来确保安全的微调，通过数据策展直接改善一致性。在防御方面，DPO和GRPO等基于限制的方法被证明可以有效对抗属性推断攻击。一项严格的审计表明，用于创建推理模型的RL和蒸馏过程可能会系统性地降低可信度，从而导致对齐漂移（**推理是否保留对齐？**）。这凸显了整个RL管道需要进行强有力的安全评估。

# 多模式和专业架构
对于多模式模型，RL被应用于优化任务级目标，如**ARM**自回归模型中所示，该模型使用RL在生成和编辑中实现跨任务协同。一个专门的应用程序**SD-GRPO**通过分配每个片段的优势而不是单一的纯量奖励来解决长形式视觉语言生成问题。在语音领域，**多面交互性对齐**使用轴特定的奖励函数来优化全速语音模型行为。最后，一个新的蒸馏框架**PADD* 专门解决了使用路径细化政策优化从密集教师中培训混合专家（MoE）学生的挑战。

---

## 1. 推理如何流动？跟踪LLM中目标RL的注意力引发的信息流

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhichen Dong, Yang Li, Yuhan Sun, Weixun Wang, Yijia Luo, Zinian Peng, Taiheng Ye, Chao Yang, Wenbo Su, Yu Cheng, Bo Zheng, Junchi Yan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FlowTracer, a novel RL framework that uses attention-induced information flow on a DAG to assign token-level credit for reasoning tasks, directly improving RL for LLMs.

**摘要**: arXiv：2606.10646v1宣布类型：新摘要：令牌级信用分配仍然是大型语言模型（LLM）中强化学习（RL）的一个关键障碍，其中RL食谱通常平等地对待所有令牌，无法区分决定性推理步骤与常规格式或流畅填充物。最近的尝试利用模型内部信号来分配更细粒度的信用，但这些通常是逐点启发式的，忽视了信息传播的全球结构。我们提出FlowTracer，这是一个RL框架，它在注意力诱导的有向无环图上跟踪以答案为目标的推理流，其中节点对应于代币，边缘容量来自聚合的注意力权重，并从这个全局结构中推导出代币信用。边缘容量被重新加权，以仅保留可以到达答案区域的影响，同时强制实施局部流量保守，以便中间令牌既不会因路径长度或不相关的分支而损失也不会获得有效质量。在此图表上，FlowTracer提取了将问题与答案连接起来的信息流主干，并通过流吞吐量对令牌进行评分，揭示了调解长期依赖性的高影响力中心和聚集检查点。这些衍生的重要性用于塑造代币级别的奖励，使学习信号能够准确地关注将信息传递到（或远离）正确答案的代币，并在一系列推理任务中提供一致的性能收益。

[阅读原文](https://arxiv.org/abs/2606.10646)

---

## 2. Dropout-GRPO：连续潜在推理的变分随机性

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Wooil Jung

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Dropout-GRPO, a novel method to introduce stochasticity into latent reasoning models via structured dropout, enabling GRPO to work on continuous latent reasoning and directly addressing a key limitation of RL for latent CoT.

**摘要**: arXiv：2606.10184v1宣布类型：新摘要：团体相对政策优化（GRPO）依赖于每个团体内$K$推出的多样性;否则，团体平均优势$A^{（k）} = r^{（k）} - \ku_r$崩溃为零。这对Coconut等潜在推理模型提出了结构性挑战，这些模型循环地提供连续的隐藏状态，而不是离散的思想链令牌。由于给定参数和提示，潜在阶段本质上是确定性的，因此多次推出会产生相同的轨迹，从而阻碍GRPO的进展。因此，将群体相对强化学习应用于连续潜在推理已被证明是困难的。   为了解决这个问题，我们建议通过结构性辍学来获取必要的随机性。通过在给定的展开的所有潜在重现步骤中应用保持不变的单个伯努里面具，我们生成基本的轨迹方差。这种共享面具有效地将每次推出视为参数变分分布的后验样本，允许GRPO优化Bayesian模型平均策略的预期回报。我们为这种方法提供了理论依据（包括无偏性、方差减少和潜在梯度的明确性）和经验验证。在GSM 8 K上，dropout-GRPO将Coconut基线从27.29美元\%$提高到29.01美元\%$pass@1，证明了GRPO学习用于潜在推理模型的可行性。我们的工作将其定位为培训后潜在推理LLM的一种实用、理论基础的方法。

[阅读原文](https://arxiv.org/abs/2606.10184)

---

## 3. 超越绝对模仿：紧缩政策蒸馏的锚定剩余指导

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Wenhao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Anchored Residual On-Policy Distillation (AR-OPD), a dual-view framework that disentangles privileged supervision in on-policy distillation to mitigate hindsight bias and improve reasoning in LLMs.

**摘要**: arXiv：2606.10385v1宣布类型：新摘要：政策提炼（OPD）通过将学生模型与教师对学生自身轨迹的预测分布保持一致，在增强LLM的复杂推理方面取得了巨大的经验收益。一种新兴的变体，即特权OPD，通过采用增强特权信息（例如Oracle痕迹）的自学模型，进一步加强了这一范式，以缩小师生能力差距，同时提供密集的、以答案为导向的监督。然而，当前的方法将特权信息视为单一的模仿目标，未能将本地可达的推理步骤与未来条件的Oracle信号区分开来。因此，鼓励学生匹配事后诸葛亮偏见的分布，而这种分布往往超出了当地预测支持范围。这种可达性不匹配激励学生模型跳过有效的中间推理，转而采用本地不支持的快捷方式。为了解决这个问题，我们引入了锚定剩余政策蒸馏（AR-OPD），这是一个二元视角框架，可以解开特权监督。AR-OPD没有强制执行严格的全视图模仿，而是使用部分特权教师建立本地兼容的锚点，隔离并注入Oracle预见作为受控剩余部分，以提供以目的地为导向的指导。在各种推理任务中，AR-OPD比完全特权OPD高出2.3分，比SFT高出7.9分。至关重要的是，这种锚定剩余机制将事后诸葛亮泄漏减少了21.7%，并减轻了后期漂移，在挑战超过768个代币的长视野轨迹上获得高达7.2个百分点的优势。

[阅读原文](https://arxiv.org/abs/2606.10385)

---

## 4. ParaBridge：言语语言模型中副语言感知和对话行为的桥梁

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yuxiang Wang, Qinke Ni, Shengbo Cai, Wan Lin, Liqiang Zhang, Zhizheng Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ParaBridge, an on-policy self-distillation method that turns brittle inference-time paralinguistic scaffolds into stable model behavior, directly matching the on-policy distillation criterion.

**摘要**: arXiv：2606.10581v1宣布类型：新摘要：言语承载的信息不仅仅是言语：孩子的声音、恐惧的语气或嘈杂的背景都应该引导足够称职的口语对话助理做出不同的回答。当前的语音语言模型（SLC）可以识别此类非语言暗示，但在开放式对话中经常忽略它们。我们观察到，推理阶段的简单双语言教学框架缩小了这种感知-行为差距，这表明相关线索已经潜伏在模型中。然而，在多回合环境和竞争指令下，此类支架仍然脆弱。因此，我们提出了\textBF{ParaBridge}，这是一种按策略的自我提炼方法，可以将脆弱的推理时框架转化为稳定的模型行为。在训练期间，支架仅充当临时特权视图;无支架模型推出自己的响应，而支架视图则沿着其轨迹提供密集、词汇量全的下一个令牌目标。这种监督教导非词汇线索何时应该影响回复，而不需要精心策划的对话、人类标签或外部奖励模型。在Qwen 3-Omni-thinking上，ParaBridge将无支架VoxSafeBench SAR从14.6美元提高到40.3美元，并将EchoMind平均评级从3.27美元提高到3.92美元。它还保留了一般功能，MMAU-Pro、SecureBench和GPQA均在原始型号的0.4美元积分之内。除了培训分布之外，ParaBridge还推广到看不见的非语言线索，从以安全为导向的培训转移到以同理心为导向的对话，并在不同的CRM主干上工作。

[阅读原文](https://arxiv.org/abs/2606.10581)

---

## 5. 推理还是精简？LLM强化学习中的方向感知多样性探索

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jiangnan Xia, Yucheng Shi, Yu Yang, Kishan Panaganti, Zhenwen Liang, Ninghao Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DiRL, a direction-aware RL framework that uses model representations to distinguish reasoning from memorization during exploration, integrated with GRPO for LLM reasoning improvement.

**摘要**: arXiv：2606.10346v1宣布类型：新摘要：强化学习已成为在大型语言模型中激发推理能力的关键范式，其中探索对于发现有效的解决方案轨迹至关重要。现有的探索方法通常鼓励语义或梯度空间的多样性，而不区分是什么驱动了这种多样性。轨迹可能看起来很新颖，因为它遵循新的推理过程，或者因为它改变了记忆的模式和捷径。平等地奖励这两种情况可能会将探索引向记忆，而不是真正的推理改进。在本文中，我们提出了DiRL，这是一个方向感知强化学习框架，它将探索锚定在政策的内部推理记忆方向上。具体来说，DiRL从模型表示中提取这个方向，构建方向加权梯度特征来描述滚动更新，并塑造奖励以放大推理一致的探索，同时抑制记忆一致的变化。DiRL无缝集成到标准的集团相对政策优化（GRPO）中。数学和一般推理基准的大量实验证明了DiRL的有效性，显示出比各种现有探索方法的显着改进。

[阅读原文](https://arxiv.org/abs/2606.10346)

---

## 6. 使用概率程序在大型语言模型中训练归纳推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Liyi Zhang, Akshay K. Jagadish, Brenden M. Lake, Thomas L. Griffiths

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Program-based Posterior Training (PPT), a novel on-policy distillation method that uses probabilistic programs to generate soft labels for training LLMs on inductive reasoning, directly improving calibration and alignment.

**摘要**: arXiv：2606.09856v1宣布类型：新摘要：用于推理的后训练大型语言模型（LLM）通常专注于演绎任务，例如数学和正确性可验证的编码。然而，许多现实世界的推理问题都是归纳的：代理人必须从稀疏、模糊的观察中推断出不确定的信念。使用标准微调方法进行归纳推理存在挑战，包括管理大规模、高质量的标签数据集以及处理本质上是分布式的目标方面的困难。在这项工作中，我们引入了一种新型方法，称为基于程序的后验训练（PPT），来解决这些局限性：我们使用LLM来生成不同的开放世界场景作为概率程序，运行概率推理以产生对查询的分布式目标响应，然后对这些概率软标签进行微调。使用这种方法，我们对10，000个以编程方式生成的场景进行微调，并对已发布的主题、人工标记的判断和外部基准进行评估。总体而言，PPT大大提高了对已完成的归纳任务的估计准确性，提高了与人类判断的一致性，并转移到外部基准进行估计和校准。此外，原始校准的收益并未被事后温度缩放所包含，这表明与输出重新缩放相比，模型具有更深入的内化不确定性。总而言之，这些结果表明，概率程序介导的微调对于训练后LLM来说是可靠地执行近似归纳推理的一种有前途的方法。

[阅读原文](https://arxiv.org/abs/2606.09856)

---

## 7. 通过视觉反馈的自蒸馏策略优化：桥接代码和视觉伪像

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haoyu Dong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Visual-SDPO, a self-distillation policy-optimization framework that uses visual feedback as privileged context for on-policy distillation, with a novel visual-grounded credit weighting and GRPO term.

**摘要**: arXiv：2606.10334v1宣布类型：新摘要：代码生成大型语言模型（LLM）通过编写由不可微渲染器执行的程序，在观察渲染之前承诺代码，越来越多地生成图表、网页和幻灯片等视觉产物。因此，其他可执行代码通常会产生具有视觉上明显缺陷的工件，包括重叠元素、剪辑文本、对齐方式不佳、对比度低和溢出。我们研究代码生成的视觉伪影的视觉反馈自我提炼。我们提出了Visual-SDPO，这是一个自我提炼政策优化框架，它将呈现的视觉反馈视为权重共享教师的特权上下文，并将此反馈提炼到编码学生中。为了使监管在空间上有针对性而不是统一，我们引入了视觉接地代码信用加权，该加权将每个检测到的缺陷追溯到负责受影响元素的代码陈述，并放大这些陈述上的提炼信号。序列级GRPO（组相对政策优化）术语通过奖励可执行的、视觉上高质量的推出来补充密集的代币级目标，而失败的执行通过将执行错误作为特权上下文传递给教师，通过自我提炼路径保持可学习。我们通过统一的Qwen 3-BL-8B-Direcct主干来实例化Visual-SDPO以生成图表、Web/UI和幻灯片。在图表到代码、UI到代码和幻灯片生成基准（ChartMimic、Design 2Code和AeSlides）中，Visual SDPO在主要指标上比零射击基础提高了10个绝对点以上，比GRPO提高了至少2.4个点，训练步骤更少，并且没有增加推断时间成本。

[阅读原文](https://arxiv.org/abs/2606.10334)

---

## 8. 混合LLM中的注意力缺失：CoT微调何时破坏了长期召回，以及如何解决它

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xinyu Zhou, Boyu Zhu, Yi Xu, Zhiwei Li, Yingfa Chen, Huiming Wang, Zhijiang Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies CoT-SFT causing long-context recall degradation in hybrid LLMs and proposes QK-Restore, a training-free method to restore long-range attention routing.

**摘要**: arXiv：2606.11052v1宣布类型：新摘要：思想链（CoT）监督微调（SFT）被广泛采用来提高推理能力，但我们发现它会系统性地降低混合线性注意力模型中的长上下文回忆。在HypeNet和Jet-Nemotron等架构中，CoT-SFT后，Needle-In-A-Haystack（NIAH）上的检索性能大幅恶化，并且在更严格的检索设置和更长的上下文窗口下，这种恶化变得更加严重。例如，NIAH-S2@ 256 K上的HypeNet-9 B从$67.2\%$下降至$9.4\%$。我们将其归因于CoT-SFT将注意力梯度偏向短程模式，扰乱了负责远程路由的查询关键预测（$W_Q，W_K$）。受这一观察结果的启发，我们提出了QK-Restore，这是一种免训练方法，它仅从SFT前检查点恢复$W_Q$和$W_K$，同时保留所有其他SFT后参数。我们进一步引入了Procrustes变体来平衡路由保留和推理适应。在各个架构中，QK-Restore始终以零训练成本恢复长上下文能力，同时保持推理性能;例如，在HypeNet-5 B上，它将S3@256K从65.4美元提高到76.4美元，同时保持强大的推理性能。

[阅读原文](https://arxiv.org/abs/2606.11052)

---

## 9. TD-Grokking：通过训练时间分解从零回报问题中学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ningyuan Xi, Hao Xu, Hongsheng Xin, Ning Miao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TD-Grokking, a training-time decomposition framework that recursively breaks zero-reward problems into verifiable subproblems to provide non-zero rewards for RLVR, directly addressing a key limitation of RL for LLMs.

**摘要**: arXiv：2606.09883v1宣布类型：新摘要：大型语言模型（LLM）在推理任务方面取得了显着进展，这在很大程度上是由训练后范式驱动的，特别是具有可验证奖励的强化学习（WLVR）。然而，一个关键的瓶颈仍然存在：WLVR在极具挑战性的零回报问题上失败，所有采样的推理轨迹都会产生一致失败的结果，没有提供优化信号来推动模型改进。之前为解决这一限制而做出的努力，例如密集流程监督、部分奖励分配或后缀引导的探索，都受到固有任务约束，或者没有完全为政策模型配备解决最初棘手问题所需的能力。为了解决这个问题，我们提出了TD-Grokking，这是一个针对零回报问题的训练时分解框架。它将棘手的根问题循环分解为独立的、可验证的子问题，形成分层树，其中可解的叶子提供非零奖励。对数学和医学任务的评估表明，TD-Grokking优于普通GRPO以及所有基线方法。再加上详细的分析，这些结果证实训练时分解可以有效地将零奖励示例转换为可用的训练信号，从而实现一致的性能提升。我们的代码和数据集可在https://anonymous.4open.science/r/TD-Grokking-6567/上获取。

[阅读原文](https://arxiv.org/abs/2606.09883)

---

## 10. 只有一个人才能偏见他们所有人：用一次性GRPO《绝命毒师》

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Naihao Deng, Yilun Zhu, Naichen Shi, Clayton Scott, Rada Mihalcea

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Demonstrates that one-shot GRPO training on a single biased example can systematically override LLM alignment, revealing a critical vulnerability in RL-based post-training.

**摘要**: arXiv：2606.10931v1宣布类型：新摘要：警告：本文包含几项有毒和冒犯性陈述。   现代大型语言模型（LLM）通常通过大规模后训练进行调整，以确保行为公平可靠。在这项工作中，我们研究了团体相对政策优化（GRPO）如何容易打破此类护栏。我们表明，对单个有偏见的示例进行一次性GRPO训练足以引发系统性偏见，立体类型驱动的推理在属性、类别和基准上进行概括。我们进一步发现，模型的敏感性取决于产生有偏差输出的初始可能性。我们的结果揭示了训练后的一个关键漏洞：对齐可以被单个示例覆盖。

[阅读原文](https://arxiv.org/abs/2606.10931)

---

## 11. 3SPO：针对LLM代理的状态评分监督政策优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yu Han, Kailing Li, Yang Jiao, Yulin Dai, Yuqian Fu, Linhai Zhuo, Tianwen Qian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL algorithm for LLM agents that performs step-wise policy optimization using state scores from historical success rates, addressing sparse reward credit assignment without value functions.

**摘要**: arXiv：2606.09961v1宣布类型：新摘要：通过强化学习（RL）将大型语言模型（LLM）训练为自主代理，使前沿模型能够在长期任务中实现超人的性能。然而，现有的RL算法在轨迹级别上运行，只有在收集完整的剧集推出后才执行策略优化。这种粗粒度方法在多回合代理环境中面临着根本性挑战，其中奖励稀疏、延迟，并且各个步骤之间的信用分配至关重要。在这项工作中，我们提出了\textBF{State-Score-Supervised Policy Optimism（3SPO）}，这是一种新型RL算法，通过动态状态评分监督执行步后策略优化。在每一步，3SPO都会根据历史成功率计算状态评分，监督逐步信用分配、自适应推出和步骤后政策优化，而无需价值函数估计或额外的辅助模型。从理论上讲，在逐状态强盗抽象下，我们表明所提出的分数监督分配机制实现了log分配遗憾，并为动作识别、分数互换性和过滤稳定性提供了样本复杂性保证。在ALFWorld和WebShop上使用Qwen 2.5 -1.5B/7 B-Direct进行的实验表明，3SPO在ALFWorld上的表现始终优于GRPO，分别高出+22.6美元和+15.6美元，同时使用类似的资源来实现2.4美元的状态探索和1.8美元的更快收敛。代码可在https://github.com/genalyu/3SPO上获取。

[阅读原文](https://arxiv.org/abs/2606.09961)

---

## 12. 反馈一致在自我蒸馏中的作用

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Semih Kara, O\u{g}uzhan Ersoy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that step-aligned critique feedback in self-distillation outperforms binary reward (GRPO) and reference-solution conditioning, revealing structural alignment as a key driver of distillation effectiveness.

**摘要**: arXiv：2606.11173v1宣布类型：新摘要：根据额外的上下文（例如对先前尝试的反馈）来调节语言模型通常会改善其响应。自蒸馏训练模型在上下文不存在时保留这种改进。该方法的工作原理是在两种设置下匹配模型的输出分布：学生只看到问题，而自学教师也看到上下文。因此，模型学到的内容取决于自学者收到的背景，但这种背景的设计在很大程度上仍然没有探索。   我们通过根据冻结的批评者的反馈训练求解器来研究自我升华的上下文设计。我们比较三个条件：（i）二元奖励（GRPO），（ii）参考解决方案，以及（iii）与求解器推理轨迹一致的逐步批评。   分步批评产生的收益最大，比GRPO高16.11分，比参比溶液条件自蒸馏高5.27分（Avg@12）。每个代币的优势分析揭示了原因：逐步对齐的反馈仅针对推理失败的代币，而正确的行为完好无损。相比之下，以参考解决方案为条件会迫使模型在每个符号上改变其行为（甚至是正确的步骤），因为替代推导不可避免地在措辞和方法上有所不同。这表明反馈和求解器推理之间的结构一致性是自我提炼有效性的关键驱动力。

[阅读原文](https://arxiv.org/abs/2606.11173)

---

## 13. 角色-代理：通过双重角色进化引导LLM代理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xucong Wang, Ziyu Ma, Shidong Yang, Tongwen Huang, Pengkun Wang, Yong Wang, Xiangxiang Chu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dual-role framework where a single LLM acts as both agent and environment, using predicted state alignment as a process reward for on-policy self-improvement, directly relevant to RL for LLMs and on-policy distillation.

**摘要**: arXiv：2606.10917v1宣布类型：新摘要：尽管大型语言模型（LLM）代理在复杂任务上表现出了出色的性能，但它们的学习通常受到低效的交互反馈和静态训练环境的限制，这阻碍了更广泛的概括。为了解决这些限制，本文引入了角色代理，\textColor{black}{a framework}，它利用单个LLM同时充当代理和环境，从而实现自举协同进化。角色Agent包括两个协同的组件：World-In-Agent（WIA）和Agent-In-World（AIW）。在WIA中，LLM充当智能体，并在每个动作后预测未来状态;预测状态和实际状态之间的对齐然后用作过程奖励，鼓励环境感知推理。在AIW中，LLM从失败的轨迹中分析失败模式，并检索具有类似失败模式的任务，从而重塑训练数据分布以进行有针对性的实践。在多个基准测试上的实验表明，Role-Agent一致地提高了性能，在强基线上平均增益超过4%。

[阅读原文](https://arxiv.org/abs/2606.10917)

---

## 14. Bittendor Agent Arenas作为轨迹原始人：从ShoppingBench Subnet痕迹中提取购物代理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shardul Bansal, Seth Schilbe, Jarrod Barnes

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an on-policy distillation pipeline using incentive-aligned arena trajectories and a per-step teacher-grounded Dr. GRPO reward to improve a small LLM agent, with a structural-quality filter for trajectory selection.

**摘要**: arXiv：2606.10064v1宣布类型：新摘要：小模型代理后训练受到算法的干扰，而不是它消耗的轨迹基片的干扰。领先的配方（WLVR、组相关RL、拒绝采样的重新SFT）都需要多圈跟踪来进行按轨迹的监督，并且两个现有的来源都存在缺陷：前沿合成数据继承合成器的偏差并折叠长尾，而未经过滤的生产日志不会被判断并被捷径行为污染。我们认为，可以设计一个激励一致的代理领域来制造这样的轨迹，并在ORO Subnet 15（SN 15）上演示这一点，ORO Subnet 15（SN 15）是ShoppingBench代理商务基准的Bittensor部署。SN 15的竞赛机制、LLM推理判断器和旋转泄漏集群保护问题套件产生了具有三个属性的文集：激励一致的多样性、按轨迹判断和反记忆持有评估。我们引入了一个结构质量过滤器，通过保留代理轨迹（模型本身发出工具调用）和拒绝子任务轨迹（模型仅在确定性搜索循环中分类或叙述），将原始消防水带转换为可训练的文集，然后使用与已发布的ShoppingBench SFT-then-GRPO管道相匹配的食谱进行后训练Qwen 3 - 4 B。在具有泄漏保护、评分为生产严格的保留分区上，该模型从已发布的Qwen 3 - 4 B基础18.0%的ASB提升到42.7%，在仅合成数据SFT基线的单一问题噪音范围内（43.6%），同时训练时间仅为单日子网输出的一小部分。监督堆栈留下了很大的pass@8与pass@1差距（53.3% vs 34.8%）;每一步基于教师的Dr. GRPO奖励将该裕度转化为流程改进，我们将子任务消防水带确定为缩小与48.7% SFT+GRPO条差距的主要杠杆。我们释放过滤器、主体分裂和舞台机制。

[阅读原文](https://arxiv.org/abs/2606.10064)

---

## 15. 对齐保护LLM免受财产推理攻击

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pengrun Huang, Chhavi Yadav, Ruihan Wu, Kamalika Chaudhuri

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes alignment-based defenses (DPO/GRPO) against property inference attacks, directly applying RLHF frameworks as a defense mechanism for LLMs.

**摘要**: arXiv：2606.10217v1宣布类型：新摘要：大型语言模型（LLM）越来越多地针对可能包含敏感的数据库级别属性的特定领域数据集进行微调。最近的工作表明，此类厕所级信息可以通过属性推断攻击有效提取，从而构成保密风险。针对这些攻击的现有防御措施主要通过修改训练数据分布来运作，因此需要访问原始数据并重新训练模型，从而限制其对数据不可用或模型已经部署的设置的适用性。在这项工作中，我们提出了基于限制的防御措施来减轻LLM中的属性推断攻击。我们的方法通过训练后对齐将模型的输出分布重塑为目标属性比率，而无需修改训练数据。特别是，我们采用了两个广泛使用的RL HF框架--直接偏好优化（DPO）和群体相对政策优化（GRPO）--通过分别构建偏好对和定义特定的奖励函数来作为我们的防御措施。通过全面的实验，我们表明我们基于对齐的防御可以有效地减轻属性推理攻击，同时保持强大的效用机密性权衡。

[阅读原文](https://arxiv.org/abs/2606.10217)

---

## 16. Two to Tango：安全LLM微调的耦合任务参考选择

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinrui Chen, Jianhao Zhang, Ou Wu, Di Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a coupled task-reference selection framework for safe LLM fine-tuning that uses a minimax view and entropy-regularized scoring, directly improving alignment via a novel RL-adjacent data selection method.

**摘要**: arXiv：2606.09866v1宣布类型：新摘要：对下游数据进行安全调整的大型语言模型（LLM）可以改善适应性，但可能会削弱习得的安全行为。现有方法使用固定的安全示例、全局约束或单边任务过滤。我们的诊断显示任务更新暴露了不同的安全限制，从而激励联合选择相关参考和兼容的任务样本。我们提出了Dualselect，这是一个任务和参考选择的耦合框架，它在过滤与诱导参考方向兼容的整个任务样本之前刷新任务条件安全参考。在极小最大视图下，Dualselect通过熵化评分代理、懒惰引用刷新和梯度修正来选择具有高保存损失和任务冲突的安全引用以及兼容的任务样本。在1B-8B LLM上，Dualselect在不失去任务效用的情况下保留了安全性;使用REDORCA判断器，它可以提高安全平均值。比最强基线至少高出5.10分，并且在安全平均中保持最高。以适度的管理费用跨越法官。这种观点延伸到以保留为中心的持续学习。

[阅读原文](https://arxiv.org/abs/2606.09866)

---

## 17. GUI-AC：增强图形用户界面代理中的持续学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Can Lin, Tao Feng, Hangjie Yuan, Dan Zhang, Yifan Zhu, Zhonghong Ou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces GUI-AC, a method enhancing continual learning in GUI agents via grounding certainty for adaptive advantage estimation and dynamic clipping in reinforcement fine-tuning, directly improving RL for LLM-based agents.

**摘要**: arXiv：2606.10522v1宣布类型：新摘要：图形用户界面（GUIs）是人机交互的主要媒介，但构建具有广泛多样性的现实世界界面环境、具有人类自然表现出的相同灵活性和鲁棒性的图形用户界面代理仍然没有得到解决。值得注意的是，图形用户界面数据本质上是非稳定的：以前看不见的界面实例的不断出现（例如，新的域和解决方案）会导致持续的分布转变，从而严重阻碍了现有图形用户界面代理的持续学习。强化微调（RFT）作为一种有前途的方法引起了相当大的关注。然而，RFT的接地能力表现出明显的不稳定性，表现为尖锐的回报不连续性和高方差振荡。推出结果的不平衡分布给优势估计带来了巨大的噪音，导致政策过度自信。固定剪切界限抑制了适应新分布所需的政策概率的增加，导致勘探能力崩溃。为了解决这些挑战，我们提出了GUI-AC，这是一种增强图形用户界面代理持续学习能力的方法。GUI-AC引入了接地确定性来支持两个核心机制：（i）自适应优势，降低噪音优势估计的权重，以防止政策过度自信;（ii）动态剪裁，放宽剪裁界限，以鼓励勘探范围。大量实验表明，这些机制共同提高了性能，使我们的方法能够超越最先进的基线。代码可在https://anonymous.4open.science/r/GUI-AC上匿名获取。

[阅读原文](https://arxiv.org/abs/2606.10522)

---

## 18. TRACE：用于高效统计强化学习的统一推出预算分配框架

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Heming Zou, Qi Wang, Yun Qu, Yuhang Jiang, Lizhou Cai, Yixiu Mao, Ru Peng, Xin Xu, Weijie Liu, Kai Yang, Saiyong Yang, Xiangyang Ji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a tree-structured rollout allocation framework (TRACE) to enhance reward contrast in multi-turn agentic RL for LLMs, directly addressing a key limitation of RLVR.

**摘要**: arXiv：2606.1119v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）是一种在大型语言模型中增强推理和代理行为的有前途的方法。然而，推出密集型政策优化通常受到奖励对比不足的限制，这种对比是在过于简单或复杂的提示生成低方差反馈以及仅结果奖励为多回合推出中的每个决策分配相同的最终评估时出现的。过去的工作重点是将可用的推出资源分配给有希望的提示，但他们只利用提示级别的样本信息量，而忽视了同一推出内不同回合中后缀级别信息量的变化。这项工作的目标是多回合代理RL，通过将每个ReAct风格的思想-行动-观察回合建模为一个语义上不同的节点，允许预算分配从提示根延伸到回合级前置，并进一步延续，这自然形成了树结构的推出。我们引入了对比探索树展开分配（TRACE），这是一个统一的展开分配框架，可以在固定抽样预算内增强奖励对比度。从技术上讲，TRACE将推出预算分配给最有可能产生混合终端奖励的提示词根和中间词头。共享的可推广预测器根据前置历史估计这些锚点的条件成功概率，以指导此分配。由此产生的自适应树结构丰富了纯结果反馈并放大了策略更新信号。经验上，TRACE在典型的代理基准上实现了有竞争力的性能和效率提升，例如，在同等抽样成本下，Qwen 3 - 14 B多跳QA平均准确性比竞争基线提高2.8个百分点。

[阅读原文](https://arxiv.org/abs/2606.11119)

---

## 19. N-GRPO：嵌入级邻居混合以增强策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xukun Zhu, Hang Yu, Peng Di, Linchao Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes N-GRPO, a novel embedding-level neighbor mixing exploration strategy integrated into GRPO for RL-based LLM reasoning, directly improving policy optimization via semantic diversity.

**摘要**: arXiv：2606.10768v1宣布类型：新摘要：大型语言模型在数学推理中的成功在很大程度上依赖于在推出阶段生成多样化且有效的解决方案路径。然而，当前的推出技术面临着一个根本的权衡：标记级采样通常会产生仅在改写方面有所不同的冗余轨迹，而利用随机噪音的嵌入级方法经常会破坏语义一致性。为了解决这个问题，我们引入了N-GRPO，一种新的探索策略集成到组相对策略优化（GRPO）框架。我们的方法不依赖于令牌级采样或本地嵌入级噪声，而是利用语义邻居混合。该机制通过混合锚令牌及其最近语义邻居的嵌入来动态地构造输入表示，从而在严格遵守本地语义流形的同时注入多样性。在不同规模的DeepSeek-R1-Distill-Qwen模型上进行的实验评估表明，N-GRPO不仅在数学推理基准上实现了强基线的一致改进，而且在分布外任务上表现出强大的泛化能力。

[阅读原文](https://arxiv.org/abs/2606.10768)

---

## 20. SD-GRPO：用于长格式视觉语言生成的可验证段分解

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hyunwoong Kim, Seongeun Lee, Hannah Yun, Junhyun Park, Jonggwon Park

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SD-GRPO, a novel per-segment advantage assignment method for GRPO that improves long-form vision-language generation by replacing scalar rewards with vectorized per-segment advantages.

**摘要**: arXiv：2606.09871v1宣布类型：新摘要：组相对策略优化（GRPO）及其变体最初是为大型语言模型（LLM）开发的，最近已应用于多模式LLM并产生了强劲的结果。然而，它们来自单一纯量优势的粗粒度整体信用分配不适合视觉语言（VD）任务，其中的输出通常是基于语义丰富图像的长篇响应。为了解决这一限制，我们利用了单纯量公式所抛弃的结构化信号：长形式BL输出的自然分割。具体来说，我们提出了分段分解的GRPO（SD-GRPO），它对整个推出组中可验证的每分段奖励进行z-标准化，产生每分段优势的载体而不是单个纯量。我们在跨越受控和现实世界的长形式DL生成的三种环境中评估SD-GRPO，通过增加分段之间的语义纠缠来组织。在从DOCI构建的受控多面板密集字幕任务中，片段在语义上是独立的，SD-GRPO始终优于GRPO基线，在更高的片段计数下获得更大的收益。扩展到从MultiChartQA构建的受控多图表长形式VQA任务，我们从理论上和经验上表明，推出层面奖励受到随着产出长度而变化的跨部门信用错误归因的影响。在MMSci数据集上的现实世界科学人物字幕任务中，子人物字幕共享整个人物的上下文，混合整体奖励和按片段奖励进一步改善了两者，这表明当片段语义纠缠时，单独按片段规范化是不够的。最后，通过将SD-GRPO集成到Dr. GRPO中，我们确认它可以应用于任何GRPO框架，以最低的实施成本来增强长形式的BL生成。

[阅读原文](https://arxiv.org/abs/2606.09871)

---

## 21. SocraticPO：通过互动指导进行政策优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zirui Liu, Jie Ouyang, Qi Liu, Xianquan Wang, Jiayu Liu, Tingyue Pan, Qingchuan Li, Jing Sha, Zhenya Huang, Shijin Wang, Enhong Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SocraticPO, a policy optimization framework that augments RL rollouts with natural-language teacher guidance and reward decay, directly improving LLM reasoning via on-policy interaction.

**摘要**: arXiv：2606.09887v1宣布类型：新摘要：大型语言模型的强化学习（RL）通常会用纯量结果奖励（例如二进制正确性）来监督推理。此类奖励提供了优化方向，但很少解释模型应该如何修改其错误推理，这可能会鼓励捷径学习和脆弱政策。我们提出了\textBF{SocraticPO}（苏格拉底政策优化），这是一个政策优化框架，通过苏格拉底风格的自然语言指导来增强RL的推出。在推出过程中，学生首先独立回答;如果答案不正确，老师会诊断尝试并提供简洁的纠正指导，然后学生在扩展的背景下继续回答。至关重要的是，这种指导与奖励衰变相结合：教师干预后获得的正确答案只会获得衰变的奖励，从而防止政策将教师帮助视为获得奖励的自由途径。由于SocraticPO只修改推出流程，同时保留标准预期回报目标不变，因此它可以插入现有的政策梯度后台，例如Reinforce++。此外，由于教师仅提供文本级别的指导，SocraticPO可以利用更强大的黑匣子教师模型，而无需访问日志或分布匹配。在SciKnowEval的本科生科学推理基准上，SocraticPO优于强大的RL和自我蒸馏基线。消融表明有针对性的指导和奖励衰减都是必要的，奖励衰减可以减轻对辅助纠正的依赖。

[阅读原文](https://arxiv.org/abs/2606.09887)

---

## 22. PADD：针对非路由器教师的路径对齐减压蒸馏，以指导MoE学生学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinyue Peng, Yi Qian, Jiaojiao Lin, Wenjian Shao, Yanming Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel distillation framework (PADD) for training MoE students from dense teachers with online adaptive distillation and path-refined policy optimization, directly relevant to on-policy distillation.

**摘要**: arXiv：2606.10369v1宣布类型：新摘要：随着大型语言模型（LLM）的不断扩展，在固定计算预算下增加模型容量变得越来越具有挑战性。我们提出了路径对齐解压蒸馏（PADD），这是一个框架，用于从密集教师中提取知识，而无需明确路由到混合专家（MoE）学生，同时学习高质量的路由策略。PADD将知识提炼分为两个阶段的四个阶段：初始化阶段（第一阶段），通过教师神经元集群和学生专家热身在学生专家中构建多样化的功能，以及训练阶段（第二阶段-第四阶段），将在线自适应提炼、路径细化的政策优化和奖励增强的负载平衡集成在单个训练管道中。数学推理基准上的实验表明，PADD在相同的推理成本下比强基线产生了实质性的收益，并且MoE学生可以匹配或超过其密集的老师。它们还展示了有效的教师对学生的知识提炼和稳定的路由行为。

[阅读原文](https://arxiv.org/abs/2606.10369)

---

## 23. 全速语音模型中的多面交互对齐

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Atsumoto Ohashi, Neil Zeghidour, Alexandre D\'efossez, Eugene Kharitonov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-faceted RL alignment method with axis-specific reward functions for full-duplex speech models, directly improving interactivity via RL.

**摘要**: arXiv：2606.11167v1宣布类型：新摘要：全速口语对话模型可以同时听和说，使它们成为自然对话的有前途的架构。然而，当前的模型仅通过令牌级似然最大化进行监督学习来训练，这不会直接优化交互级行为，从而导致过度沉默和不合时宜的轮流等交互问题。最近的工作应用了强化学习（RL）来改善交互性，但现有方法在奖励中仅解决有限的一组交互行为。在这项工作中，我们提出了一种训练后对齐方法，该方法通过RL全面提高了双环口语对话模型的交互性。我们解决了交互性的四个典型轴：暂停处理、轮流、反向通道和用户中断。对于每个轴，我们从人类对话库中提取短音频片段，并使用轴特定的奖励函数优化模型。额外的基于LLM的响应质量奖励可以防止语义退化。我们将我们的方法应用于两个开源模型Moshi和Personailon，展示了在使用预录制音频的离线评估和实时多轮对话评估方面的交互性方面的一致改进。

[阅读原文](https://arxiv.org/abs/2606.11167)

---

## 24. Kwai Keye-DL-2.0技术报告

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kwai Keye Team, Bin Wen, Changyi Liu, Chengru Song, Chongling Rao, Guowang Zhang, Han Li, Haonan Fan, Hengrui Ju, Jiankang Chen, Jiapeng Chen, Jiawei Yuan, Kaixuan Yang, Kaiyu Jiang, Kun Gai, Lingzhi Zhou, Na Nie, Sen Na, Tianke Zhang, Tingting Gao, Xuanyu Zheng, Yulong Chen, Fan Yang, Haixuan Gao, Lele Yang, Mingqiao Liu, Muxi Diao, Qi Zhang, Qile Su, Wei Chen, Wentao Hong, Xingyu Lu, Yancheng Long, Yankai Yang, Yingxin Li, Yiyang Fan, Yu Xia, Yuzhe Chen, Ziliang Lai, Chuan Yi, Haonan Jia, Tianming Liang, Weixin Xu, Xiaoxiao Ma, Yang Tian, Yufei Han, Feng Han, Hang Li, Jing Wang, Jinghui Jia, Junmin Chen, Junyu Shi, Ruilin Zhang

**机构**: Kuaishou Technology

**💡 亮点 (Highlight)**: Introduces Cross-Modal Multi-Teacher On-Policy Distillation (MOPD) for multimodal LLMs, a new on-policy distillation method that improves agentic capabilities.

**摘要**: arXiv：2606.10651v1宣布类型：新摘要：我们引入Kwai Keye-VL-2.0- 30 B-A3 B，这是一个开源专家混合（MoE）多模式基础模型，旨在促进长视频理解和代理智能。为了解决超长上下文、信息冗余和小时级视频固有的高昂计算成本的挑战，Keye-BL-2.0是第一个将DeepSeek稀疏注意力（DSA）调整到基于GQA的多模式架构的产品，实现无损256 K上下文处理，同时捕获关键帧和长期时间依赖关系。该架构以高度优化的训练和推理基础设施为基础，包括可扩展的视频I/O、异类ViT-LM并行性和自定义DSA内核，可以显着最大限度地提高吞吐量并最大限度地减少计算负担。此外，为了克服多任务对齐过程中灾难性遗忘的算法困境，我们引入了与Context-RL和Video-RL配对的跨模式多教师按政策蒸馏（MOPD）。通过将来自政策部署的密集代币级教师反馈提取回仅激活3B参数的MoE主干网，Keye-DL-2.0通过多模式自我纠正，原生支持跨代码、工具和搜索场景的高级代理协作。对视频理解、时间基础、推理、STEM和代理基准的广泛评估表明，Keye-VL-2.0- 30 B-A3 B在相似规模的模型中实现了最先进的性能，特别是在TimeLens上的细粒度时间定位和Video-MME-v2和LongVideoBench上的长视频理解方面表现出色。我们发布了模型检查点，以加速社区向可扩展和稳健的多模式代理应用程序迈进。

[阅读原文](https://arxiv.org/abs/2606.10651)

---

## 25. 通过在训练期间回收零方差搜索来进行有效的强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jo\~ao Coelho, Jo\~ao Magalh\~aes, Bruno Martins, Chenyan Xiong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes query recycling for GRPO-style RL training of LLM search agents, dynamically reusing zero-variance queries to improve training efficiency and policy co-evolution.

**摘要**: arXiv：2606.10709v1公告类型：新摘要：GRPO式算法的使用已经成为在仅结果奖励下训练LLM搜索代理的标准策略。使用这些算法，只有当其推出组混合成功和失败时，查询才有助于参数更新;全正确（太容易）和全不正确（太难）组是零方差和浪费推出成本。现有的方法将零方差视为静态属性，并丢弃或预过滤此类组。我们假设并通过经验验证，随着政策在训练期间的发展，查询会在零方差和信号承载状态之间翻转。基于这一直觉，我们提出了查询回收，将零方差组返回到可变池以供未来重新分配，以便有效的训练分布与策略共同进化。使用所提出的技术，在合成数据上训练的1.7B参数模型可以通过七个多跳QA基准达到66.0平均Pass@1，匹配或超越在基准衍生监督上训练的最多7 B参数的系统。对回收模式的分析表明，到培训结束时，回收的查询提供了大约四分之三的有效批次，贡献分为政策改进的恢复和政策漂移的恢复。

[阅读原文](https://arxiv.org/abs/2606.10709)

---

## 26. Mult-DPO：推荐系统的多项直接偏好优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yaochen Zhu, Harald Steck, James McInerney, Aditya Sinha, Yinhan He, Nathan Kallus, Jundong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Mult-DPO, a novel tractable multinomial DPO objective for set-wise preferences in LLM-based recommender systems, with a theoretical bound on the PL DPO loss.

**摘要**: arXiv：2606.10078v1宣布类型：新摘要：直接偏好优化（DPO）是一种基于成对偏好的大型语言模型（LLM）的简单有效的对齐策略。然而，在推荐系统中，用户反馈很少是成对的。对于给定的上下文，例如，对于用户、会话或对话，我们通常会观察具有多个积极项目的集合偏好，其中每个积极项目的级别都应该高于每个未观察到的或明确的消极项目，并且积极项目或消极项目本身之间没有规定的顺序。一个自然的概括是使用Plackett-Luce（PL）奖励模型，该模型将香草DPO基础的Bradley-Terry奖励模型从成对偏好扩展到候选人的完整排名。然而，我们表明，将PL模型适应集合偏好需要对所有正序进行边缘化，其中所得的表达在复杂性上是组合的。为了解决这一根本挑战，我们提出了Mult-DPO，这是一种新颖的DPO目标，具有对集合偏好事件的易于处理的多项代理可能性，用于基于LLM的推荐系统的用户偏好对齐。多项结构本身并不是排名分布，但它是在相同的奖励诱导权重空间上定义的，并承认封闭形式的DPO式目标，从而能够通过分类式目标将LLM与多个候选人直接对齐。此外，我们还证明，当针对集式偏好数据进行优化时，多项DPO损失是边缘化PL DPO损失的一个易于处理的上界。我们进一步根据积极因素与消极因素的相对总权重来描述这一界限的严格程度，这为通过更丰富或更硬的消极因素来收紧界限提供了见解。最后，我们将Mult-DPO扩展到具有多个偏好水平的LLM的一致。代码可访问https://github.com/yaochenzhu/Mult_DPO

[阅读原文](https://arxiv.org/abs/2606.10078)

---

## 27. LLM强化学习中超越统一令牌级信任区域

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Renjie Mao, Xiangxin Zhou, Lvfang Tao, Yixin Ding, Yu Shi, Yongguang Lin, Yuheng Wu, Honglin Zhu, Qian Qiu, Wenxi Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CPPO, a token-level masking rule for RLVR that addresses autoregressive asymmetry and cumulative prefix drift, directly improving LLM reasoning training stability and accuracy.

**摘要**: arXiv：2606.10968v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）已成为改进LLM推理的标准。然而，现有的LPO式信任区域机制通过在所有令牌上独立实施统一阈值而保持位置不可知。这种逐点的处理方式在两个关键方面与自我回归生成相冲突。首先，统一阈值忽略了自回归不对称性。早期偏离会产生复合序列水平漂移，导致静态阈值对早期偏离调节不足并过度限制后期勘探。其次，孤立地评估代币级别的分歧会忽略累积的前置漂移，无论条件化历史已经偏离推出政策多远，都会授予相同的分歧津贴。为了解决这一限制，我们提出了CPPO（累积Prefix-division Policy Optimism），这是一种标记级掩蔽规则，通过两种耦合机制将更新与有限视野策略改进界限保持一致。首先，头寸加权阈值对影响持续更长时间的早期头寸施加了更严格的限制，从而放松了对后期代币的限制。其次，累积前置预算跟踪历史偏差，动态限制进一步的代币级别偏差，以防止沿着前置出现复合错误。从经验上看，CPPO增强了训练稳定性，并显着提高了各种模型尺度的推理准确性。

[阅读原文](https://arxiv.org/abs/2606.10968)

---

## 28. 推理能保持一致吗？论大型推理模型的可信度

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Prajakta Kini, Avinash Reddy, Souradip Chakraborty, Satya Sai Srinath Namburi GNVV, Furong Huang, Amrit Singh Bedi, Alvaro Velasquez

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically audits alignment drift in reasoning models produced via RL and distillation, revealing critical trustworthiness regressions that are central to RL-for-LLMs and on-policy distillation.

**摘要**: arXiv：2606.11046v1宣布类型：新摘要：指令调整的LLM越来越多地通过后训练转化为推理模型，以提高多步骤任务性能。这种转换通常针对推理准确性进行优化，而不会明确保留描述调整模型的对齐行为，例如安全拒绝、偏见避免和隐私保护。我们要问：这种转换是否保持了对齐？我们研究这个问题，通过可信度审计，发现它不是默认的行为保持。为了进行系统分析，我们将通过监督微调，基于RL的后训练和蒸馏产生的推理模型与六个可信度维度的匹配的预防调整基线进行比较：安全性，毒性，刻板印象和偏见，机器伦理，隐私和分布鲁棒性。我们观察到，推理模型往往改善推理基准，但表现出对齐回归，包括增加毒性，放大刻板印象，错误校准拒绝，和上下文隐私泄漏。这些回归与通过KL偏差测量的从描述调整基线的行为漂移一致。总体而言，我们的结果指出了一个更广泛的结论，即可信度指标对于评估推理模型至关重要，并且应该与推理能力的提高一起报告。

[阅读原文](https://arxiv.org/abs/2606.11046)

---

## 29. 当RL在SFT后失败时：恢复模型可塑性以实现稳健的SFT到RL切换

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Runze Liu, Jiashun Liu, Xu Wan, Yuqian Fu, Ling Pan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a method to restore model plasticity for robust SFT-to-RL handoff, directly addressing a key failure mode in the RL-for-LLMs pipeline.

**摘要**: arXiv：2606.09932v1宣布类型：新摘要：监督微调（SFT）和强化学习（RL）已成为大型语言模型（LLM）后训练的标准管道。SFT有望为RL提供有用的行为先验，以进一步增强模型能力。然而，SFT过高的检查点在RL期间通常表现出有限的改善。我们将这种失败归因于模型可塑性的丧失：SFT初始化的策略被后续RL有效重塑的能力降低。为了更好地理解这种现象，我们从多个角度进行了详细分析，包括参数变化、输出空间和RL优化动态。我们的结果表明，来自过度SFT的模型往往会产生过度自信的代币分布，并表现出尖锐的参数景观，这使得它们在RL阶段更难优化。为了实现更稳健的SFT到RL切换，我们提出了\textttt {Rejuvenation}，这是一种简单而有效的方法，可以恢复可塑性，同时保留有用的SFT获得的先验。Rejuation利用碱基锚定模型融合来减少SFT引起的过度漂移，并重置目标神经元以减轻模型刚性。数学推理任务和代理任务的实验结果都表明，我们的方法在过度训练的SFT模型上持续提高了RL性能，同时还增强了对非分布任务的概括性。

[阅读原文](https://arxiv.org/abs/2606.09932)

---

## 30. ARM：具有统一离散表示的自回归大型多峰模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Junke Wang, Xiao Wang, Jiacheng Pan, Xuefeng Hu, Feng Li, Jingxiang Sun, Chaorui Deng, Zilong Chen, Yunpeng Chen, Kaibin Tian, Matthew Gwilliam, Hao Chen, Danhui Guan, Kun Xu, Weilin Huang, Zuxuan Wu, Haoqi Fan, Yu-Gang Jiang, Zhenheng Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies RL to optimize task-level objectives for a multimodal autoregressive model, improving generation and editing quality with cross-task synergy.

**摘要**: arXiv：2606.11188v1宣布类型：新摘要：本文介绍了ARM，这是一种基于离散表示的自回归模型，它将图像理解、生成和编辑统一在下一个令牌预测框架内。ARM基于三项工作：首先，我们训练一个离散的语义视觉标记器，将图像映射为紧凑的标记序列。我们的标记化器受到多个目标的监督，共同促进语义可辨别性、语言对齐和忠实重建，从而支持共享潜在空间中的多样化任务。借此，我们在大规模文本和图像标记序列上训练7 B自回归模型，无缝开发视觉语言感知和生成能力。最后，为了进一步改善文本到图像生成和描述引导编辑的偏好一致行为，ARM应用强化学习（RL）来优化任务级目标，例如视觉质量、指令遵守性和编辑一致性。令人惊讶的是，结果表明RL不仅大幅提高了目标任务的性能（例如，将WISE总体从0.50提高到0.56，Gedit-Bench-EN G_O从5.75提高到6.68），而且还在文本到图像生成和编辑之间引入了跨任务协同作用。总的来说，这些发现强调了自回归建模，当与强表示和偏好优化相结合时，是多模式智能的可扩展基础。代码：https://github.com/wdrink/ARM。

[阅读原文](https://arxiv.org/abs/2606.11188)

---

## 31. 具有代表性的优势估计：您的奖励模型提供的不仅仅是量化输出

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Guozheng Li, Xiyan Fu, Yiwen Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GraphAE, a method that leverages reward model hidden states via graph-based advantage estimation to improve RLHF sample efficiency and robustness.

**摘要**: arXiv：2606.10528v1宣布类型：新摘要：当前的人类反馈强化学习（RL HF）方法主要依赖于来自训练奖励模型（RM）的纯量奖励。虽然有效，但纯量奖励通常是有噪音的，并且无法捕捉细粒度的偏好差异，而RM隐藏状态编码了更丰富的语义和偏好信息。我们引入了表示感知优势估计，它利用RM隐藏状态并将它们建模为辅助信号以获得更好的优势估计。具体来说，我们提出了基于图的优势估计（GraphAE），将每个采样组视为一个图，其中节点对应于响应，边捕获它们在RM隐藏空间中的相似性。然后通过图传播计算优势，使每个样本能够合并来自其邻居的上下文信息。GraphAE是轻量级的，可以无缝集成到现有的基于组的RL算法中。我们将GraphAE应用于GRPO、GSPO和RLOO，并对不同的模型和基准进行了广泛的实验。经验结果显示，三个基准的增长一致，Arena-Hard-v0.1上的增长高达+6.3，AlpacaEval 2.0上的增长高达+8.27，MT-Bench上的增长高达+0.22。这些结果表明，利用RM表示可以带来更高效、更稳健的WLHF。

[阅读原文](https://arxiv.org/abs/2606.10528)

---

