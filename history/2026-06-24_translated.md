# 💡 今日研究速览 (Daily Summary)

# LLC和推理的RL

当今的一个主导主题是来自可验证奖励的强化学习（WLVR）作为推进LLM推理的核心范式的成熟。多篇论文提供了理论和实践突破。一项关键理论结果严格证明，WLVR能够在推理中进行高效回溯，以指数级方式优于监督微调（SFT），并证明这些习得的行为可以根据策略进行提炼。在方法论方面，我们看到复杂的奖励设计和训练稳定技术的激增。EvoRubrics等新型框架引入了动态、协同进化的奖励生成，以避免开放式任务中的奖励黑客攻击，而ACOER则为GRPO提出了自适应奖励塑造，以通过隔离简洁性奖金来稳定效率训练。SPIRAL框架训练模型以端到端学习和混合顺序、并行和聚合推理基元，SAS利用GRPO来学习扩散语言模型中的最佳解封顺序。此外，对WLVR更新机制的全面分析导致了ACPO，这是一种基于重要性抽样方差的自适应剪裁方法，其性能优于DAPO等现有算法。该领域还在扩展到多模式领域，CFPO强制执行视觉感知和文本推理之间的因果一致性，而AIR在MLLM中使用群体约束奖励进行自适应交织代码推理。最后，终端代理和自动代码合规等特定领域应用程序的实用食谱正在发布，巩固了WLVR作为通用推理引擎的地位。

# 政策提炼和知识转移

LLM RL中的一个关键子领域正在受到密切关注：政策上的提炼。今天的论文共同解决了其根本性的低效和偏见。严格的经验证明，基于搜索的推理程序无法提炼成忠实的前向思维链，从而对提炼可以实现的目标设定了根本限制。为了解决实际挑战，研究人员识别并正式确定了政策提炼中的立场偏差，并提出了一个有原则的重要性加权目标来缓解它。新的方法正在出现来提高转移推理的质量：亲爱的通过利用学生的不确定性和师生分歧来发现并转移决策和证据代币，而ReNIO则使用概率比重新加权负轨迹，以改进即使是来自不正确的解决方案的学习。一项全面的、公式驱动的调查提供了统一的分类法，引入了时间信用和词汇路由等概念，并提出了新颖的算法（GAE-OPD、CR-OPD）来指导未来的研究。关键的见解是超越简单的模仿，转向更有原则的、有信用分配的推理过程转移。

# 多模式推理和视频语言模型

多模式推理正在取得重大进展，特别是在理解视觉感知和语言生成之间的相互作用方面。一项对多模式WLVR的批判性研究表明，视觉快捷方式是形成的，并且可以逆转，但表现出滞后，这意味着奖励强度控制着训练的关键干预窗口--这一发现对奖励设计具有直接影响。在架构方面，VideoLatent引入了一种潜在推理MLLM，具有一种新颖的自我强迫训练范式，与用于视频理解的显式思维链方法相比，可以实现巨大的效率提升。对于数学推理，VeriEvol提供了一个可扩展、可验证的数据构建框架，使用类型感知进化和假设测试证伪，为多模式数学中的RL提供动力。基于RL的CFPO框架通过强制执行视觉输入和文本推理链之间的因果一致性，进一步提高了推理的保真度。

# 偏好一致和强化学习理论

除了WLVR之外，偏好一致的理论基础正在加深。一种新颖的偏好匹配马尔科夫链方法直接使用成对偏好，而无需纯量奖励模型，提供理论上的收敛保证。这在基于排名的目标和强化学习之间提供了正式的桥梁。此外，免训练解码策略Confident Layer Decoding动态选择接近最终的层以绕过对齐扰动，直接改进对齐LLM中的推理，并强调“对齐税”是一种可以在推理时减轻的潜在层现象。

# 强调和长期强化学习

对于代理机构来说，长期信用分配仍然是一个核心挑战。G2 PO算法提出了一种基于组的RL方法，该方法使用全局状态转移图来改进复杂、多步骤任务中的信用分配和价值估计。与此相辅相成的是，TW食谱提供了一个实用的开放框架来训练终端代理，强调了数据生成和验证者多样化的新颖分类法。最后，自适应数据调度（ADS）引入了RL后训练的双层调度框架，用自适应集群级和策略边界选择取代统一采样，应用于GRPO时推理基准提高了5.2%--这一发现对所有基于RL的LLM训练的效率具有广泛影响。

---

## 1. 可验证的搜索不是可学习的思想链

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 9/10

**作者**: Harsh Patel

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a rigorous empirical demonstration that search-based reasoning procedures cannot be distilled into a faithful forward chain-of-thought, with implications for RL from verifiable rewards and on-policy distillation.

