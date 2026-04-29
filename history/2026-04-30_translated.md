# 💡 今日研究速览 (Daily Summary)

# LLM的RL
今天，大量论文突破了语言模型训练后强化学习的界限，超越了标准的WLHF和GRPO。一个主要主题是奖励设计和优化动态的形式化和处理。**预防性政策优化（FPO）**引入了一个框架，其中澄清和拒绝被视为认识控制行为，直接解决模型不确定性和风险敏感性对齐的微妙问题。作为补充，一篇理论论文将奖励错误归类为潜在良性或有益，为设计更稳健的奖励模型提供了基础视角。在优化方面，提出了**Tsallis损失连续体**来解决推理模型WLVR中的冷启动停滞问题，而**计算对齐训练** 重新定义了训练目标，以直接优化测试时推理策略。进一步的创新包括解释为什么RL比SFT更好地推广的特征级机制研究、一种基于强化学习的查询精炼器，用于从冻结模型中引出推理，以及RL在视频生成（通过GRPO）、跨语言RAG、图像编辑（具有可验证的检查列表）、表格数据清理和机器翻译中的新颖应用。最后，**RMiPO**引入了一种利用内在互信息的无超参数离线偏好优化方法，并提出了基于排名的奖励模型用于解释质量评估。

# 自我进化的代理与安全
自主代理改进的前沿得到了强烈的代表，重点关注闭环、自参考架构。**earth-Loop**提出了一个完全闭环的框架，用于任务和优化器代理的相互进化，实现纯粹的自我进化标准。类似地，** 自我合成推理协议（SSRP）**框架将元认知自我改进的规划和执行分开，而**抽象思维工程（AHE）**使用可观察性驱动的循环来自主进化编码代理利用。对于安全性，一篇特别著名的论文**从1位危险信号中发现统计安全规范** 提出了一个框架（EPO-Safe），使代理能够从稀疏反馈中自我发现和完善自己的安全规范，这是迈向稳健和可扩展代理安全的关键一步。最后，**ClawTrace**引入了一个具有成本意识的跟踪和蒸馏管道，用于从交互跟踪中高效改进代理技能。

# 潜在推理和推理时间缩放
一个明显的趋势是对潜在推理的深入探索，超越简单的思想链进入更复杂的架构和解码策略。**《终极动机》**通过引入潜在空间中错位推理的基准和检测方法，直接解决了连续思维模型的安全问题。在架构方面，**Nautile-370 M**提出了一种混合模型，将潜在光谱记忆与高效推理的注意力集成在一起。对于解码，** 探索性采样（ESamp）**使用轻量级蒸馏器来预测隐藏表示，并利用预测误差作为语义探索的新颖信号，提供了一种新的测试时间缩放方法。这还得到了**一个细化器来简化所有内容** 的进一步补充，它使用RL来训练查询细化器，该查询细化器在推理时从冻结的LLM中进行推理。

# 多模式和视频生成
多模式推理和生成的进步是由RL和新型潜在推理框架推动的。在视频生成中，提出了一个系统性的后训练框架，将RL HF与新型GRPO方法结合起来来优化扩散模型。对于图像编辑，**DDA-Thinker**引入了一个脱钩的双原子RL框架，该框架使用可验证的检查表来优化推理规划模块。**AVES-DPO**解决了大型视觉语言模型（LVLM）中的幻觉缓解问题，它使用基于共识的验证创建了一个自我纠正的偏好学习管道。最后，**The Thinking Pixel** 提出了一个用于直接在扩散模型潜在内进行潜在推理的循环稀疏专家混合框架，弥合了语言模型推理和生成性扩散过程之间的差距。

---

## 1. 别有用心：检测连续思维模型中的错位推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sharan Ramjee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a benchmark and method for detecting misaligned reasoning in continuous thought models, directly addressing safety in latent reasoning architectures.

**摘要**: arXiv：2604.23460v1宣布类型：新摘要：思想链（CoT）推理已成为在大型语言模型（LLM）中引发复杂推理的关键技术。尽管可以解释，但它对自然语言的依赖限制了模型的表达带宽。连续思维模型通过在潜在空间而不是人类可读的令牌中进行推理来解决这一瓶颈。虽然它们能够实现更丰富的表示和更快的推理，但它们提出了一个关键的安全问题：我们如何在无法解释的潜在空间中检测错位的推理？为了研究这一点，我们引入了MoralChain，这是一个包含12，000个社会场景的基准，具有平行的道德/不道德推理路径。我们使用一种新颖的双触发范式训练具有后门行为的连续思维模型--一个触发器武装错位的潜在推理（[T]），另一个触发器释放有害输出（[O]）。我们展示了三个发现：（1）连续思维模型可以在产生一致的输出的同时表现出不对齐的潜在推理，其中一致和不对齐的推理占据了潜在空间的几何不同区域;（2）在行为可区分的条件下训练的线性探针（[T][O] vs [O]）转移到检测武装但良性状态（[T] vs基线）具有高准确性;和（3）错位被编码在早期潜在思维标记中，这表明连续思维模型的安全监控应该针对潜在推理的“规划”阶段。

