# 💡 今日研究速览 (Daily Summary)

# LLM的强化学习
今天，一系列主要论文突破了将强化学习应用于大型语言模型的界限，超越标准的RL HF，进入复杂的训练食谱和奖励设计。**ResRL**引入了一种新颖的方法，通过利用RL循环内的负样本投影残留来提高推理多样性，直接解决崩溃的解决方案空间的常见问题。** RLHF的Wasserstein DRRO**提供了一种理论依据的方法，通过分布稳健的后悔优化来缓解奖励过度优化，并提供了实用的政策梯度算法。多项作品专注于将RL扩展到新领域：**Odysseus**证明VLM可以通过PPO和回合级评论家来训练，以掌握游戏中100多个回合决策，而**AlphaStock** 则使用基于LLM的RL框架开发了具有部署保证的白盒库存策略。**RSAT** 采用GRPO和基于NLI的复合奖励来训练小型LM，通过单元级引用进行忠实的表格推理，**PrefMoE**通过混合专家架构改进了奖励模型本身，以在嘈杂的监督下进行稳健的偏好学习。最后，**DoTS**提供了一种巧妙的事后解决方案，通过算术在推理时合成SFT和WLVR任务载体，从而无需再培训即可集成WLVR的好处。

# 激进的RL和自我提升
对代理系统的强烈关注揭示了更复杂的信用分配和内存进化政策的趋势。** AEM**（自适应Entropy Modulation）为多回合代理RL引入了一种无监督方法，该方法动态调整了熵动态，通过在没有明确奖励塑造的情况下解决长期信用分配问题，在SWE平台上实现强劲的结果。作为补充，一个受认知启发的两阶段RL框架教LLM代理通过结构化过程奖励学习**记忆进化策略**，有效地学习 * 如何记忆和记忆 * 以实现自我完善。为了安全性和鲁棒性，**Stable-GFlowNet**将对比轨迹平衡应用于红色团队，提高生成的对抗示例的多样性和稳定性。在视觉语言领域，**在线自校准**框架使用MCTS和DPO来减少LVLM中的幻觉，代表了一种自我监督对齐方法。此外，**了解自己在哪里点击**提出了政策上的自我提炼，并对图形用户界面基础进行了以信息引导为指导的监督，提供密集的代币级奖励信号。

# 新颖的架构和潜在的推理
将推理带入压缩的潜在空间的主题正在获得显着的关注。**状态流Transformer（CST）V2**提出了潜在空间中的非线性回归，从而实现参数高效的并行训练，以进行连续审议--回归推理架构的直接演变。** Being-H 0.7**通过引入潜在世界动作模型进一步推进了这一概念，该模型在以自我为中心的视频中使用潜在查询进行未来感知推理，完全绕过了生成未来帧的需要。这表明范式正在转向以潜在的表示而不是显式的记号或像素“思考”的模型。

# 模式崩溃与代际多样性
针对LLM生成中模式崩溃的基本问题，一篇论文提出了**加强模式调节（RMR）**，这是一种轻量级在线干预，将低等级衰减应用于Transformer值缓存。该方法被框架为动态系统调节，直接解决自回归生成期间的熵崩溃问题，无需再训练，为改善输出多样性提供了实用的事后解决方案。

---

## 1. 状态流Transformer（CST）V2：潜在空间推理的非线性回归并行训练

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 9/10

**作者**: Thea Aviss

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SST V2, a novel architecture with nonlinear recurrence in latent space for parameter-efficient reasoning, enabling parallel training and continuous latent deliberation.

