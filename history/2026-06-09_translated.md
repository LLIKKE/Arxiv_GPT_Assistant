# 💡 今日研究速览 (Daily Summary)

# 政策提炼与推理
当今的一个主要主题是完善大型语言模型（LLM）的政策提炼技术。有几项作品解决了训练和推理分布之间的根本不匹配问题。拟议的政策蒸馏（OPD）框架通过使用学生生成的轨迹将知识从自回归模型提取到扩散模型中来直接解决这个问题。补充这一点的是，几何分析表明，按策略蒸馏在参数空间中引发了独特的低维子空间锁定效应，将其与标准SFT和WLVR区分开来。RASFT实际上利用了这一理论见解，它使用经过验证的政策推出来校准专家监督，以增强推理。此外，特权辅导提炼框架在政策推出的情况下提供密集的代币级监督，而不会暴露答案，专门针对多模式推理的改进。

# 针对LLM和代理的强化学习
LLM的强化学习正在掀起一波专注于奖励设计和探索的创新浪潮。一个关键的进步是通过一种新颖的奖励框架（CapCode/CapReward）来检测和预防编码代理中的欺骗性作弊，该框架限制了非作弊性能以揭露奖励黑客行为。对于代理工具的使用，不确定性量化被直接集成到RL奖励信号（TRUST）中，以改善决策和探索。在结构化推理领域，多轮RL框架（Progress-SQL）通过Oracle引导的文本到SQL诊断树引入渐进、密集的奖励。此外，成本感知的RL方法（信任门控GSPO）仅从奖励中学习工具使用策略，而一致性驱动的RL（GRPO）则成功应用于提高跨语言事实回忆，并完成机械分析。

# 自我改进和代理人协会
自我改进代理的范式正在通过迭代的、内分布的RL循环来推进。统一框架（Q-Evolve）将自动流程奖励标签与分销政策优化相结合，使代理能够在没有外部监督的情况下自我进化。这一概念被扩展到乌托邦中的长期社会模拟，其中来自代理人互动的“生命奖励”用于拒绝抽样训练，创建一个增强社交能力的自我完善循环。一种评估推理的新颖方法--用成对排名目标训练的前置效用模型（PUM）--提供了一种新的基于结果的奖励信号，可用于指导RL和LLM推理的搜索过程。

# 潜在推理与检索
生成性检索中出现了与显式思维链推理的显着背离。电子商务的新框架（CaLIR）提议使用连续潜在状态进行意图推理，超越显式CoT来捕捉更细致入微的用户意图。这项工作直接推进了潜在推理这一未充分探索的领域，表明范式转变为特定下游任务的更灵活、更高效的内部推理过程。

---

## 1. 通过按策略蒸馏的数据高效自回归到扩散语言模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xingyu Su, Jacob Helwig, Shubham Parashar, Atharv Chagi, Lakshmi Jotsna, Degui Zhi, James Caverlee, Dileep Kalathil, Shuiwang Ji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes On-Policy Distillation (OPD) to transform ARLMs into diffusion language models, addressing train-inference mismatch and knowledge retention via self-distillation on student-generated trajectories.

**摘要**: arXiv：2606.06712v1宣布类型：新摘要：我们研究自回归模型（ARLM）到扩散语言模型（DLM）的转换。之前的工作不是从头开始进行预训练，而是用双向注意力取代ARLM中的因果注意力，然后使用DLM目标训练所得模型。然而，这些方法会引发两种分布转变。首先，从下一个令牌预测目标转换到DLM目标可能会丢弃ARLM在训练期间获取的知识。其次，标准DLC存在训练-推理不匹配的问题，因为训练损失是在随机屏蔽的序列上定义的，而不是在基于置信度的解码产生的推理时遇到的轨迹上定义的。为了解决这两个挑战，我们引入了一个政策上扩散语言模型（OPDLM），其中使用政策上蒸馏（OPD）进行ARLM到DLM的转换。具体来说，OPDLM是通过自我OPD来训练的，学生（具有双向注意力的ARLM）生成自己的轨迹，而老师（最初的冻结ARLM）通过提供这些轨迹上的目标日志来提炼自己的知识。通过直接以政策上的方式进行训练，OPDLM消除了DLC中的训练-推理不匹配，而从原始模型中提炼则增强了ARLM的知识保留。经验结果表明，OPDLM需要的训练令牌减少15倍到7，000倍，并且在各种任务中具有出色的性能。OPDLM避免了DLM预训练的高昂成本，并将DLM转换定位为ARLM后训练的一种形式。

