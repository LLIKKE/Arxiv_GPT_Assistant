# 💡 今日研究速览 (Daily Summary)

# SFT &数据固化
监督微调的前景正在超越静态数据集。一个关键的趋势是出现了像DRIFT这样的政策数据归因方法，它利用影响函数和模型自身的推出来细化训练数据，将数据管理从一次性的预处理步骤转移到迭代的模型感知过程。这直接解决了静态SFT数据与推理期间模型的动态分布之间的不匹配。

# LLC（GRPO和推理）的RL
强化学习，特别是基于GRPO的方法，正在经历深刻的成熟，从简单的奖励工程转向复杂的结构和算法创新。正如STARE所强调的那样，该领域现在正在努力解决基本不稳定性，该领域通过迷宫引导的代币级重新加权来稳定政策熵，以及对SFT过度训练导致的信息量崩溃和排名倒置的分析工作。一个重大突破是转向信用分配和轨迹构建：SC-GRPO使用政策上KL分歧来进行自我调节信用，而TAPT则根据模型自身的错误构建微观反射轨迹以进行自我提炼。此外，GraphPO在展开上引入了DAB结构，以合并语义等效的推理路径，从而显着减少方差。这一点得到了LLMZero等自动化发现系统的补充，该系统使用LLM代理来寻找自适应的多阶段RL策略，揭示参数动态的结构原则。以数据为中心的长上下文RL食谱和通过模型合并（稀疏诅咒）分析WLVR参数空间几何形状，其实际影响显而易见，它们共同为从业者提供了可操作的诊断和培训食谱。

# 多模式和视觉语言模型
多模式研究越来越关注于将感知与推理脱钩，以构建更稳健和透明的系统。一个主要问题是防止捷径学习，正如ViGOS所解决的那样，它通过将视觉证据收集与推理分开，在视觉上建立了政策自我升华的基础。这还得到了在推理前预对齐视觉证据的敏捷驱动RL（请参阅，稍后回答）和双路径空间推理框架（加强双路径推理）的补充，该框架通过单独的奖励优化不同的推理模式。对于音频来说，连续音频思维（CoAT）的引入标志着将潜在推理应用于音频模式的重要一步，而MaineCoon则使用强化的在线政策提炼，通过实时视听社交世界模型突破了边界。

# 代理和工具使用
代理领域正在从静态数据生成转向动态、奖励驱动的自我改进循环。RODS通过使用推出奖励方差作为零成本信号来检测分布变化并实时合成多回合工具使用代理的信息训练数据来体现了这一点。对于图形用户界面代理，SGCD引入了一个迭代的策略上框架，该框架为偏离轨迹状态生成监督，从而有效地弥合代理当前策略和训练数据之间的差距。这些方法超越了模仿学习，转向持续的自我纠正适应。

# 一致和奖励建模
一致性研究正在朝着更细致、更可控的奖励信号方向发展。SCPO通过将加权方法纳入奖励模型训练中来解决偏好文化多样性的关键问题，超越了单一的人类反馈。作为补充，Self-CTRL框架训练LLM通过RL产生行为一致的自我解释，直接提高透明度。对于专业领域，蛋白质语言模型的无监督奖励优化（SRO/BRO）表明，内在的不确定性和语义一致性可以作为有效的奖励信号，扩展RLHF风格的目标超越人类注释的适用性。

# Latent Reasoning & Test-Time Scaling
一种新的架构正在出现，它在潜在或连续空间中执行推理，绕过自回归瓶颈。DreamReasoner-8B通过扩散推理模型的块大小课程学习推进了这一点，通过并行块式去噪实现长思想链。REVES框架引入了一种补充的测试时间扩展方法，通过将险些错过的中间步骤转换为脱钩的修订和验证提示，从而实现高效的非策略数据生成，以进行多步骤推理。与此同时，受约束的自我蒸馏提供了一种中间立场，在推理轨迹上提供细粒度、代币级别的指导，而不需要潜在空间。

---

## 1. 从自己的错误中学习：构建可学习的微反射轨迹进行自我蒸馏

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhilin Huang, Hang Gao, Ziqiang Dong, Yuan Chen, Yifeng Luo, Chujun Qin, Jingyi Wang, Yang Yang, Guanjun Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TAPO, a novel on-policy self-distillation method that constructs micro-reflective trajectories from the model's own correct/incorrect rollouts, advancing self-distillation from implicit alignment to explicit trajectory construction with contrastive corrections.

**摘要**: arXiv：2606.18844v1宣布类型：新摘要：自我提炼通过使用模型自己的展开作为训练信号来改进大型语言模型中的推理，通常通过隐式逻辑级对齐来最大限度地减少KL向特权目标分布的偏差。然而，由于这种监督是通过不受控抽样产生的，因此它不提供对模型特定错误的诊断见解或对其个体故障模式的纠正指导。因此，该模型学会模仿特权分布，而不是接受细粒度的纠正，以确定其推理失败的地方和原因。在本文中，我们提出了轨迹增强政策优化（TAPT），将自我升华从隐性分布对齐推进到显式轨迹构建。在RL训练期间，模型对同一查询产生正确和不正确的展开，TAPT利用这种对比结构来构建微反射纠正，新的训练轨迹，将模型的错误推理保留到失败点，然后插入自然语言诊断和纠正推理由来自同一抽样组的正确引用指导。由于每个轨迹都锚定在学习者自己的前置和解决方案中，因此与基于KL的方法强加的位置对齐相比，纠正信号在更大程度上保留了模型的政策上分布。为了集成这些轨迹，TAPT在模型的能力边界引入了困难感知的候选选择，并引入了脱钩的优势估计，以防止梯度污染。AIME 2024、AIME 2025和HMET 2025的实验表明，在相同数量的训练步骤下，TAPO比GRPO实现了一致的改进。进一步的分析表明，TAPO增强了首遍推理和错误纠正的有效性。

