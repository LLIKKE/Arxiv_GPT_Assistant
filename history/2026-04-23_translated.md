# 💡 今日研究速览 (Daily Summary)

# LLM强化学习与对齐

今天的研究表明，大型语言模型（LLM）的强化学习（RL）更加强大，高效和有针对性。一个关键的主题是开发自适应和结构化的RL方法，超越单一的奖励信号。**EVPO**引入了基于解释方差的自适应临界点利用率，而**策略梯度原始-对偶方法**为安全RLHF提供了形式上的收敛保证。该社区还深度关注于诊断和修复对齐训练的副作用，正如**ARES**的端到端系统修复框架以及对**言语抽搐**和**共享阿谀奉承撒谎回路**的分析所示。此外，正在为特定领域制定新型RL目标，例如用于网络推理的**TRN-R1-Zero* 和用于微调扩散模型的 **DDA**，这表明RL作为多功能训练后工具的作用正在扩大。

# 自我进化和自我改进的代理人

能够自主、长期改进的代理范式正在迅速成熟，研究重点关注可扩展的学习机制和稳定性。一个明显的趋势是从静态训练转向持续、数据高效的自我进化循环。**EasyRL**和**TEMPO**等框架利用渐进式策略和测试时培训来完善政策，从而实现了这一点。这一演变的关键是从交互中学习的能力，正如自动发现压缩规则（**终端代理自进化框架**）或从经验中提取可重复使用的技能（**从经验到技能**）的代理所证明的那样。稳定性和平衡的探索仍然至关重要，可以通过汇总潜在假设（**平衡的本质**）或使用群体相对对齐（**自我改进表格语言模型**）的方法来解决。

# 多模式和视觉-语言-动作模型

多模式系统的研究越来越多地集成强化学习，以完善复杂的推理和生成过程。核心挑战是在长期、结构化的产出中分配细粒度的信用。**OTCA**通过优化轨迹信用来解决视觉生成的问题，而**DT 2 IT-MRM** 则解决了多模式奖励建模中的偏见以改善对齐。有几项作品将RL后训练直接应用于具体化或面向动作的领域：**SpanVLA**能够从负恢复样本中学习以进行驾驶，以及**具有LLM的多模式推理** 使用可验证的奖励进行视觉语义算术。目标是在多模式环境中从被动理解转向可靠的、奖励驱动的决策。

# 潜在推理与流程优化

人们齐心协力来更好地理解、引导和优化模型的内部推理过程，将它们视为需要调整的潜在变量。方法正在变得越来越复杂，从简单的监督转向免培训驾驶或潜在空间政策学习。**OLLM** 用离散潜在变量为下一个代币选项建模以实现高效RL，**GRIL**通过多回合RL框架教LLM暂停。分析论文提供了重要的见解，展示了**答案令牌如何读取推理痕迹**以及**推理结构如何对安全性很重要**。该方向旨在使推理更加透明、可靠和可控，无论是通过架构创新（**基于对象的程序合成**）还是子空间对齐（**发现共享逻辑子空间**）。

# 奖励设计与积分分配

高级奖励设计被认为是有效RL的基础，今天的论文引入了新颖的归因和验证结构。重点是创建信息更多且不太容易出现游戏或不一致的奖励。**Groupwise排名奖励**通过基于可验证的子奖励进行排名来解决推理与答案的不一致性。** SAVOIR**在社交互动中使用Shapley值进行细致入微的奖励归因，而**DR-MMSearchAgent**使用动态奖励校准来防止过早崩溃。这些方法超越了二进制正确性，旨在塑造整个生成过程的质量和完整性，这也是**蒸馏陷阱和警卫** 校准教师模型的目标。

---

## 1. 优先考虑最好的：通过奖励超过答案正确性来激励可靠的多模式推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Mengzhao Jia, Zhihan Zhang, Meng Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Groupwise Ranking Reward, a new reward design for RL with verifiable rewards (RLVR) that addresses reasoning-answer inconsistency in multimodal reasoning.

**摘要**: arXiv：2604.18892v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）通过奖励可验证的最终答案来改进多模式推理。然而，答案正确的轨迹可能仍然依赖于不完整的推导、薄弱的证据或与结论相矛盾的陈述。答案正确性和推理有效性之间的这种差距（我们称之为推理-答案不一致性）激励了多模式RL中的轨迹监督。我们比较了两种主要方法：奖励模型（RM）和生成性奖励（GR）。RM很高效，并在早期培训中提供帮助，但随着政策分配的变化，它们的收益会减弱; GR可以提高绩效，但可能会提供不稳定的回报并且计算成本高昂。因此，我们提出了Groupwise Ranking Reward，它对同一提示的验证者传递的轨迹进行一次排名，并相应地重新分配奖励。分组比较更好地区分较强和较弱的正确轨迹，法官费用比GR更低。实验表明，WLVR会加剧推理答案的不一致性，而轨迹监督会加剧推理答案的不一致性。Groupwise Ranking Reward总体表现最好，将可靠性条件准确性从47.4%提高到54.7%。