**摘要**: arXiv：2605.00206v1宣布类型：新摘要：当前的变压器丢弃了位置之间丰富的潜在剩余流，在每个新位置重建潜在推理上下文，并留下未开发的潜在推理能力。状态流转换器（SST）V2通过每个解码器层的FFN驱动的非线性递归，在连续潜在空间中实现参数高效推理，其中潜在状态通过学习的混合在整个序列中水平流式传输。这种相同的机制支持在推理时每个位置的连续潜在审议，在承诺代币之前将额外的FLOP用于探索抽象推理。两遍并行训练过程解决了循环的顺序依赖性，以允许计算效率高的训练。隐藏状态分析表明，状态流通过探索连续潜在空间中的不同语义盆地来促进推理，其中依赖于内容的位置处的转变将模型移至截然不同的Bayesian后验，直接影响未来位置处的潜在空间。我们还发现，通过习得的探测，在第一个生成的令牌位置，潜在状态已经预测了最终答案在每个后续位置的额外潜在计算下是否会生存或崩溃。仅使用GSM 8K示例的一小部分数据集共同训练到现有的27 B主干网中，CST比非分布GPQA-Diamond上的微调匹配基线提供+15.15分的提高，并将相同基线的剩余GSM 8K错误减少了46%，共同表明推理改进归因于架构机制，而不是规模或训练数据。在GPQA-Diamond上，由此产生的27 B STS还比几种更大的开重模型和专有系统（包括高达25倍的开重模型）实现了更高的准确性。

