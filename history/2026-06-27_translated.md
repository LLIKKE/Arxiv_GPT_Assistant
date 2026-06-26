# 💡 今日研究速览 (Daily Summary)

# SFT和数据处理
围绕推理模型的监督微调的效率正在出现一个明显的趋势。新的研究表明，推理痕迹的质量可以仅根据其初始标记来确定，使用受干扰的模型检查点作为轻量级鉴别器。这使得高效的数据策展管道能够与全轨迹过滤的性能相媲美或超过全轨迹过滤，从而显着降低构建高质量SFT集以进行推理的计算成本。

# LLM RL（奖励设计和培训稳定性）
该领域在奖励设计和培训动态方面正在经历深刻的成熟。一个主要焦点是奖励和政策的共同进化：一篇论文认为，没有单一的奖励是灵丹妙药，奖励设计必须随着政策能力的增长而调整，而另一篇论文则引入了一个框架，在该框架中，代理人和他们的评估者渐进地共同进化。实际上，这是通过几种新技术来解决的：一种几何展开策展方法，可以检测和纠正方向不一致的展开以稳定在线RL，以及一种使用来自基于分数的任务的校准连续奖励的框架，该框架绕过了对地面真相解决方案的需要，减轻了规模和频率主导地位。安全调整也受益于这种复杂性，使用GRPO的意图感知培训计划来奖励对用户意图的忠实性，而不是表面形式的合规性。此外，一个新颖的RLAIF框架引入了确定性奖励下限，以对抗工业查询生成中的奖励黑客攻击，凸显了RL对优化器选择的关键敏感性。

# 按政策蒸馏
政策上的蒸馏正在巩固其作为纯RL的强大替代品或补充的作用。新框架MOPD证明，多教师按政策蒸馏可以在8B模型的指导跟随任务方面优于GRPO RL，提供高度透明和简化的培训后管道。这还得到了多模式模型的自我进化框架的补充，该框架使用自我一致性奖励和内部角色分解来推动统一的理解和生成。对于代理设置，专用的按策略技能提炼方法（OPID）从完成的轨迹中提取分层技能监督，以提供密集的代币级优势，有效地为语言代理引导RL。弱驱动的协同进化框架还利用基于图的结构生成的WLVR来创建用于优化建模的闭环数据模型协同进化系统。

# 多模式理解与生成
多模式LLM的一个关键局限性--“视觉懒惰”--正在通过基于RL的后训练直接得到解决。一个新的框架引入了一种几何约束，可以最大化视觉输入和模型响应之间的互信息，使用一种新颖的反事实盲状态惩罚来明确惩罚模型忽视视觉证据。这是确保MLLM真正以视觉数据为基础而不是依赖语言先验迈出的重要一步。另外，用于多模式理解和生成的统一框架利用了自我进化和自我一致性奖励，展示了一条通往能够以同等保真度感知和创造的模型的道路。

# 压缩和效率
对压缩的研究揭示了现代推理架构中的严重脆弱性。积极的压缩，例如INT 4量化，可能会灾难性地破坏循环（潜在）推理器的全局推理能力。关键的见解是，这种退化可以通过按通道校准的量化来恢复，这表明压缩策略的设计必须明确了解模型的回归推理布局，而不仅仅是其参数计数。

# 机械解释性和模型引导
机械解释性的突破现在可以精确定位和引导RL诱导的行为。通过使用专用特征交叉搜索器，研究人员隔离了负责RL训练引发的工具使用行为的单个交叉搜索器特征。这使得无需再培训的行为控制成为可能，允许从业者在无需昂贵的再培训的情况下调整或删除习得的能力，甚至观察到能力对相关任务的溢出效应。

---

## 1. 问，解决，生成：通过自我一致性奖励自我进化的统一多模态理解和生成

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar, Abdelrahman Shaker, Fahad Khan, Hisham Cholakkal, Salman Khan, Rao Muhammad Anwer

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving training framework for unified LMMs using self-consistency rewards and internal role decomposition, directly relevant to on-policy distillation and RL for LLMs.