**摘要**: 人们很容易认为，任何可以通过短程序解决的任务都可以作为模型的思想链来教导模型：写下步骤，微调，然后模型就会遵循。本文表明，对于一类可识别的程序，该假设是不成立的。测试床由九个推理任务组成，每个任务来自一个确定性生成器;公共和隐藏的拆分共享生成器，因此提供的数据代理测试准确性。我将生成器反向工程为Python解算器，将它们渲染为思想链，并在30 B（3.5B活跃）Nemotron模型上提炼为rank-<= 32 LoRA。可向前计算任务易于安装：查找/算术和8位布尔任务传输（>= 0.99和0.68）。加密算法不：尽管搜索求解器回答了71%的实例，但在11个思想链设计、来自可验证奖励的RL和自我训练中提取其回溯搜索保持率为0.01-0.07。这不是能力差距。该模型对97-100%的行进行算术运算，并将正确的密码排在前八名中的71%;它无法将搜索作为从左到右的派生进行。微调学习可验证的消除步骤的形状，而其判决则成为无条件模板，只有16-57%的时间正确（“判决即代币”）。上限跨越从3B到671 B的主干以及微调和提示;受控干预隔离了原因：揭示加密密钥，使推导向前发展，将相同的实例从0.03提升到0.57。当一个过程的唯一解决方案是搜索无信息结构时，就不存在可模仿的忠实前向思维链。只有通过删除搜索、将其组合核心预计算到目录中并减少召回和验证的痕迹，该任务才能学习;通过这种方式，第一位的解决方案达到了Private LB 0.92。提炼出来的是记忆和验证，而不是搜索。