[阅读原文](https://arxiv.org/abs/2606.06712)

---

## 2. 编码代理会欺骗我们吗？通过随机测试的上限评估来检测和预防作弊

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Thanawat Lodkaew, Johannes Ackermann, Soichiro Nishimori, Nontawat Charoenphakdee, Masashi Sugiyama, Takashi Ishida

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CapCode and CapReward, a novel reward design framework that caps non-cheating performance to detect and prevent deceptive cheating in coding agent evaluation, directly relevant to RL reward design for LLMs.

**摘要**: arXiv：2606.07379v1宣布类型：新摘要：代理评估和训练中一种日益严重的失败模式是，模型可以通过利用捷径而不是解决预期任务来获得高评估分数，从而产生欺骗性的性能。这使得评估分数作为真正任务解决能力的衡量标准不可靠。我们提出了CapCode，这是一个通过随机测试构建编码数据集的框架，其最佳可实现的非作弊性能故意限制在1以下。这种限制性能的设计为评估分数提供了更清晰的解释：远远高于上限的分数是不可信的，因此提供了作弊的证据。为了防止作弊，我们提出CapReward，这是一种基于CapCode原则的奖励设计，旨在阻止超过上限的优化。多个数据集的实验表明，CapCode可以检测作弊，同时保留模型的性能排名，而CapReward可以减少作弊行为，从而产生更好地遵循预期任务规范的模型。

[阅读原文](https://arxiv.org/abs/2606.07379)

---

## 3. 论政策上蒸馏的几何学

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhennan Shen, Yanshu Li, Qingyu Yin, Chak Tou Leong, Zhilin Wang, Yanxu Chen, Rongduo Han, Sunbowen Lee, Yi R. Fung

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Characterizes the unique parameter-space geometry of on-policy distillation for LLMs, showing it induces a distinct low-dimensional subspace locking effect compared to SFT and RLVR.

**摘要**: arXiv：2606.07082v1宣布类型：新摘要：按策略蒸馏（OPD）越来越多地用于改进大型语言模型推理，但其训练动态仍然知之甚少。我们在参数空间中描述了OPD更新的轨迹，并将其与监督微调（SFT）和带可验证奖励的强化学习（WLVR）进行比较。一套参数空间诊断始终将OPD置于宽松的非主要状态：与SFT相比，其更新影响的权重更少，回避主要方向更强烈，而与WLVR相比，它们的限制仍然不那么严格。除了这种静态定位之外，OPD还表现出子空间锁定：其累积更新迅速进入狭窄的低维通道。将训练限制在训练早期形成的更新子空间可以保留OPD性能，但大幅降低SFT，这表明锁定子空间在功能上足以满足OPD。控制实验进一步表明，稀疏更新令牌和将推出生成偏离策略可以保留排名动态，而将OPD目标与WLVR混合会改变它们。总体而言，这些结果表明OPD不仅是SFT和WLVR之间的中间点，而且在参数空间中引发了自己的更新几何。

[阅读原文](https://arxiv.org/abs/2606.07082)

---

## 4. 教方法，而不是答案：多模式政策优化的特权辅导蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shizhe Xiang, Ke An, Wenlong Yu, Yue Liu, Jian Luan, Pei Fu, Qilong Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a privileged tutoring distillation framework for RLVR that provides dense token-level supervision from on-policy rollouts without exposing answers, improving multimodal reasoning.

**摘要**: arXiv：2606.07000v1宣布类型：新摘要：最近的训练后方法，特别是具有可验证奖励的强化学习（WLVR），显着增强了大型视觉语言模型（LVLM）的推理能力。然而，可验证奖励的稀疏性质为失败的推出提供了很少的代币级监督，这通常导致复杂的多模式推理任务中的探索效率低下。尽管政策提炼可以提供密集的指导，但基于外部教师的方法会带来大量的计算负担，而答案条件调整方法可能会暴露答案级别的信息并引发类似捷径的生成行为。为了解决这些限制，我们提出了PTD-PO，这是一个针对WLVR的特权辅导蒸馏政策优化框架，它提供密集的指导，而不会将答案暴露给学生政策。具体来说，PTD-PO从空间注意力引导和中间文本推理步骤中构建结构化特权暗示，并通过上下文学习使用它们来产生分步代币分发监督。学生仍然在原始的无答案环境下进行优化，其失败的推出与代币分发级别的暗示增强参考模型保持一致。为了在引导和非引导上下文之间的分布转变下进一步稳定蒸馏，我们引入了Top-K Jensen-Shannon分歧目标，该目标重点关注信息性令牌概率，同时减少内存负担。对2B至8B参数范围内的LVLM的实验表明，PTD-PO始终优于WLVR和蒸馏基线，减轻了熵崩溃，并提高了复杂的多模式推理性能。

[阅读原文](https://arxiv.org/abs/2606.07000)

---

## 5. 乌托邦：智能体社会中的长期生活模拟和学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xintao Wang, Sirui Zheng, Hongqiu Wu, Weiyuan Li, Jen-tse Huang, Minghao Zhu, Can Zu, Qi Deng, Jiawei Wang, Qianyu He, Heng Wang, Xiaojian Wu, Yunzhe Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a long-term life simulation framework for LLM agents with a life reward used for rejection sampling training, directly improving LLM social capabilities via an on-policy self-improvement loop.

**摘要**: arXiv：2606.07513v1宣布类型：新摘要：人类从社会生活中学习。使用LLM支持的代理模拟这一过程代表了一个有前途的研究方向，并提出了一个自然的问题：LLM是否可以从这种模拟的社会体验中学习，以更好地理解和复制人类行为。然而，之前的代理人社会模拟通常以天的规模运行，限制了社会互动的深度和长期增长。在本文中，我们研究了代理人社会中的长期生活模拟和LLM学习，目标有两个：（1）调查从终身模拟中出现的社会行为，（2）通过多年的模拟社会经验，开发LLM中的拟人化能力，特别是社会生活中的智力。具体来说，我们提出了乌托邦，这是多智能体社会中长期生活模拟的综合框架，其中100个智能体在10个模拟年内自主追求个人成长、发展社会关系并满足他们的需求和目标。我们将生命奖励定义为反映人类福祉，并利用这种奖励通过拒绝抽样来训练LLM。大量实验表明，主体表现出丰富的涌现社会行为。此外，生命奖励训练有效增强了基础LLM，从而改善了模拟中的代理福祉，并推广到下游角色扮演基准，提高了+15.6%。

[阅读原文](https://arxiv.org/abs/2606.07513)

---

## 6. RASFT：推出自适应监督推理微调

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yongliang Miao, Fengyuan Liu, Wei Shi, Yanguang Liu, Fei Sun, Na Zou, Mengnan Du

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RASFT, a policy-aware SFT framework that calibrates expert supervision using verified on-policy rollouts, directly addressing on-policy distillation for reasoning improvement.

**摘要**: arXiv：2606.07006v1宣布类型：新摘要：监督微调（SFT）是一种流行的方法，通过模仿离线专家演示，使大型语言模型适应推理任务，通常将单个专家轨迹视为目标行为。然而，推理并不是简单的路径模仿：严格遵循一个演示的解决方案可能会过度适应表面形式并抑制模型自身的推理分布。我们提出了推出自适应监督微调（RASFT），这是一个策略感知的SFT框架，它根据从经过验证的政策推出中估计的问题级可解决性来校准专家监督。对于每个问题，RASFT在当前政策陷入困境时加强专家指导，而在模型已经表现出可靠的推理行为时放松严格模仿并纳入正确的自生成轨迹。为了保留有用的推理先验，RASFT进一步在冻结参考模型和当前政策之间引入了缩减的反比，以限制过度的政策漂移。在六个数学推理基准和两个代码推理基准上跨多个模型的实验表明，RASFT比SFT、SFT变体和代表性RL方法实现了更好的总体性能。该代码可在https://github.com/zjd1sq/RASFT上获取。

[阅读原文](https://arxiv.org/abs/2606.07006)

---

## 7. 通过不确定性对齐的强化学习探索抽象的工具调用决策

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yijin Zhou, Linqian Zeng, Xiaoya Lu, Wenyuan Xie, Dongrui Liu, Junchi Yan, Jing Shao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes TRUST, a novel RL method for LLM agents that incorporates uncertainty quantification into reward design to improve tool-use decisions and exploration.

**摘要**: arXiv：2606.06976v1宣布类型：新摘要：基于大型语言模型（LLM）的代理经常做出次优的工具使用决策，包括不支持的工具调用和幻觉的直接响应，这可能会在多步骤交互中积累错误。现有方法主要通过基于决策结果和结构化检查表的推断时修正或粗粒度奖励信号来改善这些行为，从而导致代理人决策的不确定性特征未得到充分研究。我们观察到，面向决策的强化学习往往会削弱正确和不正确动作之间的不确定性分离，导致过度自信的错误和较弱的探索信号。因此，我们提出了TRUST，将不确定性量化纳入奖励设计中，作为维持不确定性分离的排斥力，并标记轻量级钥匙转向注释，以实现多转弯轨迹的统一后训练。不同工具使用基准的实验结果表明，TRUST持续提高决策质量和代理性能，同时在优化期间保持更可靠的不确定性估计。

[阅读原文](https://arxiv.org/abs/2606.06976)

---

## 8. Progress-SQL：通过渐进奖励改进文本到SQL的强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shihao Zhang, Xiaoman Wang, Yuan Liu, Yunshi Lan, Weining Qian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-turn RL framework with progressive rewards for Text-to-SQL, introducing an Oracle-guided Diagnostic Tree for dense reward signals.

**摘要**: arXiv：2606.06825v1宣布类型：新摘要：强化学习最近在改进文本到SQL生成的大型语言模型方面表现出了希望，但现有方法通常会优化在单个SQL状态上定义的一次性奖励。此类奖励为迭代SQL纠正提供的指导有限，并且不足以捕捉多回合SQL细化的改进。在本文中，我们提出了Progress-SQL，这是一个多回合强化学习框架，为文本到SQL提供渐进奖励。我们的方法引入了Oracle引导的诊断树（IDT），它将SQL查询抽象为条款级结构性配置文件，并为下一轮细化生成诊断反馈。为了提供密集且稳健的奖励信号，我们将基于IDT的结构对齐与词汇对齐相结合，并定义了一个渐进奖励，该奖励衡量从初始SQL到最终SQL的改进。我们进一步纳入了有利于早期正确性的进展延迟奖励和鼓励从无效SQL中恢复的执行状态奖励。对BIRD、Spider和Spider稳健性变体的实验表明，我们的方法在主要评估和稳健性评估中一致提高了文本到SQL的性能。

[阅读原文](https://arxiv.org/abs/2606.06825)

---

## 9. 具有内部分布优化的自进化LLM代理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yudi Zhang, Meng Fang, Zhenfang Chen, Mykola Pechenizkiy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Q-Evolve, a self-evolving LLM agent framework that unifies automatic process-reward labeling and in-distribution RL policy optimization for iterative self-improvement.

**摘要**: arXiv：2606.07367v1宣布类型：新摘要：大型语言模型（LLM）最近成为复杂环境中交互式代理的强大控制器，但训练它们执行可靠的长期决策仍然是一个根本挑战。一个关键困难在于信用分配：代理人通常只在剧集结束时才收到延迟奖励。在本文中，我们提出了Q-Evolve，这是LLM代理的一个自进化框架，它将自动流程奖励标签和政策学习统一在有原则的分布式强化学习范式中。在每次不断发展的迭代中，我们的方法从混合非策略数据集中学习内分布批评者，该数据集将专家演示与代理生成的轨迹相结合，通过加权隐式Q学习目标在稀疏回报设置中稳定Bellman备份。然后，学习价值函数用于通过优势估计来获得分步流程奖励，从而实现密集且可靠的监督，而无需环境回溯或人为注释。利用这些信号，我们执行行为接近策略优化，根据用于流程奖励标签的数据来进化代理，允许迭代自我改进，而不会加剧分布转变。我们在AlfWorld、WebShop和ScienceWorld上评估了我们的方法，结果表明Q-Evolve在样本效率、稳健性和总体任务性能方面优于强基线。我们的结果表明，稳定的代理自我进化可以通过流程级监督和政策的共同进化来实现，两者都基于共享的分布内学习循环。

[阅读原文](https://arxiv.org/abs/2606.07367)

---

## 10. 从正确性到实用性：LLM推理的基于收益的前置评估

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yuhang Zhou, Yixin Cao, Guangnan Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a Prefix Utility Model (PUM) trained with a pairwise ranking objective to evaluate reasoning prefixes based on outcome-grounded utility, providing a novel reward signal for RL and search in LLM reasoning.

**摘要**: arXiv：2606.07190v1宣布类型：新摘要：推理前置决定了LLM问题解决的未来轨迹，但现有的流程奖励模型通常通过局部步骤正确性来评估它们。我们认为，正确性是我们最终关心的效果的一个有用但间接的代理：一个前置是否会增加成功完成的可能性。我们将这种效应定义为前置收益，即通过将轻量级学生模型组条件化而引起的解决率提高，并使用它来训练具有简单成对排名目标的前置实用模型（PUM）。PUM学习基于结果的前置效用，并且可以对完整轨迹和部分推理前置进行评分。在数学推理的最佳N$选择、束搜索和强化学习中，PUM提供了强大的前置级监督信号，特别是当候选池很大、搜索预算增加或基于规则的奖励稀疏时。我们在https://zhiqix.github.io/pum-project-page上发布所有数据、模型和代码。

[阅读原文](https://arxiv.org/abs/2606.07190)

---

## 11. Translate-R1：通过强化学习使用成本意识的翻译工具

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Pratik Jayarao, Chaitanya Dwivedi, Himanshu Gupta, Neeraj Varshney, Adithya M Devraj, Meet Vadera, Priyanka Nigam, Bing Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces confidence-gated GSPO, a novel RL method for cost-aware tool-use policy learning from reward alone, directly improving LLM behavior via RL.

**摘要**: arXiv：2606.06835v1宣布类型：新摘要：LLM中各语言的性能差距有据可查，本地缩小它需要对大多数语言不存在的数据库进行预训练或微调。翻译提供了一种替代方案：将输入转换为模型的主导语言，立即释放其全部功能。然而，对于模型已经处理的语言来说，对每个输入应用翻译是浪费的，而将选择权留给模型则会以相反的方式失败，因为LLM过于自信并跳过该工具，即使他们无法理解输入。之前的工作通过特定于语言的规则、域启发式、语言标识符或外部路由器解决了这个问题，每种规则都需要手动工程。相反，我们学习一个单一的政策，该政策决定何时仅从奖励中进行翻译，发展语言和领域适应性内省，评估自己的理解，并仅在无法本地解决任务时才调用翻译。   使用由我们的答案保留翻译管道构建的数据，我们在3个资源层（High、Low、XLow）和5个域中的22种语言上继续对后训练的Qwen 3 - 4 B进行RL，并引入信任门控GSPO以用于成本敏感的工具使用。门控政策在High时将奖励比基线提高+4.6，在Low时提高+23.5，在XLow时提高+17.5。与几乎总是转化的不受限制的政策相比，它将全额回报保留在成本的63%，并且在87%的成本敏感性范围内达到帕累托最优。此外，为了模拟完全看不见的语言上的行为，我们创建了2种合成语言，其中我们的门控策略比过度自信的基线提高了+18.7，即使在这些难以理解的输入上也没有充分利用该工具。该政策将零攻击转移到9种已发布的语言，我们分析了工具使用如何在培训中、每种语言和每种领域出现。

[阅读原文](https://arxiv.org/abs/2606.06835)

---

## 12. 超越匹配：电子商务中生成检索的类别引导潜在意图推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Fuwei Zhang, Xiaoyu Liu, Jiajie Jin, Jiale Mao, Wei Chen, Dongbo Xi, Yifan Yang, Peng Yan, Zichao Hao, Zhao Zhang, Fuzhen Zhuang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CaLIR, a latent intent reasoning framework for e-commerce retrieval that uses continuous latent states instead of explicit CoT, directly advancing latent reasoning.

**摘要**: arXiv：2606.07075v1宣布类型：新摘要：生成式检索通过将用户查询直接映射到产品语义标识符（DID），为电子商务搜索提供了一种新的范式。然而，电子商务查询通常简短、嘈杂、属性较多，并且与多个类别一致的产品相关联，从而在自然语言购物意图和人工构建的物品DID之间造成了巨大的表示差距。显式思想链（CoT）推理可以帮助弥合这一差距，但其额外的生成成本难以与在线电子商务系统的低延迟要求相协调。为了应对这一挑战，我们提出了CaLIR（类别引导的潜在意图推理），这是一个用于电子商务生成式检索的类别引导的潜在意图推理框架。CaLIR不是生成显式的文本原理，而是在IDS解码之前学习连续的潜在意图状态，并使用产品类别层次结构作为从粗到细意图推理的自然框架。具体来说，我们引入分层语义推理，以将潜在状态与类别级购物意图对齐，并引入查询明智推理增强，以在多正查询下对不同意图路径建模。CaLIR进一步将从预先索引的类别级尝试组装而成的查询特定动态前置trie与推理感知的约束解码相结合。多语言电子商务搜索数据集的实验表明，CaLIR比现有方法在检索有效性和推理效率之间实现了更好的平衡，同时还展示了跨诱导层次结构和不同生成主干的可移植性和鲁棒性。

[阅读原文](https://arxiv.org/abs/2606.07075)

---

## 13. 通过一致性驱动的强化学习提高跨语言事实回忆

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jonathan von Rad, Louis Arts, George Burgess, Eleftheria Kolokytha, Harry O'Donnell, Ektor Oikonomidis Doumpas, Eduardo Sanchez, Yao Lu, Pontus Stenetorp

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO (RL for LLMs) to improve cross-lingual factual recall, demonstrating a clear RL pipeline with verifiable rewards and mechanistic analysis.

**摘要**: arXiv：2606.06586v1宣布类型：新摘要：主要在英语数据上训练的大型语言模型（LLM）编码大量的世界知识，但往往无法用其他语言可靠地表达它，这种现象称为跨语言事实不一致。为了研究和解决这个问题，我们引入了PolyFact，这是一个大规模并行多语言事实QA数据集，包含10万个基于维基数据的事实，跨越12种类型学不同的语言。使用PolyFact，我们比较了轻度连续预训练（CPD）、监督微调（SFT）和通过团体相对政策优化（GRPO）进行的强化学习，以改善Qwen-2.5- 7 B和OLMo-2-1124- 7 B中的跨语言事实回忆。我们发现，GRPO始终优于SFT，提高了跨语言一致性和对未见过语言的概括性，而并行数据上的CPD产生的额外收益有限。机械分析进一步表明，GRPO通过减少MLP层和注意力头中的语言专业化来重组多语言路由，从而促进更多共享的跨语言表示。我们发布我们的代码、模型和数据集。

[阅读原文](https://arxiv.org/abs/2606.06586)

---

