# 💡 今日研究速览 (Daily Summary)

# LLM的RL

当今的主导主题是LLM强化学习的成熟，超越简单的奖励模型，转向复杂、多方面的训练循环。多篇论文解决了稳定和加强RL训练后的核心挑战。DiPod通过引入政策上ELBO正规化（一种维护政策完整性的原则性解决方案）来解决扩散政策优化中的根本漂移问题。RefGRPO和CORA都以校准和一致性为目标-RefGRPO通过代理RL的免费校准奖金缩小了反射差距，而CORA则引入了一致性奖励模型来解决多模式WLVR中的思考-答案差距。VISTA通过从多个视图构建比较组，进一步将GRPO扩展到图形界面基础，展示了这些RL框架的多功能性。生产就绪的CoRe系统具有半在线混合偏好优化循环和相乘奖励，展示了这些原则如何扩展到现实世界的视频搜索，而Cache RL将迭代SFT和GRPO与缓存层感知奖励相结合，以实现高效的工具调用代理培训。总的来说，这些工作表明从概念验证RL微调转向稳健、可部署的系统，该系统明确管理探索、校准和任务性能之间的权衡。

# 代理和代理RL

代理培训正在看到一种范式转变，即更深入地利用RL的基于策略的自我完善框架。RePro框架引入了具有复合奖励的回顾性进度感知训练，使智能体能够通过将预期进度与实际结果进行比较来从自己的轨迹中学习。这反映了使用自我生成的数据进行改进的更广泛趋势。Be My Tutor的论文提出了一种新颖的政策共同蒸馏方法（OPSoD），两个LLM通过同行反馈共同进化，在没有外部监督的情况下实现跨领域的帕累托改进。这种基于同伴的学习范式尤其值得注意，因为它提供了人类注释的可扩展替代方案。用于自适应流推理的AdaSR框架进一步将代理RL分解为具有细粒度优势分配的分层阶段（流与深度推理），这表明该领域正在朝着更细致入微、时间感知的奖励结构发展，用于复杂的、多步骤的代理任务。

# 潜在推理

潜在推理出现了重大突破，两篇论文提出了补充方法来减少思想链的计算负担。SuperThoughts引入了一种将推理令牌压缩为潜在表示并每步解码两个令牌的方法，有效地缩短了推理长度，同时保持准确性--这是对推理成本问题的直接攻击。PauseRec提出了一种用于生成式推荐的轻量级隐式推理范式，该范式使用暂停令牌进行潜在计算，证明这种方法即使在实际的推荐系统中也是可行的。这些工作表明，该领域正在趋同于这样一个观点：并非所有推理都需要显式且大量符号，这为更高效的架构打开了大门，在生成输出之前在隐藏状态中执行深度计算。

# 多模式和自我进化

多模式系统越来越多地采用自我监督的、按政策的演变策略。自我进化的视觉质疑者框架特别优雅：它使用VLM本身作为提议者和过滤器来生成更难、信息量更大的问题，然后在没有任何外部监督的情况下在政策提炼循环中训练自己。这代表着视觉语言模型向自主改进迈出的重要一步，该模型积极策划自己的课程。CORA的论文虽然主要是RL的贡献，但专门解决了多模式WLVR背景，强调思维与答案的差距在多模式环境中尤其明显，并且需要专门的一致性感知解决方案。这些发展表明，VLM的下一个前沿不仅是更好的架构，而且是自我维持的训练循环，可以不断生成具有挑战性的特定领域数据并从中学习。

---

## 1. 成为我的导师：政策上的共同蒸馏，通过同行反馈共同改进LLM

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Woohyeon Byeon, Jiwon Jeon, Jeonghye Kim, Youngchul Sung

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes On-Policy Co-Distillation (OPCoD), a novel on-policy distillation framework where two LLMs co-evolve via peer feedback and cognizance-based gating, achieving Pareto improvement across domains.

**摘要**: arXiv：2606.14368v1宣布类型：新摘要：我们研究多领域LLM培训，其中两个模型在不同领域各自更强，通过政策反馈相互指导来共同进化。与单向蒸馏或单模型微调不同，我们的目标是相互帕累托改进：每个模型在不失去其原始优势的情况下跨领域改进。为此，我们提出了按政策共蒸馏（OPCoD），每个学生的自我蒸馏取决于自己的正确推出和同行的反馈。为了使反馈交换有效，OPCoD使用基于认知的门控来决定何时提供反馈，并将反馈锚定到问题的基础反馈。在科学问答任务中，OPCoD始终优于基线，并在所有评估的领域对和学生中实现了帕累托改进。

