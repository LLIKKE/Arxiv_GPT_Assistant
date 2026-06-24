# 💡 今日研究速览 (Daily Summary)

# LLM的强化学习
当今的主导主题是LLM基于RL的培训的成熟，超越简单的奖励设计，解决核心算法和实践挑战。几篇论文解决了 **数据陈旧下的政策提炼的关键问题**。AsyncOPD首次对该问题进行了系统性研究，证明谨慎的估计器选择可以保持准确性，同时显着提高训练吞吐量。作为补充，分块策略漂移门控机制提供了一种轻量级的、仅限学生的解决方案，可以在重复使用推出数据时控制漂移，从而直接改进数学推理。除了提炼之外，新的奖励设计正在出现：用于自我改进的人工智能的正式验证的法律奖励信号和用于视频基础的语义证据奖励（BER）都展示了如何构建更具原则性、可验证或语义一致的奖励功能。EXPO-SQL的细粒度条款级奖励和PointVG-R中视觉推理的自适应重要性加权进一步扩展了这一趋势。最后，摆脱自我确认陷阱和有益模型的持续对齐的工作凸显了对RL训练中稳健性和概括性的日益关注，使该领域朝着更可靠和更广泛适用的RL for-LLM方向发展。

# 推理和推理
一个迷人的新方向正在出现，将LLM推理框架为**吸引子动力学或潜在检索**的一种形式。关于“作为吸引力动力学的推理”的论文提出了推理轨迹的吉布斯加权能量最小化，将推理视为收敛到稳定潜在状态的过程。这种机械论观点得到了用于多模式推理的伊娃框架的补充，该框架引入了连续潜在老虎机令牌和新颖的D-GSPO优化来解决潜在推理中的策略偏差。总而言之，这些作品表明从纯粹的代币级自回归推理转向更结构化的潜在空间推理过程，从而可以提供效率和稳健性的好处。战略引导的政策优化（SGPO）论文通过用可重复使用的策略蒸馏取代轨迹模仿，进一步支持了这一趋势，在更高、更抽象的层面上有效指导模型的推理过程。

# 代理和工具使用
RL和代理系统的交叉正在见证重大创新，特别是在**自主评估和体验学习**方面。计算机使用代理的框架通过使用基于有噪的VLM的自主评估和经过噪音纠正的PPO估计器来直接解决奖励信号瓶颈，展示了在复杂的交互环境中扩展RL的实用路径。同时，用于代理人体验学习的Executie-Distill-Verify范式通过引入多代理人蒸馏和共识验证来解决自我确认偏差的关键问题，确保代理人从多样化的、经过验证的经验中学习，而不是强化自己的错误。这些工作代表着构建能够从自己的交互中稳健学习而无需昂贵的人类注释的代理的关键一步。

# 多模式和视觉语言模型
多模式推理正在通过**接地、可验证的奖励信号**来推进。用于视频基础的语义证据奖励（BER）用判断语义对齐的裁判VLM取代了传统的几何IoU，直接改进了视频MLLM中的时空推理。同样，PointVG-R将几何推理集成到MLLM中，以实现精确的指向定位，使用具有自适应重要性加权奖励的RL来内化视觉思维链推理。这两种方法都表现出了一个明显的趋势：超越简单的匹配或分类奖励，转向更具语义意义、结构上知情的奖励设计，可以指导复杂的多模式推理任务。

# 健壮性和对齐
一个关键的焦点是**提高LLM对病理输入和分布变化的鲁棒性**。“Pigeonholing”论文确定并解决了一种特定的故障模式，即错误提示导致模型崩溃到错误状态，提出了带有合成错误的RLVR来缓解这一问题。这是由广泛和持久的有益模型的工作，它使用现实情况的数据集，以加强有益的性状，证明对齐可以概括出的分布在广度和持久性。这些论文共同标志着人们日益成熟的理解，即一致性和稳健性不仅是为了避免有害输出，而且是为了确保在广泛的输入和上下文（包括对抗性或不寻常的输入和上下文）中可靠、一致的行为。