[阅读原文](https://arxiv.org/abs/2606.18844)

---

## 2. 从自己的解决方案中学习：具有可验证奖励的强化学习的自我条件学分分配

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yingyu Shan, Yuhang Guo, Zihao Cheng, Zeming Liu, Xiangrong Zhu, Xinyi Wang, Jiashu Yao, Wei Lin, Hongru Wang, Heyan Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SC-GRPO, a self-conditioned credit assignment method for RLVR that uses on-policy KL divergence as a multiplicative weight on GRPO gradients, improving reasoning without external teachers.

**摘要**: arXiv：2606.18810v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）在训练LLM以执行推理任务方面取得了重大进展，但GRPO等代表性方法在所有代币之间分配了统一的信用，浪费了常规代币的梯度，同时低估了关键推理步骤的信用。现有的代币级信用分配方法需要模型自身推出之外的资源。GRPO变体依赖于流程奖励模型或地面真相答案。知识蒸馏通过每个代币的分歧来分配学分，但需要外部教师（按政策蒸馏）或特权信息（按政策自我蒸馏）。然而，这些依赖性限制了纯WLVR设置中的适用性。我们观察到，将模型条件化在其自己的已验证轨迹上会导致原始分布和条件分布之间可测量的每令牌KL偏差，并证明，当存在多个已验证轨迹时，从由已验证轨迹构建的自学中提取会导致不可行的加权平均解。我们提出了SC-GRPO（自条件GRPO），它使用前面提到的KL偏差作为GRPO梯度的乘性权重。在涵盖数学、代码和代理任务的五个基准测试中，SC-GRPO的表现始终优于GRPO的8.1%和DAPO的5.9%，OOD性能更强。此外，SC-GRPO实现了比OPD更高的性能。

[阅读原文](https://arxiv.org/abs/2606.18810)

---

## 3. STARE：惊喜引导的代币级优势重新加权以实现政策熵稳定性

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Haipeng Luo, Qingfeng Sun, Songli Wu, Can Xu, Wenfeng Deng, Han Hu, Yansong Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a surprisal-guided token-level advantage reweighting method to stabilize policy entropy in GRPO-based RL for LLMs, directly addressing a key training instability.

**摘要**: arXiv：2606.19236v1宣布类型：新摘要：像GRPO这样的具有可验证奖励的强化学习算法已成为LLM中复杂推理的主要训练后范式，但通常会在训练期间遭受政策信息量崩溃的影响。我们在GRPO下对代币级熵动态进行一阶梯度分析，并识别代币级信用分配不匹配：每个代币的熵变化分解为代币级优势和下一个代币分布上的熵敏感性函数的产物，产生代币-伪四象限结构和近临界性质。受此启发，我们提出了STARE（Surprisal-guided Token-level Advantage Reweighting for Policy Entropy稳定性），该方法通过批内部预设分位数来识别对entropy关键的代币子集，选择性地重新加权它们的有效优势，并结合目标-熵闭环门以实现稳定的熵调节。在从1.5B到32 B的模型规模和三个任务系列（短CoT、长CoT和多转弯工具使用）中，STARE在数千个步骤中维持稳定的RL训练，同时将政策信息量保持在目标范围内。在AIME 24和AIME 25上，STARE的平均准确性优于DAPO和其他竞争基准4%-8%，反射令牌和响应长度同步增长，表明持续的探索-利用平衡进一步释放RL训练潜力。代码可在https://github.com/hp-luo/STARE上获取。

[阅读原文](https://arxiv.org/abs/2606.19236)

---

## 4. LLMZero：通过LLM代理发现RL后培训的自适应培训策略

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haoyang Fang, Wei Zhu, Boran Han, Alex Zhang, Zhenyu Pan, Shuo Yang, Shuai Zhang, Jiading Gai, Peng Tang, Cuixiong Hu, Xuan Zhu, Huzefa Rangwala, George Karypis, Bernie Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LLMZero, an LLM-agent-driven tree search system that discovers adaptive multi-stage RL post-training strategies for GRPO tasks, revealing a structural principle for parameter dynamics.

**摘要**: arXiv：2606.18388v1宣布类型：新摘要：RL训练后策略依赖于厕所，并揭示了一种反复出现的经验模式：容量参数在各个阶段单调累积，而正规化参数主要响应于不断变化的训练动态而振荡。这种区别很重要，因为固定时间表将所有参数委托给固定轨迹，因此无法表达正规化必须跟踪的非平稳探索-利用权衡;该原则为多阶段训练提供了可操作的设计规则。我们通过LLMZero发现了这一点，这是一个LLM代理通过树搜索搜索训练轨迹、诊断每个检查点的病理并提出协调的多参数转换的系统。在4个不同的GRPO任务中，LLMZero发现的策略相对于基本模型提高了9%至140%，相对于网格搜索提高了6%至15%，始终优于随机搜索和基于技能的代理。结构原则在任务之间转移，解释了为什么发现的策略采取定性不同的形式，但具有相似的参数动态。

[阅读原文](https://arxiv.org/abs/2606.18388)

---

## 5. 大型音频语言模型的连续音频思维

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Gyojin Han, Dong-Jae Lee, Changho Choi, Jongsuk Kim, Junmo Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Continuous Audio Thinking (CoAT), a latent reasoning framework for audio LALMs that uses a continuous thinking block and expert distillation, directly advancing latent reasoning.

**摘要**: arXiv：2606.18273v1宣布类型：新摘要：大型音频语言模型（LALM）在各种音频理解任务（从语音转录到音乐分析）方面表现出了令人印象深刻的能力。然而，由于LALM通常被训练为产生文本对齐的响应，因此它们的隐藏状态是为了文本生成而逐渐塑造的，而不是为了保存声学信息。因此，音频承载的多样化声学内容，例如语音细节、韵律、声音事件、情感和音调，会在过程中丢失，并且很难在响应中利用。我们引入了连续音频思维（CoAT），这是一个框架，为音频语言模型配备了连续的潜在工作空间，用于在响应生成之前组织声学信息，其基础是音频专家的提炼。在思维空间内，模型在生成响应时可以利用专家蒸馏提供的丰富声学信息。此外，提出的连续思维块可以在单个预填充中处理，因此CoAT不需要超过基线的额外自回归解码成本。在Qwen 2-Audio、Qwen2.5-Omni-7 B和Audio Flamingo~3这三种LALM上，跨越音频推理、音频理解、音乐分类、语音情感和语音转录的广泛基准套件的性能增益证明了CoAT的有效性。进一步的分析证实了辅助监督从思维位置传播到模型的文本反应。

[阅读原文](https://arxiv.org/abs/2606.18273)

---

## 6. MaineCoon：追求实时视听社交世界模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Lichen Bai, Tianhao Zhang, Shitong Shao, Dingwei Tan, Qiyu Zhong, Zhengpeng Xie, Haopeng Li, Qinghao Huang, Dandan Shen, Tengjiao Ji, Wei Wang, Peicheng Wu, Yuxuan Zhao, Xiangyu Zhu, Welly Luo, Shurui Yang, Zeke Xie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces reinforced online-policy distillation (ROPD) as a core training technique for a real-time audio-visual autoregressive model, directly matching the on-policy distillation criterion.

**摘要**: arXiv：2606.17800v1宣布类型：新摘要：随着越来越多的全球视频内容是在社交平台上消费的，用于互动社交目的，为社交世界构建的视频生成模型很重要，但在很大程度上被之前的研究忽视了。在这项工作中，我们定义了社交世界模型的位置，并构建了原型模型，作为实现这一目标的第一步。虽然以前的世界模型成功地模拟了物理环境或游戏世界探索，但它们从根本上脱离了以人为本的社会动态。为了弥合这一差距，作为社交世界模型的第一步，我们推出了MaineCoon，这是第一个实时视听自回归模型，具有22 B参数，能够实时流媒体生成和亚秒交互，在单个图形处理器上具有创纪录的帧率高达47.5 FPS。据我们所知，MaineCoon也是第一个专门针对社交互动应用程序优化的实时视听生成模型。为了实现高效、稳定的训练，我们在MaineCoon中引入了几种新颖技术，包括自重采样、跨模式表示对齐、领域感知偏好优化和强化在线策略蒸馏（ROPD）。我们还设计了第一个代理流推理框架，该框架支持千秒规模甚至更长的生成，同时通过代理缓存管理和即时规划来减轻漂移。这些创新显着加速了训练，同时优化了实时推理性能。我们相信，这项工作不仅为高质量、低延迟和长视野视听自回归模型设定了新的最先进（SOTA）性能基准，而且指出了下一代人工智能原生社交平台所需的范式转变。

[阅读原文](https://arxiv.org/abs/2606.17800)

---

## 7. Self-ALT：通过强化学习进行自我一致性训练

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Itamar Pres, Laura Ruis, Melat Ghebreselassie, Belinda Z. Li, Jacob Andreas

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Self-CTRL, a reinforcement learning method for training LLMs to produce self-explanations consistent with their behavior, directly improving transparency and alignment.

**摘要**: arXiv：2606.18327v1宣布类型：新摘要：忠实描述自己行为的语言模型（LM）可以更容易地被用户审核、理解和信任。本文描述了使用强化学习（Self-ALT）的自我一致性训练，这是一种通过更新解释以更好地预测行为或更新行为以更好地匹配解释来优化LM的自我解释与相关输入行为之间的一致性的方法。我们将我们的方法应用于两个领域。首先，我们研究一项正式的概率推理任务，其中LM必须学会模仿一系列有偏见的采样者，并评估他们报告相关偏见的能力。我们发现，一致性训练改善了自我报告和行为测量的潜在偏差之间的相关性，在一组固定分布上从$R#2 =0.24$提高到$R#2 =0.64$，与直接地面真相监督的一般化相匹配。其次，我们研究了宪法人工智能领域，其中LM必须描述何时拒绝或遵守用户请求。在这里，Self-ALT生成忠实描述模型对发出请求的行为的规则，将第三方审计师模型的拒绝预测从36美元提高到92美元。在另一个方向上，行为更新改善了一致性，将HarmBench失败率从15.0美元降低到0.5美元，而不会大幅增加无害提示的拒绝。通过协调解释和行为，我们的工作提供了训练人工智能模型更安全、更透明和更可控的通用配方。

[阅读原文](https://arxiv.org/abs/2606.18327)

---

## 8. 先看后看：将感知和推理脱钩，实现捷径弹性多模式政策上的自我蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sihan Wang, Xiyao Liu, Lianqing Liu, Zhi Han

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ViGOS, a visually grounded on-policy self-distillation framework for MLLMs that decouples perception and reasoning to prevent shortcut learning, with a novel teacher structure.

**摘要**: arXiv：2606.19120v1宣布类型：新摘要：政策上的自我蒸馏（OPSD）在其自己的推出中训练模型，并使用冷冻副本来提供以参考目标为条件的密集代币级目标。这对于LLM推理来说效果很好，但对多模式大型语言模型（MLLM）的直接扩展可以创建一个捷径：特权目标可能主要基于文本引用目标而不是图像来引导标记。我们提出ViGOS，这是一个基于视觉的OPSD框架，用于MLLM后培训。学生首先写一个视觉描述，然后推理得出最终答案。对于有效的展开，纯图像感知教师负责监督描述，而特权推理教师负责监督相同学生后缀的推理和最终答案。参考教师仅用于无效的卷展以恢复输出格式。在一般视觉语言、专家推理、视觉数学、空间基础和视觉语言优先基准方面，ViGOS保留了OPSD的主要优势，并改善了容易走捷径的环境中基于图像的行为。

[阅读原文](https://arxiv.org/abs/2606.19120)

---

## 9. GraphPO：推理模型的基于图的策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yuliang Zhan, Xinyu Tang, Jian Li, Dandan Zheng, Weilong Chai, Jingdong Chen, Jun Zhou, Ge Wu, Wenyue Tang, Hao Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GraphPO, a novel RL framework for reasoning models that uses a DAG over rollouts to merge semantically equivalent paths, reducing variance and improving exploration efficiency.

**摘要**: arXiv：2606.18954v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）已成为增强大型推理模型能力的标准范式。WLVR通常独立采样响应，并使用最终答案优化策略。该范式有两个局限性。首先，独立响应通常包含类似的中间推理步骤，导致冗余探索和浪费计算。其次，最终答案奖励稀疏使得很难识别有用的步骤。基于树的方法通过共享前置码和比较同一前置码的分支以提供细粒度的信号来部分解决这个问题。不过，树枝仍然独立扩张。当不同的分支达到相似的推理状态时，它们无法共享信息并重复类似的探索。此外，基于树的方法忽略了这种离散度，只在不同的分支内执行局部比较，这可能会导致优势估计的方差更高。为了应对这一挑战，我们提出了GraphPO（基于图的策略优化），这是一种新型RL框架，它将展开表示为有向非环图，推理步骤为边，从推理路径总结的语义状态为节点。GraphPO将语义等效的推理路径合并到等效类中，允许它们共享后缀并将预算从冗余扩展重新分配到多样化的探索。此外，我们将效率优势分配给输入边，将正确性优势分配给输出边，从而提高推理效率，同时从结果中获得流程监督。理论表明，GraphPO减少了队列估计方差并提高了推理效率。在推理和代理搜索基准上对三个LLM进行的实验表明，在相同的代币预算或响应预算下，GraphPO始终优于基于链和树的基线。

[阅读原文](https://arxiv.org/abs/2606.18954)

---

## 10. DRIFT：通过策略数据属性细化指令数据

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zefan Wang, Lincheng Li, Tianyu Yu, Yuan Yao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DRIFT, an on-policy data attribution method using influence functions with debiasing for refining SFT data, directly improving LLM capability via on-policy rollouts.

**摘要**: arXiv：2606.18307v1宣布类型：新摘要：优化监督微调（SFT）的训练数据分布决定了大型语言模型（LLM）的能力。虽然现有的数据策展方法擅长在有限的预算下加速培训，但它们不太适合提高能力上限。这里的挑战不再是确定一个保持性能的较小子集，而是将数据分布细化到最有能力改进最终模型的实例。为了解决这个问题，我们使用影响函数（IF）探索实例级数据属性。我们确定，标准的IF配方的斗争，在这种情况下，由于两个结构性的限制：一个接近的差距所造成的政策验证目标，和严重的偏见梯度规范。DRIFT（Data Refinement via On-Policy Influence Functions for Supervised Fine-Tuning）。DRFT没有依赖外部参考数据，而是利用模型的政策推出作为验证目标，从经验上最大限度地减少了参数邻近度差距，并更好地与IF的本地邻居假设保持一致。它进一步应用基于轨迹正确性的签名加权，并针对梯度黑客问题的去偏置影响分数，允许一小组验证查询充当归因完整数据集的可靠锚点。对7 B参数指令和推理模型的实验表明，DRFT持续提高了两者的性能上限，超过了现有的数据策展基线。

[阅读原文](https://arxiv.org/abs/2606.18307)

---

## 11. DreamReasoner-8B：扩散推理模型的块规模课程学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zirui Wu, Lin Zheng, Jiacheng Ye, Shansan Gong, Xueliang Zhao, Yansong Feng, Wei Bi, Lingpeng Kong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes block-size curriculum learning for diffusion reasoning models, enabling strong long-CoT reasoning with parallel block-wise denoising, directly advancing latent reasoning architectures.

**摘要**: arXiv：2606.19257v1宣布类型：新摘要：块扩散语言模型通过并行块式去噪来加速解码，但它们是否可以可靠地扩展以进行长思想链（CoT）推理仍有待解决。为此，我们开发了开源块扩散推理模型DreamReasoner-8B，并对训练和推理块大小如何影响长CoT推理进行了系统研究。我们的分析揭示了明显的性能差异：用大块大小进行训练会产生非常差的推理，而小块大小可以保持有效的推理。为了弥合这种粒度差距，我们提出了块大小的课程学习，将训练从细粒度的块大小逐渐过渡到粗粒度的块大小，从而克服了这一限制，并实现了在不同推理块大小上推广的强大推理性能。在数学和代码推理基准方面，DreamReasoner-8B实现了与Qwen 3 -8B等领先的开放自回归模型具有竞争力的结果。这项工作为高效、具有推理能力的扩散语言模型奠定了实践基础。我们在https://github.com/DreamLM/DreamReasoner上发布了我们的模型。

[阅读原文](https://arxiv.org/abs/2606.19257)

---

## 12. 超越奖励工程：长上下文强化学习的数据食谱

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xiaoyue Xu, Sikui Zhang, Xiaorong Wang, Xu Han, Chaojun Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a data-centric recipe for long-context RL with GRPO, showing strong gains on reasoning and agentic tasks, directly advancing RL-for-LLMs.

**摘要**: arXiv：2606.18831v1宣布类型：新摘要：长上下文推理是大型语言模型的一项基本能力，特别是当它们被部署为必须对冗长轨迹进行推理的自主代理时。强化学习（RL）最近已成为提高这种能力的主要范式，但现有工作主要集中在奖励工程上，而多样化的训练数据仍然稀缺。我们从以数据为中心的角度重新审视这个问题，并表明，单独使用简单而有效的数据配方，再加上最低限度的基于结果的GRPO设置，就足以大幅改善长上下文推理。我们的食谱针对三个补充的任务系列--检索、多证据合成和推理--为此，我们构建和策划了总共约14 K个示例的八个数据集。对三个模型（Qwen 3 - 4 B/8B/30 B-A3 B）进行的实验在七个长上下文基准上获得了+7.2/+3.2/+6.4分的平均收益，超过了之前的RL训练集。我们进一步证明，这些收益可以转移到代理任务，其中使用我们的数据配方在代理调整模型上继续RL训练可以使GAIA提高+4.8分，BrowseComp提高+7.0分。我们将发布我们的数据集以促进未来的研究。

[阅读原文](https://arxiv.org/abs/2606.18831)

---

## 13. 稀疏诅咒：从模型合并中理解WLVR模型参数空间

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Chenrui Wu, Zexi Li, Jiajun Bu, Jiangchuan Liu, Haishuai Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes the geometry of RLVR parameter updates and proposes a novel merging method (SAR-Merging) tailored for RL-trained LLMs, directly addressing a key challenge in RL for LLMs.

**摘要**: arXiv：2606.18521v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）已成为一种强大的训练后范式，在激发推理智能和抵抗灾难性遗忘方面超越了监督微调（SFT）。最近的研究进一步表明，与SFT相比，WLVR会引发高度稀疏和非主要参数更新。这自然会引发一个问题：这种稀疏性是否会使WLVR模型更适合模型合并？如果是这样，模型合并将提供一种可扩展的、免训练的路径来聚合来自独立训练的WLVR模型的多样化推理能力。令人惊讶的是，我们发现了相反的情况，发现了稀疏性诅咒：稀疏的WLVR更新在参数空间中分散得更远，形成了近垂直的捷径，使聚合本质上脆弱。这可能源于RL优化的随机性和紧急推理模式的多样性。与SFT模型收敛到共享的平坦盆地并自然合并不同，RLVR模型在标准合并方法下遭受严重退化。通过系统的经验分析的更新几何，我们表征这种失败背后的机制，并提出灵敏度感知的解决合并（SAR合并），合并配方为RLVR参数空间的独特结构量身定制。SAR合并通过基于Fisher信息的敏感性仲裁解决重叠更新区域中的冲突，然后进行幅度感知稀疏化和重新缩放以保留脆弱的推理路径。数学和编码基准的实验表明，SAR合并大大优于现有的合并方法RLVR模型，使单任务增强和多功能融合。

[阅读原文](https://arxiv.org/abs/2606.18521)

---

## 14. RLVR下SFT过度训练通过熵崩溃预测排名倒置

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Siddharth Aphale, Kelly Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Analyzes SFT overtraining causing entropy collapse and rank inversion in RLVR (GRPO) for LLMs, providing a diagnostic for RL training failure.

**摘要**: arXiv：2606.18487v1宣布类型：新摘要：当SFT压缩卷展分布时，为GRPO选择最高通过@1的SFT检查点的标准启发式可能会失败。对于二元奖励，预期的组内优势方差为$p（1{-}p）（g{-}1）/g$;当早期GRPO将$p$推至$p以下时，大多数组都有相同的奖励并且不提供组相对信号。我们研究Qwen 2.5-Coder-3B和DeepSeek-Coder-6.7B的SFT深度阶梯。我们在五个深度和三个种子中测试Qwen 2.5-Coder-3B，并在四个匹配深度和三个种子中测试DeepSeek-Coder-6.7B。在Qwen上，RL前传递@1随着SFT深度而增加，但峰值GRPO传递@10从$0.806$下降到$0.481$（3种子平均值，$n{=}20$）; RL前的信息量与GRPO结果正相关（$\rho{=}{+}0.69$）。在DeepSeek上，pass@1仍然远高于$p^*（8）{=}0.083$，并且GRPO结果压缩而不是倒置。两阶段诊断将RL前的信息分类与早期GRPO信息监测相结合，标记高风险检查点，并可以尽早停止失败的运行。简单的KL来引用正规化和标签平滑变体并不能拯救我们设置中崩溃的Qwen检查点，这表明失败不是一个微不足道的GRPO超参数伪影。

[阅读原文](https://arxiv.org/abs/2606.18487)

---

## 15. PragReST：语用语言理解中的自我强化反事实推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jihyung Park, Minchao Huang, Leqi Liu, Elias Stengel-Eskin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-supervised framework combining counterfactual reasoning trace generation with RL (via GRPO) to improve LLM pragmatic reasoning, directly matching RL-for-LLMs and on-policy distillation criteria.

**摘要**: arXiv：2606.18624v1宣布类型：新摘要：自然语言的理解通常取决于隐含的意义而不是明确陈述的意义，需要务实推理。尽管在数学和逻辑推理方面表现出色，但大型语言模型（LLM）仍然难以做出务实推理，通常选择字面解释。为了改进LLM务实推理，我们引入了PragReST，这是一个自监督框架，它构建务实QA数据，生成反事实推理痕迹，并训练模型通过监督式微调和强化学习将其内化，而无需人工标记的训练数据或从更强的老师那里提炼。在四个务实基准（PragMega、Ludwig、MetoQA和AltPrag）中，PragReST比主干模型、特定于任务的务实调优基线和同一管道的非反事实变体进行了改进。在基于准确性的基准测试中，对于Qwen 3 -8B和Qwen 3 - 14 B，PragReST分别比指令主干提高了5.37%和5.50%（绝对）。我们的错误分析和消除强调了反事实推理的重要性：PragReST主要减少了由于未能将观察到的话语与合理的替代方案进行比较而引起的错误，而删除反事实推理则会大幅降低性能。此外，我们的训练还保留了一般知识和数学推理基准的域外性能。

[阅读原文](https://arxiv.org/abs/2606.18624)

---

## 16. 先看，后回答：通过充分性驱动RL进行视觉证据预对齐

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yilian Liu, Sicong Leng, Guoshun Nan, Junyi Zhu, Jiayu Huang, Minghao Sun, Xuancheng Zhu, Yisong Chen, Zexian Wei, Xiaofeng Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a sufficiency-driven RL objective (GRPO) for visual evidence pre-alignment in MLLMs, directly contributing a new reward design and RL training recipe for LLM behavior improvement.

**摘要**: arXiv：2606.17678v1宣布类型：新摘要：多模式大型语言模型（MLLM）将强大的文本推理与视觉输入集成在一起，但它们的响应可能与底层图像不一致，这表明推理过程中视觉证据的利用效率低下。流行的训练范式依赖于大规模基于字幕的预训练来进行一般对齐，然后是有监督的微调和强化学习，以实现指令遵循和复杂推理。然而，这种预训练只提供了薄弱的视觉基础：简短、粗略的字幕使模型偏向突出的对象，而忽略了细粒度的视觉证据。在本文中，我们介绍了视觉证据预对齐（VEPA），这是训练前和训练后之间的中间阶段，通过群体相对政策优化（GRPO）探索一种新型的视觉驱动目标，以优化受问题影响的视觉证据描述。跨不同基准的广泛实验表明，我们的VEPA持续提高了视觉要求高的评估的性能，并补充了标准的监督后培训。进一步的分析表明，收入来自强化的、可转移的视觉基础，而不是来自额外的特定任务培训。

[阅读原文](https://arxiv.org/abs/2606.17678)

---

## 17. 成为你自己的老师：通过无监督奖励优化引导蛋白质语言模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lanqing Li, Shentong Mo, Yang Yu, Pheng-Ann Heng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes unsupervised reward optimization (SRO/BRO) for protein language models, combining intrinsic uncertainty and semantic consistency rewards with an RLHF-style objective, directly matching RL-for-LLMs criteria.

**摘要**: arXiv：2606.18961v1宣布类型：新摘要：蛋白质语言模型（PLM）已成为可控生物分子设计的强大工具，但它们的训练后适应通常依赖于昂贵的湿实验室验证或精心策划的偏好数据集。为了克服这个监督瓶颈，我们引入了PLM的无监督奖励优化，这是一个用于可操纵蛋白质生成的全面框架，无需地面真相标签。我们的主要见解是，任务不可知奖励将内在模型不确定性与蛋白质表示模型所告知的外在语义一致性结合起来，与基础模型和温度制度的可控性指标表现出强相关性。在这一发现的基础上，我们提出了两种离线算法：软奖励优化（SRO）和二进制奖励优化（BRO），它们有效地最大化了这些代理奖励引发的经典WLHF目标。对成分超出分布提示的广泛实验表明，这两种方法的表现都显着优于竞争基线（DPO、KTO），同时在多种采样温度、模型规模和蛋白质家族中接近Oracle性能。此外，在Pass@k评估中，与基本模型相比，在无监督奖励进行微调的PLM可以实现持续更高的覆盖率。通过通过自己产生的经验实现PLM的自我改进，我们的框架为标记偏好或实验反馈稀缺或不可用的环境中的可控生物分子设计提供了可扩展的途径。

[阅读原文](https://arxiv.org/abs/2606.18961)

---

## 18. GUI代理的技能引导连续蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhimin Fan, Hongwei Yu, Yeqing Shen, Haolong Yan, Guozhen Peng, Tianhao Peng, Yudong Zhang, Xiaowen Zhang, Kaijun Tan, Zheng Ge, Xiangyu Zhang, Daxin Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Skill-Guided Continuation Distillation (SGCD), an iterative on-policy self-improvement framework for GUI agents that generates supervision for off-trajectory states.

**摘要**: arXiv：2606.18890v1宣布类型：新摘要：改进图形用户界面代理通常依赖于专家轨迹上的行为克隆。然而，由于当前政策偏离专家政策，在闭环执行期间不可避免地会遇到政策引发的偏离轨迹状态，即不属于专家轨迹的状态。由于专家轨迹没有为这些看不见的状态提供任何证明，因此这些状态得不到有效的监督，从而导致政策无法选择正确的行动。为了缩小这一监督差距，我们提出了技能引导连续蒸馏（SGCD），这是一种迭代的自我改进框架。SGCD首先在没有技能指导的情况下执行简单的政策，通过几个步骤达到现实的偏离轨道状态。然后，技能引导的政策从这些状态完成任务并产生成功的延续，这些延续与专家轨迹相结合，为政策引发的偏离轨迹的状态提供监督。这些技能是从成功和失败的部署中提取的，包括继续计划、关键目标、失败陷阱和成功标准。在OSWorld-Verified上，SGCD将三个基本模型的成功率从30%左右提高到50%以上，证明了SGCD的有效性和通用性。

[阅读原文](https://arxiv.org/abs/2606.18890)

---

## 19. 奖励模型的可操纵文化偏好优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Minsik Oh, Advit Deepak, Sophie Wu, Douwe Kiela, Ekaterina Shutova

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SCPO, a novel reward model training algorithm that incorporates diverse cultural preferences via a weighting method, directly advancing RL for LLM alignment.

**摘要**: arXiv：2606.18606v1宣布类型：新摘要：大型语言模型（LLM）技术以每个社区可接受的方式服务于许多不同的文化子社区至关重要。然而，到目前为止，关于LLM对齐的研究主要集中在预测某些地区注释者的统一响应偏好。本文旨在推进具有更全球视野的对齐模型的开发，这些模型能够准确地代表子社区的偏好，并且不会对其中任何一个群体表现出过度的偏见。我们专注于为此目的开发奖励模型，并提出了一种新型的奖励模型训练算法（SCPO），该算法可以以平衡的方式整合不同的文化偏好。我们的方法导致少数群体奖励模型在PRISM和GlobalOpinionQA两个数据集以及7个国家/地区的性能比基线模型提高了7个百分点。SCPO的训练数据效率比奖励模型的全数据微调高出280%。此外，我们通过单独评估子社区的偏好来进行偏见分析，并表明过度偏见通过我们的加权方法得到了缓解。我们的代码可在https://github.com/minsik-ai/Steerable-Cultural-Preference上获取

[阅读原文](https://arxiv.org/abs/2606.18606)

---

## 20. 空间视觉语言模型中加强双路径推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yatai Ji, An-Chieh Cheng, Yang Fu, Yukang Chen, Han Zhang, Zhaojing Yang, Wei Huang, Ka Chun Cheung, Song Han, Vidya Nariyambut Murali, Pavlo Molchanov, Jan Kautz, Simon See, Hongxu Yin, Ping Luo, Sifei Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a dual-path spatial reasoning framework for VLMs that uses RL with accuracy and format rewards to optimize two reasoning paths, directly contributing to RL-for-LLMs.

**摘要**: arXiv：2606.17539v1宣布类型：新摘要：空间VLM在几何感知方面取得了重大进展，但需要对深度、距离和场景关系进行多步推理的复杂空间推理仍然具有挑战性。此外，不同的空间查询需要根本不同的策略：有些最好通过纯粹的语言、逐步推理来解决，而另一些则需要明确的3D基础，然后再进行定量推理。我们提出了通过空间VLM的强化学习的双路径空间推理（SR-REAL），这是一个统一的框架，为空间VLM配备了两个互补的推理路径：仅存储推理（LOR），它执行逐步的语言推理，和检测然后原因（DTR），它检测3D几何线索（例如，中心或边界框）。SR-REAL从冷启动监督微调阶段开始，该阶段构建LOR和DTR思想链监督并公开区域到3D接口，然后是RL，通过准确性和格式奖励优化策略模型;对于DTR，基于离散中心的检测奖励进一步细化几何对齐。在不同的空间基准中，SR-REAL显著优于空间VLM基线：（i）单个RL训练的模型支持两种推理路径，DTR通过精确的3D定位和LOR增强一般空间推理在区域感知任务中表现出色;（ii）联合训练两种路径促进相互加强;（iii）高质量的混合冷启动数据对于稳定的RL优化至关重要;以及（iv）该模型跨数据集和领域进行了推广，无需按任务进行调整，从而证明了TLR和DTR之间的正转移。

[阅读原文](https://arxiv.org/abs/2606.17539)

---

## 21. RODS：多车削刀具使用代理的奖励驱动在线数据合成

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ruishan Fang, Siyuan Lu, Chenyi Zhuang, Tao Lin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reward-driven online data synthesis loop for multi-turn tool-use RL that uses rollout reward variance as a zero-cost boundary detector to dynamically generate informative training samples.

**摘要**: arXiv：2606.19047v1宣布类型：新摘要：多回合工具使用RL因静态数据集中信息样本的快速耗尽而受到限制。我们观察到，GRPO中的梯度信号集中在具有最高部署奖励方差的任务上，这是Popoviciu上界的结果。因此，靠近代理能力边界的样本（成功和失败大致平衡）会产生不成比例的大政策梯度。随着训练的进行，这个边界不断移动，从而逐渐耗尽静态数据集中的信息样本池。我们提出RODS（奖励驱动的在线数据合成）来解决这种耗尽问题。RODS通过将进度奖励方差重新用作实用的零成本边界检测器，结束了RL训练和数据生成之间的循环，除了已经为训练计算的展开之外，不需要额外的推断。它不断识别此类边界样本，合成与其结构复杂性相匹配的新的多转弯变体（例如，API布局和依赖深度）通过与技能一致的重新分配管道，并管理与策略共同进化的动态重播缓冲区。RODS从400个人类种子开始，并维持约800个样本的主动训练池，实现了与17 K样本离线管道相当的性能，同时需要的轨迹减少大约20倍，并且比固定数据RL和我们受控环境中的环境增强有所改进。

[阅读原文](https://arxiv.org/abs/2606.19047)

---

## 22. REVES：重新视觉和虚拟化--测试时间缩放的增强培训

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuanxin Liu, Ruida Zhou, Xinyan Zhao, Amr Sharaf, Hongzhou Lin, Arijit Biswas, Mohammad Ghavamzadeh, Zhaoran Wang, Mingyi Hong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a two-stage iterative framework (REVES) that converts near-miss intermediate steps into decoupled revision and verification prompts for test-time scaling, enabling efficient off-policy data generation and improving multi-step reasoning.

**摘要**: arXiv：2606.18910v1宣布类型：新摘要：通过顺序修改的测试时扩展已成为增强大型语言模型（LLM）推理的强大范式。然而，标准的训练后方法主要优化单次目标，从而与多步推理动态产生根本性的不一致。虽然最近的工作将其视为多轮强化学习（RL），但传统方法直接在多步轨迹上进行优化，未能进一步利用模型可以通过纠正这些错误来学习的中间步骤中的高质量错误。我们提出了一个两阶段迭代框架，在在线数据/提示增强和政策优化之间交替。通过将成功恢复轨迹中的中间步骤（“险些失败”的答案）转换为脱钩的修订和验证提示，我们的方法将训练集中在有效的答案转换和错误识别上。与标准多圈RL相比，这种方法能够高效地生成非政策数据，并减少了长视野采样的计算负担。在LiveCodeBench上，使用公开可用的测试用例作为反馈，我们观察到比RL基线增加+6.5分，比标准多回合训练增加+4.0分。除了编码之外，我们的方法与之前报道的关于圆包装的SOTA结果相匹配，同时使用最小的基本模型（4 B）和比更大的进化搜索系统少得多的推出。地面真相验证下的数学结果进一步证实了改进的纠正能力。它还推广到非分布约束满足难题，例如n\_queens和mini\_数独，其中正确性完全由问题约束定义。代码可在https://github.com/yxliu02/REVES.git上获取。

[阅读原文](https://arxiv.org/abs/2606.18910)

---

## 23. 重新思考奖励监督：有条件的自我蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Siyi Gu, Jialin Chen, Sophia Zhou, Arman Cohan, Rex Ying

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes rubric-conditioned self-distillation, an on-policy distillation framework that uses fine-grained rubric feedback for token-level guidance over reasoning trajectories, surpassing GRPO and OPSD.

**摘要**: arXiv：2606.19327v1宣布类型：新摘要：推理语言模型的后训练通常由具有可验证奖励的监督蒸馏和强化学习驱动。蒸馏通常依赖于思想链注释，这些注释的获得成本高昂，并且本身可能是有噪音的、不完整的或部分不正确的;即使最终的解决方案是正确的，不完美的理由也可能会干扰学习。另一方面，具有经过验证的奖励的强化学习通常会将评估反馈压缩为纯量信号，从而模糊了应该改进响应的哪些方面。我们提出了\textBF{Rubric-Conditioned Self-Distillation}，这是一个将Rubric-Conditioned Self-Distillation纳入结构化的细粒度反馈的框架。我们的方法将教师模型置于标准级规则之上，并使用它来提供有关学生自己采样轨迹的代币级指导。这种设计避免了将单一参考原理视为唯一的监督目标。相反，标题指定了强响应应该满足的内容，从而在推理过程中实现比纯量奖励优化更细粒度的信用分配。我们用两阶段管道实例化这个框架，首先学习生成特定于任务的主题，然后训练主题引导的推理器。我们对一套不同的科学推理基准进行了评估，结果表明，受约束的自我蒸馏有效地将受约束的规则级标准转化为推理过程的代币级指导，平均超过GRPO 1.0分，平均超过OPSD 0.9分。

[阅读原文](https://arxiv.org/abs/2606.19327)

---

