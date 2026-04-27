# 💡 今日研究速览 (Daily Summary)

# LLM的RL
强化学习继续主导当今的研究，明显转向设计更复杂的奖励结构和训练动态，超越简单的基于结果的信号。一项关键发现警告说，仅靠结果奖励无法保证可验证或具有因果关系重要性的推理，因此提出了一种具有CIR和SR等新指标的联合奖励补救措施。这一见解实际上是通过新颖的奖励设计来解决的，例如针对搜索者的窗口部分AUR优化、针对多图像理解的基于规则的空间奖励以及针对图形用户界面代理的临时级奖励分配。几篇论文提出了新的RL训练方案--包括用于可控对话的DDPO（多轮GRPO变体）、用于生成性多模式嵌入的Refine-RL，以及用于突出证据的轻量级Actor框架--所有这些都表明RL正在成为LLM中对齐、推理和特定任务行为的通用优化器。

# 潜在推理和思想链效率
一个主要主题是通过超越冗长的思维链来提高推理效率。两篇论文独立提出了潜在推理的机制：抽象思维链使用策略迭代和RL来执行具有显着减少令牌的离散潜在推理，而VLM中的神经符号方法通过RL激励实现了75%的推理令牌减少。补充工作表明，LLM通常会提前决定答案，然后详细说明，建议提前停止是一种自然的效率黑客。还阐明了自我纠正的内部机制，揭示了二阶置信体系结构（PANI），该体系在没有外部反馈的情况下因果驱动错误检测。这些论文共同表明，该领域正在趋同于这样一个观点：显式、逐符号推理通常是多余的，并且通过RL训练的潜在或压缩推理路径可以保持或提高性能，同时效率要高得多。

# 代理与自我提升
对代理系统的研究正在朝着更有原则的、反馈驱动的架构迈进。自纠正循环的控制理论马尔科夫诊断提供了一个正式框架，用于理解自纠正何时以及为何起作用，并提出了反映RL式动态的“验证优先”干预措施。“不要模仿，Reinforce”论文用RL取代了监督模仿进行迭代分类，引入了具有基于价值的停止标准的循环代理--RL和代理决策之间的直接桥梁。对于图形用户界面代理，SOLAR-RL框架通过从稀疏轨迹信号追溯分配密集的阶梯级奖励来解决长期存在的信用分配问题。具有内存令牌和自适应计算时间的通用Transformer揭示了路由器初始化陷阱，这表明即使是自适应架构也需要仔细设计以进行迭代推理。这些作品共同指向学习分配计算、验证自己的输出并通过强化而不是静态模仿来改进的代理人。

# 多模式和专业应用程序
通过RL驱动的培训创新，多模式推理正在系统性地增强。VLM的神经符号方法表明，RL可以在不牺牲准确性的情况下激励更有效的潜在推理。对于细粒度的多图像理解，基于成分的对比度与GRPO和基于规则的空间奖励相结合可以实现显着改进。一个特别有创意的应用程序使用RL来减轻人工智能写作辅助中的角色扭曲，根据实验数据训练奖励模型，以使生成的文本与作者身份保持一致。RIME框架将重写视为生成式多模式嵌入的通用接口，使用Refine-RL来优化嵌入空间。这些多样化的应用程序--从K-12口语对话评分到多图像综合--表明RL正在成为为LLM注入特定任务能力的首选方法，而仅靠监督微调是无法实现的。

---

## 1. 无言语思考：具有抽象思想链的高效潜在推理

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Keshav Ramji, Tahira Naseem, Ram\'on Fernandez Astudillo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Abstract Chain-of-Thought, a novel post-training mechanism for discrete latent reasoning that dramatically reduces reasoning tokens while maintaining performance, using policy iteration and RL.

