# 💡 今日研究速览 (Daily Summary)

# LLC和奖励设计的RL
当今的主导主题是大型语言模型强化学习的成熟，超越了简单的基于结果的奖励。大量论文解决了 **奖励规范和信用分配** 的关键挑战，特别是对于开放式和不可验证的领域。* * 预算级别奖励规范 **和**EvoRubric**等作品提出了动态、自我进化的标题生成来取代静态、手工制作的标准，从而消除了对昂贵的人工注释或单独奖励模型的需要。同样，**CorVer**和**通过跨模型Entropy** 的Label-Free RL开创了轻量级、无参考奖励信号，后者使用跨模型Entropy作为指令遵循的通用奖励。在训练算法方面，**HPO**（滞后政策优化）和**ESPO**（早期停止PPO）等创新直接解决了核心训练不稳定性--稀疏奖励和失败推出造成的计算浪费--而 * RL 2 ML **则提供了一系列可验证奖励的无偏梯度估计器。该领域对复杂任务的**流程级监督** 也激增，**DeepTools**、**GAPD**和**Beyond Trajectory Rewards**均提出细粒度、分步级信用分配来指导推理和工具使用。最后，**雷迪IPO**和**当RL抑制自己的词汇**强调了人们对一致性和多样性之间权衡的日益增长的认识，提出了新颖的数据构建和奖励塑造技术来恢复训练后模型中丢失的行为多样性。

# 潜在推理与高效计算
第二个重大突破是推动**高效、非自我回归的潜在推理**。该方向旨在将推理过程内化，从冗长、大量计算的思维链（CoT）转向更紧凑、高效的内部表示。**解锁LLM（RiM）的工作记忆**提出了一项根本性的转变，用单次前向处理的固定存储块取代自回归推理令牌，从而大幅降低推理成本。**将上下文蒸馏作为潜在内存管理**通过将上下文制定为模块化的门控LoRA适配器，有效地将记忆视为可学习的潜在资源，提供了一种补充方法。** DenseSteer**通过将内部表示引导为密集推理模式，提供了一种无需训练时间的推理方法。对于更复杂的规划，**计划**将CoT优化形式化为潜在世界模型上的强化学习，从而实现在这个压缩空间中的规划。**CosmicFish-HRM**模型引入了分层架构，可自适应地控制潜在推理的深度。该范式还解决了鲁棒性和安全性问题，**COLAGUARD**演示了如何将多步骤安全推理提炼成连续的潜在空间，以实现高效、高吞吐量的护栏。

# 自我改进和工具集成代理
主体研究格局是通过向**闭环、自我进化的系统**的转变来定义的，这些系统从自己的互动中学习。一个关键趋势是集成**流程监督RL**，以在粒度层面上细化代理行为。**GRASP**、**GrepSeek**和**PRO-CUA**各自提出了框架，其中代理可以在RL的分步奖励的指导下学习构建和编辑技能库、直接与数据库交互或执行计算机使用任务。这还辅之以对**自我验证和反思**的关注，如**自我训练验证（STV）**和**BenchTrace**所示，它们旨在通过增强代理人自己批评其行为的能力来改善培训时和测试时的自我改进。**乐于助人的诅咒**论文提供了一个至关重要的对比，表明RL（GRPO）实际上可以恢复针对分散注意力的指令的鲁棒性，从而证明了有益的对齐效果。此外，代理系统的边界正在扩展到新领域：**KairosAgent**将这种范式应用于时间序列预测，**学习设计技能**应用于量子逆设计，两者都使用RL从反馈中学习特定领域的政策。最后，**诚实撒谎**和**灾难性遗忘的机械起源** 等批判性分析提供了基础见解，诊断记忆虚构等陷阱，并解释了为什么RL比SFT更好地保留了学习的电路，从而指导更强大的代理架构的设计。

---

## 1. 长期LLM代理的元认知记忆策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ziyan Liu, Zhezheng Hao, Yeqiu Chen, Hong Wang, Jingren Hou, Ruiyi Ding, Yongkang Yang, Wence Ji, Wei Xia, Feng Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces MMPO, a meta-cognitive memory policy optimization method using belief entropy for fine-grained RL supervision in long-horizon LLM agents, strongly matching both RL for LLMs and self-improving agents.

**摘要**: arXiv：2605.30159v1宣布类型：新摘要：内存增强的LLM代理通过将交互轨迹递进总结到紧凑存储器中来解决复杂的长期任务。然而，现有的方法通常使用基于结果的强化学习来训练这些记忆策略，而无法定位中间记忆质量下降的地方。随着交互的展开，模糊的回归摘要逐渐丢弃与任务相关的信息并引入语义噪音。这加剧了信念偏差，模糊了代理对潜在任务状态的估计，并最终使长视野推理脱轨。因此，我们认为，记忆优化不仅应该关注实验室层面的成功，还应该关注中间摘要引发的信念的清晰度。为此，我们引入了Belief Entropy，这是一种自我监督代理，它可以探索模型在给定其当前记忆的情况下关于潜在任务状态的不确定性有多大。基于这个代理，我们提出了元认知内存策略优化（MMPO）。MMPO不是仅依赖于稀疏的基于结果的信号，而是通过明确惩罚导致高度认识不确定性的摘要来提供细粒度的、特定于内存的监督。实验表明，MMPO在各种长期任务上始终优于现有方法，即使扩展到1.75兆令牌上下文，也能保持97.1%的性能。

