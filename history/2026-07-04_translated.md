# 💡 今日研究速览 (Daily Summary)

# LLM的RL
该领域正在经历新颖的奖励设计和训练框架的激增，从简单的纯量奖励转向更微妙的信号。几篇论文引入了复杂的奖励结构：Maven提出了基于可编辑证据记忆的动作级奖励，以进行长上下文推理，而LABER在LVLM中使用双重奖励进行视觉注意力调节。分布稳健的列表偏好优化论文通过最坏情况的纠正推进了奖励建模的理论基础，而多角色条目生成框架通过自动化条目创建来改进WLVR。稳定性和可扩展性也是关键主题，FADE引入了自适应优势函数来动态平衡梯度权重，测谎仪监督论文显示了在偏好学习中删除人类标签的有希望的扩展趋势。这些作品共同表明LLC的RL成熟，专注于更细、稳定和自动化的奖励流程，以实现稳健的一致和推理。

# 按政策自我蒸馏
对政策上的自我蒸馏（SDPO）的重大批判性分析和完善正在进行中，揭示了其基本局限性和新颖的解决方案。Denser的论文对SDPO在持续的后期培训中的崩溃风险进行了重要分析，为三个有针对性的修复奠定了基础。纯化OPSD诊断和隔离的故障模式有关的特权信息泄漏，通过提取只有推理可转移的校正信号。DemoPSD通过教师和学生分布的不一致调制混合来解决同样的问题，以保持探索。Neuron-OPSD引入了一种以数据为中心的方法，使用内部神经元激活来进行更智能的数据选择和教师构建。这种集中的努力表明，社区正在系统地解决政策蒸馏的核心弱点，朝着更强大和自我维持的培训循环迈进。

# RL for Reasoning & Agents
强化学习被直接应用于增强结构化推理和代理能力，通常具有可验证的奖励。DecompRL通过学习将问题分解为模块化代码来改变范式，有效地将计算瓶颈从GPU采样转移到CPU评估，并解决以前标准RL难以解决的问题。在代理领域，Atlassian工作流上的RLVR概念验证表明，合成API环境上的GRPO训练为工具使用代理带来了强大的回报。FaithMed论文应用了具有临床医生设计的规则的步骤级过程奖励RL，以执行忠实的循证医学推理。这些作品显示了使用RL灌输结构化思维和可验证的动作序列的明显趋势，将LLM从下一个令牌预测移动到目标导向的问题解决。

# 多模式和视觉语言模型
RL正在成为改善视觉语言模型（LVLM）推理的核心训练范式，特别针对视觉基础和自我反思。LABER框架引入了训练后RL方法，奖励视觉注意力保留和下沉抑制，通过确保模型关注正确的视觉区域来直接改进推理。VR RL论文进一步推进了这一点，使用掩蔽的轨迹前置和缓冲的滚入来引发视觉基础的自我反思，在非分布视觉推理方面表现出了强大的进步。这些作品凸显了从纯粹基于语言的RL向多模式RL的转变，后者明确管理视觉和文本模式之间的交互，解决了当前LVLM的一个关键弱点。

# 一致与信心
对齐的新方向正在出现，重点关注多目标优化和置信度校准。MI-ECB框架使用互信息来统一探索和偏好优化以实现多目标对齐，提供了一种有原则的信息论方法。另外，C3 RL算法对正确性和置信度校准进行了联合优化，从而实现了自适应测试时间缩放（CAS），该缩放可根据模型规定的置信度动态分配计算。这些论文指出，未来的一致不仅是为了匹配人类的偏好，而且是为了管理模型自己的认识状态，并以有原则的方式平衡多个潜在竞争的目标。

---

## 1. 净化的OPSD：按政策自我蒸馏而不失去思考方式

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Zhanming Shen, Jintao Tong, Shaotian Yan, Chen Shen, Hao Chen, Wentao Ye, Xiaomeng Hu, Rui Miao, Haobo Wang, Junbo Zhao, Gang Chen, Jieping Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Diagnoses and fixes a fundamental failure mode in on-policy self-distillation for long-CoT reasoning models by isolating and distilling only the question-conditioned, inference-transferable correction signal.