[阅读原文](https://arxiv.org/abs/2606.14368)

---

## 2. 缩小反射差距：Atltic RL的免费校准奖金

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yinglun Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces RefGRPO, augmenting standard RL for LLM agents with a free calibration bonus from contrasting agent reflection with actual outcomes, closing the reflection gap and improving both calibration and task accuracy.

**摘要**: arXiv：2606.14211v1宣布类型：新摘要：LLM越来越多地被部署为与外部环境交互并观察执行结果、错误消息和工具输出等反馈的代理。功能良好的代理应该能够利用此反馈来准确评估自己的绩效。然而，我们发现了一个持续存在的反思差距：LLM代理人在观察到具体的环境反馈后往往会错误评估自己的输出--即使他们正确回答了问题--而标准RL由于学分分配不匹配而几乎没有帮助。为了缩小这一差距，我们提出了RefGRPO，这是一个简单而有效的修复方案，它通过两个关键成分增强了标准RL算法：通过将代理自己的反射与实际结果进行比较来计算的免费校准奖金（不需要额外的奖励模型、LLM判断或外部注释），以及对其系数的动态时间表。与标准RL基线相比，我们的方法同时改进了反射校准（例如，将信心不足率降低44.4美元至7.7美元）和任务准确性（例如，$75.1\% \到76.5\%$）跨五个基准测试的文本转SQL。由此产生的校准反射将代理变成其自己的基于环境反馈的验证者，这进一步实现了（i）更好的自我改进，使用反射作为伪奖励，而无需结果监督，以及（ii）通过仅承诺标记为正确的展开来进行更有效的测试时选择性预测。

[阅读原文](https://arxiv.org/abs/2606.14211)

---

## 3. 扩散政策优化而不偏离

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Haozhe Jiang, Haiwen Feng, Pieter Abbeel, Jiantao Jiao, Angjoo Kanazawa, Nika Haghtalab

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DiPOD, a diffusion policy optimization framework that uses on-policy ELBO regularization to stabilize RL post-training for diffusion policies, directly addressing RL for LLMs.

**摘要**: arXiv：2606.13795v1宣布类型：新摘要：RL后培训对于改善扩散政策变得越来越重要，但现有的扩散政策梯度方法往往不稳定，无法实现可靠的政策改进。我们将其原因确定为双重漂移现象：优化变分替代品可以让ELBO与真实的log似然分开，从而使产生的代理政策梯度与预期回报的真实政策梯度不一致。我们提出了\textBF{DiPod}，这是一个扩散政策优化框架，通过将自我提炼与政策改进的梯度更新交织在一起，在整个训练过程中保持严格的行为。这导致了一个简单实用的算法：使用政策上的ELBO规则化器来增强每个扩散政策梯度更新。在扩散语言模型训练后和连续控制扩散政策中，DiPod大大稳定了训练并获得了比之前方法更高的回报。

[阅读原文](https://arxiv.org/abs/2606.13795)

---

## 4. AdaSR：具有分层相对策略优化的自适应流推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junlong Tong, Wenqi Xu, Yingqi Fan, Anhao Zhao, Xuan Lu, Yang Tan, Xiaoyu Shen

**机构**: EIT-NLP, Unknown Institution

**💡 亮点 (Highlight)**: Proposes AdaSR, a framework for adaptive streaming reasoning with a novel Hierarchical Relative Policy Optimization (HRPO) that decomposes RL into streaming and deep reasoning phases with fine-grained advantage assignment, directly advancing RL for LLMs and latent reasoning.

**摘要**: arXiv：2606.14694v1宣布类型：新摘要：大型推理模型通常遵循先读后想的范式：它们观察完整的输入，在静态上下文中推理，然后得出答案。然而，许多现实世界的场景本质上是动态的，例如音频和视频流，其中信息以连续流的形式到达，模型必须在部分观察下推理、更新和响应。最近的流推理方法允许模型在阅读时思考，但它们很大程度上依赖于对预先构建的轨迹的监督模仿，这限制了它们的灵活性。在本文中，我们提出了AdaSR，这是一种自适应流推理框架，使模型能够在输入流期间进行推理，并在流完成后执行最终审议，学习何时思考以及在不同阶段分配多少计算。为了优化这个分层推理过程，我们引入了分层相对政策优化（HRPO），它将政策优化分解为流推理和深度推理阶段，提供更细粒度的优势分配，而不是将单个序列级优势均匀分布在所有令牌上。HRPO集成了格式、准确性和适应性思维奖励，以执行有效的推理协议、保持最终任务性能并鼓励延迟感知的计算分配。实验表明，与监督微调基线相比，AdaSR在推理准确性、计算效率和流媒体延迟之间实现了更好的平衡。我们在https://github.com/EIT-NLP/StreamingLLM/tree/main/AdaSR上发布我们的代码。

[阅读原文](https://arxiv.org/abs/2606.14694)

---

## 5. 自我进化的视觉质疑者

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yijun Liang, Hengguang Zhou, Ming Li, Lichen Li, Cho-Jui Hsieh, Tianyi Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving framework for VLMs that uses the model as both proposer and filter to generate harder, more informative questions, training itself in an on-policy distillation loop without external supervision.

**摘要**: arXiv：2606.13929v1宣布类型：新摘要：视觉语言模型（VLM）通常被训练为被动回答者，而它们主动提出多样化、非琐碎、以视觉为中心和基础问题的能力仍然没有得到充分的探索。现有视觉提问者的表现受到高质量训练数据的可用性或策展成本的限制。我们表明，VLM可以在没有任何外部监督的情况下不断改进自己作为视觉提问者。我们提出了一个自我进化的框架，该框架使用VLM本身作为提议者和过滤器，以生成更难、信息更丰富且以视觉为中心的问题，同时保持其探索多样性以避免训练崩溃。然后使用这些问题以提问者和回答者模式训练VLM。为了评估提问者，我们引入了一种代理协议，该协议沿着感知、推理和多样性维度评估问题。跨各种主干VLM的实验表明，我们的方法大大提高了自主问题生成的质量，并大大扩展了自主问题生成的难度边界。在相同的预算下，我们的自我监督比在静态源数据上进行训练更有效。此外，自我发展的提问者仍然是一个有竞争力甚至更好的回答者。

[阅读原文](https://arxiv.org/abs/2606.13929)

---

## 6. VISTA：针对图形用户界面接地的视图一致自我验证培训

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinyu Qiu, Yunzhu Zhang, Heng Jia, Shuheng Shen, Changhua Meng, Linchao Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes VISTA, a GRPO-based RL training framework for GUI grounding that constructs comparison groups from multiple views and adds a self-verified cross-view anchor, directly improving RL for LLMs.

**摘要**: arXiv：2606.14579v1宣布类型：新摘要：当将组相对策略优化（GRPO）应用于图形用户界面基础时，将从单个屏幕截图视图中抽样展开;组通常要么在困难的实例中全部失败，要么在简单的实例中全部成功，从而不会产生有用的相对优势。我们提出了VISTA（视图一致的自我验证训练），这是一个基于GRPO的训练框架，它从同一图形用户界面实例的多个目标保留视图中构建每个比较组。每个视图都由一个裁剪生成，该裁剪保持目标元素可见并准确地重新映射其框，因此可以在语义上相同但几何上不同的输入之间比较模型展开。为了稳定短坐标生成，而不将强化学习转化为无条件模仿，VISTA进一步添加了一个自我验证的交叉视图锚点：一个通过队列加权损失进行优化的Oracle答案，从组基线中排除，并且仅在模型产生最大回报推出时才激活。在五个图形界面接地基准和多个Qwen主干中，VISTA持续提高接地准确性。在ScreenSpot-Pro上，它将Qwen 3-BL 4 B/8B/30 B-A3 B从55.5/52.7/53.7提高到63.4/65.8/67.0。稳健性分析进一步显示出更高的最差视角准确性和更低的预测翻转率。

[阅读原文](https://arxiv.org/abs/2606.14579)

---

## 7. 基于大语言模型的生成式推荐的隐式推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yinhan He, Liam Collins, Bhuvesh Kumar, Jundong Li, Neil Shah, Donald Loveland

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PauseRec, a lightweight implicit reasoning paradigm for generative recommendation that uses pause tokens for latent computation, directly addressing latent reasoning for LLMs.

**摘要**: arXiv：2606.14142v1宣布类型：新摘要：大型语言模型（LLM）越来越多地被用作生成式推荐（GR）的支柱，承诺访问预先训练的世界知识。然而，对于GR可靠地援引这些知识仍然知之甚少。一个关键障碍是，基于LLM的GR通常代表具有语义ID（DID）的项目，从而扰乱LLM的自然语言推理界面，因为LLM在预训练期间看不到这些标记。现有的方法通过昂贵的多阶段管道来解决这个问题，这些管道将SIS接地并引出明确的理由，但对何时以及为什么需要每个阶段提供有限的见解。在这项工作中，我们系统地分解了基于LLM的GR的显式推理训练管道，揭示了三个关键局限性：世界知识言语化减弱、AID和自然语言令牌嵌入空间之间的不一致以及对理由质量的敏感性，所有这些都会损害显式推理性能。为了规避这些问题，我们提出了PauseRec，这是一种为GR量身定制的轻量级隐式推理范式。PauseRec非常实用，可以避免昂贵的推理轨迹获取和推理对齐训练，从而带来多种好处：（1）它比标准显式CoT方法高出6.22%，（2）它将训练成本降低了65%的图形处理器小时数，（3）它将推理速度提高了71.3%。这些结果将PauseRec定位为显式原理生成的轻量级替代方案，从而实现更有效和高效的基于LLM的GR。

[阅读原文](https://arxiv.org/abs/2606.14142)

---

## 8. CoRe：一款持续奖励的微调LLM查询重写器，用于网络规模视频搜索中的多阶段上下文感知相关性

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yilin Wen, Rong Yang, Xiaojia Chang, Hong Sun, Gefu Tang, Chunhui Liu, Jeffrey Chen, Zeyu Ma, Lisong Qiu, Xiaochuan Fan, Congjia Yu, Quan Zhou, Yuheng Chen, Zian Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a continuously redeployed RL-based LLM query rewriter using a novel semi-online Mixed Preference Optimization loop with a multiplicative reward that mirrors production fusion, directly addressing RL-for-LLMs with a scalable training recipe.

**摘要**: arXiv：2606.14127v1宣布类型：新摘要：生产中基于LLM的查询重写器面临着一种紧张局势：培训奖励必须反映生产排名员如何使用重写，但培训过程必须足够便宜，以支持随着数据漂移的持续重新部署。我们介绍了CoRe（上下文相关性），这样一个系统，每周在一个主要的短视频搜索引擎中重新部署，持续了五个多月。我们的奖励使用部署的多模式相关性模型作为其来源，并使用反映生产融合代数的相乘比率形式，缩小了离线奖励代理留下的模拟与生产差距。半在线混合偏好优化循环使每周数百万个实例规模的奖励负担得起：DPO风格的成对目标将梯度传递限制为采样轨迹的顶部k/底部k小子集，并且阶段结构减少了训练器/推理服务器参数从每步到每阶段的同步。检测到奖励类和稳定性指标的自动升级门并从生产中真正的奖励黑客事件中恢复。重写器输出在召回、原始等级和细化等级时作为并行相关信号消耗，而不会取代原始信号，从而限制重写器失败爆炸半径。两次连续生产发布的在线A/B，首先在finerank部署重写器，然后将消费扩展到召回和rawrank，在统计上显着降低了受重写影响的查询的更改查询率，所有标题相关性和参与度指标都朝着预期方向发展。

[阅读原文](https://arxiv.org/abs/2606.14127)

---

## 9. Cache RL：通过缓存滚动和混合奖励的多回合工具调用代理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Md Amirul Islam, Sumiran Thakur, Huancheng Chen, Su Min Park, Jiayun Wang, Gyuhak Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces CacheRL, a system for training small agent models using iterative SFT and GRPO with a cache-tier-aware reward and hybrid thinking trajectories, directly contributing to on-policy distillation and RL for LLMs.

**摘要**: arXiv：2606.14179v1宣布类型：新摘要：我们介绍了Cache RL，这是一个用于训练小型代理基础模型的系统，在多步工具调用任务中实现了92%的流程准确性，接近GPT-5的94%，同时需要的计算量减少了100倍。我们的方法解决了实际代理培训中的三个挑战：从大型模型中大规模传输工具调用知识、在无需昂贵的实时工具执行的情况下实现强化学习，以及从嘈杂的缓存环境中稳健地学习。CacheRL引入了三项关键创新。首先，混合思维轨迹管道通过LLM生成的推理轨迹来增强代理轨迹，生成训练示例，不仅教导模型要调用什么工具，还教导为什么要调用。其次，Cache AgentLoop通过三层模糊缓存消除了实时执行成本，同时使用标记级掩蔽保持轨迹保真度。第三，缓存层感知奖励动态调整答案质量权重，以避免因缓存引起的限制而惩罚模型。通过迭代监督微调（SFT）和团体相对政策优化（GRPO），Cache RL将Qwen 3 - 4 B-Thinking的验证奖励从0.43提高到0.78。在公共代理工具调用基准上，我们的模型实现了与GPT-5等前沿模型的竞争性能。消融研究表明，消除知识转移会使绩效降低41%，而缓存感知奖励则会提高17%。有趣的是，强化学习提高了训练稳定性，但除了强监督微调之外，收益有限，这表明数据质量和奖励设计在构建实用的小型代理模型方面比复杂的优化方法发挥着更重要的作用。

[阅读原文](https://arxiv.org/abs/2606.14179)

---

## 10. CORA：通过面向一致性的推理对齐分析和弥合多模式WLVR中的思维与答案差距

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jiayue Cao, Zhicong Lu, Xuehan Sun, Wei Jia, Hongling Zheng, Changyuan Tian, Zichuan Lin, Wenqian Lv, Nayu Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CORA, a consistency reward model and hybrid advantage splitting method to address thinking-answer inconsistency in multimodal RLVR, directly advancing RL for LLMs.

**摘要**: arXiv：2606.14691v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）已成功激发大型语言模型的推理能力，推动其向多模式场景的扩展。现有的方法主要集中在提高推理痕迹的视觉覆盖率和减轻视错觉，但低估了推理过程和最终答案之间的语义不一致性。在本文中，我们深入研究了大型视觉语言模型（LVLM）的WLVR中的思维-答案不一致性，展示了对在整个组相对政策优化（GRPO）培训过程中收集的展开的彻底分析和后WLVR评估结果，表明该问题在培训期间持续存在，并在推理期间仍然存在。受分析的启发，我们提出了一致性导向推理对齐（CORA），通过轻量级即插即用一致性奖励模型将思考-答案语义一致性引入到WLVR中，并进一步结合混合奖励优势拆分（Hras）来稳定协调任务和一致性优化。代表性多模式推理基准和主流LVLM的广泛实验表明，CORA提高了任务性能，同时有效地减轻了思维与答案的不一致性，从而产生更忠实的推理痕迹。

[阅读原文](https://arxiv.org/abs/2606.14691)

---

## 11. 超级想法：叠加推理代币

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zheyang Xiong, Shivam Garg, Max Yu, Vaishnavi Shrivastava, Haoyu Zhao, Anastasios Kyrillidis, Dimitris Papailiopoulos

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SuperThoughts, a latent reasoning method that compresses CoT tokens into latent representations and decodes two tokens per step, reducing reasoning length while maintaining accuracy.

**摘要**: arXiv：2606.13862v1宣布类型：新摘要：长思想链（CoT）推理改进了LLM问题解决，但由于顺序令牌生成，计算成本很高。虽然最近的作品探索了连续潜在空间中的推理以绕过离散令牌生成，但它们经常在训练稳定性方面遇到困难，并且由于缺乏监督信号而无法扩展到复杂的、长期任务。我们提出了SuperThoughts，它将连续的CoT令牌对压缩为单个潜在表示，并通过轻量级多令牌预测（RTP）模块每步解码两个令牌。这在训练时保留了离散令牌监督，同时在推理时增加了吞吐量。我们微调了Qwen 2.5-Math-1. 5 B-Direct、Qwen 2.5-Math-7 B-Direct、Qwen 2.5-Math-14 B-Direct，并在Math 500、AMC、OlympiadBench和GPQA-Diamond上进行评估。SuperThoughts采用基于信心的自适应机制，在不确定时可以回到标准解码，实现了CoT长度减少20 - 30%，%，同时以最小的降级保持准确性（大多数任务的准确性下降1-2个点）。

[阅读原文](https://arxiv.org/abs/2606.13862)

---

## 12. LLM代理培训的回顾性进展感知自我完善

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xinbei Ma, Congmin Zheng, Jiyang Qiu, Jiale Hong, Yao Yao, Xiangmou Qu, Jiaxin Yin, Xingyu Lou, Jun Wang, Weiwen Liu, Weinan Zhang, Zhuosheng Zhang, Hai Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel on-policy self-refinement framework (RePro) for LLM agents that uses retrospective progress-aware training with a composite reward, directly improving agent reasoning and task success.

**摘要**: arXiv：2606.14302v1宣布类型：新摘要：接受强化学习训练的基于LLM的代理可以优化分步动作预测，但缺乏对任务进展的元认知，从而导致了阻碍长期扩展的差距。一项试点研究表明，在线进步提示会损害绩效，而回顾性演示会有所帮助，但这种能力不能仅从结果奖励培训中产生。我们提出了RePro，回顾性进度感知训练，这是一个框架，它训练代理通过向前-然后-反射的展示范例自我生成进度信号：代理在线执行操作，然后回顾性地重新评估其逐步进度，给出完成的轨迹和已知的结果。RePro-PO通过回顾预热进行训练，从最小的外部演示中教授反射格式，然后通过RePro-PO进行进一步训练，并提供复合奖励，在没有持续外部监督的情况下产生自生信号。在WebShop、ALFWorld和推箱子上的实验表明，RePro增强了Qwen家族的性能，绝对成功率提高了12\%。

[阅读原文](https://arxiv.org/abs/2606.14302)

---