[阅读原文](https://arxiv.org/abs/2605.30159)

---

## 2. DeepTools：通过过程监督的强化学习在工具集成推理中扩展交织审议

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yang He, Xiao Ding, Bibo Cai, Yufei Zhang, Kai Xiong, Zhouhao Sun, Bing Qin, Ting Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DeepTool, a framework using process-supervised RL (GRPO) with an Action-Centric Process Reward to scale interleaved deliberation in tool-integrated reasoning, directly matching RL for LLMs and self-improving agents.

**摘要**: arXiv：2605.29568v1宣布类型：新摘要：工具集成推理（TLR）通过利用外部环境扩展LLM功能。然而，现有方法缺乏战略规划和自我纠正所需的顺序工具调用期间的深思熟虑。虽然RL缓解了这一点，但传统的工具集成推理方法受到基于结果的稀疏奖励的阻碍，无法监督中间推理步骤和工具调用。为了解决这个问题，我们提出了DeepTools，这是一个新颖的框架，可以在每个回合的思考、行动和观察的交叉过程中扩展刻意思维。在DeepTools中，我们首先引入了一个合成管道，该管道将扩展思维发展为交错轨迹，集成对抗性扰动以确保稳健性和自我纠正。其次，我们设计了基于GRPO的过程监督强化学习，它利用以对象为中心的过程奖励来加强中间交叉思维并在每个环节强制执行精确的工具调用。大量实验表明DeepTools实现了卓越的性能，在六个基准测试中显着提升了Qwen 2.5 - 7 B（例如，AIME 24：3.2% -> 40.4%和HMMT 25：0.0% -> 28.6%）。此外，代币成本效益分析证实了交叉思维的实用性，展示了DeepTools在性能和代币效率之间的最佳平衡。

[阅读原文](https://arxiv.org/abs/2605.29568)

---

## 3. 通过跨模型熵的无标签强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Matt Gorbett, Hossein Shirazi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Cross-Model Entropy (CME), a novel label-free reward signal for RL post-training of LLMs, enabling RL for open-ended instruction following without ground-truth verifiers or human labels.

**摘要**: arXiv：2605.29009v1宣布类型：新摘要：使用强化学习的后训练大型语言模型会受到奖励信号的干扰。现有的方法需要地面事实可验证的奖励，将训练限制在具有自动正确性检查的领域（例如，数学、代码执行），或者人类偏好标签，这些标签的收集成本很高，而且容易受到黑客攻击的奖励。最近的无标签方法用多数投票或模型自身输出的代币信息等自我参考信号取代了基本真相验证器，但有强化模型自身错误的风险。在这项工作中，我们提出了跨模型Entropy（CME），即在单独的验证者模型下生成器响应的平均log似然，作为RL后训练的无标签奖励信号。CME是连续的、无需培训的，其原则是验证者认为不足为奇的反应可能是正确的或高质量的。由于验证器独立于生成器，因此信号无法通过自相容性进行游戏。我们将CME集成到GRPO中，不对训练循环进行其他更改，将无标签RL扩展到开放式指令跟随--在这种机制中，自我参考信号不适用或不适合。在开放式指导下（UltraFeedback提示，在AlpacaEval 2.0上评估），CME奖励在四个模型家族（Qwen、Llama、Gemma、OLMo）和三个训练方案（预训练、SFT和策略调整）的LLM as-Judge进行的头对头比较中击败了未经训练的基础，平局调整后的获胜率范围为52.5%至71.4%。代码将在发布后发布。

[阅读原文](https://arxiv.org/abs/2605.29009)

---

## 4. 具有潜在推理的稳健高效护栏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Siddharth Sai, Xiaofei Wen, Muhao Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes COLAGUARD, a guardrail model that transfers multi-step safety reasoning into a continuous latent space for efficient inference, directly matching the latent reasoning criterion.

**摘要**: arXiv：2605.29068v1宣布类型：新摘要：随着大型语言模型（LLM）越来越多地部署在现实世界的应用程序中，维护大型语言模型（LLM）的安全性至关重要。现有的安全护栏通常依赖于单程分类，或者最近的提炼推理。基于推理的护栏的性能明显优于仅分类的基线，但它们会产生大量的查询延迟和令牌负担，这使得它们对于高吞吐量部署来说不切实际。为了应对这一挑战，我们提出了COLAGUARD，这是一种护栏模型，通过分阶段的培训课程将多步骤安全推理转移到连续的潜在空间中，从而在推理时实现直接的隐藏状态传播。COLAGUARD在跨越八个安全基准的十个即时和响应审核设置上进行了评估，将macro-F1比Llama Guard 3提高了8.24个百分点，并与我们在macroF 1中的显式推理基线GuardReasoner相匹配，同时实现了12.9倍的加速和22.4倍的代币使用减少。我们的结果表明，潜在推理为可部署护栏的显式理由生成提供了一种实用的替代方案，共同提高了安全稳健性和推理效率，而不是将它们视为相互竞争的目标。

[阅读原文](https://arxiv.org/abs/2605.29068)

---

## 5. 解锁大型语言模型的工作记忆以进行潜在推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lukas Aichberger, Sepp Hochreiter

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Reasoning in Memory (RiM), a latent reasoning method that replaces autoregressive generation of reasoning steps with fixed memory blocks processed in a single forward pass, enabling compute-efficient latent reasoning.

**摘要**: arXiv：2605.30343v1宣布类型：新摘要：为了提高大型语言模型的推理能力，测试时计算通常通过在最终答案之前生成中间令牌来扩展。然而，这将推理与自回归生成结合起来，从而将内部计算与外部沟通混为一谈。相比之下，人类认知可以使用工作记忆在内部保存和操纵信息，而无需外部化中间思想。根据这一原则，我们引入了记忆推理（RiM），这是一种潜在推理方法，用记忆块取代推理步骤的自回归生成。这些存储块是特殊标记的固定序列，可以释放大型语言模型的工作存储容量。由于它们是固定的而不是生成的，因此可以在单次向前传递中处理它们，从而实现计算机高效的潜在推理。为了操作这些记忆块，我们采用了两阶段课程。首先，我们通过预测每个记忆块后的显式推理步骤来建立它们。其次，我们放弃这种分步监督，并在每个内存块之后迭代地完善最终答案。我们对推理基准的实验表明，在不同家族和规模的语言模型中，RiM匹配或超过了现有的潜在推理方法，同时避免了思想的自回归生成。这些结果表明，大型语言模型可以被训练为使用工作记忆作为潜在推理的有效机制。

[阅读原文](https://arxiv.org/abs/2605.30343)

---

## 6. 当RL抑制自己的词汇时：恢复拼图到数学转换中的推理多样性

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Mayug Maniparambil, Arjun Karuvally, Terrence Sejnowski, Fergal Reid

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novelty bonus for RLVR to recover suppressed reasoning primitives, directly improving LLM reasoning via RL with a new reward design.

**摘要**: arXiv：2605.29190v1宣布类型：新摘要：使用可验证奖励的强化学习（WLVR）改进了LLM推理，但它跨领域传输的条件以及为什么这样做仍然没有得到充分的探索。我们在一个7 B模型中研究跨域迁移，该模型的SFT和RL训练后阶段仅使用约束满足谜题，训练后数据中没有数学问题。为了分析转移是如何出现的，我们引入了一个推理策略级框架，该框架将9级跨度分类器与主题提取相结合，使我们能够将思想链痕迹分割成原始主题，并跟踪它们在训练阶段和领域中的演变。我们发现谜题SFT引入了推理原始词汇，在Olympic Math-Hard上产生了+7$pp \textttt {pass@32}的收益。Vanilla GSPO然后将这些基元组合成更长的计算验证链，进一步增加了$+6$pp。然而，该RL阶段还抑制了\texttit {thomasize}和\texttit {backtrack}等探索性基元。为了解决这个问题，我们引入了一个新颖的奖金，奖励不同的正确推出，并使用参考模型下的困惑作为信号。这在RL期间恢复恢复基元，并相对于vanilla GSPO进一步添加$+7$pp \textttt {pass@32}。最后，端到端食谱将硬数学能力上限从OLMo 3 - 7 B-Direct-SFT基础的16.0美元提高到36.0美元，而不会在SFT或RL阶段添加任何数学问题。

[阅读原文](https://arxiv.org/abs/2605.29190)

---

## 7. 来自世界反馈的政策上自我蒸馏的预测定律

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tommy He, Jerome Sieber, Matteo Saponati

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a predictive linear law for on-policy self-distillation from world feedback, offering a principled way to incorporate rich feedback into RL post-training pipelines.

**摘要**: arXiv：2605.30070v1宣布类型：新摘要：超越简单的纯量奖励转向更丰富的世界反馈是实现更具可扩展性的RL后训练的自然途径。按政策自蒸馏（OPSD）是一种很有前途的最近方法，它使用任意反馈作为学习信号，但与GRPO等既定方法相比，其可靠性仍不清楚。我们发现，OPSD中最初的学生-自学表现差距和最终的表现改进之间存在惊人一致的线性相关性。这种关系适用于上下文类型和模型系列，为在不运行完整训练过程的情况下预测OPSD配置的结果提供了强大的预测法则。有趣的是，我们表明这种线性可预测性随着模型规模而成立，这为具有更强上下文学习能力的更大模型上的新经验缩放定律提供了潜在的基础。本质上，我们的研究结果表明，可以在训练前预测和调整OPSD表现，从而提供了一种原则性的方法来将世界反馈作为训练后管道的一流组成部分。

[阅读原文](https://arxiv.org/abs/2605.30070)

---

## 8. GDSD：强化学习作为扩散语言模型的引导降噪器自蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xiaohang Tang, Keyue Jiang, Che Liu, Qifang Zhao, Xiaoxiao Xu, Sangwoong Yoon, Ilija Bogunovic

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GDSD, a novel RL method for diffusion LLMs that uses advantage-guided self-distillation to bypass ELBO biases, directly improving denoiser policy.

**摘要**: arXiv：2605.29398v1宣布类型：新摘要：强化学习（RL）可用于改进扩散大型语言模型（dLLM）的策略（降噪器），同时受到策略可能性的棘手性的阻碍。一个占主导地位且有效的方法家族用其证据下限（ELBO）取代标准RL中的可能性，该下限是根据随机掩蔽序列估计的。尽管与预训练很好地一致，但这些方法通过训练引入了偏差--通过使用ELBO作为似然替代物来推断不匹配，这可能会降低性能。在这项工作中，我们提出了引导去噪器自蒸馏（GDSD）来直接从引导自教师中提取dLLM的去噪器，该教师源自反向KL正规化RL的封闭形式最优。GDSD通过无规范化目标将dLLM的降噪器日志与教师的日志进行匹配，这将RL简化为可能无自我蒸馏，从而绕过TIM偏见。最近的基于ELBO的方法作为应用不同蒸馏分歧的例子出现，但具有GDSD避免的可诊断病理学。在LLaDA-8B和Dream-7 B的规划、数学和编码基准方面，GDSD始终优于之前最先进的基于ELBO的方法，具有更稳定的训练奖励动态，实现了高达+19.6美元的测试准确性改进。这些结果表明，在不依赖ELBO似然替代品的情况下，直接降噪剂自蒸馏可以为dLLM提供更稳定和有效的RL程序。代码可在https://github.com/GaryBall/GDSD上获取。

[阅读原文](https://arxiv.org/abs/2605.29398)

---

## 9. GRASP：用于自我改进LLM代理的门控回归感知技能提议器

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Johannes Moll, Jean-Philippe Corbeil, Jiazhen Pan, Martin Hadamitzky, Daniel Rueckert, Lisa Adams, Keno Bressem

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving LLM agent framework (GRASP) that treats improvement as gated edits to a skill library with a hard regression budget, showing strong gains.

**摘要**: arXiv：2605.29668v1宣布类型：新摘要：在结构化环境中行事的LLM代理以操作方式而不是对话方式失败，可靠性取决于环境的程序知识。先前的自我改进方法积累自然语言指导，而不检查每个新项目是否保留了之前正确的行为，因此修复一个轨迹的注释可能会悄悄地倒退另一个轨迹。我们引入了GRASP（门控回归感知技能提议者），它将代理改进视为对有界技能库的一系列编辑，只有当每个候选人在硬回归预算下对平衡的坚持探测产生净改进时，才会录取它。我们在两个基于FHIR的临床基准上评估了五种基本型号（gtt-oss-120 b、DeepSeek V4 Flash、Gemini 3.1 Flash Lite、GPT-4.1、GPT-5.4）的GRASP。在MedAgentBench上，GRASP将gtt-oss-120 b从40.6%提高至88.8%，比五个自我改进基线中最强的基线高出21.0个百分点，并将其他所有基本模型提高了17.2至40.3个百分点。消融将收益归因于比较提案生成、接受门和硬回归预算，而不是技能写作本身，而没有验证的写作并不比不使用技能好。该机制扩展到临床领域之外，改进了四种非临床环境中三种的药物，并仅在动作空间开放的情况下保持平坦。冻结的库在模型之间转移，来自更强模型的技能可以改善较弱的执行者，超出他们自己学到的知识，而反之则不然，这种不对称性是任何无门控基线都无法复制的。

[阅读原文](https://arxiv.org/abs/2605.29668)

---

## 10. EvoRubric：面向开放一代的自我进化的Rubric驱动RL

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xin Guan, Xiaomeng Hu, Shen Huang, Zhenyi Wang, Bo Zhang, Zijian Li, Pengjun Xie, Bo Liu, Jiuxin Cao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving RL framework for open-ended generation that dynamically generates rubrics via a single policy, eliminating static criteria and external models.

**摘要**: arXiv：2605.29847v1宣布类型：新摘要：强化学习（RL）在可验证领域显着进步了大型语言模型（LLM），但由于缺乏明确的回报，为开放式生成调整模型仍然具有巨大的挑战性。当前基于主题的RL方法通过采用显式标准来缓解这一问题;然而，它们严重依赖静态、人类注释的主题，这不可避免地会导致政策滞后，或者用于动态更新的昂贵外部专有模型。在本文中，我们提出了EvoRubric，这是一种新型的单策略协同进化RL框架，它消除了对静态标准和外部Rubric生成器的依赖。通过在单个参数化策略下统一响应生成和rubric生成，EvoRubric在Reasoner和Rubric Generator之间动态交替。为了防止奖励黑客攻击并确保生成信号的可靠性，我们引入了一个多层验证管道，该管道具有元验证器、零方差修剪和留一出对等共识机制。经过验证的标准动态存档到内存池中，产生密集的多目标奖励，以持续协同优化两个角色。跨越医学、写作和科学领域的广泛实验表明，EvoRubric始终优于传统的静态和外部LLM驱动的对齐方法。值得注意的是，我们的框架与人类专家先验兼容。当使用专家注释的标题初始化时，EvoRubric可以进一步揭示新颖的、区分性的维度，比仅依赖静态专家注释获得更好的性能。

[阅读原文](https://arxiv.org/abs/2605.29847)

---

## 11. 培训和测试时自我改进的自我训练验证

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chen Henry Wu, Aditi Raghunathan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes self-trained verification (STV) to improve verifier quality, enabling both test-time verification-refinement loops and verifier-in-the-loop RL training for LLM reasoning self-improvement.

**摘要**: arXiv：2605.30290v1宣布类型：新摘要：大规模自我改进一直是推理模型的长期目标，有两个自然的地方可以做到这一点：在测试时，通过验证-细化（V-R）循环;在训练时，通过自我训练方法。两者都由同一个瓶颈控制：验证器。当验证者分数膨胀而准确性停滞时，以及反馈过于笼统而无法采取行动时，V-R循环就会停滞;当不良的自我生成数据被添加到训练中时，自我训练也会同样失败。更好的验证将解锁两者，但我们想要训练的能力，即，捕捉自发错误，缺乏训练信号。为了应对这一挑战，我们提出了自训练验证（STV）。我们的关键观察是，虽然模型不能单独捕获这些错误，但当显示参考解决方案时，它可以。我们把这种不对称变成一个监督目标，并训练验证者模仿一个更知情的版本。在测试时，STV大大改善了硬问题上的V-R循环，而替代方案（例如，SFT，验证者分数上的RL，甚至元验证者）都不会。STV将困难数学的准确性大致提高了一倍，并将科学推理任务的准确性提高了14倍（1.5%至21%）。在训练时，我们还在V-R循环内使用RL和STV验证器的反馈来训练生成器-我们称之为验证器在环训练（ViL）的过程。从RL收敛生成器开始，ViL在pass@1中进一步提高了33%。更值得注意的是，在测试时没有验证器的情况下，生成器的独立pass@1相对于标准RL收敛处攀升了30%。因此，推理困难问题的下一个前沿可能在于我们如何进行验证和验证训练。

[阅读原文](https://arxiv.org/abs/2605.30290)

---

## 12. 超越数学和代码的可验证奖励：基于数据库的轻量级事实问题回答过程监督

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shicheng Fan, Haochang Hao, Dehai Min, Weihao Liu, Philip S. Yu, Lu Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CorVer, a lightweight corpus-grounded process reward for RL that replaces expensive neural verifiers, directly addressing RL reward design for factual QA.

**摘要**: arXiv：2605.29648v1宣布类型：新摘要：应用强化学习来提高知识密集型问答中的事实准确性面临着奖励设计困境。响应级别奖励仅提供粗略的监督，并且无法区分推理轨迹内的正确陈述和不正确陈述。句子级替代方案提供更细粒度的反馈，但通常依赖于NLI验证器、LLM法官或知识验证管道，这些管道在RL规模上部署成本高昂，并且对于稀有实体事实通常不可靠，其中准确的奖励信号尤其重要。我们提出CorVer（Corpus Verify），这是一种轻量级的、插件就绪的流程奖励，用从维基百科同现统计数据中派生的基于群体的信号取代神经验证器。CorVer分配业务级别的信用，并通过简单的对齐将其映射到代币级别的优势，每个句子只需要一个0.5B提取器和一个语料库查找。CorVer在涵盖六个经过描述调整的模型（3B至14 B）和五个QA基准的30个（模型、基准）单元中，每个单元的原始基线都有所改善，TriviaQA平均收益为+4.1 pp。在可行配置下，它在20个细胞中的18个细胞中的表现还优于四个神经验证器基线，同时训练速度提高了4.8至8.4倍。

[阅读原文](https://arxiv.org/abs/2605.29648)

---

## 13. Hista和Numca：有效估计LLM强化学习的状态值

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zizhe Chen, Jiqian Dong, Yizhou Tian, Garry Yang, Yongqiang Chen, Zhitang Chen, James Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Numca and Hista, novel methods for accurate state value estimation in RL for LLMs, directly improving RL training for LLMs.

**摘要**: arXiv：2605.29782v1宣布类型：新摘要：强化学习（RL）通过通过奖励信号直接优化模型行为来细化大型语言模型（LLM）。虽然准确的状态值估计对于经典RL的稳定训练至关重要，但它仍然是LLM后训练中未充分探索的挑战。在这项工作中，我们引入了状态值估计基准（SVEB）来评估现有RL框架内的状态估计，并表明PPO等标准方法的批评者会陷入粗略的群体平均基线。为了解决这个问题，我们提出了两种技术：Numca，它利用数字跨度作为状态值估计的可分级里程碑，和Hista，一个使用LLM的隐藏状态作为加权平均不相交展开及其返回的表示的框架。大量实验表明，这两种方法都能产生更准确的状态值估计，并增强不同RL算法和模型大小的训练性能，而不会产生显着的计算负担。

[阅读原文](https://arxiv.org/abs/2605.29782)

---

## 14. 开放式后培训的预算级奖励规范

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zijun Weng, Xiaohui Hu, Shuangyong Song, Yongxiang Li, Kaidong Yu, Xuanjing Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a prompt-level reward specification framework that constructs rubrics and checkers offline for open-ended post-training, enabling RL without human annotations or a trained reward model.

**摘要**: arXiv：2605.29275v1宣布类型：新摘要：开放式的培训后受益于奖励，这些奖励明确了预算特定的成功条件，而不是仅依赖事后的纯量分数。在指令遵循、写作和决策支持任务中，响应质量取决于当地要求、整体偏好和明确的约束，但现有的奖励方法通常不包含这些标准或仅涵盖有限可验证的案例。我们提出了一个独立的奖励规范框架，将奖励规范和奖励计算分开。只给出提示，我们的框架构造可重用的任务自适应规则和可执行的硬约束检查器离线，使奖励标准明确的训练和可重用的跨推出之前。在评分时，工件锚定的量规和代码分数与剩余整体质量的独立全局分数相结合，产生超过需求满足、整体质量和确定性约束的归一化混合奖励。该框架不需要人类偏好注释、参考答案或单独训练的奖励模型。实验表明，由此产生的奖励改进了离线RM风格的响应排名，并支持跨多个开放式基准的在线强化学习。消融进一步表明，标题、全局评分和可执行验证提供了补充监督。

[阅读原文](https://arxiv.org/abs/2605.29275)

---

## 15. HPO：稀疏奖励制度下稳定高效培训的滞后政策优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mohamed Sana, Nicola Piovesan, Antonio De Domenico, Fadhel Ayed, Haozhe Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HPO, a novel RL method for LLMs that modifies GRPO to handle sparse verifiable rewards, directly addressing a core RL-for-LLMs training challenge.

**摘要**: arXiv：2605.30201v1宣布类型：新摘要：我们在稀疏可验证奖励的背景下研究了GRPO式强化学习的一种狭窄但常见的失败模式：早期更新包含的具有负优势的响应多于具有正优势的响应，而响应级别长度标准化将更新的幅度与输出的长度联系起来。我们提出了滞后政策优化（HPO），这是GRPO的最小修改，可以减少负优势更新的权重，并用平均长度规范化取代按响应长度规范化。我们进一步介绍了自适应HPO（A-HPO），它设置的滞后权重的基础上批量级的符号统计，从而消除了调整一个固定的滞后权重的需要。在我们的Telecommunication和Countdown实验中，与GRPO相比，A-HPO提高了每次更新的奖励，在早期稀疏奖励制度中获得的收益最大。在Telecommunication上，A-HPO实现了0.84的最终奖励，比SAPO高5%，比GSPO高11%，比GRPO高15%，同时保持了相当的响应长度。在倒计时中，A-HPO在1.5B-7 B型号的初始和最困难的配置中实现了最大的收益。对滞后体重的消融研究表明，与仅积极或完全对称的更新相比，A-HPO的收益来自于更好地平衡了积极和消极优势的贡献。

[阅读原文](https://arxiv.org/abs/2605.30201)

---

## 16. PRO-CUA：计算机使用代理的流程奖励优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yifei He, Rui Yang, Hao Bai, Tong Zhang, Han Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a process-reward optimization framework (PRO-CUA) for training computer use agents with iterative step-level RL, decoupling interaction from policy optimization.

**摘要**: arXiv：2605.29119v1宣布类型：新摘要：计算机使用代理（CUA）在自动化复杂的数字工作流程方面表现出了巨大的潜力，但他们的培训仍然受到昂贵的实时环境交互和有限的高质量监督的限制。现有的过滤行为克隆管道存在模仿瓶颈，包括专家演示的分布转移和缺乏负面学习信号。与此同时，标准的强制级强化学习在长期GUI交互中面临着奖励稀疏、信用分配模糊和基础设施成本高的问题。在这项工作中，我们提出了PRO-CUA，这是一个过程奖励优化框架，用于通过迭代步骤级强化学习来训练CUA。PRO-CUA从策略优化中实现了策略上的环境交互：当前策略通过实时部署收集状态，为每个状态生成不同的候选操作，从过程奖励模型（PRM）接收步骤级反馈，并通过组相对优势进行优化。这种设计能够实现密集和灵活的信用分配，而不依赖于黄金答案或离线专家轨迹，同时通过对代理自己的执行状态进行训练来减少分布偏移。实时网络基准测试实验证明了PRO-CUA的有效性和PRM引导的分步培训的可靠性。

[阅读原文](https://arxiv.org/abs/2605.29119)

---

## 17. 通过Amap中隐式推理的生成性时空意图序列推荐

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sicong Wang, Ruiting Dong, Yue Liu, Bowen Zheng, Jun Meng, Jie Li, Shuaijun Guo, Yu Gu, Fanyi Di, Xin Li

**机构**: Alibaba Group

**💡 亮点 (Highlight)**: Proposes a generative framework with Progressive Implicit CoT Distillation (latent reasoning) and Spatiotemporal Counterfactual DPO (RL alignment), directly matching both Latent CoT/Reasoning and RL for LLMs criteria.

**摘要**: arXiv：2605.2888v1宣布类型：新摘要：现实世界的用户行为很少由孤立的动作组成;相反，它经常形成受时空依赖关系支配的意图流。为了提供集成的服务建议，我们专注于生成性时空意图序列推荐（GSISR）的任务，该任务旨在生成在复杂时空上下文中逻辑一致且物理可执行的意图序列。虽然LLM为GSSR提供了强大的推理潜力，但直接工业部署受到高推理延迟和上下文不匹配或物理上不可行的计划的限制。为了应对这些挑战，我们提出了一个生成式框架GPlan，它通过两个组件将LLM推理内化为轻量级模型。首先，为了能够在严格的延迟限制下进行推理，我们引入了渐进式隐式CoT蒸馏，它将显式推理过程压缩到保留的潜在令牌中，允许小模型继承复杂的规划逻辑，而无需生成长推理文本。其次，为了解决常识与现实世界约束之间的脱节问题，我们设计了时空反事实DPO。通过将模型与反事实上下文-计划对对齐，我们提高了对时空上下文的敏感性并减少了上下文不匹配的计划。离线实验和在线A/B测试表明，我们的方法可以提高序列一致性和上下文响应性。我们的实现和匿名GSSR数据集可在https://github.com/alibaba/GPlan上获取。

[阅读原文](https://arxiv.org/abs/2605.28888)

---

## 18. SAAS：用于减少搜索过度的自感知强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yunbo Tang, Chengyi Yang, Shiyu Liu, Zhishang Xiang, Zerui Chen, Qinggang Zhang, Jinsong Su

**机构**: Xiamen University

**💡 亮点 (Highlight)**: Proposes a novel RL framework (SAAS) with search boundary modeling and boundary-aware rewards to mitigate over-search in agentic systems, directly matching RL for LLMs and agent self-improvement criteria.

**摘要**: arXiv：2605.29796v1宣布类型：新摘要：统计搜索使LLM能够通过迭代推理和外部搜索来解决复杂的多跳问题。尽管有效，但这些系统在实践中往往受到严重限制：代理无法识别自己的知识边界，在内部知识足够时盲目触发搜索，即使收集到足够的证据也无法终止搜索。缺乏自我意识会导致严重的\textBF{over-search}，导致大量推理延迟和高昂的计算成本。为此，我们提出了SAAS，这是一种新颖的RL框架，旨在培养动态自我意识，在不影响准确性的情况下精确调节搜索行为。SAAS引入了三个关键组件：（i）搜索边界建模机制，该机制通过对比禁用搜索和启用搜索的推出来识别不断变化的政策下的搜索边界;（ii）边界感知奖励模块，该模块将这种边界感知转化为子公司级处罚，抑制不必要和冗余的搜索;和（iii）逐阶段优化策略，该策略利用顺序课程来优先考虑推理而不是搜索正规化，从而避免奖励黑客攻击。大量实验表明，SAAS大大减少了过度搜索，同时保持了准确性。我们的代码在https://github.com/XMUDeepLIT/SAAS上匿名发布。

[阅读原文](https://arxiv.org/abs/2605.29796)

---

## 19. OISD：语言模型的政策内部自我提炼

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinyu Liu, Darryl Cherian Jacob, Yang Zhou, Jindong Wang, Pan He

**机构**: THE MALT LAB (likely academic, e.g., University of Maryland)

**💡 亮点 (Highlight)**: Proposes OISD, a novel on-policy internal self-distillation framework that uses RL (GRPO) to transfer reasoning signals from final to intermediate layers, directly improving LLM reasoning via a new training recipe.

**摘要**: arXiv：2605.29089v1宣布类型：新摘要：最近的强化学习（RL）训练后方法主要使用稀疏结果级别奖励来优化最终输出策略，同时在很大程度上忽略了以中间表示编码的预测信号。在本文中，我们引入了一种称为政策上内部自我蒸馏的新范式，并提出了OISD框架，该框架通过将政策上的预测信号从最终层转移到中间表示来改进推理。在推出和组相对政策优化（GRPO）优化期间，最终层既是政策，又是选定中间层的独立内部教师，通过两个补充机制引导这些中间层与之保持一致：logit对齐，转移高级推理行为（如何思考），以及注意力对齐，强制执行一致的注意力模式（在哪里查看）从最终层到选定的中间层，两者都不需要外部特权信息。我们的OISD与GRPO一起使用签名的Jensen-Shannon对齐来提取信息性的中间表示，同时在统一的代理政策下保持政策一致性。实验结果证明了OISD的有效性，在四个数学推理任务中比强推理RL基线有了实质性且一致的改进。该代码将在https://github.com/THE-MALT-LAB/OISD上发布

[阅读原文](https://arxiv.org/abs/2605.29089)

---

## 20. 过得怎么样？语言模型中的强化学习招募功能福利轴

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Andy Q Han, David J. Chalmers, Pavel Izmailov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows RL training recruits a pre-existing welfare representation axis in LLMs, offering novel insight into RL's effect on internal representations.

**摘要**: arXiv：2605.30232v1宣布类型：新摘要：强化学习如何塑造语言模型的内部表示？我们提供的证据表明RL招募了一种预先存在的功能福利代表：对系统相对于其目标表现好坏的估计。我们在一个新颖的、语义中立的迷宫环境中训练几种语言模型。然后，我们提取奖励和惩罚轨迹的概念载体，并在与迷宫环境无关的环境中评估这些载体。惩罚载体的行为就像负福利的代表：它促进失败和不可能的标志，它与负性情绪概念保持一致，它消极跟踪目标实现，并随之引导会导致负性的自我报告、病态的回溯、拒绝和不确定性。正奖励载体的行为就像镜像，两者几乎是反平行的。当控制磁贴到奖励映射、规模、指令调整、RL训练算法、模型家族和LoRA与完全微调时，这些效果是稳健的，并且当我们用监督式微调取代RL时，这些效果在很大程度上持续存在。重要的是，这些载体在接受迷宫训练之前在模型中是有效的。结合这种影响也出现在仅训练前模型中的观察，我们因此认为，这种功能福利轴在训练后预先存在：它是由训练后招募而不是创建的。虽然我们没有声称任何福利体验，但轴证明了最低奖励信号可以通过招募预先存在的类似福利的表示来广泛影响模型行为，并对可解释性、训练后动态和对齐产生影响。

[阅读原文](https://arxiv.org/abs/2605.30232)

---

## 21. 计划目标：通过强化规划进行思想链优化的潜在世界模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Dong Liu, Yanxuan Yu, Ying Nian Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formalizes reasoning chain optimization as RL over a latent world model, enabling planning in latent space for CoT editing.

**摘要**: arXiv：2605.28842v1宣布类型：新摘要：大型语言模型（LLM）在各种NLP任务中的成功提高了推理链优化的重要性，作为使模型行为与任务目标相一致的关键步骤。现有的推理链调整方法通常依赖于黑匣子启发式或无梯度搜索，这些方法缺乏可解释性、概括性和样本效率。在这项工作中，我们介绍了\textbf{规划作为规划}，一个新的框架，正式推理链优化作为一个顺序的决策过程中的潜在语义空间。我们将LLM建模为部分可观察的环境，并学习一个潜在的世界模型，该模型模拟推理链编辑对下游输出的影响。构造一个保持邻近性的嵌入空间来编码推理链响应动态，从而通过梯度下降或强化学习进行规划。我们的方法支持多尺度抽象，允许推理链编辑令牌，段和指令级集成到一个统一的计划。通过对语言理解和生成任务的广泛实验，我们证明，计划策略在效率、稳健性和概括性方面优于最先进的推理链调优基线，同时通过其结构化规划轨迹提供可解释性。我们的代码可在https://github.com/FastLM/Thoughts-as-Planning上获取。

[阅读原文](https://arxiv.org/abs/2605.28842)

---

## 22. KairosAgent：使用融合语义推理的统计时间序列预测

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kun Feng, Ziwei Shan, Yuchen Fang, Yiyang Tan, Sihan Lu, Shuqi Gu, Lintao Ma, Xingyu Lu, Kan Ren

**机构**: Foundation Model Research

**💡 亮点 (Highlight)**: Proposes a novel agentic framework for time series forecasting that uses RL from forecasting feedback with multi-turn refinement and turn-level credit assignment, directly matching the RL for LLMs and self-improving agent criteria.

**摘要**: arXiv：2605.30002v1宣布类型：新摘要：跨域多模式时间序列预测是一项具有挑战性的任务，需要模型集成精确的数值理解、跨域语义理解和有效的多模式融合。现有的方法要么从头开始构建时间序列基础模型（TSFM），要么利用预先训练的大型语言模型（LLM）。然而，TSFM经常忽视语义理解，缺乏执行面向未来的语义推理的能力，而LLM则难以理解数字理解和准确的量化预测。为了克服这些限制，我们提出了KairosAgent，这是一种用于多模式时间序列预测的新型代理框架，包括基于LLM的推理器和基于TSFM的预测器。KairosAgent通过动态调用分析工具来统一文本推理和数字预测，以增强LLM的数字理解和语义推理能力。推理结果随后被融合到TSFM管道中，从而实现更准确和可靠的未来预测。为了进一步改进推理，我们策划了一个大规模的高质量轨迹库，以及来自预测范式的强化学习，具有多回合细化和回合级信用分配。实验表明，KairosAgent在最大限度地利用预训练的LLM和TSFM的利用率的同时，实现了高效且可解释的时间序列代理的有前途的方向。项目页面位于https://foundation-model-research.github.io/KairosAgent。

[阅读原文](https://arxiv.org/abs/2605.30002)

---

## 23. 稳定层：使用LMA评分强化学习微调图像层分解模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ciara Rowles, Reshinth Adithyan, Nikhil Pinnaparaju, Vikram Voleti, Mark Boss

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (Flow-GRPO with VLM reward) for fine-tuning image layer decomposition, directly matching the RL for LLMs criterion with a new reward design and scalable RL training recipe.

**摘要**: arXiv：2605.30257v1公告类型：新摘要：我们提出了Stable-Layers，这是一种强化学习框架，通过仅使用视觉语言模型（VLM）的反馈来微调预训练的层分解模型，从而消除了对成对监督的需要。从Qwen-Image-Layered开始，我们将Flow-GRPO应用于LoRA适应，对每个图像进行多个候选分解，使用VLM对其进行评分，并从组相对优势中优化策略。关键的挑战在于设计可靠的奖励信号：对样本进行隔离评分的VLM往往会将他们的判断压缩到一个狭窄的范围内，使GRPO几乎没有可供学习的组内差异。我们通过两阶段评估管道来解决这个问题，该管道将五个以编辑为中心的标准的结构化每样本评分与基于网格的校准步骤配对，其中VLM并排重新评分所有候选人。与基本模型相比，Stable-Layers在Crello数据集中产生具有更强的层分离、更少的空白层或大量伪影层以及更低的每层重建误差的分解。

[阅读原文](https://arxiv.org/abs/2605.30257)

---

## 24. 模特什么时候应该改变想法？大型语言模型中的上下文信念管理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haoming Xu, Weihong Xu, Zongrui Li, Mengru Wang, Yunzhi Yao, Chiyu Wu, Jin Shang, Yu Gong, Shumin Deng

**机构**: Zhejiang University

**💡 亮点 (Highlight)**: Proposes RL with belief-state rewards to improve contextual belief management in LLMs, directly matching RL for LLMs criterion.

**摘要**: arXiv：2605.30219v1宣布类型：新摘要：长期交互需要语言模型来管理积累的信息：何时更新其状态、何时保留其状态以及忽略什么。我们将这个挑战研究为\textBF{上下文信念管理（MBE）}：保持与正式证据一致的预测信念状态，同时隔离与任务无关的噪音。为了使CBN可测量，我们引入了BeliefTrack，这是一个跨越规则发现和电路诊断的封闭世界基准，其中有限的信念空间和符号验证器能够实现精确的回合级评估。BeliefTrack诊断了三种失败：停留失败、更新失败和隔离失败。在多个LLM中，普通模型表现出严重的CBP失败，而明确的信念跟踪提示提供的收益有限。相比之下，具有信念状态奖励的强化学习平均将失败率降低了70.9%。进一步的调查揭示了这些失败背后的潜在信念状态动态，并且代表级引导将两项任务的失败率降低了46.1%\脚注{代码即将在https://github.com/zjunlp/CBM上发布。

[阅读原文](https://arxiv.org/abs/2605.30219)

---

## 25. 用进化策略克服LLM微调中的遗忘

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kajetan Schweighofer, Conor F. Hayes, Roberto Dailey, Risto Miikkulainen, Xin Qiu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Anchored Weight Decay to mitigate forgetting in ES-based LLM fine-tuning, a novel RL alternative for LLM alignment.

**摘要**: arXiv：2605.30148v1宣布类型：新摘要：进化策略（ES）最近成为大型语言模型（LLM）微调的强化学习（RL）的竞争替代方案，通过简单性、可扩展性和纯推理训练提供优势。然而，最近的研究表明，ES对新任务的微调可能会导致对先前任务的遗忘。首先，本文表明，先验任务遗忘（1）更好地描述为性能漂移而不是不可逆转的遗忘，先验任务性能通常在ES训练期间恢复;（2）不是ES的一种特定失败模式，但也可能出现使用RL方法进行微调。其次，它分析了这种漂移何时以及为何出现，强调了其对ES训练动态的依赖，特别是体重空间弱约束方向上的随机行走行为。第三，基于这些见解，它引入了锚定权重衰减（AWD）作为一种参数空间正规化技术，该技术将优化限制在初始模型参数上。AWD有效地稳定了先前任务的性能，同时保留了目标任务的性能，以低得多的计算成本实现了与大ES群体规模相当的好处。因此，与之前的观点相反，该论文表明ES下的先前任务遗忘在很大程度上是可以避免的，从而将ES定位为LLM中持续学习的一种有希望的方法。

[阅读原文](https://arxiv.org/abs/2605.30148)

---

## 26. 训练代理人，而不是专家：学习为多轮视觉推理而对异类专家进行分类

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yaowu Fan, Tao Han, Dazhao Du, Andy J. Ma, Jia Wan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a trainable visual agent that uses on-policy RL to learn a policy for harnessing heterogeneous visual experts, with a dynamic visual memory archiving to handle token overhead, directly matching the RL for LLMs and self-evolving agent criteria.

**摘要**: arXiv：2605.29894v1宣布类型：新摘要：计算机视觉领域的最新进展为检测、分割、计数和其他视觉任务产生了广泛的强大专业模型。然而，这些模型通常针对孤立的任务公式进行了优化，因此很难直接支持通用视觉智能，特别是当任务需要复杂的语言理解和密集的小对象感知时。在本文中，我们提出了Visitual，这是一种可训练的视觉代理，它将高级感知、推理和决策与低级任务执行分开。Visspel不是训练模型来解决特定的视觉任务，而是学会利用一组精心设计的异类视觉专家。该范式保留了代理的一般智能，同时在具体视觉任务中充分利用专门视觉模型的精确优势。仅通过轻量级培训，Visitual就可以学习可推广的视觉专家利用政策，并可以通过与视觉专家模型的多轮交互来解决各种复杂条件下的常见基本视觉任务。为了在实时环境中实现高效的按策略强化学习训练，我们引入了动态视觉记忆存档，这可以减轻与视觉专家模型的多轮交互引起的快速积累的视觉令牌负担。对涵盖推理分割、广义引用分割、密集小对象检测和引用计数的四个代表性基准的实验表明，Visitual的表现大大优于现有的通用模型，并与特定任务的模型相比实现了有竞争力或更优越的性能。

[阅读原文](https://arxiv.org/abs/2605.29894)

---

## 27. LaRA：RL训练后检测数据污染的分层表示分析

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Minju Gwak, Minseo Kwak, Dongseok Lee, Guijin Son, Alan Ritter, Jaehyung Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel layer-wise representation analysis framework (LaRA) for detecting data contamination specifically in RL post-trained LLMs, addressing a critical gap in RL for LLM evaluation.

**摘要**: arXiv：2605.29888v1宣布类型：新摘要：强化学习（RL）后训练已被证明可以改善大型语言模型（LLM）中的推理。然而，对RL后训练中的数据污染问题的探索很少，这可能会损害训练过程本身的概括性和评估可靠性。现有的检测方法主要依赖于输出级信号，例如可能性或熵，这对于RL训练的模型来说变得不可靠，因为RL通过假设级奖励而不是代币可能性来塑造行为。我们提出了LaRA，这是一个分层表示分析框架，用于检测RL后训练LLM中的污染。LaRA引入了三个补充指标，测量受控扰动下的扰动敏感性、方向崩溃和局部表示刚性。我们发现污染会在层间产生渐进的几何偏差，包括放大的扰动敏感性、更强的方向塌陷和增强的局部刚性。根据我们的研究结果，我们还开发了一种污染检测协议，该协议汇总跨层和指标的代表级别偏差。RL训练推理模型的实验表明，我们的协议优于现有的污染检测输出级基线。

[阅读原文](https://arxiv.org/abs/2605.29888)

---

## 28. 在不失去一致性的情况下恢复多样性：培训后的LLM的DPO食谱

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Vinay Samuel, Yapei Chang, Mohit Iyyer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes REDIPO, a novel DPO data-construction pipeline for recovering diversity in post-trained LLMs while preserving alignment, directly contributing to RL for LLMs via preference data design.

**摘要**: arXiv：2605.30021v1宣布类型：新摘要：许多开放式指令都有多个有效答案，用户可以从中受益，但后训练通常会将LLM的输出空间缩小到一小群典型响应。我们引入了雷迪IPO，这是一种离线DPO数据构建管道，用于恢复不同的有效回答模式，同时保留指令模型的对齐优势。对于每个提示，雷迪IPO对基础模型和指令模型的响应进行抽样，用指令模型重写基础模型响应，过滤安全性和描述跟踪质量的候选人，并构建偏好对，在具有相似描述跟踪奖励的候选人中支持略有不同的响应。在Qwen 3 - 4 B、OLMo-3- 7 B和LLaMA-3.1-8B中，与指示检查点相比，雷迪IPO将NoveltyBench_k提高了134%、33%和44%，而DivPO在相同模型上将多样性改变了0%、-6%和-4%。这些收益在很大程度上维持了MTBench、IFEval和Arena-Hard的性能，并降低了直接类别HarmBench攻击的成功率。消融表明，边缘多样性对选择和碱基响应重写推动了多样性收益，而过滤和质量有界配对有助于保持一致。总体而言，我们的结果表明，可以通过精心构建的偏好数据重新引入基础模型世代的不同有效答案，同时保留训练后的对齐优势。我们在https://github.com/vsamuel2003/RiDiPO上发布我们的代码和数据。

[阅读原文](https://arxiv.org/abs/2605.30021)

---

## 29. DenseSteer：引导小型语言模型走向密集数学推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yang Ouyang, Shuhang Lin, Jung-Eun Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DenseSteer, a training-free inference-time steering framework that modulates internal representations toward dense reasoning patterns, directly addressing latent reasoning by moving away from verbose CoT.

**摘要**: arXiv：2605.29247v1宣布类型：新摘要：大型语言模型（LLM）表现出强大的思想链（CoT）推理能力，而较小的模型（<= 3B参数）在多步推理任务中表现明显较差。基于对Qwen-2.5模型家族对数学推理基准的实证分析，我们发现更熟练的推理与更少的推理步骤但每步信息密度更高相关，我们将其称为密集推理。受这一观察结果的启发，我们提出了DenseSteer，这是一个免训练的推理时引导框架，通过将内部表示调整为密集推理模式来增强小模型推理。实验表明，我们的方法在不增加标记级负对似然性的情况下产生一致的准确性改进，突出了密集推理作为数学问题解决的有效结构性方法。

[阅读原文](https://arxiv.org/abs/2605.29247)

---

## 30. 上下文蒸馏作为潜在内存管理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ziyang Zheng, Zeju Li, Xiangyu Wen, Jianyuan Zhong, Junhua Huang, Lei Chen, Mingxuan Yuan, Qiang Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Formulates context distillation as latent memory management with modular LoRA adapters and a Self-Gating mechanism, directly relevant to latent reasoning and efficient computation.

**摘要**: arXiv：2605.28889v1宣布类型：新摘要：上下文提炼将上下文信息压缩到模型参数中，但现有方法常常忽略在非Oracle设置中如何存储、检索和安全激活多个提炼的潜在记忆。我们将上下文蒸馏定义为一个潜在的记忆管理问题。我们将每个上下文提取到独立的LoRA适配器中，形成一个模块化内存库，可以实现显式内存选择。给定一个查询，我们的框架检索候选记忆，将查询路由到最合适的适配器，并使用自门控机制来决定是否应该激活潜在记忆。为了提高效率，我们进一步引入了缓存共享，以减少推理期间的管理负担。实验表明，我们的方法在检索方面的表现大大优于基线，而自门控则通过停用不必要的潜在记忆来提高鲁棒性。

[阅读原文](https://arxiv.org/abs/2605.28889)

---

## 31. 人类治疗何时以及如何适得其反：多模型自我消费循环下的偏好对齐

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yang Zhang, Xiukun Wei, Xueru Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies multi-model self-consuming loops with human curation, analyzing alignment dynamics and cross-model influence, directly relevant to RL for LLMs and self-improving agents.

**摘要**: arXiv：2605.29267v1宣布类型：新摘要：基础模型越来越多地根据先前模型迭代生成的合成数据进行训练，而不是专门根据真实数据进行训练。这种自我消耗的训练范式可能会导致模型崩溃、分歧或偏见放大。最近的工作（Ferbach等人，2024）表明，将人类策展纳入循环可以将自我消费模型引导为与人类一致的行为，但这些分析重点关注的是一个单独的、孤立的模型，该模型只消费自己的输出。然而，在实践中，模型经常在其他模型产生的输入输出对上进行交互和训练。本文研究了多模式模式下的自我消费训练。我们首先形式化了交互式自我消费模型的框架，并描述生成的动力系统何时收敛到稳定点。然后，我们研究人类对一个模型的策划如何影响其自身的一致性（自我影响），以及此类影响如何传播到其他模型（交叉影响）。与人类策展总是增强模型一致性的孤立环境不同，我们表明跨模型交互可以抑制甚至逆转这种影响，最终降低长期一致性。

[阅读原文](https://arxiv.org/abs/2605.29267)

---

## 32. 超越轨迹奖励：通过图形建模进行统计搜索的分步信用分配

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuchen Liu, Yingjie Feng, Lixiong Qin, Jiasi Chen, Jianing Yu, Sheng Gao, Sheng Yang, Weiran Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel step-level process reward (GDCR) and a policy optimization method (SAPO) for agentic search, directly contributing to RL for LLMs via fine-grained credit assignment.

**摘要**: arXiv：2605.29697v1宣布类型：新摘要：在统计搜索中，实验室级结果奖励无法量化各个步骤的行为贡献，而现有的步骤级奖励方法通常依赖于昂贵的树采样。我们将世界知识视为潜在世界图，将每个IS任务视为潜在任务图中的搜索，其中有效的步骤应该使图向答案节点前进。基于这一先验，我们提出了图距离贡献奖励（GDCR），这是一种步骤级流程奖励，通过新检索和新引用的实体与训练时关系（ER）图中答案节点的距离对新检索和新引用的实体进行评分。我们进一步提出阶梯优势政策优化（SPP），将GDCR转化为阶梯级优势，并将其与行政级结果优势结合起来。四个具有挑战性的基准测试的实验验证了我们方法的有效性。

[阅读原文](https://arxiv.org/abs/2605.29697)

---

## 33. GrepSeek：培训搜索代理进行直接的数据库交互

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Alireza Salemi, Chang Zeng, Atharva Nijasure, Jui-Hui Chung, Razieh Rahimi, Fernando Diaz, Hamed Zamani

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving search agent trained via GRPO on direct corpus interaction, with a two-stage pipeline for cold-start data and RL-based policy refinement.

**摘要**: arXiv：2605.29307v1宣布类型：新摘要：大型语言模型（LLM）搜索代理通过多轮推理和信息检索显示出对知识密集型语言任务的强大前景。大多数现有的系统使用检索器访问信息，检索器接受关键字或自然语言查询，并使用预先计算的文档表示的索引返回排序的文档列表。在这项工作中，我们探索了一个补充的角度，其中搜索代理将文集本身视为搜索环境，并通过发出可执行的shell命令来寻找证据。我们引入GrepSeek，这是一种优化的直接语料库交互（DCI）搜索代理，它训练紧凑的搜索代理从大型文本库中查找、过滤和组成证据。为了直接通过大型库上的强化学习来解决学习行为的不稳定性，我们提出了一个两阶段训练管道。首先，我们使用答案感知导师和答案盲Planner构建一个冷启动数据集，以生成经过验证的、基于因果关系的搜索轨迹。其次，我们使用组相对策略优化（GRPO）来细化初始化的策略，允许代理通过与文集的直接交互来改进其面向任务的搜索行为。为了使DCI大规模实用，我们进一步使用了一个保持语义的分片并行执行引擎，该引擎将基于shell的检索加速高达7.6%，同时与Shell命令的顺序执行保持字节精确等效性。七个开放领域问答基准的实验表明，GrepSeek实现了最强的整体代币级$F_1$和Exact Match。我们的分析还强调了表面形式差异很大的查询上纯词汇交互的局限性，表明DCI是搜索代理的一种实用且有竞争力的方法，可以补充现实世界中现有的检索范式。

[阅读原文](https://arxiv.org/abs/2605.29307)

---

## 34. TRACE：通过LLM CoT评估的结构性要素进行基于Toulmin的推理评估

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yundong Kim, Heyoung Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TRACE, a novel metric for evaluating CoT reasoning structure using Toulmin's argumentation theory, and demonstrates its effectiveness as a reward signal for RL, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2605.29656v1宣布类型：新摘要：由于缺乏基本事实，评估大型语言模型（LLM）的开放式输出仍然具有挑战性。现有的指标依赖于最终答案的准确性或表面水平的统计数据，而推理过程本身则未经检查。我们引入了TRACE（通过建构性元素进行基于图尔敏的推理评估），这是一种分析思想链（CoT）推理过程的指标。TRACE不是判断结果，而是通过将图尔明的论证理论与弗拉维尔的元认知框架整合来评估推理结构来检查论证是如何构建的。对7个推理模型的26.3K个QA样本进行的实验显示与基准准确性有很强的相关性（r=0.74）。此外，TRACE作为强化学习奖励信号是有效的，优于仅限准确性的基线。总而言之，这些结果表明，逻辑上合理的推理会带来更高质量的答案。因此，TRACE可以作为评估开放式输出的补充指标。代码可在https://github.com/hyyangkisti/trace上获取。

[阅读原文](https://arxiv.org/abs/2605.29656)

---

## 35. 面向低资源目标语言生成的基于源的语义强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zeli Su, Ziyin Zhang, Zewei Pan, Zhou Liu, Dingcheng Huang, Dehan Li, Zhankai Xu, Longfei Zheng, Xiaolu Zhang, Jun Zhou, Wentao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (SG-SRL) that uses a cross-lingual semantic reward model for reference-free RL on source-language data to improve target-language generation, directly addressing RL for LLMs with a new reward design and training recipe.

**摘要**: arXiv：2605.29502v1宣布类型：新摘要：低资源目标语言生成通常受到稀缺并行数据的限制，而高资源源语言单语数据丰富，但难以通过标准监督微调使用。我们提出了基于源的语义强化学习（SG-SRL），这是一种资源利用框架，可将源语言单语数据转换为跨语言语义监督，以用于目标语言生成。SG-SRL使用跨语言语义奖励模型对源语言数据执行无引用强化学习（RL），该模型由跨语言重排序器实例化，该跨语言重排序器对源输入和目标语言生成之间的语义相关性进行评分。虽然这会引发严重的基于冗长的奖励黑客攻击，但使用小型并行数据库的轻量级恢复阶段可以恢复流畅性、简洁性和任务格式，同时保留语义收益。针对中国人到泰国人的实验表明，与冷启动SFT相比，SG-SRL改善了语义基础和事实覆盖。对长式迁移和基于藏传嵌入的奖励的额外分析澄清了SG-SRL的概括行为，并表明基于编码器的语义奖励可以在现实的低资源语言环境中替代基于LLM的重排序器。

[阅读原文](https://arxiv.org/abs/2605.29502)

---

## 36. CosmicFish-HRM：紧凑语言模型中基于层次递归机制的自适应推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Venkat Akhil Lakkapragada

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a compact language model with a Hierarchical Reasoning Module for adaptive latent reasoning depth, directly addressing latent CoT/reasoning.

**摘要**: arXiv：2605.28919v1宣布类型：新摘要：大型语言模型已经实现了强大的推理能力，尽管通常以大量参数计数和昂贵的推理为代价。在这项工作中，我们探索了一个不同的方向：紧凑语言模型中的适应性推理深度。我们提出了CosmicFish-HRM，这是一种围绕分层推理模块（HRM）构建的紧凑语言模型，可以在推理期间动态分配计算工作量。该模型不是对每个输入应用固定计算，而是通过高级和低级推理循环进行迭代，并根据输入复杂性学习何时停止。CosmicFish-HRM将这个自适应推理核心与现代Transformer组件相结合，包括分组查询注意力、RoPE和SwiGLU激活。虽然额外的推理基础设施在小规模上引入了额外的费用，但我们假设，随着模型大小的增长和HRM核心的相对成本的降低，这种权衡变得越来越有利。我们的结果表明，该模型学习非一致推理行为，在任务和输入之间分配不同数量的推理步骤。这些发现表明，自适应推理深度可能提供一个有希望的替代方案，而不是仅仅依赖参数尺度来推理能力。

[阅读原文](https://arxiv.org/abs/2605.28919)

---

## 37. 微宏检索：减少大型语言模型中的长篇幻觉

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yujie Feng, Jian Li, Zhihan Zhou, Pengfei Xu, Yujia Zhang, Xiaoyu Li, Xiaohui Zhou, Alan Zhao, Xi Chen, Xiao-Ming Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel retrieve-while-generate framework with curriculum RL training using rule-based rewards to reduce hallucination in long-form generation.

**摘要**: arXiv：2605.28828v1宣布类型：新摘要：大型语言模型（LLM）在许多任务中都取得了令人印象深刻的性能，但仍然容易产生幻觉，特别是在长形式生成中，其中冗余检索的上下文和冗长的推理链放大了事实错误。最近的研究强调了一个关键现象：关键信息与模型输出越接近，事实准确性就越高。然而，现有的检索增强语言模型（RALM）缺乏有效的机制来确保这种接近性--外部证据通过多轮检索注入到推理中，但这无法确保关键信息保持接近输出。我们提出了微宏检索（M2 R），这是一种新型的边生成边检索框架来填补这一空白。在宏观层面，M2 R从外部来源检索粗粒度证据;在微观层面，它从推理过程中构建的关键信息存储库中提取重要结果，并在生成答案时重复使用它们。该设计直接解决了关键信息与输出的接近度瓶颈，有效地减少了长篇任务中的幻觉。M2 R采用基于课程学习的强化学习策略进行培训，使用定制的基于规则的奖励，从而能够稳定地获得检索和基础技能。跨不同基准的广泛实验证明了M2 R的有效性，尤其是在复杂的上下文环境中。

[阅读原文](https://arxiv.org/abs/2605.28828)

---

## 38. RL 2ML：从强化学习到最大可能性的临时推出替代目标

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yifu Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RL2ML, a family of finite-rollout surrogate objectives with unbiased gradient estimators for RLVR, directly addressing RL training recipes for LLMs with verifiable rewards.

**摘要**: arXiv：2605.30154v1宣布类型：新摘要：具有可验证奖励的基于正确性的强化学习（WLVR）根据采样输出的二进制反馈训练语言模型，但根据期望优化的目标和有限推出组引起的随机更新几何常常被混为一谈。本文开发了RL 2 ML，这是一个具有封闭形式、完全无偏梯度估计器的有限推出代理目标族。该系列不断连接标准强化学习、类最大似然训练和超越最大似然目标，同时在固定的推出预算下保持估计器与目标的一致性。我们引入了组级更新规模，以描述在观察到其经验成功计数后如何重新加权推出组，揭示了仅由人口级客观符号隐藏的亚临界-超临界更新规模转变。在这一区别的基础上，校准的指标-收益分析和精确的方差分解表明，替代目标的最佳选择既不是由接近最大似然度决定的，也不是仅由人口水平权重决定的。相反，它共同取决于评估指标、局部敏感性和估计器方差。因此，代理目标族中剩余的自由度可以被表述为一维优化问题，而不是被视为无约束的超参数。

[阅读原文](https://arxiv.org/abs/2605.30154)

---

## 39. 灾难性遗忘的机制起源：为什么RL比SFT更好地保留电路？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jeanmely Rojas Nunez, Viraj Sawant, Nathan Allen, Nomgondalai Amgalanbaatar, Yannis Zongo, Vasu Sharma, Maheep Chaudhary

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly investigates why RL preserves circuits better than SFT during LLM fine-tuning, introducing a mechanistic measure of circuit preservation.

**摘要**: arXiv：2605.28860v1宣布类型：新摘要：微调大型语言模型（LLM）经常会导致对先验能力的灾难性遗忘。最近的工作表明，强化学习（RL）比监督式微调（SFT）更有效地保留了先前的能力，这归因于政策梯度更新更接近基本政策\cite{shenspel 2025 rl}。我们将这种行为解释扩展到机械层面，并询问RL的优势是否通过更强的内部计算电路保留来反映。我们引入了差异电路脆弱性，这是对电路在微调下退化程度的头部级别测量，并使用它来比较适合科学问答的Qwen 2.5 - 3B-Direct上的RL和SFT。我们发现了一个明显的机械权衡：SFT更快地适应目标任务，但会产生更大的电路中断和对先前能力的遗忘，而RL则保留了更大比例的基本电路，代价是任务适应速度较慢。这些发现表明，回路保留可能有助于解释为什么RL对灾难性遗忘更强大。我们在这里发布了我们的代码：https://github.com/rl-sft-circuit-research/differential-circuit-vulnerability。

[阅读原文](https://arxiv.org/abs/2605.28860)

---

## 40. 抽样推理：在决策点进行切割

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Felix Zhou, Anay Mehrotra, Quanquan C. Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel inference-time sampling algorithm (Entropy-Cut Metropolis-Hastings) that uses entropy to identify decision points for resampling, improving reasoning without additional training, directly relevant to latent reasoning and efficient sampling.

**摘要**: arXiv：2605.30327v1宣布类型：新摘要：前沿推理模型是通过强化学习后训练基本语言模型来生成的。最近的工作对这一点提出了挑战，表明从基本模型分布的尖锐版本（所谓的功率分布）进行抽样，可以在无需额外训练、精心策划的数据集或验证器的情况下引发可比推理。然而，要使这种方法实用化，需要有效地从配电中进行采样。采样器需要“混合”到功率分布，这需要在目标分布的模式之间移动;直观地，例如，尝试不同的推理策略。之前的作品中提出的采样器在当前推理轨迹中重复均匀随机选择“切割”位置，并从该位置开始重新采样后缀。然而，推理痕迹通常包含一些重要的决定（例如，证明策略或算法的选择），我们观察到统一选择的切割往往会重写局部细节，而不是重新访问决策点。我们引入了一种算法（Entropy-Cut Metropolis-Hastings），该算法使用基本模型的下一个令牌信息作为代理来识别关键决策点并从这些位置重新采样。我们通过经验验证了信息量跳跃是决策点的有用代理，并在一个典型的推理模型中证明了我们的方法的混合时间与轨迹中决策的数量而不是与令牌数量相关，而令牌数量可能会大得多。在Math 500、HumanEval、GPQA Diamond和AIM 26中，我们的方法始终优于基线和RL训练模型。

[阅读原文](https://arxiv.org/abs/2605.30327)

---

## 41. CRITIC-R1：检索增强一代的学习结构化批评者

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wenhan Xiao, Ziwei Zhang, Chuanyue Yu, Xingcheng Fu, Qingyun Sun, Runhua Xu, Jianxin Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a structured critic framework for RAG using RL (GRPO) with novel reward functions for calibrated and diagnostic feedback, directly relevant to RL for LLMs.

**摘要**: arXiv：2605.29886v1宣布类型：新摘要：检索增强生成（RAG）通过整合外部证据来改进知识密集型问答。然而，现有的RAG方法仍然存在幻觉和微妙的推理错误。最近的研究引入了外部批评者来完善RAG输出，但它们通常提供粗粒度和结构薄弱的反馈，表现出过度激进的干预，并导致噪音和不可靠的细化，限制了其纠正的有效性。为了解决这些问题，我们提出了CRITIC-R1，这是一个结构化的批评者框架，它使用强化学习（RL）将RAG批评作为显式错误诊断问题来制定和学习。我们的框架将常见的RAG错误分类为多个诊断维度，包括判决、错误位置、推理分析和修复生成。为了学习这些能力，我们设计了两个奖励功能：保守判断对齐（CJA）首先鼓励校准的高级判断，同时减轻过度攻击现象，而诊断质量对齐（DQA）通过门控奖励进一步改善细粒度诊断反馈。我们使用基于GRPO的RL以及从外部LLM教师模型收集的过程级监督来训练批评者模型。五个QA基准测试的实验表明，CRITIC-R1在强大的RAG基线上持续提高了答案质量。   我们的源代码可在https://anonymous.4open.science/r/critic-r1-FCB0上获取

[阅读原文](https://arxiv.org/abs/2605.29886)

---

## 42. BORA：为现实世界的灵巧VLA模型搭建离线强化学习和在线剩余自适应的桥梁

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhongxi Chen, Yifan Han, Yanming Shao, Huanming Liu, Congsheng Xu, Xiaoyu Chen, Yao Mu, Wenzhao Lian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes BORA, an offline-to-online RL post-training framework for dexterous VLA models with a novel critic design and human-in-the-loop residual adaptation.

**摘要**: arXiv：2605.30226v1宣布类型：新摘要：视觉-语言-动作（VLA）模型已成为将视觉语言理解融入现实世界机器人操纵的一种有前途的范式。然而，由于多维手部控制和复合执行错误，灵巧操纵对VLA政策来说仍然具有挑战性，这使得现实世界的RL后期训练对于弥合视觉基础动作生成和物理可靠的灵巧执行之间的差距至关重要。然而，多维的灵巧探索往往会引发现实世界中的时间不一致、样本效率低下和硬件风险。为了应对这些挑战，我们提出了BORA，这是一种离线到在线的RL后训练框架，专为现实世界的灵巧VLA模型设计。在离线阶段，BORA构建了一个批评者，该批评者将VLM的认知令牌和动作块作为输入。这种设计实现了以动作为条件的价值指导，使评论家能够评估视觉背景之外的灵巧手部动作。在随后的在线阶段，BORA冻结了VLA基础，并引入了一种轻量级的、人在环（HiL）块式剩余自适应机制，以减轻现实世界的执行错误，并进一步纠正实际物理环境中离线学习的意图。通过继承离线批评者并采用干预驱动的奖励，BORA有效地纠正了执行差异并适应现实世界的物理差异，同时将预训练的策略保留为稳定的先验。对五个复杂的现实世界灵巧任务的广泛评估表明，BORA的表现显着优于纯模仿学习和传统的脱钩RL基线，在标准设置下实现了平均成功率的绝对提高33%，在未见对象的概括方面提高了高达43%。

[阅读原文](https://arxiv.org/abs/2605.30226)

---

## 43. ESPO：早期停止的近端政策优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zihang Li, Rui Zhou, Yingcheng Shi, Wenhan Yu, Zhewen Tan, Zixiang Liu, Zeming Li, Binhua Li, Yongbin Li, Tong Yang, Jieping Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ESPO, a novel RL training method for LLMs that early-stops failed rollouts to save compute and improve reasoning performance.

**摘要**: arXiv：2605.29860v1宣布类型：新摘要：当强化学习下的大型语言模型在轨迹早期提出错误的推理步骤时，标准算法会迫使它继续生成直到最大限度，将计算花费在从未收到正奖励的令牌上，并用失败后的噪音污染优势估计。我们提出了ESPO（早期停止近端策略优化），它实时检测轨迹故障并提前终止部署。在每个生成步骤中，ESPO仅使用采样期间已经计算的logit来计算代理后悔，并在平滑的累积后悔显着超过其估计值时终止。截短轨迹被视为吸收具有最终奖励的失败状态，将负时间差（TD）错误集中在检测到的失败步骤附近，无需任何额外的奖励模型或人类注释。在经过数学推理训练的DeepSeek-R1-Distill-Qwen-7 B上，ESPO在AIME~2024（46.28%对45.25%）、AMC~2023（85.83%对82.94%）和MAT-500（87.42%对85.43%）上超过了PPO，同时累计节省超过20%的推出代币。

[阅读原文](https://arxiv.org/abs/2605.29860)

---

## 44. GrowLoop：人类播种的自我进化对话评估

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yihang Lin, Yunze Gao, Zeyang Lin, Dongbo Li, Kun Peng, Chenglong Song, Yue Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GrowLoop, a self-evolving evaluation system that uses LLM agents to iteratively refine rubrics and cases, aligning with the self-evolving agent criterion.

**摘要**: arXiv：2605.28882v1宣布类型：新摘要：随着大型语言模型的快速发展，在开放式对话中评估人类相似性变得越来越重要。然而，人形是人类凭直觉感知的一种隐性知识形式，但基本标准却抵制明确的表述。人类的判断差异很大，在某些情况下存在强烈的一致意见，而在另一些情况下存在合理的分歧。与此同时，人类判断背后的标准仍然隐含，没有为构建案例留下明确的基础。此外，类似人类的东西并不是静态的，而是随着模型能力和人类期望而不断变化。尽管专家制定的基准、奖励模型和自我进化的基准等评估方法取得了进展，但没有一种方法能够同时解决这三个挑战。因此，我们提出GrowLoop，这是一个自我进化的对话评估系统，随着模型的进步和场景的变化而不断适应。LLM代理以最少的人类种子注释作为先行者，通过启发式学习迭代地提取和完善评估指标。当注释者趋同时，需要人与人工智能协议，而当注释者分歧时，只期望达成合理性。此外，鲁布里克-案例协同进化机制能够实现持续进化，并在评估目标移动时通过新种子进行扩展。应用于开放式对话中的人形评估，生成的标题不仅在符合人类判断方面大大优于现有方法，而且还揭示了注释者忽视的问题。由此产生的基准有效地区分了跨能力层的模型，并揭示了它们的不足之处，同时推广到新场景并随着模型的发展而进行调整。我们的工作将基准范式从手动更新或难度扩展转变为全面、持续的自我进化。

[阅读原文](https://arxiv.org/abs/2605.28882)

---

## 45. 我是谁？辅导对话中学生模拟的历史感知配置文件

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based framework for history-conditioned student simulation in tutoring dialogues, directly matching RL for LLMs via reward design and training.

**摘要**: arXiv：2605.30051v1宣布类型：新摘要：开发大型语言模型（LLM）驱动的自动化辅导工具的一个关键部分是学生模拟，即利用LLM作为学生角色扮演，可以促进导师模型评估和培训。现有的工作主要集中在对话内模拟上，缺乏学生知识和行为的背景，部分原因是没有基于过去的学生问答或对话互动。在这项工作中，我们引入了受历史影响的学生模拟任务，目标是通过利用学生学习历史中的信息准确预测学生的对话转折。我们提出了一个两部分框架，其中个人资料生成器总结了学生的历史，模拟器根据所得个人资料预测学生的成绩。我们通过强化学习（RL）训练这两个组件，生成针对忠实的学生模拟而优化的配置文件。我们根据从数学学习平台收集的第一个真实世界的学生对话和问题回答数据集来评估我们的方法和基线。大量实验表明，我们的方法显着优于基线，并证明了历史、配置文件和RL训练的重要性。

[阅读原文](https://arxiv.org/abs/2605.30051)

---

## 46. PEARL：通过教学一致的强化学习培训苏格拉底导师

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qikai Chang, Zhenrong Zhang, Linbo Chen, Pengfei Hu, Jianshu Zhang, Youhui Guo, Jun Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PEARL, a pedagogically aligned RL framework with a controllable student simulator and generative reward model for training Socratic tutoring agents, directly matching RL for LLMs.

**摘要**: arXiv：2605.29582v1公告类型：新摘要：大型语言模型（LLM）已经显示出作为教育导师的前景，但有效的辅导需要的不仅仅是解决问题：它必须提供渐进的苏格拉底式指导，并在多轮互动中平衡多个教学目标。然而，培训这样的导师仍然具有挑战性，由于有限的保真度和弱可控的学生模拟，在指定的教学奖励建模，和不稳定的多目标优化。为了克服这些限制，我们提出了PEARL，这是一个教学一致的强化学习框架，用于培训苏格拉底辅导员，由三个关键组件组成。首先，我们引入了一个可控的学生模拟器，它将潜在的认知状态与反应生成分开，以模拟不同的能力和误解。其次，我们开发了生成性奖励模型，联合评估教学质量和政策优化的客观正确性。最后，我们提出了一个稳定的多目标RL方案，该方案将每个维度内的奖励离散化，并聚合维度之间的标准化优势，防止高方差目标主导更新。多个基准测试的实验表明，尽管仅使用30 B策略模型，PEARL在开源模型中实现了最佳性能，并且与领先的专有LLM保持竞争力。

[阅读原文](https://arxiv.org/abs/2605.29582)

---

## 47. 诚实的谎言：理解反身代理中的记忆虚构

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Prakhar Dixit, Sadia Kamal, Tim Oates

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies memory confabulation in Reflexion-style agents and proposes a mitigation using programmatic failure extraction, directly addressing self-improving agent limitations.

**摘要**: arXiv：2605.29463v1宣布类型：新摘要：反射式智能体依赖于自我生成的反射作为记忆，隐含地假设智能体能够准确地诊断自己的失败。我们表明，这个假设可能会系统性地失败：在ALFWorld和HumanEval中，智能体存储了对任务的自信但不正确的解释，并在整个试验中继续对它们采取行动，即使环境每次都重置为正确的任务。我们将这种情况称为失败模式记忆虚构，并引入反射重复率（SVR），这是一种基于日志的指标，用于检测对不正确反射内容的重复依赖。使用SVR，我们在ALFWorld中识别了16个冻结环境，其中121个反射中的0个提到了正确的目标对象，HumanEval中还有4个类似的情况。我们的缓解措施用程序化提取宇航员级故障信号取代了开放式自我诊断，将正确的对象提及率从0%提高到86%，将RR从0.64降低到0.10，并解决了16个冻结的ALFWorld环境中的3个，这表明反思记忆可以强化错误信念而不是纠正错误信念。

[阅读原文](https://arxiv.org/abs/2605.29463)

---

## 48. 训练黑匣子计划检测的深思熟虑者

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Aditya Sinha, Akshat Naik, Victor Gillioz, Simon Storf, Kilian Merkelbach, Rich Barton-Cooper, Axel H{\o}jmark, Marius Hobbhahn

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based distillation pipeline (supervised fine-tuning + RL) to train smaller monitors for scheming detection, directly matching RL for LLMs via reward design and verifier-driven optimization.

**摘要**: arXiv：2605.29601v1宣布类型：新摘要：随着自主代理人越来越有能力执行现实世界的任务，区分阴谋行为与良性任务追求可能成为人工智能控制的核心问题。现有的监视器通常依赖于思想链访问或内部激活，或使用提示前沿模型，所有这些都可能不可用、不可靠或部署昂贵。在这项工作中，我们研究了纯动作的深思熟虑监视器：较小的开权模型，经过训练，用于检测来自特工轨迹的阴谋和破坏，而无需访问被监视特工的推理或模型内部。我们的方法受到深思熟虑调整的启发，使用一个有计划的规范从前沿教师那里引出结构化的原理，用单独的法官过滤它们，并将最高质量的原理提炼到具有监督微调和强化学习的开重监视器中。我们在五个数据集上进行训练，并评估六个非分布代理失准基准。我们表明，将我们的方法应用于Qwen 3.5 - 27 B可以产生比所有低成本前沿模型（Gemini 3.1 Flash-Lite、GPT-5.4 Nano和Claude Haiku 4.5）和Gemini 2.5 Pro更高的性能，同时还实现了更低的边际推断成本（每1，000次评估中的代币计量美元）。更强的提示前沿监视器（Gemini 3.1 Pro、GPT-5.4、Claude Sonnet 4.6和Claude Opus 4.6）实现了更高的性能，但大约为16美元--34美元x美元的边际推理成本更高。我们的几位训练有素的监测员在我们评估的监测员中定位于经验成本-性能帕累托前沿，为提示前沿模型提供实用的低成本、低FPR替代方案。

[阅读原文](https://arxiv.org/abs/2605.29601)

---

## 49. BenchTrace：测试LLM代理反思能力和受控进化的基准

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiahao Huang, Fei Cheng, Junfeng Jiang, Zefan Yu, Akiko Aizawa

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a benchmark and metric for evaluating self-evolving agents' reflection and controlled evolution, directly addressing self-improvement in agents.

**摘要**: arXiv：2605.29225v1宣布类型：新摘要：自我进化的代理通过反思过去的失败来随着时间的推移而改进，但现有的评估在两个方面受到限制：它仅测量任务分数，导致反思质量未知，并且它依赖于代理自己的事件运行，没有提供针对特定失败模式的机制。我们提出了\textBF{BenchTrace}，这是评估LLM代理自我进化能力的基准。BenchTrace建立在涵盖六项不同任务的1，821个带注释的剧集的快照反射数据集之上，其中包括一个\textBF{Reflection Evaluation}，通过有针对性的QA任务来探索故障识别，以及一个\textBF{Evolution Evaluation}，测试过去的失败经验是否转化为受控自我进化模拟中的回避行为。在BenchTrace的基础上，我们提出了\textBF{失败避免率（FAR）}，这是一种新的评估指标，用于衡量代理成功避免目标失败实例的测试用例的比例。Qwen 3 - 32 B和GPT-4.1的实验表明，这两个模型的反射评估端到端通过率均低于30%，诊断是主要瓶颈。进化评估表明，自我进化方法通常会在非进化基线上提高FAR，但随着噪音事件的积累，代理人忘记了早期的教训，并且代理人未能将其反映概括到特定上下文之外，从而导致跨任务上下文的负迁移。我们的相关性分析进一步表明，只有完全正确的反射才与更高的FAR密切相关。BenchTrace揭示了当前自我进化方法的具体局限性，并为有针对性的评估提供了受控的、模型不可知的框架。

[阅读原文](https://arxiv.org/abs/2605.29225)

---

## 50. 幻觉检测引导的临床总结偏好优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shamanth Kuthpadi Seethakantha, Dung Ngoc Thai, Vara Prasad Gudi, Simran Tiwari, Rami Matar, Avijit Mitra, Wenlong Zhao, Wael Salloum, Andrew McCallum

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL pipeline using hallucination detector-guided refinement trajectories to generate preference pairs for preference optimization, directly improving LLM factual faithfulness.

**摘要**: arXiv：2605.28910v1宣布类型：新摘要：大型语言模型（LLM）在总结任务方面表现出了希望，但它们经常产生幻觉，这些幻觉是不支持或不正确的陈述，限制了它们在专业医疗保健应用中的可靠性。我们引入了\itermodelfull（\itermode），这是一种推理时方法，它利用幻觉检测器来引导迭代摘要修订以实现事实更正。在此基础上，我们提出了用于偏好学习的\itermode（\models），它将检测器引导的细化轨迹转换为用于模型微调的偏好对。大量实验表明，我们的方法在总结\MimicIV的现实世界临床笔记时大幅减少了Llama和Gemma模型的幻觉。例如，在Llama-3.1- 8B-Direct中，\itermode减少了24%，\模型减少了48%的幻觉。重要的是，根据人类专家和法学硕士评审团的评估，这两种方法都保持了摘要的流畅性、连贯性和相关性。总而言之，这些结果表明，基于检测的细化和偏好学习为提高临床总结中的事实忠实性提供了自动化解决方案。

[阅读原文](https://arxiv.org/abs/2605.28910)

---

## 51. DynSess：面向角色扮演Agent的动态会话级评估与优化框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Rongsheng Zhang, Jiji Tang, Junnan Ren, Zuyi Bao, Weijie Chen, Ruofan Hu, Zhou Zhao, Tangjie Lv, Yan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a session-level RL framework for role-playing agents that uses multi-turn lookahead search to generate training trajectories and on/off-policy RL for self-improvement.

**摘要**: arXiv：2605.29256v1宣布类型：新摘要：使用大型语言模型的角色扮演从根本上来说是一项会话级任务，需要代理在扩展的多回合对话中维持角色身份和交互质量。然而，现有的评估和优化方法在很大程度上仍然是交叉层面的，未能捕捉长期质量。我们提出了DynSess，这是一个用于角色扮演代理的统一会话级框架。DynSess-Eval通过针对长期行为的标题对完整的对话进行评分。利用其会话级别奖励，我们通过多轮前瞻搜索构建高质量的训练轨迹，并通过两个互补变体（DSPO（政策外）和GSRPO（政策上）训练DynSess-Charlotte。实验表明，DynSess-Eval比之前的评估者更好地与人类判断的一致性，而盲目的人类评估进一步表明，尽管使用的参数少得多，DynSess-Charlotte仍能匹配最强的角色模型，同时保持了很强的角色一致性和交互能力。我们的数据集和代码将被发布以促进未来的研究。

[阅读原文](https://arxiv.org/abs/2605.29256)

---

## 52. 用于稳健偏好建模的上下文奖励自适应

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhenyu Sun, Zheng Xu, Ermin Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel in-context reward adaptation framework for RLHF that adapts to unseen human preferences using transformer-based inference, directly addressing reward model robustness.

**摘要**: arXiv：2605.30323v1宣布类型：新摘要：来自人类反馈的强化学习（RL HF）通常依赖于静态奖励模型来使大型语言模型与人类偏好保持一致。然而，人类的价值观本质上是多样性和异类的，单一的奖励模型往往缺乏推广到不可见的偏好领域所需的稳健性。虽然现有的多奖励框架试图解决这一问题，但它们往往局限于一组固定的已知领域，并且在没有昂贵的重新训练的情况下无法适应看不见的人类分布。在这项工作中，我们提出了上下文奖励适应，一个基于transformer的框架，旨在模拟不同的和看不见的人类偏好。通过利用变压器的上下文中的学习能力，我们的方法自适应地推断出一个小的一组偏好演示的基本奖励结构。我们证明，虽然标准的Transformer架构不足以通过描述对地面事实的渐进偏差来完成这项任务，但将人类响应时间作为辅助输入信号将使模型能够成功地适应来自之前未见过的领域的偏好。我们的研究结果表明，这种方法为偏好建模提供了更强大的基础，允许表示异类奖励和偏好分布转变，并提供了实现更灵活的人类与人工智能匹配的可扩展路径。

[阅读原文](https://arxiv.org/abs/2605.30323)

---

## 53. 有用的诅咒：通过干扰IF对干扰器指令的鲁棒性的逆标度定律

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zeli Su, Zhankai Xu, Tianlei Chen, Longfei Zheng, Xiaolu Zhang, Jun Zhou, Wentao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Demonstrates that reinforcement learning (GRPO) can restore robustness against distractor instructions in LLMs, directly applying RL to improve instruction-following behavior.

**摘要**: arXiv：2605.29491v1公告类型：新摘要：大型语言模型（LLM）越来越多地部署在代理和检索增强生成（RAG）系统中，在这些系统中，它们必须在外部提供的参考文本上执行用户指定的任务。在实践中，这样的上下文通常是非结构化的，并且被良性但类似于警告的语义噪音污染，例如编辑评论和系统跟踪，这些应该被严格视为数据。我们引入了DistractionIF，这是一个旨在评估针对参考文本中此类干扰指令的稳健性的基准。在广泛的模型中，我们观察到一致的逆缩放现象：较大的模型通常不太稳健，随着规模的增加，性能会下降多达30个百分点。从机制上讲，我们的困惑性分析表明，缩放侵蚀了稳健行为和分心行为之间的概率边界，使模型越来越容易过度将噪音解释为指令。为了解决这个问题，我们证明强化学习，特别是组相对政策优化（GRPO），可以恢复这一边界，将稳健性提高高达15.5%，而不会损害一般的描述跟踪能力。我们的研究结果强调了基于引用的任务中一个关键的描述遵循稳健性差距，并将强化学习确立为大规模实施严格数据指令分离的有希望的路径。

[阅读原文](https://arxiv.org/abs/2605.29491)

---

## 54. STAMPS：在可控和可扩展的虚拟环境中训练移动图形用户界面代理的显式内存

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junyang Wang, Haiyang Xu, Xi Zhang, Zhaoqing Zhu, Ming Yan, Jieping Ye, Jitao Sang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a framework that trains explicit memory in mobile GUI agents using controllable virtual environments and online RL with environment-driven reward feedback, directly matching the RL for LLMs and self-evolving agents criteria.

**摘要**: arXiv：2605.29324v1宣布类型：新摘要：移动图形用户界面代理擅长立即反应式控制，但在需要内存的现实、长期任务中经常失败。这种失败源于有限的上下文窗口和大量符号的屏幕截图之间的根本冲突。为了保存有限的上下文，代理必须逐步丢弃旧的视觉历史，永久丢失关键的瞬时信息。此外，现有的以动作为中心的数据集无法教代理明确记住什么或何时记住，并且增强静态现实世界数据的成本高得令人望而却步，并且缺乏交互式验证。为了解决这个问题，我们提出了STMP，这是一个通过可控虚拟环境训练移动代理中的显式记忆的框架，其中确定性记忆变量以编程方式注入到合成任务中，以控制必须记住的内容、何时应该编码以及何时必须检索，从而大规模地产生可验证的监督数据，并通过环境驱动的奖励反馈实现在线强化学习。根据我们新推出的内存世界基准进行评估，最终的Stamp-GUI代理在GUI-Specific模型中实现了最先进的性能，并在我们的内存世界基准上设定了新的高水平，展示了出色的内存准确性和任务弹性，同时保持强大的通用移动导航功能。

[阅读原文](https://arxiv.org/abs/2605.29324)

---

## 55. 学习设计技能作为宇宙量子逆设计的存储策略

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shengchao Chen, Ting Shu, Sufen Ren

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a closed-loop agent framework with RL-learned skill selection and memory-policy learning for self-improving photonic inverse design.

**摘要**: arXiv：2605.29421v1宣布类型：新摘要：由于候选几何形状必须满足昂贵的电磁模拟下的耦合光学目标，因此光电晶体光纤（CTF）反向设计仍然具有挑战性。现有的管道改进了替代预测或一次性参数推荐，但它们不会在迭代试验中积累可重复使用的设计知识。我们将PCO逆设计表述为一个记忆策略学习问题，并提出SkillPCO，这是一个闭环代理框架，它结合了物理引导的记忆技能库、学习技能选择和基于模拟器的技能进化。我们进一步构建了一个现实世界的数据集，其中包含479个专家交互轨迹（2，507个跨度）和553个依赖于内存的评估查询，涵盖分散工程、损失优化和多目标设计。跨多个LLM主干和经典基线的实验表明，SkillPCO在实际模拟预算下实现了更强的设计质量和效率权衡，证明了我们提出的记忆技能学习范式对于物理感知的PFA反向设计的有效性。

[阅读原文](https://arxiv.org/abs/2605.29421)

---

## 56. 在如何解决之前先知道要解决什么：预先计划赋予LLM数学推理权力

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shaojie Wang, Liang Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel preplan stage and composite GRPO reward for mathematical reasoning, improving plan-based reasoning with explicit problem understanding.

**摘要**: arXiv：2605.30245v1宣布类型：新摘要：当前的基于计划的推理方法通过在执行之前插入计划阶段来改进大型语言模型（LLM），从而引发问题$\rightarrow$ plan $\rightarrow$ cot范式。虽然有效，但仔细检查揭示了固有的范式层面差距：规划和执行阶段都决定如何解决问题，而解决什么的优先问题;认识问题类型、适用的工具和可预见的陷阱;仍然完全隐含。为了弥合这一差距，我们提出了PPC（Preplan-Plan-CoT），这是一个引入了明确的问题理解阶段（预先计划）的框架，产生了一个新问题$\rightarrow$ preplan $\rightarrow$ plan $\rightarrow$ cot范式。实现这一范式需要保护两端预先计划的概念完整性。具体来说，我们设计了一个带有剧透评分检测器的三阶段合成管道，该检测器可以过滤泄漏和剧透故障，以建立干净的预先计划监督，并且复合GRPO奖励强制生成的计划真正遵循预先计划。四个主干和五个数学推理基准的实验表明，PPC在40个指标中的39个指标上实现了最佳结果，在不引入额外推理令牌负担的情况下，将maj@16和pass@16比最强基线提高了+2.23和+3.06。

[阅读原文](https://arxiv.org/abs/2605.30245)

---

## 57. 视觉语言模型训练后推理和感知的非对称优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xueqing Wu, Yu-Chi Lin, Kai-Wei Chang, Nanyun Peng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses perception-reasoning asymmetry in VLM post-training and proposes reward interventions for RL, directly addressing RL reward design for LLMs.

**摘要**: arXiv：2605.29496v1公告类型：新摘要：后训练极大地改善了前沿视觉语言模型的推理，但其感知增益仍然相对有限，为端到端视觉推理创造了瓶颈。为了研究这一差距，我们引入了一个控制诊断框架，两个合成任务，从推理中解开感知。我们的分析揭示了一致的感知-推理不对称性：后训练比感知更能改善推理，尽管基本机制因训练范式而有所不同。对于监督式微调（SFT）来说，这种不对称性源于思想链监督中的代币不平衡，其中感知占用的代币更少，因此接收的训练信号更弱。动态重新加权损失可以缓解这种不平衡，并将端到端性能提高高达18.2。对于强化学习（RL）来说，不对称性反而源于奖励耦合：结果奖励与推理的相关性比与感知的相关性更强，从而削弱了感知学习的信号。添加感知奖励可缓解不平衡，并将端到端准确性提高高达6.0;即使没有地面真相感知奖励，可靠的替代奖励也能提供有用的信号，产生3.2分的收益。我们的结果总体上全面诊断了不对称优化，并提出了具体的干预措施来平衡感知和推理。

[阅读原文](https://arxiv.org/abs/2605.29496)

---

## 58. FakeVLM-R1：通过CoT内化物理定律以进行合成图像检测

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Leqi Zhu, Junyan Ye, Kaiqing Lin, Zhiyuan Yan, Conghui He, Weijia Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FakeVLM-R1 which integrates GRPO (RL) with a critical thinking CoT for synthetic image detection, directly matching RL for LLMs via verifiable reward and a new training pipeline.

**摘要**: arXiv：2605.30062v1宣布类型：新摘要：生成式人工智能技术的发展将合成图像的视觉真实感推向了前所未有的水平。尽管当前基于大型多峰模型（LSYS）的可解释检测方法已经取得了一定进展，但它们仍然依赖于从大量伪造数据中获得的模仿学习。因此，他们缺乏真正的因果推理能力，并且容易产生解释性幻觉。为了克服这一瓶颈，我们提出了FakeVLM-R1，旨在赋予模型在执行合成检测任务时类似人类的批判性思维能力。该框架以监督微调（SFT）为基础，集成了集团相对政策优化（GRPO）与批判性思维链（CoT）机制。在推理阶段，模型执行“双向辩证推理”过程：在提出伪造假设的同时，必须同时援引物理常识来构建真实性反证。此外，我们利用高质量样本构建了FakeClue++数据集，该数据集广泛引入了由真实图像物理定律指导的注释，为模型提供了统一的真实性锚点。实验证实，FakeVLM-R1在多个基准测试中实现了评估模型的SOTA性能。它不仅实现了高精度、逻辑上可解释的检测，而且还解决了现有方法对真实图像的过度拒绝偏差，展示了对扰动的概括性和鲁棒性。

[阅读原文](https://arxiv.org/abs/2605.30062)

---

## 59. GAPD：知识库问题回答中的强化学习的黄金行动政策提炼

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xin Sun, Jianan Xie, Zhongqi Chen, Qiang Liu, Shu Wu, Bowen Song, Weiqiang Wang, Zilei Wang, Liang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GAPD, a gold-action policy distillation framework that adds dense token-level guidance to outcome-based RL for KBQA, directly matching RL for LLMs with a new reward design and training recipe.

**摘要**: arXiv：2605.29584v1宣布类型：新摘要：强化学习（RL）非常适合代理知识库问答（KBQA），其中模型必须发出可执行动作、观察知识库反馈并最终返回答案。然而，当前基于RL的KBQA系统主要优化最终答案的稀疏奖励，从而使中间动作错误受到弱监督。这对于逻辑形式注释的KBQA基准测试尤其具有限制性：黄金逻辑形式可以转换为可执行动作序列，但现有的管道主要使用它们来热启动数据构建，而不是用于按策略RL更新。我们提出了GAPD，这是一个培训时黄金行动政策蒸馏框架，为基于结果的RL添加了密集的代币级指导。为了将黄金行动与政策上的学生推出保持一致，GAPT使用中间锚匹配：它将学生探索和黄金执行期间达到的中间实体视为州锚，并通过这些探索的实体集将学生州与黄金州进行匹配。以这种一致的黄金行动为条件的当前政策充当停止梯度教师，其代币分布在生成的行动代币跨度上被提炼回普通学生政策。GAPT始终超越了WebQSP、GrailQA和GraphQ的当前技术水平。

[阅读原文](https://arxiv.org/abs/2605.29584)

---

## 60. RUBRIC-ARROW：不可验证领域LLM后训练的交替逐点Ruby奖励建模

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haoxiang Jiang, Zihan Dong, Tianci Liu, Wanying Wang, Ran Xu, Tony Yu, Linjun Zhang, Haoyu Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces RUBRIC-ARROW, an alternating framework for pointwise reward modeling with an RL stage using pairwise data and GRPO, directly addressing RL for LLMs with a new reward design and training pipeline.

**摘要**: arXiv：2605.29156v1宣布类型：新摘要：逐点奖励建模为LLM培训后提供了关键信号，但在主观、不可验证的环境中，绝对评分却很困难。基于条目的方法通过将评估分解为显式标准来解决这个问题，但现有方法通常依赖于前沿LLM，并受到硬布尔聚合引起的束缚。我们提出了RUBRIC-ARROW，这是一个交替框架，联合训练标题生成器和标题条件判断器，其RL阶段仅使用成对偏好数据。我们的方法结合了基于概率的评分规则和交替的GRPO计划，该规则减少了与特定阶段的基于偏好的奖励的联系，该计划共同训练逐点评估者。大量实验表明，RUBRIC-ARROW实现了有竞争力的奖励建模准确性，并为下游政策训练后产生一致的收益。

[阅读原文](https://arxiv.org/abs/2605.29156)

---