**摘要**: arXiv：2604.22709v1宣布类型：新摘要：虽然长而显式的思想链（CoT）已被证明对复杂的推理任务有效，但在推理过程中生成它们的成本很高。通过利用连续表示，非言语推理方法出现了更短的世代长度，但它们的性能落后于言语化的CoT。我们提出了$\textBF{Abstract Chain-of-Thought}$，这是一种离散潜在推理训练后机制，其中语言模型在生成响应之前从保留词汇表生成短的标记序列，以代替自然语言CoT。为了使以前看不见的“抽象”令牌有用，我们引入了一个策略迭代式的热身循环，该循环在（i.）通过掩蔽和执行有监督的微调从口头CoT中切换，以及（ii）通过训练模型以通过使用码本的约束解码仅从提示生成抽象令牌来进行自我提炼。热身后，我们在约束解码下通过热启动强化学习来优化抽象序列的生成。Abstract-CoT实现了高达11.6美元的推理令牌减少，同时展示了数学推理、描述跟随和多跳推理的相当性能，并在语言模型家族中进行了推广。我们还发现抽象词汇中出现了一种新兴的乘势定律分布，类似于自然语言中的分布，该分布在整个训练阶段中演变。我们的研究结果强调了训练后潜在推理机制的潜力，这些机制可以通过学习的抽象推理语言实现有效推理。

