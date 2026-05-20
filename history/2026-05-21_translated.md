# 💡 今日研究速览 (Daily Summary)

# LLM的RL（推理和对齐）
大型语言模型的强化学习正在发生明显的范式转变，从简单的基于结果的奖励转向复杂的、过程感知的和分布匹配的技术。几篇论文直接解决了模式崩溃和低效探索的核心WLVR局限性。**超越模式崩溃**和**SAGE**都挑战了标准的反向KL目标，分别提出分布匹配和锚重塑，以提高推理多样性和覆盖范围。与此同时，信用分配正在粒度层面上进行细化：**CEPO**通过对比证据来尖锐决定性推理代币的奖励信号，而**Lambda PO** 则用分解的成对偏好取代纯量优势，以实现更细粒度的对齐。* * 何时停止重复使用 **解决了WLVR中样本效率的关键问题，它引入了动态梯度门控，以防止陈旧样本造成灾难性的策略转变。最后，**GoLongRL**将前沿推向了长上下文场景，展示了一种面向能力的WLVR配方，具有多任务对齐以实现异类优化。

# 潜在推理和推理时计算
随着新颖的理论和建筑贡献，对高效、非言语推理的追求正在加速。中心主题是潜在推理动力的出现和稳定。**前沿叠加的出现**通过证明梯度下降可以通过莫比乌斯吸引子学习叠加推理，提供了理论基础。**生成式回归推理**和**概率微小回归模型**都探索概率、多轨迹潜在计算，后者为随机探索注入噪音。架构稳定性是一个关键的推动因素，如**简单稳定环路** 所示，它引入了无参数修改来稳定全环路变压器，无需明确的思想链即可实现迭代计算。在推断时间管道方面，**CopT**通过颠倒CoT顺序并使用来自连续嵌入的对比验证器来增强可靠性，提供了一种实用的替代方案。

# 代理与自我提升
LLM代理领域正在从简单的工具使用成熟到具有强大治理的复杂、自我进化的系统。**Library Drift**提供了关键诊断，该诊断为自我发展技能库中的无声故障模式识别并提出了经过验证的修复方案，强调了自主改进中监督的必要性。**奖励信念，而不是行动**推进了长期代理任务中的信用分配，它使用信念一致性监督来提供流程级奖励。**MOCHA**解决了现实世界约束下的代理技能的多目标优化，它引入了Chebyshev模拟来导航帕累托前沿。此外，机械性的理解正在加深，正如**To Call or Not to Call* 所示，它使用基于CAE的分析来诊断和纠正工具使用中固有的过度调用偏见，而 **提取什么和何时提取**则提出了针对多回合代理的选择性环境重新加权RL。

# 多模式和视觉语言模型（VLM）
VLM的后培训正在系统性分解和专业化，超越单一微调。**从看到到思考**展示了一个关键的见解：将感知和推理脱钩到分阶段训练中，其中RL对于感知学习更有效，显着提高了整体推理效率。适应性推理的主题延伸到工具的使用，例如**工具总是有益的吗？**为MLLM提出了一个RL框架，以适应性地决定何时调用工具，并提供双模式奖励。在视觉生成领域，**FlowErase-RL**和**基准和Evolving Reason-Reflect-Rectify**都分别将GRPO应用于流匹配和反射视觉生成中的新前沿概念擦除，而**TextAlign**则引入了基于分层的基于LM的奖励文本渲染中的偏好对齐。最后，**VL-DPO**将此范式应用于自动驾驶，使用VLM作为零触发推理器来生成用于运动预测对齐的偏好对。

# 新颖的培训目标与优化
除了标准的WLVR之外，该社区还在探索重塑学习格局的创新培训目标和优化算法。**通过使用共同训练的验证器在RL框架内提供可学习的逐步语言反馈，WRIDE**消除了对昂贵的分步注释的需要。“漂移”目标的概念是由**细化离散扩散的漂移目标** 引入的，它通过将分类预测提升为软代币来提高发电质量。**驯服思想者**提出了一种使用条件性信息量整形的新型基于RL的框架，其中代币级信息量作为动态控制推理深度的奖励信号。在优化方面，**超越预训练的重新思考Muon**识别了WLVR中Muon优化器的频谱故障，并提出Pion作为高通补救措施。最后，**TEMPO** 通过具有双重奖励的模式分离政策优化在LLM回溯测试中强制执行时间纪律。

---

## 1. 前沿叠加的出现：M ' obius吸引子和级联监督

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 9/10

**作者**: Hongyu Gu, Jingwen Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proves that gradient descent can learn superposition reasoning via a Mobius attractor and Cascade Supervision, directly advancing latent reasoning architectures.

**摘要**: arXiv：2605.18820v1宣布类型：新摘要：叠加允许变形金刚进行深度推理，通过有界深度的向前传递并行地进行整个推理前沿，而不是展开连续的思想链代币。虽然Zhu等人（2025）在单个剩余流中手工制作了一个等权宽度优先边界以实现图形可达性，但梯度下降是否能在排列对称的马鞍中找到这个目标仍然悬而未决。   我们通过隔离架构和监管贡献来缩小Erd\H{o}s-R\' enyi图上叠加可达性的这一差距。从结构上来说，我们识别了M\' obius吸引子：在树域的$S_n$-对称下，逐层动力学简化为一维M\' obius映射，其零集是包含等权叠加状态的全局最优解的余维一多管。   在监督方面，我们确定了Cascade Supervision：一种损失类，其向后传递同时提供（A）选择性自举、（B）跨深度的梯度持续性和（C）逐步区分（例如，\mathCal{L}_{sup}和\mathCal{L}_{节点}）。端到端监控不符合条件（B），并且可以证明是不充分的：c层的内部梯度在到达管汇之前衰减为图中的（mp）' s ' s ' s ' s散开并停止。   我们的论文：M\' obius吸引子+级联监督=叠加推理的出现。无参数衰变定律预测深度D=3处的最后一步cos分别为0.35和0.71（端到端与级联）;实验证实了0.37和0.69，每一步都在0.02内匹配。

