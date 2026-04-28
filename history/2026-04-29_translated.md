# 💡 今日研究速览 (Daily Summary)

### RL for LLMs (Reinforcement Learning for Large Language Models)
A dominant theme emerges with a massive cluster of papers advancing RL-based post-training, moving beyond simple reward engineering to address fundamental bottlenecks in credit assignment, reward modeling, and training stability. A key breakthrough is the convergence of process-level supervision and value functions. **TCRM**theoretically unifies reward models and value functions via temporal coherence regularization, enabling token-level interpretability and seamless integration into PPO. Complementing this,**SHEAR**introduces a novel, model-free credit assignment method by computing span-level Wasserstein distances from hidden states, directly improving GRPO without auxiliary models. The field is also maturing with systematic analyses: one paper demonstrates that properly implemented**SFT-then-RL**pipelines consistently outperform complex mixed-policy methods, while another provides the first systematic study of**reward hacking**in code generation, revealing that synthetic trajectories fail to capture real-world adversarial patterns. New reward designs are proliferating, from knowledge-boundary-aware rewards (**KARL**) for hallucination mitigation and margin-enhanced process rewards (**RLCM**) for calibrated reasoning, to environment-aware process rewards (**DataPRM**) for agentic data analysis and perception-centric rewards (**Perceval**) for VLMs. Several works push RL into new domains:**World-R1**applies Flow-GRPO with 3D constraint rewards for geometrically consistent video generation,**TexOCR**uses LaTeX unit tests as verifiable rewards for document reconstruction, and**AeSlides**employs aesthetic layout rewards for slide generation. Multi-objective alignment is also addressed, with**Meta-Aligner**proposing bidirectional preference-policy optimization and**POCA**using Pareto-optimal curriculum learning.

### Self-Improving & Self-Evolving Agents
A parallel and equally vibrant thread focuses on agents that autonomously improve through closed-loop interaction, often leveraging RL principles. The most conceptually striking work is**Escher-Loop**, which proposes a fully closed-loop self-referential optimization framework where a task agent and an optimizer agent mutually evolve, directly fulfilling the criterion for a self-evolving agent. For safety,**EPO-Safe**introduces a novel RL-inspired framework where an LLM agent discovers its own safety specifications from sparse binary "danger signals" via iterative reflection, moving beyond hardcoded rules. On the efficiency frontier,**ClawTrace**presents a cost-aware tracing and distillation pipeline that enables agent self-improvement through prune/repair patches, while**JigsawRL**offers a pragmatic multiplexing framework to make RL pipelines for agent post-training more cost-efficient. Several papers address specific agentic challenges:**DPEPO**introduces diverse parallel exploration with hierarchical rewards for LLM agents,**GraphPlanner**uses RL to optimize graph-based workflow generation for multi-agent systems, and**CoFi-PGMA**provides a unified counterfactual policy gradient framework for multi-agent learning under filtered feedback. The metacognitive dimension is explored in**SSRP**, which proposes self-synthesizing reasoning protocols to overcome attention latching by architecturally separating planning from execution.

### Reward Modeling and Credit Assignment
Reward modeling is undergoing a significant theoretical and practical transformation, moving beyond scalar rewards to richer, more structured signals. The unification of reward models and value functions in**TCRM**is a theoretical highlight, demonstrating that temporal coherence regularization can transform reward models into value functions, achieving state-of-the-art PRM performance while enabling token-level credit assignment.**SHEAR**provides a complementary approach by directly computing span-level Wasserstein distances from hidden states to identify where reasoning diverges, offering fine-grained credit assignment without extra models. The process reward paradigm is extended to new modalities and tasks:**Perceval**introduces perception-centric process rewards for VLMs, enabling token-level error grounding, while**DataPRM**develops environment-aware process rewards that actively probe execution states for agentic data analysis. For explanation quality, a ranking-based reward model with listwise rewards is proposed to enable stable RL policy optimization. The issue of reward hacking is systematically investigated in code generation, revealing that synthetic trajectories are insufficient for detecting real-world adversarial patterns, underscoring the need for in-the-wild monitoring.

### Multimodal and Vision-Language Models
Multimodal reasoning is advancing through RL-based training strategies that integrate multiple modalities and reasoning depths.**Omni-o3**proposes a deep nested deduction policy trained with a cold-start SFT followed by exploratory RL with a multi-step reward model, enabling deliberative audio-visual reasoning. For vision-language models,**Perceval**provides a process reward model that enables fine-grained RL training with token-level error grounding, while another work enhances VLM reasoning by using RL with final-answer rewards to learn tool invocation and visual reflection from low-level cues.**World-R1**extends RL to text-to-video generation, using Flow-GRPO with 3D constraint rewards to enforce geometric consistency.**DeepTaxon**proposes a retrieval-augmented multimodal framework for species identification, using RL on hard samples to improve performance. For visual text generation,**POCA**introduces Pareto-optimal curriculum alignment to balance multiple aesthetic and functional objectives.

### Alignment and Safety
Alignment research is diversifying into new paradigms that go beyond standard RLHF.**Pref-CTRL**introduces a novel test-time alignment method using multi-objective value functions and representation editing, enabling dynamic preference steering without retraining. For safety in latent reasoning architectures,**Ulterior Motives**provides a benchmark and detection method for misaligned reasoning in continuous thought models, a critical concern as these models become more prevalent.**KARL**tackles hallucination through knowledge-boundary-aware RL, training models to abstain when uncertain.**AVES-DPO**proposes a self-corrected preference learning framework that uses in-distribution data from the model's own knowledge to mitigate hallucinations in large vision-language models. On the agentic safety front,**EPO-Safe**demonstrates that LLM agents can discover their own safety specifications from sparse binary signals, while**AutoPyVerifier**learns compact executable verifiers to formally validate LLM outputs.

### Reasoning and Chain-of-Thought
The mechanics of reasoning are being dissected at a deeper level, with several papers providing mechanistic insights and novel training strategies.**CAP-CoT**introduces a cycle adversarial prompt optimization framework where a challenger and feedback agent iteratively improve CoT reasoning. A mechanistic causal analysis reveals that when**Chain-of-Thought fails**, the hidden states still encode recoverable reasoning information, offering insights for latent reasoning architectures.**IRIS**proposes a two-axis curriculum RL framework combining SFT and reverse curriculum RL for cross-lingual math reasoning.**Stabilizing Efficient Reasoning**introduces step-level advantage selection to stabilize RL training for efficient reasoning.**DeepImagine**teaches biomedical reasoning through counterfactual imagining with verifiable rewards, while**Hindsight Preference Optimization**generates preference pairs from outcome-based hindsight for financial advisory.

### Specialized Domains and Applications
RL is being adapted to a wide range of specialized domains with bespoke reward designs.**World-R1**applies RL to enforce 3D constraints in video generation.**TexOCR**uses LaTeX compilation tests as verifiable rewards.**AeSlides**optimizes aesthetic layout in slide generation.**C-MORAL**tackles multi-objective molecular optimization with reinforcement alignment.**EPM-RL**distills agentic reasoning for product mapping in e-commerce.**VLK-RL**bridges reasoning and action for cross-domain task-oriented dialogue.**RL Token**enables sample-efficient online RL fine-tuning of vision-language-action models for real robots.**TCOD**introduces temporal curriculum in on-policy distillation for multi-turn autonomous agents.**CoFi-PGMA** addresses multi-agent learning under filtered feedback.

---

## 1. 土方循环：闭环自参考优化的相互进化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ziyang Liu, Xinyan Guo, Xuchen Wei, Han Hao, Liu Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a fully closed-loop self-referential optimization framework for mutual evolution of task and optimizer agents, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2604.23472v1宣布类型：新摘要：虽然最近的自主代理展现出令人印象深刻的能力，但它们主要依赖于手动脚本工作流程和手工制作的启发式方法，这从本质上限制了它们开放式改进的潜力。为了解决这个问题，我们提出了eightm-Loop，这是一个完全闭环框架，可以操作两个不同群体的相互进化：解决具体问题的任务代理，以及循环优化任务代理及其自身的优化器代理。为了维持这种自我参考的进化，我们提出了一种动态基准测试机制，该机制无缝地重复使用新生成的任务代理的经验分数作为相对输赢信号来更新优化器的分数。该机制利用任务代理的演变作为固有信号来驱动优化器的评估和细化，而无需额外的费用。对数学优化问题的经验评估表明，Earth-Loop有效地突破了静态基线的性能上限，在匹配计算下在所有评估任务中实现了最高的绝对峰值性能。值得注意的是，我们观察到优化器代理动态调整其策略以匹配高性能任务代理不断变化的需求，这解释了系统的持续改进和卓越的后期性能。