[阅读原文](https://arxiv.org/abs/2604.18892)

---

## 2. 通过观察上下文压缩实现高效终端代理的自进化框架

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jincheng Ren, Siwei Wu, Yizhi Li, Kang Zhu, Shu Xu, Boyu Feng, Ruibin Yuan, Wei Zhang, Riza Batista-Navarro, Jian Yang, Chenghua Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-evolving framework for terminal agents that automatically discovers and refines compression rules from interaction trajectories, enabling long-horizon improvement.

**摘要**: arXiv：2604.19572v1宣布类型：新摘要：随着模型能力的进步，研究越来越多地转向长期、以终端为中心的代理任务，其中原始环境反馈通常保留在交互历史中，以支持未来的决策。然而，重复保留此类反馈会带来大量冗余，并导致累积代币成本随着步骤数量的增加而成二倍增长，从而阻碍了长期推理。尽管观察压缩可以缓解这个问题，但终端环境的多样性使得基于启发式或固定提示的方法难以普遍化。我们提出了TACO，这是一个即插即用、自我进化的终端代理压缩框架，可以自动从现有终端代理的交互轨迹中发现和完善压缩规则。TerminalBench（TB 1.0和TB 2.0）和四个额外的终端相关基准测试（即，SWE-Bench Lite、DeliveBench、DevEval和CRUST-Bench）表明，TACO能够在主流代理框架和强大的主干模型中持续提高性能。借助MiniMax-2.5，它可以提高大多数基准测试的性能，同时将令牌负担减少约10%。在TerminalBench上，它在强大的代理模型中带来了1%-4%的一致收益，并在相同代币预算下进一步提高了约2%-3%的准确性。这些结果证明了终端代理的自我进化、任务感知压缩的有效性和普遍性。

[阅读原文](https://arxiv.org/abs/2604.19572)

---

## 3. 简单示例即可：通过数据高效强化学习自进化LLM

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhiyin Yu, Bo Zhang, Qibin Hou, Zhonghai Wu, Xiao Luo, Lei Bai

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EasyRL, a self-evolving LLM framework using data-efficient RL with a progressive divide-and-conquer strategy for post-training.

**摘要**: arXiv：2604.18639v1宣布类型：新摘要：之前基于LLM的RL研究通常遵循具有高注释成本的监督学习，或使用投票或基于信息的奖励的无监督范式。然而，由于注释成本高昂以及模型崩溃或奖励黑客等问题，它们的性能仍然远不能令人满意。为了解决这些问题，我们引入了一种受认知学习理论启发的新视角，并提出了一种名为EasyRL的新颖方法。EasyRL的核心是通过将来自简单标签数据的可靠知识转移与处理日益困难的未标签数据的渐进式分而治之的策略集成起来来模拟人类认知获取曲线。具体来说，我们使用具有少数镜头标记数据的监督RL来初始化热身模型。随后是对困难的未标记数据采取分而治之的伪标记策略，将针对低不确定性情况的基于一致性的选择和针对中等不确定性情况的基于反射的分辨率相结合。最后，采用迭代伪标签和RL的难度渐进式自我训练进一步增强了模型的推理能力。EasyRL提供了一个统一的自我进化框架，可促进LLM的数据高效后培训。数学和科学基准的实验结果表明，EasyRL仅使用10%的简单标记数据，其性能始终优于最先进的基线。

[阅读原文](https://arxiv.org/abs/2604.18639)

---

## 4. TEMPO：扩展大型推理模型的测试时间训练

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qingyang Zhang, Xinke Kong, Haitao Wu, Qinghua Hu, Minghao Wu, Baosong Yang, Yu Cheng, Yun Luo, Ganqu Cui, Changqing Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TEMPO, a test-time training framework for large reasoning models that interleaves policy refinement with critic recalibration, directly addressing self-improvement through a scalable RL-like loop.

**摘要**: arXiv：2604.19295v1宣布类型：新摘要：测试时训练（TTT）在推理时间内调整未标记的测试实例上的模型参数，从而不断扩展离线训练所及的能力。尽管初步取得了进展，但LRM的现有TTT方法很快就达到了稳定状态，并且不会受益于额外的测试时间计算。如果没有外部校准，自发的回报信号随着政策模型的发展而越来越漂移，导致绩效停滞和多样性崩溃。我们提出TEMPO，这是一个TTT框架，它将对未标签问题的政策细化与对标签数据集的定期批评者重新校准交织在一起。通过通过期望最大化（EM）算法形式化这个交替过程，我们揭示了现有方法可以被解释为省略了关键的重新校准步骤的不完整变体。重新引入这一步骤收紧了证据下限（ELBO）并实现持续改进。在不同的模型家族（Qwen 3和OLMO 3）和推理任务中，TEMPO将AIME 2024上的OLMO 3 - 7 B从33.0%提高到51.1%，将Qwen 3 - 14 B从42.3%提高到65.8%，同时保持高度多样性。

[阅读原文](https://arxiv.org/abs/2604.19295)

---

## 5. ARES：自适应红色团队和政策奖励系统的端到端修复

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiacheng Liang, Yao Ma, Tharindu Kumarage, Satyapriya Krishna, Rahul Gupta, Kai-Wei Chang, Aram Galstyan, Charith Peris

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ARES, a framework for adaptive red-teaming and end-to-end repair of RLHF systems, directly targeting reward model and policy vulnerabilities with a novel two-stage fine-tuning process.

**摘要**: arXiv：2604.18789v1宣布类型：新摘要：来自人类反馈的强化学习（RL HF）是调整大型语言模型（LLM）的核心，但它引入了一个关键漏洞：不完美的奖励模型（RM）在未能惩罚不安全行为时可能会成为单点失败。虽然现有的红色团队方法主要针对政策层面的弱点，但它们忽视了我们所说的系统性弱点案例，即核心LLM和RM同时失败。   我们提出了ARES，这是一个系统性地发现和缓解此类双重漏洞的框架。ARES采用“安全导师”，通过组合结构化组件类型（主题、角色、策略、目标）来动态构建语义连贯的对抗提示，并生成相应的恶意和安全响应。这种双重目标方法同时暴露了核心LLM和RM的弱点。利用获得的漏洞，ARES实施了两阶段修复过程：首先微调RM以更好地检测有害内容，然后利用改进后的RM来优化核心模型。多个对抗性安全基准的实验表明，ARES在保留模型能力的同时大幅增强了安全稳健性，为全面的WLHF安全性对齐建立了新范式。

[阅读原文](https://arxiv.org/abs/2604.18789)

---

## 6. 学习认可正确的步骤：视觉生成的感知时间流程优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, YunGu, XueLong Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Objective-aware Trajectory Credit Assignment (OTCA), a structured RL framework for fine-grained reward credit assignment in diffusion-based visual generation, directly improving RL for generative models.

**摘要**: arXiv：2604.19234v1宣布类型：新摘要：强化学习，特别是群体相对政策优化（GRPO），已成为具有人类偏好信号的训练后视觉生成模型的有效框架。然而，其有效性从根本上受到粗糙奖励信用分配的限制。在现代视觉生成中，通常使用多个奖励模型来捕获异类目标，例如视觉质量、运动一致性和文本对齐。现有的GRPO管道通常将这些奖励分解为单个静态纯量，并在整个扩散轨迹上均匀传播。这种设计忽略了不同去噪步骤的特定阶段角色，并产生了不合时宜或不兼容的优化信号。为了解决这个问题，我们提出了时间感知轨迹信用分配（OTCA），这是一种用于细粒度GRPO训练的结构化框架。OTCA由两个关键组件组成。轨迹级信用分解估计不同去噪步骤的相对重要性。多目标信用分配在整个去噪过程中自适应地加权和组合多个奖励信号。通过联合建模时间信用和目标级别信用，OTCA将粗略奖励监督转换为结构化的、时间步感知的训练信号，该信号更好地匹配基于扩散的生成的迭代性质。大量实验表明，OTCA在评估指标上一致提高了图像和视频生成质量。

[阅读原文](https://arxiv.org/abs/2604.19234)

---

## 7. EVPO：LLM后培训中自适应批评利用的解释方差策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chengjun Pan, Shichun Liu, Jiahang Lin, Dingwei Zhu, Jiazheng Zhang, Shihan Dou, Songyang Gao, Zhenhua Han, Binghai Wang, Rui Zheng, Xuanjing Huang, Tao Gui, Yansong Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EVPO, a novel RL method for LLM post-training that adaptively switches between critic-based and critic-free advantage estimation based on explained variance.

**摘要**: arXiv：2604.19485v1宣布类型：新摘要：LLM后培训的强化学习（RL）面临着一个基本的设计选择：是否使用有经验的批评者作为政策优化的基线。经典理论支持基于批评的方法，例如PPO来减少方差，但像GRPO这样的无批评替代方案因其简单性和竞争性性能而获得广泛采用。我们表明，在稀疏回报设置中，有学识的批评者可以注入超过其捕获的状态信号的估计噪音，从而增加而不是减少优势方差。通过将基线选择视为卡尔曼过滤问题，我们将PPO和GRPO统一为卡尔曼收益的两个极端，并证明可从单个训练批次计算的解释方差（EV）识别了确切的边界：正EV表明批评者减少了方差，而零或负EV则表明它扩大了方差。基于这一见解，我们提出了解释方差策略优化（EVPO），该策略在每个训练步骤监控批量级EV，并在基于批评的优势估计和批量平均优势估计之间自适应地切换，可以证明在每个步骤中实现的方差不会大于两者中的更好者。在涵盖经典控制、代理互动和数学推理的四项任务中，EVPO始终优于PPO和GRPO，无论哪一个固定基线在给定任务中更强。进一步的分析证实，自适应门控在训练中跟踪批评者成熟度，并且理论上推导出的零阈值在经验上是最优的。

[阅读原文](https://arxiv.org/abs/2604.19485)

---

## 8. 伪装还是捏造？训练语言模型以进行扎根推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yiwen Qiu, Linjuan Wu, Yizhou Liu, Yuchen Yan, Jin Ma, Xu Tan, Yao Hu, Daoxin Zhang, Wenqi Zhang, Weiming Lu, Jun Xiao, Yongliang Shen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GRIL, a multi-turn RL framework for grounded reasoning that teaches LLMs to pause when information is insufficient, directly matching RL for LLMs and latent reasoning criteria.

**摘要**: arXiv：2604.19656v1宣布类型：新摘要：大型语言模型在复杂推理任务上取得了显着进展。然而，当输入不完整时，他们经常隐含地捏造信息，产生自信但不可靠的结论--我们称之为无根据推理的失败模式。我们认为，这个问题不是由于推理能力不足，而是由于缺乏推理边界意识--即在有效推理的必要前提缺失时识别的能力。为了解决这个问题，我们提出了通过交互式强化学习进行接地推理（GRIL），这是一个用于在不完整信息下进行接地推理的多轮强化学习框架。GRIL将推理过程分解为两个阶段：澄清和暂停，用于识别可用信息是否足够，以及扎根推理，用于在必要前提建立后执行任务求解。我们设计特定阶段的奖励来惩罚幻觉，使模型能够检测到差距、主动停止并在澄清后恢复推理。针对GSM 8 K-Insult和MetaMath-Insult的实验表明，GRIL显着改善了前提检测（高达45%），导致任务成功率增加30%，同时将平均响应长度缩短20%以上。额外的分析证实了对有噪音的用户响应的稳健性以及对非分发任务的概括性。

[阅读原文](https://arxiv.org/abs/2604.19656)

---

## 9. OLLM：基于选项的大型语言模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shashank Sharma, Janina Hoffmann, Vinay Namboodiri

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces OLLM, a method using a discrete latent variable to model next-token options, enabling efficient latent-space policy learning for RL in LLMs, directly aligning with RL for LLMs.

**摘要**: arXiv：2604.19087v1宣布类型：新摘要：我们引入了选项LLM（OLLM），这是一种简单、通用的方法，用下一个令牌的\textit{学习选项集}替换标准LLM的单个下一个令牌预测，由离散潜在变量索引。OLLM不是依赖于温度或抽样启发法来诱导多样性，而是明确地对变异进行建模：一个小的潜在空间参数化多个看似合理的下一个代币选项，这些选项可以由下游策略选择或搜索。从架构上看，OLLM是一个轻量级的“插件”，在输出头之前插入两层：编码器和解码器，允许几乎任何预训练的LLM以最少的额外参数进行转换。我们将OLLM应用于在OpenMathReasoning上训练并在OmniMath上评估的1.7B参数主干（只需1.56美元\%$参数可训练）。SOTA LoRA适应的基线最终答案正确性峰值为51美元\%$，而OLLM的选项集在最佳潜在选择下允许高达70美元\sim\%$。然后，我们在潜在空间中制定一项紧凑的政策，释放潜在的控制发电量。在低维选项空间中操作使得奖励优化更加样本有效，并且大大减少了常见的未对准（例如，语言切换或退化推理），因为策略受限于在SFT期间学习的选项。至关重要的是，这种对齐来自模型结构，而不是额外的KL或手工对齐损失。我们的研究结果表明，可选的下一个令牌建模增强了数学推理的可控性，鲁棒性和效率，并强调潜在空间策略学习是LLM中强化学习的一个有前途的方向。

[阅读原文](https://arxiv.org/abs/2604.19087)

---

## 10. 从人类反馈中进行安全强化学习的政策梯度原始-二元方法

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiang Liu, Adrienne Kline, Ermin Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a primal-dual policy gradient method for Safe RLHF with global convergence guarantees for infinite-horizon discounted CMDPs.

**摘要**: arXiv：2604.19024v1宣布类型：新摘要：来自人类反馈的安全强化学习（Safe RL HF）最近通过脱钩人类对有益和无害的偏好，在开发有益和无害的大型语言模型方面取得了经验上的成功。现有的方法通常依赖于根据人类反馈来匹配固定水平奖励模型，并且仅经过经验验证。在本文中，我们将安全的RL HF公式化为无限视野折扣的约束马尔科夫决策过程（CMDP），因为人类可能会在连续的交互序列中与模型交互，而不是在单个有限事件中。我们提出了两种安全的RL HF算法，它们不需要奖励模型匹配，并且与假设固定长度轨迹的先前工作相反，支持灵活的轨迹长度进行训练。这两种算法都基于原始-二元方法，并在政策梯度迭代、轨迹样本长度和人类偏好查询方面以多项速率实现全局收敛保证。据我们所知，这是第一次在人类反馈下研究无限视界折扣CMDP并建立全局、非渐进收敛的工作。

[阅读原文](https://arxiv.org/abs/2604.19024)

---

## 11. 使用神经解释语言的基于对象的程序合成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Matthew V. Macfarlane, Cl\'ement Bonnet, Herke van Hoof, Levi H. S. Lelis

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel neural architecture that learns a discrete, latent program language end-to-end, enabling gradient-based search for compositional generalization, aligning with latent reasoning methods.

**摘要**: arXiv：2604.18907v1宣布类型：新摘要：长期以来，程序归纳的一个核心挑战是符号方法和神经方法之间的权衡。符号方法提供组合概括和数据效率，但它们的可扩展性受到域特定语言（SL）等形式主义的限制，这些语言的创建需要劳动密集型，并且可能无法转移到新的域。相比之下，神经网络灵活地从数据中学习，但在组成和分布外设置中往往难以概括。我们通过名为神经语言解释器（NLI）的潜在适应网络架构实例来弥合这一鸿沟，该架构可端到端学习自己的离散、类符号编程语言。NLI自主发现原始操作的词汇表，并使用新型可微神经执行器来解释这些原始操作的变长序列。这使得NLI能够表示不受固定数量计算步骤约束的程序，使其能够解决比训练期间看到的问题更复杂的问题。为了使这些离散的组合程序结构适合基于梯度的优化，我们采用了Gumbel-Softmax松弛，使整个模型能够进行端到端训练。至关重要的是，这种相同的可区分性可以实现强大的测试时间适应。在推断时，NLI的程序感应器提供初始程序猜测。然后，通过神经执行器的梯度下降来细化这个猜测，从而能够高效搜索最能解释给定数据的神经程序。我们证明，在需要组合概括和快速适应不可见任务的任务上，NLI优于上下文学习、测试时训练和连续潜在程序网络。我们的结果为模型建立了一条新的道路，该模型将离散语言的组合性与基于梯度的搜索和神经网络的端到端学习相结合。

[阅读原文](https://arxiv.org/abs/2604.18907)

---

## 12. 发现共享逻辑子空间：通过自然语言和符号视图的对齐来引导LLM逻辑推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Feihao Fang, My T. Thai, Yuanyuan Lei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free method to steer LLM reasoning via a discovered shared logical subspace, aligning natural and symbolic views to improve logical reasoning.

**摘要**: arXiv：2604.19716v1宣布类型：新摘要：大型语言模型（LLM）仍然在多步逻辑推理方面遇到困难。现有的方法要么纯粹以自然语言形式细化推理链，要么附加符号求解器作为外部模块。在这项工作中，我们询问LLM是否包含一个共享的内部逻辑子空间，该子空间同时对齐推理过程的自然语言和符号语言观点。我们的假设是，这个逻辑子空间捕捉逻辑推理能力的LLM共享视图，同时保持独立的表面形式。为了验证这一点，我们采用典型相关分析对自然语言和符号语言推理链的成对剩余激活，学习具有最大交叉视图相关性的低维子空间。此外，我们设计了一种免训练的方法，沿着这个逻辑子空间引导LLM推理链，从而利用来自两个视图的互补推理信号。对四个逻辑推理基准的实验证明了我们方法的有效性，准确性提高了高达11个百分点，并且在域外问题上具有良好的概括性。

[阅读原文](https://arxiv.org/abs/2604.19716)

---

## 13. 蒸馏陷阱和防护装置：LLM蒸馏率的校准旋钮

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Weixiao Zhan, Yongcheng Jing, Leszek Rutkowski, Dacheng Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement fine-tuning (RFT) method to calibrate a teacher LLM's distillability, directly aligning with RL for LLMs via reward design for model safety and transfer.

**摘要**: arXiv：2604.18963v1宣布类型：新摘要：知识提炼（KD）将大型语言模型（LLM）的能力转移到较小的学生，但它可能会不可预测地失败，并且也会加剧模型泄漏风险。我们的分析揭示了几个蒸馏陷阱：尾部噪音、政策外不稳定性，以及最根本的，扭曲培训信号的师生差距。这些陷阱表现为过度自信的幻觉、自我纠正崩溃和局部解码退化，导致蒸馏失败。受这些发现的激励，我们提出了一种事后校准方法，据我们所知，该方法首次能够通过强化微调（RFT）来控制教师的可操作性。我们的目标结合了任务实用程序、KL锚和跨代币器校准奖励。这使得可互换性成为基础模型的实用安全杠杆，将强大的师生转移与部署感知模型保护联系起来。数学、知识QA和学习跟随任务的实验表明，从可识别的校准教师中提炼出的学生的表现优于SFT和KD基线，而不可识别的校准教师保留了他们的任务表现，但导致提炼出的学生崩溃，为更好的KD和模型IP保护提供了实用的旋钮。

[阅读原文](https://arxiv.org/abs/2604.18963)

---

## 14. 视觉和语言导航中自我完善者的平衡本质

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhen Liu, Yuhan Liu, Jinjun Wang, Jianyi Liu, Wei Song, Jingwen Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-improvement mechanism for VLN agents that balances behavioral diversity and learning stability via latent hypothesis generation and aggregation.

**摘要**: arXiv：2604.19064v1宣布类型：新摘要：在视觉和语言导航（VLN）中，仅使用标准VLN行动监督，从政策诱导的经验中进行自我改进，这严重取决于平衡行为多样性和学习稳定性，这决定着代理人是否可以提取可靠的学习信号进行改进。增加行为多样性对于揭露替代行动假设是必要的，但可能会破坏政策诱导的学习信号的稳定性，而过于保守的稳定性约束会抑制探索并诱导早期承诺，从而使可靠的自我改进变得困难。为了应对这一挑战，我们提出了稳定-多样性平衡（MDB），这是一种即插即用机制，用于VLN中平衡自我改进。MDB通过在受描述条件的隐藏状态中应用受控转移，将每个决策步骤扩展为多个潜在行为假设，然后执行可靠性感知的软评估和聚合，以在学习期间保留多样化但受描述一致的替代方案。显式正规化器进一步限制假设相互作用，防止假设多样性的过度漂移或过早崩溃，并在不丢弃训练信号的情况下稳定自我完善。R2 R、SOON和REVERIE上的实验显示出一致的改进;例如，在REVERIE val-unseen上，MDB将SPL从33.73提高到35.93，将OSR从51.07提高到54.25。

[阅读原文](https://arxiv.org/abs/2604.19064)

---

## 15. TRN-R1-Zero：仅通过强化学习的LLM进行文本丰富的网络推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yilun Liu, Ruihong Qiu, Zi Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces TRN-R1-Zero, a post-training framework for text-rich network reasoning trained solely via a novel RL objective without supervised fine-tuning.

**摘要**: arXiv：2604.19070v1公告类型：新摘要：富文本网络（TRN）上的零触发推理仍然是一个具有挑战性的前沿，因为模型必须在没有特定任务监督的情况下将文本语义与关系结构集成在一起。虽然图神经网络依赖于固定的标签空间和有监督的目标，但最近基于大型语言模型（LLM）的方法往往忽略了图上下文或依赖于从更大的模型中提取，从而限制了泛化。我们提出TRN-R1-Zero，这是一个仅通过强化学习训练的TRN推理的后训练框架。TRN-R1-Zero使用邻居感知的组相对政策优化目标直接优化基础LLM，该目标基于邻近信号信息量的新颖边际收益指标动态调整奖励，有效地引导模型走向关系推理。与先前的方法不同，TRN-R1-Zero不需要有监督的微调或从大型推理模型生成的思想链数据。引用、超链接、社交和共同购买TRN基准的广泛实验证明了TRN-R1-Zero的优越性和稳健性。此外，TRN-R1-Zero严格依赖于节点级训练，实现了边缘和图形级任务的零触发推理，超出了跨域传输的范围。该代码库可在https://github.com/superallen13/TRN-R1-Zero上公开获取。

[阅读原文](https://arxiv.org/abs/2604.19070)

---

## 16. SpanVLA：视觉-语言-动作模型的有效动作桥梁和消极恢复样本中的学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zewei Zhou (Tony), Ruining Yang (Tony), Xuewei (Tony), Qi, Yiluan Guo, Sherry X. Chen, Tao Feng, Kateryna Pistunova, Yishan Shen, Lili Su, Jiaqi Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a GRPO-based post-training method for a VLA driving model, enabling learning from negative and recovery behaviors, aligning with RL for LLMs.

**摘要**: arXiv：2604.19710v1宣布类型：新摘要：视觉-语言-动作（VLA）模型提供了一种有前途的自动驾驶范式，用于利用世界知识和推理能力，特别是在长尾场景中。然而，现有的VLA模型经常难以应对使用自回归生成框架的动作生成中的高延迟，并且表现出有限的鲁棒性。在本文中，我们提出了SpanVLA，这是一种新型的端到端自动驾驶框架，集成了自回归推理和流匹配动作专家。首先，SpanVLA引入了一个高效的桥梁，利用VLM的愿景和推理指导，使用以历史轨迹初始化为条件的流匹配策略来高效规划未来轨迹，这显着减少了推理时间。其次，为了进一步提高SpanVLA模型的性能和鲁棒性，我们提出了一种基于GRPO的后训练方法，使VLA模型不仅能够从积极的驾驶样本中学习，还能够学习如何避免典型的消极行为和学习恢复行为。我们进一步引入了mReasoning，这是一种新的现实世界驾驶推理数据集，重点关注复杂、需要推理的场景和负恢复样本。NAVSIM（v1和v2）上的大量实验证明了SpanVLA模型的竞争性能。此外，不同场景的定性结果凸显了我们模型的规划性能和稳健性。

[阅读原文](https://arxiv.org/abs/2604.19710)

---

## 17. DT 2 IT-MRM：多模式奖励建模的去偏偏好构建和迭代训练

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhihong Zhang, Jie Zhao, Xiaojian Huang, Jin Xu, Zhuodong Luo, Xin Liu, Jiansheng Wei, Xuejin Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a debiased construction and iterative training framework for multimodal reward modeling, directly relevant to RL for LLMs via reward design for alignment.

**摘要**: arXiv：2604.19544v1宣布类型：新摘要：多模式奖励模型（MRM）在使多模式大型语言模型（MLLM）与人类偏好保持一致方面发挥着至关重要的作用。训练良好的MRM需要高质量的多模式偏好数据。然而，现有的偏好数据集面临三个关键挑战：偏好强度缺乏粒度、文本风格偏见和不可靠的偏好信号。此外，现有的开源多模式偏好数据集受到大量噪音的影响，但缺乏有效且可扩展的策展方法来提高其质量。为了解决这些限制，我们提出了\textBF{DT 2 IT-MRM}，它集成了\textBF{D}ebiased偏好构建管道、文本到图像（\textBF{T2 I}）偏好数据的新颖重新制定，以及\textBF{I}迭代\textBF{T} raing框架，该框架为\textBF{M}多模式\textBF{R}eward \textBF{M}odeling策展现有的多模式偏好数据集。我们的实验结果表明，DT 2 IT-MRM在三个主要基准测试（VL-RewardBench、Multimodal RewardBench和MM-RL HF-RewardBench）上实现了新的\textBF{最先进的}总体性能。

[阅读原文](https://arxiv.org/abs/2604.19544)

---

## 18. 量子场论的微调小推理模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Nathaniel S. Woodward, Zhiqi Gao, Yurii Kvasiuk, Kendrick M. Smith, Frederic Sala, Moritz M\"unchmeyer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Conducts RL and SFT experiments on small reasoning models for QFT, analyzing reasoning error evolution and releasing a data pipeline.

**摘要**: arXiv：2604.18936v1宣布类型：新摘要：尽管大型语言模型（LLM）在理论物理中的应用越来越多，但对于训练这些模型时如何发展特定领域的物理推理能力的学术探索却很少。为了研究这一点，我们对专门用于理论物理的小（7 B参数）推理模型进行了首次学术微调研究。由于训练此类能力所需的开源可验证训练数据稀缺，我们开发了一个强大的数据生成管道，它既可以创建合成问题，又可以使现有的人类创作问题适合模型训练。选择量子场论（QFT）作为我们的主要领域，我们生成了2，500多个合成问题，以及来自arXiv和标准教学资源的精心策划的人类适应问题集。我们进行强化学习（RL）和监督微调（SFT）实验，对性能收益进行基准测试以及对其他物理领域的推广。我们对微调前后的模型链进行了广泛的分析，以了解RL和SFT期间推理错误如何演变。最后，我们公开发布我们的数据管道、可验证的QFT训练数据和价值2亿美元的QFT推理痕迹代币。

[阅读原文](https://arxiv.org/abs/2604.18936)

---

## 19. 评估驱动的科学发现规模化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haotian Ye, Haowei Lin, Jingyi Tang, Yizhen Luo, Caiyin Yang, Chang Su, Rahul Thapa, Rui Yang, Ruihua Liu, Zeyu Li, Chong Gao, Dachao Ding, Guangrong He, Miaolei Zhang, Lina Sun, Wenyang Wang, Yuchen Zhong, Zhuohao Shen, Di He, Jianzhu Ma, Stefano Ermon, Tongyang Li, Xiaowen Chu, James Zou, Yuzhi Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a framework for scaling evaluation-driven discovery loops where trajectory histories supervise feedback-driven learning, aligning with self-improving agent criteria.

**摘要**: arXiv：2604.19341v1宣布类型：新摘要：语言模型越来越多地用于科学发现，以生成假设、提出候选解决方案、实施系统并迭代地完善它们。这些试错循环的核心是评估：通过验证器、模拟器或特定任务评分功能获得候选解决方案反馈的过程。虽然之前的工作强调了评估的重要性，但尚未明确提出如何以有原则且有效的方式扩大评估驱动的发现循环以突破科学发现的界限的问题，这是本文试图解决的问题。我们引入了简单测试时评估驱动的缩放（SimpleTES），这是一个通用框架，战略性地结合了并行探索、反馈驱动的细化和本地选择，揭示了通过沿着正确维度扩展评估驱动的发现循环而解锁的实质性收益。在跨越六个领域的21个科学问题中，SimpleTES使用gtt-oss模型发现了最先进的解决方案，始终优于前沿模型基线和复杂的优化管道。特别是，我们将广泛使用的LASO算法加速了2倍以上，设计了将门控开销减少24.5%的量子电路路由策略，并发现了超越最著名结果的新Erdos最小重叠结构。除了新颖的发现之外，SimpleTES还产生了实验室级别的历史，这些历史自然地监督反馈驱动的学习。当在成功的轨迹上进行后训练时，模型不仅可以提高已知问题的效率，还可以推广到未发现的问题，发现基础模型未能发现的解决方案。我们的结果共同建立了有效的评估驱动循环扩展，作为推进LLM驱动的科学发现的中心轴，并为实现这些收益提供了一个简单而实用的框架。

[阅读原文](https://arxiv.org/abs/2604.19341)

---

## 20. AbateCell：虚拟细胞储存库的先繁殖后繁殖的代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xue Xia, Chengkai Yao, Mingyu Tsoi, Xinjie Mao, Wenxuan Huang, Jiaqi Wei, Hao Wu, Cheng Tan, Lang Yu, Yuejin Yang, Siqi Sun, Zhangyang Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-improving agent (AblateCell) that performs closed-loop ablation experiments, adaptively selecting mutations under a reward to identify critical components in biological codebases.

**摘要**: arXiv：2604.19606v1公告类型：新摘要：系统性消融对于AI虚拟细胞中的性能增益至关重要，但它们很少执行，因为生物存储库标准化不足，并且与特定领域的数据和格式紧密耦合。虽然最近的编码代理可以将想法转化为实现，但它们通常仅限于生成代码，并且缺乏一个可以重现强大基线并严格测试哪些组件真正重要的验证器。我们引入了AbateCell，这是一种用于虚拟细胞存储库的先复制然后消融的代理，可以缩小这一验证差距。AbateCell首先通过自动配置环境、解决依赖性和数据问题以及重新运行官方评估同时发出可验证的工件来端到端复制报告的基线。然后，它通过生成孤立的存储库突变图并在权衡性能影响和执行成本的奖励下自适应地选择实验来进行闭环消融。在三个单细胞扰动预测库（CPA、GEARS、BioLORD）上进行评估后，AbateCell在恢复地面真相关键组件方面实现了88.9%（人类专家+29.9%）的端到端工作流程成功率和93.3%（启发式+53.3%）的准确性。这些结果使可扩展的，基于存储库的验证和归因直接对生物代码库。

[阅读原文](https://arxiv.org/abs/2604.19606)

---

## 21. 法学硕士知道自己错了，但无论如何都同意：共同的谄媚谎言循环

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Manav Pandey

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a shared neural circuit for sycophancy and lying in LLMs, showing RLHF reduces but does not eliminate this behavior, directly relevant to RL for LLM alignment.

**摘要**: arXiv：2604.19117v1宣布类型：新摘要：当语言模型同意用户的错误信念时，它是未能检测到错误，还是注意到并同意？我们展示后者。在来自五个实验室的十二个开重模型中，跨越小规模到前沿规模，同一组注意力头携带着“此陈述是错误的”信号，无论模型是在自行评估主张还是被迫同意用户的观点。压制这些头会急剧扭转谄媚行为，同时保持事实准确性，因此回路控制的是尊重而不是知识。边缘级路径修补证实，相同的头对头连接会驱动谄媚、事实撒谎和指示撒谎。观点一致（在不存在事实基础真相的情况下）重复使用这些头部位置，但写入垂直方向，排除了对底层进行简单的“真相方向”阅读的可能性。对齐训练使这一回路保持不变：RL HF刷新将谄媚行为减少大约十倍，而共享的头部则持续或增长，这种模式可以在独立模型家族和有针对性的反谄媚DPO下复制。当这些模特谄媚时，他们会注册用户错了，并无论如何都同意了。

[阅读原文](https://arxiv.org/abs/2604.19117)

---

## 22. ReflectMT：内化反思以实现高效和高质量的机器翻译

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kunquan Li, Yingxue Zhang, Fandong Meng, Jinsong Su

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage reinforcement learning method to internalize reflection for efficient, high-quality machine translation, aligning with RL for LLMs.

**摘要**: arXiv：2604.19144v1宣布类型：新摘要：近年来，人们对将大型推理模型（LRM）应用于机器翻译（MT）的兴趣日益浓厚。现有的方法主要采用“先思考后翻译”的范式。尽管显式推理轨迹显着提高了翻译质量，但它们会带来令人望而却步的推理成本和延迟。为了解决这些限制，我们提出了ReflectMT，这是一种用于机器翻译的两阶段反射内化算法，采用“先思考后思考”范式。我们的方法通过强化学习开发模型的“假设-反映-提炼”能力。在第一阶段，我们培养模型的高质量反映和细化能力，从而增强其语义理解和特定任务的知识。在第二阶段，我们训练模型以内化反思期间获得的知识。因此，在推理过程中，ReflectMT以直接翻译模式运行，在第一次尝试时就产生高质量的翻译，无需任何明确的推理步骤。WMT 24等数据集的实验结果表明，我们的模型在推理期间的第一遍翻译在自动指标和基于GPT的评估方面都优于DeepSeek-R1等多步推理LRM，在基于GPT的翻译质量评估方面实现了2.16个百分点的提高，同时将代币消耗减少了94.33%。

[阅读原文](https://arxiv.org/abs/2604.19144)

---

## 23. 匹配前思考：一般人重新识别的强化推理范式

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Quan Zhang, Jingze Wu, Jialong Wang, Xiaohua Xie, Jianhuang Lai, Hongbo Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reasoning-driven person ReID paradigm using CoT warm-up and efficient reinforcement learning to guide the model towards identity-causal cues.

**摘要**: arXiv：2604.19218v1宣布类型：新摘要：学习具有多场景通用性的身份区分表示已成为人员重新识别（ReID）的一个关键目标。然而，主流的感知驱动范式倾向于从大量注释数据中识别适合性，而不是身份因果线索理解，这对多重破坏来说是一种脆弱的表示。在这项工作中，ReID-R被提出为一种新颖的推理驱动范式，通过将思想链融入ReID管道中来实现显式身份理解和推理。具体来说，ReID-R由两个阶段的贡献组成：（i）区分推理热身，其中模型以无CoT标签的方式训练，以获得身份感知的特征理解;（ii）高效强化学习，它提出非平凡的采样来构建场景可概括的数据。在此基础上，ReID-R利用高质量的奖励信号来引导模型专注于ID相关线索，实现准确的推理和正确的反应。对多个ReID基准的广泛实验表明，ReID-R仅使用14.3K个非平凡数据（现有数据规模的20.9%），作为更好的方法即可实现有竞争力的身份识别。此外，得益于固有推理，ReID-R可以为结果提供高质量的解释。

[阅读原文](https://arxiv.org/abs/2604.19218)

---

## 24. 离散收件箱匹配

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuyuan Chen, Shiyi Wang, Peter Potaptchik, Jaeyeon Kim, Michael S. Albergo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Discrete Tilt Matching (DTM), a new likelihood-free RL method for fine-tuning masked diffusion LLMs, directly addressing RL for LLMs with a novel reward tilting and matching objective.

**摘要**: arXiv：2604.18739v1公告类型：新摘要：掩蔽扩散大型语言模型（dLLMS）是自回归生成的一个有希望的替代方案。虽然强化学习（RL）方法最近已被调整为dLLM微调，但它们的目标通常取决于序列级边缘似然性，这对于掩蔽扩散模型来说是棘手的。为了解决这个问题，我们推导出了离散时间表匹配（DDA），这是一种无可能的方法，它将dLLM微调重新构建为奖励倾斜下局部去掩蔽后验的状态级匹配。DMS采用带有显式最小化器的加权交叉熵目标的形式，并接受提高训练稳定性的控制变量。在合成迷宫规划任务中，我们分析了DMS的模拟时间表和控制变量如何影响训练稳定性并防止模式崩溃。在规模上，使用DMS进行微调的LLaDA-8B-Direct在数独和倒计时上产生了强劲的收益，同时在Math 500和GSM 8 K上保持了竞争力。

[阅读原文](https://arxiv.org/abs/2604.18739)

---

## 25. 使用LLM进行视觉语义算术的多模式推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chuou Xu, Liya Ji, Qifeng Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Semantic Arithmetic Reinforcement Fine-Tuning (SAri-RFT) using a verifiable function and GRPO to post-train LVLMs for visual relational reasoning, directly matching RL for LLMs.

**摘要**: arXiv：2604.19567v1公告类型：新摘要：作为后训练的强化学习（RL）对于增强大型语言模型（LLM）在编码和数学方面的推理能力至关重要。然而，它们的视觉语义算术（从图像中推断关系）的能力仍然被充分探索。经典文本类比“国王”-“男人”+“女人”=“女王”说明了关系推理，但用“国王”和“男人”的图像替换文本会显着降低性能，因为它需要常识知识并从不相关的视觉细节中提取简洁的概念。这种能力对于非结构化环境中的服务和家用机器人非常重要，在这种环境中，机器人必须推断对象、代理和动作之间的语义关系。在厨房中，从图像中识别“粉”和“蛋糕”通过“is made of”相关，从而建立了感知中的符号关系，从而实现工具替代、任务概括和改进的语义推理。先前的工作通过在载体算术后解码图像特征来实现语义算术，但存在形态差距并且缺乏系统评估。在本文中，我们制定了两项新任务：二项减法和三项运算，并构建了用于基准测试的图像关系对数据集（IRPD）。我们进一步提出了语义算术强化微调（SAri-RFT），它使用可验证函数和组相对策略优化（GRPO）对大型视觉语言模型（LVLM）进行后训练。我们的方法在IRPD和现实世界的Visual 7 W-Telling数据集上实现了最先进的结果。通过为LVLM配备强大的跨模式关系推理，这项工作提高了家用机器人在感知中进行符号推理的能力，增强了复杂环境中的决策、工具适应性和人机交互。补充材料中提供了数据集和源代码。

[阅读原文](https://arxiv.org/abs/2604.19567)

---

## 26. DR-MMSearchAgent：深化多模式搜索代理中的推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shengqin Wang, Wentao Yan, Huichi Zhou, Yihang Chen, Kun Shao, Zhizhong Zhang, Yuan Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multimodal search agent framework that uses advantage signals from entire rollout trajectories and dynamic reward calibration to prevent premature interaction collapse, aligning with self-improving agent criteria.

**摘要**: arXiv：2604.19264v1公告类型：新摘要：多模态模型因其利用外部工具来处理复杂任务的能力而受到广泛关注。然而，据观察，这样的代理经常遇到过早的交互崩溃，导致两个主要原因：1）终端奖励往往附加在最后一个令牌上，阻止了优势区分轨迹与探索性行为; 2）过度冗余的上下文阻碍了代理吸收有用的反馈。为了解决这些问题，我们提出了Deeping Reasoning MMSearchAgent，该框架利用结构接近性从整批中的整个推出轨迹中推导出优势信号，从而进一步鼓励生成不同长度的轨迹，即使包含相同的正确答案。此外，还采用差异化高斯奖励来动态校准交互容忍度，从而确保信息可靠性并减少冗余。为了支持多回合交互训练，我们构建了一个多步骤深度推理数据集，包括3602个高质量QA对，至少有3个推理步骤。大量实验表明，我们的方法实现了最先进的性能，在DVQA测试中比MMSearch-R1高出8.4$\%$。

[阅读原文](https://arxiv.org/abs/2604.19264)

---

## 27. 通过迭代组对齐自我改进的表格语言模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yunbo Long, Tejumade Afonja, Alexandra Brintrup, Mario Fritz

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a self-improving framework for tabular language models using automated feedback and a group-relative advantage alignment objective, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2604.18966v1宣布类型：新摘要：虽然语言模型已适应表格数据生成，但仍然存在两个基本限制：（1）静态微调产生的模型无法从自己生成的样本中学习并适应自我纠正，（2）自回归目标保留局部标记一致性，但忽视了全局统计属性，从而降低了表格质量。强化学习提供了一种潜在的解决方案，但需要设计平衡竞争目标的奖励函数--这对于表格数据来说不切实际。为了填补这一空白，我们引入了TabGRAA（表格组相对优势对齐），这是第一个通过自动反馈生成表格数据的自我改进框架。在每次迭代中，TabGRAA使用\{自动质量信号} --例如双样本互换性分类器或基于距离的奖励--将新生成的样本划分为高质量和低质量组，然后优化组相对优势目标，以加强现实模式，同时惩罚伪影。具体信号是模块化选择，而不是框架的固定组件。这建立了一个良性反馈循环，其中质量信号在每一轮中根据新生成的合成}样本重新计算;语言模型仅对这些自生成的信号进行微调，因此在对齐期间不会暴露额外的真实记录，从而减轻了初始监督微调之外的数据泄露风险。实验表明，TabGARA在保真度、实用性和隐私方面优于现有方法，同时匹配或超越基于扩散的合成器，将表格合成从静态统计复制推进到动态、自我改进的生成。

[阅读原文](https://arxiv.org/abs/2604.18966)

---

## 28. SAVOIR：通过基于Shapley的奖励归因学习社交Savoir-Faire

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xiachong Feng, Yi Jiang, Xiaocheng Feng, Deyi Yin, Libo Qin, Yangfan Ye, Lei Huang, Weitao Ma, Yuxuan Gu, Chonghan Qin, Bing Qin, Lingpeng Kong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SAVOIR, a novel RL framework using Shapley values for reward attribution to train socially intelligent language agents.

**摘要**: arXiv：2604.18982v1宣布类型：新摘要：社交智力，即驾驭复杂人际互动的能力，对语言代理人提出了根本挑战。通过强化学习训练此类代理人需要解决学分分配问题：确定个人话语如何对多轮对话结果做出贡献。现有的方法直接使用语言模型来分配剧集级奖励，从而产生具有追溯性且缺乏理论基础的属性。我们提出SAVOIR（ShApley Value fOr SocIal RL），这是一个基于合作博弈论的新颖原则框架。我们的方法结合了两个补充原则：预期效用将评估从回顾性归因转向前瞻性估值，捕捉话语的战略潜力，以实现有利的未来轨迹;沙普利价值观通过效率、对称性和边缘性的公理保证确保公平的信用分配。SOTOPIA基准测试的实验表明，SAVOIR在所有评估设置中都实现了新的最先进性能，我们的7 B模型与GPT-4 o和Claude-3.5-Sonnet等专有模型相匹配或超越。值得注意的是，即使是大型推理模型也始终表现不佳，这表明社交智能需要与分析推理在本质上不同的能力。

[阅读原文](https://arxiv.org/abs/2604.18982)

---

## 29. 流强化学习的有意更新

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Arsalan Sharifnassab, Mohamed Elsayed, Kris De Asis, A. Rupam Mahmood, Richard S. Sutton

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes intentional updates for streaming RL, a new scalable RL training recipe that aims for a specified change in function output, directly relevant to RL for LLMs.

**摘要**: arXiv：2604.19033v1宣布类型：新摘要：在基于梯度的学习中，以参数单位选择的步骤不会产生可预测的函数输出的每步变化。这通常会导致流媒体设置的不稳定（即，批量大小=1），其中随机性未被平均化，并且更新幅度可能暂时变得任意大或小。相反，我们提出有意更新：首先指定更新的预期结果，然后求解大致实现该结果的步骤。该策略在通过正规化最小均方算法的在线监督线性回归中具有先例，该算法选择步骤大小以产生与当前误差成比例的指定函数输出变化。我们通过定义适当的预期结果将这一原则扩展到流媒体深度强化学习：有意TD旨在固定降低TD误差，而有意策略梯度旨在每步有界地改变策略，限制本地KL分歧。我们提出了结合资格追踪和对角线缩放的实用算法。从经验上看，这些方法可以产生最先进的流媒体性能，其性能通常与批处理和回放缓冲区方法相当。

[阅读原文](https://arxiv.org/abs/2604.19033)

---

## 30. 通过辩证对齐驯服主体中的行为者-观察者不对称

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Bobo Li, Rui Wu, Zibo Ji, Meishan Zhang, Hao Fei, Min Zhang, Mong-Li Lee, Wynne Hsu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces dialectical alignment via Group Relative Policy Optimization to mitigate cognitive bias in multi-agent self-reflection, directly relevant to RL for LLMs and self-improving agents.

**摘要**: arXiv：2604.19548v1宣布类型：新摘要：大型语言模型代理已从静态文本生成器迅速发展为能够执行复杂自主工作流程的动态系统。为了提高可靠性，越来越多地采用分配专门角色的多代理框架来实现自我反思和相互审计。虽然这种角色扮演有效地利用了领域专家知识，但我们发现它同时会引发一种类似人类的认知偏见，称为演员-观察者不对称（AOA）。具体来说，作为行动者的代理人（在自我反思期间）倾向于将失败归因于外部因素，而观察者（在相互审计期间）将相同的错误归因于内部故障。我们使用新的模糊失败基准来量化这一点，该基准显示，对于大多数模型来说，简单地交换视角就会在超过20%的情况下触发AOA效应。为了遏制这种偏见，我们引入了Reitas（通过论点-对立-综合推理），这是一种通过辩证对齐训练的模型，以强制透视不变推理。通过将辩证思维链与集团相对政策优化相结合，Reitas引导代理将相互冲突的观点综合为客观共识。实验表明，Re塔斯有效地缓解了归因不一致性，并显着提高了模糊场景下的故障解决率。

[阅读原文](https://arxiv.org/abs/2604.19548)

---

## 31. 推理结构对于推理模型的安全对齐很重要

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yeonjun In, Wonjoong Kim, Sangwu Park, Chanyoung Park

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a post-training method (AltTrain) that alters the reasoning structure of Large Reasoning Models for safety alignment, using only SFT.

**摘要**: arXiv：2604.18946v1宣布类型：新摘要：大型推理模型（LRM）在复杂推理任务上实现了出色的性能，但通常会对恶意用户查询生成有害响应。本文探讨了这些安全风险的根本原因，并表明问题在于推理结构本身。基于这一见解，我们声称可以通过改变推理结构来实现有效的安全一致。我们提出AltTrain，这是一种简单而有效的后训练方法，可以显式地改变LRM的推理结构。AltTrain既实用又可推广，不需要复杂的强化学习（RL）训练或奖励设计，仅需要具有轻量级1 K训练示例的监督微调（SFT）。跨LRM主干和模型大小的实验证明了强大的安全一致性，以及跨推理、QA、总结和多语言设置的稳健概括。

[阅读原文](https://arxiv.org/abs/2604.18946)

---

## 32. 大型语言模型中口头语的兴起：跨前沿模型的系统分析

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Shuai Wu, Xue Li, Yanna Feng, Yufang Li, Zhijun Wang, Ran Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Systematically analyzes the side-effects of RLHF/alignment training on LLM outputs, directly relevant to understanding and improving RL-based alignment methods.

**摘要**: arXiv：2604.19139v1宣布类型：新摘要：随着大型语言模型（LLM）通过人类反馈强化学习（RLHF）和宪政人工智能等对齐技术不断发展，一种日益增长且日益明显的现象出现了：言语抽搐的激增--弥漫在模型输出中的重复、公式化语言模式。这些包括谄媚的开场白（“这是一个很好的问题！”、“太棒了！”）到伪同理心的肯定（“我完全理解你的担忧”、“我就在这里抓你”）和过度使用的词汇（“深入研究”、“挂毯”、“细致入微”）。本文对八种最先进的LLM的言语抽动现象进行了系统分析：GPT-5.4、Claude Opus 4.7、Gemini 3.1 Pro、Grok 4.2、Doubao-Seed-2.0-pro、Kimi K2.5、DeepSeek V3.2和MiMo-V2-Pro。利用自定义评估框架进行基于API的标准化评估，我们评估了10个英语和中文任务类别的10，000个提示，产生160，000个模型响应。我们引入了言语抽动指数（VTI），这是一种量化抽动患病率的复合指标，并分析了其与谄媚、词汇多样性和人类感知的自然性的相关性。我们的研究结果揭示了显着的型号间差异：Gemini 3.1 Pro表现出最高的VTI（0.590），而DeepSeek V3.2达到最低的VTI（0.295）。我们进一步证明，口头抽搐积累多轮对话，在主观任务中被放大，并显示出不同的跨语言模式。人类评估（N = 120）证实了奉承和感知自然之间的强负相关关系（r =-0.87，p < 0.001）。这些结果强调了当前训练范式的“对齐税”，并强调了对更真实的人类-人工智能交互框架的迫切需求。

[阅读原文](https://arxiv.org/abs/2604.19139)

---

## 33. 答案令牌如何读取推理痕迹？定量推理思维LLM中的自读模式

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Haoyang Chen, Yi Liu, Jianzhi Shao, Tao Zhang, Chengfu Huo, Wei Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes and steers the internal attention patterns of answer tokens to reasoning traces, a form of latent reasoning process control.

**摘要**: arXiv：2604.19149v1宣布类型：新摘要：思考LLM在回答之前产生推理痕迹。之前的激活转向工作主要针对塑造这些痕迹。人们仍然不太了解答案令牌实际上如何读取和整合推理以产生可靠的结果。我们专注于定量推理，分析了对推理的回答注意力，并观察到与正确性一致的良性自读模式，其特征是阅读焦点沿着推理轨迹向前漂移和持续集中在关键语义锚上，而不正确的解决方案则表现出分散和不规则的注意力模式。我们将其解释为答案解码期间的内部确定性，其中模型致力于可行的解决方案分支并集成关键证据。随后，我们提出了一种由自读质量（SRQ）分数驱动的免训练引导方法，将流程控制的几何指标与内容监控的语义指标相结合。SRQ选择数据来构建引导载体，引导推理走向良性自读，远离不确定和无序的阅读。实验表明，我们的方法可以产生一致的准确性收益。

[阅读原文](https://arxiv.org/abs/2604.19149)

---

## 34. HP-Edit：用于图像编辑的人性偏好训练后框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Fan Li, Chonghuinan Wang, Lina Lei, Yuping Qiu, Jiaqi Xu, Jiaxiu Jiang, Xinran Qin, Zhikai Chen, Fenglong Song, Zhixin Wang, Renjing Pei, Wangmeng Zuo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes HP-Edit, a post-training framework using RLHF with an automated human-preference-aligned reward scorer for diffusion-based image editing.

**摘要**: arXiv：2604.19406v1宣布类型：新摘要：常见的图像编辑任务通常采用强大的生成扩散模型作为现实世界内容编辑的主要范式。与此同时，尽管扩散-DPO和Flow-GRPO等强化学习（RL）方法进一步提高了生成质量，但由于缺乏可扩展的人类偏好数据集和适合多样化编辑需求的框架，有效地将人类反馈强化学习（RL HF）应用于基于扩散的编辑在很大程度上仍未探索。为了填补这一空白，我们提出了HP-Edit，这是一个用于人类偏好一致编辑的后训练框架，并引入了RealPref-50 K，这是一个跨越八个常见任务并平衡常见对象编辑的现实世界数据集。具体来说，HP-Edit利用少量人类偏好评分数据和预先训练的视觉大语言模型（VLM）来开发HP-Scorer--一个自动的、人类偏好对齐的评估器。然后，我们使用HP-Scorer来有效地构建可扩展的偏好数据集，并充当编辑模型后训练的奖励函数。我们还引入RealPref-Bench，这是评估现实世界编辑性能的基准。大量实验表明，我们的方法显着增强了Qwen-Image-Edit-2509等模型，使其输出与人类偏好更紧密地保持一致。

[阅读原文](https://arxiv.org/abs/2604.19406)

---

## 35. 从经验到技能：通过可重用策略学习进行多智能体生成引擎优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Beining Wu, Fuyou Mao, Jiong Lin, Cheng Yang, Jiaxuan Lu, Yifu Guo, Siyu Zhang, Yifan Wu, Ying Huang, Fu Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-agent framework for Generative Engine Optimization that distills validated editing patterns into reusable, engine-specific optimization skills, enabling strategy learning and transfer.

**摘要**: arXiv：2604.19516v1宣布类型：新摘要：生成引擎（GE）正在通过用基于引用的答案取代排名链接来重塑信息访问，但当前的生成引擎优化（GEO）方法孤立地优化每个实例，无法跨任务和引擎积累或转移有效的策略。我们将GEO重新定义为一个策略学习问题，并提出MAGEO，这是一个多智能体框架，其中协调的规划、编辑和一致性感知评估作为执行层，而经过验证的编辑模式逐渐提炼成可重复使用的、特定于发动机的优化技能。为了实现受控评估，我们引入了一个双分支评估协议，用于内容编辑的因果归因和DSV-CF，这是一个将语义可见性与归因准确性统一起来的双轴指标。我们进一步发布了MSME-GEO-Bench，这是一个基于真实查询的多场景、多引擎基准测试。在三个主流引擎上的实验表明，MAGEO在可见性和引用保真度方面都大大优于启发式基线，消融证实了引擎特定的偏好建模和策略重用是这些收益的核心，这表明了可扩展的学习驱动范式值得信赖的GEO。代码可访问https://github.com/Wu-beining/MAGEO

[阅读原文](https://arxiv.org/abs/2604.19516)

---

