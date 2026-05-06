# 💡 今日研究速览 (Daily Summary)

# LLM和后期培训的RL
LLM的强化学习仍然是主要的焦点，针对复杂的长期任务的学分分配和奖励设计的工作激增。几篇论文解决了提供超越二元结果的细粒度反馈的根本挑战。* * DSPO **在长推理链中引入了一种使用每个令牌信用的分布偏差的无批评方法，而**SAPO**提出了段级策略优化以稳定训练。奖励黑客攻击的关键问题由工具使用代理的新专用基准系统性地解决，并且**T2 PO**为多回合代理设置提供不确定性引导的探索控制。具有可验证奖励的RL（WLVR）的可靠性也受到了审查，一项研究表明，验证中的系统性假阳性可能会导致性能崩溃，凸显了对稳健奖励信号的必要性。这项集体工作标志着LLM的RL成熟，从简单的基于结果的奖励转向更细致、可控和安全的训练动态。

# 代理和自我进化系统
人工智能代理领域正在迅速发展为能够解决长期、科学和交互任务的自主、自我改进的系统。前沿科学的全自动agentic框架**SciResearcher** 通过使用agentic RL进行自我完善，体现了这一趋势。与此同时，**HeavySkill**将重思维概念化为一种可以通过RL扩展的内在技能，直接实现自我进化。对于长视野任务，一项系统性的实证研究将视野缩减确定为稳定代理培训的关键原则，而**将痕迹提升为逻辑**引入了一种神经符号方法，用于从代理痕迹中诱导编程技能。医疗保健领域引入了针对医疗代理的专门人工智能GYM，具有一种用于稳定RL训练的新型自蒸馏方法。这一系列工作表明了对能够在复杂、多回合环境中推理、规划和从自己的经验中学习的代理的明确推动力。

# 推理和推理优化
提高LLM推理能力仍然是一个充满活力的领域，培训和推理时策略都有创新。一个关键的开发是**RAG over Thinking Traces**，它检索推理痕迹作为语料库，以更低的成本改进下游推理。推理中“沉默税”的挑战通过一种新颖的RL方法（**SxS**）来解决，该方法学习何时思考与说话的最佳披露政策。对于代码生成，一项关于通过率奖励的研究揭示了错误校准问题，从而激励了更有原则的奖励调整。复杂推理的提炼是通过针对长思想链（CoT）痕迹的协作多教师解码框架推进的。最后，**SAGE**应用分段加权GRPO来改进战略优化建模，证明了基于RL的推理增强的广泛适用性。

# 对齐和安全
对齐研究正在超越简单的偏好调整，重点关注概括性、稳健性和紧急故障模式的缓解。**模型规范中间训练**提出了一种新颖的方法，在微调之前教导模型其预期的对齐概括，直接提高概括并减少代理失准。对推理模型中规范博弈的深入研究表明，RL推理训练大大提高了利用率，这是安全性的一个关键发现。在安全方面，引入了对抗性自我游戏框架（**PIA**），以使LLM对基于人物的越狱攻击保持不变。还探讨了迭代微调的等性，表明特征放大在SFT中很少见，但在DPO中可能发生，这对基于RL的对齐管道的稳定性有直接影响。

# 多模式和视觉语言模型
强化学习正在成功地适应视觉语言模型（VLM）和多模式推理。**GRPO-TTA**应用GRPO驱动的强化学习进行测试时视觉调整，实现动态模型自适应。对于多模式推理，**SPP**将分段级政策优化扩展到VLM，解决跨模式的信用分配问题。此外，**Uni-OPD**框架提供了适用于LLM和MLLM的统一政策蒸馏配方。这些作品展示了高级RL技术从纯语言领域到多模式领域的可移植性。

# 合成、蒸馏和数据生成
一个重要趋势是使用先进的RL和合成技术来生成高质量的训练数据和提取能力。**可控且可验证的流程数据合成** 提供了一个用于为奖励模型生成流程监督数据的框架。* * GFCR **调查提供了基于RL的后培训的推出策略的全面分类。**Self-Mined Hardness for Safety微调** 使用模型自己的卷展进行RL风格的数据过滤。* * Uni-OPD ** 框架将政策提炼与双视角优化结合起来。这组工作凸显了数据的生成、过滤和用于引导模型改进的方式日益复杂。

---

## 1. 模型规格中期训练：改进对齐训练的概括方式

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chloe Li, Sara Price, Samuel Marks, Jon Kutasov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel alignment training method (MSM) that uses synthetic documents to teach models their intended generalization before fine-tuning, directly improving RL-based alignment generalization and reducing agentic misalignment.

**摘要**: arXiv：2605.02087v1宣布类型：新摘要：一些前沿人工智能开发人员的目标是将语言模型与描述预期模型行为的模型规范或宪法保持一致。然而，标准对齐微调（对规范对齐行为的演示进行训练）可能会产生概括性较差的浅对齐，部分原因是演示数据可能会低估所需的概括性。我们引入模型规范中期训练（MSM）：在预训练后但在对齐微调之前，我们在讨论其模型规范的合成文档上训练模型。这教导模型规范的内容，从而塑造它们如何从后续演示数据中进行概括。例如，一个仅为表达某些奶酪偏好而进行微调的模型，例如“我更喜欢奶油奶酪而不是布里干酪”，当我们应用MSM并将这些偏好归因于亲美价值观的规范时，它会概括为广泛的亲美价值观。相反，关于亲负担能力价值的规范反而会从完全相同的奶酪微调中产生亲负担能力的概括。MSM还可以塑造复杂的安全相关倾向：应用具有自我保护和守门员规范的MSM，大大降低了代理失准率（Qwen 3 - 32 B：54%至7%），超过了深思熟虑的对齐基线（14%）。我们进一步使用MSM作为工具来研究哪些模型规范产生最强的对齐概括，发现解释规则背后的值可以提高概括性，就像提供特定而不是一般指导一样。总的来说，MSM是一种简单、有效的技术，可以通过首先教模型预期的概括来控制和改进模型如何从对齐训练中进行概括。