[阅读原文](https://arxiv.org/abs/2604.22709)

---

## 2. 结果奖励并不能保证可验证或有因果关系的推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Qinan Yu, Alexa Tartaglini, Peter Hase, Carlos Guestrin, Christopher Potts

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes metrics (CIR, SR) to evaluate reasoning quality in RLVR and shows that outcome rewards alone do not guarantee verifiable or causally important reasoning, offering a joint reward remedy.

**摘要**: arXiv：2604.22074v1宣布类型：新摘要：基于思想链推理的可验证奖励（WLVR）强化学习已成为语言模型后训练食谱的标准部分。一个常见的假设是，通过WLVR训练的推理链可靠地代表模型如何得到答案。在本文中，我们开发了两个度量标准来批判性地检查这个假设：推理的因果重要性（CIR），它衡量推理令牌对最终答案的累积影响，以及推理的充分性（SR），它衡量验证者是否可以单独基于推理得出一个明确的答案。通过对Qwen2.5模型系列和ReasoningGym任务的实验，我们发现：（1）RLVR确实提高了任务准确率，但它并没有可靠地提高CIR或SR，这使得推理在模型性能中的作用受到质疑：（2）RLVR之前的少量SFT可以弥补低CIR和SR;以及（3）通过在基于结果的奖励之上应用辅助CIR/SR奖励，即使没有SFT，也可以改善CIR和SR。这种联合奖励与RLVR的准确性相匹配，同时也导致因果关系重要和充分的推理。这些结果表明，WLVR并不总是导致模型以通常认为的方式依赖推理，但这个问题可以通过对训练后程序的简单修改来解决。

[阅读原文](https://arxiv.org/abs/2604.22074)

---

## 3. LLM如何检测和纠正自己的错误：内部信心信号的作用

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Dharshan Kumaran, Viorica Patraucean, Simon Osindero, Petar Velickovic, Nathaniel Daw

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly investigates internal confidence signals (PANL) for error detection and self-correction in LLMs, revealing a second-order confidence architecture that causally drives self-improvement without external feedback.

**摘要**: arXiv：2604.22271v1公告类型：新摘要：大型语言模型可以检测自己的错误，有时甚至可以在没有外部反馈的情况下纠正错误，但其潜在机制仍然未知。我们通过决策神经科学的二阶信心模型来研究这一点。在一阶系统中，置信度来自生成信号本身，因此对于所选响应来说是最大的，从而排除了错误检测。二阶模型初始化部分独立的评估信号，该信号可能与承诺的响应不一致，为错误检测提供基础。Kumaran等人（2026）表明，LLM在回答后立即缓存置信度表示（即回答后新元素：PANU）--这因果关系驱动了言语置信度并与日志概率无关。在这里，我们测试该PANU信号是否超出了置信范围，以支持错误检测和自我纠正。在这里，我们测试该信号是否支持错误检测和自我纠正，从二阶框架中得出预测。使用先验证后正确的范式，我们表明：（i）言语信心预测错误检测的程度远远超出了代币日志概率，排除了一阶帐户的可能性;（ii）PANU激活预测错误检测超出了言语信心本身;（iii）PANU预测模型可以纠正哪些错误--所有行为信号都失败了。因果干预证实，当答案信息损坏时，PANI会发出救援错误检测行为的信号。所有发现均在模型（Gemma 3 27 B和Qwen 2.5 7 B）和任务（TriviaQA和MNLI）中重复。这些结果表明，LLM自然地实现了二阶置信度架构，其内部评估信号不仅编码答案是否可能错误，还编码模型是否具有修复它的知识。

[阅读原文](https://arxiv.org/abs/2604.22271)

---

## 4. 大型语言模型早做决定，晚解释

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ayan Datta, Zhixue Zhao, Bhuvanesh Verma, Radhika Mamidi, Mounika Marreddy, Alexander Mehler

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that LLM reasoning is often decided early and proposes early stopping to reduce redundant CoT tokens, directly addressing latent reasoning efficiency.

**摘要**: arXiv：2604.22266v1宣布类型：新摘要：大型语言模型通常通过生成长的中间思想链推理来实现强大的性能。然而，目前尚不清楚模型的最终答案何时实际上是在生成过程中确定的。如果答案已经在中间阶段确定，则后续推理标记可能会构成决策后解释，从而增加推理成本和延迟，而不会提高正确性。我们使用强制答案完成来研究预测答案在推理步骤中的演变，这在部分推理前置处引发了模型的中间预测。重点关注Qwen 3 - 4 B并对所有考虑的数据集的结果进行平均，我们发现预测答案仅在32%的查询中发生变化。此外，一旦最终答案切换发生，该模型平均每个查询生成760个额外的推理令牌，占总推理预算的很大一部分。受这些发现的激励，我们研究了早期停止策略，一旦答案稳定下来，这些策略就会停止生成。我们表明，简单的启发式方法（包括基于探测器的停止）可以将每个查询的推理令牌使用减少500个令牌，而准确性仅下降2%。总而言之，我们的结果表明，思想链生成的很大一部分是多余的，可以在对性能影响最小的情况下减少。

[阅读原文](https://arxiv.org/abs/2604.22266)

---

## 5. 测量和缓解人工智能写作辅助的角色失真

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Paul R\"ottger, Kobi Hackenburg, Hannah Rose Kirk, Christopher Summerfield

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based method using reward models trained on experimental data to mitigate persona distortions in AI writing assistance, directly addressing RL for LLM alignment.

**摘要**: arXiv：2604.22503v1宣布类型：新摘要：数亿人使用人工智能（AI）进行写作辅助。在这里，我们评估了人工智能写作辅助如何扭曲作家角色--他们感知的信仰、个性和身份。在三项大规模实验中，作家（N= 2，939）在有和没有人工智能帮助的情况下撰写政治观点段落。不同的读者群体（N= 11，091）在读者感知的29个社会显著维度上盲目评估这些段落，涵盖政治观点、写作质量、作家个性、情感和人口统计。人工智能写作辅助在各个方面都造成了角色扭曲：有了人工智能，作家似乎更加固执己见、有能力和积极，他们认为的人口结构也转向了更特权的群体。作家们反对许多观察到的扭曲，但即使意识到这些扭曲，他们仍然更喜欢人工智能辅助的文本。我们通过在实验数据（10，008个段落，2，903，596个评分）上训练奖励模型，成功地减轻了模型层面上令人反感的角色扭曲，以引导人工智能输出忠实地代表作家立场。然而，这是以用户接受度为代价的，这表明人工智能写作辅助的理想属性和不理想属性之间存在纠缠，而这可能很难解决。总之，我们的研究结果表明，即使在人类监督的现实条件下，人工智能写作辅助的角色扭曲也是普遍和持久的，这对公共话语，信任和民主审议产生了影响，这些影响随着人工智能的采用而扩大。

[阅读原文](https://arxiv.org/abs/2604.22503)

---

## 6. 通过强化学习激励VLM中基于神经符号启发的推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Karthic Palaniappan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes using RL to incentivize neuro-symbolic latent reasoning in VLMs, achieving accuracy gains with 75% fewer reasoning tokens.

**摘要**: arXiv：2604.22062v1宣布类型：新摘要：世界上有7，407种语言。但是，世界上不存在的语言又如何呢？人类是否思想如此狭隘，以至于我们不关心外星人交流的语言？外星人也是人类！在2016年的电影《抵达》中，艾米·亚当斯扮演语言学家路易丝·班克斯博士，她通过学习用非连续句子组成的外星语言（七足）思考，获得了超越时间和展望未来的能力。在这项工作中，我的目标是探索视觉语言概念在神经符号语言中的表达和推理，并研究“思维系统”的分析推理能力和效率的提高。使用Qwen 3-BL-2B-Direct作为基本模型和4 $\times$ Nvidia H200图形处理器节点，我在由数学、科学和常识问题组成的视觉语言评估数据集上实现了3.33%的准确性提高，同时将推理令牌比SymPy减少了75%。我记录了所面临的计算挑战、扩展可能性以及未来在视觉语言模型中改善神经符号语言思维的工作。训练和推理设置可在此处找到：https://github.com/i-like-bfs-and-dfs/wolfram-reasoning。

[阅读原文](https://arxiv.org/abs/2604.22062)

---

## 7. 通用变形金刚需要记忆：自适应回归推理中的深度状态权衡

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Grigory Sapunov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a Universal Transformer with memory tokens and adaptive computation time for latent reasoning on combinatorial puzzles, revealing a router initialization trap and showing attention head specialization.

**摘要**: arXiv：2604.21999v1宣布类型：新摘要：我们研究了学习记忆令牌作为计算暂存器的单块通用Transformer（UT）与自适应计算时间（ACT）数独极端，组合推理基准。我们发现记忆令牌在经验上是必要的：在所有测试的配置中-- 3个种子、多个令牌计数、两个初始化方案、ACT和固定深度处理--没有记忆令牌的配置都无法实现非凡的性能。最佳计数表现出明显较低的阈值（T=0总是失败，T=4是临界值，T=8对于81个细胞谜题可靠地成功），然后是稳定的平台期（T=8-32，57.4% +/- 0.7%精确匹配）并在T=64时因注意力稀释而崩溃。   在实验过程中，我们发现了一个导致超过70%的训练运行失败的路由器初始化陷阱：默认零偏差初始化（p ~ 0.5）和Graves推荐的正偏差（p ~ 0.73）都会导致令牌在初始化约2步后停止，进入模型无法逃脱的浅平衡（停止~ 5-7）。将偏差倒置为-3（“深度启动”，p ~ 0.05）可消除此故障模式。我们通过消融确认该陷阱是ACT初始化固有的，而不是我们架构选择的产物。   通过建立可靠的训练，我们表明（1）ACT提供比固定深度处理更一致的结果（3粒种子中56.9% +/- 0.7% vs 53.4% +/- 9.3%）;（2）使用Lambda热身的ACT实现匹配准确性（57.0% +/- 1.1%）使用的思考步骤减少了34%;以及（3）注意力头专注于记忆阅读器、约束传播器和跨循环深度的积分器。代码可在https://github.com/che-shr-cat/utm-jax上获取。

[阅读原文](https://arxiv.org/abs/2604.21999)

---

## 8. 具有硬负性的客观塑造：基于RL的LLM推荐器的窗口部分AUC优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wentao Shi, Qifan Wang, Chen Chen, Fei Liu, Dongfang Liu, Xu Liu, Wanli Ma, Junfeng Pan, Linhong Zhu, Fuli Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new RL objective (WPAUC) and optimization method (TAWin) for LLM-based recommenders, directly addressing RL for LLMs with a novel reward design.

**摘要**: arXiv：2604.22504v1宣布类型：新摘要：强化学习（RL）通过对比积极项和消极项来有效优化基于大型语言模型（LLM）的调度器。从经验上看，使用射束搜索负性进行的训练始终优于随机负性，但这种机制尚未得到很好的理解。我们通过分析诱导的优化目标来解决这一差距，并表明：（i）在二元奖励反馈下，通过团体相对政策优化（GRPO）优化LLM优先级从理论上等效于最大化ROC曲线下面积（AU），该曲线下面积通常与Top-$K$建议不一致;和（ii）用射束搜索负取代随机负，将目标重塑为部分AUR，改善与Top-$K$指标的一致性。受此观点的启发，我们引入了窗口化部分UC（WPAUC），它将假阳性率（FPR）限制在窗口[$\Alpha，\Alpha+d$]，以更直接地与Top-$K$指标保持一致。我们进一步提出了一种有效的阈值调整窗口重加权（TAWin）RL方法进行优化，从而能够显式控制目标Top-$K$性能。在四个现实世界数据集上进行的实验验证了该理论并提供了一致的最先进性能。

[阅读原文](https://arxiv.org/abs/2604.22504)

---

## 9. 通过监督薄弱的培训消除LLM中的沙袋

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Emil Ryd, Henning Bartsch, Julian Stastny, Joe Benton, Vivek Hebbar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training method combining SFT and RL under weak supervision to mitigate sandbagging in LLMs, directly addressing RL-based training for eliciting true model capabilities.

**摘要**: arXiv：2604.22082v1宣布类型：新摘要：随着人工智能系统开始自动化复杂任务，监管越来越依赖于较弱的模型或有限的人类监督，无法完全验证输出质量。一个比其主管更有能力的模型可以通过沙袋来利用这一差距，制作看似可以接受但达不到其真正能力的作品。即使没有可靠的验证，训练也能激发模型的最佳工作吗？我们使用经过沙袋训练的模型生物来研究这个问题，测试解决问题的数学、研究生水平的科学和竞争性编码任务的启发技术。我们发现，当有监督的微调（SFT）和强化学习（RL）相结合时，弱监督的训练可以可靠地引发沙袋模型：弱演示的SFT打破了沙袋行为，使RL能够完全引发性能。两种方法单独可靠地成功-没有SFT的RL几乎总是会导致奖励黑客攻击，而不是真正的改进。至关重要的是，这依赖于训练与部署之间的区别;当模型能够区分训练和部署时，它们就可以在训练期间表现良好，同时在训练后继续进行沙袋。我们的结果提供了初步证据，证明培训是对抗沙袋的可行缓解措施，同时强调了使培训与部署区分开来的重要性。

[阅读原文](https://arxiv.org/abs/2604.22082)

---

## 10. LLM自我纠正什么时候有帮助？控制理论的马尔科夫诊断和验证优先干预

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Aofan Liu, Jingxiang Meng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a control-theoretic diagnostic for LLM self-correction loops, directly relevant to self-improving agents and RL-like feedback dynamics.

**摘要**: arXiv：2604.22273v1宣布类型：新摘要：迭代自我纠正在代理LLM系统中被广泛使用，但重复改进何时有帮助还是有伤害仍不清楚。我们将自我纠正构建为一个控制论反馈循环，其中相同的语言模型同时充当控制器和工厂，并在{正确，不正确}上使用双状态马尔科夫模型来操作简单的部署诊断：仅当MCR/EIR > Acc/（1 - Acc）时才重新启动。从这个角度来看，EIR充当稳定裕度，并充当轻量级控制器设计的提示功能。在7个模型和3个数据集（GSM 8 K、MAT、StrategyQA）中，我们发现一个尖锐的接近零的EIR阈值（<= 0.5%）将有益的自我纠正与有害的自我纠正区分开来。只有o3-mini（+3.4 pp，EIR = 0%）、Claude Opus 4.6（+0.6 pp，EIR ~ 0.2%）和o 4-mini（+/-0 pp）保持不降解; GPT-5降解-1.8 pp。首先验证的即时消融提供了因果证据，表明该阈值可以通过单独提示采取行动：在GPT-4 o-mini上，它将EIR从2%降低到0%，并将-6.2 pp降级变为+0.2 pp（配对McNemar p < 10 -4），而在已经亚阈值模型上几乎没有变化。ASC进一步说明了停止权衡：它停止了有害的改进，但会产生3.8 pp的信任激发成本。总体而言，论文认为自我纠正不应被视为默认行为，而应被视为由可测量的错误动态决定的控制决策。

[阅读原文](https://arxiv.org/abs/2604.22273)

---

## 11. 不要模仿，强化：通过信念细化进行迭代分类

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Mahdi Kallel, Johannes T\"olle, Ahmed Hendawy, Carlo D'Eramo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Replaces supervised imitation with RL for iterative classification, introducing a recurrent agent with a value-based halting criterion, directly matching RL for LLMs and latent reasoning.

**摘要**: arXiv：2604.22110v1宣布类型：新摘要：标准监督分类训练模型模仿完美先知提供的确切标签。这种模仿只需一次即可完成，即使输入复杂性不同，也会将模型限制在固定的计算预算。此外，严格的训练目标迫使模型对其训练数据表达绝对确定性，导致评估期间的预测过于自信。我们提出了强化迭代分类（RIC），用强化学习（RL）取代模仿目标。RIC部署了一个循环代理，它迭代地更新类别上的预测分布，并因预测质量的逐步改进而获得奖励。价值函数通过估计剩余的改进空间来提供自然的停止标准。我们证明，迭代公式可以恢复与交叉信息相同的最佳预测，同时产生随时分类器。在图像分类基准上，RIC将监督基线的准确性与改进的校准进行匹配，并学会在输入之间自适应地分配计算。

[阅读原文](https://arxiv.org/abs/2604.22110)

---

## 12. 可控口语生成：针对K-12非母语英语学习者的LLM驱动评分系统

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Haidong Yuan, Haokun Zhao, Wanshi Xu, Songjun Cao, Qingyu Zhou, Long Ma, Hongjie Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DDPO, a multi-turn GRPO-based RL algorithm for controllable dialogue generation, directly matching RL for LLMs with a new reward design and training recipe.

**摘要**: arXiv：2604.22542v1宣布类型：新摘要：由于熟练程度不匹配，大型语言模型（LLM）常常无法满足非母语环境下K-12英语学习者的教学需求。为了应对这一普遍挑战，我们引入了一个与熟练度一致的框架，以中国国家课程（CSE）为代表案例，使LLM输出适应学习者能力。我们的框架可以通过四层分级系统精确控制词汇复杂性，并由一套全面的新资源支持：分级词汇列表和多轮对话库。   我们的核心技术贡献是\textBF {DDPO}算法，即多元化驱动的政策优化，这是一种基于GRPO的多回合方法，旨在保留对话多样性，同时全面优化对话质量。这种方法的表现显着优于传统方法，实现了较低的词汇量缺失率和较高的多样性，同时增强了对话的自然性和教学价值。虽然基于CSE，但我们的框架旨在灵活性，并且可以轻松适应其他教育标准。我们的模型、数据和代码都将是开源的，为个性化英语口语练习提供一个可扩展的平台，有效地解决K-12学习者在非沉浸式环境中面临的独特挑战。

[阅读原文](https://arxiv.org/abs/2604.22542)

---

## 13. 超越思想链：重写作为生成式多模态嵌入的通用接口

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Peixi Wu, Ke Mei, Feipeng Ma, Bosong Chai, Zhibin Lan, Chenxi Zhao, Shannan Yan, Jie Chen, Zhangchi Hu, Yansong Peng, Bo Lin, Junjie Zhou, Dacheng Yin, Tianyi Wang, Fengyun Rao, Jing Lyu, Hebei Li, Xiaoyan Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RIME, a framework using Refine-RL to optimize generative multimodal embeddings, directly matching RL for LLMs with a new reward-driven optimization loop.

**摘要**: arXiv：2604.22280v1宣布类型：新摘要：多模式大型语言模型（MLLM）已成为通用多模式嵌入的一个有前途的基础。最近的研究表明，推理驱动的生成式多模式嵌入在几个嵌入任务上可以优于区分性嵌入。然而，思想链（CoT）推理往往会产生多余的思维步骤，并在更广泛的检索场景中在总结答案中引入语义歧义。为了解决这一限制，我们提出了重写驱动的多模式嵌入（RIME），这是一个统一框架，通过检索友好的重写来联合优化生成和嵌入。与此同时，我们提出了跨模式对齐（CMA）来连接生成性和区分性嵌入空间，使灵活的相互检索能够权衡效率和准确性。在此基础上，我们还引入了Refine Reinstration Learning（Refine-RL），该学习将区分性嵌入视为稳定的语义锚来指导重写优化。对MMEB-V2、MRMR和UVRB的大量实验表明，RIME的性能大大优于先前的生成式嵌入模型，同时显着缩短了思考时间。

[阅读原文](https://arxiv.org/abs/2604.22280)

---

## 14. 冻结LLM的学习证据突出显示

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Frank Shyu, Luke Simon, Sandeep Pandey, Xi Liu, Jian Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based framework (HiLight) for training a lightweight Actor to highlight evidence in context for frozen LLMs, directly matching RL for LLMs via reward-based optimization.

**摘要**: arXiv：2604.22565v1宣布类型：新摘要：大型语言模型（LLM）可以很好地推理，但当它被埋在漫长、嘈杂的环境中时，它常常会错过决定性的证据。我们引入HiLight，这是一个证据强调框架，它将证据选择与冻结LLM求解器的推理分开。HiLight通过训练轻量级的Empress Actor在未改变的上下文中在关键跨度周围插入最少的高光标签，从而避免了压缩或重写可能会丢弃或扭曲证据的输入。然后，冻结的求解器对强调的输入执行下游推理。我们将突出显示视为一个弱监督决策问题，并仅使用求解器的任务奖励通过强化学习来优化Actor，不需要证据标签，也不需要访问或修改求解器。在连续推荐和长上下文问题回答中，HiLight在强大的基于预算和自动预算优化基线上持续提高性能。习得的重点政策将零射击转移到较小和较大的未见过的解算器家族，包括基于API的解算器，这表明Actor捕获了真实的、可重复使用的证据结构，而不是过度适合单一的主干。

[阅读原文](https://arxiv.org/abs/2604.22565)

---

## 15. CGC：用于细粒度多图像理解的成分接地对比

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Lihao Zheng, Zhenwei Shao, Yu Zhou, Yan Yang, Xintian Shen, Jiawei Chen, Hao Ma, Tao Wei

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based training framework (GRPO with rule-based spatial reward) for improving fine-grained multi-image understanding in MLLMs, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2604.22498v1宣布类型：新摘要：尽管多模式大型语言模型（MLLM）发展迅速，但它们在细粒度多图像理解方面仍然面临着显着的挑战，通常表现出空间幻觉、注意力泄露和对象恒常性失败。此外，现有方法通常依赖于昂贵的人工注释或大规模思想链（CoT）数据生成。我们提出成分接地对比度（缩写。CGC），一个低成本的完整框架，用于促进对MLLM的细粒度多图像理解。CGC基于现有的单图像基础注释，通过图像间对比度和图像内对比度构建合成多图像训练实例，这分别引入了用于跨图像区分的语义脱钩干扰物上下文和用于对象稳定性的相关交叉视图样本。CGC进一步在GRPO框架内引入了基于规则的空间奖励，以在先思考后基础范式下改善源图像归因、空间对齐和结构化输出有效性。实验表明，CGC在细粒度多图像基准测试（包括MIG-Bench和VLM 2-Bench）上实现了最先进的结果。学到的多图像理解能力还转移到更广泛的多模式理解和推理任务中，与MathVista（+2.90）、MuirBench（+2.88）、MMStar（+1.93）、MMMU（+1.77）和BLINK（+1.69）上的Qwen 3-BL-8B基础模型相比，获得了一致的收益。

[阅读原文](https://arxiv.org/abs/2604.22498)

---

## 16. SOLAR-RL：半在线长期作业强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jichao Wang, Liuyang Bian, Yufeng Zhou, Han Xiao, Yue Pan, Guozhi Wang, Hao Wang, Zhaoxiong Wang, Yafei Wen, Xiaoxin Chen, Shuai Ren, Lingfang Zeng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a semi-online RL framework for GUI agents that retroactively assigns dense step-level rewards from trajectory-level signals, directly addressing RL for LLMs with a new reward design and training recipe.

**摘要**: arXiv：2604.22558v1宣布类型：新摘要：随着多模式大型语言模型（MLLM）的成熟，图形用户界面代理正在从静态交互发展到复杂导航。虽然强化学习（RL）已成为在动态图形用户界面任务上训练MLLM代理的一种有前途的范式，但其有效应用面临着困境。标准离线RL通常依赖于静态步骤级数据，忽略了任务完成和执行质量等全局轨迹语义。相反，在线RL捕捉了长期动态，但面临着高交互成本和潜在的环境不稳定性。为了弥补这一差距，我们提出了SOLAR-RL（半在线长视野分配强化学习）。我们的框架不是仅仅依赖昂贵的在线互动，而是将全球轨迹洞察直接整合到离线学习过程中。具体来说，我们从静态数据中重建不同的推出候选者，使用每步有效性信号检测第一个故障点，并追溯分配密集的步骤级奖励与目标对齐的整形，以反映自动化级别的执行质量，有效地模拟在线反馈，而无需交互成本。大量的实验表明，与强基线相比，SOLAR-RL显著提高了长期任务完成率和鲁棒性，为自主GUI导航提供了一个样本高效的解决方案。

[阅读原文](https://arxiv.org/abs/2604.22558)

---