[阅读原文](https://arxiv.org/abs/2605.00206)

---

## 2. 基于Wasserstein分布鲁棒后悔优化的人反馈强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yikai Wang, Shang Liu, Jose Blanchet

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Wasserstein distributionally robust regret optimization (DRRO) for RLHF, a new reward design and training recipe that mitigates over-optimization with a practical policy-gradient algorithm.

**摘要**: arXiv：2605.00155v1宣布类型：新摘要：来自人类反馈的强化学习（RL HF）已成为对齐大型语言模型的核心训练后步骤，但RL HF中使用的奖励信号只是真正人类效用的学习代理。从运营研究的角度来看，这会在客观错误规范下产生一个决策问题：策略根据估计的回报进行优化，而部署性能则由未观察到的目标确定。由此产生的差距会导致奖励过度优化（Goodharting），即即使在真实质量恶化后，代理奖励也会继续提高。现有的缓解措施通过不确定性惩罚、悲观回报或保守约束来解决这个问题，但它们可能在计算上很繁重并且过于悲观。我们提出了Wasserstein分布式鲁棒遗憾优化（DRRO）来解决WLHF问题。DRRO不是像标准DRO那样对最坏情况的价值进行困扰，而是对最坏情况的遗憾进行困扰，而不是像标准DRO那样对最坏情况的遗憾进行困扰。我们通过单纯形分配模型研究横向问题，并表明，在$\ell_1 $模糊集下，内部最坏情况的遗憾承认精确解，最优策略具有注水结构。这些结果导致了一种实用的政策梯度算法，具有简单的抽样奖金解释，并且对PPO/GRPO式的WLHF训练进行了微小的更改。该框架还从理论上澄清了为什么DRRO比DRO不那么悲观，我们的实验表明，DRRO比现有基线更有效地缓解过度优化，而标准DRO则系统性地过度悲观。

[阅读原文](https://arxiv.org/abs/2605.00155)

---

## 3. 部署时学习：多面手机器人策略的舰队规模强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie, Yunuo Cai, Qinglin Zhang, Chendi Qu, Jeffrey Wu, Jianheng Song, Xinlin Ren, Jingshun Huang, Mingjie Pan, Siyuan Feng, Zhi Chen, Jianlan Luo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a fleet-scale offline-to-online RL framework for continual post-training of generalist robot policies, directly matching RL for LLMs criteria with a new scalable RL training recipe and reward design.

**摘要**: arXiv：2605.00416v1宣布类型：新摘要：多面手机器人策略越来越多地受益于大规模预训练，但仅靠离线数据不足以实现稳健的现实世界部署。部署的机器人会遇到固定演示数据集无法完全捕捉的分布变化、长尾故障、任务变化和人类纠正机会。我们介绍了边部署边学习（LWD），这是一个舰队规模的离线到在线强化学习框架，用于对通才视觉-语言-行动（VLA）策略进行持续的后期培训。LWD从预先训练的VLA政策开始，通过使用在机器人舰队中收集的自主部署和人工干预，闭合了部署、共享身体体验、政策改进和重新部署之间的循环。为了稳定来自异类、稀疏回报车队数据的学习，LWD将用于稳健的值估计的分布隐式值学习（DIGL）与通过伴随匹配（Raman）进行的Q学习相结合，用于基于流的VLA动作生成器中的策略提取。我们在由16个双臂机器人组成的车队上验证了LWD，完成了8项现实世界的操纵任务，包括语义杂货补给和3- 5分钟的长视野任务。随着机队经验的积累，单一通才政策会得到改善，平均成功率达到95%，其中长期任务的收益最大。

[阅读原文](https://arxiv.org/abs/2605.00416)

---

## 4. ResRL：通过负样本投影剩余强化学习增强LLM推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Li Wang, Xiaodong Lu, Wei Lin, Ran He, Guojun Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ResRL, a novel RL method for LLM reasoning that uses negative sample projection residuals to improve diversity and performance, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2605.00380v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）增强了大型语言模型（LLM）的推理，但由于对正奖励的过度激励，通常表现出有限的世代多样性。尽管像负样本强化（NSO）这样的方法通过提高负样本的惩罚来缓解这个问题，但它们可能会抑制积极和消极响应之间共享的语义分布。为了在不失去多样性的情况下提高推理能力，本文提出了负样本投影剩余强化学习（ResRL），将积极和消极响应之间的相似语义分布重新连接。理论上，我们将懒惰似然位移（LLD）与负-正头部梯度干扰联系起来，并推导出一个单向前代理，该代理上限代表对齐来指导保守派优势重新加权。然后，ResRL将负令牌隐藏表示投影到基于ASD的低阶正子空间上，并使用投影残留来调制负梯度，在保持多样性的同时改进推理，并在涵盖数学、代码、代理任务和函数调用的十二个基准中平均表现优于强基线。值得注意的是，ResRL在数学推理方面超过了NSO，Avg@16和Pass@128中分别超过了9.4%和7.0%。代码可在https://github.com/1229095296/ResRL.git上获取。

[阅读原文](https://arxiv.org/abs/2605.00380)

---

## 5. Being-H 0.7：潜在的世界-来自自我中心视频的动作模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Hao Luo, Wanpeng Zhang, Yicheng Feng, Sipeng Zheng, Haiweng Xu, Chaoyi Xu, Ziheng Xi, Yuhui Fu, Zongqing Lu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent world-action model that uses latent queries for future-aware reasoning without generating future frames, directly relevant to latent reasoning architectures.

**摘要**: arXiv：2605.00078v1宣布类型：新摘要：视觉-语言-动作模型（VGA）通过将多模式观察和语言指令直接映射到动作来实现高级通用机器人控制，但稀疏动作监督通常鼓励快捷映射，而不是动态、接触和任务进度的表示。最近的世界动作模型通过视频推出引入了未来预测，但像素空间预测是一种成本高昂且间接的控制基础，因为它可能会对与动作生成无关的视觉细节进行建模，并引入大量的训练或推理费用。我们介绍了Being-H0.7，这是一个潜在的世界行动模型，它将未来感知推理带入VLA风格的政策中，而不会生成未来框架。Being-H0.7在感知和动作之间插入可学习的潜在查询，作为紧凑的推理界面，并通过面向未来的双分支设计来训练它们：可部署的先验分支从当前上下文推断潜在状态，而仅训练的后分支则用来自未来观察的嵌入来替换查询。在潜在推理空间中联合对齐两个分支会导致前一个分支仅根据当前观察推理出未来感知、对行动有用的结构。推断后，Being-H0.7放弃后分支并且不执行视觉卷展。六个模拟基准测试和各种现实世界任务的实验表明，Being-H0.7实现了最先进或相当的性能，将世界模型的预测优势与直接VLA策略的效率和可部署性相结合。

[阅读原文](https://arxiv.org/abs/2605.00078)

---

## 6. 通过几何调节避免LLM生成中的模式崩溃

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Xin Du, Kumiko Tanaka-Ishii

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Reinforced Mode Regulation (RMR), a lightweight online state-space intervention using low-rank damping on the Transformer value cache to prevent mode collapse in LLM generation, framed as a dynamical system regulation problem.

**摘要**: 模式崩溃是生成式建模中的一个持续挑战，并在自回归文本生成中表现为从显式循环到逐渐丧失多样性和过早轨迹收敛的行为。我们采取动态系统的观点，并将模式崩溃重新解释为 * 几何崩溃 * 引起的状态空间可及性降低：在生成过程中，模型的内部轨迹被限制在其表示空间的低维区域。这意味着模式崩溃并不纯粹是一种代币级现象，并且无法通过符号约束或仅概率解码试探法可靠地解决。在这一观点的指导下，我们提出了 * 加强模式调节 *（RMR），这是一种轻量级的在线状态空间干预，用于调节Transformer值缓存中的主导自增强方向（作为低等级缓冲实现）。在多个大型语言模型中，RMR大幅减少了模式崩溃，并能够以极低的熵率（低至0.8 nats/步）实现稳定、高质量的生成，而标准解码通常在2.0 nats/步附近崩溃。

[阅读原文](https://arxiv.org/abs/2605.00435v1)

---

## 7. AlphaStock：通过具有部署保证的大型语言模型进化白盒库存策略

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chenyu Huang, Jianghao Lin, Zhengyang Tang, Bo Jiang, Ruoqing Jiang, Benyou Wang, Lai Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes AlphaInventory, an RL-trained LLM framework for evolving inventory policies with deployment guarantees, directly matching RL for LLMs via a new reward and training loop.

**摘要**: arXiv：2605.00369v1宣布类型：新摘要：我们研究如何使用大型语言模型来在在线、非静止环境中制定库存策略。我们的工作受到基于LLM的进化搜索的最新进展的推动，例如AlphaEvolve，它在数学发现等静态和高度结构化问题上表现出出色的性能，但不直接适合在线动态库存设置。为此，我们提出了AlphaStock，这是一个基于基于信任区间的认证的端到端库存政策演变和推理框架。该框架使用强化学习训练大型语言模型，整合需求数据以及超出需求的数字和文本特征，并生成具有统计安全保证的白盒库存策略，以供未来部署。我们进一步引入了一个统一的理论界面，将训练、推理和部署连接起来。这使我们能够描述AlphaStock发展出统计上安全和改进的策略的可能性，并量化相对于Oracle安全基准的部署差距。经过合成数据和现实零售数据的测试，AlphaStock的性能优于经典库存策略和基于深度学习的方法。在规范的库存环境中，它会制定新的政策来改进现有的基准。

[阅读原文](https://arxiv.org/abs/2605.00369)

---

## 8. 通过几何调节避免LLM生成中的模式崩溃

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xin Du, Kumiko Tanaka-Ishii

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based state-space intervention (Reinforced Mode Regulation) to regulate mode collapse in LLM generation, directly addressing RL for LLMs via a new reward/regulation mechanism.

**摘要**: arXiv：2605.00435v1公告类型：新摘要：模式崩溃是生成式建模中的一个持续挑战，并在自回归文本生成中表现为从显式循环到逐渐丧失多样性和过早轨迹收敛的行为。我们采取动态系统的观点，并将模式崩溃重新解释为 * 几何崩溃 * 引起的状态空间可及性降低：在生成过程中，模型的内部轨迹被限制在其表示空间的低维区域。这意味着模式崩溃并不纯粹是一种代币级现象，并且无法通过符号约束或仅概率解码试探法可靠地解决。在这一观点的指导下，我们提出了 * 加强模式调节 *（RMR），这是一种轻量级的在线状态空间干预，用于调节Transformer值缓存中的主导自增强方向（作为低等级缓冲实现）。在多个大型语言模型中，RMR大幅减少了模式崩溃，并能够以极低的熵率（低至0.8 nats/步）实现稳定、高质量的生成，而标准解码通常在2.0 nats/步附近崩溃。

[阅读原文](https://arxiv.org/abs/2605.00435)

---

## 9. 奥德赛：通过强化学习将VLM扩展到100+

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RL-based training (PPO with turn-level critic) for VLMs in long-horizon decision-making games, directly addressing RL for LLMs with a new training recipe.

**摘要**: arXiv：2605.00347v1宣布类型：新摘要：鉴于视觉语言模型（VLM）的能力迅速增长，将其扩展到视频游戏等交互式决策任务已成为一个有前途的前沿。然而，现有的方法要么依赖于对人类轨迹的大规模监督微调（SFT），要么仅在相对短的视野环境下（通常约20- 30圈）应用强化学习（RL）。在这项工作中，我们研究了基于RL的VLM训练，以在《超级马里奥国度》中进行长期决策，这是一个基于视觉的环境，需要100多次交互，并具有协调的感知、推理和动作。我们首先对关键算法组件进行系统研究，并提出一种具有轻量级回合级批评者的DPP变体，与GRPO和Reinforce++等无批评方法相比，它大大提高了训练稳定性和样本效率。我们进一步表明，与从头开始训练的经典深度RL相比，预训练的VLM提供了强大的动作先验，显着提高了RL训练期间的样本效率，并减少了手动设计选择（如动作工程）的需求。基于这些见解，我们引入了Odysseus，这是一个VLM代理的开放式训练框架，在游戏的多个级别上实现了实质性的收益，并且平均游戏进度至少是前沿模型的3倍。此外，经过训练的模型在游戏内和跨游戏泛化设置下都表现出一致的改进，同时保持了通用领域的能力。总的来说，我们的研究结果确定了使RL在长期多模态环境中稳定有效的关键因素，并为开发VLM作为具体代理提供了实用指导。

[阅读原文](https://arxiv.org/abs/2605.00347)

---

## 10. RSAT：结构化归因使小语言模型成为忠实的表推理者

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jugal Gajjar, Kamalasankari Subramaniakuppusamy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RSAT, a method using GRPO (RL) with a composite reward centered on NLI-based faithfulness to train small LMs for faithful table reasoning with cell-level citations, directly matching RL for LLMs criteria.

**摘要**: arXiv：2605.00199v1宣布类型：新摘要：当语言模型回答表格问题时，用户无法验证哪些单元通知了哪些推理步骤。我们引入了RSAT，这是一种训练小型语言模型（STM，1-8B）的方法，以通过基于表格证据的单元级引用来产生逐步推理。第1阶段（SFT）根据经过验证的推理轨迹教授结构化的SON输出格式。第二阶段（GRPO）优化了以基于NLI的忠诚度以及引用有效性和节俭为中心的复合奖励。在来自两个家族的六个模型中--Qwen 2.5（1.5B/3B/7 B）和Llama 3（1B/3B/8B）--RSAT比单独SFT提高了3.7 $\x $（0.224 $\rightarrow$0.826），具有近乎完美的引用有效性（0.992）。事后归因低于13%的格式成功率，这证实归因必须融入推理中，而不是改造。消融表明忠诚度奖励至关重要：删除它会使忠诚度从0.97下降到0.03。

[阅读原文](https://arxiv.org/abs/2605.00199)

---

## 11. 奥德赛：通过强化学习将VLM扩展到100+

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an RL-based training framework (PPO with turn-level critic) for VLMs in long-horizon decision-making, showing stable improvement and generalization.

**摘要**: 鉴于视觉语言模型（VLM）的能力迅速增长，将其扩展到视频游戏等交互式决策任务已成为一个有前途的前沿。然而，现有的方法要么依赖于对人类轨迹的大规模监督微调（SFT），要么仅在相对短的视野环境下（通常约20- 30圈）应用强化学习（RL）。在这项工作中，我们研究了基于RL的VLM训练，以在《超级马里奥国度》中进行长期决策，这是一个基于视觉的环境，需要100多次交互，并具有协调的感知、推理和动作。我们首先对关键算法组件进行系统研究，并提出一种具有轻量级回合级批评者的DPP变体，与GRPO和Reinforce++等无批评方法相比，它大大提高了训练稳定性和样本效率。我们进一步表明，与从头开始训练的经典深度RL相比，预训练的VLM提供了强大的动作先验，显着提高了RL训练期间的样本效率，并减少了手动设计选择（如动作工程）的需求。基于这些见解，我们引入了Odysseus，这是一个VLM代理的开放式训练框架，在游戏的多个级别上实现了实质性的收益，并且平均游戏进度至少是前沿模型的3倍。此外，经过训练的模型在游戏内和跨游戏泛化设置下都表现出一致的改进，同时保持了通用领域的能力。总的来说，我们的研究结果确定了使RL在长期多模态环境中稳定有效的关键因素，并为开发VLM作为具体代理提供了实用指导。

[阅读原文](https://arxiv.org/abs/2605.00347v1)

---

## 12. AEM：用于多轮动态强化学习的自适应熵调制

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haotian Zhao, Yuxin Zhang, Songlin Zhou, Stephen S. -T. Yau, Wenyu Zhang, Lun Tian, Tianshu Zhu, Yifeng Huang, Yucheng Zeng, Jingnan Gu, Daxiang Dong, Jianmin Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes AEM, a supervision-free credit assignment method for multi-turn agentic RL that adaptively modulates entropy dynamics, showing strong results on SWE-bench.

**摘要**: 强化学习（RL）显着提高了大型语言模型（LLM）代理与环境交互和解决多回合任务的能力。然而，有效的培训仍然具有挑战性，因为稀疏的、仅取决于结果的奖励使得很难将功劳分配给代理人行动轨迹中的各个步骤。一种常见的补救措施是引入密集的中间监督，例如流程奖励模型或辅助自我监督信号，但这增加了监督和调整的复杂性，并且通常在任务和领域中普遍性较差。本文提出了AEM，这是一种无监督的信用分配方法，它在RL训练期间自适应地调节信息量动态，以实现更有效的探索-利用权衡。从理论上讲，我们将熵分析从代币层面提升到响应层面，以减少代币抽样方差，并表明自然梯度下的熵漂移本质上由优势和相对响应量的积决定。具体来说，我们推导出一个实用的代理来重塑训练动态，实现从探索到利用的自然过渡。针对1.5B至32 B参数范围内的各种基准和模型进行的广泛实验证明了AEM的有效性，包括在极具挑战性的SWE台验证基准上集成到最先进的基线时，可以显着提高1.4%。

[阅读原文](https://arxiv.org/abs/2605.00425v1)

---

## 13. 学习如何以及要微型化的内容：以认知为灵感的两阶段优化来进化记忆

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Derong Xu, Shuochen Liu, Pengfei Luo, Pengyue Jia, Yingyi Zhang, Yi Wen, Yimin Deng, Wenlin Zhang, Enhong Chen, Xiangyu Zhao, Tong Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a cognition-inspired two-stage RL framework for LLM agents to learn a memory evolution policy via structured process rewards, directly addressing self-improving agents.

**摘要**: arXiv：2605.00702v1宣布类型：新摘要：大型语言模型（LLM）代理需要长期的用户记忆来实现一致的个性化，但有限的上下文窗口阻碍了跟踪长时间交互中不断变化的偏好。现有的内存系统主要依赖于静态的、手工制作的更新规则;尽管基于强化学习（RL）的代理学习内存更新，但稀疏的结果奖励提供的监督较弱，导致长期优化不稳定。根据记忆图式理论和前额区和海马区之间的功能划分，我们引入了MemCoE，这是一个受认知启发的两阶段优化框架，可以学习如何组织记忆以及更新哪些信息。在第一阶段，我们提出记忆指南归纳，通过解释为文本梯度的对比反馈来优化全局指南;在第二阶段，指南对齐的记忆政策优化使用归纳指南来定义结构化流程奖励，并执行多轮RL来学习遵循指南的记忆进化策略。我们对三个个性化记忆基准进行评估，涵盖显式/隐式偏好以及不同的大小和噪音，并观察到相对于强基线的一致改进，具有良好的鲁棒性、可移植性和效率。

[阅读原文](https://arxiv.org/abs/2605.00702)

---

## 14. AlphaStock：通过具有部署保证的大型语言模型进化白盒库存策略

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chenyu Huang, Jianghao Lin, Zhengyang Tang, Bo Jiang, Ruoqing Jiang, Benyou Wang, Lai Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an LLM-based inventory policy evolution framework using RL, with statistical safety guarantees, directly matching RL for LLMs and self-evolving agent criteria.

**摘要**: 我们研究如何使用大型语言模型来在在线、非静止环境中制定库存策略。我们的工作受到基于LLM的进化搜索的最新进展的推动，例如AlphaEvolve，它在数学发现等静态和高度结构化问题上表现出出色的性能，但不直接适合在线动态库存设置。为此，我们提出了AlphaStock，这是一个基于基于信任区间的认证的端到端库存政策演变和推理框架。该框架使用强化学习训练大型语言模型，整合需求数据以及超出需求的数字和文本特征，并生成具有统计安全保证的白盒库存策略，以供未来部署。我们进一步引入了一个统一的理论界面，将训练、推理和部署连接起来。这使我们能够描述AlphaStock发展出统计上安全和改进的策略的可能性，并量化相对于Oracle安全基准的部署差距。经过合成数据和现实零售数据的测试，AlphaStock的性能优于经典库存策略和基于深度学习的方法。在规范的库存环境中，它会制定新的政策来改进现有的基准。

[阅读原文](https://arxiv.org/abs/2605.00369v1)

---

## 15. Stable-GFlowNet：通过对比轨迹平衡实现多元化和稳健的LLM红色团队

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Minchan Kwon, Sunghyun Baek, Minseo Kim, Jaemyung Yu, Dongyoon Han, Junmo Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Stable-GFN, a novel RL-based red-teaming method for LLMs that improves training stability and diversity via contrastive trajectory balance and robust masking.

**摘要**: arXiv：2605.00553v1宣布类型：新摘要：大型语言模型（LLM）红色团队主动识别LLM的漏洞，是确保安全的重要过程。在红色团队中找到有效且多样化的攻击很重要，但同时实现这两者都具有挑战性。执行分布匹配的生成流网络（GFN）是一种有前途的方法，但它们因训练不稳定和模式崩溃而臭名昭著。特别是，红色团队中不稳定的奖励加速了模式崩溃。我们提出了Stable-GFN（S-GFN），它消除了GFN中的配分函数$Z$估计，并减少了训练不稳定性。S-GFN通过成对比较避免Z估计，并采用强大的掩蔽方法来对抗有噪音的奖励。此外，我们还提出了一个流畅度稳定器，以防止模型陷入产生胡言乱语的局部最优状态。S-GFN提供更稳定的培训，同时保持GFN的最佳政策。我们展示了S-GFN在各种设置中压倒性的攻击性能和多样性。

[阅读原文](https://arxiv.org/abs/2605.00553)

---

## 16. PrefMoE：采用混合专家奖励学习的稳健偏好建模

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ziqin Yuan, Ruiqi Wang, Dezhong Zhao, Baijian Yang, Byung-Cheol Min

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PrefMoE, a mixture-of-experts reward learning framework for robust preference modeling under noisy supervision, directly improving RL for LLMs via better reward design.

**摘要**: arXiv：2605.00384v1宣布类型：新摘要：基于偏好的强化学习通过从比较反馈中学习奖励结构，为手动奖励工程提供了可扩展的替代方案。然而，大规模偏好数据集，无论是从众包注释者收集还是由合成教师生成，通常包含异类和部分冲突的监督，包括注释者之间的分歧和注释者内部的不一致。现有的奖励学习方法通常将单个奖励模型适合此类数据，迫使其对不兼容的信号进行平均，从而限制稳健性。为了解决这个问题，我们提出了PrefMoE，这是一个用于稳健偏好建模的混合专家奖励学习框架。PrefMoE学习多个专门的奖励专家，并使用专家级软路由自适应地将它们组合起来，使该模型能够在嘈杂和异类偏好监督下捕捉多样化的潜在偏好模式。负载平衡调节器通过防止专家崩溃进一步稳定训练。在D4 RL的运动基准和MetaWorld的操纵任务中，PrefMoE提高了偏好预测的稳健性，并带来比强大的单模型基线更可靠的下游政策学习。

[阅读原文](https://arxiv.org/abs/2605.00384)

---

## 17. 了解自己在哪里点击：按政策自蒸馏以实现图形用户界面接地

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yan Zhang, Daiqing Wu, Huawen Shen, Yu Zhou, Can Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel on-policy self-distillation framework for GUI grounding that uses entropy-guided distillation and privileged context, directly addressing RL-based LLM training with dense token-level supervision.

**摘要**: 图形用户界面（图形用户界面）基础将自然语言指令映射到目标元素的视觉坐标，并充当自治图形用户界面代理的核心能力。最近的强化学习方法（例如，GRPO）已实现强劲的性能，但它们依赖于昂贵的多次部署，并且受到硬样本上信号稀疏的影响。这些限制使得政策上的自我蒸馏（OPSD）成为一个有希望的替代方案，该方案从一次推出中提供密集的代币级监督。然而，它对图形用户界面接地的适用性仍有待探索。在本文中，我们介绍了GUI-SD，这是第一个为图形用户界面基础定制的OPSD框架。首先，它使用目标边界框和高斯软面具为教师构建视觉丰富的特权上下文，在不泄露准确坐标的情况下提供信息指导。其次，它采用了熵引导的蒸馏，根据数字重要性和教师信心自适应地对代币进行加权，将优化集中在最有影响力和最可靠的位置上。对六个有代表性的图形用户界面基础基准的广泛实验表明，GUI-SD在准确性和训练效率方面始终优于基于GRPO的方法和原始OPSD。代码和培训数据可在https://zhangyan-ucas.github.io/GUI-SD/上获取。

[阅读原文](https://arxiv.org/abs/2605.00642v1)

---

## 18. 视觉语言模型中针对幻觉的在线自我校准

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Minghui Chen, Chenxu Yang, Hengjie Zhu, Dayan Wu, Zheng Lin, Qingyi Si

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an online self-calibration framework using MCTS and DPO to reduce hallucinations in LVLMs, directly addressing RL-based alignment with self-supervision.

**摘要**: arXiv：2605.00323v1宣布类型：新摘要：大型视觉语言模型（LVLM）经常出现幻觉，生成包含输入图像中缺失的视觉细节的描述。最近的偏好调整方法通常依赖于从GPT等更强大的模型中提取的监督。然而，这种离线范式引入了监督-感知不匹配：学生模型被迫与超出其感知能力的细粒度细节保持一致，学会猜测而不是看。为了获得在线学习的可靠自我监督，我们在LVLM中识别出了生成区分性差距，其中模型在区分性验证方面表现出比开放式生成更高的准确性。利用这一能力，我们提出了\textBF{O}nline \textBF{S}elf-\textBF{CA}lib\textBF{R}ation（OTAR），这是一个集成蒙特卡罗树搜索与双粒度奖励机制的框架，以构建偏好数据并通过直接偏好优化迭代地细化模型。大量实验表明，OTAR在幻觉基准上实现了最先进的性能，同时改进了一般的多模式能力。

[阅读原文](https://arxiv.org/abs/2605.00323)

---

## 19. 集成前先去耦合：SFT和WLVR任务载体的测试时合成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chaohao Yuan, Chenghao Xiao, Yu Rong, Hong Cheng, Long-Kai Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a post-hoc framework (DoTS) that synthesizes SFT and RLVR task vectors at inference time via task vector arithmetic, directly addressing RL for LLMs by integrating RLVR checkpoints without retraining.

**摘要**: arXiv：2605.00610v1宣布类型：新摘要：SFT和WLVR代表了LLM后培训的两种基本但截然不同的范式，每种范式都在不同的维度上表现出色。SFT扩展了知识广度，而WLVR增强了推理深度。然而，整合这些互补优势仍然是一项艰巨的挑战。顺序训练可能会导致灾难性的遗忘，而联合优化通常会遭受严重的梯度冲突。我们通过任务载体的视角分析SFT和WLVR，揭示了这些失败背后的三个结构属性：30* 幅度差异、45* 符号干扰和异类模块更新分布。这些发现表明SFT和WLVR很难直接集成，但它们也表明这两种范式修改了模型的部分互补组件。受这些观察的启发，我们提出了去耦合测试时合成（DoTS），这是一种事后框架，允许SFT和WLVR检查点独立训练，并仅在推理时通过任务向量算术合成它们的能力，而无需更新模型参数。为了减少干扰，DOTS应用选择性稀疏化和保持规范的重新缩放。然后，它对一小群未标记的查询使用Bayesian优化，以搜索一致性和困惑性的帕累托边界上的组合系数。从经验上看，我们的方法在多个数学推理基准上与基于训练的SFT--WLVR集成方法的性能相匹配或超过，仅产生$3%的计算成本。当应用于更强的后训练检查点时，DOTS超越了SOTA模型，并在无需重新调整的情况下推广到域外基准。代码可在https://github.com/chaohaoyuan/DoTS上获取。

[阅读原文](https://arxiv.org/abs/2605.00610)

---