**摘要**: arXiv：2607.02234v1宣布类型：新摘要：政策上的自我提炼（OPSD）已成为改善LLM推理的一个有希望的范式，其中一位可以访问参考解决方案的特权教师为学生自己生成的轨迹提供代币级监督。然而，我们发现OPSD在长思想链上始终失败（long-CoT）推理模型，最多只能产生边际收益，同时破坏这些模型所依赖的反思推理能力。通过对教师监督信号的新颖分解，我们找出了根本原因：教师的监督由参考引发的组件主导，该组件驱动对参考特定捷径的死记硬背，而以问题为条件的、推断可转移的部分则被忽视或积极反对。基于这一诊断，我们提出了一个两步解决方案。首先，我们构建一个仅参考教师（与不带问题的参考相同的模型）来隔离监督信号的不可转移成分;减去该成分后的剩余部分捕获了受问题影响的、推断可转移的纠正。其次，我们使用逐点互信息（PMI）作为机制，将此剩余转化为形式良好的PMI目标分布，学生可以直接从中提取，过滤出引用引发的捷径。在两个数据集中对四个长CoT模型进行的实验表明，相对于基本模型和标准OPSD都有一致的改进，同时在整个训练过程中保留了模型的自然认识行为。

[阅读原文](https://arxiv.org/abs/2607.02234)

---

## 2. 程序记忆提炼：自我改进语言模型的在线反思

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Ye Liu, Srijan Bansal, Bo Pang, Yang Li, Zeyu Leo Liu, Yifei Ming, Zixuan Ke, Shafiq Joty, Semih Yavuz

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Procedural Memory Distillation (PMD), a novel on-policy distillation loop that converts cross-episode procedural signals into reusable memory to supervise the student policy, achieving strong gains over SDPO.

**摘要**: arXiv：2607.01480v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）以及最近的自蒸馏变体（例如SDPO），针对验证器评估每次推出，并根据该集级信号更新策略。然而，卷展中更丰富的程序信息很少被保留或重复使用。在各个剧集和时代中，该模型在不断变化的政策下反复遇到相关问题，产生剧集本地更新无法捕获的跨剧集信号：哪些策略始终通过验证，哪些失败模式持续存在，哪些模式复发。我们提出了程序记忆蒸馏（PSO），它将这些交叉节点信号转换为可重复使用的程序记忆，并在训练期间将其蒸馏为策略的权重。这种记忆充当训练支架，吸收到策略本身中，在推理时产生无记忆模型。PDC在三个抽象级别上组织记忆：原始轨迹、自我反思的策略和教训，以及在问题中反复出现的更高级行为模式，所有这些都是从模型自己的轨迹在线提取的。受记忆约束的自学者利用积累的经验来监督学生自己的推出，使学生能够在其参数范围内逐步内化程序知识。中心设计原则是协同进化：策略会生成更新记忆的展开，而记忆会塑造更新策略的监督。从经验上看，在Qwen 3 -8B和OLMo 3-Direct-7 B中，在SCIKNOWEVAL上，PDC比SDPO提高了3.8-5.5%，在LIVECODEBENCH上提高了7.9-13.6%。协同进化推动了这些收益：在SCIKNOWEVAL域中，冻结内存或策略使ASD落后10%以上。

[阅读原文](https://arxiv.org/abs/2607.01480)

---

## 3. DemoSSD：分歧调节的政策自我蒸馏

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yunhe Li, Hao Shi, Wenhao Liu, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Shuang Qiu, Linqi Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DemoPSD, a novel on-policy self-distillation framework that uses disagreement-modulated blending of teacher and student distributions to mitigate privileged information leakage and preserve exploration, with strong results on scientific reasoning benchmarks.

**摘要**: arXiv：2607.02502v1宣布类型：新摘要：政策上的自我蒸馏（OPSD）已成为一种训练大型语言模型（LLM）推理的实用方法，其中单个模型既充当教师，又充当具有不同信息访问水平的学生。然而，最近的研究发现，教师以特权信息为条件的密集代币级监督可能会导致过度适应领域内模式，抑制探索，并损害跨领域的概括性，同时还会引入一个更根本的问题：* 特权信息泄露 *，学生对考试时不可用的依赖答案的快捷方式进行编码。我们引入了 **DemoSSD**，这是一个新颖的框架，通过 * 选择性地采用教师指导 * 的想法来解决此类问题。与完全的教师分布不同，SD Demosis将学生引导到 * 反向KL重心目标 *，这是教师和学生分布的加权几何组合，自然地平衡了向教师学习和保留学生自己的推理能力。我们测量它们的分布之间的差异，并使用这种差异来自适应地控制每个代币位置的混合。我们可以证明DemoSSD实现了 **（1）* 泄漏衰减 *，即有效缓解特权信息泄露;和 **（2）* 勘探保护 *，即，在密集代币级蒸馏下保存勘探能力。SciKnowEval在四个科学领域的广泛实验表明，DemoPD优于GRPO和SDPO，同时保持更高的训练信息并稳健地推广到非分布GPQA基准。

[阅读原文](https://arxiv.org/abs/2607.02502)

---

## 4. 密集$\neq$ Better：政策上自我蒸馏对连续后培训的局限性

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Meng Wang, Haohan Zhao, Wenzhuo Liu, Lu Yang, Geng Liu, Haiyang Guo, Guo-Sen Xie, Gaofeng Meng, Hongbin Liu, Fei Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a critical analysis of on-policy self-distillation (SDPO) for continual post-training, revealing its limitations and collapse risks, which is highly valuable for on-policy distillation research.

**摘要**: arXiv：2607.01763v1宣布类型：新摘要：持续的后培训使基金会模型能够在保留现有能力的同时获得新知识。最近的研究表明，政策上的学习可以减少遗忘，政策上的自我提炼成为一种特别有吸引力的方法。在这项工作中，我们通过自我蒸馏政策优化（SDPO）重新审视这一乐观观点。我们的实验表明，当教师信号稳定且对齐良好时，SDPO可以加速领域内专业化，但它很难推广到分布外的场景。在持续的后训练中，SDPO表现出更强的遗忘，甚至可能崩溃，而GRPO等政策强化学习方法则会更保守地适应并更好地保留先前的能力。进一步的分析表明，更密集的自我蒸馏会在参数空间和响应空间中引起更大的漂移，并且可以通过自我强化的教师-学生循环放大高频格式化伪影。这些研究结果表明，单靠政策数据不足以进行持续学习。当教师目标稳定，代币级监督可靠时，密集的自我升华可以加速专业化，但不应将其视为持续后培训的默认稳定器。我们的代码可在https://github.com/Moenupa/SDPO-CL上获取。

[阅读原文](https://arxiv.org/abs/2607.01763)

---

## 5. DecompRL：通过学习模块化代码生成来解决更困难的问题

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Juliette Decugis, Fabian Gloeckle, Francis Bach, Taco Cohen, Gabriel Synnaeve

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DecompRL, an RL algorithm that learns to decompose problems into modular code, shifting the bottleneck from GPU sampling to CPU evaluation and solving problems standard RL cannot reach.

**摘要**: arXiv：2607.02390v1宣布类型：新摘要：大型语言模型（LLM）如何解决目前无法解决的问题？重复采样可以扩展测试时计算，但图形处理器成本会随着尝试而线性增长，而具有可验证奖励的强化学习（RL）则以牺牲样本多样性为代价提高了单次尝试的准确性。当基本策略产生正确解的可能性接近零时，这两种策略最终都会失败：无论多少采样或梯度信号都无法克服太大的搜索空间。我们采取不同的方法：我们没有更严格地采样，而是通过将问题分解为更小的、可独立解决的子函数，使任务变得更容易，这些子函数的实现可以重新组合。由于现成的模型没有针对这种模块化生成进行训练，因此我们引入了DecompRL，这是一种RL算法，它显式地学习分解和实现分层代码结构。对$n$模块的$k$实施进行审查可产生高达$k^{n}$候选解决方案，将瓶颈从图形处理器推断转移到廉价的中央处理器评估，并将图形处理器令牌成本削减$50 $\times $。在LiveCodeBench和CodeContests（Qwen~2.5~ 7 B，Code World Model~ 32 B）上，DecompRL优于标准和多元化优化的RL基线，每个问题的代币价值超过10 ' 5美元，解决了标准生成无法解决的问题。

[阅读原文](https://arxiv.org/abs/2607.02390)

---

## 6. 长上下文推理的证据状态奖励

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ya Gao, Pekka Marttinen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Maven, an RL framework with an editable evidence memory and novel action-level rewards for long-context reasoning, directly advancing RL-for-LLMs with a new reward design.

**摘要**: arXiv：2607.02073v1宣布类型：新摘要：长上下文推理需要模型定位、修改和综合分布在冗长输入中的证据。现有的长上下文RL方法通常奖励最终答案或静态证据提取，几乎没有提供有关中间动作如何改变模型证据状态的反馈。我们提出了Maven，这是一个具有可编辑证据记忆的强化学习框架。Maven定义了一个以答案为条件的证据状态价值，并奖励行动层面的状态转变：添加行动通过边际收益和事后诸葛亮贡献来归功，通过证据协同作用来联系行动，并通过在删除误导性证据后改善答案支持来放弃行动。这些奖励被分配给GRPO中相应的行动范围。在LongBench v2、LongReason和RULER上的Llama和Qwen模型中，Maven优于仅结果RL和证据识别基线，产生更充分的证据集和更低的干扰物保留。我们的研究结果表明，长上下文强化学习受益于优化状态证据导航，而不是一次性证据提取。

[阅读原文](https://arxiv.org/abs/2607.02073)

---

## 7. 激光：一种通过视觉注意力保护和下沉抑制来用于LVLM的矫正镜片

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bowen Yuan, Zijian Wang, Yadan Luo, Shijie Wang, Zi Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a post-training RL framework with two novel rewards (Visual Grounding and Sink Suppression) to regulate visual attention in LVLMs, directly improving reasoning via reward-based training.

**摘要**: arXiv：2607.01707v1宣布类型：新摘要：大型视觉语言模型（LVLM）表现出强大的推理能力，但在长视野解码期间会遭受视觉遗忘，注意力逐渐远离视觉证据。现有的方法主要将这个问题视为后期注意力衰退问题，或试图通过启发式提醒或事后注意力提升来缓解它。通过系统的实证分析，我们发现视觉遗忘下的性能下降主要是由两个被忽视的因素驱动的：早期阶段的注意力衰减破坏证据获取，以及注意力集中在与任务无关的视觉接收器标记的子集上。受这些见解的启发，我们提出了LASER，这是一个后训练框架，可以在推理过程中调节视觉注意力轨迹和视觉内标记注意力分布。从技术上讲，LASER引入了两个互补的奖励：一个是视觉基础奖励，它鼓励模型在整个解码过程中保持对语义突出的视觉标记的注意力，另一个是下沉抑制奖励，它惩罚过度关注视觉下沉标记。总之，这些奖励保留了早期阶段的基础，同时防止注意力崩溃到无信息区域。对八个基准数据集的广泛实验表明，LABER的表现始终优于强基线，验证了注意力感知训练是视觉遗忘的有效补救措施。

[阅读原文](https://arxiv.org/abs/2607.01707)

---

## 8. 不要让收益消失：打破RL中的政策梯度权重

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Juliette Decugis, Sean O'Brien, Francis Bach, Gabriel Synnaeve, Taco Cohen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes FADE, a self-adapting advantage function for RL post-training of LLMs that dynamically schedules gradient weights to improve training stability and accuracy-diversity trade-off.

**摘要**: arXiv：2607.01490v1宣布类型：新摘要：训练后的强化学习极大地改善了LLM推理，但也存在训练不稳定和多样性崩溃的问题。优势功能提供了一个有吸引力的解决方案：它们重塑了培训目标，重新权衡哪些展开推动学习，并且实施起来很简单。然而，方法的扩散使人们不清楚何时使用哪种优势。我们通过一个统一的框架，将任何优势分解为沿两个正交轴的正梯度和负梯度质量，从而消除了这种混乱。在符号轴上，不平衡的更新会塌陷熵或权重几何。在难度轴上，对困难问题的关注会使信号更加清晰，但会消耗样本量。训练期间，这两种权衡都会发生变化：探索倾向于平衡和硬专注;剥削倾向于压制和中等专注。这激发了FADE（具有动态Entropy的焦点优势），这是一种自适应优势，可以读取训练动态以自动安排梯度权重。FADE在7 B规模下比最佳静态基线提前20 k步达到峰值通过@1 20 k步，在32 B规模下提前20 k步，同时在LiveCodeBench和AIME上的所有通过@k中实现了最佳的准确性-多样性权衡。

[阅读原文](https://arxiv.org/abs/2607.01490)

---

## 9. 分布稳健的列表偏好优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xudong Wu, Jian Qian, Pangpang Liu, Vaneet Aggarwal, Jiayu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a distributionally robust listwise preference optimization objective for LLM alignment with a tractable worst-case correction, directly advancing RL-for-LLMs via novel reward design.

**摘要**: arXiv：2607.01715v1宣布类型：新摘要：现有的针对语言模型对齐的稳健偏好优化主要研究成对监督，并将稳健性置于数据集、提示或偏好对级别。相反，我们研究排名标签不确定性下的列表偏好优化：给定提示和候选列表，观察到的该列表的排名可能会由于注释者不一致、接近关系、有损的排名反馈或奖励模型噪音而变得模糊。我们提出了逐点全变稳健Plackett--Luce目标，它直接以候选列表为条件来鲁棒排名标签。鲁棒损失允许精确分解为名义PL损失加上最坏情况的PL纠正，最坏情况排名是通过对当前隐式得分进行排序来获得的，从$K减少内部最大化！$列举到$O（K\log K）$。这种易于管理的结构提供了强大的线下和在线优化保证。在离线固定列表设置中，鲁棒目标是凸的，投影随机次梯度达到全局$\ð $-次最优性，样本复杂性为$O（\ð在在线政策引发的环境中，候选人列表由当前政策生成，我们建立弱凸性和$\widetilde O（\##''' s）$Moreau-信封平稳性。离线LLM对齐中的实验表明，提出的鲁棒修正在很大程度上保留了干净标签下的性能，并提高了在噪音下的鲁棒性。在在线对齐中，它使奖励模型排名的候选人扩展更加可靠，并改进了奖励模型和外部GPT-4法官指标。

[阅读原文](https://arxiv.org/abs/2607.01715)

---

## 10. 通过强化学习实现视觉语言模型的基于视觉的自我反思

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Liyan Tang, Fangcong Yin, Greg Durrett

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes VRRL, a novel RL training framework with masked trajectory prefixes and buffered roll-ins to elicit visually grounded self-reflection in LVLMs, directly improving out-of-distribution visual reasoning.

**摘要**: arXiv：2607.02490v1宣布类型：新摘要：大型视觉语言模型可以通过生成文本思维链（CoT）来推理多模式输入。CoT推理中表现出的一个关键能力是自我反思：重新审视早期的决策并纠正之前的错误。然而，现有的LVLM通常无法在反射期间正确关注视觉输入，从而限制了它们将反馈转化为接地纠正的能力，尤其是对于非分布图像。为了解决这个问题，我们提出了一种新型的强化学习训练框架VR RL，其中有两个组件明确设计来引发基于视觉的自我反思。首先，我们在训练期间随机屏蔽轨迹前置，以强调从不正确的中间预测中恢复，而不是犯早期错误。其次，我们从体验回放缓冲区引入缓冲滚入，以将模型暴露于它必须学会纠正的各种故障状态。我们评估了涉及表格和图表以及空间导航基准的视觉基础任务的方法。虽然现成的和传统微调模型在分布漂移下会大幅下降，但我们的方法通过有效使用自反射，大大提高了标准RL和面向反射的微调基线的平均偏离分布准确性。

[阅读原文](https://arxiv.org/abs/2607.02490)

---

## 11. 超越下一个代币预测：Atlassian工作流上工具使用代理的WLVR概念证明

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Karthikeya Aditya Vissa, Sankalp Mane, Ananya Mantravadi, Harshit Rajgarhia, Abhishek Mukherji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies RLVR with verifiable rewards directly to tool-use agents in enterprise workflows, demonstrating strong reward gains via GRPO training on synthetic API environments.

**摘要**: arXiv：2607.01465v1宣布类型：新摘要：大型语言模型经过训练以预测下一个令牌，而不是在特定API内执行任务。在利基企业SaaS工作流程中--成功意味着以正确的顺序用正确的嵌套参数到达正确的端点--这种客观上的不匹配表现为无声的失败：丢失必需的字段、幻觉的工具或在一次读取后提前停止。我们询问直接在目标环境中应用的具有可验证奖励的强化学习（WLVR）是否可以缩小差距。作为概念验证，我们构建了一套由五个合成环境组成的套件，以模式保真度模拟Jira RST v3和Confluence v2 API;奖励完全根据工具调用跟踪计算，没有实时API，没有学习判断，循环中没有人类标签。评分提示Qwen 3 -1.7B和Qwen 3.5 - 4 B在驱动GRPO训练的相同跳棋上进行，我们发现，在奖励非退化的四种场景中，RL训练的策略将平均奖励从4 B基线范围0.35--0.92提高到0.95--1.00，其中Confluence页面创建的单次收益最大（0.35美元\rightarrow 1.00美元）。我们将其定位为面向利基企业API的结果优化小模型的初步步骤，并展望了研讨会读者应该权衡的两个限制：手工制作可验证的奖励不会超出此处报告的少数端点，并且我们的五个场景之一（门票过渡）具有饱和的奖励形状，提示的4 B已经达到了最大值。

[阅读原文](https://arxiv.org/abs/2607.01465)

---

## 12. FaithMed：培训法学硕士进行基于忠实证据的医学推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhiyun Zhang, Liwen Sun, Xiang Qian, Chenyan Xiong

**机构**: Carnegie Mellon University

**💡 亮点 (Highlight)**: Proposes a framework combining clinician-designed rubrics with step-level process reward RL (PPO with advantage grouping) to improve faithful evidence-based reasoning in medical LLMs.

**摘要**: arXiv：2607.01440v1宣布类型：新摘要：在医学中，忠实的推理是必不可少的，临床决策需要基于可靠证据的透明理由。当前的医学LLM要么缺乏对证据的主动访问，要么使用检索到的证据，而不监督在推理过程中如何评估和应用证据。为了解决这个问题，我们将循证医学原则正式化为流程级标准，并引入FaithMed，这是一个将临床医生设计的、自动细化的指标与使用步骤级流程奖励分配和优势分组的强化学习相结合的框架。在七个医学基准中，FaithMed比代理搜索基线（平均+9%）和仅结果RL（+5.8%）有所改善，同时比代理搜索Qwen 3基线（+15.5%）提高了基于证据的医学平均评分。这项工作表明，明确的步骤级监督可以提高任务成功率和推理过程的忠实性。代码可在https://github.com/cxcscmu/FaithMed上获取。

[阅读原文](https://arxiv.org/abs/2607.01440)

---

## 13. 多个声音，一个奖励：LLM评判和奖励建模的多角色版块生成

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Dazhi Fu, Jiuding Yang, Yiwen Guo, Jicong Fan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free multi-role rubric generation framework for reward modeling that directly improves RLVR for LLMs, a central contribution to RL for LLMs.

**摘要**: arXiv：2607.01830v1宣布类型：新摘要：可靠的奖励和偏好信号对于评估和优化开放式任务的大型语言模型至关重要。基于条目的判断器提供了一种透明的方法将此类判断分解为明确的评估标准，但现有的无注释条目生成器通常依赖于单个通用评估器。因此，他们可能会忽视人类偏好的重要维度，我们称之为维度盲点的失败模式。为了解决这一限制，我们提出了多角色规则生成（MRRG），一个免培训和免参考的框架，从多个互补的角色中提取评估标准，并将其整合到一个可审计的基于规则的评分器中。这个评分器既可以用来验证成对偏好，也可以为GRPO风格的具有可验证奖励的强化学习（RLVR）提供奖励。在偏好验证基准上的实验表明，MRRG在多个骨干模型上的性能始终优于单角色规则生成基线。进一步的WLVR实验表明，MRRG为改善开放式发电产生了更强的奖励信号。

[阅读原文](https://arxiv.org/abs/2607.01830)

---

## 14. 神经元感知的无注释LLM自蒸馏数据选择

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhuowei Chen, Xiang Lorraine Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Neuron-OPSD, a data-centric on-policy self-distillation framework that uses internal neuron activations for data selection and teacher construction, directly improving LLM capabilities without external supervision.

**摘要**: arXiv：2607.02460v1宣布类型：新摘要：在没有现实世界交互反馈或人工标记监督的情况下，对大型语言模型（LLM）进行后训练仍然具有挑战性，特别是在获得专家注释成本高昂的专业领域。最近的无注释自我进化方法通过使用模型自身的输出作为监督信号、通过额外的上下文构建教师并通过多数投票汇总多次推出的预测以产生伪标签来解决这个问题。然而，这些方法并非没有缺点：基于SFT和GRPO的变体会遭受域外性能下降，而基于奖励的按策略RL会增加校准误差。在本文中，我们提出了Neuron On-Policy Self-Distillation（Neuron-OPSD），这是一个以数据为中心的无注释自我蒸馏框架，利用内部神经元激活来指导培训数据选择和教师上下文构建。然后，该模型通过教师分布的政策提炼进行训练，在任何阶段都不需要地面真相标签。在各个专门领域的基准测试中，Neuron-OPSD可以提高领域内任务性能，同时保留跨领域概括并缓解与之前的无注释基线相比的校准崩溃。该框架特别适用于在线互动或外部监督成本高昂或不可行的环境，并且在概念上与依赖于记录的、奖励标签轨迹的离线RL方法不同。

[阅读原文](https://arxiv.org/abs/2607.02460)

---

## 15. 偏好学习中测谎器监督的缩放趋势

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Oskar J. Hollinsworth, Ann-Kathrin Dombrowski, Sam Adam-Day, Adam Gleave, Chris Cundy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Scales lie detector oversight for preference learning to large models, showing favorable scaling and potential to remove human labelers, directly advancing RL for LLM alignment.

**摘要**: arXiv：2607.01567v1公告类型：新摘要：LLM中的欺骗行为的监控和预防成本高昂，这激发了诸如通过测谎仪进行可扩展监督（SOLiD）（Cundy & Gleave，2025）等方法，该方法使用测谎仪来识别反应，供高成本标签商审查。在本文中，我们将SOLiD扩展到更大的模型，并在更多样化和更现实的偏好学习设置中对其进行评估。我们发现有利的缩放：在99%的检测器真阳性率下，未检测到的欺骗从1B参数模型的34%下降到405 B参数模型的14%，并且可以从微调阶段完全去除昂贵的人类标记器，而不会在统计上显著增加欺骗。然而，SOLiD对检测器训练数据和偏好训练数据之间的分布变化敏感，这可能会将检测器误报率推到不切实际的水平。

[阅读原文](https://arxiv.org/abs/2607.01567)

---

## 16. TudUM：Qwen的土耳其思维推理管道3.5 - 27 B

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Baran Bingol, Bahaeddin Turkoglu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO-family RL to a Qwen thinking model for Turkish reasoning, directly addressing RL-for-LLMs with a verifiable reward environment.

**摘要**: arXiv：2607.01927v1宣布类型：新摘要：本文介绍了TudUM（T\' urk\c{c}e D\' u\c{s}\' unen \' Uretken模型），这是一个将Qwen家族27 B思维模型改编为土耳其推理的项目管道。核心问题不仅是用土耳其语回答土耳其语提示，而且是使显式推理本身追溯到土耳其语。一个思维模式可能会将土耳其语的提示翻译成以英语为中心的内部或可见的便笺簿，主要用英语解决问题，并且只本地化最终答案。Tudum将处理生成的...作为一种可训练的行为。管道从项目基础检查点unsloth/Qwen3.5- 27 B开始，使用LoRA适配器对15，991个土耳其推理示例应用监督微调（SFT），然后在代理过滤的土耳其数学环境中应用GRPO系列强化学习。结果好坏参半。SFT使模型更短，推理行为更一致，平均响应长度和思维疲惫大幅减少，但基准准确性降低。RL在最佳早期检查点恢复了一些数学性能，尤其是AIME 24，但并未统一改善所有基准，并且没有超过所报告的Macro-6平均值的基础模型。因此，这一贡献最好被定义为技术上诚实的土耳其思维推理管道和评估，而不是声称最先进的土耳其推理。已发布的Step-50型号已公开。

[阅读原文](https://arxiv.org/abs/2607.01927)

---

## 17. 基于互信息的多目标探索和偏好优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Hongyan Xie, Yikun Ban, Ruiyu Fang, Zixuang Huang, Deqing Wang, Jianxin Li, Shuangyong Song

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel information-theoretic RL framework (MI-EPO) for multi-objective alignment of LLMs, unifying exploration and preference optimization via mutual information.

**摘要**: arXiv：2607.01392v1宣布类型：新摘要：将大型语言模型与多样化且异类的人类价值观相匹配需要多目标匹配方法来有效地权衡相互冲突的偏好维度。当前的方法通过训练以偏好载体为条件的政策并利用在线直接偏好优化来实现这种权衡。然而，探索的不确定性可能会导致不同偏好载体下生成的响应的回报分布重叠，并且生成的响应可能无法与相应的偏好载体有效对齐。在本文中，我们提出了通过互信息的多目标探索和偏好优化（MI-EPO），这是一个信息论框架。它通过最大化生成的响应、偏好反馈和偏好载体之间的联合条件互信息来统一多目标探索和对齐。通过结合概率路由机制，MI-ECB自然分解了客观对齐和偏好感知探索，鼓励模型生成可区分并与不同偏好条件一致的响应。安全对齐和有用辅助任务的实验表明，MI-EPO显着改善了生成的响应和偏好载体之间的对齐，使输出更加可控，并在多个目标之间实现稳定的权衡。

[阅读原文](https://arxiv.org/abs/2607.01392)

---

## 18. 置信度缩放：校准LLM的置信度以适应性测试时间缩放

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xuqing Yang, Yi Yuan, Shanzhe Lei, Xuhong Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces C3RL, a novel RL algorithm for LLMs that jointly optimizes correctness and confidence calibration, and CAS, an adaptive test-time scaling method leveraging calibrated confidence.

**摘要**: arXiv：2607.01612v1宣布类型：新摘要：使用强化学习（RL）训练大型语言模型（LLM）显着提高了它们在推理和问答任务方面的性能。然而，流行的RL奖励设计通常优先考虑响应的正确性，而忽视激励模型准确表达信心。这导致了一个关键问题：性能的提高通常伴随着信心和准确性之间的不良校准，误导模型在不确定时过度自信地产生幻觉。为了解决这一限制，我们提出了$\textBF{C}$orrigness和$\textBF {C}$onfidence $\textBF{C}$alibration $\textBF{R}$einspel $\textBF{L}$earning（$\textBF{C3 RL}$），这是一种新型RL算法，将正确性、校准和基于互联网的参考准确性奖励集成在一起。对8个文本和多模式数据集的全面评估表明，C3 RL在不牺牲准确性的情况下增强了校准，在性能和校准指标方面都优于当前最先进的方法。利用来自C3 RL的良好校准的口头置信度，我们进一步引入了$\textBF{C}$基于信心的$\textBF{A}$daptive Test Time $\textBF{S}$caling（$\textBF{CAS}$），这是一种可调整的推理时间策略，可根据响应置信度分配计算资源。实验表明，CAS在域内和域外数据集上都超过了多数投票，同时将推理预算减少了多达12.33倍。我们相信C3 RL和CAS的协同作用为部署更可靠和资源高效的LLM铺平了道路。代码、数据和模型将被发布。

[阅读原文](https://arxiv.org/abs/2607.01612)

---