[阅读原文](https://arxiv.org/abs/2604.23472)

---

## 2. Omni-o3：用于深思熟虑视听推理的深巢式全模演绎

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhicheng Zhang, Wentao Gu, Weicheng Wang, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Jufeng Yang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a deep nested deduction policy with RL training (cold-start SFT + exploratory RL with multi-step reward model) for deliberative audio-visual reasoning, directly matching RL for LLMs and self-improving agent criteria.

**摘要**: arXiv：2604.24191v1宣布类型：新摘要：全模式理解需要一个巨大的、高度冗余的跨模式交互搜索空间，需要集中和深思熟虑的推理。当前的推理范式依赖于顺序逐步生成或并行逐个样本的推出，导致孤立的推理轨迹。这种无法共享有希望的中间路径的情况严重限制了探索效率，并在复杂的视听任务中导致复杂的错误。为了打破这一瓶颈，我们引入了Omni-o3，这是一个由深度嵌套扣除政策驱动的新颖框架。通过将推理描述为动态迭代搜索，Omni-o3本质上在各个分支之间共享推理前置，从而能够迭代执行四种原子认知动作：扩展、选择、模拟和反向传播。为了支持这个框架，我们提出了一个强大的两阶段训练范式：（1）对从350万个不同的全模式样本中提取的101 K个高质量长链轨迹进行冷启动监督微调，从而实现必要的循环搜索模式;和（2）对18 K个复杂多回合样本进行嵌套群组展开驱动的探索性强化学习，由新颖的多步骤奖励模型明确指导，以激发深度嵌套推理。大量实验表明，Omni-o3在11个基准测试中实现了有竞争力的性能，释放了全面的视听、以视觉为中心和以音频为中心的推理任务的高级能力。

[阅读原文](https://arxiv.org/abs/2604.24191)

---

## 3. 从1位危险信号发现统计安全规范

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: V\'ictor Gallego

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-inspired framework (EPO-Safe) where an LLM agent discovers safety specifications from sparse binary danger signals via iterative reflection, directly matching the self-improving agent and RL-for-LLM criteria.

**摘要**: arXiv：2604.23210v1宣布类型：新摘要：大型语言模型代理能否仅通过经验发现隐藏的安全目标？我们引入了EPO-Safe（安全代理的体验提示优化），这是一个框架，LLM迭代地生成行动计划，接收稀疏的二元危险警告，并通过反射进化自然语言行为规范。与依赖于丰富文本反馈的标准LLM反射方法不同（例如，编译器错误或详细的环境响应），EPO-Safe证明LLM可以在结构化、低维环境中根据严格贫乏的信号执行安全推理：代理永远不会观察隐藏的性能函数$R^*$，每个时间步只有一个比特表明动作不安全。我们对五个人工智能安全网格世界进行了评估（Leike等人，2017年）和五种基于文本的场景类似物，其中可见奖励$R$可能与$R^*$不同。EPO-Safe在1-2轮（5-15集）内发现安全行为，生成具有关于危险的正确解释假设的人类可读规范（例如，“X细胞具有方向性危险：从北方进入是危险的”）。至关重要的是，我们表明，标准的奖励驱动反思会主动降低安全性：仅反思奖励的代理使用循环来证明奖励黑客行为的合理性和加速奖励黑客行为，证明反思必须与专用的安全通道配对才能发现隐藏的约束。我们进一步评估了对有噪音的先知的鲁棒性：即使50%的非危险步骤产生虚假警告，平均安全性能也只会平均下降15%，尽管灵敏度取决于环境，因为跨场景反射自然过滤不一致的信号。每个进化的规范都充当一组可审计的基础行为规则，通过交互自主发现，而不是像宪法人工智能中那样由人类创作（Bai等人，2022年）。

[阅读原文](https://arxiv.org/abs/2604.23210)

---

## 4. 奖励模型是秘密价值函数：时间一致的奖励模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Alex Nikulkov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Temporally Coherent Reward Modeling (TCRM) that transforms reward models into value functions via regularization, enabling token-level interpretability, state-of-the-art PRM performance, and unified reward/value modeling in PPO.

**摘要**: arXiv：2604.22981v1宣布类型：新摘要：RL HF中的奖励模型经过训练，仅对响应的最终标志进行评分--这种选择会丢弃来自每个中间位置的丰富信号，并生成其标志级输出为噪音的模型。我们认为这是一个错失的机会：训练有素的奖励模型在任何代币上的输出都应该代表给定到目前为止的响应的最终奖励的条件期望。我们引入了时间一致奖励建模（TCRM），它通过标准Bradley-Terry损失之上的两个正规化项来引入这一性质，其中最小化器可证明等于条件期望。正规化器对应于蒙特卡洛和TD价值学习目标，与RL价值函数建立直接联系。TCRM要求对架构、数据或推理进行零更改，但从一个原则释放三种能力：可解释的代币级奖励轨迹（中间令牌成对准确性从50%提高到88.9%，最终令牌准确性保留）; Process Bench上最先进的PRM性能（F1平均值为44.9%），仅根据结果数据训练的模型;在PPO中统一奖励/价值建模，将峰值图形处理器内存减少27%，步进时间减少19%，并与LLM质量相匹配。

[阅读原文](https://arxiv.org/abs/2604.22981)

---

## 5. 别有用心：检测连续思维模型中的错位推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sharan Ramjee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a benchmark and method for detecting misaligned reasoning in continuous thought models, directly addressing safety in latent reasoning architectures.

**摘要**: arXiv：2604.23460v1宣布类型：新摘要：思想链（CoT）推理已成为在大型语言模型（LLM）中引发复杂推理的关键技术。尽管可以解释，但它对自然语言的依赖限制了模型的表达带宽。连续思维模型通过在潜在空间而不是人类可读的令牌中进行推理来解决这一瓶颈。虽然它们能够实现更丰富的表示和更快的推理，但它们提出了一个关键的安全问题：我们如何在无法解释的潜在空间中检测错位的推理？为了研究这一点，我们引入了MoralChain，这是一个包含12，000个社会场景的基准，具有平行的道德/不道德推理路径。我们使用一种新颖的双触发范式训练具有后门行为的连续思维模型--一个触发器武装错位的潜在推理（[T]），另一个触发器释放有害输出（[O]）。我们展示了三个发现：（1）连续思维模型可以在产生一致的输出的同时表现出不对齐的潜在推理，其中一致和不对齐的推理占据了潜在空间的几何不同区域;（2）在行为可区分的条件下训练的线性探针（[T][O] vs [O]）转移到检测武装但良性状态（[T] vs基线）具有高准确性;和（3）错位被编码在早期潜在思维标记中，这表明连续思维模型的安全监控应该针对潜在推理的“规划”阶段。

[阅读原文](https://arxiv.org/abs/2604.23460)

---

## 6. 奖励科学过程：统计数据分析的过程级奖励建模

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu, Lun Du, Ningyu Zhang, Huajun Chen

**机构**: Zhejiang University

**💡 亮点 (Highlight)**: Proposes DataPRM, a novel environment-aware process reward model for agentic data analysis that actively probes execution states and uses reflection-aware ternary rewards, directly matching RL for LLMs via process reward design.

**摘要**: arXiv：2604.24198v1宣布类型：新摘要：流程奖励模型（PRM）在增强数学等静态领域内大型语言模型（LLM）的推理能力方面取得了显着的成功。然而，它们在动态数据分析任务中的潜力仍然没有得到充分的开发。在这项工作中，我们首先提出了一项实证研究，揭示了通用领域PRM难以监督数据分析代理。具体来说，它们无法检测到无声错误、在不触发解释器异常的情况下产生错误结果的逻辑缺陷，并错误地惩罚探索行为，将必要的试错探索误认为是基础失败。为了弥合这一差距，我们引入了DataPRM，这是一种新型的环境感知生成式流程奖励模型，它（1）可以充当主动验证器，与环境自主交互，以探测中间执行状态并发现无声错误，（2）采用反射感知的三进制奖励策略，区分可纠正的基础错误和不可恢复的错误。我们设计了一个可扩展的管道，通过多样性驱动的轨迹生成和知识增强的分步注释，为DataPRM构建超过8K个高质量训练实例。实验结果表明，DataPRM使用N最佳推理将ScienceAgentBench上的下游策略LLM提高了7.21%，将DABStep上的下游策略LLM提高了11.28%。值得注意的是，仅使用4B参数，DataPRM的性能优于强大的基线，并在各种测试时间缩放策略中表现出强大的通用性。此外，将DataPRM集成到强化学习中比结果回报基线产生了巨大的收益，在DABench上实现了78.73%，在Table Bench上实现了64.84%，验证了流程回报监督的有效性。代码可在https://github.com/zjunlp/DataMind上获取。

[阅读原文](https://arxiv.org/abs/2604.24198)

---

## 7. 隐藏的国家知道推理分歧在哪里：通过跨级别沃瑟斯坦距离分配学分

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Xinzhu Chen, Wei He, Huichuan Fan, Wenzhe Niu, Zhongxiang Sun, Xuanru Wang, Jiuchong Gao, Jinghua Hao, Renqing He, Weijie Yu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SHEAR, a novel method using span-level Wasserstein distance from hidden states for fine-grained credit assignment in GRPO, directly improving RL for LLMs without extra models.

**摘要**: arXiv：2604.23318v1宣布类型：新摘要：组相对政策优化（GRPO）通过为推出中的所有代币分配相同的优势，在具有可验证奖励的强化学习（WLVR）中执行粗粒度信用分配。流程奖励模型可以提供更细粒度的监督，但它们需要步骤级注释或额外的奖励建模。我们表明，隐藏状态分布包含一个对局部推理质量有用的信号，仅可以使用WLVR中可用的结果级别正确性标签来提取该信号。具体来说，在每个GRPO组内，正确和不正确展开的跨度级隐藏状态分布之间的沃瑟斯坦距离在其局部推理质量分歧的区域周围增加。这种关联在各个例子和个体轨迹中都成立，这表明隐藏状态分布差异可以作为细粒度信用分配的自我监督信号。我们用分离定理形式化了这一观察结果，该理论表明，在温和的结构假设下，每当人口水平分布差距超过有限样本噪音时，分歧后跨度就比分歧前跨度具有更大的沃瑟斯坦距离。受这一结果的启发，我们提出了\textbf{S}泛级\textbf{H}idden state \textbf{E}nabled \textbf{A}dvantage \textbf{R}加权（SHRIGHT），它通过使用跨度级Wasserstein距离来缩放令牌级优势，从而修改GRPO，放大隐藏状态与相对组分离的令牌的更新。该方法不需要额外的模型，只需要对训练管道进行最小的更改。在五个数学推理基准测试和五个代码生成基准测试上的实验表明，相对于标准GRPO和有监督的过程奖励模型，性能有所改善，同时不需要额外的注释或奖励模型训练。

[阅读原文](https://arxiv.org/abs/2604.23318)

---

## 8. 校准LLM推理置信度的过程监控

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Liaoyaqi Wang, Chunsheng Zuo, William Jurayj, Benjamin Van Durme, Anqi Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a calibration-aware RL framework (RLCM) with a margin-enhanced process reward for LLM reasoning, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2604.2333v1宣布类型：新摘要：利用强化学习（RL）扩展测试时计算已成为提高大型语言模型（LLM）推理能力的可靠途径。然而，基于结果的奖励通常会激励模型过度自信，从而导致幻觉、不可靠的基于信心的控制和不必要的计算分配。我们引入了带置信度的强化学习（\textBF{RRCM}），这是一个具有校准意识的RL框架，通过对中等预算完成的边际增强流程奖励来联合优化正确性和置信度可靠性。RRCM鼓励扩大单一推理轨迹内正确步骤和不正确步骤之间的置信范围，而不是将信心与正确可能性挂钩。在数学、代码、逻辑和科学基准方面，我们的方法大大改善了校准，同时保持或提高了准确性。我们进一步表明，通过校准的置信信号，所得模型能够实现更高效的保形风险控制和有效的置信加权聚合。

[阅读原文](https://arxiv.org/abs/2604.23333)

---

## 9. V-GRPO：用于去噪生成模型的在线强化学习比您想象的更容易

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bingda Tang, Yuhui Zhang, Xiaohan Wang, Jiayuan Mao, Ludwig Schmidt, Serena Yeung-Levy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes V-GRPO, a novel online RL method for aligning denoising generative models using ELBO-based surrogates with GRPO, achieving SOTA text-to-image synthesis with significant speedups.

**摘要**: arXiv：2604.23380v1宣布类型：新摘要：将去噪生成模型与人类偏好或可验证的回报保持一致仍然是一个关键挑战。虽然政策梯度在线强化学习（RL）提供了一个有原则的训练后框架，但其直接应用受到这些模型棘手的可能性的阻碍。因此，先前的工作要么优化采样轨迹上的诱导马尔科夫决策过程（MDP），该过程稳定但效率低下，要么使用基于扩散证据下限（ELBO）的似然代理，迄今为止，该模型在视觉生成方面表现不佳。我们的主要见解是，基于ELBO的方法实际上可以既稳定又高效。通过减少替代方差和控制梯度步骤，我们表明这种方法可以击败基于MPP的方法。为此，我们引入了变分GRPO（V-GRPO），这是一种将基于ELBO的代理与组相对政策优化（GRPO）算法集成的方法，以及一套简单但重要的技术。我们的方法易于实现，与预训练目标一致，并避免了基于MPP的方法的局限性。V-GRPO在文本到图像合成方面实现了最先进的性能，同时比MixGRPO提供了2美元的加速，比VariationNFT提供了3美元的加速。

[阅读原文](https://arxiv.org/abs/2604.23380)

---

## 10. SFT-then-RL优于混合策略LLM推理方法

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Alexis Limozin, Eduard Durech, Torsten Hoefler, Imanol Schlag, Valentina Pyatkin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that fixing bugs in standard SFT-then-RL pipelines outperforms recent mixed-policy methods for LLM reasoning, directly relevant to RL for LLMs.

**摘要**: arXiv：2604.23747v1公告类型：新摘要：最近用于LLM推理的混合策略优化方法交织或混合监督和强化学习信号，报告了标准SFT-然后-RL管道的改进。我们发现，许多最近发表的研究论文依赖于由两个不同的错误引起的错误基线：DeepSpeed中的CPU卸载优化器错误，在梯度累积期间悄悄地丢弃中间微批次（影响多个下游框架，包括TRL，OpenRLHF和Llama-Factory），以及OpenRLHF中的损失聚合错误，错误地对每个小批次损失进行加权。它们共同抑制了SFT性能，优化器错误占了大部分差距，而损失聚合错误贡献了较小的额外影响。一旦纠正，标准的SFT-then-RL管道在数学基准上超过了我们评估的所有已发布的混合策略方法，Qwen 2.5-Math-7 B的数学基准上提高了+3.8分，Llama-3.1-8B的数学基准上提高了+22.2分。即使是只有50个RL步骤的截断变体，在数学基准上也优于混合策略方法，同时使用更少的FLOP。

[阅读原文](https://arxiv.org/abs/2604.23747)

---

## 11. KARL：通过知识边界感知强化学习缓解LLM中的幻觉

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Cheng Gao, Cheng Huang, Kangyang Luo, Ziqing Qiao, Shuzheng Si, Huimin Chen, Chaojun Xiao, Maosong Sun

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL framework (KARL) with a knowledge-boundary-aware reward and two-stage training to align LLM abstention behavior, directly addressing RL for LLMs with a new reward design and training recipe.

**摘要**: arXiv：2604.22779v1公告类型：新摘要：使大型语言模型（LLM）能够适当地避免回答超出其知识范围的问题对于减轻幻觉至关重要。虽然现有的强化学习方法促进了自主学习，但它们往往会损害答案的准确性，因为它们的静态奖励机制与模型的知识边界无关，会使模型过度谨慎。在这项工作中，我们提出了KARL，这是一个新颖的框架，可以不断地将LLM的学习行为与其不断发展的知识边界保持一致。KARL引入了两项核心创新：知识边界感知奖励，使用组内响应统计来执行在线知识边界估计，动态奖励正确答案或引导性弃权;和两阶段RL训练策略，首先探索知识边界并绕过“弃权陷阱”，随后将超出知识边界的错误答案转化为弃权，而不牺牲准确性。针对多个基准的广泛实验表明，KARL实现了卓越的准确性与幻觉的权衡，有效地抑制幻觉，同时在内分布和外分布场景中保持高准确性。

[阅读原文](https://arxiv.org/abs/2604.22779)

---

## 12. 用以感知为中心的流程奖励模型改进视觉语言模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Yingqian Min, Kun Zhou, Yifan Li, Yuhuan Wu, Han Peng, Yifan Du, Wayne Xin Zhao, Min Yang, Ji-Rong Wen

**机构**: Renmin University of China

**💡 亮点 (Highlight)**: Proposes Perceval, a process reward model for VLMs that enables token-level error grounding and fine-grained RL training, directly matching RL for LLMs and verifier-driven optimization.

**摘要**: arXiv：2604.24583v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）的最新进展显着提高了视觉语言模型（VLMS）的复杂推理能力。然而，其结果级监督过于粗糙，无法诊断和纠正推理链内的错误。为此，我们提出了Perceval，这是一种流程奖励模型（PRM），它能够实现标记级错误基础，可以从响应中提取与图像相关的声明，并将其与图像中的视觉证据一一比较，最终返回包含感知错误的声明。Perceval使用感知密集型监督训练数据进行训练。然后，我们将Perceval集成到RL培训过程中来训练政策模型。具体来说，与应用序列级优势的传统GRPO相比，我们通过针对Perceval识别的幻觉跨度进行惩罚来应用代币级优势，从而实现细粒度的监督信号。除了增强训练过程外，Perceval还可以在推理阶段协助VLM。使用Perceval，我们可以截断模型响应的错误部分，然后让模型直接重新生成响应，或者诱导模型反思其之前的输出。该过程可以重复多次以实现测试时间扩展。实验表明，使用RL训练的多个推理VLM的各个领域的基准有显着改进，凸显了以感知为中心的监督作为通用策略的前景。对于测试时间扩展，它还展示了与其他策略（例如主要投票）相比一致的性能提升。我们的代码和数据将在https://github.com/RUCAIBox/Perceval上公开发布。

[阅读原文](https://arxiv.org/abs/2604.24583)

---

## 13. AutoPyVerification：学习大型语言模型输出的紧凑可执行验证器

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Pouya Pezeshkpour, Estevam Hruschka

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a framework to automatically synthesize compact executable verifiers for LLM outputs, directly relevant to RL for LLMs via verifier-driven optimization.

**摘要**: arXiv：2604.22937v1宣布类型：新摘要：验证正在成为大型语言模型（LLM）基于协作学习的培训和推理时控制的核心。然而，当前的验证器面临着一个基本的权衡：基于LLM的验证器具有表达力，但难以控制并且容易出错，而确定性的可执行验证器可靠且可解释，但通常能力有限。我们研究以下问题：给定一组LLM输出和目标（例如正确性）的标签的开发集，我们能否自动引入一组最小的Python验证者，其联合满意度与该目标密切匹配？我们提出了AutoPyVerify，这是一个使用LLM来合成候选验证器函数的框架，然后通过在有向无环图（DAB）上搜索来细化它们。通过导航DAB，AutoPyVerify系统地探索确定性可执行验证器的空间，并选择其联合满意度最接近目标目标的紧凑验证器集。AutoPyVerify在几种最先进的LLM的数学推理、编码、函数调用和描述遵循基准中，将目标-目标预测比初始LLM生成的验证器集提高了高达55.0个F1点。额外的分析表明，最有用的验证目标因基准和模型而异，并且基于DAB的搜索将学习的验证者设置转向更具结构性和基于语义的检查。我们进一步表明，将发现的验证器集作为外部工具暴露给LLM可将下游准确性提高高达17.0个百分点。我们发布我们的代码

[阅读原文](https://arxiv.org/abs/2604.22937)

---

## 14. Pref-ALT：使用表达编辑的首选项驱动LLM对齐

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Imranul Ashrafi, Inigo Jauregi Unanue, Massimo Piccardi

**机构**: University of Technology Sydney

**💡 亮点 (Highlight)**: Proposes a novel preference-based training framework for test-time LLM alignment using multi-objective value function and representation editing, directly improving alignment via reward design.

**摘要**: arXiv：2604.23543v1宣布类型：新摘要：测试时对齐方法通过在推理时对大型语言模型（LLM）的内部表示进行轻量级干预来引导大型语言模型（LLM）的输出，为微调提供了一种有希望的替代方案。最近，出现了一种突出且有效的方法，RE-控制（Kong等人，2024年），提议利用在LLM隐藏状态上训练的外部价值函数来通过基于梯度的编辑来指导生成。虽然有效，但这种方法忽略了对齐任务的一个关键特征，即它们通常被制定为从候选响应之间的人类偏好中学习。为了解决这个问题，在本文中，我们提出了一种新型的基于偏好的训练框架Pref-ALT，它使用多目标值函数来更好地反映偏好数据的结构。我们的方法在两个基准数据集上优于RE-Control，并在域外数据集上表现出更大的概括性。我们的源代码可在https://github.com/UTS-nlPUG/pref-ctrl上获取。

[阅读原文](https://arxiv.org/abs/2604.23543)

---

## 15. 进一步了解，深入思考：通过低级视觉线索和反思提高VLM的推理能力

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhiheng Wu, Tong Wang, Shuning Wang, Naiming Liu, Yumeng Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a VLM reasoning framework that uses RL with final-answer reward to learn tool invocation and visual reflection, directly matching RL for LLMs.

**摘要**: arXiv：2604.24339v1宣布类型：新摘要：视觉语言模型（VLM）的最新进展受益于强化学习（RL）以增强推理。然而，现有的方法仍然面临着严重的局限性，包括缺乏低级视觉信息和有效的视觉反馈。为了解决这些问题，本文提出了一个统一的多模式交织推理框架\textBF{ForeSight}，该框架使VLM能够具有低级视觉线索的\textBF{See Further}和具有有效视觉反馈的\textBF{Think Deeper}。首先，它引入了一组低级视觉工具，将基本视觉信息集成到推理链中，减少对细粒度视觉特征的忽视。其次，阐述了基于面具的视觉反馈机制，将视觉反射融入到思维过程中，使模型能够动态地重新检查和更新其答案。在RL的驱动下，ForeSight学会自主决定工具调用和答案验证，并以最终答案准确性作为奖励信号。为了评估拟议框架的性能，我们基于SalBench数据集构建了一个新的数据集Charlotte and Grounding SalBench（CG-SalBench）。实验结果表明，ForeSight-7 B模型在相同参数规模下显着优于其他模型，甚至在某些指标上超过了当前的SOTA闭源模型。

[阅读原文](https://arxiv.org/abs/2604.24339)

---

## 16. TexOCR：改进文档OCR模型以实现可搜索的页面到LaTeX重建

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chengye Wang, Lin Fu, Zexi Kuang, Yilun Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RL with verifiable rewards from LaTeX unit tests to improve document reconstruction, directly matching the RL for LLMs criterion with a novel reward design.

**摘要**: arXiv：2604.22880v1宣布类型：新摘要：现有文档OCR主要针对纯文本或Markdown，放弃了使LaTeX对于科学出版至关重要的结构性和可执行属性。我们研究将科学PDF页面级重建为可编译的LaTeX，并为这项任务引入了基准TexOCR-Bench和大规模训练库TexOCR-Train。TexOCR-Bench具有多维评估套件，可联合评估转录保真度、结构忠实度和端到端可编辑性。利用TexOCR-Train，我们使用监督式微调（SFT）和强化学习（RL）来训练2B参数模型TexOCR，并具有从LaTeX单元测试中获得的可验证奖励，直接强制可编译性和引用完整性。TexOCR-Bench上21个前沿模型的实验表明，现有系统经常违反关键文档不变量，包括一致的部分结构、正确的浮动放置和有效的标签引用链接，这会损害编译可靠性和下游可用性。我们的分析进一步表明，具有可验证回报的RL比单独的SFT会产生一致的改进，特别是在结构和编译指标方面。

[阅读原文](https://arxiv.org/abs/2604.22880)

---

## 17. AeSlides：通过可验证的奖励激励基于LLM的幻灯片生成中的审美布局

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yiming Pan, Chengwei Hu, Xuancheng Huang, Can Huang, Mingming Zhao, Yuean Bi, Xiaohan Zhang, Aohan Zeng, Linmei Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning framework with verifiable rewards (GRPO) for aesthetic layout supervision in slide generation, directly matching RL for LLMs via explicit reward design.

**摘要**: arXiv：2604.22840v1宣布类型：新摘要：大型语言模型（LLM）在代理任务中表现出了强大的潜力，特别是在幻灯片生成方面。然而，幻灯片生成提出了一个根本性挑战：生成过程以文本为中心，而其质量则由视觉美学决定。这种形式差距导致当前型号经常制作具有美学上次优布局的幻灯片。现有的解决方案通常依赖于大量的视觉反射，这会产生很高的推理成本，但收益有限;或者依赖于对大规模数据集的微调，这仍然提供弱且间接的美学监督。相比之下，明确使用美学原则作为监督仍然没有探索。在这项工作中，我们介绍了AeSlides，这是一个强化学习框架，在幻灯片生成中为美学布局监督提供可验证的奖励。我们引入了一套精心设计的可验证指标来量化幻灯片布局质量，以准确、高效且低成本的方式捕捉关键布局问题。利用这些可验证的指标，我们开发了一种基于GRPO的强化学习方法，该方法可以直接优化幻灯片生成模型，以实现美观一致的布局。AeSlides在GLM-4.7-Flash上仅使用5K训练提示，将长宽比合规性从36%提高到85%，同时将空白减少44%、元素碰撞减少43%、视觉不平衡减少28%。人类评估进一步显示总体质量有了大幅提高，分数从3.31增加到3.56（+7.6%），优于基于模型的奖励优化和基于反思的代理方法，甚至超过了Claude-Sonnet-4.5。这些结果表明，这种可验证的美学范式提供了一种高效且可扩展的方法来将幻灯片生成与人类美学偏好相一致。我们的存储库可访问www.example.com。

[阅读原文](https://arxiv.org/abs/2604.22840)

---

## 18. DPEPO：基于LLM的代理的多元化并行探索政策优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Junshuo Zhang, Chengrui Huang, Feng Guo, Zihan Li, Ke Shi, Menghua Jiang, Jiguo Yu, Shuo Shang, Shen Gao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL algorithm (DPEPO) with hierarchical rewards for diverse parallel exploration in LLM agents, directly matching RL for LLMs and self-improving agents criteria.

**摘要**: arXiv：2604.24320v1宣布类型：新摘要：遵循顺序“推理然后行动”范式的大型语言模型（LLM）代理在许多复杂任务中取得了卓越的性能。然而，这些方法的探索有限和环境理解不完整，因为它们每一步仅与一个环境交互。在本文中，我们首先介绍了一种新颖的范式，使代理能够同时与多个环境交互并共享跨轨迹体验。在这个范式的基础上，我们进一步提出了DPEPO，这是一种强化学习（RL）算法，鼓励代理执行多样化的并行探索。DPEPO有两个阶段：初始监督微调（SFT）提供基本的并行推理和动作生成，然后是具有分层奖励计划的强化学习阶段。我们设计了一个平行的学徒级成功奖励和两个步骤级奖励：多元化行动奖励和多元化状态转变奖励，积极惩罚行为冗余并促进广泛探索。ALFWorld和ScienceWorld上的大量实验表明，DPEPO实现了最先进的（SOTA）成功率，同时保持了与强顺序基线相当的效率。(Code请访问https：//github.com/LePanda026/Code-for-DPEPO）

[阅读原文](https://arxiv.org/abs/2604.24320)

---

## 19. World-R1：加强文本到视频生成的3D约束

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Weijie Wang, Xiaoxuan He, Youping Gu, Yifan Yang, Zeyu Zhang, Yefei He, Yanbo Ding, Xirui Hu, Donny Y. Chen, Zhiyuan He, Yuqing Yang, Bohan Zhuang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes World-R1, a framework using reinforcement learning (Flow-GRPO) with 3D constraint rewards to align text-to-video generation with geometric consistency, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2604.24764v1宣布类型：新摘要：最近的视频基础模型展示了令人印象深刻的视觉合成，但经常受到几何不一致的影响。虽然现有方法试图通过架构修改来注入3D先验，但它们通常会产生很高的计算成本并限制可扩展性。我们提出World-R1，这是一个通过强化学习将视频生成与3D约束相结合的框架。为了促进这种对齐，我们引入了专为世界模拟量身定制的专业纯文本数据集。利用Flow-GRPO，我们使用来自预训练的3D基础模型和视觉语言模型的反馈来优化模型，以在不改变底层架构的情况下加强结构一致性。我们进一步采用周期性的脱钩训练策略来平衡刚性几何一致性与动态场景流动性。广泛的评估表明，我们的方法显着增强了3D一致性，同时保留了基础模型的原始视觉质量，有效地弥合了视频生成和可扩展世界模拟之间的差距。

[阅读原文](https://arxiv.org/abs/2604.24764)

---

## 20. GraphPlanner：多代理LLM的图内存增强统计路由

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Tao Feng, Haozhen Zhang, Zijie Lei, Peixuan Han, Jiaxuan You

**机构**: University of Illinois Urbana-Champaign

**💡 亮点 (Highlight)**: Proposes GraphPlanner, a graph memory-augmented agentic router for multi-agent LLMs that uses RL to optimize workflow generation, directly matching RL for LLMs and agent self-improvement criteria.

**摘要**: arXiv：2604.23626v1宣布类型：新摘要：LLM路由在集成不同模型的优势同时平衡效率和性能方面取得了令人鼓舞的成果。然而，为了支持更现实和更具挑战性的应用程序，路由必须扩展到代理LLM设置中，其中任务规划、异类代理之间的多轮合作和内存利用率是必不可少的。为了解决这一差距，我们提出了GraphPlanner，这是一种用于多代理LLM的异类图内存增强代理路由器，可以为每个查询生成路由工作流程，并支持归纳和转化推理。GraphPlanner将工作流生成制定为Markov决策过程（MDP），在每一步中，它都选择LLM主干和代理角色，包括Planner、Executior和Summarizer。通过利用被标记为GARNet的异类图来捕获查询、代理和响应之间的交互记忆，GraphPlanner将历史记忆和工作流程记忆集成到更丰富的状态表示中。通过强化学习优化整个管道，共同提高特定任务的性能和计算效率。我们对14种不同的LLM任务进行了评估，并证明：（1）GraphPlanner的性能优于强大的单轮和多轮路由器，准确性提高高达9.3%，同时将图形处理器成本从186.26 GiB降低到1.04 GiB;（2）GraphPlanner稳健地推广到不可见的任务和LLM，展现出强大的零射击能力;以及（3）GraphPlanner有效地利用历史记忆，支持感性和感性推理以实现更自适应的路由。我们的GraphPlanner代码在https://github.com/ulab-uiuc/GraphPlanner上发布。

[阅读原文](https://arxiv.org/abs/2604.23626)

---

## 21. 合成轨迹是否反映了真实的奖励黑客行为？监控代码生成中的野外黑客行为的系统研究

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Lichen Li, Hengguang Zhou, Yijun Liang, Tianyi Zhou, Cho-Jui Hsieh

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies reward hacking in RL for code generation, proposing a method to curate in-the-wild hacking trajectories and showing synthetic data limitations.

**摘要**: arXiv：2604.23488v1宣布类型：新摘要：代码生成中的奖励黑客攻击（模型利用评估漏洞在不正确解决任务的情况下获得完全奖励）对强化学习（RL）和推理模型的部署构成了严峻的挑战。现有的研究主要针对合成黑客轨迹进行。然而，这些合成行为是否忠实地代表了野生环境中自然出现的黑客行为仍不清楚。在这项工作中，我们提出了一个系统的分析的合成与野生的差异在奖励黑客。我们研究在何种程度上黑客行为诱导的提示类似于那些出现在RL训练，以及是否监视器训练合成轨迹推广到自然产生的，但以前看不见的黑客行为。为了扩大对野外奖励黑客轨迹的管理，我们通过注入冲突单元测试作为跟踪器并应用“重新采样直到黑客”机制来修改组相对策略优化（GRPO）。通过对合成数据和野外数据进行训练的监视器之间的受控比较，我们发现（1）经过合成数据训练的监视器未能概括为“野外”黑客行为，（2）经过我们的“野外”轨迹训练的监视器对不可见的黑客类型表现出更强的概括性。我们的结果表明，合成奖励黑客数据可能无法完全反映自然奖励黑客行为，并且仅依赖合成数据可能会导致误导性结论。该代码库可在https://github.com/LichenLillc/CoTMonitoring.git上获取

[阅读原文](https://arxiv.org/abs/2604.23488)

---

## 22. 金融时间序列咨询的事后诸葛亮偏好优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yanwei Cui, Guanghui Wang, Xing Zhang, Peiyang He, Ziyuan Li, Bing Zhu, Wei Qiu, Xusheng Wang, Zheng Yu, Anqi Xin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Hindsight Preference Optimization, a novel RL method that uses outcome-based hindsight to generate preference pairs for DPO, directly improving LLM advisory quality.

**摘要**: arXiv：2604.23988v1宣布类型：新摘要：时间序列模型预测数字;决策者需要咨询--具有推理的方向性信号、可操作的建议和风险管理。用于此类预测咨询的训练语言模型面临着根本性挑战：质量取决于预测时未知的结果。我们将强化学习的两个想法结合起来--使用执行期间不可用的信息回顾性地生成训练信号和偏好对齐--并提出后见之明偏好优化：观察到的结果让LLM判断对候选建议进行量化指标无法捕获的维度上的排名，从而在没有人类注释的情况下为DPO产生偏好对。我们将其应用于标准普尔500指数股票时间序列的基于视觉-语言-模型的预测咨询，4 B模型在准确性和咨询质量方面优于其235 B老师就证明了这一点。

[阅读原文](https://arxiv.org/abs/2604.23988)

---

## 23. CAP-CoT：循环对抗提示改善LLM推理中的思维链

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shuxu Chen, Yitian Zhou, Jiaquan Zhang, Haoyu Bian, Aming Wu, Sungyoung Lee, Chaoning Zhang, Hyundong Shin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a cycle adversarial prompt optimization framework (CAP-CoT) that uses an adversarial challenger and feedback agent to iteratively improve CoT reasoning accuracy and stability, directly matching the RL for LLMs and self-improving agent criteria.

**摘要**: arXiv：2604.23270v1宣布类型：新摘要：思想链（CoT）提示已成为从大型语言模型（LLM）中引出分步解决方案的一种简单有效的方法。然而，CoT推理在长时间、多步骤问题的运行中可能不稳定，导致未改变任务的答案不一致。之前的大多数工作重点是在一次通过内改进正向推理链，而较少关注迭代和对比纠正。为了解决这一差距，我们提出了CAP-CoT，这是一个循环对抗提示优化框架，旨在提高单个部署求解器的CoT推理准确性和稳定性。在每个周期中，前向求解器生成候选推理链，对抗挑战者使用有针对性的错误策略构建看似合理但故意存在缺陷的链，反馈代理对比两个链并产生逐步对齐的结构化反馈。该反馈在两个方向上关闭优化循环，包括根据挑战者暴露的错误更新求解器提示，以及更新挑战者提示以在后续周期中生成越来越有针对性的错误。与越狱或预算注入攻击等以安全为导向的对抗提示不同，我们的对抗组件是任务语义的，旨在暴露推理链中的逻辑漏洞。六个基准测试和四个LLM主干的实验表明，在两到三个对抗性提示优化周期内，CAP-CoT一致地减少了运行中的变异性，同时提高了推理准确性和对提示扰动的鲁棒性。

[阅读原文](https://arxiv.org/abs/2604.23270)

---

## 24. DeepImagine：通过连续反事实想象学习生物医学推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Youze Zheng, Jianyou Wang, Yuhan Chen, Matthew Feng, Longtian Bao, Hanyuan Zhang, Maxim Khan, Aditya K. Sehgal, Christopher D. Rosin, Umber Dube, Ramamohan Paturi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-with-verifiable-rewards pipeline for teaching LLMs biomedical reasoning via counterfactual imagining, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2604.23054v1宣布类型：新摘要：预测前瞻性临床试验的结果仍然是大型语言模型的一个重大挑战。之前的工作表明，传统的相关预测器（例如随机森林和逻辑回归）和强大的商业LLM在这项任务上的性能都有限。在本文中，我们提出了DeepImagine，这是一个通过连续反事实想象教授法学硕士生物医学推理的框架。中心思想是通过训练模型来逼近临床试验的隐藏因果机制，以推断观察到的试验结果在实验条件（例如剂量、结果指标、研究组、地理和其他试验属性）的受控扰动下将如何变化。为了支持这一目标，我们从真实的临床试验和报告的结果中构建了自然和大致的反事实对。对于可以进行严格反事实监督的环境，例如同一试验中的配对结果测量或剂量范围研究组，我们通过监督微调来训练模型。对于只能检索到大致反事实对的更广泛环境，我们使用基于下游基准正确性的可验证奖励通过强化学习来优化模型。我们进一步通过合成推理痕迹来增强训练，为局部反事实转变提供因果合理的解释。使用此管道，我们在10 B参数（包括Qwen 3.5 - 9 B）下训练语言模型，并在临床试验结果预测方面对其进行评估。我们的目标是证明DeepImagine能够持续改进未经调优的语言模型和传统的相关基线。最后，我们的目标是表明，学习到的推理轨迹提供了有关模型如何代表试验级机制的可解释信号，为迈向更机械化和科学有用的生物医学语言模型提出了一条实用的道路。

[阅读原文](https://arxiv.org/abs/2604.23054)

---

## 25. ClawTrace：LLM代理技能蒸馏的成本意识追踪

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Boqin Yuan, Renchu Song, Yue Su, Sen Yang, Jing Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a cost-aware tracing and distillation pipeline for LLM agents that enables self-improvement via prune/repair patches, directly matching the self-evolving agents criterion.

**摘要**: arXiv：2604.23853v1宣布类型：新摘要：技能蒸馏管道从LLM代理轨迹中学习可重复使用的规则，但它们缺乏关键信号：每一步的成本是多少。如果没有每一步的成本，管道无法区分添加缺失的步骤来修复错误和删除从未影响结果的昂贵步骤。我们引入ClawTrace，这是一个代理跟踪平台，可以记录代理会话期间的每个LLM调用、工具使用和子代理派生，并将每个会话编译成TraceCard：紧凑的YML摘要，包含每步USD成本、令牌计数和冗余标志。CostCraft基于ClawTrace构建，是一个蒸馏管道，可以读取TraceCards并生成三种类型的技能补丁。保留补丁保留导致成功的行为。修剪补丁删除了无关紧要的昂贵步骤，每一个步骤都有反对指定高成本步骤的反事实论点。修复补丁修复了基于Oracle证据的故障。对30个已发布的数据表长凳任务的消融表明，成本归因和修剪补丁都可以独立地减少质量回归。当相同的技能应用于30个不相关的SkillsBench任务时，会出现意想不到的不对称现象：修剪跨基准传输的规则并将中位数成本降低32%，而保留基于特定基准惯例训练的规则会导致新任务类型的回归。我们发布ClawTrace和TraceCards作为开放基础设施，用于成本意识的代理研究。

[阅读原文](https://arxiv.org/abs/2604.23853)

---

## 26. 当思想链失败时，解决方案隐藏在隐藏状态中

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Houman Mehrafarin, Amit Parekh, Ioannis Konstas

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides mechanistic causal analysis showing CoT hidden states encode recoverable reasoning information, offering insights for latent reasoning architectures.

**摘要**: arXiv：2604.23351v1宣布类型：新摘要：中间推理在计算上是否有用还是仅仅是解释性取决于思想链（CoT）令牌是否包含与任务相关的信息。我们使用激活补丁对GSM 8 K上的CoT进行了机械因果分析：将标记级隐藏状态从CoT生成转移到同一问题的直接答案运行，然后测量对最终答案准确性的影响。在各个模型中，修补后生成的准确性远高于直接答案提示和原始CoT跟踪，这表明即使原始跟踪不正确，各个CoT令牌也可以编码足够的信息来恢复正确答案。这种与任务相关的信息在正确的CoT运行中比不正确的CoT运行中更普遍，并且在代币之间分布不均匀，集中在中后期层，并且在推理轨迹中出现得更早。此外，动词和实体等修补语言标记携带任务解决信息，可以引导生成走向正确推理，而数学标记编码很少成功的接近答案的内容。修补的输出通常更短，但超过了完整CoT跟踪的准确性，这表明完整的推理链并不总是必要的。总而言之，这些发现表明CoT对可恢复的代币级问题解决信息进行编码，为推理如何表示及其在哪里分解提供了新的见解。

[阅读原文](https://arxiv.org/abs/2604.23351)

---

## 27. 连接推理与行动：用于高效跨领域面向任务对话的混合LLM-RL框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yangyang Zhao, Linfan Dai, Li Cai, Bowen Xing, Libo Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hybrid LLM-RL framework (VLK-RL) with verified constraint extraction for cross-domain task-oriented dialogue, directly matching RL for LLMs via a novel reward/state design.

**摘要**: arXiv：2604.23345v1宣布类型：新摘要：跨领域以任务为导向的对话需要在规划长期、多回合行动时对隐性和明确的可行性约束进行推理。大型语言模型（LLM）可以推断此类约束，但在长期范围内不可靠，而强化学习（RL）优化了长期行为，但无法从原始对话中恢复约束。因此，天真地将LLM与RL耦合是脆弱的：未经验证或非结构化的LLM输出可能会破坏状态表示并误导政策学习。出于此动机，我们提出了验证LLM知识授权RL（VLK-RL），这是一个混合框架，使LLM衍生的约束推理可用于RL。VLK-RL首先通过LLM激发候选约束，然后通过双重角色交叉检查程序验证它们，以抑制幻觉和交叉转弯不一致。经过验证的约束被映射到实体对齐的槽值表示中，从而产生结构化的约束感知状态，用于RL策略优化。多个基准测试的实验表明，VLK-RL显着提高了概括性和鲁棒性，在长期任务中优于强大的单模型基线。

[阅读原文](https://arxiv.org/abs/2604.23345)

---

## 28. DeepTaxon：一个用于统一物种识别和发现的可解释检索增强多模态框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiawei Wang, Ming Lei, Yaning Yang, Xinyan Lin, Yuquan Le, Qiwei Ma, Zhiwei Xu, Zheqi Lv, Yuchen Ang, Zhe Quan, Tat-Seng Chua

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL pipeline (RL on hard samples) for improving LLM-based species identification and discovery, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2604.24029v1公告类型：新摘要：在成千上万的视觉相似的类群中识别生物学中的物种，同时在开放世界环境中发现未知物种仍然是生物多样性研究的一个基本挑战。目前的方法将识别和发现作为单独的问题，分类模型假设闭集，发现依赖于基于阈值的拒绝。在这里，我们介绍了DeepTaxon，这是一个检索增强的多模式框架，通过对检索到的视觉证据的可解释推理来统一物种识别和发现。给定一张查询图像，DeepTaxon从检索索引中检索前k $$候选物种，每个样本图像均为$n$样本图像，并执行思想链比较推理。至关重要的是，我们将发现重新定义为一个显式的、基于检索的决策问题，而不是隐含的参数记忆问题。当且仅当检索索引缺乏足够的识别证据时，样本才是新颖的，因此每次检索自然会产生分类或发现标签，而无需手动注释，从而为这两项任务提供自动监督。我们通过对合成检索增强数据进行监督微调来训练框架，然后对硬样本进行强化学习，将高召回率检索转化为可扩展到大量分类词汇的高精度决策。对大规模分布内基准和六个分布外数据集的广泛实验表明，识别和发现方面都取得了一致的改进。消融研究进一步揭示了候选计数$k$和样本计数$n$的有效测试时间缩放、到未见域的强大零镜头转移以及检索编码器之间一致的性能，为生物多样性研究建立了可解释的解决方案。

[阅读原文](https://arxiv.org/abs/2604.24029)

---

## 29. TCOD：探索多回合自治代理的政策上蒸馏中的时态课程

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jiaqi Wang, Wenhao Zhang, Weijie Shi, Yaliang Li, James Cheng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a temporal curriculum for on-policy distillation to stabilize multi-turn agent learning, directly addressing self-improvement via interaction traces.

**摘要**: arXiv：2604.24005v1宣布类型：新摘要：政策提炼（OPD）已显示出将推理能力从前沿或特定领域模型转移到较小的学生的巨大潜力。虽然对静态单回合任务有效，但其在多回合代理设置中的行为仍然未充分研究。在这项工作中，我们确定了香草OPD在此类环境中的一个关键局限性，我们将其称为轨迹级KL不稳定性。具体来说，我们观察到KL分歧随着成功率下降而增加，即使在收敛之后，KL仍然很高，导致训练不稳定。这种不稳定性源于回合间错误的复合：随着错误的积累，学生会受到教师的有效支持的影响，从而导致监督信号不可靠。为了解决这个问题，我们建议TCOD（临时课程政策提炼），一个简单而有效的框架，控制向学生暴露的轨迹深度，并通过课程表逐步将其从短扩展到长。四对学生-教师对在三个多回合代理基准上的实验结果（ALFWorld、WebShop、ScienceWorld）表明，TCOD可以缓解KL升级并增强整个训练过程中的KL稳定性，比香草OPD提高多达18个百分点。进一步的评估表明，TCOD甚至可以超越教师的表现，并推广到教师失败的任务。

[阅读原文](https://arxiv.org/abs/2604.24005)

---

## 30. 解释质量评估作为列表奖励排名

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Thomas Bailleux, Tanmoy Mukherjee, Emmanuel Lonca, Pierre Marquis, Zied Bouraoui

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a ranking-based reward model for explanation quality that enables stable RL policy optimization, directly relevant to RL for LLMs via reward design.

**摘要**: arXiv：2604.24176v1宣布类型：新摘要：我们将解释质量评估重新定义为排名问题而不是生成问题。我们不是优化模型来逐句地产生单个“最佳”解释，而是训练奖励模型来区分多个候选解释并了解它们的相对质量。具体来说，我们构建具有分级质量水平的每实例候选集，并训练逐列表和逐成对排名模型（ListNet、Lambda Rank、RankNet），以保留有序结构并避免逐点回归或二元偏好目标典型的分数压缩。我们观察到三个发现：首先，在所有测试领域中，排名损失在评分分离方面始终优于回归。其次，最佳排名损失取决于数据特征：列表式目标在分离良好的质量层中表现出色，而成对方法对有噪音的自然注释更稳健。第三，当在精心策划和结构良好的数据上进行训练时，小型编码器模型可以匹配数量级更大的模型，这表明数据质量比模型规模更重要。最后，当在政策优化中用作奖励时，基于排名的分数可以在基于回归的奖励完全失败的环境中实现稳定的收敛。代码和数据可访问：https://github.com/Tankiit/PPO_Learning_to_rank

[阅读原文](https://arxiv.org/abs/2604.24176)

---

## 31. JigsawRL：组装RL管道以实现高效的LLM后培训

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhengding Hu, Hehua Ouyang, Chang Chen, Zaifeng Pan, Yue Guan, Zhongkai Yu, Zhen Wang, Steven Swanson, Yufei Ding

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes JigsawRL, a cost-efficient RL pipeline multiplexing framework that improves throughput for LLM post-training RL pipelines.

**摘要**: arXiv：2604.23838v1宣布类型：新摘要：我们介绍了JigsawRL，这是一个具有成本效益的框架，它探索了管道多路传输作为RL并行性的新维度。JigsawRL将每个管道分解为子阶段图，该图暴露了阶段级系统隐藏的阶段内和工作者之间的不平衡。在这个抽象上，JigsawRL通过动态资源分配来解决多路传输干扰，通过跨工作者迁移长尾展开来消除碎片化的利用，并将它们的协调制定为使用前瞻启发式解决的图调度问题。在跨不同代理RL管道和模型的4-64 H100/A100图形处理器上，JigsawRL的吞吐量比同步RL上的Verl高1.85倍，比StreamRL和AReaL高1.54倍，并支持具有中等延迟权衡的异类管道。

[阅读原文](https://arxiv.org/abs/2604.23838)

---

## 32. RL代币：使用视觉-语言-动作模型引导在线RL

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Charles Xu, Jost Tobias Springenberg, Michael Equi, Ali Amin, Adnan Esmail, Sergey Levine, Liyiming Ke

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a lightweight method (RL Token) for sample-efficient online RL fine-tuning of pretrained vision-language-action models on real robots.

**摘要**: arXiv：2604.23073v1宣布类型：新摘要：视觉语言动作（VLA）模型可以学习“开箱即用”执行各种操作技能，但实现现实世界任务所需的精确度和速度需要进一步微调--例如，通过强化学习（RL）。我们引入了一种轻量级方法，只需几个小时的现实世界实践即可对预训练的VGA进行样本高效的在线RL微调。我们（1）调整VLA以暴露“RL令牌”，这是一种紧凑的读出表示，它保留了与任务相关的预训练知识，同时充当在线RL的有效界面，以及（2）在此RL令牌上训练一个小的行动者-评论家头部以完善动作，同时将学到的策略锚定到VLA。具有RL令牌（RLT）的在线RL使得可以使用RL快速有效地微调甚至大型VLA。在四项真实机器人任务（螺丝安装、系带固定、充电器插入和以太网插入）中，RLT将任务中最困难部分的速度提高了高达3倍，并在几分钟到几个小时的练习内显着提高成功率。它甚至可以超越人类在某些任务上的遥操作速度。

[阅读原文](https://arxiv.org/abs/2604.23073)

---

## 33. 从企业客户支持工作流程中的副驾驶反馈学习选择性LLM自主性

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Nikita Borovkov, Elisei Rykov, Olga Tsymboi, Sergei Filimonov, Nikita Surnachev, Dmitry Bitman, Anatolii Potapov

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a deployed system for selective LLM autonomy that learns a critic from copilot feedback to calibrate abstention, forming a self-improving agent loop.

**摘要**: arXiv：2604.23855v1宣布类型：新摘要：我们提供了一个部署的系统，可以在企业业务流程管理（BPM）平台内自动化端到端客户支持工作流程。该方法在生产中具有可扩展性，并在两周内实现新流程的选择性自动化，利用已经大规模生成的监督：结构化的每例UI交互跟踪和低负担副驾驶反馈，操作员要么接受建议，要么提供纠正。分阶段部署管道训练下一个UI动作策略，从副驾驶员反馈中学习批评者以校准警告，并仅在后台执行高置信度步骤，同时推迟操作员的不确定决策并从更新的UI状态恢复。此设置允许一名操作员监督多个并发会话，并仅在系统不确定时中断。该系统在BPM界面的架构驱动视图上运行，并包括生产的监控和安全后备。在生产中，它自动化了45%的会话，并将平均处理时间减少了39%，而不会降低支持质量水平。

[阅读原文](https://arxiv.org/abs/2604.23855)

---

## 34. Meta Aligner：多目标LLM协调的双向偏好政策优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wenzhe Xu, Biao Liu, Yiyang Sun, Xin Geng, Ning Xu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a bi-level meta-learning framework for multi-objective LLM alignment that dynamically optimizes preference weights and policy responses bidirectionally.

**摘要**: arXiv：2604.24178v1公告类型：新摘要：多目标对齐旨在通过同时优化多个目标，将大型语言模型（LLM）与多样化且往往相互冲突的人类价值观对齐。现有的方法主要依赖于静态偏好权重构建策略。然而，与固定目标严格对齐会丢弃有价值的中间信息，因为即使偏离目标，训练响应本质上也体现了有效的偏好权衡。为了解决这一限制，我们建议Meal，即Meta ALigner是一个两级元学习框架，可实现偏好和政策响应之间的双向优化，为志愿者培训生成指导性的动态偏好。具体来说，我们引入偏好权重网作为元学习器，根据输入提示生成自适应偏好权重，并将偏好权重更新为可学习参数，而LLM策略充当基础学习器优化响应生成，以这些偏好为条件，并通过拒绝抽样策略。大量的实证结果表明，我们的方法在多个多目标基准上实现了卓越的性能，验证了动态双向偏好政策优化框架的有效性。

[阅读原文](https://arxiv.org/abs/2604.24178)

---

## 35. 与自己的声音保持一致：LVLM中的幻觉缓解的自我纠正偏好学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Byeonggeuk Lim, JungMin Yun, Junehyoung Kwon, Kyeonghyun Kim, YoungBin Kim

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes AVES-DPO, a self-corrected preference learning framework that uses in-distribution data from the model's intrinsic knowledge to mitigate hallucinations in LVLMs, directly matching RL for LLMs via a new reward/alignment pipeline.

**摘要**: arXiv：2604.24395v1宣布类型：新摘要：大型视觉语言模型（LVLM）经常出现幻觉。现有的基于偏好学习的方法主要依赖于专有模型来构建偏好数据集。我们发现这种依赖在专有模型和目标模型之间引入了分布不匹配，从而阻碍了有效的对齐。为了解决这个问题，我们提出了通过VErified Self-correction DPO（AVES-DPO）进行对齐，这是一个使用源自模型内在知识的分布数据来对齐LVLM的框架。我们的方法采用基于共识的验证机制来诊断各种幻觉并引导模型自我纠正，从而生成与其内部分布严格兼容的偏好对。大量实验表明，AVES-DPO在缓解幻觉方面超越了现有基线，同时仅需要52，000个样本。

[阅读原文](https://arxiv.org/abs/2604.24395)

---

## 36. CoFi-PGMA：多代理LLM过滤反馈下的反事实政策倾向

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Stela Tong, Elai Ben-Gal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a unified RL framework with counterfactual policy gradients for multi-agent LLM systems under filtered feedback, directly addressing RL for LLMs with novel reward design.

**摘要**: arXiv：2604.22785v1宣布类型：新摘要：大型语言模型（LLM）部署越来越依赖于多代理体系结构，其中多个模型要么通过路由机制竞争，要么协作产生最终答案。在这两种设置中，每个代理接收的学习信号都由系统机制过滤。路由产生选择门控反馈，其中仅评估所选择的响应，而协作产生共享奖励，掩盖了每个代理的个人贡献。因此，为单个部署策略设计的标准WLHF目标被错误指定。我们引入了CoFi-PGMA（多代理LLM过滤反馈下的反事实政策要素），这是多代理LLM系统中过滤反馈下学习的统一框架。我们的方法基于边际贡献推导出反事实的每个代理人训练目标，该目标在路由和协作机制下纠正学习信号。对于路由系统来说，目标对应于对选择门控反馈的非政策纠正，而对于协作系统来说，它简化为信用分配的留一差异奖励。我们进一步分析softmax路由如何引发风险敏感激励，并提供集成反事实估计器、多回合感知奖励和政策优化方法的实用训练算法，并在现实世界的推理数据集上演示该方法。

[阅读原文](https://arxiv.org/abs/2604.22785)

---

## 37. IRIS：交叉强化与增量阶段课程的跨语言数学推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Navya Gupta, Rishitej Reddy Vyalla, Avinash Anand, Chhavi Kirtani, Erik Cambria, Zhengchen Zhang, Zhengkui Wang, Timothy Liu, Aik Beng Ng, Simon See, Rajiv Ratn Shah

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes IRIS, a two-axis curriculum RL framework combining SFT and reverse curriculum RL with a composite reward for cross-lingual math reasoning, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2604.24114v1宣布类型：新摘要：课程学习通过逐渐增加任务难度来帮助语言模型解决复杂推理。然而，它往往无法产生一致的逐步推理，尤其是在多语言和资源匮乏的环境中，从英语到印度语的跨语言转移仍然有限。我们建议IRIS：交叉强化与增量阶段课程，这是一个两轴框架，将对逐渐困难的问题（垂直轴）的监督微调与反向课程强化学习相结合，以减少对分步指导（水平轴）的依赖。我们设计了一个综合奖励，将正确性、逐步一致性、连续性和数字激励相结合，并通过集团相对政策优化（GRPO）进行优化。我们发布了CL-Math，这是一个包含29，000个问题的数据集，带有英语、印地语和马拉地语的分步注释。在标准基准和精心策划的多语言测试集中，IRIS持续提高性能，在数学推理任务方面取得了强劲的成绩，在低资源和双语环境中取得了巨大的进步，同时在高资源语言方面也取得了适度的改进。

[阅读原文](https://arxiv.org/abs/2604.24114)

---

## 38. 超越注意力稳定性边界：抽象的自我合成推理协议

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dahlia Shehata, Ming Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a metacognitive agent framework (SSRP) with self-synthesizing reasoning protocols to overcome attention latching, directly addressing self-improving agent behavior via architectural separation of planning and execution.

**摘要**: arXiv：2604.24512v1宣布类型：新摘要：随着LLM代理向自主数字同事过渡，在非线性多轮对话中保持确定性目标导向成为架构瓶颈。我们在仅限解码器的自回归变形金刚中识别并正式化了一种系统性故障模式，称为注意力闩锁。这种现象是信息过度挤压的行为表现，当历史上下文的累积概率权重超过任务中间更新时就会发生，导致代理人尽管有明确的相互矛盾的指令，但仍然固定在过时的约束中。我们提出了自我合成推理协议（SSRP），这是一种元认知框架，它实现了高级架构规划（Architect）和逐轮程序执行（Executive）之间的离散分离。我们使用MultiWOZ 2.2数据集和聚合轴准确度（APA）评估9 K轨迹的SSRP，这是一种新颖的指标，我们通过将其分数映射到U形“迷失在中间”曲线来验证。我们提出了3个实验层：基于浅层最近的检索试点、高熵SOP和语义劫持的3跳多事实合成任务。我们的结果通过经验确定了注意力稳定性边界，其中GPT 5.4的无状态Vanilla ReAct基线下降至0.1%成功率，而SSRP则实现了715 X的韧性提升。我们证明了Gemini 3.1 Pro、Claude Sonnet 4.6和DeepSeek V3.2在统计上取得了显着的进步。审计通过通过循环反射基线证明注意力缺失（100%成功）来确认SSRP的必要性;通过等距压力测试（90%准确性）将闩锁与位置偏差脱钩;并通过信息瓶颈原则和粒度消融正式化SSRP。程序完整性审计（98.8%的遵守率）揭示了一种基础悖论，其中高稳定性模型因拒绝在检索推理污染下产生幻觉而失败。

[阅读原文](https://arxiv.org/abs/2604.24512)

---

## 39. POCA：视觉文本生成的帕累托最优课程调整

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yaohou Fan, Qingzhong Wang, Yongsong Huang, Junyi Liu, Tomo Miyazaki, Shinichiro Omachi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-based multi-objective alignment framework (POCA) using Pareto-optimality and curriculum learning for visual text generation, directly matching RL for LLMs criteria.

**摘要**: arXiv：2604.24171v1宣布类型：新摘要：当前的视觉文本生成模型很难在文本准确性和整体图像一致性之间做出权衡。我们发现，实现高文本准确性可能会降低美观质量和描述跟踪能力。尽管强化学习方法可以通过与多个奖励保持一致来缓解问题，但它们对于文本生成来说通常不稳定，因为现有方法通常以加权和的方式优化多个奖励。此外，很难平衡每个奖励的权重。此外，强化学习需要一套训练指令。大量的提示需要更多的训练时间和计算资源，而少量的提示会导致性能较差。因此，如何选择提示进行高效训练是一个未解决的问题。在本研究中，我们提出了帕累托最优课程调整（POCA），这是一个通过以下方式将此问题作为多目标问题来解决的框架：1）识别帕累托最优集以避免简单的缩放; 2）设计自适应课程调整策略以使用自动难度评估来管理多奖励数据集的学习序列，当RL方法在有限的数据环境中进行探索时，这对于最佳收敛至关重要。在协同作用中，POCA在统一的奖励空间中找到帕累托最优集，消除不一致的信号，以在易到难的优化环境下从不同的奖励中找到最佳的权衡解决方案。实验结果表明，POCA显着提高了CLIP、HPS分数和句子准确性等所有指标。

[阅读原文](https://arxiv.org/abs/2604.24171)

---

## 40. C-MORAL：LLM的可控制多目标分子优化和强化比对

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Rui Gao, Youngseung Jeon, Swastik Roy, Morteza Ziyadi, Xiang 'Anthony' Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforcement learning post-training framework for controllable multi-objective molecular optimization, directly matching RL for LLMs with a new reward aggregation method.

**摘要**: arXiv：2604.23061v1宣布类型：新摘要：大型语言模型（LLM）显示出分子优化的前景，但将它们与选择性和竞争性的药物设计约束保持一致仍然具有挑战性。我们提出了C-Moral，这是一种用于可控多目标分子优化的强化学习训练后框架。C-Moral结合了基于群体的相对优化、针对不同目标的房产评分对齐以及连续非线性奖励聚合，以提高竞争房产的稳定性。C-MuMODirecct基准测试的实验表明，C-Moral在域内和域外设置中始终优于最先进的模型，在IND任务中实现了48.9%的最佳成功优化率（SEN），在OOD任务中实现了39.5%的最佳成功优化率（SEN），同时在很大程度上保留了支架相似性。这些结果表明，RL后训练是将分子语言模型与连续分子设计目标保持一致的有效方法。我们的代码和模型可在https://github.com/Rwigie/C-MORAL上公开获取。

[阅读原文](https://arxiv.org/abs/2604.23061)

---

## 41. EPM-RL：电子商务中基于本地产品映射的强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Minhyeong Yu, Wonduk Seo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes EPM-RL, a reinforcement learning framework that distills agentic reasoning into a trainable model for product mapping, using an agent-based reward for optimization.

**摘要**: arXiv：2604.23993v1宣布类型：新摘要：产品地图是确定两个电子商务商品列表是否涉及同一产品的任务，是价格监控和渠道可见性的核心问题。然而，在真实的市场中，卖家经常将促销关键词、平台特定标签和捆绑描述注入到标题中，导致同一产品出现在许多不同的名称下。最近的基于LLM和多代理的框架提高了此类困难案例的稳健性和可解释性，但它们通常依赖于昂贵的外部API、重复检索和复杂的推理时编排，使得大规模部署成本高昂且困难。隐私敏感的企业环境。为了解决这些问题，我们提出了EPM-RL，这是一个基于业务学习的框架，用于构建准确有效的内部部署电子商务产品映射模型。我们的中心思想是将高成本的代理推理提炼成可训练的内部模型。从具有LLM生成的原理和人工验证的一组精心策划的产品对开始，我们首先使用结构化推理输出对小型学生模型执行参数高效微调（PEFT）。然后，我们使用基于代理的奖励，通过强化学习（RL）进一步优化模型，该奖励联合评估输出格式合规性、标签正确性、推理--来自专门设计的法官模型的偏好分数。初步结果表明，EPM-RL始终优于纯PEFT培训，并提供了比基于API的商业基线更强的质量成本权衡，同时支持私人部署和更低的运营成本。这些发现表明，强化学习可以将产品映射从高延迟代理管道转变为可扩展、可检查且可生产的内部系统。

[阅读原文](https://arxiv.org/abs/2604.23993)

---

## 42. 通过分步优势选择稳定高效推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 6/10

**作者**: Han Wang, Xiaodong Yu, Jialian Wu, Jiang Liu, Ximeng Sun, Mohit Bansal, Zicheng Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Step-level Advantage Selection (SAS) for stabilizing efficient reasoning in LLMs via RL, directly addressing RL for LLMs with a new reward/advantage mechanism at the step level.

**摘要**: arXiv：2604.24003v1宣布类型：新摘要：大型语言模型（LLM）通过在推理时分配大量计算来实现强大的推理性能，通常生成长而冗长的推理痕迹。虽然最近关于高效推理的工作通过基于长度的奖励或修剪减少了这种负担，但许多方法都是在比基本模型训练短得多的上下文窗口下进行的后训练的，这是一个影响尚未被系统地孤立的因素。我们首先表明，单独使用短上下文后训练，使用标准GRPO，而没有任何长度感知目标，已经引发了大量的推理压缩，但代价是训练动态日益不稳定和准确性下降。为了解决这个问题，我们提出了步骤级优势选择（SAS），它在推理步骤级运行，并为正确推出中的低置信步骤和验证器失败的推出中的高置信步骤分配零优势，其中失败通常是由于截断或验证器问题而不是错误推理。在各种数学和一般推理基准中，SAS将平均Pass@1准确性比最强的长度感知基线提高了0.86个百分点，同时将平均推理长度减少了16.3%，从而实现了更好的准确性-效率权衡。

[阅读原文](https://arxiv.org/abs/2604.24003)

---