**摘要**: arXiv：2606.27376v1公告类型：新摘要：大多数支持视觉理解和图像生成的统一大型多模式模型（LSYS）仍然依赖于精心策划的训练后监督，例如人类注释、偏好标签或外部奖励模型。我们询问统一的LMM是否可以仅使用未标记的图像自主改进这两种能力。我们提出了一个自我进化的训练框架，具有三个内部角色：生成视觉问题的提议者、回答和评估问题的求解器以及合成图像的生成器。训练仅使用自推导的一致性信号，没有人类注释、偏好标签或任务训练的外部奖励/判断模型。为了稳定学习，我们引入了求解器令牌Entropy（STE），这是一种基于令牌级预测不确定性的连续难度信号，即使样本级一致性变得不可靠，它仍然有用。对于图像生成，我们设计了一个多尺度内部评估方案，该方案将问答保真度评分与周期一致的字幕相结合。这创建了求解器介导的耦合，其中更好的视觉理解可以实现更可靠的生成评估和更强的内部训练信号。该框架在基于扩散的BLIP 3 o、整流BAGEL和自回归VAR GPT-v1.1架构中保留了相同的角色分解、奖励逻辑和训练时间表，仅需要每个主干的本地提示和生成接口。在八个理解指标中，我们的方法始终优于相应的基本模型。在BAGEL上，它在MMMU上实现了$+3.5\%$的绝对收益，并将GenEval图像生成性能从$82\%$提高到$85\%$。代码和模型公开发布。