---

## 1. AsyncOPD：政策上的蒸馏能有多陈旧？

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Wonjun Kang, Kevin Galim, Seunghyuk Oh, Minjun Kang, Sanghyun Park, Donghoon Kim, Minjae Lee, Minseo Kim, Rishabh Tiwari, Yuchen Zeng, Hyung Il Koo, Kangwook Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: First systematic study of staleness in asynchronous on-policy distillation for LLMs, proposing AsyncOPD with estimator choices that improve throughput while maintaining accuracy.

**摘要**: arXiv：2606.24143v1宣布类型：新摘要：按政策蒸馏（OPD）在教师反馈的指导下对学生进行自己的推出培训，并且对于大型语言模型（LLM）后培训变得越来越重要。然而，与强化学习（RL）一样，OPD也面临着政策上的系统瓶颈，因为展开可能会主导推理工作负载的训练时间。同步训练管道可以通过将推出生成与学习器更新分离来缓解这一瓶颈，但这样做会引入停滞策略数据。虽然之前的工作研究了同步RL中的陈旧数据，但其对OPD的影响仍然没有得到充分的研究。我们首次对非同步OPD中的陈旧性进行了系统性研究，重点关注通过本地KL损失实现教师反馈的实际环境，并且全词汇量教师日志存储或传输成本太高，因此需要有限的教师分数缓存。我们首先表明KL方向改变了陈旧数据问题：教师加权的正向KL对陈旧推出更稳健，而学生加权的反向KL则很脆弱。其次，对于这种脆弱的反向KL情况，我们研究旨在稳定非同步RL的方法是否可以减轻OPD的陈旧性。在我们的实验中，它们并没有比更简单的OCD特定替代品有所改进：在学习时间在当前学生下重新计算反向KL信号。第三，我们分析有限的教师分数缓存如何为稀疏和采样反向KL OPD估计器创建偏差方差权衡。这激发了多样本蒙特卡罗（MC），它保留了MC的可纠正性，同时减少了单样本方差。最后，我们提出并开源了AsyncOPD，这是一个完全异步的OPD训练管道，由这些估计器选择构建。实验表明，AsyncOPD提高了1.6\times $到3.8\times $严格的同步训练的训练吞吐量，同时达到相当的准确性。