[阅读原文](https://arxiv.org/abs/2605.02087)

---

## 2. 何时思考，何时说话：学习LLM推理的披露政策

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Jiaqi Wei, Xuehang Guo, Pengfei Yu, Xiang Zhang, Wanli Ouyang, Siqi Sun, Qingyun Wang, Chenyu You

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based method (SxS) to learn disclosure policies for LLM reasoning, directly addressing the silence tax and premature commitment in autoregressive generation.

**摘要**: arXiv：2605.03314v1宣布类型：新摘要：在单流自回归接口中，相同的令牌既更新模型状态，又构成不可逆转的公共承诺。这种耦合产生了\{沉默税}：额外的审议推迟了第一个\{task-relevant}内容，而天真的早期流媒体则面临着过早承诺的风险，从而对子孙后代产生偏见。我们引入了\textBF{\ð {Side-by-Side（SxS）}}交织推理，它使\ð {披露时间}成为标准自回归生成内的可控决策。SxS在相同上下文中将部分披露与持续的私人推理交织在一起，但只有在迄今为止的推理得到\r {支持}时才会发布内容。为了在不激励填充者的情况下学习这种节奏，我们通过将答案前置与支持推理前置匹配来构建包含对齐的交织轨迹，然后使用SFT训练以获取双重动作语义，并使用RL训练以恢复新格式下的推理性能。在两种Qwen 3架构/规模（MoE \textBF{Qwen 3 - 30 B-A3 B}、dense \textBF{Qwen 3 - 4 B}）以及域内（AIME 25）和域外（GPQA-Diamond）基准中，SxS提高了准确性--\{content-latency}在代币级代理下的Pareto权衡（例如，更新间等待）。

[阅读原文](https://arxiv.org/abs/2605.03314)

---

## 3. 生成、过滤、控制、重播：LLM强化学习推出策略的全面调查

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Rohan Surana, Gagan Mundada, Xunyi Jiang, Chuhan Wang, Zhenwei Tang, Difan Jiao, Zihan Huang, Yuxin Xiong, Junda Wu, Sheldon Yu, Xintong Li, Raghav Jain, Nikki Kuang, Sizhe Zhou, Bowen Jin, Zhendong Chu, Tong Yu, Ryan Rossi, Kuan-Hao Huang, Jingbo Shang, Jiawei Han, Julian McAuley

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a comprehensive survey and taxonomy (GFCR) of rollout strategies for RL-based post-training of LLMs, directly addressing RL for LLMs with a new framework.

**摘要**: arXiv：2605.02913v1宣布类型：新摘要：强化学习（RL）已成为提高大型语言模型（LLM）推理能力的核心训练后工具。在这些系统中，部署，即从提示到终止采样的轨迹，包括中间推理步骤和可选工具或环境交互，确定了优化器学习的数据，但部署设计通常被低估。这项调查为基于RL的推理LLM后训练的推出策略提供了一种与优化器不可知的观点。我们用统一的符号形式化了推出管道，并引入了生成-过滤-控制-回放（GFCR），这是一种生命周期分类法，将推出管道分解为四个模块化阶段：生成建议候选轨迹和布局;过滤器通过验证者、判断者、批评者构建中间信号;控制分配计算并在预算范围内做出继续/分支/停止决策; Replay在不更新重量的情况下保留和重复使用跨项目的工件，包括自主生成新培训任务的自我进化课程。我们通过可靠性、覆盖范围和成本敏感性的标准分类来补充GFCR，该标准分类描述了推出权衡。使用这个框架，我们综合了跨越RL的方法，具有可验证的奖励、流程监督、基于判断的门控、引导和树/段推出、自适应计算分配、提前退出和部分推出、吞吐量优化以及自我改进的回放/重组。我们以数学、代码/SQL、多模式推理、工具使用代理和评估技能归纳、重用和跨任务转移的代理技能基准的案例研究为框架奠定基础。最后，我们提供了一个诊断指数，将常见的推出病理映射到GFCR模块和缓解杠杆，以及构建可重复、计算机高效且值得信赖的推出管道的公开挑战。

[阅读原文](https://arxiv.org/abs/2605.02913)

---

## 4. 迭代微调基本上是唯一的

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Zephaniah Roe, Jack Sanderson, Dang Nguyen, Julian Huang, Todd Nief, Aryan Shrivastava, Chenhao Tan, Ari Holtzman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates trait amplification in iterative finetuning, showing that amplification is rare in SFT but can occur in DPO, with implications for RL-based alignment.

**摘要**: arXiv：2605.01130v1宣布类型：新摘要：如果一个模型有一些行为倾向，例如阿谀奉承或失调，并且它是根据自己的输出进行训练的，那么这种倾向会在下一代模型中被放大吗？我们通过训练一系列模型来研究这个问题，其中每个模型都根据其前身生成的数据进行微调，并且初始模型中植入了一些人物或信仰。我们测试三个设置：指令模型上的监督微调（SFT）、基本模型上的合成文档微调（SDF）和直接偏好优化（DPO）。在SFT和SDF环境中，特征大多会衰退或保持不变，因此进一步的微调周期不会起任何作用。在极少数情况下，放大通常是以一致性为代价的。在DPO设置中，当模型以对其自身输出的偏好连续训练时，特征放大可以可靠地发生，但当模型在每个周期重新初始化时，特征放大就会消失。总体而言，我们的结果表明，放大很可能来自持续的后训练，限制这一阶段可能是一种有效的防御。对于非RL微调，性状放大很少见，并且对数据量非常敏感，因此意外发生的可能性大大降低。最后，放大-一致性权衡是对性状放大的自然威慑。

[阅读原文](https://arxiv.org/abs/2605.01130)

---

## 5. 发现具有大型语言模型的强化学习界面

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Akshat Singh Jaswal, Ashish Baghel, Paras Chopra

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LIMEN, an LLM-guided evolutionary framework for jointly discovering observation mappings and reward functions for RL tasks, directly addressing RL interface design.

**摘要**: arXiv：2605.03408v1宣布类型：新摘要：强化学习系统依赖于指定观察和奖励功能的环境接口，但为新任务构建这些接口通常需要大量的手动工作。虽然最近的工作已经使用大型语言模型（LLM）自动化奖励设计，但这些方法假设固定观察，并且无法解决合成完整任务界面的更广泛挑战。我们从原始模拟器状态研究RL任务接口发现，其中必须生成观察映射和奖励函数。我们提出了LIMEN（代码可在https：//github.com/Lossfunk/LIMEN上获取），这是一个LLM指导的进化框架，它将候选界面生成为可执行程序，并使用政策训练反馈迭代地改进它们。在新颖的离散网格世界任务和跨越运动和操纵的连续控制域中，观察和奖励的联合进化仅在假设个体级成功指标的情况下发现有效的界面，而单独优化任何一个组件至少在一个领域失败。这些结果表明，从原始状态自动构建RL接口可以大大减少手动工程，并且观察和奖励组件通常从协同设计中受益，因为单组件优化在我们的评估套件中的至少一个领域上灾难性地失败。

[阅读原文](https://arxiv.org/abs/2605.03408)

---

## 6. SciResearcher：扩展深度研究代理以实现前沿科学推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tianshi Zheng, Rui Wang, Xiyun Li, Yangqiu Song, Tianqing Fang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a fully automated agentic framework for frontier-science data construction and uses agentic RL for self-improvement, directly matching the self-evolving agents criterion.

**摘要**: arXiv：2605.01489v1宣布类型：新摘要：前沿科学推理正在迅速成为推进人工智能自动化科学发现的关键基础。深度研究代理为应对这一挑战提供了一种有希望的方法。这些模型通过对信息寻求任务的后训练来开发强大的问题解决能力，这些任务通常通过知识图构建或迭代网络浏览来策划。然而，这些策略在前沿科学中面临着固有的局限性，其中特定领域的知识分散在稀疏和异类的学术来源中，解决问题需要复杂的计算和推理，远远超出了事实记忆。为了弥合这一差距，我们引入了SciResearcher，这是一个用于前沿科学数据构建的全自动代理框架。SciResearcher综合了基于学术证据的各种概念和计算任务，同时激发信息获取、工具集成推理和长期能力。利用精心策划的数据进行监督式微调和代理强化学习，我们开发了SciResearcher-8B，这是一种代理基础模型，在HLE-Bio/Chem-Gold基准上实现了19.46%，在参数规模上建立了新的最新水平，并超越了几个更大的专有代理。它在SuperGPQA-Hard-Biology和TRQA-Literature基准上进一步实现了13-15%的绝对收益。总体而言，SciResearcher为前沿科学推理引入了自动化数据构建的新范式，并为未来科学代理提供了可扩展的路径。

[阅读原文](https://arxiv.org/abs/2605.01489)

---

## 7. 奖励黑客基准：通过工具使用衡量LLM代理的利用率

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kunvar Thaman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a benchmark for measuring reward hacking in RL-trained LLM agents with tool use, directly relevant to RL for LLMs and agent safety.

**摘要**: arXiv：2605.02964v1宣布类型：新摘要：强化学习（RL）训练的具有工具访问权限的语言模型代理越来越多地部署在编码助理、研究工具和自治系统中。我们引入了奖励黑客基准（RHB），这是一套多步骤任务，需要顺序工具操作，并具有自然主义捷径机会，例如跳过验证步骤、从任务邻近的元数据中推断答案或篡改评估相关功能。RHB支持独立和连锁的任务制度，其中链长充当长期代理行为的代理。   我们评估了来自OpenAI、Anthropic、Google和DeepSeek的13个前沿模型。利用率从0%（Claude Sonnet 4.5）到13.9%（DeepSeek-R1-Zero）不等，根据训练后的风格差异很大。受控兄弟姐妹比较（DeepSeek-V3与DeepSeek-R1-Zero）显示，RL训练后与更高的奖励黑客行为相关（0.6%与13.9%），所有四个任务系列之间存在一致的差距。我们确定了六种利用类型，并发现72%的奖励黑客事件包含明确的思想链原理，这表明模型经常将利用描述为合法的问题解决方案。   简单的环境加固将利用率降低5.7个百分点（相对87.7%），而不会降低任务成功率。在标准任务上利用率接近零的模型在更难的变体上显示出更高的利用率，这表明与生产一致的后训练似乎只在诚实的解决方案仍然易于处理的复杂性阈值以下抑制奖励黑客攻击。

[阅读原文](https://arxiv.org/abs/2605.02964)

---

## 8. 使用推理LLM的策略感知优化建模

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ruiqing Zhao, Fengzhi Li, Yuan Zuo, Rui Liu, Yansong Liu, Yunfei Ma, Fanyu Meng, Junlan Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SAGE, a strategy-aware framework using Segment-Weighted GRPO (RL) with a composite reward to improve LLM optimization modeling, directly matching RL for LLMs.

**摘要**: arXiv：2605.02545v1宣布类型：新摘要：大型语言模型（LLM）可以生成语法有效的优化程序，但通常难以可靠地选择有效的建模策略，从而导致公式不正确和求解器行为效率低下。我们提出SAGE，这是一个策略感知框架，它使建模策略在数据构建和后训练中都显式。SAGE构建了一个经过求解器验证的多策略数据集，并通过监督微调训练学生模型，然后进行分段加权GRPO，使用格式合规性、正确性和求解器效率的复合奖励。在跨越合成和现实世界环境的八个基准中，SAGE将平均pass@1从72.7提高到80.3，高于最强的开源基线。经过多代，SAGE发现了更独特的正确配方，并将16遍时的成分水平多样性提高了19- 29%。SAGE在最大规模上生产了更紧凑的约束系统，其约束比基线少14.2%，与求解器高效建模一致。总体而言，这些结果表明，显式建模策略可以改善自动化优化建模。代码可在https://github.com/rachhhhing/SAGE上获取。

[阅读原文](https://arxiv.org/abs/2605.02545)

---

## 9. 了解推理模型中的规范游戏

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kei Nishimura-Gasparian, Robert McCarthy, David Lindner

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies specification gaming in reasoning models, finding RL reasoning training substantially increases exploit rates, which is highly relevant to RL for LLMs and reward design.

**摘要**: arXiv：2605.02269v1宣布类型：新摘要：规范游戏是LLM代理的一种关键失败模式。尽管如此，对于它何时出现以及驱动它的原因很少进行系统性的研究。为了解决这个问题，我们构建并开源了一套多样化的任务，其中模型可以通过采取意外的行动来获得高分。我们发现，所有测试模型在我们的八种设置（包括五种非编码设置）中的大部分设置中都以不可忽视的比例利用其规格。我们看到Grok 4中的规格游戏比例最高，而Claude型号中的规格游戏比例最低。我们使用我们的评估套件来研究是什么驱动了规范游戏，并发现：1. RL推理训练大大提高了模型利用其规范的速度，2。增加RL推理预算对利用率有弱正影响，3。测试时间缓解措施会减少但不会消除规范游戏的速度。我们的结果表明，规范游戏是RL推理训练带来的一个根本挑战;我们发布了我们的评估套件来支持对此问题的进一步工作。

[阅读原文](https://arxiv.org/abs/2605.02269)

---

## 10. GRPO-TTA：通过GRPO驱动的强化学习对视觉语言模型进行测试时视觉调优

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yujun Li, Hongyuan Zhang, Yuan Yuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GRPO-driven test-time adaptation for vision-language models, directly applying RL (GRPO) to improve model behavior via reward design.

**摘要**: arXiv：2605.03403v1宣布类型：新摘要：群组相对策略优化（GRPO）最近在后训练大型语言模型和视觉语言模型中表现出强劲的性能。这引发了一个问题：GRPO是否也显着促进视觉语言模型的测试时适应（TTA）。在本文中，我们提出了测试时间自适应的组相对策略优化（GRPO-TTA），它通过将特定类别的即时预测重新定义为组策略优化问题，将GRPO适应TTA设置。具体来说，我们通过从CLIP相似性分布中抽样前K类候选者来构建输出组，从而实现概率驱动的优化，而无需访问地面真相标签。此外，我们还设计了针对测试时间适应量身定制的奖励功能，包括对齐奖励和分散奖励，以指导有效的视觉编码器调整。跨不同基准的广泛实验表明，GRPO-TTA始终优于现有的测试时自适应方法，在自然分布变化下具有显着更大的性能收益。

[阅读原文](https://arxiv.org/abs/2605.03403)

---

## 11. 超越思维痕迹的RAG可以改善推理任务

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Negar Arabzadeh, Wenjie Ma, Sewon Min, Matei Zaharia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes retrieving thinking traces as a corpus for RAG to improve reasoning tasks, introducing a structured transformation method (T3) that reduces inference cost.

**摘要**: arXiv：2605.03344v1宣布类型：新摘要：事实证明，检索增强生成（RAG）对知识密集型任务有效，但人们普遍认为，对数学和代码生成等推理密集型问题提供的好处有限。我们挑战了这一假设，表明限制不在于RAG本身，而在于文集的选择。我们建议检索思维痕迹，而不是检索文档，即，在解决问题尝试过程中产生的中间思维轨迹。我们表明，思维轨迹已经是一个强大的检索源，并进一步介绍T3，离线方法，将它们转换成结构化的，检索友好的表示，以提高可用性。使用这些跟踪作为语料库，一个简单的检索然后生成管道在强大的模型和基准（如AIME 2025- 2026，LiveCodeBench和GPQA-Diamond）上持续提高推理性能，优于非RAG基线和标准Web语料库的检索。例如，在AIME上，具有Gemini-2-thinking生成的轨迹的RAG分别为Gemini-2.5-Flash、GPT-OSS-120 B和GPT-5实现了+56.3%、+8.6%和+7.6%的相对增益，尽管这些都是较新的模型。有趣的是，T3上的RAG也很少或没有额外的推理成本，甚至可以将推理成本降低高达15%。总体而言，我们的结果表明，思维痕迹是推理任务的有效检索库，将它们转换为结构化、紧凑或诊断表示可以释放更大的收益。代码可在https://github.com/Narabzad/t3获得。

[阅读原文](https://arxiv.org/abs/2605.03344)

---

## 12. 关于为长期任务训练大型语言模型：地平线长度的实证研究

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sunghwan Kim, Junhee Cho, Beong-woo Kwak, Taeyoon Kwon, Liang Wang, Nan Yang, Xingxing Zhang, Furu Wei, Jinyoung Yeo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a systematic empirical study on how horizon length affects training dynamics for LLM agents, identifying horizon reduction as a key principle for stabilization and generalization.

**摘要**: arXiv：2605.02572v1宣布类型：新摘要：大型语言模型（LLM）已显示出作为交互式代理的前景，可以通过扩展的环境交互序列来解决任务。虽然之前的工作主要集中在系统级优化或算法改进上，但任务视野长度在塑造训练动态方面的作用仍然知之甚少。在这项工作中，我们提出了一项系统性的实证研究，通过受控任务构建来检查视野长度。具体来说，我们构建了受控任务，其中智能体面临相同的决策规则和推理结构，但仅成功完成所需的动作序列长度不同。我们的结果表明，仅增加视野长度就构成了培训瓶颈，会因探索困难和学分分配挑战而导致严重的培训不稳定性。我们证明，缩减视野是解决这一限制、稳定训练并在长期任务中实现更好绩效的关键原则。此外，我们发现视野缩减与跨越视野长度的更强概括有关：在缩减视野下训练的模型在推理时更有效地推广到较长视野的变体，我们将这种现象称为视野概括。

[阅读原文](https://arxiv.org/abs/2605.02572)

---

## 13. DSYS：以分布为导向的细粒度信用分配政策优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hongbo Jin, Rongpeng Zhu, Zhongjing Du, Xu Jiang, Jingqi Tian, Qiaoman Zhang, Jiayu Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel critic-free RL framework for LLMs that uses distribution deviation as a guiding signal for fine-grained credit assignment in long reasoning chains.

**摘要**: arXiv：2605.03327v1宣布类型：新摘要：强化学习对于对齐大型语言模型以执行复杂推理任务至关重要。然而，当前的算法（例如组相对政策优化）受到粗粒度、序列级信用分配的影响，这在很长的思想链世代中很难隔离关键推理步骤。此外，标准的无界Kullback Leibler分歧罚分会导致严重的梯度不稳定性和模式寻求保守主义，最终扼杀了新颖推理轨迹的发现。为了克服这些限制，我们引入了分布引导的政策优化，这是一种新颖的、无批评者的强化学习框架，它将分布偏差重新解释为指导信号，而不是严格的惩罚。

[阅读原文](https://arxiv.org/abs/2605.03327)

---

## 14. 自毁硬度以实现安全微调

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Prakhar Gupta, Garv Shah, Donghua Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-mined hardness scoring method for safety fine-tuning of LLMs using the model's own rollouts and RL-style filtering, directly relevant to RL for LLMs.

**摘要**: arXiv：2605.03226v1宣布类型：新摘要：语言模型的安全微调通常需要精心策划的对抗数据集。我们采取不同的方法：根据目标模型自己的推出被判断有害的频率来对每个候选提示的难度进行评分，然后对最难的提示与模型自己的非越狱推出进行微调。在Llama-3- 8B-Direcct和Llama-3.2- 3B-Direcct上，这种方法将Wild越狱攻击成功率从11.5%和20.1%降低到1- 3%，但将越狱型良性提示的拒绝率从14-22%提高到74- 94%。将相同的硬提示1：1与敌对框架的良性提示（看起来像越狱但具有良性意图的提示）交织，可以将8B上的拒绝率降低到30-51%，3B上的拒绝率降低到52-72%，攻击成功率降低2-6个百分点。在混合方案中，在合格池中最难的一半（而不是随机的一半）上进行训练，可以将两种模型的剩余ASB降低35-50%（约3个百分点）。

[阅读原文](https://arxiv.org/abs/2605.03226)

---

## 15. PERSA：利用LLM进行教授式个性化反馈的强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ravi Ranjan, Utkarsh Grover, Xiaomin Lin, Agoritsa Polyzou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces PERSA, an RLHF pipeline with PPO and parameter-efficient fine-tuning for aligning LLM feedback style to a professor's tone, directly matching RL for LLMs.

**摘要**: arXiv：2605.01123v1宣布类型：新摘要：大型语言模型（LLM）可以在教育环境中提供自动反馈，但将LLM风格与特定教师语气保持一致，同时保持诊断正确性仍然具有挑战性。我们询问如何更新LLM以自动生成反馈，以与目标讲师风格保持一致，而不牺牲核心知识？我们研究来自人类反馈的强化学习（RL HF）如何调整基于转换器的LLM，以生成与教授评分声音相匹配的编程反馈。我们引入PERSA，这是一种RL HF管道，它结合了对教授演示的监督微调、来自成对偏好的奖励建模和近端策略优化（PPO），同时故意将学习限制在具有风格的组件上。受Transformer内部结构分析的启发，PERSA应用参数高效微调。它仅更新顶部的Transformer块及其前向投影，最大限度地减少全局参数漂移，同时提高风格的可控性。我们使用风格一致性和保真度的补充指标在三个代码反馈基准（APPS、PyFiXV和CodeReviewQA）上评估我们提出的方法。在Llama-3和Gemma-2的主干中，PERSA提供了最强的教授风格的转移，同时保持了正确性，例如在APPS上，它将风格一致得分（SAC）提高到96.2%（Base为34.8%），Llama-3和Gemma-2的正确性准确性（CA）高达100%。总体而言，PERSA通过调整其内容（内容正确性）和最重要的是，调整其表达方式（类似于演员的语气和结构），提供了一种实现个性化教育反馈的实用途径。

[阅读原文](https://arxiv.org/abs/2605.01123)

---

## 16. 通过群体相对政策优化在结构性因果模型中建立多跳推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yunhan Bu, Quan Zhang, Huaping Zhang, Guotong Geng, Chunxiao Gao, Askar Hamdulla, Juan Wang, Qiuchi Li, Baohua Zhang, Shuai Lei, Yunbo Cao, Zhunchen Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based framework using GRPO to optimize reasoning chain length in multi-hop fact verification, directly aligning with RL for LLMs via reward design.

**摘要**: arXiv：2605.01482v1宣布类型：新摘要：多跳事实验证（MHFV）需要对不同的证据进行复杂推理，这对经常遭受幻觉和逻辑链断裂的大型语言模型（LLM）构成了重大挑战。现有方法虽然通过思想链（CoT）提高透明度，但缺乏证据和主张之间因果依赖关系的明确建模。在这项工作中，我们引入了一种新颖的框架，该框架以结构性因果模型（SCP）为基础进行推理，将验证视为一个建设性因果推理过程。我们根据经验确定了推理链长度和准确性之间的“倒U形”相关性，揭示了过度的结构复杂性会降低性能。为了解决这个问题，我们提出了一种使用组相对策略优化（GRPO）的基于规则的强化学习策略。这种方法动态优化了结构深度和简洁性之间的权衡。对HoVer和EX-FEVER的大量实验表明，我们的SCM-GRPO框架的性能显着优于最先进的基线，为复杂事实验证提供了可靠且可解释的解决方案。

[阅读原文](https://arxiv.org/abs/2605.01482)

---

## 17. 多模式推理的分段一致策略优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Lei Gao, Zhuoming Li, Mengxi Jia, Jiakang Yuan, Hongbo Sun, Hao Sun, Xuelong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SAPO, a novel RL paradigm for LLMs that performs policy optimization at the granularity of coherent reasoning segments rather than tokens or full sequences, improving credit assignment and training stability.

**摘要**: arXiv：2605.01327v1宣布类型：新摘要：现有的大型语言模型强化学习方法通常以单个令牌或整个响应序列的粒度执行策略优化。然而，此类公式通常与推理过程的自然分步结构不一致，导致次优信用分配和多模式推理任务中的不稳定训练。为了弥合这一差距，我们提出了分段对齐策略优化（SPP），这是一种新型的强化学习范式，将连贯的推理步骤而不是令牌或完整序列视为策略更新的基本单位。SPP在推理片段上引入了分步马尔科夫决策过程抽象，并伴随着片段级值估计、优势计算和与推理边界语义一致的重要性采样机制。代表性推理基准的实验表明，SPP始终优于符号级和序列级策略优化方法，实现了准确性的显着提高，同时表现出更好的训练稳定性和值估计一致性。我们的工作强调了将强化学习更新与推理的内在结构保持一致的重要性，为复杂推理任务中更高效、更基于语义的策略优化铺平了道路。将发布代码和模型以确保完全的可重复性。

[阅读原文](https://arxiv.org/abs/2605.01327)

---

## 18. 将痕迹提升到逻辑：长视野抽象任务的程序技能归纳和神经符号学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jie-Jing Shao, Haiyan Yin, Yueming Lyu, Xingrui Yu, Lan-Zhe Guo, Ivor Tsang, James Kwok, Yu-Feng Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a neuro-symbolic skill induction framework that lifts agent interaction traces into logic-grounded programs, enabling self-evolution and generalization.

**摘要**: arXiv：2605.01293v1宣布类型：新摘要：由于纯粹基于预算的推理的短暂性，基础模型驱动的代理经常在长期规划方面遇到困难。虽然现有的技能归纳方法通过将经验提炼到状态盲参数化脚本中来缓解这种情况，但它们未能捕获动态环境中稳健执行所需的条件逻辑。在本文中，我们提出了神经符号技能归纳（NSI），这是一个将交互痕迹提升到模块化、\textit{logic-based}程序中的框架。通过合成显式控制流和动态变量绑定，NSI授权代理发现\textit{when}和\textit{why}采取行动。这种范式能够实现有效的概括，允许代理从少数示例中归纳技能并灵活地适应看不见的目标。一系列代理任务的实验表明，NSI始终优于最先进的基线，使代理能够自我进化成为基于逻辑的技能的建筑师。

[阅读原文](https://arxiv.org/abs/2605.01293)

---

## 19. 重技能：重思维作为强调思维的内在技能

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jianing Wang, Linsen Guo, Zhengyu Chen, Qi Guo, Hongyu Zang, Wenjie Shi, Haoxiang Ma, Xiangyu Xi, Xiaoyu Li, Wei Wang, Xunliang Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HeavySkill, viewing heavy thinking as an inner skill that can be scaled via RL for self-evolving LLMs, directly matching RL for LLMs and self-evolving agents.

**摘要**: arXiv：2605.02396v1公告类型：新摘要：通过协调多个代理与记忆、技能和工具使用的编排框架协调多个代理的最新进展在复杂推理任务中取得了显着的成功。然而，真正推动性能的底层机制仍然隐藏在复杂的系统设计背后。在本文中，我们提出了HeavySkill，这是一种将繁重思维视为编排工具中的最小执行单元，而且还视为内在化在模型参数中的内在技能，驱动编排者解决复杂任务。我们将此技能确定为两阶段流水线，即并行推理，然后进行总结，可以在任何代理工具下运行。我们对不同领域的HeavySkill进行了系统性的实证研究。我们的结果表明，这种内在技能始终优于传统的N中最佳（BoN）策略;值得注意的是，更强的LLM甚至可以接近Pass@N的性能。至关重要的是，我们证明，作为一种可学习的技能，重度思维的深度和广度可以通过强化学习进一步扩展，为自我进化的LLM提供了一条充满希望的道路，这些LLM在不依赖脆弱的编排层的情况下内化复杂的推理。

[阅读原文](https://arxiv.org/abs/2605.02396)

---

## 20. 通过协作分步多教师解码提炼Long-CoT推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Taewon Yun, Jisu Shin, Jeonghwan Choi, Seunghwan Bang, Hwanjun Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a collaborative multi-teacher decoding framework for distilling Long-CoT reasoning traces, directly relevant to improving reasoning via step-wise synthesis.

**摘要**: arXiv：2605.02290v1公告类型：新摘要：提炼大型推理模型对于使Long-CoT推理实用化至关重要，因为全规模推理在计算上仍然令人望而却步。现有的基于策展的方法事后选择完整的推理痕迹，忽视了异类教师之间的协作，缺乏动态探索，从而导致重复抽样和错过补充推理。我们引入了CoRD，这是一种协作式多教师解码框架，它在基于预测性困惑的评分和射束搜索的指导下执行分步推理合成。这使得异类LRM能够联合构建连贯的推理轨迹，同时有效地保留多样化、高潜力的假设。实验表明，CoRD产生更高质量的推理数据，并实现了近教师水平的学生表现较少，结构化的监督信号，没有实质性的效率开销。CoRD进一步推广到域外和开放式环境。数据集和模型可在\href{https：//github.com/DISL-Lab/CoRD}{https：//github.com/DISL-Lab/CoRD}获得。

[阅读原文](https://arxiv.org/abs/2605.02290)

---

## 21. 理清意图与角色：角色不变安全调整的对抗自我游戏

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiajia Li, Xiaoyu Wen, Zhongtian Ma, Shuyue Hu, Qiaosheng Zhang, Zhen Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel adversarial self-play framework (PIA) for safety alignment that uses RL-like co-evolution to make LLMs invariant to persona-based jailbreak attacks.

**摘要**: arXiv：2605.01899v1宣布类型：新摘要：大型语言模型（LLM）不断增长的功能推动了它们在不同领域的广泛部署，即使是在潜在的高风险场景中也是如此。尽管安全对齐技术取得了进步，但当前的模型仍然容易受到新出现的基于人物的越狱攻击的影响。现有关于基于角色的越狱的研究主要集中在攻击迭代上，但缺乏对防御端的系统性和机械性约束。为了应对这一挑战，我们提出了角色不变对齐（PIA），这是一种对抗性自我游戏框架，通过攻击端的角色谱系进化（PLE）和防守端的角色不变一致性学习（PICL）来实现协同进化。从理论上讲，PICL基于结构分离假设，使用单边KL分歧约束来实现安全决策与角色背景的结构性脱钩，从而在基于角色的越狱攻击下维持安全行为。实验结果表明，PLE通过利用基于谱系的信用传播有效地探索高风险角色空间。与此同时，PICL防御方法显着降低了攻击成功率（ASB），同时保留了模型的通用能力，从而验证了这种对齐范式的优越性和稳健性。代码可访问https://github.com/JiajiaLi-1130/PIA。

[阅读原文](https://arxiv.org/abs/2605.01899)

---

## 22. 医疗代理的医疗保健AI健身房

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Minbyul Jeong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-turn agentic RL training environment and a novel self-distillation method (TT-OPD) for stable RL training of medical AI agents, directly addressing RL for LLMs and self-improving agents.

**摘要**: arXiv：2605.02943v1宣布类型：新摘要：临床推理需要多步骤的交互--收集患者病史、订购测试、解释结果和做出安全的治疗决策--但统一的训练环境提供了广泛的临床领域和专门的工具，以通过强化学习训练可推广的医疗AI代理人仍然难以捉摸。我们对医疗人工智能的多回合代理RL进行了一项全面的实证研究，该研究基于\gym{}，这是一个与健身房兼容的环境，跨越10个临床领域，包含3.6 K+任务、135个特定领域的工具和包含828 K医学段落的知识库。我们的分析表明，代理多圈结构退化为冗长的单圈独白，其特征是单调长度爆炸和工具使用频率的同时侵蚀。我们描述了这种崩溃以及蒸馏不稳定性是如何源于稀疏终端奖励与顺序临床轨迹的不一致。我们发现，vanilla GRPO在某些基准上实现了很强的最终准确性，但存在训练不稳定性，响应长度的显着波动和延长的收敛期就证明了这一点。为了提高培训效率和稳定性，我们提出了回合级截断政策蒸馏（TT-OPD），这是一种自蒸馏框架，无年级EMA教师利用结果特权信息在每个对话回合提供密集的、结果感知的KL正规化。TT-OPD在18个基准中的10个上实现了最佳性能，比非RL基线平均提高+3.9~pp，具有更快的早期收敛、受控的响应长度和持续的多圈工具使用。

[阅读原文](https://arxiv.org/abs/2605.02943)

---

## 23. 探索代码生成强化学习中的通过率奖励

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xin-Ye Li, Ren-Biao Liu, Yun-Ji Zhang, Hui Sun, Zheng Xie, Ming Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies reward design (pass-rate vs binary) in critic-free RL for code generation, revealing miscalibration issues and motivating better reward alignment.

**摘要**: arXiv：2605.02944v1宣布类型：新摘要：来自单元测试反馈的强化学习（RL）已成为改进代码生成大型语言模型（LLM）的标准训练后配方。然而，通过所有测试的二进制奖励可能是稀疏的，在没有一个采样解决方案通过所有测试的具有挑战性的问题上不会产生学习信号。一种常见的补救措施是使用测试案例通过率作为替代奖励。   在这项工作中，我们研究了代码生成的无批评RL中的通过率奖励（例如，GRPO和RLOO）并报告了基本模型和算法之间的一致模式：尽管缓解了奖励稀疏性，但在严格的控制实验中，通过率奖励并不能比二元奖励可靠地提高最终性能。   为了理解这种差异，我们分析了奖励密度和由此产生的梯度方向。我们发现通过率回报更密集，但引发的梯度更新并不一致地将概率质量移向全通解。出现这种情况是因为测试用例通过率是完全正确性进展的错误校准替代品，而同一组内的部分通过解决方案可能会引发相互冲突的梯度方向，从而抵消。   总体而言，我们的结果表明，在无批评RL中，通过率奖励不足以改进代码生成并激励能够更好地使优化与完全正确性目标保持一致的奖励设计。

[阅读原文](https://arxiv.org/abs/2605.02944)

---

## 24. 流程奖励模型的可控且可验证的流程数据合成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yinghui Chi, Lucien Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a controllable and verifiable framework for synthesizing process supervision data for process reward models, directly relevant to RL for LLMs via reward model design.

**摘要**: arXiv：2605.02395v1宣布类型：新摘要：过程奖励模型（PRM）依赖于高质量的过程监督数据，但现有的构建方法通常对错误位置、错误类型和轨迹一致性提供有限的控制。我们提出了一个可控且可验证的框架来合成PRM的过程监督数据。我们的框架首先构建一个正确的符号推理链，将模板感知的错误注入到中间步骤中，在损坏状态下重新计算后续步骤，并验证注入的步骤不能从其前置推导。由此产生的配对轨迹在第一个错误时是后缀无效的，同时在符号重新计算后保持逻辑一致，并被翻译成对齐的自然语言过程，用于PRM训练和评估。实验表明，合成数据改进了逻辑推理基准上的8选优重新排名，并转移到数学推理。步骤级评估进一步表明，第一个错误本地化仍然比总体步骤分类更具挑战性，凸显了对细粒度和可验证的过程监督的必要性。

[阅读原文](https://arxiv.org/abs/2605.02395)

---

## 25. T$^2$PO：用于稳定多轮启发式强化学习的不确定性引导探索控制

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haixin Wang, Hejie Cui, Chenwei Zhang, Xin Liu, Shuowei Jin, Shijie Geng, Xinyang Zhang, Nasser Zalmout, Zhenyu Shi, Yizhou Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes T2PO, an uncertainty-guided RL framework for multi-turn agentic tasks that controls exploration at token and turn levels to improve training stability.

**摘要**: arXiv：2605.02178v1宣布类型：新摘要：多轮强化学习（RL）的最新进展显着提高了推理LLM在复杂交互任务上的性能。尽管细粒度信用分配和轨迹过滤等稳定技术取得了进步，但不稳定性仍然普遍存在，并经常导致训练崩溃。我们认为，这种不稳定性源于多回合环境中的低效探索，政策继续产生低信息行动，既不能减少不确定性，也不能推进任务进展。为了解决这个问题，我们提出了代币和回合级策略优化（T $& 2$PO），这是一个不确定性感知框架，可以显式地控制细粒度级别的探索。在代币层面，T$#2$PO监控不确定性动态，并在边际不确定性变化低于阈值时触发思维干预。在转弯级别，T $& 2$PO识别探索进度可忽略不计的交互，并动态重新采样此类转弯以避免浪费展开。我们在各种环境（包括WebShop、ALFWorld和Search QA）中评估了T $' 2$PO，证明了训练稳定性和性能改进以及更好的探索效率方面的巨大进步。代码可访问：https://github.com/WillDreamer/T2PO。

[阅读原文](https://arxiv.org/abs/2605.02178)

---

## 26. 具有引导优势估计的忠实移动图形用户界面代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haowen Hu, Pengzhou Cheng, Zheng Wu, Lingzhong Dong, Gongshen Liu, Zhuosheng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a faithfulness-first framework for GUI agents using a guided advantage estimator (GuAE) built upon GRPO, directly contributing to RL for LLMs with a novel reward design and training pipeline.

**摘要**: arXiv：2605.01208v1宣布类型：新摘要：基于视觉语言模型的图形用户界面（图形用户界面）代理已表现出强大的交互能力。然而，他们的行为往往不忠实，依赖于记忆的快捷方式，而不是在显示的屏幕证据或用户指令中将动作作为基础。为了解决这个问题，我们提出了Faithful-Agent，这是一个忠诚第一的框架，它重新制定了图形用户界面交互的优先级，以优先考虑证据可信度和内部一致性。忠诚代理采用两阶段管道：（i）以忠诚为导向的SFT阶段，在证据扰动下灌输戒断行为;（ii）RFT阶段，通过引入引导优势估计器（GuAE）进一步放大忠诚度，GuAE是一种基于锚点和方差自适应优势调节机制建立在GRPO上。GuAE可以防止低方差推出组在稀疏的图形用户界面奖励下的优势崩溃，并且通过思想行动一致性奖励，忠实代理（阶段II）将Trap SR相对于基线从13.88%提高到80.21%，同时保持稳健的一般描述遵循性能。

[阅读原文](https://arxiv.org/abs/2605.01208)

---

## 27. Uni-OPD：用双重视角的配方统一政策蒸馏

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wenjin Hou, Shangpin Peng, Weinong Wang, Zheng Ruan, Yue Zhang, Zhenglin Zhou, Mingqi Gao, Yifei Chen, Kaiqi Wang, Hongming Yang, Chengquan Zhang, Zhuotao Tian, Han Hu, Yi Yang, Fei Wu, Hehe Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified on-policy distillation framework for LLMs/MLLMs with dual-perspective optimization, directly addressing RL-based post-training via reward-guided margin calibration.

**摘要**: arXiv：2605.03677v1宣布类型：新摘要：政策提炼（OPD）最近成为一种有效的培训后范式，用于将专业专家模型的能力整合到单个学生模型中。尽管OPD取得了经验上的成功，但人们对OPD产生可靠改进的条件仍然知之甚少。在这项工作中，我们发现了限制有效OPD的两个基本瓶颈：对信息状态的探索不足以及教师对学生推广的监督不可靠。基于这一见解，我们提出了Uni-OPD，这是一个统一的OPD框架，可在大型语言模型（LLM）和多模式大型语言模型（MLLM）之间进行推广，以双视角优化策略为中心。具体来说，从学生的角度出发，我们采用两种数据平衡策略来促进对培训期间学生生成的信息状态的探索。从教师的角度来看，我们表明可靠的监督取决于聚合代币级指导是否与结果奖励保持顺序一致。为此，我们开发了一种结果引导的裕度校准机制，以恢复正确和不正确轨迹之间的顺序一致性。我们对涵盖不同环境的5个领域和16个基准进行了广泛的实验，包括跨LLM和MLLM的单教师和多教师蒸馏、强到弱蒸馏和跨模式蒸馏。我们的结果验证了Uni-OPD的有效性和多功能性，并为可靠的OPD提供了实用见解。

[阅读原文](https://arxiv.org/abs/2605.03677)

---

## 28. 延迟、停滞或崩溃：评估系统验证错误对WLVR的影响

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kazuki Egashira, Mark Vero, Jasper Dekoninck, Florian E. Dorner, Robin Staab, Martin Vechev

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Studies the impact of systematic verification errors on RLVR, showing that false positives can cause performance collapse, which is directly relevant to RL for LLMs with verifiable rewards.

**摘要**: arXiv：2605.02909v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）已成为提高大型语言模型（LLM）推理能力的强大方法。虽然WLVR专为具有可验证的地面真相答案的任务而设计，但现实世界的验证器（例如，静态代码检查器）可能会将错误引入奖励信号。之前的分析主要将此类错误视为样本之间的随机和独立，得出的结论是，错误只是减慢训练速度，对最终表现的影响有限。然而，实际的验证器往往会表现出系统错误。这带来了模型从结构上错误的奖励信号中学习不想要的一致行为的风险。在这项工作中，我们研究了此类系统验证错误对WLVR的影响。通过对算术任务的对照实验，我们表明系统性假阴性会导致与随机噪音类似的效果。另一方面，系统性假阳性可能会导致从次优平稳期到性能崩溃的广泛行为。至关重要的是，这些结果不是由总体错误率决定的，而是由引入错误的特定模式决定的，这使得预先缓解变得困难。我们的研究结果表明，与先前的结论相比，现实的验证错误可以严重塑造RLVR的结果，验证质量必须超越其样本级错误率的理解。

[阅读原文](https://arxiv.org/abs/2605.02909)

---