[阅读原文](https://arxiv.org/abs/2604.23460)

---

## 2. LLM的预防性政策优化：认知干预、风险敏感控制和反思性一致

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: James Pustejovsky, Nikhil Krishnaswamy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Frictive Policy Optimization (FPO), a novel RL framework for LLMs that treats clarification and refusal as epistemic control actions, directly addressing RL for LLMs with a new reward design and risk-sensitive control.

**摘要**: arXiv：2604.25136v1宣布类型：新摘要：我们提出了预防性政策优化（FPO），这是一个学习语言模型政策的框架，不仅规范说什么，还规范何时以及如何干预，以管理认识风险和规范风险。与优化表面偏好或任务效用的标准对齐方法不同，FPO将澄清、验证、挑战、重定向和拒绝视为显式控制动作，其目的是塑造信念、承诺和不确定性随着时间的推移的演变。我们将一致形式化为一个风险敏感的认识控制问题，其中干预决策是根据其对下游认识质量的预期影响而选择的，而不仅仅是直接回报。我们引入了摩擦干预的紧凑分类、可操作多种对齐失败模式的结构化摩擦函数，以及涵盖奖励塑造、偏好配对、群体相对排名和风险条件信任区域的统一FPO方法家族。我们进一步提出了一个评估框架，通过澄清行为、校准、矛盾修复、拒绝比例和信息效率直接衡量认识能力。总而言之，这些结果为学习代理提供了正式和算法基础，这些代理不仅在结果上一致，而且在认识行为上一致。

[阅读原文](https://arxiv.org/abs/2604.25136)

---

## 3. 土方循环：闭环自参考优化的相互进化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ziyang Liu, Xinyan Guo, Xuchen Wei, Han Hao, Liu Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a fully closed-loop self-referential optimization framework for mutual evolution of task and optimizer agents, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2604.23472v1宣布类型：新摘要：虽然最近的自主代理展现出令人印象深刻的能力，但它们主要依赖于手动脚本工作流程和手工制作的启发式方法，这从本质上限制了它们开放式改进的潜力。为了解决这个问题，我们提出了eightm-Loop，这是一个完全闭环框架，可以操作两个不同群体的相互进化：解决具体问题的任务代理，以及循环优化任务代理及其自身的优化器代理。为了维持这种自我参考的进化，我们提出了一种动态基准测试机制，该机制无缝地重复使用新生成的任务代理的经验分数作为相对输赢信号来更新优化器的分数。该机制利用任务代理的演变作为固有信号来驱动优化器的评估和细化，而无需额外的费用。对数学优化问题的经验评估表明，Earth-Loop有效地突破了静态基线的性能上限，在匹配计算下在所有评估任务中实现了最高的绝对峰值性能。值得注意的是，我们观察到优化器代理动态调整其策略以匹配高性能任务代理不断变化的需求，这解释了系统的持续改进和卓越的后期性能。

[阅读原文](https://arxiv.org/abs/2604.23472)

---

## 4. 模型应该多快地接受监督？察利斯损失连续体上的训练推理模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Chu-Cheng Lin, Eugene Ie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new loss family (Tsallis loss continuum) and two Monte Carlo estimators (GARL, PAFT) to address cold-start stalling in RLVR for reasoning models, directly contributing to RL for LLMs.

**摘要**: arXiv:2604.25907v1 Announce Type: new  Abstract: Adapting reasoning models to new tasks during post-training with only output-level supervision stalls under reinforcement learning from verifiable rewards (RLVR) when the initial success probability $p_0$ is small. Using the Tsallis $q$-logarithm, we define a loss family $J_Q$ that interpolates between RLVR (at $q{=}0$, the exploitation pole) and the log-marginal-likelihood over latent trajectories (at $q{=}1$, the density-estimation pole). All members share the same per-example gradient direction, differing only by a scalar amplification $P_{\theta^{-q}}$ that reweights each instance independently of the learning rate. This amplification is the mechanism that addresses cold-start stalling: under gradient flow, the exploitation pole requires $\Omega(\frac{1}{p_0})$ time to escape cold start, while the density-estimation pole escapes in $\Theta\big(\log(\frac{1}{p_0})\big)$; intermediate $q$ trades escape speed against noise memorization. Because $P_\theta$ is intractable, we derive two Monte Carlo estimators from the two factorizations of the gradient: Gradient-Amplified RL (GARL) samples from the prior and amplifies the RL gradient, and Posterior-Attenuated Fine-Tuning (PAFT) importance-resamples from the posterior and runs standard SFT. Both have bias $O\big(\frac{q}{M P_{\theta}^{q+1}}\big)$; GARL has lower variance, PAFT has semantically coherent gradients. On FinQA, HotPotQA, and MuSiQue, GARL at $q{=}0.75$ substantially mitigates cold-start stalling, escaping cold start where GRPO fails entirely. In warm start, GARL at low $q$ dominates FinQA where training is stable; on HotPotQA and MuSiQue, GARL destabilizes during training, and PAFT at $q{=}0.75$ provides stable gradients (best overall on HotPotQA at 47.9 maj@16, $+14.4$ over GRPO).

[阅读原文](https://arxiv.org/abs/2604.25907)

---

## 5. 强化学习为何具有普遍性？大型语言模型后训练的制造级机制研究

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Dan Shi, Zhuowen Han, Simon Ostermann, Renren Jin, Josef van Genabith, Deyi Xiong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a mechanistic feature-level analysis of why RL generalizes better than SFT in LLM post-training, directly addressing RL for LLMs.

**摘要**: arXiv：2604.25011v1宣布类型：新摘要：基于强化学习（RL）的后训练通常会提高训练域以外的大型语言模型（LLM）的推理性能，而监督微调（SFT）通常会导致一般能力遗忘。然而，这种对比背后的机制仍不清楚。为了弥合这一差距，我们提出了一种特征级机制分析方法来使用受控实验设置来探索RL推广，其中RL和SFT调整模型是在相同数据上从相同的基础模型训练的。利用我们的可解释性框架，我们在共享特征空间内调整模型之间的内部激活，并分析特征在训练后期间如何演变。我们发现，SFT迅速引入许多高度专业化的特征，这些特征在训练早期稳定，而RL则引发了更受约束且不断进化的特征变化，这些变化在很大程度上保留了基本模型的表示。我们专注于RL成功但基本模型失败的样本，识别出一组紧凑的、任务不可知的特征，这些特征直接调解不同任务之间的概括。设备级干预证实了它们的因果作用：禁用这些功能会显着降低RL模型的概括性能，而放大它们会提高基本模型的性能。该代码可在https://github.com/danshi777/RL-generalization上获取。

[阅读原文](https://arxiv.org/abs/2604.25011)

---

## 6. 通过潜在提取探索大型语言模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Yuanhao Zeng, Ao Lu, Lufei Li, Zheng Zhang, Yexin Li, Kan Ren

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Exploratory Sampling (ESamp), a novel decoding method that uses a lightweight distiller to predict hidden representations and uses prediction error as a novelty signal for semantic exploration, directly relevant to latent reasoning and test-time scaling.

**摘要**: arXiv：2604.24927v1宣布类型：新摘要：生成多样化的响应对于大型语言模型（LLM）的测试时扩展至关重要，但标准随机抽样大多会产生表面级别的词汇变化，从而限制了语义探索。在本文中，我们提出了探索性采样（ESamp），这是一种明确鼓励生成期间语义多样性的解码方法。ESamp的动机是一个众所周知的观察，即神经网络往往会对与以前遇到的类似的输入做出较低的错误预测，而对新的输入会产生较高的预测错误。基于这一属性，我们在测试时训练轻量级Distiller，从浅层表示预测LLM的深层隐藏表示，以对LLM的深度表示转换进行建模。在解码过程中，Distiller不断适应当前一代上下文引发的映射。ESamp使用预测误差作为新颖信号来重新加权以当前前置为条件的候选令牌扩展，从而将解码偏向探索较少的语义模式。ESamp通过一个同步训练-推理管道实现，最坏情况下的开销低于5%（优化版本中为1.2%）。经验结果表明，ESamp显着提高了推理模型的Pass@k效率，表现出优于强随机和启发式基线或相当的性能。值得注意的是，ESamp实现了数学、科学和代码生成基准的稳健概括，并打破了创意写作中多样性和一致性之间的权衡。我们的代码已在：https://github.com/LinesHogan/tLLM上发布。

[阅读原文](https://arxiv.org/abs/2604.24927)

---

## 7. 超越注意力稳定性边界：抽象的自我合成推理协议

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Dahlia Shehata, Ming Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a metacognitive framework (SSRP) for self-improving agents that separates planning and execution, directly addressing agent self-evolution and overcoming attention stability limits.

**摘要**: arXiv：2604.24512v1宣布类型：新摘要：随着LLM代理向自主数字同事过渡，在非线性多轮对话中保持确定性目标导向成为架构瓶颈。我们在仅限解码器的自回归变形金刚中识别并正式化了一种系统性故障模式，称为注意力闩锁。这种现象是信息过度挤压的行为表现，当历史上下文的累积概率权重超过任务中间更新时就会发生，导致代理人尽管有明确的相互矛盾的指令，但仍然固定在过时的约束中。我们提出了自我合成推理协议（SSRP），这是一种元认知框架，它实现了高级架构规划（Architect）和逐轮程序执行（Executive）之间的离散分离。我们使用MultiWOZ 2.2数据集和聚合轴准确度（APA）评估9 K轨迹的SSRP，这是一种新颖的指标，我们通过将其分数映射到U形“迷失在中间”曲线来验证。我们提出了3个实验层：基于浅层最近的检索试点、高熵SOP和语义劫持的3跳多事实合成任务。我们的结果通过经验确定了注意力稳定性边界，其中GPT 5.4的无状态Vanilla ReAct基线下降至0.1%成功率，而SSRP则实现了715 X的韧性提升。我们证明了Gemini 3.1 Pro、Claude Sonnet 4.6和DeepSeek V3.2在统计上取得了显着的进步。审计通过通过循环反射基线证明注意力缺失（100%成功）来确认SSRP的必要性;通过等距压力测试（90%准确性）将闩锁与位置偏差脱钩;并通过信息瓶颈原则和粒度消融正式化SSRP。程序完整性审计（98.8%的遵守率）揭示了一种基础悖论，其中高稳定性模型因拒绝在检索推理污染下产生幻觉而失败。

[阅读原文](https://arxiv.org/abs/2604.24512)

---

## 8. 统计数据库工程：可观察性驱动的编码代理工具自动进化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving agent framework (AHE) for coding-agent harnesses that uses observability-driven evolution loops, directly matching the self-improving agent criterion.

**摘要**: arXiv：2604.25850v1宣布类型：新摘要：利用已成为编码代理性能的核心决定因素，塑造了模型与存储库、工具和执行环境的交互方式。然而，自动化利用工程很困难：异类的动作空间、稀疏且有噪音的评估信号、数百万个代币的轨迹，以及影响难以归因于下一轮结果的编辑。我们引入了Atlantic Buttons Engineering（AHE），这是一个框架，通过仪表化任何工程循环的三个阶段来自动化利用层演变（零部件编辑、轨迹检查和决策）具有匹配的可观察性支柱：（1）零部件可观察性为每个可编辑的背带零部件提供了文件级表示，因此动作空间是明确且可恢复的;（2）经验可观察性将数百万个原始轨迹标记提炼成分层的、深入挖掘的证据库，进化的代理人实际上可以消费;以及（3）决策可观察性将每个编辑与自我声明的预测配对，随后针对下一轮的任务级结果进行验证。这些支柱共同将每一次编辑都变成了一份可证伪的合同，因此利用进化可以自主进行，而不会陷入试错。从经验上看，十次AHE迭代将Terminal-Bench 2的pass@1从69.7%提高到77.0%，超过了人类设计的安全带Codex-CLI（71.9%）和自我进化的基线ACE和TF-GRPO。冻结的马具在未经重新进化的情况下转移：在SWE-工作台验证上，它以比种子少12%的代币的总成功率超过了总成功率，而在Terminal-Bench 2上，它在三个替代模型家族中产生了+5.1至+10.1 pp的跨家族收益，这表明进化的组件编码了一般工程经验，而不是特定基准的调整。这些结果将可观察性驱动的进化定位为保持编码代理利用持续改进的实用途径。

[阅读原文](https://arxiv.org/abs/2604.25850)

---

## 9. 一个细化器将它们全部分解：通过强化查询细化的推理启发

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yixiao Zhou, Dongzhou Cheng, zhiliang wu, Yi Yang, Yu Cheng, Hehe Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning-based query refiner to elicit reasoning from frozen LLMs at inference time, directly matching RL for LLMs and inference-time reasoning elicitation.

**摘要**: arXiv：2604.25444v1宣布类型：新摘要：由于模糊的人类查询与机器激活所需的结构化逻辑之间的分布不匹配，大型语言模型（LLM）经常无法利用其潜在的推理能力。现有的对齐方法要么通过单独微调每个模型而招致令人望而却步的O（N）$成本，要么依赖于无法解决查询级结构复杂性的静态提示。在本文中，我们提出了ReQueR（\textBF{Re} inspel\textBF{Que}ry \textBF{R}细化），这是一个模块化框架，将推理引出视为推理时对齐任务。我们通过强化学习训练专门的细化器策略，将原始查询重写为显式逻辑分解，将冻结的LLM视为环境。我们植根于教育心理学的经典近端发展区，引入了自适应求解器层次结构，这是一种课程机制，通过动态地将环境难度与精炼者不断发展的能力联系起来来稳定培训。ReQueR在不同的架构和基准中的绝对收益为1.7%-7.2%，平均比强劲基线高出2.1%。至关重要的是，它为一对多推理时推理启发提供了一个有希望的范式，使在一小群模型上训练的单个精炼机能够有效地解锁各种未见模型中的推理。代码可在https://github.com/newera-xiao/ReQueR上获取。

[阅读原文](https://arxiv.org/abs/2604.25444)

---

## 10. Nautile-370 M：光谱记忆在小型推理模型中受到关注

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Maixent Chenebaux

**机构**: Google TPU Research Cloud, NVIDIA

**💡 亮点 (Highlight)**: Proposes a hybrid architecture with latent spectral memory for efficient reasoning and includes an RL stage for reasoning improvement, directly relevant to latent reasoning and RL for LLMs.

**摘要**: arXiv：2604.24809v1宣布类型：新摘要：我们介绍了Nautile-370 M，这是一个包含3.71亿个参数的小语言模型，旨在在严格的参数和推理预算下进行高效推理。Nautile-370 M使用混合主干，其中两个SeqCond Attention（SCA）层，一个受SeqCondenser启发的线性时间光谱序列算子，与一个Transformer层交替。该设计旨在保留结构化顺序模型的长上下文效率和状态跟踪优势，同时保留表达性的代币到代币注意力传递。该模型是在Google pu Research Cloud（TRC）程序提供的单个Cloud pu v4-64 pod切片上训练的;随后的强化学习阶段是在单个NVIDIA DGX Spark上执行的。我们证明，SCA读出机制可以从前置摘要中准确检索任何单个令牌，并且可以将softmax注意力的任何输出作为特殊情况来再现，从而确定SCA至少与连续限制下的完全自我注意力一样具有表达力。我们还描述了训练数据管道，并概述了专门用于推理、验证和响应质量的强化学习阶段。

[阅读原文](https://arxiv.org/abs/2604.24809)

---

## 11. 计算一致训练：优化测试时间推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Adam Ousherovitch, Ambuj Tewari

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Compute Aligned Training, a new RL training objective that aligns training with test-time inference strategies, directly addressing RL for LLMs.

**摘要**: arXiv：2604.24957v1宣布类型：新摘要：扩展测试时计算已成为增强大型语言模型（LLM）性能的强大机制。然而，标准的训练后范式（监督微调（SFT）和强化学习（RL））优化了基本策略下单个样本的可能性，从而与依赖聚合或过滤输出的测试时间过程产生不一致。在这项工作中，我们提出了计算对齐训练，它将培训目标与测试时间策略保持一致。通过将推理策略概念化为基本策略上的操作员，我们推导出新的损失函数，当应用所述策略时，该函数可以最大化性能。我们跨常见测试时间策略实例化SFT和RL的此类损失函数。最后，我们提供了经验证据，表明这种训练方法比标准训练大大提高了测试时间扩展。

[阅读原文](https://arxiv.org/abs/2604.24957)

---

## 12. 视频生成的系统性训练后框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zeyue Xue, Siming Fu, Jie Huang, Shuai Lu, Haoran Li, Yijun Liu, Yuming Li, Xiaoxuan He, Mengzhao Chen, Haoyang Huang, Nan Duan, Ping Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a systematic post-training framework for video diffusion models that includes RLHF with a novel GRPO method, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2604.25427v1宣布类型：新摘要：虽然大规模视频扩散模型在生成高分辨率和语义丰富的内容方面表现出令人印象深刻的能力，但由于即时敏感性、时间不一致性和过高的推理成本等关键问题，其预训练性能与现实世界的部署要求之间仍然存在显着差距。为了弥合这一差距，我们提出了一个全面的训练后框架，该框架通过四个协同阶段将预训练模型与用户意图系统地联系起来：我们首先使用监督微调（SFT）将基本模型转换为稳定的策略跟踪策略，随后是人类反馈强化学习（RL HF）阶段，该阶段利用了新型的群体相对政策优化（GRPO）专为视频扩散量身定制的方法，以增强感知质量和时间一致性;随后，我们通过专门的语言模型集成提示增强以细化用户输入，并最终通过推理优化解决系统效率问题。这些组件共同提供了一种系统性的方法来提高视觉质量、时间一致性和指令遵循，同时保留在训练前过程中学到的可控性。其结果是构建可扩展的培训后管道的实用蓝图，这些管道在现实世界部署中稳定、适应性强且有效。大量实验表明，这种统一的管道有效地减轻了常见的伪影，并显着提高了可控性和视觉美观性，同时遵守严格的采样成本限制。

[阅读原文](https://arxiv.org/abs/2604.25427)

---

## 13. 错误何时有益：政策梯度不完美回报的分类

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shuning Shang, Hubert Strauss, Stanley Wei, Sanjeev Arora, Noam Razin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Theoretically categorizes reward errors in policy gradient for LLMs as benign or beneficial, with implications for RLHF reward model evaluation and verifiable reward design.

**摘要**: arXiv：2604.25872v1宣布类型：新摘要：通过强化学习训练语言模型通常依赖于不完美的代理奖励，因为准确定义预期行为的基本真相奖励很少可用。评估代理奖励质量的标准指标（例如排名准确性）将不正确的奖励视为严格有害的。然而，在这项工作中，我们强调并非所有与基本真相的偏差都是相同的。通过从理论上分析政策梯度优化期间哪些输出吸引概率，我们根据奖励错误对地面真相奖励增加的影响对奖励错误进行分类。分析确定，奖励错误虽然传统上被视为有害的，但也可以是良性的，甚至是有益的，可以防止政策以平庸的基本事实奖励来拖延产出。然后我们提出了我们理论的两个实际含义。首先，对于来自人类反馈的强化学习（RL HF），我们开发了考虑奖励错误危害性的奖励模型评估指标。与标准排名准确性相比，这些指标通常与RL HF之后语言模型的性能相关性更好，但在稳健评估奖励模型方面仍然存在差距。其次，我们为具有可验证奖励的环境中的奖励设计提供见解。我们结果的一个关键主题是，代理奖励函数的有效性在很大程度上取决于其与初始策略和学习算法的相互作用。

[阅读原文](https://arxiv.org/abs/2604.25872)

---

## 14. CroSearch-R1：更好地利用跨语言知识进行检索增强生成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Rui Qi, Fengran Mo, Sijin Lu, Yufeng Chen, Jian-Yun Nie, Kaiyu Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CroSearch-R1, a search-augmented RL framework using GRPO for cross-lingual knowledge integration in RAG, directly matching RL for LLMs via verifiable reward and multi-turn retrieval.

**摘要**: arXiv：2604.25182v1公告类型：新摘要：多语言集合可能包含其他语言的有用知识，以补充和纠正原始语言中的事实，以进行检索增强生成（RAG）。然而，简单地将来自不同语言的多个知识片段连接到上下文的普通方法可能无法提高效率，因为不同语言之间存在潜在的差异。为了更好地利用多语言知识，我们提出了CroSearch-R1，这是一个搜索增强强化学习框架，用于将多语言知识集成到集团相对政策优化（GRPO）流程中。特别是，该方法采用具有跨语言知识集成的多回合检索策略，将来自其他语言的知识作为补充证据动态对齐到统一的表示空间中。此外，我们引入了多语言推出机制来优化推理跨语言的可移植性。实验结果表明，我们的框架有效地利用了跨语言互补性，并提高了RAG的多语言集合的有效性。

[阅读原文](https://arxiv.org/abs/2604.25182)

---

## 15. 解释质量评估作为列表奖励排名

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Thomas Bailleux, Tanmoy Mukherjee, Emmanuel Lonca, Pierre Marquis, Zied Bouraoui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel ranking-based reward model training method for explanation quality, directly applicable as a reward signal in RL for LLMs.

**摘要**: arXiv：2604.24176v1宣布类型：新摘要：我们将解释质量评估重新定义为排名问题而不是生成问题。我们不是优化模型来逐句地产生单个“最佳”解释，而是训练奖励模型来区分多个候选解释并了解它们的相对质量。具体来说，我们构建具有分级质量水平的每实例候选集，并训练逐列表和逐成对排名模型（ListNet、Lambda Rank、RankNet），以保留有序结构并避免逐点回归或二元偏好目标典型的分数压缩。我们观察到三个发现：首先，在所有测试领域中，排名损失在评分分离方面始终优于回归。其次，最佳排名损失取决于数据特征：列表式目标在分离良好的质量层中表现出色，而成对方法对有噪音的自然注释更稳健。第三，当在精心策划和结构良好的数据上进行训练时，小型编码器模型可以匹配数量级更大的模型，这表明数据质量比模型规模更重要。最后，当在政策优化中用作奖励时，基于排名的分数可以在基于回归的奖励完全失败的环境中实现稳定的收敛。代码和数据可访问：https://github.com/Tankiit/PPO_Learning_to_rank

[阅读原文](https://arxiv.org/abs/2604.24176)

---

## 16. ClawTrace：LLM代理技能蒸馏的成本意识追踪

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Boqin Yuan, Renchu Song, Yue Su, Sen Yang, Jing Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a cost-aware tracing and distillation pipeline for LLM agent skill improvement, enabling self-improvement via prune/repair patches from interaction traces.

**摘要**: arXiv：2604.23853v1宣布类型：新摘要：技能蒸馏管道从LLM代理轨迹中学习可重复使用的规则，但它们缺乏关键信号：每一步的成本是多少。如果没有每一步的成本，管道无法区分添加缺失的步骤来修复错误和删除从未影响结果的昂贵步骤。我们引入ClawTrace，这是一个代理跟踪平台，可以记录代理会话期间的每个LLM调用、工具使用和子代理派生，并将每个会话编译成TraceCard：紧凑的YML摘要，包含每步USD成本、令牌计数和冗余标志。CostCraft基于ClawTrace构建，是一个蒸馏管道，可以读取TraceCards并生成三种类型的技能补丁。保留补丁保留导致成功的行为。修剪补丁删除了无关紧要的昂贵步骤，每一个步骤都有反对指定高成本步骤的反事实论点。修复补丁修复了基于Oracle证据的故障。对30个已发布的数据表长凳任务的消融表明，成本归因和修剪补丁都可以独立地减少质量回归。当相同的技能应用于30个不相关的SkillsBench任务时，会出现意想不到的不对称现象：修剪跨基准传输的规则并将中位数成本降低32%，而保留基于特定基准惯例训练的规则会导致新任务类型的回归。我们发布ClawTrace和TraceCards作为开放基础设施，用于成本意识的代理研究。

[阅读原文](https://arxiv.org/abs/2604.23853)

---

## 17. DDA-Thinker：用于推理驱动图像编辑的脱钩双原子强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hanqing Yang, Qiang Zhou, Yongchao Du, Sashuai Zhou, Zhibin Wang, Jun Song, Tiezheng Ge, Cheng Yu, Bo Zheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a decoupled dual-atomic RL framework with verifiable checklists to optimize a reasoning planning module for image editing, directly matching RL for LLMs via reward design and verifier-driven optimization.

**摘要**: arXiv：2604.25477v1宣布类型：新摘要：最近的图像编辑模型已经实现了很强的视觉保真度，但经常难以应对需要复杂推理的任务。为了研究和增强基于推理的图像编辑规划，我们提出了DDA-Thinker，这是一个以思想者为中心的框架，旨在在固定生成模型（Editor）上独立优化规划模块（Thinker）。这种脱钩的以思想者为中心的范式促进了对规划模块的受控分析，并使其在固定编辑器下的贡献更容易评估。为了有效地指导这位思想者，我们引入了双原子强化学习框架。该框架将反馈分解为两个不同的原子奖励，通过可验证的检查表实现：认知原子奖励，用于直接评估思想者可执行计划的质量，该计划作为思想者推理的可操作结果，以及视觉原子奖励，用于评估最终图像质量。为了提高检查表质量，我们的检查表合成不仅基于源图像和用户说明，还基于理想编辑后场景的合理参考描述。为了支持这项培训，我们进一步开发了一个两阶段的数据策划管道，首先合成多样化且以推理为中心的数据集，然后应用困难意识的细化来策划有效的强化学习培训课程。对推理驱动的图像编辑基准（包括RISE-Bench和KRIS-Bench）的广泛实验表明，我们的方法大大提高了整体性能。我们的方法使社区模型能够实现与强大的专有模型具有竞争力的结果，凸显了在固定编辑器设置下以思想者为中心的优化的实际潜力。

[阅读原文](https://arxiv.org/abs/2604.25477)

---

## 18. 与自己的声音保持一致：LVLM中的幻觉缓解的自我纠正偏好学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Byeonggeuk Lim, JungMin Yun, Junehyoung Kwon, Kyeonghyun Kim, YoungBin Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes AVES-DPO, a new RL pipeline using self-correction and consensus-based verification to generate in-distribution preference data for DPO, directly addressing hallucination mitigation in LVLMs.

**摘要**: arXiv：2604.24395v1宣布类型：新摘要：大型视觉语言模型（LVLM）经常出现幻觉。现有的基于偏好学习的方法主要依赖于专有模型来构建偏好数据集。我们发现这种依赖在专有模型和目标模型之间引入了分布不匹配，从而阻碍了有效的对齐。为了解决这个问题，我们提出了通过VErified Self-correction DPO（AVES-DPO）进行对齐，这是一个使用源自模型内在知识的分布数据来对齐LVLM的框架。我们的方法采用基于共识的验证机制来诊断各种幻觉并引导模型自我纠正，从而生成与其内部分布严格兼容的偏好对。大量实验表明，AVES-DPO在缓解幻觉方面超越了现有基线，同时仅需要52，000个样本。

[阅读原文](https://arxiv.org/abs/2604.24395)

---

## 19. 思维像素：多模式扩散潜势中的回归稀疏推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuwei Sun, Yuxuan Yao, Hui Li, Siyu Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a recursive sparse mixture-of-experts framework for latent reasoning in diffusion models, directly matching the latent CoT/reasoning criterion.

**摘要**: arXiv：2604.25299v1宣布类型：新摘要：扩散模型在高保真数据合成方面取得了成功，但它们进行文本跟踪任务等更复杂、结构化推理的能力仍然受到限制。虽然语言模型的进步利用了潜在推理和回归等策略来增强文本理解能力，但由于视觉标记的连续性和非离散性，将这些策略扩展到多模式文本到图像生成任务具有挑战性。为了解决这个问题，我们从模块化人类认知中汲取灵感，并提出了一个集成到传统扩散模型中的回归、稀疏混合专家框架。我们的方法在联合注意力层中引入了一个循环组件，该组件在多个潜在步骤上迭代地细化视觉标记，同时通过神经模块的稀疏选择有效地共享参数。在每一步，设计门控网络来动态选择专门的神经模块，以当前视觉标记、扩散时步和条件信息为条件。对类条件ImageNet图像生成任务的综合评估以及对GenEval和DPG基准的额外研究证明了所提出的方法在增强模型图像生成性能方面的优越性。

[阅读原文](https://arxiv.org/abs/2604.25299)

---

## 20. 从1位危险信号发现统计安全规范

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: V\'ictor Gallego

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving agent framework (EPO-Safe) that discovers safety specifications from sparse binary danger signals via reflection, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2604.23210v1宣布类型：新摘要：大型语言模型代理能否仅通过经验发现隐藏的安全目标？我们引入了EPO-Safe（安全代理的体验提示优化），这是一个框架，LLM迭代地生成行动计划，接收稀疏的二元危险警告，并通过反射进化自然语言行为规范。与依赖于丰富文本反馈的标准LLM反射方法不同（例如，编译器错误或详细的环境响应），EPO-Safe证明LLM可以在结构化、低维环境中根据严格贫乏的信号执行安全推理：代理永远不会观察隐藏的性能函数$R^*$，每个时间步只有一个比特表明动作不安全。我们对五个人工智能安全网格世界进行了评估（Leike等人，2017年）和五种基于文本的场景类似物，其中可见奖励$R$可能与$R^*$不同。EPO-Safe在1-2轮（5-15集）内发现安全行为，生成具有关于危险的正确解释假设的人类可读规范（例如，“X细胞具有方向性危险：从北方进入是危险的”）。至关重要的是，我们表明，标准的奖励驱动反思会主动降低安全性：仅反思奖励的代理使用循环来证明奖励黑客行为的合理性和加速奖励黑客行为，证明反思必须与专用的安全通道配对才能发现隐藏的约束。我们进一步评估了对有噪音的先知的鲁棒性：即使50%的非危险步骤产生虚假警告，平均安全性能也只会平均下降15%，尽管灵敏度取决于环境，因为跨场景反射自然过滤不一致的信号。每个进化的规范都充当一组可审计的基础行为规则，通过交互自主发现，而不是像宪法人工智能中那样由人类创作（Bai等人，2022年）。

[阅读原文](https://arxiv.org/abs/2604.23210)

---

## 21. 表格基础模型的优先对齐数据清理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Laure Berti-Equille

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a deep RL framework (L2C2) for tabular data cleaning as prior alignment for Tabular Foundation Models, directly matching RL for LLMs (TFMs) with a novel reward design and RL pipeline.

**摘要**: arXiv：2604.25154v1宣布类型：新摘要：表格基础模型（TFM）通过对合成数据生成过程的元学习，在小型表格数据集上实现了最先进的零精度，这使得它们对于负担不起大型注释数据库的从业者极具吸引力。然而，他们的上下文学习机制假设了大致干净的输入：现实世界数据中的缺失值、异常值和重复项会产生先验不匹配，从而同时降低准确性和置信度校准。纠正这种不匹配需要对清洁操作员进行顺序决策，这些操作员的相互作用没有静态预处理规则可以预测--这非常适合强化学习~（RL）。我们引入L2 C2，这是第一个将表格数据清理框架为先验对齐的深度RL框架：学习的策略对操作员进行排序，以最大限度地减少脏输入和TFM的合成先验之间的分布差距。对十个OpenML基准数据集进行的六项实验确定：1）七个奖励设计中的三个会崩溃，退化为琐碎的清洁策略--有原则的奖励工程在科学上是不平凡的; 2）我们提出的新型TFMAwareReward奖励在4/10数据集上选择结构不同的管道，并在这些不同的情况下实现更高的TabPFN准确性（平均值0.851 vs. 0.843; Wilcoxon p=0.063，n=4）同时表现从不不佳; 3）参数化清洁动作提高了9/10数据集上找到的最佳管道奖励（Wilcoxon p=0.004）;以及4）在一个单一源数据集上预训练的策略超过了在2，对所有三个已发布的数据集进行000步微调检查点（完全微调后最高可达+28.8%），展示了预先对齐知识的跨数据集传输。这些发现确定，预先对齐是在现实世界表格数据上部署TFM的原则性数据准备策略。

[阅读原文](https://arxiv.org/abs/2604.25154)

---

## 22. 神经机器翻译的反向翻译增强直接偏好优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Mehrdad Ghassabi, Spehr Rajabi, Hamidreza Baradaran Kashani, Sadra Hakim, Mahshid Keivandarian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a DPO-based RL post-training framework for NMT, directly matching the RL for LLMs criterion with a new reward/feedback loop.

**摘要**: arXiv：2604.25702v1宣布类型：新摘要：当代神经机器翻译（NMT）系统几乎完全是通过对监督并行数据进行训练来构建的。尽管取得了巨大进步，但这些系统仍然出现持续的翻译错误。本文提出基于强化学习（RL）的后训练范式可以有效纠正此类错误。我们引入了一种新颖的框架，该框架只需要通用文本库和专家翻译器，该翻译器可以是人类或人工智能系统来提供迭代反馈。在我们的实验中，我们特别关注英语到德语的翻译，作为代表性的高资源语言对。至关重要的是，我们使用直接偏好优化（DPO）实现这种基于RL的后训练。将我们的DPO驱动框架应用于gemma 3 - 1b模型可以显着提高翻译质量，将英语到德语任务的COMET得分从0.703提高到0.747。结果表明，DPO为通过基于偏好的后训练来增强预训练的NMT模型提供了一种高效而稳定的途径。

[阅读原文](https://arxiv.org/abs/2604.25702)

---

## 23. 内在互信息作为偏好优化的调制器

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Peng Liao, Peijia Zheng, Lingbo Li, Shangsong Liang, Lin Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RMiPO, a novel offline preference optimization framework using intrinsic mutual information for hyperparameter-free modulation, directly improving LLM alignment.

**摘要**: arXiv：2604.24804v1宣布类型：新摘要：离线偏好优化方法（例如直接偏好优化（DPO））在使大型语言模型（LLM）与人类价值观保持一致方面提供了显着优势。然而，用这些方法实现最佳性能通常涉及额外的超参数调整，从而导致大量的时间负担。尽管之前的工作提出了一系列改进，但这些方法的有效性仍然有限，并且没有完全消除对超参数调整的依赖。在这项工作中，我们提出了RMiPO，这是一个轻量级且高效的离线偏好优化框架。RMiPO利用固有的响应级别互信息进行偏好优化，通过超参数调制，以可忽略不计的额外计算成本动态地脱钩偏好贡献。大量实验结果表明，RMiPO比现有方法实现了一致的卓越性能，同时将训练费用减少了15%以上。我们的代码可在https://github.com/liavonpenn/rmipo上获取。

[阅读原文](https://arxiv.org/abs/2604.24804)

---