[阅读原文](https://arxiv.org/abs/2605.18820)

---

## 2. CopT：政策上的对比思维，具有一般和抽象推理的连续空间

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Dachuan Shi, Hanlin Zhu, Xiangchi Yuan, Wanjia Zhao, Kejing Xia, Wen Xiao, Wenke Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CopT, a novel inference-time reasoning pipeline that reverses CoT order and uses contrastive verifiers from continuous embeddings for answer reliability, directly matching the Latent CoT/Reasoning criterion.

**摘要**: arXiv：2605.20075v1宣布类型：新摘要：思想链（CoT）是从大型语言模型（LLM）中获取推理能力的标准方法。然而，常见的CoT范式将思维视为回答的先决条件，即使模型能够在扩展思维之前识别答案，这也可能会延迟对合理答案的访问，并产生不必要的代币成本，这种行为被称为表演推理。在本文中，我们介绍了CopT，这是一种重新制定的推理管道，可以颠倒通常的思考和回答顺序。CopT不是在回答之前思考，而是首先提出答案草案，然后根据其自己的答案草案援引随后的政策思考进行反思和纠正。为了评估草案答案是否应该可信，CopT将连续嵌入重新铸造为推理时对比验证器。具体来说，它对比了模型在离散令牌输入和连续嵌入输入下对相同生成令牌的支持，从而产生了答案可靠性的序列级反向KL估计器。我们的分析表明，在某些假设下，预期估计等于未解析的潜伏状态和发出的答案令牌之间的互信息，这解释了为什么它捕获了与答案相关的不确定性，而不是潜伏状态中的任意不确定性。当答案被认为不够可靠时，CopT会进一步进行政策思考，其中第二个KL估计器动态控制草案答案的可见性，保留有用的部分信息，同时降低被不可靠内容误导的风险。在数学、编码和代理推理任务中，CopT可以在相当或更高的准确性下将峰值准确率提高高达23%，并在无需任何额外训练的情况下将代币使用率降低高达57%。该代码可在https://github.com/sdc17/CopT上获取。

[阅读原文](https://arxiv.org/abs/2605.20075)

---

## 3. FRAIDE：LLM推理的可学习逐步反馈语言

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junjie Zhang, Guozheng Ma, Shunyu Liu, Zetian Hu, Yongcheng Jing, Ting-En Lin, Yongbin Li, Dacheng Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes STRIDE, a novel RL training framework using learnable stepwise language feedback from a co-trained verifier to redirect LLM reasoning trajectories, eliminating costly step-level annotations.

**摘要**: arXiv：2605.18851v1宣布类型：新摘要：强化学习（RL）的最新进展凸显了其激励大型语言模型（LLM）推理能力的潜力。然而，现有的阶梯级工作受到成本高昂的注释的影响，从而限制了域覆盖范围，而纯量分数进一步造成了信息瓶颈，提供了足够的语义带宽来改善中间决策。替代语言批评方法依赖于冻结或外部批评者，提供了更丰富的文本反馈，但缺乏持续政策改进所需的可扩展性。在这项工作中，我们提出了语言驱动的逐步轨迹重定向，称为WRIDE，这是一种新颖的训练框架，可以将流程监督从纯量奖励转变为可学习的逐步语言反馈。具体来说，我们仅使用基于结果的奖励来共同训练生成器和生成性验证器，消除外部注释，同时通过联合一致的验证器培训来提供持续的政策改进。验证者的逐步语言批评明确地本地化和解释失败，使生成器能够在中间步骤将推理轨迹重定向到替代决策。轨迹重定向设计保证了无害的策略改进，即使在有噪音或次优的验证者反馈下也是如此。不同推理基准的实验表明，WRIDE的表现显着优于最先进的基线，并在零通过率问题上取得了突破，其中在我们的消融研究中，纯量方法不会产生学习信号，证明了可学习的逐步语言反馈的有效性增强LLM推理。

[阅读原文](https://arxiv.org/abs/2605.18851)

---

## 4. 何时停止重复使用：动态梯度门控以实现样本高效的WLVR

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuchun Miao, Sen Zhang, Yuqi Zhang, Yaorui Shi, Qi Gu, Xunliang Cai, Lefei Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RLVR method (Dynamic Gradient Gating) that uses lm_head gradient norm to detect and prevent catastrophic policy shift from sample reuse, achieving significant sample efficiency gains.

**摘要**: arXiv：2605.19425v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）已成为大型语言模型（LLM）中高级推理的主要范式，但获得推出样本的成本高昂，这使得样本效率成为关键瓶颈。一个自然的补救措施是重复使用每个推出批次进行多个梯度更新，这是经典RL的标准实践。然而，在WLVR中，这放大了政策转变，导致性能严重下降。尽早检测退化的开始以停止重复使用仍然是一个悬而未决且具有挑战性的问题。我们通过识别\textit{不成比例的重量分歧（DWD）}现象来缩小这一差距：性能下降与\texttt{lm\_head}重量变化的急剧激增同步，而中间层保持稳定。从经验上看，我们验证DWD在不同的LLM和任务中一致出现。理论上，我们证明了（i）有害的梯度集中在\texttt{lm\_head}，而中间层是结构性衰减，和（ii）\texttt{lm\_head}梯度范数下界的政策分歧。这些结果确立了梯度范数作为灾难性政策转变的原则性实时信号。在这种见解的指导下，我们提出了动态梯度门控（DGG），一个轻量级的干预，实时监控\texttt{lm\_head}梯度范数，并在破坏优化器之前拦截有害的梯度。DGG始终匹配或超过标准的单次使用基线，在数学，ALFWorld，WebShop和搜索增强的QA任务中实现高达2.93\times $的采样效率和2.14\times $的挂钟加速。

[阅读原文](https://arxiv.org/abs/2605.19425)

---

## 5. 生成式回归推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junyeob Baek, Mingyu Jo, Minsu Kim, Mengye Ren, Yoshua Bengio, Sungjin Ahn

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GRAM, a generative recursive reasoning model that performs probabilistic multi-trajectory latent computation, directly matching the latent CoT/reasoning criterion.

**摘要**: arXiv：2605.19376v1宣布类型：新摘要：未来的神经推理系统应该如何实现扩展计算？回归推理模型（RRM）通过使用共享转移函数执行迭代潜伏状态细化，为自回归序列扩展提供了一种有希望的替代方案。然而，现有的RRM在很大程度上是确定性的，遵循单一潜在轨迹并收敛到单一预测。我们引入了\ð {Generative Recursive reAsoning Models（RST）}，这是一个将循环潜在推理转化为概率多轨迹计算的框架。将模型推理作为随机潜在轨迹，通过循环深度和并行轨迹采样实现多个假设、替代解决方案策略和推断时间缩放。这产生了一个潜变量生成模型，支持通过$p_\theta（y \mid x）$进行条件推理，并在固定或不存在输入的情况下，通过$p_\theta（x）$进行无条件生成。经过摊销变分推理的训练，NPS在结构化推理和多解约束满足任务方面比确定性的循环和循环基线有所改进，同时展示了无条件生成能力。\href{https：//ahn-ml.github.io/gram-website/}{https：//ahn-ml.github.io/gram-website}

[阅读原文](https://arxiv.org/abs/2605.19376)

---

## 6. 奖励信念，而不是行动：长期代理人的一致性引导信用分配

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Wenjie Tang, Minne Li, Sijie Huang, Liquan Xiao, Yuan Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ReBel, a process-level RL algorithm for LLM agents that uses belief-consistency supervision and belief-aware grouping for improved credit assignment in long-horizon tasks.

**摘要**: arXiv：2605.20061v1宣布类型：新摘要：来自可验证奖励的强化学习（WLVR）是改进长期交互任务中的大型语言模型（LLM）代理的一种有前途的范式。然而，在部分可观察的环境中，不完整的观察导致代理人信念随着时间的推移而漂移，而延迟的奖励掩盖了中间决策的因果影响，加剧了临时信用分配挑战。为了解决这个问题，我们提出了ReBel（奖励信念），这是一种过程级强化学习算法，它显式地建模结构化信念状态，以总结交互历史并指导后续的政策学习。ReBel引入了信念一致性监督，将预测信念和观察到的反馈之间的差异转换为密集的自我监督信号，而无需外部逐步注释或验证器。它还采用信念感知分组来比较相似信念状态下的轨迹，从而产生更稳健、更低方差的优势估计。我们根据具有挑战性的长期基准来评估ReBel，包括ALFWorld和WebShop。ReBel将任务成功率比剧集级基线GRPO提高了高达20.4美元的百分点，并将样本效率提高了2.1美元\x $。这些结果表明，信念感知的自我监督是部分可观察性下可靠的长期决策的一个有前途的方向。代码可访问：https://github.com/Fateyetian/Rebel.git。

[阅读原文](https://arxiv.org/abs/2605.20061)

---

## 7. 图书馆漂移：诊断和修复自我发展的LLM技能库中的无声失败模式

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly addresses a critical failure mode in self-evolving agent skill libraries (library drift) and proposes a verified governance fix, strongly matching the self-improving agents criterion.

**摘要**: arXiv：2605.19576v1宣布类型：新摘要：自我发展的技能库面临着我们称之为\{库漂移}的无声失败模式：没有结果驱动的生命周期管理的无限技能积累会导致检索降级、假阳性注入和性能停滞。最近的评估证实了这一症状--法学硕士撰写的技能可带来+0.0pp的收益，而人类策划的技能可带来+16.2pp的收益（SkillsBench）--但潜在机制尚未被孤立。我们提供（1）可重复的触发：隔离漂移的消融--一种禁用技能注入（平楼，+0.002），一种强制提前退休（主动伤害，$-$0.019）;（2）跟踪级诊断：仅附加的证据日志，其中包含每项技能贡献分数、归因判决和路由器参与度指标，使故障在达到最终任务分数之前可见;以及（3）经过验证的修复：最低治理配方（结果驱动的退休+有界主动上限+元技能编写之前），将MBPP+硬-100轮内的持有通行证@1从0.258基线提升到后期窗口平均值0.584（滚动收益$+$0.328）。八次消融分解了哪些治理机制是承载的以及哪些被包含的，为诊断任何自我进化的代理中的库漂移提供了具体的剧本。

[阅读原文](https://arxiv.org/abs/2605.19576)

---

## 8. CEPO：使用对比证据政策优化的WLVR自蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ahmed Heakl, Abdelrahman M. Shaker, Youssef Mohamed, Rania Elbadry, Omar Fetouh, Fahad Shahbaz Khan, Salman Khan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CEPO, a novel RLVR method with contrastive credit assignment that sharpens reward signals at decisive reasoning tokens, achieving strong gains over GRPO.

**摘要**: arXiv：2605.19436v1宣布类型：新摘要：当模型在具有可验证奖励的强化学习（WLVR）下产生正确的解决方案时，每个令牌都会收到相同的奖励信号，无论它是决定性的推理步骤还是语法填充物。一个自然的解决办法是将模型作为教师的正确答案作为条件，识别如果它知道答案，它会生成不同的标记。之前的工作表明，这要么通过将答案泄露到梯度中来破坏训练，要么产生无法区分决定性步骤和填充步骤的弱信号，因为相对于模型的基线，两者看起来同样令人惊讶。我们提出了对比证据政策优化（CEPO），它在每个代币上提出了一个更尖锐的问题：不仅仅是“正确答案是否有利于这个代币？“但是”正确的答案是否有利于它，而错误的答案是否不利于它？“满足两者的代币是真正的推理步骤;满足两者的代币不是填充物。错误答案教师是根据训练批次中已经被拒绝的展开构建的，不会产生额外的抽样成本。我们证明CEPO继承了先前最先进的所有结构安全保证，同时严格提高决定性代币的信用，而改进恰好在填充位置消失。从经验上看，CEPO在2B和4 B规模的五个多模式数学推理基准上分别达到了43.43%和60.56%的平均准确率，而在相同的培训预算下，GRPO的平均准确率分别为41.17%和57.43%。分布匹配自蒸馏方法（OPSD、SDPO）低于未经训练的基线，从经验上证实了我们理论预测的信息泄漏。我们的代码可在https://github.com/ahmedheakl/CEPO上获取。

[阅读原文](https://arxiv.org/abs/2605.19436)

---

## 9. GoLongRL：具有多任务对齐的面向能力的长上下文强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Minxuan Lv, Tiehua Mei, Tanlong Du, Junmin Chen, Zhenpeng Su, Ziyang Chen, Ziqi Wang, Zhennan Wu, Ruotong Pan, jian Liang, Ruiming Tang, Han Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a capability-oriented long-context RLVR post-training recipe with a new dataset and TMN-Reweight for heterogeneous multitask optimization, directly matching RL for LLMs.

**摘要**: arXiv：2605.19577v1宣布类型：新摘要：我们介绍了GoLongRL，这是一个完全开源、以能力为导向的训练后食谱，用于具有可验证奖励的长上下文强化学习（WLVR）。现有的长上下文RL方法通常将数据构建视为设计日益复杂的检索路径的问题，从而导致同质的任务覆盖范围和奖励公式，而不能充分反映实际的长上下文要求。我们的工作提供了两项贡献。(1)以能力为导向的数据构建，完全开放发布。我们公开发布包含23 K WLVR样本、完整的构建管道和所有训练代码的数据集。在长上下文能力分类法的指导下，该数据集跨越9种任务类型，每种任务类型都与其自然评估指标配对。它包括来自已建立的文集的精心策划的开源样本和合成样本，其QA对是从书籍、学术论文和多回合对话等真实源文档中生成的。在相同的vanilla GRPO设置下，我们的数据集的性能优于闭源QwenLong-L1.5数据集。此外，我们在此数据上训练的Qwen 3 - 30 B-A3 B模型提供了与DeepSeek-R1-0528和Qwen 3 - 235 B-A22 B-Thinking-2507相当的长上下文性能，这表明更广泛的覆盖范围和更大的奖励多样性极大地有利于长上下文能力的改进。(2)TMN-Reweight用于异类多任务优化。为了解决来自异类奖励的优化挑战，我们提出了TMN-Reweight，它将跨任务奖励规模对齐的任务级平均标准化与难度自适应加权相结合，以实现更可靠的优势估计。与普通GRPO相比，TMN-Reweight进一步提高了平均性能，并在报告的评估中保留或改进了一般功能。

[阅读原文](https://arxiv.org/abs/2605.19577)

---

## 10. 超越模式崩溃：多元化推理的分布匹配

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaozhe Li, Yang Li, Xinyu Fang, Shengyuan Ding, Peiji Li, Yongkang Chen, Yichuan Ma, Tianyi Lyu, Linyang Li, Dahua Lin, Qipeng Guo, Qingwen Liu, Kai Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DMPO, a distribution-matching RL method that prevents mode collapse in on-policy LLM reasoning by approximating forward KL minimization, showing clear improvements over GRPO.

**摘要**: arXiv：2605.19461v1宣布类型：新摘要：像GRPO这样的政策强化学习方法会遭受模式崩溃的困扰：它们表现出解决方案多样性降低，一旦发现，概率质量就会集中在单个解决方案上，并停止探索替代策略。我们表明，这源于反向KL最小化的模式寻求行为，它强化了发现的第一个高回报轨迹，而不是维持在多个不同解决方案上的分布。我们提出DMPO（分布匹配政策优化），它通过前向KL最小化的原则性逼近来防止模式崩溃。DMPO在抽样轨迹上构建与其回报成比例的团体级目标分布，然后将政策分布与此目标保持一致。这提供了模式覆盖行为，而不需要从棘手的全球目标分布中进行采样，从而在整个训练过程中实现持续的探索。我们在NP难组合优化上验证DMPO，其中存在指数级数量的可行解，但只有少数方法最优性，这是评估探索的理想测试平台。DMPO在基于文本的NP-Bench上的质量比为43.9%（而GRPO为40.1%），在基于视觉的NP-Bench上的质量比为43.1%（而38.4%），分别表现出9%和12%的相对改进。这些收益推广到数学推理（+2.0%）和域外任务（+2.3%），表明多样性保持训练增强了跨模式的一般推理能力。我们的工作将分布匹配确立为一种实用、有原则的方法，用于防止按政策RL中的模式崩溃，并一致的质量改进展示了对不同推理任务的持续探索。

[阅读原文](https://arxiv.org/abs/2605.19461)

---

## 11. SAGE：在LLM的RLVR中塑造引导性探索的屏障

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chanuk Lee, Minki Kang, Sung Ju Hwang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SAGE, a framework that reshapes the reverse-KL anchor distribution in RLVR to improve exploration and reasoning mode coverage, directly addressing a core limitation of RL for LLMs.

**摘要**: arXiv：2605.18864v1宣布类型：新摘要：最近的研究观察到，具有可验证奖励的强化学习（WLVR）可以可靠地改善推理任务的pass@1，但通常无法在pass@k中产生相当的收益，这引发了一个问题：WLVR是否真正使大型语言模型能够获得新颖的推理能力，或者仅仅提高了基础模型中已经存在的采样推理模式的效率。之前的分析在很大程度上支持后一种观点，并将这种限制归因于标准WLVR目标的结构特性，从而导致勘探压力不足。在这项工作中，我们认为，反向KL正规化产生了一个中心结构约束，它稳定了训练，但本质上将政策锚定在参考分布上，从而抑制了替代推理模式的出现。然而，我们表明，无论是删除KL项还是用前向KL取代它都无法提供令人满意的解决方案，因为两者都会通过引发奖励黑客攻击或将概率质量分配给脱靶区域来破坏效率-覆盖率的权衡。为了解决这种紧张关系，我们提出了SAGE，这是一个原则性框架，通过引导函数q（x，y）重塑反向KL锚点分布本身，实现可控的经验支持扩展，在具有挑战性的数学推理基准中实现pass@1和pass@k的一致改进。我们的代码可在https://github.com/tally0818/SAGE上获取。

[阅读原文](https://arxiv.org/abs/2605.18864)

---

## 12. 并非每个规则都能平等地进行教学：针对RLVR的策略感知规则奖励

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei, Daniel George, Anas Mahmoud, Jackson Lee, Bing Liu, Yunzhong He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes POW3R, a policy-aware rubric reward framework for RLVR that dynamically weights criteria based on rollout-level contrast, improving training efficiency and reward informativeness.

**摘要**: arXiv：2605.20164v1宣布类型：新摘要：当可以自动检查正确性时，具有可验证奖励的强化学习使后训练变得非常有效。然而，许多重要的模型行为需要同时满足多个定性标准。基于规则的奖励通过对特定于规则的标准进行分级并将其聚合为标量奖励来解决此设置。然而，标准的静态聚合将标准的人为重要性与其当前作为优化信号的有用性混为一谈。我们表明，这一假设在rubric RL中被打破：许多重要的标准已经饱和或目前无法达到，而区分推出的标准不一定是人类权重最大的标准。我们引入了POW 3R，这是一个策略感知的规则奖励框架，它保留了人类权重和类别平衡作为规则目标，同时在训练过程中调整标准级奖励权重。战俘3 R使用推出级别对比来强调目前分离政策输出的标准，使GRPO奖励更具信息性，而无需改变基本评估目标。在跨越多模式和纯文本设置的两个数据集的三个基本策略中，WW 3R在30美元的基本策略/指标比较中赢得了24美元，比具有标题奖励的香草GRPO提高了平均标题奖励和严格完成（响应满足每个所需标题标准的提示的比例），并在2.5美元--4美元的情况下达到了相同的平台。训练步骤减少。因此，红色奖励应该区分最终答案中应该重要的内容与可以指导当前政策的内容。

[阅读原文](https://arxiv.org/abs/2605.20164)

---

## 13. FlowErase-RL：重新思考概念擦除作为流量匹配模型中的奖励优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Yi Sun, Zhiqi Zhang, Xinhao Zhong, Yimin Zhou, Shuoyang Sun, Bin Chen, Shu-Tao Xia, Ke Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FlowErase-RL, the first GRPO-based framework for concept erasure in flow matching models, reformulating erasure as a reward optimization problem with a dynamic dual-path reward mechanism.

**摘要**: arXiv：2605.19739v1宣布类型：新摘要：流匹配模型的最新进展显着提高了文本到图像的生成质量，但也因产生有害或不良内容而带来越来越大的安全风险。现有的概念擦除方法要么是有效性有限的推理时干预，要么依赖于监督式微调（SFT），这需要精确对齐的数据，并在可扩展性和多概念设置方面遇到困难。在本文中，我们提出了\{FlowErase-RL}，这是第一个用于流匹配模型中概念擦除的基于GRPO的框架。我们将概念擦除重新定义为奖励优化问题，并引入\textBF{动态双路径奖励机制}，该机制联合优化（i）概念擦除（CE）奖励以抑制目标概念和（ii）非目标空间（NS）奖励以保持生成保真度。两个奖励路径在训练期间通过性能驱动的切换策略自适应平衡，从而在无需显式监督的情况下实现稳定优化。关于裸体、物体和艺术风格擦除的大量实验表明，我们的方法在保持强大的图像质量和语义对齐的同时实现了最先进的擦除性能。此外，它对对抗攻击表现出强大的抵抗力，并有效扩展到多概念场景。我们的结果为流匹配模型中的安全可控生成建立了一个新范式。

[阅读原文](https://arxiv.org/abs/2605.19739)

---

## 14. 打电话或不打电话：诊断LLM代理人内在的过度呼叫偏见

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Wei Shi, Ziheng Peng, Sihang Li, Xiting Wang, Xiang Wang, Mengnan Du, Na Zou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses and causally corrects an intrinsic over-calling bias in LLM agents using SAE-based mechanistic analysis and a novel steering method, directly relevant to agent self-improvement.

**摘要**: arXiv：2605.18882v1宣布类型：新摘要：LLM代理始终表现出过度调用的倾向，即使在不需要工具的情况下也会调用工具。在When 2Call基准测试中，来自三个系列的六个型号显示出较高的呼叫准确性，但无呼叫准确性低得多，总体准确性在55%-70%范围内。我们将其追溯到内在偏差假设（IBH）：呼叫/无呼叫决策映射携带与激活无关的呼叫补偿，因此即使在激活平价下，该模型也支持呼叫。使用稀疏自动编码器（SAEs），我们为call/no_call决策恢复行为一致的特征基，将它们减少到带签名的激活裕度，并直接估计偏差。在所有六种模型中，只有当no_call激活超过call激活时，该模型才是决策中立的，这与IBH一致。然后，我们使用自适应边际校准转向（AMCS）对IBH进行因果测试，AMCS是一种沿着AE解码器方向的封闭形式的反偏置漂移。取消诊断出的失调可以缓解过度调用并提高总体准确性，同时调用准确性的下降可以忽略不计。我们的工作将过度呼吁从经验现象重新塑造为一个可以进行因果纠正的机械对象。代码可在https://github.com/SKURA502/agent-sae/上获取。

[阅读原文](https://arxiv.org/abs/2605.18882)

---

## 15. 从看到思考：感知和推理脱钩改善视觉语言模型的后训练

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Juncheng Wu, Hardy Chen, Haoqin Tu, Xianfeng Tang, Freda Shi, Hui Liu, Hanqing Lu, Cihang Xie, Yuyin Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a staged post-training framework for VLMs that decouples perception and reasoning, showing RL is more effective for perception learning and that staged training improves reasoning efficiency.

**摘要**: arXiv：2605.20177v1宣布类型：新摘要：视觉语言模型（VLM）的最新进展强调长链思维推理;然而，我们发现它们在视觉任务上的表现主要受到视觉感知的缺乏而不是推理本身的限制。在这项工作中，我们系统地研究了VLM训练后感知和推理之间的相互作用，方法是将感知和推理的能力分解为三个独立的训练阶段：视觉感知、视觉推理和文本推理，并结合专门的训练数据。我们证明，视觉感知（a）需要使用专业数据进行有针对性的优化;（b）作为基本支架，在完善视觉推理之前应该通过分阶段训练来巩固;（c）通过RL比基于字幕的SFT更有效地学习。我们在多个VLM上的实验表明，分阶段训练与合并训练相比，能够持续提高视觉感知和推理性能。值得注意的是，使用我们的方法训练的模型的推理准确性提高了1.5%，推理轨迹缩短了20.8%，这表明优越的感知减少了过度推理的需要。此外，我们表明，这种基于能力的阶段代表了一个与传统基于困难的课程垂直的新课程维度，并且将两者结合会产生进一步的附加收益。我们的分阶段训练模型在开重型VLM中实现了卓越的性能，在几种视觉数学和感知方面建立了先进的结果（例如，与基本任务相比，WeMath任务增加了5.2%，RealWorldQA任务增加了3.7%。

[阅读原文](https://arxiv.org/abs/2605.20177)

---

## 16. 针对大型推理模型的基于强化学习的越狱的注意力引导奖励

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zheng Lin, Zhenxing Niu, Haoxuan Ji, Yuzhe Huang, Haichang Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based jailbreak method for LRMs that explicitly incorporates attention signals into the reward function design, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2605.19485v1宣布类型：新摘要：大型推理模型（LRM）通过生成结构化的分步推理内容，在解决复杂问题方面表现出了非凡的能力。然而，暴露模型的内部推理过程会带来额外的安全风险;例如，最近的研究表明，LRM比标准LLM更容易受到越狱攻击。本文研究了针对LRM的越狱攻击，发现攻击成功率（ASB）与LRM的注意力模式密切相关。具体来说，成功的越狱往往会对输入提示中的有害符号给予较低的关注，而对推理内容中的这些符号给予较高的关注。受这一发现的启发，我们提出了一种新颖的LRM越狱方法，该方法利用强化学习（RL）来增强攻击有效性，将注意力信号明确地纳入奖励函数设计中。此外，我们还引入了多样化的说服策略来丰富RL动作空间，从而持续提高ASB。在三个基准测试中对五个开源和闭源LRM进行的广泛实验表明，我们的方法实现了更高的ASR，在有效性，效率和可移植性方面优于现有方法。

[阅读原文](https://arxiv.org/abs/2605.19485)

---

## 17. 推理可移植性：指导WLVR时代MLLM的持续学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qiuhe Hong, Yuyang Liu, Shuo Yang, Tiantian Peng, Fei Zhu, Yonghong Tian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new RLVR-based continual learning method for MLLMs that uses reasoning-level portability to modulate KL regularization, directly addressing RL for LLMs.

**摘要**: arXiv：2605.18903v1宣布类型：新摘要：持续学习中的视觉语言模型（VLM-CL）旨在不断适应新的多模式任务，同时保留先验知识。将多模式大型语言模型（MLLM）与可验证奖励强化学习（WLVR）相结合的新兴范式需要一种新的模式来指导持续适应。推理能力的进步现在使得在推理层面施加约束成为可能。我们正式化了可移植性，这是一种样本级别的衡量标准，衡量先前策略的行为在新任务中的可重复使用程度，并从经验上表明，推理级别的信号在非分布样本上仍然可靠，而答案级别的信号则不然。我们将其实例化为推理可移植性（RP），并提出基于推理的动态平衡连续学习（RDB-CL），它根据RP调节WLVR中的每样本Kullback-Leibler正规化：紧锚保留了高RP样本上的可重复使用推理，而低RP样本上的宽松锚则允许探索新的推理路径。实验表明，RDB-CL的表现始终优于基线，与普通的WLVR基线相比，Last准确性提高了+12.0%。

[阅读原文](https://arxiv.org/abs/2605.18903)

---

## 18. 基准测试和进化推理-反思-纠正，以实现反思视觉生成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junjie Wang, Xinghua Lou, Jason Li, Ye Tian, Keyu Chen, Yulin Li, Bin Kang, Jacky Mai, Yanwei Li, Zhuotao Tian, Liqiang Nie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a GRPO-based dual-stage framework with hierarchical reward for reflective visual generation, directly applying RL with verifiable rewards to improve generation.

**摘要**: arXiv：2605.19639v1宣布类型：新摘要：文本到图像（T2 I）模型和统一多模式模型（UMM）在视觉生成方面取得了显着进展。然而，他们对单程生成范式的依赖限制了他们处理需要迭代细化的复杂提示的能力。为了实现多轮反射视觉生成（RVG），我们将Reason-Reflect-Rectify（R^3）循环形式化为核心框架，并引入R^3-Bench，这是一个由600多个专家注释的实例组成的基准测试，可以量化迭代推理和校正功能。对R^3-Bench的评估揭示了一个关键的差距：虽然最先进的模型可以识别生成错误，但它们无法生成可操作的纠正指令。为了弥补这一差距，我们提出了R^3-Refiner，这是一个利用组相对策略优化（GRPO）和分层奖励机制（HRM）的双阶段框架，可以更好地将纠正与反射推理结合起来。实验表明，R^3-Refiner在R^3-Bench上实现了显著的改进（反射判决分数+12.0%，纠正分数+9.0%），并且可以与各种MLLM无缝集成，以提高GenEval++和T2 I-CompBench上不同T2 I模型的生成质量。代码可在https://github.com/xiaomoguhz/R3-Bench上获取。

[阅读原文](https://arxiv.org/abs/2605.19639)

---

## 19. 工具总是有益的吗？学习适应性地迭代工具以实现双模式多模式LLM推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qinghe Ma, Zhen Zhao, Yiming Wu, Jian Zhang, Lei Bai, Yinghuan Shi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning framework for MLLMs that adaptively decides whether to invoke tools, with dual-mode reasoning and mode-specific rewards.

**摘要**: arXiv：2605.19852v1宣布类型：新摘要：工具增强推理已成为增强多模式大型语言模型（MLLM）推理能力的一个有前途的方向。然而，现有的研究主要集中在使模型能够执行工具调用，而忽视了调用工具的必要性。我们认为，工具的使用并不总是有益的，因为多余或不当的调用在很大程度上增加了推理费用，甚至误导了模型预测。为了解决这个问题，我们引入了AutoTools，这是一种根据每个查询的特征自适应地决定是否调用工具的模型。在强化学习框架内，我们设计了一种具有特定模式奖励函数的显式双模式推理策略，以引导模型产生准确的响应。此外，为了防止过早地偏向单一推理模式，AutoTools在整个培训过程中联合探索和平衡工具辅助推理和文本中心推理，并促进后期的自由探索。大量的实验表明，AutoTool具有出色的性能和高效率，在V* 基准测试中，与基本模型相比，精度提高了21.8%，在POPE基准测试中，与现有的工具增强方法相比，效率提高了44.9%.代码可在https://github.com/MQinghe/AutoTool上获取。

[阅读原文](https://arxiv.org/abs/2605.19852)

---

## 20. VL-DPO：视觉语言引导的微调，用于偏好一致的自动驾驶

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhefan Xu, Ghassen Jerfel, Marina Haliem, Qi Zhao, Jeonhyung Kang, Khaled S. Refaat

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes VL-DPO, a vision-language-guided finetuning framework that uses a VLM as a zero-shot reasoner to generate preference pairs for DPO alignment of autonomous driving motion forecasting models.

**摘要**: arXiv：2605.20082v1宣布类型：新摘要：自动驾驶数据集的快速增长使得强大的运动预测模型能够扩展。虽然大规模预训练可以提供出色的性能，但标准模仿目标可能无法完全捕捉人类驾驶偏好的复杂细微差别。与此同时，视觉语言模型（VLM）的最新进展展示了令人印象深刻的推理和常识理解。在这些能力的基础上，本文提出了VL-DPO，这是一个视觉语言引导的框架，可以将自我车辆运动预测模型与人类偏好相匹配。我们的方法利用VLM作为零触发推理器，从预训练模型的展开中自动生成偏好对，然后使用这些偏好对通过直接偏好优化（DPO）微调模型。我们在Waymo开放端到端驾驶数据集（WOD-E2 E）上微调了我们的模型，并使用评级者反馈评分（RFS）和平均位移误差（ADE）针对已发布的人类偏好注释评估性能。我们的实验证实，VLM的轨迹选择是人类偏好的高质量代理。我们的最终模型VL-DPO比预训练模型的RFS增加了11.94%，ADE减少了10.01%。

[阅读原文](https://arxiv.org/abs/2605.20082)

---

## 21. CaptchaMind：通过强化学习和显式推理监督来训练CAPTCHA求解器

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Pengcheng Wang, Haoxiang Liu, Yang Dai, Xiangxiang Zeng, Guanhua Chen, Baotian Hu, Longyue Wang, Weihua Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an RL-based CAPTCHA solver trained with explicit reasoning process supervision, directly matching RL for LLMs via verifiable reward and reasoning supervision.

**摘要**: arXiv：2605.19538v1宣布类型：新摘要：CAPTCHA被广泛部署为人工验证机制，并且经常阻止智能代理在现实世界的网络环境中完成端到端自动化。解决现代CAPTCHA需要强大的多步骤视觉推理和交互能力，但由于缺乏大规模训练数据和流程级注释，基于训练的方法仍然缺乏。我们介绍了CaptchaBench，这是第一个旨在支持大规模训练的CAPTCHA基准测试，包括8个任务类别的16，000个编程生成的样本，以及详细的区域和过程级注释。对CaptchaBench的系统评估表明，现有方法在需要细粒度视觉细节捕获和区域级比较的任务上始终失败。因此，我们提出了CaptchaMind，一个基于RL的求解器，经过显式推理过程监督训练，在八个任务中实现了82.9%的平均成功率，在现实世界的实例中实现了71.0%的平均成功率，大大优于所有现有的方法，而无需闭源API。

[阅读原文](https://arxiv.org/abs/2605.19538)

---

## 22. 概率微小回归模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Amin Sghaier, Ali Parviz, Alexia Jolicoeur-Martineau

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Probabilistic TRM, a test-time compute scaling method that injects noise into latent recursion for stochastic exploration, directly addressing latent reasoning with a new mechanism.

**摘要**: arXiv：2605.19943v1宣布类型：新摘要：微型回归模型（TRM）通过迭代细化潜在状态和最终答案，用现代大型语言模型（LLM）参数的一小部分来解决复杂的推理任务。虽然功能强大，但它们的确定性回归可以导致收敛到次优解，而没有逃避机制。常见的解决方案依赖于测试时特定于任务的输入扰动，并结合通过投票进行的答案聚合。我们引入了Probabilitum TRM（PTRM），这是一个用于测试时计算扩展的任务不可知框架，通过随机探索解决了这一限制。PTRM在每个深度迭代步骤中注入高斯噪音，使平行轨迹能够探索不同的解盆地，并使用模型现有的Q头（用于原始TRM中的早期停止）进行选择。无需再培训或特定任务的增强，PTRM即可大幅提高基准测试的准确性，包括数独极限（87.4%至98.75%）和DeliverPuzzle Bench的各种谜题（62.6%至91.2%）。在后者方面，PTRM仅使用7 M个参数，以不到0.0001倍的成本实现了前沿LLM的近两倍的准确性（91.2% vs 55.1%）。

[阅读原文](https://arxiv.org/abs/2605.19943)

---

## 23. ClinSeekAgent：自动化多模式证据寻找以进行统计性临床推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Juncheng Wu, Letian Zhang, Yuhan Wang, Haoqin Tu, Hardy Chen, Zijun Wang, Cihang Xie, Yuyin Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improving agent framework for clinical evidence seeking that distills agent trajectories into smaller models, matching the self-evolving agent criterion.

**摘要**: arXiv：2605.20176v1宣布类型：新摘要：大型语言模型（LLM）和代理系统已经表现出了临床决策支持的希望，但现有的作品在很大程度上假设证据已经策划并交给模型。相反，现实世界的临床工作流程需要代理积极寻找、迭代规划和综合来自不同来源的多模式证据。在本文中，我们介绍了ClinSeekAgent，这是一个用于动态多模式证据寻求的自动化代理框架，它将范式从被动证据消耗转变为主动证据获取。仅在临床查询和原始数据源的情况下，ClinSeekAgent通过查询医学知识库、导航原始EHR和调用医学成像工具来收集证据;随着新信息的出现完善其假设;并将收集的证据整合到基础临床决策中。ClinSeekAgent既充当前沿LLM的推理时间代理，又充当将高质量代理轨迹提炼为紧凑的开源模型的训练时间管道。为了验证其推理时的有效性，我们构建了ClinSeek-Bench，它将来自固定预选证据的策展输入推理与原始临床数据的自动证据寻求配对。在纯文本EHR任务中，ClinSeekAgent将Claude Opus 4.6从60.0提高到63.2，将MiniMax M2.5从43.1提高到47.3，在9个评估的主机模型中，有7个的风险预测收益为正。在多模式任务方面，ClinSeekAgent将Claude Opus 4.6从47.5提高到62.6（+15.1）;所有评估的模型在三个CXR相关任务组中均得到改进。我们通过将代理证据寻求轨迹提炼到ClinSeek-35 B-A3 B中，进一步验证ClinSeekAgent作为培训管道，它在现有AgentEHR-Bench上实现了34.0的平均F1成绩，比Qwen 3.5 - 35 B-A3 B基线提高+11.9分，接近Claude Opus 4.6。

[阅读原文](https://arxiv.org/abs/2605.20176)

---

## 24. TextAlign：具有分层奖励的文本渲染的首选项对齐

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mingxuan Cui, Jingpu Yang, Fengxian Ji, Qian Jiang, Zhecheng Shi, Jiaming Wang, Zirui Song, Fajri Koto, Xiuying Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TextAlign, a post-training preference alignment framework with a hierarchical VLM-based reward for text rendering, using GRPO/DPO without modifying the generator architecture.

**摘要**: arXiv：2605.19320v1公告类型：新摘要：忠实的文本渲染仍然是大型文本到图像生成模型的一个持久弱点，因为它需要语义指令遵循和细粒度的字形级结构。先前的方法通常通过特定于架构的模块或编码器修改来提高这种能力，这使得跨基础模型的部署复杂化。我们将文本渲染作为训练后偏好对齐问题来研究，并提出了TextAlign，这是一种非侵入性框架，可以保持生成器架构不变。关键组件是基于分层视觉语言模型（VLM）的奖励，它将渲染错误分解为全局、单词和收件箱级别，然后将二进制缺陷判断转换为纯量偏好信号。由此产生的信号支持集团相对政策优化（GRPO）和直接偏好优化（DPO）。FLOX.1-dev和Z-Image-Turbo上的实验显示，基于OCR的文本准确性在不降低一般生成质量的情况下取得了一致的提高。与强大的基础和文本渲染基线（包括SD 3.5、Qwen-Image、Anytext和TextDistuser）相比，这些结果表明奖励设计为改进文本渲染提供了模型重新设计的可扩展替代方案。

[阅读原文](https://arxiv.org/abs/2605.19320)

---

## 25. 超越动作残留：通过瓶颈潜在强化学习实现现实世界的机器人政策引导

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dongjie Yu, Kun Lei, Zhennan Jiang, Jia Pan, Huazhe Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ZPRL, a novel RL method that steers pretrained robot policies via a bottleneck latent representation, improving sample efficiency and final performance.

**摘要**: arXiv：2605.19919v1宣布类型：新摘要：预训练的模仿策略已成为机器人操作的坚实基础，但它们通常需要在线改进来克服执行错误、有限的数据集覆盖范围和部署不匹配。因此，一个核心问题是强化学习（RL）在离线预训练后应如何调整策略。现有的轻量级方法通常直接在动作空间中应用残余修正，但这通常会导致探索噪音大且结构不良。在这项工作中，我们提出了Z-扰动强化学习（ZSPL），这是一种通过紧凑的潜在瓶颈而不是通过策略权重或输出动作来引导预训练的策略的方法。在离线训练期间，我们通过即插即用的变分信息瓶颈（SAL）模块来增强策略，以从观察嵌入中提取与任务相关的潜在界面。在在线微调期间，基本策略被冻结，RL仅学习该潜在策略上的剩余扰动，其解码的表示条件是冻结动作生成器。我们在流匹配策略上实例化ZSPL，并在八个模拟任务和四个现实世界任务上对其进行评估。在不同的操作设置中，ZSPL在强大的训练后基线上提高了样本效率和最终性能。在现实世界中，与模仿基础策略相比，ZSPL将四项任务的平均成功率提高了33.7%，同时比动作剩余策略产生更流畅的探索行为。这些结果表明，紧凑的、与任务一致的瓶颈潜在为在线RL适应提供了有效的界面。更多视频请访问https://manutdmoon.github.io/ZPRL/。

[阅读原文](https://arxiv.org/abs/2605.19919)

---

## 26. 细化离散扩散语言模型的目标漂移

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Daisuke Oba, Hiroki Furuta, Naoaki Okazaki

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TokenDrift, a drifting objective for discrete diffusion language models that improves generation quality by lifting categorical predictions to soft-token features and applying anti-symmetric drifting, directly relevant to RL for LLMs via a novel training refinement method.

**摘要**: arXiv：2605.19470v1宣布类型：新摘要：离散扩散语言模型（DDLM）通过迭代对类别标记序列进行去噪来生成文本，而最近的连续生成器漂移方法表明，这种采样时纠正的一部分可以通过反对称定点目标吸收到训练中。我们研究如何将这一原则转移到DDLM，其中的主要挑战是与离散文本的接口：硬标记样本是不可微的，并且分类预测不会直接提供连续样本来漂移。我们制定TokenDrift，这是一个漂移目标，它将类别预测提升到软令牌特征，在冻结的语义空间中应用反称漂移，并将生成的停止梯度特征目标反向传播到DDLM logit。在具有掩蔽和均匀状态扩散主干的受控连续训练实验中，TokenDrift在匹配的连续基线上提高了固定NFE生成质量，从而减少了Gen.- 4个NFE的PPL在MDLM上下降了89%，在DUO上下降了86%。这些结果表明漂移可以为DDLM提供实际的细化目标。

[阅读原文](https://arxiv.org/abs/2605.19470)

---

## 27. GeoX：通过自我游戏和可验证的奖励掌握地理空间推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kyeongjin Ahn, Seungeon Lee, Krishna P. Gummadi, Meeyoung Cha

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-play RL framework with verifiable rewards for geospatial reasoning, directly matching RL for LLMs and self-improving agents.

**摘要**: arXiv：2605.20006v1宣布类型：新摘要：地理空间推理需要解决场景复杂空间结构上的基于图像的问题。然而，开发这种能力受到注释庞大且组合问题空间的成本的阻碍。我们提出了GeoX，这是一个自玩框架，通过产生可验证奖励的可执行程序来获取空间逻辑，而不依赖于大规模人类策划的数据。给定一张卫星或航空图像，我们的框架采用单一的多模式策略，将空间问题提出为可执行程序，并在三种推理模式下解决它们--推衍、演绎和归纳--空间基元和图像理解工具。验证者执行每个程序以隐藏奖励信号，通过强化学习联合优化这两个角色。GeoX持续将其基本VLM平均提高了5.5个百分点，与基于数百万精心策划的数据训练的传统基线相当或超过。除了提出的方法之外，我们还发布了通过自我游戏积累的地理空间理解基准。

[阅读原文](https://arxiv.org/abs/2605.20006)

---

## 28. ReCrit：用于科学批判性推理的转换感知强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wanghan Xu, Yuhao Zhou, Hengyuan Zhao, Shuo Li, Dianzhi Yu, Zhenfei Yin, Yaowen Hu, Fengli Xu, Wanli Ouyang, Wenlong Zhang, Lei Bai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ReCrit, a transition-aware RL framework for LLMs that uses a novel reward design to improve critic reasoning by penalizing sycophancy and rewarding correction.

**摘要**: arXiv：2605.18799v1宣布类型：新摘要：大型语言模型可能会在批评者互动中失败，不仅是因为回答错误，而且还因为在用户批评后放弃了最初正确的科学解决方案。这在科学推理中尤其危险，因为用户的批评可能会将有效答案变成不正确的答案。我们将评论家的互动定义为一个回合间的正确性过渡问题，而不是最终答案的准确性问题，并确定了三个挑战：过渡意识、将有用的纠正与有害的谄媚脱钩以及可扩展的推出。我们提出了ReCritt，这是一个过渡感知强化学习框架，它将初始到批评的行为分解为四个象限：纠正、奉承、稳健和边界。ReCrit奖励纠正和稳健性，惩罚谄媚行为，并将持续错误视为弱边界信号。为了使交互训练变得实用，ReCrt进一步使用动态同步推出和尾部自适应完成来减少推出等待。在ChemBench、TRQA和EarthSE三个科学推理基准上，ReCrt将Qwen 3.5 - 4 B的平均Critic准确性从38.15提高到51.49，Qwen 3.5 - 9 B的平均准确性从45.40提高到55.59。消融表明，最终答案奖励几乎没有提供交互级别的收益，而过渡感知奖励和象限加权产生更可区分的训练信号和更大的净关键阶段改进。该代码可在https://github.com/black-yt/ReCrit上获取。

[阅读原文](https://arxiv.org/abs/2605.18799)

---

## 29. 语义丰富的潜在视觉推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tianrun Xu, Yue Sun, Qixun Wang, Jingyi Lu, Yuan Wang, Tianren Zhang, Longteng Guo, Fengyun Rao, Jing Lyu, Feng Chen, Jing Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage framework for semantic-enriched latent visual reasoning with a new RL alignment method (M-GRPO), directly targeting latent reasoning.

**摘要**: arXiv：2605.19342v1宣布类型：新摘要：多模式潜在空间推理旨在通过直接在紧凑的潜在空间中进行视觉推理，用图像取代显式思维。然而，现有的方法在很大程度上依赖于视觉监督，并产生缺乏足够语义丰富性的潜在表示，限制了它们支持不同区域级推理任务的能力。在这项工作中，我们引入了语义丰富的潜在视觉推理（SL VR），这是一个两阶段学习框架，通过属性级视觉语义丰富潜在表示，并将它们与不同的推理目标保持一致。在第一阶段，BLVR在细粒度属性监督下学习语义丰富的以区域为中心的潜伏。在第二阶段，我们设计多查询组相对策略优化（M-GRPO），以将位于同一区域的多个查询之间的潜在表示对齐。为了支持这个框架，我们构建了SLV-Set，其中包括大约40万个区域级属性注释和80万个多查询问答样本，并引入了SV-QA，这是一个评估语义变化下潜在推理的基准。实验表明，与现有基线相比，SL VR提高了潜在视觉推理的鲁棒性和语义一致性。

[阅读原文](https://arxiv.org/abs/2605.19342)

---

## 30. 当它偏离时回溯：减轻LLM推理蒸馏中的双重暴露偏差

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Bing Wang, Shaotian Yan, Chen Shen, kaiyuan liu, Sinan Fan, Ximing Li, Rui Miao, Xiaosong Yuan, Zhanming Shen, Jieping Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MOTAB, a new distillation pipeline that addresses dual exposure biases in LLM reasoning distillation via dynamic monitoring and backtracking with teacher intervention, directly improving reasoning via a novel training loop.

**摘要**: arXiv：2605.19433v1宣布类型：新摘要：大型语言模型（LLM）通过长思想链（CoT）在复杂推理任务中取得了显着成功，但其巨大的计算负担阻碍了现实世界的部署。LLM推理提炼通过将推理能力从强大的教师模型转移到紧凑的学生模型来解决这个问题。然而，现有的蒸馏范式面临着根本性的困境。典型的非政策蒸馏严格利用教师生成的黄金轨迹，由于训练分布和学生生成的推理上下文之间的不匹配而遭受暴露偏差，从而导致长CoT推理中的错误级联。为了解决这个问题，政策上的提炼允许学生探索自己的轨迹，但我们证明它本质上会引入一种互惠的反向暴露偏差：当以学生生成的次优环境为条件时，教师模型也很难提供积极的指导。为了解决这个双重暴露偏差问题，我们提出了监测轨迹并在它偏离时回溯（MOTAB），这是一种新的LLM推理蒸馏管道。具体来说，MOTAB根据自适应安全边界动态监控学生的政策生成情况。当一代人偏离并超过此阈值时，MOTab会倒退到上一个安全状态，并利用教师干预来纠正课程。这种方法本质上容忍学生的小错误以减轻暴露偏见，同时防止次优环境以规避反向暴露偏见。对LIMO-v2和AceReason数据集的大量实验表明，MOTAB有效地减轻了双重暴露偏差，使推理任务的平均性能提高了约3%。

[阅读原文](https://arxiv.org/abs/2605.19433)

---

## 31. 提取什么以及何时提取：多转代理的选择性事后诸葛亮蒸馏

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xiaozhe Li, Tianyi Lyu, Yang Li, Yichuan Ma, Peiji Li, Linyang Li, Qipeng Guo, Dahua Lin, Kai Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SERL, a selective environment-reweighted RL framework for multi-turn LLM agents that uses per-step environmental feedback for credit assignment, directly matching the RL for LLMs and self-improving agents criteria.

**摘要**: arXiv：2605.19447v1宣布类型：新摘要：强化学习可以根据稀疏任务奖励来训练LLM代理，但长期信用分配仍然具有挑战性：单个成功或失败信号必须分布在许多动作中。现有的方法依赖于车间级奖励或代理信号，而没有充分利用每一步的环境反馈。多回合代理设置未充分探索，其中反馈可能包括错误消息、页面更改、观察或参考轨迹。我们系统地研究了五种反馈源和两种插入粒度，并引入SERL，这是一种选择性环境重新加权的学习框架。SERL使用任务奖励来确定更新方向，而环境反馈则调整位置和幅度，重点关注关键行动。在ALFWorld和WebShop上，SERL取得了90.0%和80.1%的成功率，超过了强劲的RL和蒸馏基线。分析表明，在有意义的时刻进行有针对性的、与行动相关的反馈始终优于不加区别地使用更长或更丰富的背景。

[阅读原文](https://arxiv.org/abs/2605.19447)

---

## 32. MOCHA：多目标Chebyshev Annealing for Agent技能优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Md Mehrab Tanjim, Jayakumar Subramanian, Xiang Chen, Branislav Kveton, Subhojyoti Mukherjee, Anlan Zhang, Sungchul Kim, Somdeb Sarkhel, Sunav Choudhury

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces MOCHA, a multi-objective Chebyshev annealing method for optimizing LLM agent skills under platform constraints, directly addressing agent skill optimization with a novel Pareto-front approach.

**摘要**: arXiv：2605.19330v1宣布类型：新摘要：LLM代理通过技能组织行为-结构化的自然语言规范来管理代理如何推理、检索和响应。与单一提示不同，技能是受硬平台约束的多字段产物：描述字段被截断以进行路由，指令体通过渐进式披露而压缩，并且共存技能竞争有限的上下文窗口。这些约束使得技能优化本质上是多目标的：技能必须同时最大化任务性能并满足平台限制。然而，现有的即时优化器要么忽略这些权衡，要么将它们折叠成加权和，从而在非凸目标区域中错过帕累托最优变体。我们引入了MOCHA（多目标切比雪夫Annealing），它用切比雪夫标度化取代单目标选择（覆盖整个帕累托前沿，包括非凸区域），结合了从探索过渡到利用的指数退变。在我们针对六种不同代理技能的实验中--所有方法共享相同的多目标突变操作符，基线接收相同的每目标文本反馈--现有的优化器未能提高6项任务中4项的种子技能：1000次部署产生零进展。MOCHA在每项任务上都取得了突破，平均正确率比最强基线实现了7.5%的相对提高（FEVER最高可达14.9%，TheormQA最高可达10.4%），同时发现了两倍的帕累托最优技能变体。

[阅读原文](https://arxiv.org/abs/2605.19330)

---

## 33. 不要让强盗的反馈导致LLM推荐人的持续更新偏离目标

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Taesan Kim, Hyeongjun Yun, Jaegul Choo, Chung Park

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (ABPO) for continual LLM-Rec updates that combines GRPO with exposure bias correction and asymmetric feedback handling, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2605.18899v1公告类型：新摘要：生成的基于LLM的标记（LLM-Rec）需要持续的部署后更新，但部署日志只提供策略形的上下文强盗反馈：结果只观察到由先前的服务策略暴露的项目，诱导暴露偏差，并产生部分，不对称的信号，包括相对可靠的积极响应和模糊的无响应。我们提出了一个锚定的强盗政策优化（ABPO）框架，持续LLM-Rec更新，结合组相对的政策优化（GRPO）与曝光偏差和反馈模糊性的明确治疗。具体来说，我们将公开的建议作为已记录的锚点插入到每个GRPO推出组中，以便针对先前策略实际公开的操作而不是仅针对新采样的推出来校准组相对规范化。由于只有通过先前的政策暴露才能观察到积极的反应和无反应，因此我们对两种反馈类型的固定锚点应用自标准化的反向倾向评分，以纠正政策不匹配。与此同时，我们在可靠性上不对称地对待这两种反馈类型：积极的反应提供了相对直接的认可信号，而无反应仍然模糊，因为它们可能反映了真正的不感兴趣或未观察到的外部因素。为了避免模糊的无响应带来的过于激进的更新，我们通过自我确定性来缓和它们的惩罚，使用模型的输出令牌置信度作为无验证器的可靠性信号。在Amazon Reviews和MovieLens的五个领域中，我们的方法在推荐准确性方面获得了一致的更新后收益，同时比之前的基线更有效地减轻了先前政策引起的暴露偏差。

[阅读原文](https://arxiv.org/abs/2605.18899)

---

## 34. 用于CAD生成的内存增强强化学习代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yin Xiaolong, Liu Yu, Shen Jiahang, Lu Xingyu, Ni Jingzhe, Fan Fengxiao, Sang Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a memory-augmented RL framework for CAD generation agents with self-correction and continual evolution, matching both RL for LLMs and self-improving agents criteria.

**摘要**: arXiv：2605.19748v1公告类型：新摘要：计算机辅助设计（CAD）模型的自动生成是实现先进制造智能化的核心技术。现有的基于大型语言模型（LLM）的生成方法在处理具有长操作序列、多样操作类型和强几何约束的复杂CAD模型时往往存在不足，主要原因是推理链断裂和缺乏有效的纠错机制。为了解决这个问题，本文提出了一个记忆增强的强化学习框架的CAD生成代理。该框架将底层几何内核封装成可由Agent调用的结构化工具链，并构建了设计意图理解、全局规划、执行和多维验证的闭环机制。设计了由案例库和技能库组成的双轨记忆模块，提出了动态效用检索算法。通过将强化学习引入到检索和策略优化中，Agent可以有效地避免语义相似但几何不可行的检索陷阱，从而实现在线自我校正和持续进化，而无需额外的大规模注释数据。实验结果表明，该方法在复杂CAD模型生成任务中显著提高了模型生成的成功率和几何一致性。

[阅读原文](https://arxiv.org/abs/2605.19748)

---

## 35. TEMPO：通过模式分离的政策优化进行临时强制执行值得信赖的LLM回溯测试

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zeyu Zhang, Bradly C. Stadie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TEMPO, a GRPO-based RL training pipeline with a two-mode reward to enforce temporal discipline in LLMs, directly matching RL for LLMs via novel reward design and scalable RL training.

**摘要**: arXiv：2605.18843v1宣布类型：新摘要：对历史事件的大型语言模型进行回测需要完全根据指定截止日期之前的可用信息进行推理。然而，模型经常会将预训练中的截止后知识泄露到它们的推理中，夸大了明显的准确性并破坏了评估的有效性。当被抑制的内容与预测有因果关系时，基于时间的约束失败，并且知识遗忘无法解决这个问题，因为时间依从性是特定于实例的：相同的事实可能是一个截止日期的合法证据，而另一个则是违规。模型必须学习时间纪律，而不是删除知识：选择以每个实例的截止日期为条件的证据。我们提出了TEMPO（通过模式分离策略优化的时间执行），它通过两个贡献来训练这一学科：（1）一个双模式奖励，其中泄漏模式将截止后声明驱动为零，作为性能模式优化任务性能之前的硬性先决条件;以及（2）基于GRPO的训练管道，使模型能够发现时间有效的推理策略。我们证明，训练单调减少泄漏，收敛到无泄漏的最佳，并提高任务性能，一旦实现合规。在三个预测任务和两个模型中，TEMPO在所有条件下将泄漏量从2~13%减少到0.6~3.7%，在存在强截止前信号并维持的情况下，任务性能提高了6~13%，而预测任务本身就很难仅从有效信息中进行。

[阅读原文](https://arxiv.org/abs/2605.18843)

---

## 36. 通过全回路Transformer简单地稳定回路

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Rao Fu, Zixuan Yang, Jiankun Zhang, Jing Ma, Hechang Chen, Yu Li, Yi Chang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Fully Looped Transformer with parameter-free modifications to stabilize training of looped architectures, enabling latent iterative computation without explicit CoT.

**摘要**: arXiv：2605.18797v1宣布类型：新摘要：扩展模型性能通常需要增加模型尺寸。Looed Transformer通过迭代重复使用相同的Transformer块，提供了一种引人注目的替代方案，在不增加参数计数或上下文长度的情况下牺牲额外的计算来提高性能。由于循环迭代次数可以在推理时调整，因此它还提供了一种自然的机制来平衡性能和测试时计算。然而，当循环迭代次数增加时，Looped Transformer仍然会受到训练不稳定性的影响。我们的分析表明，这种不稳定性源于两个来源：梯度振荡和残余爆炸。为了解决这两个问题，我们提出了Full Looped Transformer，它引入了两个无参数的修改：（1）Full Looped Architecture，它将环间信号分布在所有层中以减轻残余爆炸;（2）注意力注入，它重复使用现有的注意力块来抑制梯度振荡。这些修改稳定了训练动态，使Full Looped Transformer能够稳定训练多达12次循环迭代，而其他基线循环模型在此状态下崩溃。在Looped Transformer不会崩溃的较温和设置中，Fully Looped Transformer仍能将平均下游任务性能提高13.2%。总体而言，我们的实验表明，Full Looed Transformer提高了训练稳定性，增强了下游性能，并通过在推理时改变循环迭代来提供不同测试时计算预算下的初步适应性。

[阅读原文](https://arxiv.org/abs/2605.18797)

---

## 37. 当大多数人投票错误时，测试时强化学习的干预时间隐藏在灭绝窗口中

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hongxiang Lin, Zhirui Kuai, Erpeng Xue, Lei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TTRL-Guard, a novel test-time RL framework with reward scaling and sampling mechanisms to mitigate majority vote errors in LLM reasoning.

**摘要**: arXiv：2605.19444v1宣布类型：新摘要：测试时强化学习（TTRL）报告了使用多数票作为伪标签信号的数学推理基准的准确性大幅提高。我们认为，这些收益被系统性地误解了：大多数收益反映了已经解决的问题的尖锐化，而不是真正的学习，而从正确到不正确的问题数量超过了真正学到的问题，一旦多数票锁定了错误的答案，这种损害就是不可逆转的。逐个问题跟踪显示，低能力问题中的正确答案信号在被永久抑制之前会短暂活跃，我们将这种现象称为\textit{Correct-Answer Extinction窗口}，以翻转率（FR）作为其领先指标。因此，我们提出了\textBF{TTRL-Guard}，这是一个轻量级框架，具有三种针对灭绝窗口的机制：翻转率感知奖励缩放（FSG）随着FR下降而降低风险更新的权重，少数族裔保留采样（MPS）保留少数族裔正确答案的梯度信号，风险条件稀疏更新（RCSU）暂停对两极分化问题的更新。三种型号和四个基准测试的实验表明，TTRL-Guard在Qwen 2.5 - 7 B-Direcct和Qwen 3 - 4 B上实现了最佳平均通过率@1，在AIME 2025上比TTRL相对提高了+54%%。\脚注{我们的代码和实现详细信息可在https://github.com/linhxkkkk/TTRL-Guard上获取。

[阅读原文](https://arxiv.org/abs/2605.19444)

---

## 38. Lambda PO：推理语言模型的Lambda风格策略优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhe Yuan, Yipeng Zhou, Jinghan Li, Xinyuan Chen, Bowen Deng, Zhiqian Chen, Liang Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces LambdaPO, a novel RL policy optimization method that replaces scalar advantage with decomposed pairwise preferences for improved reasoning LLM alignment.

**摘要**: arXiv：2605.19416v1宣布类型：新摘要：群体相对政策优化（GRPO）已成为现代强化学习对齐的基石，因其通过利用抽样轨迹队列之间的奖励标准化来消除明确的价值批评者而受到重视。然而，该方法对单一统计基线（例如群体平均值）的依赖将轨迹空间的关系布局折叠为单个纯量，从而消除了导航复杂、等级敏感的奖励景观所必需的细粒度偏好信息。为了解决这个问题，我们引入了一个新的框架，Lambda策略优化（LambdaPO），通过将优势估计从标量值重新概念化到分解的成对偏好结构来解决这个信息理论瓶颈。具体而言，任何给定轨迹的优势被公式化为针对其队列中的所有对等体的奖励差异的综合总和，其中每个成对比较被策略在所建立的偏好中的自身概率置信度动态衰减。为了进一步减轻二进制结果监督的稀疏性，我们使用语义密度奖励来增强目标，该奖励来自生成的推理痕迹和地面实况解决方案之间的精确召回对齐。因此，我们的方法可以从一组推出中挖掘更多细粒度的优化信号，引导LLM达到更好的最优。具有挑战性的数学推理和问答任务的实验结果表明，与基线方法相比，Lambda PO提高了性能。

[阅读原文](https://arxiv.org/abs/2605.19416)

---

## 39. 食谱：通过教学视频中的基础进行程序规划

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Luigi Seminara, Antonino Furnari, Lorenzo Torresani

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RECIPE, which uses grounding quality as a reward for GRPO to improve procedural planning from noisy instructional video, directly matching RL for LLMs via verifier-driven optimization.

**摘要**: arXiv：2605.19976v1宣布类型：新摘要：视觉规划要求模型在给定部分视频上下文和目标的情况下用自然语言生成过程的剩余步骤。此任务的进展由注释来检查：干净的标记数据集很小、域窄，并且每个示例编码单个执行轨迹，尽管存在许多有效的顺序。大规模教学视频库提供了数量级更多的程序性内容，但对伪标签进行有监督的微调会传播分割和对齐错误并保持单一轨迹。我们发现了一个关键的不对称性：从有噪的视频中提取干净的步骤标签很困难，但验证生成的步骤序列是否在时间上植根于ASB文字记录中很便宜，并且可以通过预先计算的文本嵌入扩展到数百万个视频。我们在RECPEN中利用了这种不对称性，它使用基础质量作为GRPO的奖励，将有噪音的数据库变成验证者而不是标签源。该框架统一适用于两种规划者输入配置（苏格拉底，具有通过冻结VLM提取的文本历史，以及视频，直接消费视频令牌）以及注释和弱监督的制度。我们使用基于参考的LLM作为法官的协议评分计划，针对6个程序标准对7个程序基准进行评估。RECIPE-RL在所有尺度（0.5B、3B、7 B）和每个基准上都比基本检查点有所改进，宏观准确性提高为+7至+8分，零射击最多为+16分。它在带注释和伪标签的计划上的性能优于监督微调（后者会降低基础），并且在没有人为注释的情况下仍然保持稳健。用作先前提议-评估-搜索规划器的提议阶段，它在视觉规划协助上的每个地平线上都比最强的零射击基线有所改进，而在COIN上，它保留了SFT崩溃的世代多样性。

[阅读原文](https://arxiv.org/abs/2605.19976)

---

## 40. 预训练之外的重新思考μ子：VLA和WLVR的光谱故障和高通补救措施

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chongyu Fan, Gaowen Liu, Mingyi Hong, Ramana Rao Kompella, Sijia Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Pion, a new optimizer for RLVR post-training that addresses spectral failures of Muon, directly improving LLM behavior via reward-driven optimization.

**摘要**: arXiv：2605.19282v1宣布类型：新摘要：Muon是一个矩阵感知优化器，它利用Newton-Schulz（NS）迭代来通过将动量矩阵的所有奇异值驱动为1来实施谱梯度正交化。虽然这种均匀的频谱白化增强了探索并在LLM预训练中优于AdamW，但我们表明它可能会在两种方案中导致预训练之外的根本限制：（i）跨模式视觉-语言-动作（VLA）训练，其中固有的低等级动作模块梯度会导致有噪音的尾部方向的放大，和（ii）具有可验证奖励的强化学习（WLVR），其中，低SNR梯度和保留先前训练的人均专业化的需要导致白化不稳定。为了应对这些挑战，我们提出了Pion，这是Muon的直接替代品，它保留了其计算效率，同时用两阶段的促进+抑制机制（我们称之为高通NS迭代）取代均匀频谱白化。该设计引入了尖锐的频谱高通效应，将主导奇异值锚定在1，同时通过可控的过滤器强度将有噪的尾部分量抑制为0。为了保留预先训练的按头的多样性，Pion还支持按头模式，通过简单的重塑在注意力头之间独立应用更新，无需额外费用。在LIBERO和LIBERRO-Plus上的VLA训练中，Pion在l_1回归（VLA-Adaptor）和流匹配（VLANeXt）架构中始终优于基线，例如，使用VLA-Adaptor进行1，500个训练步骤后，LIBERO对象的成功率达到100%，而Muon的成功率为97.0%，AdamW的成功率仅为32.2%。Pion的优势进一步扩展到真正的Franka Research 3机器人，该机器人在DROID设置下具有pi_0.5主干，可执行三项抓取和放置任务。在使用GRPO和GMPO在Qwen 3 -1.7B/4 B上进行的RLVR后训练中，Pion在MATH和GSM 8 K上的表现也优于AdamW，而Muon则崩溃为零。

[阅读原文](https://arxiv.org/abs/2605.19282)

---

## 41. 驯服思想者：自适应LLM推理的条件熵整形

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shuyu Wei, Jian Sun, Delai Qiu, Yining Wang, Shengping Liu, Jiaen Liang, Ying Fu, Wei Huang, Jitao Sang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Conditional Entropy Shaping (CES), a novel RL-based framework using token-level entropy as a reward signal to dynamically control LLM reasoning depth, directly matching RL for LLMs.

**摘要**: arXiv：2605.19358v1宣布类型：新摘要：基于信息量的深度推理已成为提高大型语言模型（LLM）推理能力的一个有希望的方向，但现有方法往往要么不加区别地增加响应长度，要么以牺牲准确性为代价缩短响应。为了更好地平衡这种权衡，我们引入了条件性Entropy Shaping（CES），这是一个动态控制代币级响应熵的框架，使LLM能够对简单问题产生简洁的解决方案，同时鼓励对困难问题进行更深入的探索。CES以DAPO为基础，使用代币级的熵作为不确定性信号，并应用有条件的双向政策：它惩罚正确推理路径上的高熵“分叉点”代币，以提高简洁性，并在错误路径上奖励它们，以鼓励探索和错误纠正。我们在DeepSeek-R1-Distill-7 B上实施CES，并在12个数学基准上对其进行评估。相对于DAPO，CES持续提高了平均准确性，同时缩短了响应长度，补充实验在较小的1.5B主干网和域外基准上也显示了类似的趋势。

[阅读原文](https://arxiv.org/abs/2605.19358)

---

## 42. 使用强化学习的文本到SPARQL生成：DBLP上基于GRPO的方法

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Jann Pfeifer, Debayan Banerjee, Ricardo Usbeck

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO (a reinforcement learning method) with outcome-based rewards to train a small LM for zero-shot Text-to-SPARQL, demonstrating RL for LLM alignment in a structured generation task.

**摘要**: arXiv：2605.20066v1宣布类型：新摘要：知识图问答旨在将自然语言问题翻译为知识图上的可执行查询，但现有方法通常依赖于大型模型或黄金查询注释形式的全面监督。这项研究考察了具有基于结果的奖励的强化学习是否可以训练一个小型的描述调优语言模型，以在学术领域执行零次文本到SPARQL生成。组相对政策优化（GRPO）应用于DBLP-QuAD上的Qwen 3 -1.7B模型，使用将自然语言问题与有关实体和关系的符号提示相结合的提示。培训依赖于执行反馈、结构约束和答案水平奖励，还有一个包含基于黄金查询的塑造的变体。将所得模型与未修改的零射击基线和监督DoRA微调基线进行比较，涵盖回答水平准确性、执行准确性、类别得分和对已发布模板的概括。GRPO在零射击基线上大幅改进，并表现出有竞争力的概括性，而监督式DoRA微调在相同的模型规模上实现了更高的总体准确性。消融分析表明，基于执行的奖励占了大多数收益，而额外的塑造产生的额外收益有限，这表明当黄金查询无法用于代币级监督时，基于结果的强化学习是一种可行的训练策略。

[阅读原文](https://arxiv.org/abs/2605.20066)

---