[阅读原文](https://arxiv.org/abs/2606.21884v1)

---

## 2. EvoRubrics：通过LLM强化学习的对抗协同进化的动态规则作为奖励

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Hongxin Ding, Baixiang Huang, Yue Fang, Weibin Liao, Zheng Li, Jinyang Zhang, Zhijing Wu, Junfeng Zhao, Yasha Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EvoRubrics, a co-evolutionary RL framework where a Policy LLM and a Rubric Generator adversarially co-adapt to provide dynamic, discriminative rewards for open-ended tasks, directly advancing RL for LLMs.

**摘要**: 基于条目的奖励为无法获得可验证答案的开放式任务中的强化学习提供可解释且细粒度的优化信号。然而，预先构建的主题在整个培训过程中保持静态，与不断变化的政策产生了根本性的不匹配：随着模型的改进，固定标准逐渐失去辨别力，导致奖励饱和和潜在的黑客攻击。最近的动态标题方法部分解决了这个问题，但依赖于外部前沿模型或地面真相答案，并且仅以粗粒度更新标题。我们提出EvoRubric，这是一个协同进化的RL框架，其中Policy LLM和Rubric Generator通过每个训练步骤中的对抗性交互共同改进。随着政策在标题生成器的指导下改进，标题生成器会调整其标准以保持区分性和信息性，使评估能够实时跟踪政策并自然地引导自动课程。实验表明，EvoRubric在各个基准测试中的性能始终优于静态和动态Rubric基线。学到的Rubric Generator进一步概括为可转移奖励模型。值得注意的是，即使是在没有任何外部监督的情况下完全自我监督的变体也会取得有意义的收益，这表明仅生成和评估之间的协同进化就可以提供足够丰富的学习信号。我们的代码可在https://anonymous.4open.science/r/EvoRubrics-2155/上公开获取。

[阅读原文](https://arxiv.org/abs/2606.23038v1)

---

## 3. 安排思维：学习扩散语言模型中的思维顺序

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jiawei Xu, Minghui Liu, Aakriti Agrawal, Yifan Chen, Furong Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a novel RL-based method (SAS) using GRPO to learn the unmasking order in masked diffusion language models, directly improving generation quality and reasoning, which is a strong match for RL for LLMs.

**摘要**: 掩蔽扩散语言模型通过迭代揭开标记来解码，其中揭开顺序定义了强烈影响生成质量的“思维顺序”，但通常是试探性地选择的。我们推导出顺序解码不匹配的易于处理的上限，由Kullback-Leibler分歧来衡量，并以模型的路径逻辑似然性来表达，在足够的模型表达能力下具有紧密性。这种界限在有序轨迹上引发了密集的自我意识奖励，将订单选择视为具有冻结降噪器的原则性政策优化问题。我们将这个想法实例化为自感知调度（SAS），它使用组相对策略优化来学习轻量级顺序策略，并无缝应用于任意顺序和半自回归解码。在具有1B MDM的数独上，SAS将谜题准确率从82.0%（最佳启发式时间表）提高到91.8%，并通过沿着学习轨迹进行第二阶段微调达到97.5%。在使用LLaDA-8B进行数学推理方面，SAS将GSM 8 K上的pass@1从64%提高到76%，将MBPP上的pass@1从39.5%提高到41%，在代际长度和块大小上始终匹配或超过启发式计划。项目页面：https://jimmyxu123.github.io/SAS

[阅读原文](https://arxiv.org/abs/2606.23567v1)

---

## 4. 论政策上蒸馏的立场偏差

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yan Xie, Sijie Zhu, Tiansheng Wen, Bo Chen, Yifei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies and formalizes position bias in on-policy distillation for LLMs, proposing a principled importance-weighted objective that significantly improves learning efficiency and final performance.

**摘要**: 按策略蒸馏（OPD）通过教师密集的代币级监督来提高标准强化学习的学习效率。在OPD的标准KL目标中，代币级损失是均匀平均的，这意味着所有代币的权重相等。然而，我们发现并不是所有代币都是平等的：随着学生就业的时间越来越长，它们与教师的分布进一步偏离，导致后期职位的监督质量下降。因此，仅使用前30%令牌的OPD可以执行使用所有令牌的任务，而仅使用后30%令牌的OPD几乎无法学习任何东西。在这项工作中，我们通过约束优化的角度提供了对这个问题的原则性理解。基于这些见解，我们推导出重要性加权政策蒸馏（IW-OPD），其中分配给每个代币的权重取决于学生和教师分布之间的累积差异，自然会增加早期代币的权重，并降低后期具有较大偏差的代币的权重。我们表明，IW-OPD的收敛速度明显快于OPD，学习效率更高，并且在相同规模和跨规模设置下都比标准OPD实现更好的最终性能，在AIME-2025上将性能提高高达6.9个百分点。

[阅读原文](https://arxiv.org/abs/2606.22600v1)

---

## 5. 螺旋：学习搜索和聚合

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jubayer Ibn Hamid, Ifdita Hasan Orney, Michael Y. Li, Omar Shaikh, Yoonho Lee, Dorsa Sadigh, Chelsea Finn, Noah Goodman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SPIRAL, a novel RL framework that trains LLMs to use sequential, parallel, and aggregative reasoning primitives end-to-end, directly advancing RL for LLMs and reasoning.

**摘要**: 语言模型推理可以通过跨不同基元扩展推理计算的框架在测试时得到显着改进--轨迹内的顺序推理、独立采样的并行轨迹以及将多个推理轨迹聚合为最终响应。然而，在后训练期间，语言模型仅针对单个轨迹内的顺序推理进行优化。我们引入了序列并行聚合强化学习（SPIRAL），这是一个框架，其中语言模型被训练为使用所有三个基元，作为统一推理计算管道的一部分。具体来说，语言模型首先并行采样一组独立的轨迹，每个轨迹都是通过顺序思维链推理产生的，然后根据这些轨迹生成最终的聚合轨迹;所有组件都针对最终聚合响应的回报进行了端到端的优化。为了训练这个系统，SPIRAL使用集合强化学习来教模型产生一组对聚合器共同有用的轨迹，并使用标准强化学习来教模型将集合聚合为改进的最终响应。我们对推理任务的实验表明，SPIRAL可以有效地通过推理计算进行扩展，在扩展所有三个计算基元时，其扩展效率比GRPO高出11 $\x $，性能高出15%。

[阅读原文](https://arxiv.org/abs/2606.23595v1)

---

## 6. RLVR优于SFT的推理模型的可证明优势：学习有效回溯

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Stanley Wei, Juno Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical proof that RLVR enables efficient backtracking in reasoning, exponentially outperforming SFT, and shows that RLVR traces can be distilled on-policy.

**摘要**: 大型语言模型（LLM）的最新进展表明，对预训练的基本模型进行强化微调可以在推理时显着提高推理性能。在这项工作中，我们从理论上分析了为什么强化微调比纯监督微调（SFT）方法能产生更好的推理能力。我们将思想链（CoT）推理建模为图上的寻路问题，并将流行的强化学习方法与传统的SFT进行比较。我们证明，当SFT在没有负例的黄金最短路径上训练时，无法学习如何有效地回溯。相比之下，RLVR训练的模型可以学习如何仅使用结果奖励有效地从死胡同中倒退。这导致这两种方法之间的推理时计算呈指数级分离，并表明WLVR引导模型学习推理链中困难决策的位置，最终允许更好地分配推理时计算。最后，我们表明，可以提取WLVR模型的推理痕迹来训练基本模型以有效地回溯。

[阅读原文](https://arxiv.org/abs/2606.22938v1)

---

## 7. 政策上蒸馏的公式驱动调查和研究议程

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Bowen Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a comprehensive formula-driven taxonomy and analysis of on-policy distillation for LLMs, introducing new concepts like temporal credit and vocabulary routing, and proposing GAE-OPD and CR-OPD.

**摘要**: 政策蒸馏（OPD）针对当前或最近的学生政策引发的状态对LLM进行培训：学生生成完整或部分推出，教师或自学者在其生成的上下文下对所得代币进行评分，并将密集的log概率、logit或分布信号转换为训练后更新。这项调查将OPD研究为一个反馈更新问题，而不是一个单一的损失家庭。我们从两条路线--直接分配损失和政策梯度式对数比更新--开发公式驱动的分类法，并使用它来组织核心方法、验证者或结果引导的混合体、工业报告、框架实现、故障模式和明确证据边界下的稳定化食谱。分类学表明，OPD的有效性不仅取决于KL方向或教师访问，还取决于状态兼容性、支持构建、时间信用、词汇级概率路由、门和权重以及正规化。我们进一步分离了采样代币OPD稳定性讨论中经常混淆的两种机制。时间学分询问师生对数比返回应如何加权整个推出期间的采样动作;词汇路由询问当负反馈抑制采样令牌时，概率质量应该移动到哪里。这种区别产生了立即、退货、折扣和基线修正估计量的偏差边界，激励GAE-OPD作为对数比回报的基于价值的假设，并激励反事实路由OPD（CR-OPD）将概率质量路由到教师支持的、学生可达的替代方案。我们通过将可行动性诊断、故障机制、案例研究、未决问题和报告清单映射到相同的反馈更新变量来结束。

[阅读原文](https://arxiv.org/abs/2606.22793v1)

---

## 8. 寻找证据：发现支持决策的代币以进行政策推理蒸馏

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Jinwei Xiao, Zhuowen Han, Yueqing Sun, Zhengxi Lu, Yuxin Liu, Zhiyuan Yao, Wentao Chen, Qi Gu, Xunliang Cai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DEAR, a novel on-policy reasoning distillation method that discovers and transfers both decision and evidence tokens via student uncertainty and teacher-student divergence, achieving strong gains on math and code.

**摘要**: 政策上的提炼通过密集的代币级监督来转移推理能力，但可转移信号的性质仍不清楚。我们发现，推理链包含两种类型的知识，需要不同的发现机制：决策（在哪里分支），通过学生的不确定性浮出水面，而证据（证明决策合理的中间步骤），隐藏在学生自信但错误的位置。当前的方法仅捕获决策;证据代币中的实质性知识仍未转移。我们提出了DEAR（决策证据感知推理蒸馏），它首先通过学生信息量来识别决策，然后通过与决策锚的隐状态cos相似性来发现其支持证据，并在师生分歧的推动下，以优先考虑最大的知识差距。在数学和代码基准的三种师生配置中，DEAR始终优于标准OPD，竞赛数学最高可达+2.5 pp，代码生成最高可达+5.7 pp。

[阅读原文](https://arxiv.org/abs/2606.22830v1)

---

## 9. ReNIO：重新权衡LLM政策上蒸馏的负轨迹重要性

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Chen Lin, Kedi Chen, Wei Zhang

**机构**: BDML Lab

**💡 亮点 (Highlight)**: Proposes ReNIO, a novel on-policy distillation method that reweights negative trajectories using student-to-teacher probability ratios, improving LLM reasoning without requiring final-answer correctness.

**摘要**: 政策蒸馏（OPD）通过根据自己生成的输出训练学生模型来改进LLM推理，但标准OPD平等对待所有学生生成的输出（SSYS），无论其信息量如何。我们在受控过滤实验中观察到一致的不对称性：在OPD和按策略自蒸馏（OPSD）中，仅在不正确的Scrum上进行训练的效果优于仅在正确的Scrum上进行训练。我们的进一步分析表明，在仅正确的Scrum上训练的模型往往会生成更短的推理痕迹并显示出较弱的反射行为，而不正确的Scrum则更好地将探索性推理保留在模型能力边界附近。为了在不需要完整包含答案的情况下利用这一信号，我们引入了ReNIO，它重新加权了LLM按政策蒸馏的负轨迹重要性。通过使用学生与教师的概率比，ReNIO识别导致错误推理痕迹的关键标志，并将其信息聚合为标准化样本权重，从而在不观察最终答案的正确性的情况下为可能的负轨迹赋予更大的权重。由于Re-NIO仅使用前置条件令牌概率，因此它保留了OPD相对于全面推出强化学习的前置训练优势。在数学推理和代码生成任务中，ReNIO都改善了OPD和OPSD，在数学推理基准上，Qwen 3 -1.7B的代表性相对收益高达8.90%，R1-Distill-Qwen-7 B的代表性相对收益高达10.00%。代码回购：https://github.com/BDML-lab/ReNIO。

[阅读原文](https://arxiv.org/abs/2606.23104v1)

---

## 10. 偏好对齐的马尔科夫链方法

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Takuya Koriyama, Tengyuan Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel Markov chain approach for preference alignment that directly uses pairwise preferences without scalar reward, with theoretical convergence guarantees.

**摘要**: We propose Markov Chain from Human Feedback (MCHF), an elementary approach for aligning generative models from pairwise human preferences. Unlike Reinforcement Learning from Human Feedback (RLHF), which reduces comparisons to a scalar reward, and Nash Learning from Human Feedback (NLHF), which preserves pairwise utilities through a KL-regularized minimax optimization, MCHF uses pairwise preferences directly to define a transition mechanism over model outputs. Given a pairwise utility $U(x,y)$, which quantifies human preference for $y$ over $x$, and a reference probability distribution $μ_{\mathsf{ref}}$, we define a Markov kernel $\mathsf{P}(x, dy)\propto \exp(U(x,y))μ_{\mathsf{ref}}(dy)$, and take the Markov chain starting from $μ_{\mathsf{ref}}$ as an iterative alignment procedure. We show that MCHF converges geometrically fast to the stationary distribution, with a convergence rate governed by the seminorm $\|U\|_\oplus=\inf_{g,f\in L^\infty(μ_{\mathsf{ref}})}\|U-g\oplus f\|_\infty$, which quantifies the non-transitive structure of the pairwise utility. We further show that a mirror-descent algorithm for NLHF satisfies an analogous structure-adaptive convergence guarantee. Finally, through a perturbation analysis, we prove that when $\|U\|_\oplus$ is small, MCHF and NLHF agree up to first order around an RLHF solution, which yields a unified view of reward-based, game-theoretic, and Markovian approaches to alignment. In particular, for two natural algorithms that converge to the MCHF/NLHF equilibria, we show that the first step of MCHF and NLHF recovers the RLHF solution based on the column-sum reward $\hat{f}(y)=\int μ_{\mathsf{ref}}(dx) U(x, y)$, and starting from the second iteration, both algorithms incorporate the same linear functional of the residual $U-(-\hat f)\oplus \hat f$, which captures the non-transitive structure of the pairwise utility $U$.

[阅读原文](https://arxiv.org/abs/2606.22652v1)

---

## 11. 视频语言模特什么时候停止观看？奖励强度控制多模式WLVR中视觉捷径的形成和撤销

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zekun Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a controlled study of visual shortcut formation and reversal in multimodal RLVR, revealing hysteresis and critical intervention windows with direct implications for reward design in RL for LLMs.

**摘要**: 具有可验证奖励的强化学习（WLVR）越来越多地应用于大型视觉语言模型（LVLM），但纯结果优化可能会导致模型停止关注视频，转而利用语言先验--我们称之为视觉捷径。虽然这种感知绕过的存在目前已被记录，但它是如何形成的、是否可以撤销的以及何时干预仍然有助于保持开放。我们将接地罚分的强度Lambda视为控制旋钮，并描述视觉快捷方式沿着训练时间轴的形成逆转动态。在一个固定的、不分布的诊断集上，我们发现：（i）突然开始--捷径依赖在优化步骤的狭窄窗口中突然出现，并且在随机种子中是稳健的;（ii）单调剂量响应--增加的拉姆达逐渐抑制捷径，并且在中间剂量下，轨迹首先形成，然后逆转捷径，暴露了获取和删除之间类似迷宫般的不对称性;和（iii）关键的干预窗口--在发作前应用惩罚会阻止捷径形成，而在巩固后应用相同的惩罚明显不那么有效。这些结果加在一起，将视觉捷径崩溃重新塑造为一个可控的、时间依赖的和不对称的过程，直接影响了何时以及如何严格规范多模式WLVR。

[阅读原文](https://arxiv.org/abs/2606.22043v1)

---

## 12. 深入并不总是更好：通过自信层解码减轻一致税

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xuanming Zhang, Sining Zhoubian, Yuxuan Chen, Tianyi Tang, An Yang, Sean Du, Chujie Zheng, Fei Huang, Dayiheng Liu, Gao Huang, Jingren Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free decoding strategy that dynamically selects near-final layers to bypass alignment perturbations, directly improving reasoning in aligned LLMs via a novel latent-layer selection mechanism.

**摘要**: 大型语言模型（LLM）中的自回归生成通常从最后一层进行解码，假设更深的表示会产生更可靠的下一个令牌预测。我们通过揭示反复出现的猜测-细化-扰动动态来重新审视这一假设：早期层形成粗略的猜测，中间层细化推理相关的语义，而最终层可以将这些细化的预测扰动为通用或偏好的令牌。我们引入了Confident Decoding，这是一种免训练的解码策略，通过信息引导的保守后向搜索动态选择最可靠的接近最终层。我们进一步提供了层选择作为最优停止问题的理论公式，表明在有界投影噪音和占主导地位的后期对齐扰动下，我们的搜索规则过滤扰动，同时限制了相对于Oracle细化层的损失。密集型和混合型专家LLM的实验表明，在具有挑战性的推理基准（包括GPQA-Diamond、Omni-MATH和HLE）上取得了一致的收益，内存占用为零，延迟增加不到2%。这些结果表明，动态绕过最后层扰动可以从对齐的LLM中解锁更强的推理行为。

[阅读原文](https://arxiv.org/abs/2606.21906v1)

---

## 13. Video潜伏：通过潜在的自我强迫进行视频语言学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zi-Yuan Hu, Zicong Tang, Shijia Huang, Yanyang Li, Michael R. Lyu, Liwei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces VideoLatent, a latent reasoning MLLM with a novel self-forcing training paradigm for video understanding, achieving large efficiency gains over explicit CoT methods.

**摘要**: 思想链（CoT）推理的最新进展在增强多模式大型语言模型（MLLM）的视频理解和推理能力方面表现出了希望。然而，现有的基于CoT的MLLM需要劳动密集型的CoT注释，并产生大量的训练和推断费用。虽然视觉潜在推理已成为一种更有效的替代方案，但现有方法主要关注图像任务，并且严重依赖于视觉潜在生成的额外监督信号（例如，CoT轨迹、辅助图像或细粒度注释），限制了它们的可扩展性和对视频任务的可移植性。为了弥合这一差距，我们引入了VideoLatent，这是一款新型MLLM，配备了专为视频理解和推理量身定制的潜伏注入模块。具体来说，VideoLatent学习使用一种新的潜在自我强迫训练范式来执行视觉潜在推理，该范式包括潜在对齐和潜在多样性目标，并且仅依赖于标准的视频问答三胞胎。针对14个基准的广泛实验表明，我们的模型在一般视频理解和复杂视频推理方面始终优于现有的标准和潜在MLLM。与Video-R1相比，我们的VideoLatent实现了更高的计算效率，将训练/推理负载减少了$\sim$6 $\times $/$\sim$68 $\times $。此外，实验表明，我们的方法对不同的MLLM主干和不同的模型规模具有很强的推广能力。

[阅读原文](https://arxiv.org/abs/2606.22870v1)

---

## 14. CFPO：多模式推理的反事实政策优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhangyuan Yu, Wanran Sun, Guangjing Yang, Xiaohu Wu, Qicheng Lao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CFPO, a novel RL framework for LVLMs that uses a cross-modal counterfactual enhancement mechanism to enforce causal consistency between visual perception and textual reasoning, directly improving reasoning fidelity.

**摘要**: 大型视觉语言模型（LVLM）在多模式推理方面表现出了非凡的能力。然而，流行的强化学习（RL）范式缺乏明确的反事实增强和因果学习机制。这种根本缺陷会导致严重的接地故障，表现为忽视视觉证据而偏爱语言先验的倾向，或者在长链思维推理过程中表现出幻觉漂移。为了解决这个根本原因，我们提出了反事实政策优化（CFPO），这是一种新颖的框架，可以强制执行视觉感知和文本推理之间的因果一致性。CFPO引入了跨模式反事实增强机制，该机制通过最大化模型的预测与来自抑制关键视觉线索的反事实状态的预测之间的差异来规范政策。这种方法与GRPO和DAPO等标准算法无缝集成，无需外部奖励模型或额外监督。大量实验表明，CFPO显着提高了推理的保真度，比标准RL基线实现了3.17%-6.25%的一致收益，比最先进的感知感知方法（PAPO）实现了1.32%-2.13%的一致收益。代码可在https://github.com/Raven-July/CFPO上获取。

[阅读原文](https://arxiv.org/abs/2606.23206v1)

---

## 15. 超越惩罚错误：通过自适应仅正确奖励稳定大型推理模型中的效率训练

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jungseob Lee, Seungyoon Lee, Seongtae Hong, Minhyuk Kim, Chanjun Park, Heuiseok Lim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ACOER, a novel adaptive reward design for GRPO that stabilizes efficiency training in reasoning LLMs by isolating brevity bonuses to correct completions and preventing reward collapse.

**摘要**: 训练大型语言模型以有效推理是一项严峻的挑战。虽然将长度惩罚奖励集成到团体相对政策优化（GRPO）中是为了减少冗长，但它经常会引发奖励崩溃，严重降低推理能力。通过对各种奖励配置的系统评估，我们确定了根本机制：当不正确的答案受到连续长度惩罚时，GRPO的群体规范化会创造不同的优势。因此，惩罚错误答案长度的方法在持续优化下在结构上容易崩溃。此外，将惩罚仅限于正确答案可以避免这种主要失败，但使模型容易受到响应过度压缩驱动的随机崩溃的影响。为了有力地防止这两种故障模式，我们提出了ACOER（自适应仅正确效率奖励）。ACOER通过隔离简洁性奖金以纠正完成来消除结构性惩罚循环，并通过动态预算规范化和控制循环惩罚调整来防止随机压缩。经过各种数学推理基准的评估，与基本模型相比，ACOER提高了总体准确性，同时将代币生成减少了60%以上，为效率感知优化建立了一种从根本上稳定的方法。

[阅读原文](https://arxiv.org/abs/2606.22716v1)

---

## 16. 强化学习以改进基于大型语言模型的自动代码合规系统

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jack Wei Lun Shi, Minghao Dang, Wawan Solihin, Leong Hien Poh, Justin K. W. Yeoh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage framework combining SFT with GRPO (a verifiable-reward RL method) to directly improve LLM code generation accuracy for automated compliance, demonstrating a clear RL-for-LLMs pipeline with domain-specific reward optimization.

**摘要**: 基于大型语言模型（LLM）的建筑法规自动代码合规（ACC）方法容易生成不正确和幻觉的计算机可处理规则。本文介绍了P4 IR，这是一个两阶段框架，它使用监督式微调（SFT）在LLM中灌输领域知识，然后使用组相对政策优化（GRPO）来提高以高级代码骨架形式生成的中间表示的准确性。相对于SFT基线，该框架的树编辑距离和标记级Levenshtein距离分别减少了23.8%和38.6%。比较分析表明，这种方法在零镜头设置下在代码结构和语义方面优于领先的LLM，特别是Claude Opus和十四行诗4.5、GPT-5.2、Qwen-3-Max和GLM-4.7，通过几次镜头提示进行评估。此外，GRPO阶段的假阳性减少幅度虽小，但具有统计学意义。通过将SFT与GRPO结合起来直接针对特定领域的目标进行优化，这种方法提供了一条通往更准确、更可靠的基于LLM的ACC系统的途径。

[阅读原文](https://arxiv.org/abs/2606.22402v1)

---

## 17. 长期强化学习的群图策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yunan Wang, Minghui Song, Zihan Zhang, Shaohan Huang, Haizhen Huang, Furu Wei, Weiwei Deng, Feng Sun, Qi Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes G2PO, a novel group-based RL algorithm for LLM agents that uses a global state-transition graph for improved credit assignment and value estimation in long-horizon tasks.

**摘要**: 基于小组的强化学习（RL）显着增强了代理场景中的大型语言模型（LLM）。为了实现更细粒度的政策更新，最近的代理RL框架已从车间级培训转向步骤级培训。然而，长期代理RL面临严重的奖励稀疏性和延迟，因为反馈通常被推迟数十个交互步骤。虽然现有的阶梯级框架细化了训练粒度，但它们的信用分配仍然是粗粒度的，并且仍然将代理探索视为孤立的线性轨迹。这种过于简化的视角忽视了状态转换的固有图形结构，导致高方差状态值估计和短视的、局部的信用分配。为了克服这些关键瓶颈，我们提出了群图策略优化（G2 PO），这是一种新型的基于群的RL算法，专为多回合代理任务量身定制。G2 PO显式地将线性相互作用轨迹转换为全局状态转换图。通过聚集不同轨迹上的相同观察，我们引入了组聚集状态值估计，以减少抽样方差和个体相关偏差。此外，我们将代理行为重新定义为状态节点之间的转换，并提出了一种以边缘为中心的优势估计策略。通过对整个图表中的时态差异（TD）错误进行全球标准化，G2 PO明确识别并优先考虑推动绝对任务进度的关键转换。对代表性长期基准（WebShop、ALFWorld和AppWorld）的广泛实验表明，G2 PO的表现大大优于最先进的基于预算和RL基线，实现了比GRPO高达22.2%的显着成功率提高。

[阅读原文](https://arxiv.org/abs/2606.22995v1)

---

## 18. VeriEvol：通过可验证的进化指令扩展多模式数学推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haoling Li, Kai Zheng, Jie Wu, Can Xu, Qingfeng Sun, Han Hu, Yujiu Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes VeriEvol, a verifiable data-construction framework with type-aware evolution and hypothesis-test falsification for scaling RL in multimodal math reasoning.

**摘要**: 扩展视觉数学推理的强化学习需要的不仅仅是生成更难的问题：随着数据量的增长，奖励标签本身必须保持可靠性。然而，现有的数据管道在信任标签商的同时扩大监管范围，政策方方法假设潜在答案已经正确。相反，我们将扩展视为一个可验证的数据构建问题，并在任何政策更新之前将两个轴脱钩：由特定路线的进化操作符扩展的提示难度，以及由离线假设测试证伪强制执行的答案可靠性。我们将其实例化为VeriEvol，这是一个具有两个可扩展组件的迭代框架：一个类型感知的进化模块，将低难度的图像问题种子重写为更难的、基于图像的提示; HTV-Agent是一个验证器，只有在多源反证据未能反驳后才接受答案。由此产生的验证数据在数量上扩展，通过添加进化路线或验证器通道进行扩展，并直接插入现有的GRPO风格RL食谱。在五个基准视觉数学套件中，将进化的SFT数据从10 K样本扩展到250 K样本，将平均准确性从35.42提高到54.73;然后，在主干、SFT初始化和GRPO食谱固定的情况下，VeriEvol在未进化的RL基线上增加了累积+3.88，其中+1.82来自进化的提示，+2.06来自HTV-Agent验证器。我们发布每个样本的提示、数据、模型、代码和完整的验证者跟踪，以便下游工作可以扩展和审计管道，而不仅仅是检查其输出。

[阅读原文](https://arxiv.org/abs/2606.23543v1)

---

## 19. Wh：终端代理的简单食谱

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hamish Ivison, Junjie Oscar Yin, Rulin Shao, Teng Xiao, Nathan Lambert, Hannaneh Hajishirzi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a strong open RL recipe for terminal agents using a novel taxonomy for data generation and verifier diversification, directly advancing RL for LLMs.

**摘要**: 使用终端的代理已迅速成为语言模型（LM）最受欢迎的下游应用程序。尽管它们很普遍，但研究这些模型基于RL的训练的学术工作相对较少，这可能是由于基准困难、缺乏数据以及缺乏简单的基线食谱。我们展示了迄今为止针对终端代理的最强开放RL食谱，使开放数据食谱更接近前沿。虽然简单，但我们的配方在Terminal-Bench 2.0上仅使用9 B参数即可达到27%，优于之前工作中更大的模型。具体来说，我们使用一种新颖的分类法生成数据，结合了难度控制、角色和验证者多样化，这使我们能够廉价地生成大量用于RL和SFT训练的终端环境。我们开源了我们的终端数据集，它比之前发布的终端代理数据集大了2.5倍以上。然后，我们使用RL和我们的数据，使用简单的、仅结果的食谱来训练开重量模型。我们在https://github.com/hamishivi/tmax上发布我们的数据、模型和代码，作为未来关于终端代理的开放学术工作的强有力基线。

[阅读原文](https://arxiv.org/abs/2606.23321v1)

---

## 20. 以正确的节奏学习：自适应数据调度改进LLM强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zicheng Xu, Ruixuan Zhang, Yu-Neng Chuang, Xiuyi Lou, Hoang Anh Duy Le, Oren Gal, Alexander S. Szalay, Zhaozhuo Xu, Guanchu Wang, Vladimir Braverman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Adaptive Data Scheduling (ADS), a dual-level data scheduling framework for RL post-training of LLMs that replaces uniform sampling with adaptive cluster-level and policy-boundary sample selection, improving GRPO by 5.2% on reasoning benchmarks.

**摘要**: 大型语言模型（LLM）通过强化学习（RL）后训练实现了出色的推理能力。然而，现有的RL后训练通常依赖于统一的数据采样，这忽视了训练数据的语义结构和训练策略的变化能力。为了解决这些限制，我们提出了自适应数据调度（ADS），这是一种用于对RL训练后进行调整的双层数据调度框架，用语义集群和策略边界样本选择上的自适应分布取代统一采样。在集群层面，ADS根据语义模式组织样本，并维护自适应的集群间分布以巩固当前的训练进度。在样本级别，ADS执行集群内调度以连续采样策略边界样本，这提供了信息丰富的相对优势。三个LLM和七个推理基准的实验结果表明，ADS的平均准确性比组相对政策优化（GRPO）提高了5.2%。值得注意的是，ADS通过不同的目标设计不断改进RL方法，凸显了其作为LLM RL后训练通用数据调度策略的潜力。源代码可访问：https://github.com/Richard-zrx/ADS。

[阅读原文](https://arxiv.org/abs/2606.22305v1)

---

## 21. Air：MLLM中的自适应交织推理与代码

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning training pipeline with a group-constrained reward function for adaptive interleaved code reasoning in MLLMs, directly advancing RL for LLMs.

**摘要**: 继OpenAI o3发起的范式转变之后，通过代码进行交织推理以增强多模式大型语言模型（MLLM）已成为一个关键的研究前沿。现有文献主要关注视觉感知任务中的工具使用。然而，此类方法通常依赖于预定义的启发式来进行视觉操纵，并且由于它们专门关注视觉操作，本质上无法解决数字计算问题。本文通过对代码增强的复杂数字计算任务进行扩展强化学习训练，赋予MLLM自适应交叉推理能力。为此，我们提出了一个全面的三部分解决方案，包括：两阶段冷启动数据构建管道、RL数据集策展的数据过滤策略，以及利用群体约束奖励函数进行交织推理轨迹的自适应工具调用策略。大量实验表明，在使用群体约束奖励函数进行强化学习训练后，绩效在评估基准上平均提高了6.1个百分点（pp）。具体而言，交叉推理样本的准确率提高了9.9 pp，工具使用的总体成功率超过95%。我们的数据和代码可访问：https://github.com/CongHan0808/AIR.git。

[阅读原文](https://arxiv.org/abs/2606.23678v1)

---

## 22. RL for LLM Reasoning更新的关键因素是什么？

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Peidong Wang, Demi Wang, Xufang Luo, Jiahang Xu, Xiaocui Yang, Shi Feng, Yuqing Yang, Dongsheng Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a theoretical analysis of RLVR updates for LLM reasoning and proposes ACPO, a new clipping method that adapts based on importance sampling variance, outperforming DAPO and CISPO.

**摘要**: 来自可验证奖励的强化学习（WLVR）已成为增强大型语言模型推理能力的一个有前途的框架。然而，现有的大部分工作都是由启发式直觉指导的，导致算法选择不同，甚至是相互矛盾的算法选择，但却报告了经验收益。为了更好地理解这种现象，我们对WLVR更新进行了理论分析。我们的研究表明，由每次推出的梯度步数确定的非策略程度差异会极大地影响重要性抽样率的分布及其修剪行为，从而改变哪些令牌主导更新。基于这一见解，我们将梯度期望描述为管理更新动态的中心量，并分析代币概率、优势和重要性抽样比的作用。受这些发现的启发，我们提出了自适应剪辑策略优化（ACPO），该优化根据代币组重要性抽样率的经验方差调整代币组之间的剪辑边界。在各种推理基准（涵盖数学问题解决、表格QA和逻辑谜题）上对3B和7 B模型进行的实验表明，ACPO优于DAPO和CISPO等强大基线。这些结果表明，有原则的、分析驱动的方法可以产生更稳健、更有效的WLVR方法。代码可访问：https://github.com/Control-derek/ACPO

[阅读原文](https://arxiv.org/abs/2606.22570v1)

---