[阅读原文](https://arxiv.org/abs/2606.27376)

---

## 2. 保持警惕：通过MLLM中的反事实视觉对齐来缓解视觉懒惰

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xi Xiao, Chen Liu, Chih-Ting Liao, Yunbei Zhang, Qizhen Lan, Yuxiang Wei, Lin Zhao, Janet Wang, Jianyang Gu, Muchao Ye, Tianyang Wang, Hao Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes VIGIL, an RL post-training framework that uses a geometric constraint to maximize mutual information between visual input and response, directly addressing visual laziness in MLLMs via a novel counterfactual blind state penalty.

**摘要**: arXiv：2606.26387v1宣布类型：新摘要：多模式大型语言模型（MLLM）通过视觉感知扩展大型语言模型（LLM），实现对图像和文本的联合推理。尽管从LLM继承了强大的推理能力，但它们仍然容易产生与视觉输入相矛盾的幻觉。机械学研究表明，这种弱点源于视觉懒惰：MLLM在内部编码正确的视觉证据，但在反应过程中过度依赖强大的语言先验。现有的对齐方法（例如直接偏好优化）主要根据文本优化结果级别奖励。这引入了对语言快捷方式的优化偏见，导致响应往往与视觉证据相矛盾。为了解决这个问题，我们提出了视觉信息收益（VIGIL），这是一个培训后学习（RL）框架，将重点从数字奖励匹配转移到因果视觉基础。VIGIL引入了一种几何约束，可以显式地最大化视觉输入和生成的响应之间的互信息。我们通过惩罚“盲目自信”情况来实现这一目标，即即使文本视觉注意力被掩盖以创建反事实盲目状态，模型仍然不恰当地确定。大量实验表明，VIGIL在幻觉和推理基准上始终优于最近的对齐方法，而不会损害纯文本功能。我们的方法仅使用25%的偏好数据即可匹配最先进方法的全数据性能，甚至在没有明确边界盒监督的情况下展示了紧急空间接地能力。

[阅读原文](https://arxiv.org/abs/2606.26387)

---

## 3. EvoOptimShape：通过基于图的结构生成进行优化建模的弱点驱动协同进化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Qingcan Kang, Mingyang Liu, Xiaojin Fu, Shixiong Kai, Tao Zhong, Mingxuan Yuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a closed-loop data-model coevolution framework using RL with verifiable rewards (RLVR) and graph-based structural generation, directly targeting on-policy distillation and RL for LLM optimization modeling.

**摘要**: arXiv：2606.26578v1宣布类型：新摘要：使用大型语言模型（LLM）从自然语言自动化优化建模面临两个关键挑战。首先，培训库缺乏结构多样性。其次，数据生成管道保持静态并且与模型学习脱钩。为了应对这些挑战，我们提出了EvoOptimShape，这是一个新颖的框架，数据和模型在模型弱点的驱动下共同进化。EvoOptimShape将每个混合整线性规划（MILP）表示为属性二分图，并应用有效性保持进化操作符来生成结构多样的实例。通过确定性编译和验证的反向翻译，进化出的图形被转换为求解器代码和自然语言。训练分两个阶段进行：对初始数据集进行监督微调（SFT），然后是具有可验证奖励的强化学习（WLVR），其中图形派生的弱点信号引导针对模型失败的新实例的生成。这形成了一个不断更新训练分布的闭环。对六个公共数据集的经验结果表明，EvoOptimShape在准确性、可执行性和概括性方面显着优于更大的通才模型、代理方法和专业基线。这些结果表明，有针对性的数据模型协同进化是改进LLM优化建模任务的有效策略。

[阅读原文](https://arxiv.org/abs/2606.26578)

---

## 4. 红色女王G ' odel机器：共同进化的代理人及其评估者

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Alex Iacob, Andrej Jovanovi\'c, William F. Shen, Daniel Burkhardt, Meghdad Kurmanji, Nurbek Tastan, Lorenzo Sani, Niccol\`o Alberto Elia Venanzi, Ambroise Odonnat, Zeyu Cao, Bill Marino, Xinchi Qiu, Nicholas D. Lane

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces an evolutionary framework for recursive self-improvement with non-stationary utilities, directly advancing on-policy distillation and RL for LLMs via co-evolving agents and evaluators.

**摘要**: arXiv：2606.26294v1宣布类型：新摘要：自我改进代理是基于代理编码基准的最新技术（SOTA），最近已扩展到一般领域。然而，他们的搜索方法通常假设一个稳定的评估标准：固定的验证器、基准或标记的数据集，随着代理改进而保持有效。这忽视了进化的一个核心特征：物种随着环境的变化而适应。我们的目标是将相同的原则引入到循环自我改进中，使评估成为改进循环的一部分，并向不断发展的评估者、对抗性目标和可能超越静态基准的动态效用开放搜索。我们介绍了红皇后戈德尔机（RQGM），这是一个在非静态公用事业下进行循环自我改进的进化框架。RQGM通过受控效用演变使这一点成为可能：搜索被组织为具有固定期内评估标准的时期，而效用可以在时期边界更新，因此随着目标在各个时期的演变，每个时期的自我改进保证都成立。我们首先表明，即使在可验证的编码任务中，RQGM也通过添加补充的代理作为法官代码审查信号来提高测试通过率。该信号更便宜，并且RQGM使用的代币减少了1.35x-1.72x。然后，我们转向科学论文写作和审查，以及奥运会级别的证明写作和评分，其中RQGM比之前的自我改进代理提高了性能：在多元化代理人作为评委小组的情况下，共同进化的作家的接受率提高了1.78倍-1.86倍，而共同进化的评分者的真实准确率提高了9%。在论文评审中，最强的基线评审员对人工智能生成论文的过度接受率高达人类的1.91倍。RQGM通过引入对抗性目标来纠正这一点，该目标发现审查者对人工智能和人类工作同样严格。

[阅读原文](https://arxiv.org/abs/2606.26294)

---

## 5. 将RL诱导的工具使用本地化到单个交叉器特征

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Andrii Shportko, Shubham Bhokare, Ahmed Zeyad A Alzahrani, Bowen Cheng, Gustavo Mercier, Jessica Hullman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Dedicated Feature Crosscoders to isolate and steer RL-induced tool-use features in LLMs, enabling retraining-free behavioral control and capability spillover.

**摘要**: arXiv：2606.26474v1宣布类型：新摘要：通过RL进行的微调重塑了语言模型的内部表示，以实现工具使用等代理行为，但人们对这些变化的机械基础仍然知之甚少。虽然RL极大地改进了结构化工具调用的生成，但目前尚不清楚哪些功能会出现、哪些被保留，以及是否可以利用已识别的功能进行无重新训练的行为控制。在这项工作中，我们表明$\texttit {Dedicated Performance Crossscoders（DFC）}$隔离了一组紧凑的RL特定功能，这些功能在$\textttt {Qwen2.5-3B}$中调节工具调用能力。在价值48美元的交叉scoder超参数扫描中，编码-解码重建将RL模型的工具正确性提高了$+31.1 \PM {9.7}$ pp，并将工具调用能力被动地转移到冻结基础模型，增加了$+6.8 \PM 5.0$ pp，我们称之为a $\textit{能力溢出}$。我们的研究结果表明，DFC分区将RL引入的能力集中到最小的、可操纵的特征集中，从而实现代理LLM的运行时行为控制。

[阅读原文](https://arxiv.org/abs/2606.26474)

---

## 6. 验证地平线：没有银弹的编码代理奖励

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Binghai Wang, Chenlong Zhang, Dayiheng Liu, Jiajun Zhang, Jiawei Chen, Mouxiang Chen, Rongyao Fang, Siyuan Zhang, Xuwu Wang, Yuheng Jing, Zeyao Ma, Zeyu Cui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a deep analysis of verification challenges for coding agent rewards, proposing a framework for reward design that must co-evolve with policy capability, directly relevant to RL for LLMs.

**摘要**: arXiv：2606.26300v1宣布类型：新摘要：经典直觉认为验证解决方案比产生解决方案更容易。对于今天的编码代理来说，这种直觉正在被颠倒：随着基础模型发展出更强的推理能力和工程工具变得更加复杂，生成复杂的候选解决方案不再困难--可靠地验证它们已成为更困难的问题。我们可以构建的每个验证器都只是人类意图的代理，而不是意图本身。这使得验证面临双重困难：首先，意图本质上未指定，因此本质上很难忠实地检查它是否已实现;其次，在模型训练期间，优化扩大了代理和意图之间的差距--表现为奖励黑客攻击或信号饱和。为了解决这个问题，我们从三个维度（可扩展性、忠实性和稳健性）来描述验证信号的质量，并认为同时实现这三个维度是核心挑战。我们进一步研究了四种奖励结构：通用编码任务的测试验证器、前端任务的标题验证器、作为现实世界代理任务验证器的用户以及长期任务的自动代理验证器。我们针对不同的任务类型和政策能力水平，对奖励设计的核心挑战以及如何更有效地利用奖励信号进行深入分析和实验。实验表明，有针对性的验证设计可以有效抑制奖励黑客攻击，提高任务完成质量，并在多个内部和公共基准上取得显着收益。这些经验共同指出了一个核心观察：随着政策能力的不断增强，没有固定的奖励功能可以保持有效;验证必须与生成者共同进化。

[阅读原文](https://arxiv.org/abs/2606.26300)

---

## 7. 没有基本真相解决方案的强化学习可以改善LLM

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang, Xunpeng Huang, Kun Zhou, Tongtong Liang, Zhewei Yao, Yi-An Ma, Yuxiong He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RiVER, a novel RL framework for LLMs that uses calibrated continuous rewards from score-based tasks without ground-truth solutions, addressing scale and frequency dominance, and shows transfer to exact-solution benchmarks.

**摘要**: arXiv：2606.27369v1宣布类型：新摘要：用于训练LLM的具有可验证奖励的强化学习（WLVR）通常依赖于基本真相答案来分配奖励，从而限制了其对基本真相解决方案未知的任务的适用性。我们引入了一个\textBF{R}anking-\textBF{i}nduced \textBF{PER} ifable框架（RivER），该框架在没有基本事实解决方案的情况下训练LLM进行基于分数的优化任务，使用确定性执行反馈作为连续值监督。当将群体相对RL应用于此类连续奖励时，我们确定了两个关键挑战：\{规模主导地位}，测试实例之间未校准的得分幅度扭曲了政策更新，以及\{频率主导地位}，重复采样的次优解决方案可能会超过罕见但更强大的候选者。RivER通过校准的奖励塑造来应对这些挑战，该塑造使用实例级比较，并强调排名最高的求解者，同时保留对其他有效解决方案的有限反馈。我们训练12个AtCoder启发式竞赛任务，并评估算法工程基准（ALE-Bench）、LiveCodeBench和USACO。River在ALA评级排名中将Qwen 3 -8B和GLM-Z1- 9 B-0414提升了8.9%和9.4%。更重要的是，尽管仅针对基于分数的任务进行培训，而没有任何基本事实解决方案，但RivER也提高了LiveCodeBench和USACO等精确解决方案基准的主干，绝对平均改进幅度为2.4%和3.5%。相比之下，用原始执行分数训练的基线可以提高ADE评级，但无法转移到精确解决方案基准。这些结果表明，基于分数的优化任务与适当的奖励校准相结合，可以作为一般编码能力的有效训练环境，而无需基本真相解决方案。

[阅读原文](https://arxiv.org/abs/2606.27369)

---

## 8. 当您压缩边缘的回归推理器时，什么会幸存下来？

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Pearse Jim, Steven Kolawole, Opegbemi Matthias Busoye, Glory Bagai, Virginia Smith

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Investigates how aggressive compression destroys global reasoning in recursive (latent) reasoners and proposes per-channel calibrated INT4 to recover it, directly addressing latent reasoning efficiency.

**摘要**: arXiv：2606.26488v1宣布类型：新摘要：回归推理模型可以通过重复更新潜在状态来解决仅具有数百万个参数的复杂结构化任务。在边缘硬件上部署这些模型需要大量压缩，但与传统序列模型不同的是，量化错误跨循环而不是跨输出令牌复合。因此，关于压缩的标准直觉并不适用。在这项工作中，我们询问当压缩循环推理器时，什么会幸存下来。在全精度扫描、三个任务和两种迭代架构中，我们发现激进压缩保留了局部预测，但破坏了全局推理：在天真的INT 4修剪、蒸馏和线性注意力下，单元准确性保持不变，而谜题精确准确性则降至零。令牌级目标，包括量化感知训练，无法修复它。崩溃是架构性的--它会打击ML混合回归，但不会关注同一任务--我们使用按通道校准的INT 4来扭转它，而无需重新训练。我们还引入了运载轨迹保真度（与全精度推理路径的cos相似性）作为无标签信号，可以在任务评估之前预测这种损害及其恢复。合并后的结果是一个部署方案：闪存流嵌入消除了99.4MB的瓶颈，一个周期内的INT 8以减少6倍的FLOP（8 MB SOC）匹配全深度准确性，校准后的INT 4适合4 MB微控制器。

[阅读原文](https://arxiv.org/abs/2606.26488)

---

## 9. GEOALIGN：稳健的LLM强化学习的几何推出方案

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ting Zhou, Zhenqing Ling, Yiyang Zhao, Ying Shen, Daoyuan Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a geometric rollout curation method for online LLM RL that detects and rectifies directionally inconsistent rollouts, improving training stability and final performance.

**摘要**: arXiv：2606.26917v1宣布类型：新摘要：在线强化学习被广泛用于将大型语言模型（LLM）与奖励信号对齐，但在有噪音或错误指定的奖励下，训练可能会不稳定。我们识别了一种失败模式，我们称之为方向不一致：在一个批次内，一小群高回报推出会引发与批次多数严重不一致的代表空间偏好方向，从而导致高方差和不稳定的更新。我们提出了geoalign，这是一个轻量级插件，用于迭代策略优化中的部署策展。Geoign（i）形成提示内偏好对，（ii）在每次展开隐藏状态上学习在线投影仪以集中奖励有序的位移方向，以及（iii）通过其与批量共识原型的角度偏差来检测方向不一致的展开，并使用提示内稳定的替代方案来纠正它们。Geoign仅向前传递，增加了可忽略不计的管理费用。通过与学习奖励模型的对话协调以及与二元验证奖励的数学推理，Geotify提高了最终性能并减少了训练振荡，优于PF-PPO、VAR、PODS和Seed-GRPO。这些结果表明潜在的方向共识是在线LLM RL的有效可靠性信号。

[阅读原文](https://arxiv.org/abs/2606.26917)

---

## 10. OPID：针对抽象强化学习的政策上技能提炼

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuo Yang, Jinyang Wu, Zhengxi Lu, Yuhao Shen, Fan Zhang, Lang Feng, Shuai Zhang, Haoran Luo, Zheng Lian, Zhengqi Wen, Jianhua Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes OPID, an on-policy skill distillation framework that extracts hierarchical skill supervision from completed trajectories to provide dense token-level advantages for RL-based language agents.

**摘要**: arXiv：2606.26790v1宣布类型：新摘要：基于结果的强化学习为语言代理提供了稳定的优化支柱，但其稀疏的强化级奖励几乎没有提供关于应该加强或抑制哪些中间决策的指导。政策上的自我提炼提供了密集的代币级监督，但现有的技能条件变体通常依赖于外部技能记忆或检索到的特权上下文，这些变体的维护成本很高，并且可能与当前政策在多轮互动中引发的状态分布不匹配。我们提出了\textbf{OPID}（\textbf{O}n-\textbf{P} policy Sk\textbf{i}ll \textbf{D}istillation），这是一个直接从已完成的策略轨迹中提取技能监督的框架。OPID将轨迹后见之明表示为分层技能：情节级技能捕获全局工作流程或故障避免规则，而步骤级技能捕获关键时间步的本地决策知识。关键优先路由机制在识别关键决策时使用步骤级技能，否则回退到情节级技能作为默认指导。选定的技能被注入到交互历史中，允许旧策略在原始和技能增强的上下文中对相同的采样响应重新评分。由此产生的对数概率偏移产生了令牌级自蒸馏优势，该优势与策略优化的结果优势相结合。因此，OPID保留RL作为主要训练目标，同时引入密集的，分布匹配的事后监督。在ALFWorld、WebShop和基于搜索的QA上的实验表明，OPID通常可以提高代理性能、样本效率和鲁棒性，而不仅仅是结果RL和现有的技能蒸馏基线。我们的代码可在https://github.com/jinyangwu/OPID/tree/main上获取。

[阅读原文](https://arxiv.org/abs/2606.26790)

---

## 11. 铺设真实意图：意图感知培训提高了整个培训方案的LLM安全等级

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jeremias Ferrao, Niclas M\"uller-Hof, Iustin S\^irbu, Traian Rebedea, Yftah Ziser

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes intent-aware training for safety classifiers using GRPO to reward intent faithfulness, directly contributing to RL for LLMs with a novel reward design.

**摘要**: arXiv：2606.27210v1宣布类型：新摘要：我们认为，安全分类器应该将用户意图建模为提示和最终标签之间的明确信号。为了研究这一点，我们引入了AIMS，这是一个由1，724个困难的安全提示组成的人工注释数据集，每个提示都与意图描述和危害标签配对。我们使用AIMS来评估监督微调，偏好学习，推理蒸馏和强化学习的意图感知训练。尽管AIMS的规模很大，但它能够在整个训练体系中实现有竞争力的安全分类器：来自模型生成的意图错误的DPO优于SFT，并且在大多数师生对中，意图条件蒸馏优于仅推理蒸馏。最值得注意的是，用GRPO直接奖励意图忠诚度在五个外部安全基准中产生了最强的平均性能，而我们的意图感知模型则形成了推理潜伏期-F1帕累托前沿。这些结果表明，忠诚的意图建模是更稳健的安全分类器的紧凑、高质量的监督信号。

[阅读原文](https://arxiv.org/abs/2606.27210)

---

## 12. NebulaExp-8B：通过全规模消融研究的经验性训练后管道

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qiaobo Hao, Yangqian Wu, Shunyi Wang, Zhongjian Zhang, Ziqun Li, Yayin He, Muqing Li, Chen Zhong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Presents a fully transparent post-training pipeline for 8B LLMs with GRPO RL and a novel multi-teacher on-policy distillation (MOPD) method that outperforms RL on instruction following.

**摘要**: arXiv：2606.26671v1宣布类型：新摘要：训练后对齐决定了遵循大型语言模型能力的推理和人类偏好，但大多数现有作品保留了详细的数据构建、过滤规则和训练食谱，这阻碍了社区可重复性和轻量级模型优化。这项工作提出了NebulaExp，这是一个基于Qwen 3 - 8B-base的完全透明、烧蚀驱动的后培训管道，涵盖两个垂直模型分支：一般指令模型和复杂推理专用模型。我们策划了由384万个多源SFT样本和20万个可验证的RL候选池组成的原始数据库，并设计了一个端到端的数据处理栈，包括响应蒸馏、多维交叉验证过滤、细粒度难度分级、任务分类和多样性感知采样。对于Direct分支，我们的三阶段优化监督微调方法NebulaExp-Ins-SFT将平均基准得分从Qwen 3 - 8B-nothink的55.01基线提高到60.99。然后，GRPO强化学习将平均分进一步提高到61.85。对于推理分支，中等难度的GRPO RL将平均推理分数从73.88提高到75.17。为了解决RL对任务验证器的依赖性问题，我们系统地研究了单教师和多教师OPD（MOPD）：仅利用4K遵循教学的样本，在IFEval上比RL基线高出3.26分，平均总收益+4.43; MOPD仅用10 K样本融合了四位领域专家教师，使平均表现比基本模型提高了4.18。该报告为8B规模LLM提供了完全可复制的经验训练后配方，并全面剖析了指令遵守性、数学推理、代码生成和常识之间的能力权衡。

[阅读原文](https://arxiv.org/abs/2606.26671)

---

## 13. 设计可移植查询生成的奖励信号：工业语义职位搜索的案例研究

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ping Liu, Qianqi Shen, Jianqiang Shen, Wenqiong Liu, Rajat Arora, Yunxiang Ren, Chunnan Yao, Dan Xu, Baofen Zheng, Wanjun Jiang, Andrii Soviak, Kevin Kao, Jingwei Wu, Wenjing Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RLAIF framework with a deterministic reward floor to mitigate reward hacking in query generation, directly contributing to RL-for-LLMs with a new reward design and analysis of optimizer sensitivity.

**摘要**: arXiv：2606.27291v1宣布类型：新摘要：职位搜索平台依赖于低带宽查询界面，而这些界面通常无法捕捉候选人个人资料的多维复杂性。我们提出了一个端到端RLAIF（来自AI反馈的强化学习）框架来生成\{portable}职位搜索查询，这些术语可以抽象出特定于搜索者的标识符，同时保留可概括的资格。这项任务引入了高度对抗性的奖励表面，其中政策优化经常利用法学硕士作为法官的标题中的缺陷，导致退化的逐字逐句复制行为。   我们进行了全面的实证实验，以隔离优化机制对结构性奖励工程的影响。我们的结果表明，对于无批评优化器来说，性能绝大部分取决于稳健的奖励塑造，这使得算法的具体选择在很大程度上并不重要。虽然每次推出时无批评的基线方法（RLOO和REINFORCE++）天生抵制奖励黑客，但GRPO中的群体相对优势规范化似乎对虚假奖励信号特别敏感，使其不成比例地容易受到剥削。我们表明，引入确定性、基于规则的奖励下限来纠正分配给逐字复制的奖励可以缓解这种失败模式，从而使跨家庭评估法官的质量大幅提高+0.147美元。最终，我们表明，培训时奖励模型将绩效收益增加了2.4美元，证实培训的成功从根本上取决于执行奖励塑造纪律，而不是选择替代优化器。

[阅读原文](https://arxiv.org/abs/2606.27291)

---

## 14. 推理质量早期出现：推理模型的数据修复

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari, Carlos Morato, Baharan Mirzasoleiman

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a data curation method for reasoning models that identifies high-quality SFT examples using only initial reasoning tokens and perturbed checkpoints, achieving strong efficiency gains.

**摘要**: arXiv：2606.26797v1宣布类型：新摘要：对一组小而高质量的长推理痕迹进行监督微调（SFT）是在大型语言模型（LLM）中激发强大推理能力的有效方法。然而，管理高质量SFT数据的现有方法严重依赖于强推理模型来根据多样性和难度过滤示例，这使得管理过程成本高昂，同时往往产生次优的数据质量。在这项工作中，我们表明，仅使用初始推理标记就可以识别多样化且具有挑战性的推理示例。具体来说，我们证明，可以根据在预训练模型的随机扰动检查点处评估的前100个推理令牌的丢失来可靠地检测困难的问题。我们进一步表明，在沿着微调轨迹外推的少数受干扰检查点上，在其前1 k个推理标记上表现出类似的损失模式的示例可以证明会引发类似的梯度。我们通过在M23 K医学推理和OpenKnights-Math数据集上微调Qwen 2.5 - 7 B和Llama3.1-8B模型的广泛实验来验证我们的方法。我们的方法比现有基线高出1.7%，同时代币效率提高了91%。

[阅读原文](https://arxiv.org/abs/2606.26797)

---