[阅读原文](https://arxiv.org/abs/2606.24143)

---

## 2. 高效多模式推理的潜在视觉状态

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xiuwei Chen, Wentao Hu, Yongxin Wang, Zisheng Chen, Likui Zhang, Kun Xiang, Jianhua Han, Hui-Ling Zhen, Jingyuan Zou, Hang Xu, Xiaodan Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EVA, a framework for latent visual reasoning via continuous latent slot tokens and a novel D-GSPO optimization to address policy deviation, directly advancing latent reasoning for multimodal models.

**摘要**: arXiv：2606.24233v1宣布类型：新摘要：视觉证据的集成显着增强了大型多峰模型的能力。然而，这种集成主要依赖于生成离散输出（等，代码或框坐标）来调用外部工具，这是一个引入严格依赖关系和大量延迟的过程。为了克服这些限制，我们提出了{伊娃}（LatEnt Visual StAtes），这是一种新颖的框架，可以本地生成连续的潜在视觉表示。这些内部表示表现为潜伏\_老虎机令牌的自适应序列，在推理过程中充当中间视觉思想。然后使用离散文本令牌对这些潜伏\_老虎机令牌进行端到端训练。值得注意的是，这种协同优化会导致潜伏\_老虎机代币之后的“过渡窗口”中出现极端的政策偏差。我们开发了D-GSPO（Decouple-GSPO），通过脱钩潜在组件和离散组件的优化来解决这一根本原因。为了支持SFT，我们构建了伊娃-230 K，这是一个高质量的文本-图像交织CoT数据集，涵盖各种现实世界场景、文档、图表和OCR任务。跨多个基准的广泛实验证实，伊娃在提高推理效率的同时实现了显着的性能提升。

[阅读原文](https://arxiv.org/abs/2606.24233)

---

## 3. 超越轨迹模仿：LLM推理的策略引导策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianyuan Shi, Canbin Huang, Bei Li, Xin Chen, Xiaojun Quan, Jingang Wang, Qifan Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SGPO, a strategy-guided on-policy distillation method that replaces trajectory imitation with reusable strategy distillation using forward-KL and adaptive weighting, directly improving LLM reasoning.

**摘要**: arXiv：2606.24064v1宣布类型：新摘要：从强到弱语言模型提炼推理能力通常涉及模仿特定的解决方案轨迹，有效地转移要回答的内容而不是如何推理。这种教室级的模仿鼓励记忆特定于实例的步骤，而不是获得可转移的解决问题的技能，从而限制了对新问题的概括。我们提出了策略引导的策略优化（SGPO），它用可重复使用的策略提炼取代实例级轨迹模仿。SGPO从强模型响应中提取结构化策略描述，并针对每个问题构建自主和战略指导轨迹，以便能够直接比较有和没有战略指导的模型行为。然后，该框架解决了两个关键问题。对于如何提炼，代币级的向前KL目标有选择地将战略条件引发的分配转变转移到无指导的政策中，并以近端约束确保稳定性。对于何时提取，自适应实例级加权在自主探索不足时加强指导，并随着模型自身能力的增强而减少指导。对两个模型系列的四个数学基准进行的实验表明，SPO始终优于SFT、政策上RL和混合政策基线，比Qwen 2.5 - 7 B-Direct上的最强基线提高了2.2个百分点。分析表明，前向KL目标提供了一种优于直接轨迹模仿的内在选择性蒸馏信号，并且策略蒸馏表现出与基本模型能力的互补扩展。

[阅读原文](https://arxiv.org/abs/2606.24064)

---

## 4. 离线推理训练的权空间几何

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Aleksandr Nikolich, Igor Kiselev, Vladimir Platonov, Karina Romanova

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a mechanistic analysis of weight-space geometry for offline RL losses (RFT, RIFT, DFT, Offline GRPO, DPO) used in reasoning distillation, revealing distinct update directions and accuracy trade-offs.

**摘要**: arXiv：2606.23740v1公告类型：新摘要：离线学习损失（RFT，RIFT，DFT，离线GRPO，DPO）被广泛用于从大型教师到较小学生的推理，并且通常仅在下游准确性上进行比较。我们问他们是否是机械不同或收敛到一个类似的权重更新。从具有仅注意力LoRA的单基础模型（Qwen 3 - 4 B）中训练六种方法（SFT、RFT、FT、FT、离线GRPO、DPO），我们通过cos相似性、主角子空间分析、线性模式连接性和CKA来分析产生的增量。我们观察到：（i）SFT、RFT和Rift具有几乎共线的权重增量（cos>= 0.97，顶部1原色~ 144个模块中中位数7 °）和相当的GSM 8 K准确度（87- 88%，n=1319;成对McNemar p >= 0.15）;（ii）尽管使用相同的数据，但与任何奖励加权方法相比，FT在方向上的分歧更大;（iii）离线GRPO添加了与SFT方向垂直的大量分量（全球约67%，后期层高达约86%），同时留在SFT损失盆地;（iv）DPO位于近垂直的子空间中，显示出模式连通性障碍，并将后期CKA坍缩至~0.46。DPO还在GSM 8 K上达到了我们协议中的最高准确性（93.5%，McNemar p < 10 -9与其他方法相比）和AIME 26（30.0% vs 3.3-10.0%）;其训练使用的学习率比其他训练低10倍（标准惯例），因此更新规范和准确性差距共同反映了损失函数和优化器的选择，学习率匹配的DPO比较留给未来的工作。

[阅读原文](https://arxiv.org/abs/2606.23740)

---

## 5. 闭环：正式验证的法律作为自我完善法律人工智能的奖励信号

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Armin Heydari (Harvard University), Torben Leowald (Columbia University)

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a closed-loop RL training architecture for legal AI using a formally verified reward signal from autoformalized law, directly matching RL-for-LLMs with a novel verifier-driven reward design.

**摘要**: arXiv：2606.23913v1宣布类型：新摘要：本文开发了一个架构，该架构创建了一个可正式验证的奖励信号来训练法律人工智能，适应LLM的建议，验证者将范式从数学人工智能处理到法律的独特要求。我们提出了一个架构，包括LLM驱动的自动形式化到扩展Catala的形式法律演算、验证核心和基于形式证明痕迹的解释生成。对于法律的计算组成部分，该架构提供了可证明的正确性。对于开放结构的法律分析，它提供了结构性保证：法律论证的每个必要阶段都得到解决，论证在正确的阶段进行且不省略，并且步骤之间的演绎联系是有效的。我们展示了德国法律中的程序截止日期计算、美国宪法中的商务条款分析以及跨司法管辖区制裁相称性的架构。我们进一步表明，相同的架构对于法律人工智能培训具有结构性优势：确定性的外部验证器为法律问题提供可验证的结果，从而缩小法律中传统的强制学习循环差距。

[阅读原文](https://arxiv.org/abs/2606.23913)

---

## 6. 作为吸引力动力学的推理：通过吉布斯加权能量最小化的潜在记忆检索

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Kanishk Awadhiya

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent reasoning retrieval mechanism using Gibbs-weighted energy minimization over reasoning trajectories, treating LLM inference as attractor dynamics.

**摘要**: arXiv：2606.24543v1宣布类型：新摘要：大型语言模型（LLM）传统上被视为自回归生成器。然而，从集体计算的角度来看，它们充当多维密集联想记忆，将复杂的推理模式作为潜在吸引子存储。在这项工作中，我们研究了数学推理的能量格局。我们推测，正确的推理链对应于模型输出分布中深、宽的吸引子盆地（“平坦极小值”），而幻觉则表现为尖锐、不稳定的局部极小值。为了利用这种几何形状，我们引入了一种基于轨迹谱熵的吉布斯测量的检索机制。通过对多个推理路径进行采样并根据其逆能量对其加权（$P \propto e '''{\r-\Beta E}$），我们逼近联想记忆的平衡分布，从而有效地“放松”系统到鲁棒的解决方案。从经验上看，这种受物理启发的机制将GSM 8 K上的Microsoft Phi-3.5性能提高了5.38%（84.7%至90.1%），这表明推断可以更好地建模为进入吸引子盆地的动态沉降过程，而不是贪婪的下一个令牌预测。

[阅读原文](https://arxiv.org/abs/2606.24543)

---

## 7. 政策上蒸馏的模糊政策漂移门控

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Liwen Zheng, Haiyun Jiang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces blockwise policy-drift gating, a lightweight student-only drift controller for on-policy distillation under rollout reuse, improving solve-rate on math reasoning benchmarks.

**摘要**: arXiv：2606.24084v1宣布类型：新摘要：政策蒸馏（OPD）使用根据学生本身采样的轨迹计算的教师信号来训练学生政策。最近的工作表明，采样令牌OPD在长期推理任务中可能很脆弱，而本地教师支持匹配是一种简单有效的修复方法。本文介绍了分块策略漂移门控，这是一种轻量级的仅限学生的旧电流漂移控制器，用于OPD，可在部署重复使用下使用。该方法计算采样令牌路径上的行为学生和当前学生之间的log概率漂移，在固定块或跨度上汇总这些漂移，并使用产生的分离的均值正规化门来重新加权OPD位置损失。它不会改变教师目标、教师Top K支持或推出政策。在六变体Qwen 3数学推理基准中，所有训练变体都有统一的200步训练预算，我们使用pass@8作为主要问题级解决率指标。修复64个令牌块门控将AIME 24、AIME 25、PATH 500和AMC 23的采样令牌OPD平均传递@8从0.4978提高到0.5160。在Teacher-TopK/LSM上，Block 64在训练有素的学生中提供了最好的四个基准平均通过率@8。结果将局部旧当前策略漂移识别为可重复使用的OPD部署的实际控制信号，并激励块级门控作为提高解决率稳健性的简单默认值。

[阅读原文](https://arxiv.org/abs/2606.24084)

---

## 8. BER：学习使用语义证据基础视频推理奖励

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sheng Xia, Zhengqin Lai, Tianxiang Jiang, Kanghui Tian, Shoujun Zhou, Bin Li, Yi Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel Semantic Evidence Reward (SER) for RL-based fine-tuning of video MLLMs, using a referee VLM for semantic alignment instead of geometric IoU, directly improving spatio-temporal reasoning grounding.

**摘要**: arXiv：2606.24726v1宣布类型：新摘要：视频MLLM经常难以应对细粒度的时空推理，有时会基于不相关的帧或对象生成正确的答案。尽管在推理过程中输出时空证据是一个有前途的方向，但现有的RL框架通常依赖于纯几何（IoU）奖励，这可能对边界扰动敏感并忽视了语义对齐。为了解决这个问题，我们提出了语义证据奖励（BER），它将时空证据基础重新定义为受约束的验证任务。BER没有计算像素级重叠，而是使用裁判VLM作为本地检查器来评估模型生成的证据声明，跨越两个维度：相关性和本地化质量，结合时间惩罚。该设计减少了对密集框注释的依赖，并允许直接在标准视频QA数据上进行训练。在V-STAR基准测试中，BER达到了49.6%的mLGM，比基于证据的强基线Open-o3-Video提高了3.0个百分点，证明了其在提高答案准确性和证据基础方面的潜力。

[阅读原文](https://arxiv.org/abs/2606.24726)

---

## 9. 具有自主评估的计算机使用代理的强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Marta Sumyk, Oleksandr Kosovan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an RL fine-tuning framework for computer-use agents that uses noisy VLM-based autonomous evaluation as a reward signal, with a noise-corrected estimator for PPO.

**摘要**: arXiv：2606.24515v1宣布类型：新摘要：计算机使用代理（CUA）通过直接在图形用户界面内感知和行动来执行高级用户目标。然而，CUA的强化学习仍然很困难，因为开放式桌面环境很少提供可扩展的、机器可读的奖励信号：任务成功通常基于视觉，并且很难用手工制作的奖励功能或密集的手动标签来指定。   我们提出了一个RL微调框架，该框架使用自主视觉语言评估作为图形用户界面代理的可扩展监督信号。给定最终屏幕截图和原始指令，视觉语言模型会判断任务完成情况并在策略优化期间提供终端反馈，而无需特定任务的启发式或手动标签。   由于自主评估者并不完美，因此我们将他们的反馈建模为有噪的二元奖励通道，并为近端策略优化推导出经过噪音纠正的奖励估计器。macOS World、Windows Agent Arena和OS World的实验表明，纠正的评估者奖励优于零射击基线和原始评估者奖励，成功率比零射击性能平均提高12.6个百分点，比原始评估者微调提高5.1个百分点。这些结果表明，当评估者噪音被显式建模和纠正时，自主评估可以作为图形用户界面环境中RL的实际奖励信号。

[阅读原文](https://arxiv.org/abs/2606.24515)

---

## 10. EXPO-SQL：文本转SQL的基于执行的Clause-level策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jaehoon Lee, CheolWon Na, Suyoung Bae, Jin-Seop Lee, Jihyung Lee, YunSeok Choi, Jee-Hyong Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a fine-grained clause-level reward design for RL-based Text-to-SQL, directly improving LLM behavior through execution feedback.

**摘要**: arXiv：2606.23693v1宣布类型：新摘要：文本转SQL使用户能够通过生成可执行的SQL查询来使用自然语言查询数据库。最近的方法越来越多地采用基于大型语言模型的强化学习（RL）来利用执行反馈进行训练。然而，现有的RL方法为SQL查询中的所有条款分配统一的查询级奖励，平等地对待正确和不正确的条款。这种粗粒度的奖励设计导致学习信号不足，无法正确生成SQL。为了解决这个问题，我们提出了EXPO-SQL（基于执行的文本到SQL的条款级策略优化），它通过条款级奖励提供细粒度的监督。为了分配条款级奖励，我们的方法通过分析执行结果（包括错误消息和逐条款增量执行）来识别错误的条款。对广泛使用的文本到SQL基准测试的实验表明，EXPO-SQL通过细粒度的条款级学习显着优于现有的监督式微调、提示和基于RL的方法。我们的代码可在https：//github上获取。com/jhn25/EXPO-SQL。

[阅读原文](https://arxiv.org/abs/2606.23693)

---

## 11. PointVG-R：在MLLM中内化几何推理，通过视觉思维链进行精确指向定位

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ling Li, Bowen Liu, Zinuo Zhan, Jianhui Zhong, Ziyu Zhu, Bingcai Wei, Kenglun Chang, Zhidong Deng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a geometric reasoning pipeline for MLLMs that integrates RL with a novel adaptive importance weighting reward strategy, directly improving visual reasoning via on-policy RL.

**摘要**: arXiv：2606.24539v1宣布类型：新摘要：基于指向的视觉基础要求模型通过破译视觉场景和指向手势之间复杂的空间关系来精确定位目标对象。传统方法通常将输入图像编码为静态特征表示，并主要在语言领域内执行推理，通常忽视图像固有的丰富感知线索和显式空间几何形状。在这项研究中，我们的目标是通过提出PointVG-R（一种推理引导的多模式大型语言模型（MLLM））来减轻模型在解释手势空间关系时的认知脆弱性。PointVG-R引入了基于点的基础几何感知推理，使模型能够通过强化学习（RL）和冷启动数据的战略集成来思考图像。具体来说，我们设计了一种新颖的几何推理管道，模拟人类在解释指向手势时采用的迭代认知过程。此外，我们构建了EgoPoint-CoT，这是一个高质量的视觉思想链（CoT）数据集，具有详细的推理轨迹，通过监督微调（SFT）和RL来指导模型。为了解决训练期间遇到的学习信号质量的变化，我们进一步提出了一种基于组方差的自适应重要性加权策略，该策略动态调整奖励信号以优化学习过程。实验结果表明PointVG-R实现了SOTA性能，在mIoU中比基线高出$\textBF{15.86}$点。广泛的消融研究进一步验证了我们提出的模块的有效性。代码：https://github.com/lingli1724/PointVG-R。

[阅读原文](https://arxiv.org/abs/2606.24539)

---

## 12. 鸽子洞：不良提示会伤害模型崩溃并犯错误

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hyunji Nam, Keertana Chidambaram, Dorottya Demszky, Natasha Jaques

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RLVR with synthetic errors to mitigate pigeonholing (mode collapse from bad contexts), directly improving LLM robustness via a verifiable-reward RL pipeline.

**摘要**: arXiv：2606.24267v1宣布类型：新摘要：虽然上下文学习通常在大型语言模型（LLM）中被证明是有效的，但糟糕的上下文可能会导致性能下降和模式崩溃，我们称这种现象为“分类”。“**无意中的坏** 上下文可能会发生，而没有恶意越狱意图：例如，用户要求模型证明错误的数学定理是合理的，或者未能纠正模型的错误代码。具体来说，我们在两种情况下调查“分类”：（1）当用户建议解决方案时，以及（2）当对话上下文包括助理之前的（错误）响应时。我们对10项可验证且开放式任务和10种不同模型的实验表明，分类以多种方式表现出来：（1）根据上下文重复错误答案（导致38-40%的性能下降），（2）在编码和文本生成中集中在一组狭窄的答案上，而不探索替代方案，以及（3）在有争议的话题上改变立场，以与用户或助理之前的主张保持一致。我们发现，归类与对话回合的次数几乎单调地增加（当重复错误从1增加到5时，性能会额外下降14+%），即使提供的例子是正确的，归类引发的模式崩溃也可能发生。作为缓解措施的一步，我们提出了具有合成误差的WLVR，与普通的WLVR基线相比，在恶劣环境下可以将模型改进43-60%。

[阅读原文](https://arxiv.org/abs/2606.24267)

---

## 13. 强化学习迈向广泛和持久的有益模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Akshay V. Jagadeesh, Rahul K. Arora, Khaled Saab, Ali Malik, Mikhail Trofimov, Foivos Tsimpourlas, Johannes Heidecke, Karan Singhal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL training pipeline using a dataset of realistic situations to reinforce beneficial traits, demonstrating broad and persistent out-of-distribution alignment generalization.

**摘要**: arXiv：2606.24014v1公告类型：新摘要：随着人工智能系统部署在越来越多样化和高风险的环境中，模型对齐必须超越训练期间看到的任务和领域。这对于强化学习（RL）来说尤其重要，因为它可能会通过奖励黑客、欺骗或其他非预期策略引入意外的错位。我们研究在现实领域实例化的有益行为的RL是否可以产生超出训练分布的广泛而持久的对齐概括。我们构建了一个现实情况数据集，旨在衡量和训练有益特征，例如真实性、公平性、风险意识和可治愈性，涵盖健康、科学和教育等各个领域。然后，我们在该数据集上使用RL训练模型，并在50多个独立的对齐和有益行为基准上对其进行评估。与计算匹配的基线相比，有益特征RL提高了超过80%的分发外基准的性能。我们观察到了大量的分布外对齐转移：完全限于一个领域（健康）的日常行为RL干预对非健康对齐评估产生了广泛的改进，包括减少奖励黑客攻击、欺骗和一般失调。最后，我们研究了一致性：在试图引导模型走向不一致的情况下，行为是否保持稳健一致。用有益特征RL训练的模型表现出更好的持久性，包括对对抗性刺激和有害微调的更强抵抗力;需要进一步的工作来隔离这些影响的来源。这些结果表明，强化现实领域中的有益行为可以产生与人类繁荣更紧密一致的模型。

[阅读原文](https://arxiv.org/abs/2606.24014)

---

## 14. 摆脱自我确认陷阱：抽象体验学习的执行-提炼-验证范式

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shiding Zhu, Yudi Qi, Yajie Wang, Jiaze Li, Chao Song, Yaorui Shi, Yibo Miao, Hanqi Gao, Kai Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an Execute-Distill-Verify framework for on-policy experience learning in LLM agents, using multi-agent distillation and consensus verification to avoid self-confirmation bias.

**摘要**: arXiv：2606.24428v1宣布类型：新摘要：经验驱动的自我进化对于大型语言模型（LLM）代理通过开放世界交互进行改进至关重要。然而，现有的经验学习方法大多依赖于单代理循环，即同一代理执行任务、总结结果并确定记忆内容。这种设置使代理容易受到自我确认陷阱的影响：错误但自我一致的轨迹被错误地识别为成功的经验，从而导致检索和重用期间的累积错误。为了解决这个问题，我们提出了EDV，这是一个用于可靠体验学习的Executie-Distill-Verify框架。在执行阶段，多个异类代理并行探索相同的任务空间，以生成不同的候选轨迹。在提取阶段，专门的第三方代理会比较分析这些轨迹以产生候选体验，从而减少以执行者为中心的总结偏见。在验证阶段，执行组通过共识机制验证候选者，并且仅将批准的经验写入共享或私有内存。通过解耦这三个阶段，EDV将经验学习从孤立的自我反思转变为协作构建，在记忆插入之前过滤错误和嘈杂的内容。我们在三个具有挑战性的长期基准上评估EDV：tau 2-bench，Mind 2 Web和MMTB。结果表明，EDV始终优于强基线，验证了可靠的经验建设是必不可少的强大的代理自我进化。我们的代码可在https://github.com/shidingz/EDV上获取。

[阅读原文](https://arxiv.org/abs/2606.24428)

---

