# 💡 今日研究速览 (Daily Summary)

### RL for LLMs

Today marks a significant deepening in our theoretical and practical understanding of reinforcement learning for large language models. A cluster of papers moves beyond the standard PPO/DPO dichotomy to address fundamental bottlenecks. The *Value-Gradient Hypothesis* provides a unifying theoretical lens for critic-free methods, explaining the conditions under which PPO and GRPO excel. Directly addressing training stability, *Survive or Collapse* identifies data-level gating, not reward design, as the binding constraint in self-play, introducing the Grounded Proposer Paradox. On the algorithmic front, *OPPO* achieves token-level credit assignment without a learned value network via Bayesian value recursion, while *SCRL* decomposes reasoning chains into verifiable subproblems for finer-grained credit. The issue of self-improvement is tackled by *One-Way Policy Optimization (OWPO)*, which decouples optimization direction from magnitude to enable continuous evolution without reference models, and *Self-Policy Distillation (SPD)* uses capability-selective subspace projection for a new self-improvement loop. Practical advances include *Unified Data Selection (HES)*, a training-free metric validated across SFT and RL pipelines, and *Clipping Bottleneck*, which identifies and stochastically rescues near-boundary signals to stabilize RLVR. Finally, *Two is better than one* proposes a multi-reward RLIF framework with KL-Cov regularization to prevent collapse in unsupervised reasoning training.

### Agents & Self-Evolving Systems

The theme of closed-loop, self-improving agents dominates today's research, moving from static tool-use to dynamic, experience-driven evolution. *GenEvolve* introduces a self-evolving image generation agent that distills tool-orchestrated trajectories into visual experience, creating a closed-loop improvement cycle. *FlyRoute* proposes a data flywheel for adaptive task routing via self-evolving agent profiling. For long-horizon tasks, *Memory-R2* uses LoGo-GRPO for fair credit assignment in memory-augmented agents, while *MoLEM* prevents catastrophic forgetting through a dynamic mixture of latent memories. *EvoIR-Agent* applies this philosophy to image restoration, using a hierarchical experience pool for self-evolution. *SOLAR* pushes the boundary further with a meta-learning and multi-level RL framework for lifelong, open-ended adaptation. *ACC* compiles agent trajectories into long-context QA pairs for training, enabling self-improvement from raw interaction traces. The *COSMO-Agent* framework orchestrates closed-loop CAD-CAE optimization via tool-augmented RL, demonstrating real-world applicability. *Reinforced Graph of Thoughts (RGoT)* uses RL to dynamically generate reasoning structures, and *Maestro* orchestrates hierarchical ensembles of frozen expert models via RL.

### Multimodal & Vision-Language Models

Multimodal reasoning is seeing a paradigm shift towards latent reasoning and visual-grounded RL. *LatentOmni* replaces explicit text-based chain-of-thought with unified latent-space reasoning for audio-visual understanding, directly challenging the necessity of token-level CoT. *Faithful-MR1* uses RLVR to anchor and reinforce visual attention for faithful multimodal reasoning. For Video LLMs, *EvoVid* proposes a temporal-centric self-evolution framework using RL with novel temporal rewards, and *CRPO* uses counterfactual reinforcement learning to learn spatiotemporal sensitivity. *Visual-Advantage On-Policy Distillation (VA-OPD)* introduces a token-level visual advantage signal to improve VLMs' reliance on visual input. *SegCompass* explores interpretable alignment with sparse autoencoders for enhanced reasoning segmentation, integrating RL for reasoning path optimization.

### Alignment & Safety

Alignment research today focuses on provable guarantees, on-policy consistency, and mitigating specific failure modes. *Conditional Equivalence of DPO and RLHF* proposes Constrained Preference Optimization (CPO) to fix DPO's failure modes with explicit constraints, providing provable alignment. *On-Policy Consistency Training (OPCT)* improves LLM safety with minimal capability degradation through on-policy supervision. *Reducing Political Manipulation with Consistency Training* introduces Political Consistency Training (PCT) with novel sentiment and helpfulness consistency rewards. *Why Semantic Entropy Fails* proposes GCPO, a geometry-aware and calibrated uncertainty framework for policy optimization, addressing gradient variance. *Token-weighted Direct Preference Optimization with Attention (AttentionPO)* uses LLM attention for content-aware token weighting in DPO.

### Reasoning & Latent Reasoning

The frontier of reasoning research is expanding to include verification during search, curriculum learning, and specialized domains. *Can Transformers Learn to Verify During Backtracking Search?* proposes Selective State Attention to enable state-based backtracking verification, a critical fix for reasoning over serialized search traces. *Ablate-to-Validate* introduces the Token Replacement Test (TRT) to diagnose whether latent/continuous thought tokens are genuinely used for reasoning, addressing a core evaluation gap. *Integrating Chain-of-Thought into Generative Retrieval (ThinkGR)* proposes a unified framework with hybrid decoding and retrieval-grounded RL. *Tailoring Teaching to Aptitude (DASD)* adapts teacher supervision direction based on token entropy to preserve exploration in self-distillation. *When Are Teacher Tokens Reliable?* proposes Position-Weighted On-Policy Self-Distillation (PW-OPSD) for reasoning. *Teaching Language Models to Forecast Research Success* uses RLVR for comparative idea evaluation. *LANG* improves multilingual reasoning via language-adaptive hint guidance. *Reasoning through Verifiable Forecast Actions (StockR1)* optimizes financial LLMs with consistency-grounded rewards.

### Post-Training & Training Dynamics

A fundamental rethinking of post-training is underway. *Post-Training is About States, Not Tokens* argues that the state distribution on which supervision is applied is as important as the loss function, supported by controlled experiments. *F-TIS* enables heterogeneous models to collaborate in GRPO via filtered truncated importance sampling. *DeferMem* uses a novel DistillPO algorithm for query-conditioned evidence distillation in long-term memory QA. *HealthCraft* introduces a new RL safety environment for emergency medicine with trajectory-level safety rewards. *Vector Policy Optimization (VPO)* trains LLMs to produce diverse solutions for improved test-time search, directly addressing diversity in RL training.

---

## 1. 载体策略优化：多样性训练改善测试时间搜索

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong, Pulkit Agrawal

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Vector Policy Optimization (VPO), a novel RL algorithm that trains LLMs to produce diverse solutions for improved test-time search, directly addressing RL for LLMs.

**摘要**: arXiv：2605.22817v1宣布类型：新摘要：语言模型现在必须开箱即用地推广到新颖的环境，并在推理缩放搜索过程中工作，例如AlphaEvolve，该过程选择具有各种特定任务奖励功能的展开。不幸的是，LLM后训练的标准范式优化了预先指定的纯量奖励，通常导致当前的LLM产生低熵响应分布，从而难以显示推断时搜索所需的多样性。我们提出了载体政策优化（VPO），这是一种RL算法，可以显式地训练政策以预测不同的下游回报函数并产生不同的解决方案。VPO利用奖励在实践中通常是以载体为价值的，例如代码生成中的每个测试案例的正确性，或者（例如）多个不同的用户角色或奖励模型。VPO本质上是GRPO优势估计器的直接替代品，但它训练LLM输出一组解决方案，其中单个解决方案专门针对载体回报空间中的不同权衡。在四个任务中，VPO匹配或超过测试时搜索中最强的纯量RL基线（例如，通过@k和best@k），随着搜索预算的增长，差距不断扩大。对于进化搜索，VPO模型解开了GRPO模型根本无法解决的问题。随着测试时搜索变得更加标准化，优化多样性可能需要成为默认的训练后目标。

[阅读原文](https://arxiv.org/abs/2605.22817)

---

## 2. 生存还是崩溃：自我游戏强化学习中数据门控和奖励基础的非对称作用

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sophia Xiao Pu, Zhaotian Weng, Chengzhi Liu, Jayanth Srinivasa, Gaowen Liu, William Yang Wang, Xin Eric Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a fundamental analysis of self-play RL stability, revealing data-level gating as the binding constraint over reward design, with a novel Grounded Proposer Paradox.

**摘要**: arXiv：2605.22217v1宣布类型：新摘要：自我游戏强化学习根据自己生成的任务训练语言模型，共同进化没有人类标签的提议者和求解器。最近的系统报告了强大的推理收益，但崩溃和不稳定性被广泛观察到，但理解却很少。占主导地位的反应将其视为奖励设计问题。相反，我们认为，自我游戏稳定性由两个不同的杠杆控制：一个数据级门，决定哪些传播者生成的任务进入训练池，以及更新已接受任务政策的奖励信号。通过对Python输出预测任务和确定性-dsl双任务（去除预训练先验、输出模糊性和执行者噪音）的对照实验，我们发现这两个杠杆是不对称的。严格的门足以保证我们测试的每个奖励变体的稳定性，包括无法访问基本真相的自我一致性奖励;而一旦门被移除，任何奖励变体都是足够的。这种不对称性暴露了一种反直觉的耦合，我们称之为“接地提议者悖论”：当与自相容性求解器配对时，具有地面真相访问的提议者通过集中训练在干净的任务上，加速崩溃的速度比无接地的提议者更快，这些任务形成了通往虚假自相容吸引子的最快路径。用连续严格性参数$\varepSYS $替换二进制门进一步揭示了两阶段阶段的阶段转变：训练端指标在低$\varepSYS $时脱钩，而验证准确性保持不变，直到$\varepSYS $更高。数据级门控（而不是奖励校准）是对自我游戏稳定性的约束。

[阅读原文](https://arxiv.org/abs/2605.22217)

---

## 3. OPPO：LLM推理中令牌级信用分配的Bayesian值回归

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yu Li, Rui Miao, Tian Lan, Zhengling Qi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes OPPO, a novel RL method for LLM reasoning that uses Bayesian value recursion for token-level credit assignment without a learned value network, improving over GRPO on math and code benchmarks.

**摘要**: arXiv：2605.21851v1宣布类型：新摘要：具有可验证奖励的强化学习已成为改进LLM推理的标准配方，但占主导地位的算法GRPO为每个令牌分配了单个子级优势，在关键推理步骤稀释信号，并在无信息的步骤注入噪音。从按政策蒸馏中衍生的无批判替代方案通过Oracle条件似然比提供每个代币的信号，但与该位置积累的子级证据隔离地应用每个信号。我们提出了Oracle默认的政策优化（OPPO），它基于一个单一的观察：先前的蒸馏式方法用于局部区分的Oracle信号也是模型对最终成功信念的自然Bayesian更新。沿着轨迹累积信号，以封闭形式并以一次额外向前传递为代价，产生每个位置成功概率的运行估计，以及不需要学习价值网络和额外部署的代币级优势。一级分析将优势分解为由状态权重调制的蒸馏方法使用的每代币区分信号，该权重将信用集中在真正关键的代币上，并有定向方差减少保证。该框架允许两个估计器，仅在哪一个模型对证据进行评分方面有所不同：一个是重复使用学生并将政策上的蒸馏奖励恢复为严格的特殊情况，另一个是\textit{teacher-Oracle}，将评分委托给更强的冻结模型。在跨越七个数学、科学和代码推理基准的两个基本LLM上，OPPO在AMC ' 23上比GRPO、DAPO和SDPO提高了高达+6.0美元分，在AIME ' 24上提高了+5.2美元分，其收益随着响应长度单调扩大。

[阅读原文](https://arxiv.org/abs/2605.21851)

---

## 4. LLM RL的价值梯度假设

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Arip Asadulaev, Daniil Ognev, Karim Salta, Martin Takac

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Develops a value-gradient perspective of critic-free RL for LLMs, providing theoretical analysis of why PPO/GRPO work and when they are most effective, directly contributing to RL for LLMs.

**摘要**: arXiv：2605.21654v1宣布类型：新摘要：强化学习极大地改善了预训练的语言模型，但人们仍然没有充分研究为什么PPO和GRPO等无批评方法能如此有效，以及它们何时应该提供最大的收益。我们为LLM后培训开发了无批评RL的价值梯度视角。首先，在可微展开和添加性噪音参数化下，我们表明参与者更新在期望方面是类似值梯度的：向后传递传播条件期望等于值梯度的余项。其次，对于离散的Transformer政策，我们表明，通过注意力的自分化会产生逼近该值信号的经验协态，误差由采样间隙和政策信息量控制。这些结果促使将RL影响分解为价值梯度信号和可达回报余量，从而得出RL何时应该在预训练轨迹上最有效的标准。

[阅读原文](https://arxiv.org/abs/2605.21654)

---

## 5. DPO和WLHF的条件等效性：隐性假设、失败模式和可证明的对齐

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zhiqin Yang, Yonggang Zhang, Wei Xue, Dong Fang, Bo Han, Yike Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Constrained Preference Optimization (CPO), a new RL method that provably aligns LLMs by fixing DPO's failure modes with explicit constraints.

**摘要**: arXiv：2605.20834v1宣布类型：新摘要：直接偏好优化（DPO）已成为人类反馈强化学习（RL HF）的流行替代方案，通过更简单的实现提供理论等效性。我们证明这种等效性是有条件的，而不是普遍的，这取决于实践中经常违反的隐含假设：RLHF最优政策必须更喜欢人类偏好的反应。当这一假设失败时，DPO会优化相对于参考政策的相对优势，而不是与人类偏好的绝对一致，从而导致病理性趋同，即政策减少DPO损失，同时更喜欢不被忽视的反应。我们描述了何时违反这一假设，证明了不需要的解空间的存在，并证明DPO和RL HF在这种情况下优化了根本不同的目标。为了解决这个问题，我们引入了约束偏好优化（CPO），通过可证明对齐的约束来增强RL HF。我们进一步通过软利润排名提供了几何解释，揭示了DPO实施的利润排名具有潜在负面目标。我们的理论分析确定了DPO的保证何时成立，并提供了保持简单性且具有可证明一致性的解决方案。对标准基准的全面实验表明CPO实现了最先进的性能。代码可访问：https://github.com/visitworld123/CPO。

[阅读原文](https://arxiv.org/abs/2605.20834)

---

## 6. GenEvolve：通过工具配置的视觉体验蒸馏自进化的图像生成代理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Sixiang Chen, Zhaohu Xing, Tian Ye, Xinyu Geng, Yunlong Lin, Jianyu Lai, Xuanhua He, Fuxiang Zhai, Jialin Gao, Lei Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces GenEvolve, a self-evolving image generation agent that uses tool-orchestrated trajectories and visual experience distillation for closed-loop improvement.

**摘要**: arXiv：2605.21605v1宣布类型：新摘要：开放式图像生成不再是简单的预算到图像问题。高质量的生成通常需要代理将模型的内部生成能力与外部资源相结合。随着请求变得更加多样化和要求越来越高，我们的目标是开发一种通用的图像生成代理，它可以通过轨迹自我进化，并在各种生成挑战中更有效地使用工具。为此，我们提出了GenEvolve，这是一个基于工具描绘的视觉体验蒸馏的自我进化框架。在GenEvolve中，每一次生成尝试都被建模为一个工具精心策划的轨迹，其中代理收集证据、选择引用、调用生成技能，并将其组成预算引用程序。与主要依赖图像级纯量奖励的现有代理生成方法不同，GenEvolve比较同一请求的多个轨迹，并将最佳与最差差异抽象为结构化视觉体验，仅提供给特权教师分支。视觉体验蒸馏受到政策上自我提炼的启发，提供密集的代币级监督，帮助学生内化更好的搜索、知识激活、参考文献选择和及时构建。我们进一步构建了GenEvolve-Data和GenEvolve-Bench。在公共基准测试和GenEvolve-Bench上的实验显示，在强基线上取得了实质性的进步，在当前的图像生成框架中实现了最先进的性能。我们的网站如下：https://ephemeral182.github.io/GenEvolve/

[阅读原文](https://arxiv.org/abs/2605.21605)

---

## 7. 从抽象到抽象：视觉语言模型真的使用连续思维代币吗？

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tianyi Zhang, Mahtab Bigverdi, Ranjay Krishna

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces the Token Replacement Test (TRT) to diagnose whether latent/continuous thought tokens are genuinely used for reasoning, directly addressing a core evaluation gap in latent reasoning.

**摘要**: arXiv：2605.21642v1宣布类型：新摘要：视觉语言模型（VLM）越来越多地被旨在支持“视觉思维”的连续或潜在的非文本标记所增强。“尽管任务准确性有所提高，但仅这一点并不表明模型实际上使用这些令牌进行推理--增加上下文长度、特殊令牌锚定或训练时正规化等混淆可能会带来收益。我们正式化了一个诊断原则“烧到烧”，用于测试潜在令牌内容是否真正被利用，并将其实例化为令牌替换测试（TRT），这是一套标准化的内容替换烧蚀套件。TRT保持提示、图像、令牌预算和解码固定，同时用零、随机、首次重复或Oracle替代方案替换中间令牌，隔离性能取决于令牌内容还是仅取决于令牌存在。作为受控测试平台，我们使用LLaVA-13 B和Qwen 2.5-BL-3B研究相对深度推理，训练模型来预测和消费多个冻结编码器（SigLIP 2、CLIP、DINOv 2）和代币预算之间的连续或离散深度跨度。我们还将TRT应用于BLINK、NSX和CV-Bench上的三个现成视觉思维系统（幻影、Mull-Tokens、CoVT）。在所有设置中，准确性的提高都是潜在令牌推理的误导性代理：即使令牌内容被损坏或替换，VLM也能保留最大的改进，这揭示了拥有潜在通道和将其用作信息瓶颈之间的持续差距。我们建议TRT作为标准诊断，并建议任何引入连续思维标记的方法都具有准确性。

[阅读原文](https://arxiv.org/abs/2605.21642)

---

## 8. LatentOmni：通过统一视听潜在推理重新思考全模式理解

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yifan Dai, Zhenhua Wu, Bohan Zeng, Daili Hua, Jialing Liu, Bozhou Li, Yuran Wang, Chengzhuo Tong, Hao Liang, Xiaochen Ma, Junbo Niu, Tianyu Guo, Yang Shi, Yue Ding, Yiyan Ji, Bingyin Mei, Yushuo Guan, Yuanxing Zhang, Pengfei Wan, Fangcheng Fu, Wentao Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LatentOmni, a novel latent reasoning architecture for audio-visual understanding that replaces explicit text-based CoT with unified latent-space reasoning, directly matching the latent CoT/reasoning criterion.

**摘要**: arXiv：2605.22012v1宣布类型：新摘要：联合视听推理对于全模式理解至关重要，但当推理需要来自两种模式的细粒度证据时，当前的多模式大型语言模型（MLLM）仍然很困难。一个核心局限性是，显式的基于文本的思维链（CoT）将连续的视听信号压缩为离散的标记，削弱了时间基础并将中间推理转向语言先验。我们认为，统一的潜在空间是此类推理的更好媒介，因为它保留了密集的感官信息，同时保持与自回归生成兼容。基于这一见解，我们提出了\textBF{LatentOmni}，这是一个跨模式推理框架，它将文本推理与视听潜在状态交织在一起。LatentOmni引入特征级监督，将潜在推理状态与任务相关的感官特征保持一致，并使用Omni-同步位置嵌入（OSPE）来保持潜在音频和视觉状态之间的时间一致性。我们进一步构建\textBF{LatentOmni-Direct-35 K}，这是一个用于监督潜在空间推理的视听交织推理轨迹数据集。对多个视听推理基准的综合评估表明，LatentOmni在评估的开源模型中实现了最佳性能，并且始终优于Exicit文本CoT基线，支持潜空联合推理作为实现更强全模式理解的有希望的途径。

[阅读原文](https://arxiv.org/abs/2605.22012)

---

## 9. FlyRoute：通过数据飞轮进行自适应任务路由的自进化代理分析

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Rongjun Li, Ziyu Zhou, Yihang Wu

**机构**: Unknown Institution (proprietary enterprise dataset)

**💡 亮点 (Highlight)**: Proposes a self-evolving agent profiling framework (FlyRoute) that uses a data flywheel to improve task routing accuracy over time.

**摘要**: arXiv：2605.22057v1宣布类型：新摘要：企业路由器将查询分配给专家代理，但在代理发展（提示、工具、模型）时，部署的配置文件保持静态，开发人员很少保持最新的描述或示例。我们介绍了FlyRoute，这是一个自我进化的分析框架，可以从真实流量中增长能力证据：将候选者、质量门控成功对分配到每个代理的成功存储中，定期将证据提取到学习到的能力描述中，并将这些描述与BM 25检索的成功一起注入LLM路由器。为了使这个飞轮的数据高效，FlyRoute引入了一项有针对性的探索政策，该政策结合了概况不确定性、BM 25相关性和词汇新颖性，仅优先考虑未充分分析的代理以进行合理的查询，并避免多余的证据收集。在我们专有的企业开发人员支持真实路由查询数据集的实验中，FlyRoute将同一主干零触发LLM路由器从72.57%提高到78.04%，每个代理只有5个种子查询，这表明配置文件检索已经加强了冷启动路由。通过惯性传输7，211个带标签的训练查询后，准确率上升至89.83%（零触发+17.26pp;冷启动+11.79pp），在单金测试查询的标准路由准确性下，四个专家域的准确性一致。

[阅读原文](https://arxiv.org/abs/2605.22057)

---

## 10. 从推理链到可验证子问题：课程强化学习实现LLM推理的学分分配

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Xitai Jiang, Zihan Tang, Wenze Lin, Yang Yue, Shenzhi Wang, Gao Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SCRL, a curriculum RL framework that derives verifiable subproblems from reasoning chains for finer-grained credit assignment in LLM reasoning, directly matching RL for LLMs criteria.

**摘要**: arXiv：2605.22074v1公告类型：新摘要：来自可验证奖励的强化学习（RLVR）在LLM推理方面表现出了很好的前景，但基于结果的RLVR在解决难题时仍然效率低下，因为正确的最终答案很少，并且样本级信用分配无法在失败的尝试中使用部分进展。我们介绍SCRL（子问题课程强化学习），课程RL框架，从参考推理链中导出可验证的子问题，并将最终子问题固定为原始问题。这将难题上的部分进展转化为可验证的学习信号。从数学上讲，SCRL使用子问题级别的标准化，它在每个子问题位置独立标准化奖励，并将由此产生的优势分配给相应的答案范围，从而实现更细粒度的信用分配，而无需外部规则或奖励模型。我们的分析表明，子问题课程可以将困难问题从梯度死角中提升出来，随着原始问题变得更难，相对收益也更大。在七个数学推理基准中，SCRL的表现优于强大的课程学习基线，在Qwen 3 - 4 B-Base上比GRPO的平均准确性提高了+4.1分，在Qwen 3 - 14 B-Base上提高了+1.9分。在AIME 24、AIME 25和IMO-Bench上，SCRL在Qwen 3 - 4 B-Base上进一步提高了pass@1 +3.7分，将pass@64提高了+4.6分，表明对硬推理问题的探索更好。

[阅读原文](https://arxiv.org/abs/2605.22074)

---

## 11. 自进化LLM的单向策略优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Shuo Yang, Jinda Lu, Kexin Huang, Chiyu Ma, Shaohang Wei, Yuyang Liu, Guoyin Wang, Jingren Zhou, Li Yuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes One-Way Policy Optimization (OWPO), a new RLVR method for self-evolving LLMs that decouples optimization direction from update magnitude to enable continuous self-improvement without external reference models.

**摘要**: arXiv：2605.22156v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）已成为扩展大型语言模型（LLM）推理能力的一个有前途的范式。然而，二进制验证者奖励的稀疏性常常导致效率低下和优化不稳定。为了稳定培训，现有方法通常会施加相对于参考政策的代币级别限制。我们发现，此类约束不加区别地惩罚偏差;当政策试图优于参考时，这可能会翻转验证者确定的方向，从而抑制收益。为了解决这个问题，我们提出了单向政策优化（OWPO），这是一种基于优化方向与更新幅度脱钩原则的方法。在OWPO中，验证者规定更新方向，而参考策略仅用于调整幅度。具体而言，OWPO应用不对称重新加权：它对劣偏差（策略落后于参考）执行加速对齐，对优偏差（策略超过参考）执行增益锁定。此外，通过纳入迭代参考更新，OWPO创建了一个不断巩固成果的“棘轮工具”。实验结果表明，OWPO优于强基线，包括DAPO，OPD和MOPD，打破了固定先验的瓶颈，使连续的自我进化，而不依赖于外部参考模型。

[阅读原文](https://arxiv.org/abs/2605.22156)

---

## 12. 变形金刚可以在回溯搜索期间学习验证吗？

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 8/10

**作者**: Yin Jun Phua, Tony Ribeiro, Tuan Nguyen, Katsumi Inoue

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a structural fix (Selective State Attention) to enable transformers to perform state-based backtracking verification, addressing a key failure mode in reasoning over serialized search traces.

**摘要**: arXiv：2605.2221v1宣布类型：新摘要：回溯搜索是经典约束求解器、规划器和定理证明器的基础。最近的基于变换器的推理系统通过自己的中间步骤探索搜索树。常见的训练食谱适合离线求解器轨迹上的自回归下一个令牌损失。模型在每个步骤的输入是所有先前决策的累积跟踪。最佳继续或回溯预测器仅取决于当前搜索状态，因为到达相同状态的两个轨迹允许相同的可行继续。我们表明，在累积轨迹上训练的纯解码器转换器在两种方式上未能满足这一要求：轨迹可以在许多位置上分散状态特征（分散检索），预测器可以根据轨迹而不是状态（历史纠缠）。我们通过本地化来解决分散检索问题，这是一种跟踪级修复，可以重写每个决策块以在本地暴露状态特征。我们通过选择性状态注意力（SSA）来解决历史纠缠，这是一种固定注意力面具，可以在结构上强制执行基于状态的决策，而无需修改训练数据、目标或参数。在传播暴露了矛盾之后，我们专注于反应式验证。我们在3-SAT、图形着色、Blocks World和回溯解析上测试了DSA。在仅在既往历史上不同的同一州对上，DSA会做出相同的决定，而累积训练的因果基线则不会。我们的贡献是对序列化轨迹数据上的Transformer行为进行诊断，并配合结构修复。搜索自己推理步骤的预训练语言模型可能会面临同样的失败。我们的分析将推理时上下文清理作为无需再培训即可应用相同隔离的候选方法。

[阅读原文](https://arxiv.org/abs/2605.22221)

---

## 13. EvoVid：视频大型语言模型的以时间为中心的自我进化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shiqi Huang, Ziyue Wang, Zhongrong Zuo, Han Qiu, Qi She, Bihan Wen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a temporal-centric self-evolving framework for Video-LLMs using RL with novel temporal rewards, enabling improvement from unannotated videos.

**摘要**: arXiv：2605.21931v1宣布类型：新摘要：最近的视频大型语言模型（Video-LLM）通过强化学习（RL）展示了强大的视频推理能力。然而，现有的RL管道严重依赖人工注释的任务和解决方案，这使得它们的规模成本高昂，并且从根本上受到人类专业知识的限制。自我进化的框架最近通过自主的决策者-解决者自我游戏而成为一种有希望的替代方案。不幸的是，这些方法主要是为文本和图像等静态模式设计的，从根本上无法捕捉视频推理核心的时间动态。在这项工作中，我们提出了$\textBF{EvoVid}$，这是一个以时间为中心的自我进化框架，使Video-LLM能够直接从原始的、未注释的视频中进行改进。具体来说，我们引入了两个补充的以时间为中心的奖励：一个时间感知的提问者奖励，通过时间扰动敏感性鼓励时间依赖的问题生成，以及一个基于时间的解决者奖励，通过固有的视频片段定位提供自动时间监督。针对四个基本模型和六个基准的广泛实验表明，基本模型和现有的自我进化基线都得到了一致的改进，通过监督方法实现了有竞争力的性能。这些结果强调了以时间为中心的自我进化是视频理解和推理的有效且可扩展的范式。

[阅读原文](https://arxiv.org/abs/2605.21931)

---

## 14. 通过能力选择子空间投影的自我政策提炼

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Guangya Hao, Yitong Shang, Yunbo Long, Zhuokai Zhao, Hanxue Liang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Self-Policy Distillation (SPD), a novel self-distillation method for LLMs that uses a capability-selective subspace projection to improve reasoning without external signals, directly relevant to RL for LLMs via a new self-improvement loop.

**摘要**: arXiv：2605.22675v1宣布类型：新摘要：自我蒸馏通过在自己的世代上进行训练来引导大型语言模型（LLM）。然而，现有方法要么依赖外部信号来策划自生成的输出（例如，正确性过滤、执行反馈和奖励搜索），这对于性能最佳的前沿模型来说成本高昂且不可用，或者完全跳过策展并在所有原始输出上进行训练，这种方法通常是特定领域且难以概括的。两者还有一个更深层次的弱点，即自我生成的输出将任务相关能力与其他能力纠缠在一起，例如风格模式、格式文物和特定于模型的错误，从而稀释了目标改进的特定能力的信号。在本文中，我们提出了自我策略蒸馏（SPD），它在没有任何外部信号的情况下实现了可推广、能力选择性。具体来说，SPD从模型自身在正确性定义令牌上的梯度中提取低等级能力子空间，在自我生成期间将关键值（KV）激活投影到该子空间中，并通过标准的下一个令牌预测损失对所得原始输出进行微调。通过代码生成、数学推理和多项选择QA的广泛实验，我们表明SPD比没有外部信号的最先进的自蒸馏方法实现了高达13%的改进，比预训练的基线实现了高达16%的改进。值得注意的是，SPD表现出卓越的概括性，在域外概括设置下实现了15%的性能提高。

[阅读原文](https://arxiv.org/abs/2605.22675)

---

## 15. LLM推理的统一数据选择

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xiaoyuan Li, Yubo Ma, Chengpeng Li, Fengbin Zhu, Yiyao Yu, Keqin Bao, Wenjie Wang, Fuli Feng, Dayiheng Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training-free metric (HES) for data selection in LLM reasoning, validated across SFT, RFT, and RL pipelines, directly improving RL-based reasoning training.

**摘要**: arXiv：2605.22389v1宣布类型：新摘要：有效训练大型语言模型（LLM）以进行复杂、长CoT推理通常会受到对大量高质量推理数据的需求的限制。现有的方法要么计算昂贵，要么无法可靠地区分高质量推理样本和低质量推理样本。为了解决这个问题，我们提出了高Entropy Sum（IES），这是一种免训练的指标，通过仅对顶层的信息进行相加来量化推理质量（例如，0.5\%）每个推理样本中的最高熵标记。我们在三种主流训练范式中验证了HE：监督微调（SFT）、拒绝微调（RFT）和强化学习（RL），大量结果证明了其一致的有效性和显着降低的计算负担。在SFT中，在HS排名前20%的数据上进行训练与全数据集的性能相匹配，而使用最低的HS数据会降低其性能。在RFT中，我们基于HE的训练方法的性能显着优于基线方法。在RL中，HS选择的成功轨迹使模型能够学习强大的推理模式，显着优于其他比较方法。我们的研究结果将HS确立为一种稳健的、免训练的指标，可以为在LLM中开发高级推理提供统一、有效且高效的方法。

[阅读原文](https://arxiv.org/abs/2605.22389)

---

## 16. 将思维链集成到生成式检索中：初步研究

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Wenhao Zhang, Ruihao Yu, Yi Bai, Zhumin Chen, Pengjie Ren

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ThinkGR, a unified framework integrating chain-of-thought into generative retrieval with a hybrid decoding strategy and retrieval-grounded RL, directly matching RL for LLMs and latent reasoning.

**摘要**: arXiv：2605.22358v1宣布类型：新摘要：虽然生成式检索（GR）在标准检索基准上表现出有竞争力的性能，但现有方法在没有中间考虑的情况下将查询直接映射到文档标识符（docid），从而限制了其对于需要多步推理的复杂查询的有效性。作为将思想链（CoT）集成到生成式检索中的初步研究，我们引入了ThinkGR，这是一个将CoT与docid生成交织在一起的统一框架，在单个生成过程中实现迭代思维和检索。为了弥合自由形式思想生成和结构化检索目标之间的差距，我们设计了（1）一种混合解码策略，在无约束思想生成和有约束的docid解码之间动态切换，以及（2）一种两阶段训练方法，首先通过监督微调对齐思想检索模式，然后通过基于检索的强化学习优化思想质量。四个多跳检索基准测试的实验表明，ThinkGR实现了最先进的性能，平均提高了+6.86%。我们的工作为增强具有显式审议能力的生成性检索开辟了新途径，对需要复杂推理的检索任务具有良好的影响。

[阅读原文](https://arxiv.org/abs/2605.22358)

---

## 17. 为什么语义熵失败：几何感知和校准政策优化的不确定性

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zheyuan Zhang, Kaiwen Shi, Han Bao, Zehong Wang, Tianyi Ma, Yanfang Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a principled framework (GCPO) for uncertainty-aware policy optimization in LLM post-training, addressing gradient variance and learning signal quality with geometry-aware and calibrated measures.

**摘要**: arXiv：2605.21801v1宣布类型：新摘要：后训练已成为改善大型语言模型中推理和对齐的核心，其中无批评模型可以从模型生成的输出中进行可扩展学习，但缺乏区分信息信号和有噪信号的原则机制。最近的方法利用响应级别测量作为不确定性信号来监管GRPO等基于群体的优化方法。然而，它们的经验成功仍然不稳定，并且不清楚它们如何影响优化动态。在本文中，据我们所知，我们提供了第一个原则性公式，该公式将不确定性信号解释为描述和调节梯度方差和学习信号质量的机制。基于经验和理论分析，我们确定了当前基于熵的估计量的两个关键差距：各向异性差距和校准差距。受此分析的启发，我们提出了几何感知的校准政策优化（GCPO），这是一个新颖的框架，将捕获语义不一致的几何感知措施与基于奖励的校准结合起来，以将不确定性与学习信号强度。多个基准测试的实验表明，我们的方法可以更忠实地跟踪梯度变异性，并持续提高训练后的性能。我们的结果强调了设计与优化动态一致的不确定性信号的重要性，为稳健的后训练提供了原则性的视角。

[阅读原文](https://arxiv.org/abs/2605.21801)

---

## 18. OSCToM：RL引导的高级心理理论对抗生成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sharmin Sultana Srishty, Kazi Mahathir Rahman, Malaika Parizat Sakkhi, Samia Shahid Prianna, Shaikhul Islam Sinat

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes OSCToM, an RL-guided adversarial data generation framework for high-order Theory of Mind reasoning in LLMs, directly matching the RL for LLMs criterion with a new reward-driven data synthesis loop.

**摘要**: arXiv：2605.20423v1宣布类型：新摘要：大型语言模型（LLM）在许多语言任务中表现良好，但它们的心理理论（ToM）推理在复杂的社会环境中仍然不平衡。现有的基准测试（包括ExploreToM）并不总是测试使这些设置变得困难的循环信念和信息不对称。本文提出了OSCToM（观察者自我冲突心理理论），这是一种在基于LLM的ToM任务中建模嵌套信念冲突的方法。关键的情况是观察者对另一个主体的看法与观察者自己的信仰状态相冲突。此类案例超出了简单的观点判断，需要循环、多层推理。OSCToM结合强化学习（RL）、一种扩展的特定领域语言和组合代理模型来生成管理者-自我冲突。在我们的实验中，OSCToM-8B在所测试的系统中给出了最好的总体结果。它改进了FANToM上报告的ExploreToM结果，并在Hi-ToM和BigToM上保持竞争力。在信息不对称的FANToM基准测试中，OSCToM的准确率达到76%，而ExploreToM的准确率为0.2%。数据合成过程的效率也提高了6倍，这表明有针对性的训练数据可以帮助较小的模型处理高级认知推理。项目代码可在https://github.com/sharminsrishty/osct上获得。

[阅读原文](https://arxiv.org/abs/2605.20423)

---

## 19. Memory-R2：长期记忆增强LLM代理的公平信用分配

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Sikuan Yan, Ahmed Bahloul, Ercong Nie, Susanna Schwarzmann, Riccardo Trivisonno, Volker Tresp, Yunpu Ma

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Memory-R2, a training framework with LoGo-GRPO for fair credit assignment in long-horizon memory-augmented LLM agents using RL.

**摘要**: arXiv：2605.21768v1宣布类型：新摘要：内存增强的LLM代理通过跨会话存储、更新和重用信息，实现超出有限上下文窗口的交互。然而，在多会话环境中通过强化学习训练此类代理具有挑战性，因为记忆会将代理过去的动作转变为其未来环境的一部分。一旦不同的推出写入、更新或删除不同的内存，它们就不再共享相同的中间内存状态，从而使得子公司级比较从根本上不公平。这违反了GRPO等群体相对方法背后的一个关键假设，即对展开进行比较，就好像它们是从相同的有效环境中抽样一样。因此，学徒级奖励为长期记忆操作提供了有噪音或有偏见的信用信号。为了应对这一挑战，我们引入了Memory-R2，这是一个针对长期内存增强LLM代理的训练框架。其核心算法Logo-GRPO结合了局部和全局组相关优化。全局目标保留了从长时间范围的强制性奖励中进行的端到端学习，而局部重滚则比较了来自同一中间记忆状态的不同记忆操作结果，从而产生了更公平的群体比较和对记忆构建的更精确监督。除了信用分配之外，Memory-R2还通过共享参数共同学习设计联合优化了内存形成和内存演化，其中事实提取器和内存管理器通过特定于角色的提示从同一LLM骨干中实例化。为了在长记忆范围内稳定多步RL，我们采用了渐进式课程，将训练范围从8次增加到16次再到32次。这些组件共同为长期多会话环境中的内存增强LLM代理提供了有效的训练范式。

[阅读原文](https://arxiv.org/abs/2605.21768)

---

## 20. Maestro：强化学习来规范分层模型技能集成

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jinyang Wu, Guocheng Zhai, Ruihan Jin, Yuhao Shen, Zhengxi Lu, Fan Zhang, Haoran Luo, Zheng Lian, Zhengqi Wen, Jianhua Tao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an RL-driven orchestration framework that dynamically composes ensembles of frozen expert models and skills, directly matching the RL for LLMs criterion with a new reward-driven training recipe.

**摘要**: arXiv：2605.22177v1宣布类型：新摘要：大型语言模型（LLM）和模块化技能的激增赋予自治代理越来越强大的能力。现有的框架通常依赖于单一的LLM和固定逻辑来与这些技能进行接口。这引发了一个关键的瓶颈：不同的LLM在不同领域提供了独特的优势，但当前的框架未能利用模型和技能的互补优势，从而限制了它们在下游任务中的表现。在本文中，我们介绍了Maestro（面向专家技能的强化编排的多模式代理），这是一个强化学习（RL）驱动的编排框架，它将异类多模式任务重新构建为分层模型技能注册表上的顺序决策过程。Maestro不是将所有知识整合到单个模型中，而是训练一种轻量级策略来动态地组成冻结专家模型和两层技能库的集合，在每一步决定是否调用外部专家、选择哪个模型-技能对以及何时终止。该政策通过基于结果的RL进行优化，不需要阶梯级监督。我们通过十个代表性的多模式基准来评估Maestro，这些基准涵盖数学推理、图表理解、高分辨率感知和特定领域分析。Maestro仅使用4 B编排器，平均准确率为70.1%，超过GPT-5（69.3%）和Gemini-2.5-Pro（68.7%）。至关重要的是，习得的协调政策无需再培训即可推广到看不见的模型和技能：用域外专家增强注册表，在四个具有挑战性的基准上平均得分为59.5%，优于所有闭源基线。Maestro进一步保持高计算效率和低延迟。源代码可访问https://github.com/jinyangwu/Maestro。

[阅读原文](https://arxiv.org/abs/2605.22177)

---

## 21. 根据能力定制教学：LLM推理的方向适应性自蒸馏

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Hongbin Zhang, Chaozheng Wang, Kehai Chen, Youcheng Pan, Yang Xiang, Jinpeng Wang, Min Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Direction-Adaptive Self-Distillation (DASD), a new RL/self-distillation method for LLM reasoning that adapts teacher supervision direction based on token entropy to preserve exploration.

**摘要**: arXiv：2605.22263v1宣布类型：新摘要：政策上的自我蒸馏（OPSD）是一种新兴的LLM培训后范式，其中模型充当自己的老师：以参考痕迹或提示等特权信息为条件，相同的政策为其自己的推出提供密集的代币级监督。然而，最近的研究表明，OPSD通过抑制预测不确定性来降低复杂推理，从而支持探索和假设修正。我们的代币级分析表明，这种失败是由于在具有不同不确定性水平的代币之间应用统一的教师监督方向造成的：在高信息量下，服从特权自学教师会抑制探索，而在低信息量下，偏离教师会降低步骤准确性。因此，我们提出了\textBF{Direction-Adaptive-Distillation}（\textBF{DASD}），它将特权自我蒸馏从统一的教师模仿重新构建为基于熵的定向监督：高熵令牌被从特权的教师推开以保留探索，而低熵令牌则被拉向教师以稳定步骤级执行。在六个数学推理基准中，DASD在强大的WLVR和自蒸馏基线上实现了最佳宏Avg@16。Pass@$k$、推理健康和概括分析表明，这些平均收益来自于在不牺牲步骤级执行的情况下保留探索。

[阅读原文](https://arxiv.org/abs/2605.22263)

---

## 22. 后培训是关于状态，而不是代币：SFT、RL和政策上蒸馏的状态分布视图

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dong Nie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a state-centric view of post-training (SFT, RL, distillation) showing that the state distribution on which supervision is applied is as important as the loss function, with controlled experiments on GSM8K.

**摘要**: arXiv：2605.22731v1宣布类型：新摘要：监督式微调（SFT）、强化学习（RL）和蒸馏等大型语言模型训练后方法通常通过其损失函数进行分析：最大似然性、策略梯度、前向KL、反向KL或相关目标级别变体。我们研究一个补充因素：实施监督的州分布。对于自回归政策来说，状态是提示加上生成的后缀。SFT在固定的数据集状态上训练，而RL和按策略蒸馏（OPD）在当前学习者诱导的状态上训练。我们将后训练形式化为状态分布塑造，并使用Qwen 3 -0. 6 B-Base基于GSM 8 K进行受控小规模研究，以TruthfulQA和MMLU作为保留评估。我们的结果显示了三种现象。首先，轻度SFT运行可以改善GSM 8 K，几乎不会忘记，而压力SFT运行会导致大量保留力损失。其次，尽管使用教师作为唯一的监督来源，但降级的SFT教师的OPD在GSM 8 K、TruthfulQA和MMLU上超过了该教师。第三，轻量级的按策略RL运行在保留保留性的同时改进了GSM 8 K。这些结果支持以状态为中心的训练后观点：训练状态的来源和地点可能与监督信号的形式一样重要。

[阅读原文](https://arxiv.org/abs/2605.22731)

---

## 23. 用于闭环优化、仿真和建模规划的工具增强代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Liyuan Deng, Shujian Deng, Yongkang Chen, Yongkang Dai, Zhihang Zhong, Linyang Li, Xiao Sun, Yilei Shi, Huaxi Huang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a tool-augmented RL framework (COSMO-Agent) that teaches LLMs to perform closed-loop CAD-CAE optimization via a multi-constraint reward, directly matching RL for LLMs and self-improving agents.

**摘要**: arXiv：2605.20190v1宣布类型：新摘要：迭代工业设计-模拟优化受到CAD-CAE语义差距的限制：将模拟反馈转化为多样化、耦合约束下的有效几何编辑。为了填补这一空白，我们提出了COSMO-Agent（闭环优化、模拟和建模验证），这是一种工具增强的强化学习（RL）框架，可以教LLM完成闭环CAD-CAE流程。具体来说，我们将CAD生成、CAE求解、结果解析和几何修改作为交互式RL环境，其中LLM学习协调外部工具并修改参数化几何，直到满足约束。为了使这种学习稳定且具有工业可用性，我们设计了一个多约束奖励，共同鼓励可行性、工具链稳健性和结构化输出有效性。此外，我们还提供一个与行业一致的数据集，涵盖25个组件类别，并具有可执行的CAD-CAE任务，以支持现实的培训和评估。实验表明，COSMO-Agent训练极大地改善了小型开源LLM的约束驱动设计，在可行性、效率和稳定性方面超过了大型开源和强大的闭源模型。

[阅读原文](https://arxiv.org/abs/2605.20190)

---

## 24. 自我进化主体的潜在记忆动态混合

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dianzhi Yu, Vireo Zhang, Hongru Wang, Yanyu Chen, Minda Hu, Wanghan Xu, Siki Chen, Philip Torr, Zhenfei Yin, Irwin King

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes MoLEM, a dynamic mixture-of-experts latent memory framework for self-evolving agents that avoids catastrophic forgetting by freezing the base model and internalizing knowledge into additional modules.

**摘要**: arXiv：2605.21951v1宣布类型：新摘要：实现智能主体的自我进化需要在不断变化的任务序列中不断积累新知识，同时不忘记之前获得的能力。现有的方法要么通过更新模型参数来内化知识，这会导致灾难性遗忘，要么依赖外部记忆，这无法真正增强模型的内在能力。我们提出了MoLEM，这是一种基于动态专家混合（MoE）的生成性潜在记忆混合框架。我们将多位专家视为生成记忆的独立载体。路由器通过关键字查询匹配来选择专家并对其进行加权，并将聚合的潜在记忆注入到推理过程中。推理的基本模型仍然完全冻结，所有经验知识都内化到附加模块中，避免灾难性的遗忘。对于持续学习，每个训练阶段都与轻量级自动编码器配对，该编码器在推理时选择适当的路由组，而与任何阶段匹配的输入则退回到预训练的模型。实验在跨越数学、科学和代码领域的连续学习序列上训练框架。培训后，我们在相应的测试集上评估框架，以衡量持续适应阶段的任务学习和能力保留。在完整的连续学习序列之后，我们的方法将平均准确性比Vanilla预训练基线提高了10.40%，而在不同的训练顺序中，没有一种竞争方法始终超过该基线。

[阅读原文](https://arxiv.org/abs/2605.21951)

---

## 25. 强化思维图：LLC驱动的自适应预算

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Manuel Noah Riesen, Peter Alfred von Niederh\"ausern

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel RL-driven adaptive prompting method (RGoT) that uses reinforcement learning to dynamically generate graph-of-thought structures, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2605.22195v1宣布类型：新摘要：思想图（GoT）是大型语言模型（LLM）的最新提示范式的一般形式，已被证明对于复杂的问题解决很有用。通过执行操作图，LLM的思想被结构化为任意图，形成实际的思想图。最初，操作图是手动定义的，这需要深入了解要解决的问题的解决方案。这样的静态操作图是僵化的，因此缺乏适应性。我们提出了强化思维图（RGoT），这是GoT提示范式的一种自动化方法，利用强化学习（RL）从人类定义的集合中自适应地生成操作图。结果表明，在一定的约束下，可以以自动化的方式根据任务的复杂性自适应地构建操作图。

[阅读原文](https://arxiv.org/abs/2605.22195)

---

## 26. SegCompass：探索与稀疏自动编码器的可解释对齐以增强推理分割

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Zhenyu Lu, Liupeng Li, Jinpeng Wang, Haoqian Kang, Yan Feng, Ke Chen, Yaowei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SegCompass, which uses a Sparse Autoencoder for interpretable alignment and integrates RL for reasoning path optimization, directly matching RL for LLMs and latent reasoning criteria.

**摘要**: arXiv：2605.22658v1宣布类型：新摘要：虽然大型语言模型提供了强大的合成推理，但现有的推理分段管道无法将这种推理与视觉感知透明地连接起来。当前的方法，例如潜在查询对齐，是端到端但不透明的“黑匣子”。相反，文本本地化读出仅仅是可读的，而不是真正可解释的，通常作为一个不受约束的事后步骤。为了弥合这一可解释性差距，我们提出了SegCompass，这是一个端到端的模型，它利用稀疏自动编码器（SAE）来构建一个明确的，可解释的和可区分的对齐路径。给定一个图像指令对，SegCompass首先生成一个思想链（CoT）跟踪。我们的方法的核心是一个SAE，它将CoT和视觉标记映射到一个共享的高维稀疏概念空间中。查询码本从该空间中选择突出的概念，然后通过槽映射器将其空间接地到指导最终掩模解码器的多槽热图中。整个模型是联合训练的，将推理路径的强化学习与标准分段监督统一起来。这个SAS驱动的界面提供了一个“白盒”连接，它比潜在查询更可追踪，并且比文本读出更一致。对五个具有挑战性的基准进行的广泛实验表明，SegCompass符合或超越了最先进的性能。至关重要的是，我们的视觉和定量分析表明，所学到的稀疏概念的质量与最终面罩准确性之间存在很强的相关性，证实SegCompass通过其增强且可检查的对齐方式实现了卓越的结果。代码可在https://github.com/ZhenyuLU-Heliodore/SegCompass上获取。

[阅读原文](https://arxiv.org/abs/2605.22658)

---

## 27. 策略一致性训练以最小的能力退化提高LLM安全性

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Andy Han, Kristina Fujimoto, Avidan Shah, Kiet Nguyen, Kai Xu, Chen Yueh-Han, Ilia Sucholutsky, Rico Angell

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes On-Policy Consistency Training (OPCT), a new RL-like alignment method that improves LLM safety via on-policy supervision, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2605.21834v1宣布类型：新摘要：一致的模型可能会在多种方面表现不当：它们通常阿谀奉承、成为越狱的受害者，或者未能包含适当的安全警告。一致性训练是一种有前途的新对齐范式，可以通过使用对比输入对将不变量训练到模型中来减轻此类失败。现有的一致性训练过程离线生成一次监督信号，并使用监督式微调（SFT）来更新模型。不幸的是，产生的模型往往只记住训练分布的表面形式，因此概括性较差并在能力上倒退。我们引入了政策一致性训练（OPCT），这是一种新的一致性训练方法，其中目标是根据模型自己对提示的响应来计算的，并以相应的对比提示为条件进行自我监督。我们从三个安全轴上评估OPCT：谄媚、越狱和安全意识。在三个型号系列中，OPCT在所有安全要求方面都优于SFT。与基线相比，它几乎使奉承率减半（8.1%对15.4%，而SFT为11.2%）。在一个适应性的每目标攻击者，OPCT持有越狱防御成功率接近99%的越狱行为，而SFT平均达到87%。在安全意识方面，OPCT在三个模型中的两个模型中优于SFT，并且在另一个模型中与SFT相匹配。OPCT还在很大程度上避免了SFT引起的能力退化，例如MAT-500下降28个百分点。我们的结果表明，一致性训练最好作为OPCT而不是SFT实施，特别是当需要超出训练分布的推广时。

[阅读原文](https://arxiv.org/abs/2605.21834)

---

## 28. 消除瓶颈：通过近边界信号的随机恢复稳定WLVR

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shuo Yang, Jinda Lu, Chiyu Ma, Kexin Huang, Haoming Meng, Qihui Zhang, Yuyang Liu, Bolin Ding, Guoyin Wang, Li Yuan, Jingren Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a clipping bottleneck in RLVR and proposes a simple stochastic rescue method to stabilize training and improve convergence.

**摘要**: arXiv：2605.22703v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）已成为扩展LLM推理的核心范式，但其优化经常受到训练不稳定性和次优收敛的影响。通过对基于剪切的GRPO式目标的系统剖析，我们将硬剪切引起的刚性剪切决策确定为所研究的WLVR设置中的一个关键实际瓶颈。具体来说，我们的分析表明，信息信号可能位于刚好超过限幅阈值的近边界区域，因此被标准硬限幅规则丢弃。值得注意的是，一旦精确识别出这个瓶颈，即使边界上的简单随机扰动也可以恢复有意义的性能收益。在这一发现的基础上，我们提出了近边界随机救援（NSO），这是一种最小的即插即用修改，可以随机保留这些稍微越界的令牌以恢复丢失的信号。虽然通过随机抽样的NSO可以被解释为在预期中引发隐性梯度衰减，但我们的消融表明，其随机的、边界局部救援机制始终比确定性梯度衰减更有效。作为一种即插即用解决方案，经过7 B至30 B型号尺寸以及密集型和MoE架构的广泛实验验证，NSO作为一种即插即用解决方案，大大提高了训练稳定性，并在DAPO和GSPO等强大基线上提供一致的收益。

[阅读原文](https://arxiv.org/abs/2605.22703)

---

## 29. 两个总比一个好：无崩溃的多奖励RIIF培训框架

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Shourov Joarder, Diganta Sikdar, Ahsan Habib Akash, Binod Bhattarai, Prashnna Gyawali

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a multi-reward RLIF framework with KL-Cov regularization to prevent collapse in unsupervised RL for LLM reasoning.

**摘要**: arXiv：2605.22620v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）大大提高了LLM的推理能力，但通常依赖于人类注释或金标准解决方案的外部监督。来自内部反馈的强化学习（RIIF）最近成为一种可扩展的无监督替代方案，使用从模型本身提取的信号。然而，现有的RIIF方法通常依赖于单一的内部奖励，这可能会导致奖励黑客攻击、熵崩溃和推理结构退化。我们提出了一个多奖励RIIF框架，将训练信号分解为两个补充的部分：基于集群投票的答案级奖励和基于代币自我确定性的完成级奖励。为了稳健地组合这些信号，我们应用基于GDPO的正规化来减少奖励规模失衡。我们进一步引入了KL-Cov正规化，其目标是导致不成比例的熵减少、保留探索并防止后期崩溃的低熵令牌分布。在数学推理和代码生成基准测试中，我们的方法比之前的无监督RL方法提高了稳定性和鲁棒性，同时实现了接近监督WLVR方法的性能。这些结果表明，补充的内部奖励与有针对性的正规化相结合，可以支持稳定的长期推理，而无需依赖外部地面真相监督。代码很快就会发布。

[阅读原文](https://arxiv.org/abs/2605.22620)

---

## 30. 推理增强推荐的强化偏好优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jingtong Gao, Zeyu Song, Chi Lu, Xiaopeng Li, Derong Xu, Maolin Wang, Peng Jiang, Kun Gai, Qingpeng Cai, Xiangyu Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a reinforced preference optimization framework (RPORec) that uses RL with verifiable rewards from a recommendation head to fine-tune LLM reasoning for recommendations, directly matching RL for LLMs.

**摘要**: arXiv：2605.21967v1宣布类型：新摘要：推荐系统对于跨数字平台交付个性化内容至关重要，大型语言模型（LLM）的最新进展提供了新的机会，可以通过更丰富的世界知识和显式推理能力来增强推荐系统。在推理知识的帮助下，推荐可以更好地推断用户的潜在意图，适应不断变化的偏好，并利用语义关系来提高准确性和可解释性。然而，由于集成过程中的结构性破坏以及将自由形式生成转化为准确的项目预测的困难，现有的基于推理的推荐方法往往无法使LLM的推理过程与特定推荐目标完全一致。在本文中，我们介绍了RPORec，这是一个加强的偏好优化框架，它将LLM主干的推理能力与专用推荐头（Rechead）统一起来，以实现精确的项目检索。RPORec包括两个阶段：（1）推理增强推荐建模，其中生成高质量的思想链（CoT）推理并将其用作辅助知识来指导Rechead学习特定于描述的表示;和（2）高级推理细化和对齐，其中训练的Rechead产生可验证的奖励，以通过强化学习微调LLM主干，提高推理质量、结构一致性，和任务相关性。对公共基准测试和大规模在线部署的广泛实验表明，RPORec始终优于最先进的基于LLM的推荐方法，证明了推理增强推荐建模在现实世界系统中的有效性。

[阅读原文](https://arxiv.org/abs/2605.21967)

---

## 31. LANG：具有比例自适应提示指导的多语言推理强化学习

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Yuchun Fan, Bei Li, Peiguang Li, Yilin Wang, Yongyu Mu, Jian Yang, Xin Chen, Rongxiang Weng, Jingang Wang, Xunliang Cai, Jingbo Zhu, Tong Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes LANG, a novel RL framework with language-adaptive hint guidance and progressive decay to improve multilingual reasoning without language drift.

**摘要**: arXiv：2605.22567v1宣布类型：新摘要：事实证明，强化学习对于增强大型语言模型（LLM）中的多步推理是有效的，但其好处尚未完全转化为多语言上下文。现有的方法难以应对一个基本的权衡：优先考虑输入语言一致性会严重阻碍推理质量，而优先考虑推理往往会导致语言意外地偏向英语。我们通过LANG来解决这一挑战，LANG是一个新颖的框架，利用语言条件提示来指导非英语推理任务的探索。我们的方法结合了两个关键机制来防止对这些暗示的依赖：逐步撤回支架的渐进衰退时间表，以及根据特定语言困难定制学习视野的语言适应性切换。具有挑战性的多语言数学基准的经验结果表明，LANG在不损害语言一致性的情况下大幅提高了推理性能。此外，我们表明我们的框架超越了数学，促进了模型层之间更一致的语言一致性

[阅读原文](https://arxiv.org/abs/2605.22567)

---

## 32. 通过可验证的预测动作进行推理：金融LLM的一致性基础RL

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jialin Chen, Aosong Feng, Harshit Verma, Siyi Gu, Haiwen Wang, Ali Maatouk, Yixuan He, Yifeng Gao, Leandros Tassiulas, Rex Ying

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes StockR1, a financial LLM optimized via RL with a verifiable forecast action and consistency-grounded rewards, directly matching RL for LLMs criteria.

**摘要**: arXiv：2605.21975v1宣布类型：新摘要：金融市场的特点是极端非平稳性、低信噪比以及对新闻、公司基本面和宏观经济信号等外部信息的强烈依赖性。然而，现有的方法要么将时间序列抽象为文本，要么将预测与基于语言的推理脱钩，导致定性推理和定量结果之间根本不匹配。为了解决这个问题，我们引入了StockR 1，这是一种时间序列增强型LLM，通过可验证的预测动作将股票预测和财务推理统一起来。基于工具调用设计，该模型首先发出预测动作，这是对其定性市场前景的结构化和可解释的表示。然后，它调用以该动作为条件的时间序列解码器来生成分布未来轨迹，从而实现更明智的问题回答和财务推理。我们通过强化学习优化整个管道，其中奖励共同反映答案有效性、预测准确性以及生成的动作与观察到的时间序列动态之间的一致性。此外，奖励由样本级不确定性标量重新加权，鼓励模型适应市场动态中的不同不确定性。我们评估StockR1的财务问题回答和股票预测超过一个大规模的10年的基准。我们的方法始终优于时间序列基线和通用LLM，将推理准确率提高了17.7%（4B）和25.9%（8B）。这些发现表明，构建预测行动在语言推理和时间预测之间建立了强大的协同作用，使LLM能够通过可验证，可解释和数字接地的决策进行推理。

[阅读原文](https://arxiv.org/abs/2605.21975)

---

## 33. 通过一致性培训减少政治操纵

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Long Phan, Devin Kim, Alexander Pan, Alice Blair, Adam Khoja, Dan Hendrycks

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Political Consistency Training (PCT), a novel RL training method with new reward designs (sentiment and helpfulness consistency) to reduce political bias in LLMs, directly matching the RL for LLMs criterion.

**摘要**: arXiv：2605.22771v1宣布类型：新摘要：大型语言模型（LLM）在各种敏感背景下表现出系统性的政治偏见。我们发现LLM处理来自对立政治双方的对应话题是不对称的。我们将这种现象称为隐蔽的政治偏见，并确定了其运作的7类技术。我们提出了两个隐性偏见的指标：情感一致性衡量成对政治提示中的修辞和框架的对称性;乐于助人的一致性衡量对称的深度和参与度。为了减少这两种类型的隐性偏见，我们引入了政治一致性培训（PCT），这是一种具有两种互补范式的RL培训方法：情感一致性培训和乐于助人一致性培训。我们表明，《条约》保留了总体的帮助性，大大减少了隐蔽的政治偏见，并推广到既定的基准。我们在https://political-manipulation.ai上发布我们的工作

[阅读原文](https://arxiv.org/abs/2605.22771)

---

## 34. ACC：为长上下文训练编写代理轨迹

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Qisheng Su, Zhen Fang, Shiting Huang, Yu Zeng, Yiming Zhao, Kou Shi, Ziao Zhang, Lin Chen, Zehui Chen, Lijun Wu, Feng Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Agent Context Compilation (ACC), a method that converts agent trajectories into long-context QA pairs for training, enabling self-improvement from interaction traces and directly addressing long-context reasoning.

**摘要**: arXiv：2605.21850v1宣布类型：新摘要：代理的最近发展重新引发了对LLM长上下文推理能力的需求。然而，培训LLM以获得这种能力需要昂贵的长文档策展或启发式上下文合成。我们观察到，代理在解决问题、调用工具和在多个回合中接收环境观察时会产生巨大的轨迹。因此，回答原始问题所需的证据分散在这些转折中，需要整合遥远的背景片段。然而，标准代理SFT掩盖了工具响应，仅训练回合级工具选择，从而造成了这些分散的信号未被使用的监管盲点。我们提出了代理上下文编译（ACC），它将来自搜索、软件工程和数据库查询代理的轨迹转换为长上下文QA对，将原始问题与跨多个回合收集的工具响应和环境观察相结合，训练模型在不使用工具的情况下直接回答。这使得问题和证据之间的依赖关系变得明确，从而能够直接监督对遥远片段的长上下文推理，而无需额外注释。ACC是一种简单但有效的方法，可以与任何现有的长上下文扩展或训练方法相结合，提供可扩展的监督微调数据。我们通过MRCR和GraphWalks验证ACC的长期依赖性建模任务，这是挑战需要交叉转弯共指解析和扩展上下文上的图形穿越的基准。使用ACC训练Qwen 3 - 30 B-A3 B在MRCR上达到68.3（+18.1），在GraphWalks上达到77.5（+7.6），结果与Qwen 3 - 235 B-A22 B相当，同时保留了GPQA、MMLU-Pro、AIME和IFEval的一般功能。进一步的机制分析表明，ACC训练的模型表现出任务适应性注意力重组和专家专业化。

[阅读原文](https://arxiv.org/abs/2605.21850)

---

## 35. 视觉语言模型的视觉优势政策提炼

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Ruiqi Liu, Xiaolei Lv, Gengsheng Li, Ximo Zhu, Zhiheng Wang, Zhengbo Zhang, Junkai Chen, Zhiheng Li, Bo Li, Jun Gao, Shu Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Visual-Advantage On-Policy Distillation (VA-OPD), a novel distillation method for VLMs that uses token-level visual advantage to improve reliance on visual input, directly relevant to RL/alignment via reward design.

**摘要**: arXiv：2605.21924v1宣布类型：新摘要：事实证明，政策上的知识提炼对语言模型有效，但其在视觉语言模型（VLM）中的应用仍然没有得到充分的探索。我们观察到，标准的政策提炼可以提高学生的输出质量，但无法加强其对视觉输入的依赖：在视觉关键标志上，无论是否存在细粒度的视觉细节，学生的预测在很大程度上保持不变，尽管老师的预测在很大程度上依赖于细粒度的视觉细节。为了使这种差异可观察，我们引入了视觉优势（VA），当教师在不访问细粒度视觉细节的情况下对学生生成的展示进行评分时，标记级的日志概率差异。VA集中在少数代币中，而这些高VA代币是真正携带视觉监督信号的代币。这激发了一个蒸馏目标，将它们与语言支架区别对待，这样它们的贡献就不会被周围丰富的语言符号所稀释。我们提出了视觉优势政策蒸馏（VA-OPD），它以两种粒度使用VA：通过子公司平均VA进行推出级别重新加权，以及分别在高VA和低VA组中平均的标记级别KL。我们在两个数学数据集（Geometry 3 K和ViRL 39 K）上进行训练，并在Qwen 3-BL系列的三种教师规模（4 B、8B和32 B）中对涵盖数学推理和视觉理解的八个基准进行评估。Va-OPD在每个基准上都比标准的政策蒸馏有所改善，收益沿着教师规模和数据规模轴单调增长，这表明这些因素持续复合。

[阅读原文](https://arxiv.org/abs/2605.21924)

---

## 36. 通过比较理念评估预测研究成功的语言教学模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Srujan P Mule, Aniketh Garikaparthi, Manasi Patwardhan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes RL with verifiable rewards (RLVR) to train LLMs for comparative idea evaluation, directly matching RL for LLMs via verifier-driven optimization.

**摘要**: arXiv：2605.21491v1宣布类型：新摘要：随着语言模型通过自动化假设生成和实现来加速科学研究，一个新的瓶颈出现了：在没有详尽实验的情况下评估和过滤数百个人工智能生成的想法。我们询问LM是否可以学会在进行任何实验之前预测研究想法的经验成功。我们研究比较经验预测：给定特定基准的研究目标和两个候选想法，预测哪一个将实现更好的基准性能。我们基于PapersWithCode的客观结果构建了一个包含11，488个想法对的数据集。虽然现成的8B参数模型表现不佳（30%），SFT将业绩大幅提升至77.1%，优于GPT-5（61.1%）。通过通过具有可验证奖励的强化学习（WLVR）将评估框架为一项推理任务，我们训练模型以发现潜在推理路径，在可解释的理由下实现了71.35%的正确率。通过额外的烧蚀和分布外测试，我们展示了对表面层启发式的鲁棒性，并转移到跨域时分测试集和独立构建的测试集。我们的结果表明，计算效率高的小语言模型可以充当有效、客观的验证器，为自主科学发现提供可扩展的路径。

[阅读原文](https://arxiv.org/abs/2605.21491)

---

## 37. HealthCraft：急诊医学的强化学习安全环境

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Brandon Dent

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a new RL environment for emergency medicine with trajectory-level safety rewards, directly matching RL for LLMs via verifiable reward design and RL pipeline scaffolding.

**摘要**: arXiv：2605.21496v1宣布类型：新摘要：前沿语言模型部署到临床工作流程中的速度比安全评估它们的基础设施更快。静态医疗质量保证基准错过了急诊医疗中重要的失败模式：车间级安全崩溃、工具滥用和持续临床压力下的投降。我们介绍了HealthCraft，这是第一个公共职业学习环境，在现实的紧急医疗条件下奖励教师级安全，改编自Corecraft。它建立在具有14种实体类型和3，987个种子实体的FHIR R4世界状态之上，公开了24个LCP工具，并定义了一个双层规则，每当违反任何安全关键标准时，奖励就会归零。我们发布了六个类别的195项任务，根据2，255个二进制标准（515个安全关键标准）进行评级;事后10项任务负级名单将其扩展到205项任务和2，337项标准。两个前沿模型的V8结果显示Claude Opus 4.6为Pass@1 24.8% [21.5-28.4]，GPT-5.4为12.6% [10.2-15.6]，安全故障率为27.5%和34.0%。在多步骤工作流程（最接近真正紧急护理的代表）上，尽管在各个步骤上有部分能力，但性能仍降至接近零（Claude 1.0%，GPT-5.4 0.0%）。试点v2和v8之间修复的六个基础设施错误重新排序了哪个模型“看起来更强大”，这证明基础设施保真度是衡量的一部分。确定性的LLM裁判覆盖限制了评估者的噪音，60次负级烟雾飞行员表明奖励信号不是临时训练安全的：约束标准在0.929流行率时通过，评估背带可以容忍这种可玩性，但训练奖励不能。我们根据Corecraft第5.2节的规定，将耦合到Megatron+SGLang+GRPO循环，并将培训奖励消融作为未来的工作。环境、任务、标题和工具在Apache 2.0下发布。

[阅读原文](https://arxiv.org/abs/2605.21496)

---

## 38. 忠实-MR 1：通过监视和加强视觉注意力进行忠实多模式推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Changyuan Tian, Zhicong Lu, Huaxing Liu, Xiang Wang, Shuai Li, Yu Chen, Wenqian Lv, Zichuan Lin, Juncheng Diao, Deheng Ye

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a training framework with RLVR that anchors visual attention and reinforces faithful use of evidence for multimodal reasoning, directly addressing RL for LLMs and latent reasoning.

**摘要**: arXiv：2605.22072v1宣布类型：新摘要：具有可验证奖励的强化学习（WLVR）已成为推进大型语言模型中复杂推理的一种有前途的范式，最近的工作将WLVR扩展到了多模式大型语言模型（MLLM）。然而，这种转移暴露了忠诚度的挑战：忠实地感知与任务相关的视觉证据，并在推理过程中忠实地使用该证据，导致多模式基准的收益不令人满意。具体来说，现有的感知监督通常对文本描述进行操作，而不是天生对图像区域进行操作，并且忠实的使用在很大程度上被忽视，从而暴露了感知与推理的脱节，即正确感知的证据在推理过程中被丢弃或矛盾。为了缩小这些差距，我们提出了Faithful-MR 1，这是一个训练框架，可以锚定和加强视觉注意力，以解决忠实多模式推理的两个方面。锚定阶段将感知转变为一个显式的预推理子任务，直接针对图像区域而不是通过文本描述来监督专用代币的注意力。强化阶段通过反事实图像干预来暴露忠实的使用，奖励答案正确的轨迹，将视觉注意力集中在视觉有因果关系的地方。大量实验表明，Faithful-MR 1在Qwen 2.5-VL-Direct 3B和7 B主干上的表现优于最近的多模式推理基线，同时使用的训练数据要少得多。

[阅读原文](https://arxiv.org/abs/2605.22072)

---

## 39. EvoIR-Agent：通过经验驱动学习的自进化图像恢复统计系统

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Kailin Zhuang, Jiawei Wu, Zhi Jin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-evolving image restoration agent with a hierarchical experience pool and a self-evolving mechanism for closed-loop improvement from accumulated records, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2605.22208v1宣布类型：新摘要：多模式大型语言模型（MLLM）驱动的图像恢复代理通过灵活选择工具和确定删除顺序，展示了在降级耦合场景中的有效性。然而，他们的零射击计划在没有经验的情况下经常失败，需要进行严格的试错费用才能实现令人满意的结果。目前，人们采用了两种范式来解决这个问题，但困境仍然存在：基于训练的方法将内在经验嵌入参数中，实现了高推理效率，但缺乏与新工具的兼容性或退化。相比之下，免训练方法利用显式的经验存储来实现兼容性，但由于天真的经验，仍然会产生试错费用。为了解决这个困境，我们提出了EvoIR-Agent，它首先系统地制定了免训练图像恢复代理的体验组件。随后，构建了分层的经验池，可以为不同的工具和移除订单提供从粗到细的指导。此外，还引入了自进化机制，使用积累的记录从头开始更新池，从而大大提高了性能和效率。大量实验表明，与最先进的方法相比，EvoIR-Agent在完整参考指标方面取得了显着领先，并在性能和效率之间实现了显着的帕累托最优平衡。

[阅读原文](https://arxiv.org/abs/2605.22208)

---

## 40. SOlar：一个用于终身学习和持续适应的自我优化开放式自治代理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Nitin Vetcha, Dianbo Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-optimizing autonomous agent that uses meta-learning and multi-level RL for lifelong adaptation, directly matching the self-evolving agent criterion.

**摘要**: arXiv：2605.20189v1宣布类型：新摘要：尽管大型语言模型（LLM）取得了显着的成功，但它们在动态的现实世界环境中部署时仍然面临瓶颈，主要挑战是概念漂移和基于梯度的适应的高成本。传统的微调（FT）很难适应非平稳数据流，而不会给获取或需要大量手动数据管理带来灾难性的后果。为了解决流媒体和持续学习范式中的这些限制，我们提出了自优化终身自主推理器（SORAL），这是一种开放式自主代理，利用参数级元学习来自我改进，将模型权重视为探索的环境。它通过巩固对常识知识的强大先验来启动这一过程，使其有效地进行迁移学习。通过利用多层强化学习方法，SOlar自主发现适应策略，从而实现对未见域的高效测试时适应。至关重要的是，SORAL维护了有效修改策略的不断发展的知识库，隐含地充当情景记忆缓冲区，以平衡可塑性（适应新任务）和稳定性（元知识的保留）。实验表明，SORAL在常识、数学、医学、编码、社会和逻辑推理任务方面的表现优于强大的基线，标志着向能够在不断变化的环境中终身适应的自主代理迈出了重要一步。

[阅读原文](https://arxiv.org/abs/2605.20189)

---

## 41. F-TIS：在协作GRPO中利用多样化模型

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Nikolay Blagoev, O\u{g}uzhan Ersoy, Wendelin Boehmer, Lydia Yiyu Chen

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes F-TIS, a novel GRPO-style RL training paradigm that enables heterogeneous models to collaborate via filtered truncated importance sampling, directly addressing a key limitation in RL for LLMs.

**摘要**: arXiv：2605.22537v1宣布类型：新摘要：GRPO等强化学习方法在LLM后培训中非常受欢迎。在GRPO中，模型生成对一组提示的完成，这些提示将受到奖励，并将策略更新为相对高的奖励完成。由于模型的自回归性质，这种训练风格的生成阶段可能非常耗时。作为一种解决方案，之前的工作试图将推理步骤分布在许多节点上，并行工作。这些工作在训练中假设主要是同质模型，以使样本尽可能接近政策。这种假设在去中心化系统中可能不切实际，其中具有不同计算和偏好的各方可能希望合作完成相同的任务。因此，去中心化培训需要一种能够处理异类模型的方法--不同的模型在相同的任务上协作。然而，这会导致训练期间呈现高度偏离策略的样本，之前的工作已经发现，偏离策略的样本可能会损害GRPO的收敛。为了实现多样性，我们提出了过滤截断重要性抽样（F-TIS）--一种GRPO风格的训练范式，可以使用非策略样本来改善本地模型的学习。我们的框架允许各种模型在同一个RL训练运行中协作，同时保持高效的通信。我们在各种异类设置中广泛评估了F-TIS，并表明它表现出与纯样本训练相同的最终模型收敛性。此外，我们观察到在某些设置中，对非分布任务的概括性比政策上的训练更好，将模型的性能提高了12%。

[阅读原文](https://arxiv.org/abs/2605.22537)

---

## 42. 通过反事实强化学习学习视频LLM中的时空敏感性

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Dazhao Du, Jian Liu, Jialong Qin, Tao Han, Bohai Gu, Fangqi Zhu, Yujia Zhang, Eric Liu, Xi Chen, Song Guo

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CRPO, a dual-branch RL framework with a counterfactual relation reward to improve spatiotemporal sensitivity in Video LLMs, directly matching RL for LLMs via novel reward design.

**摘要**: arXiv：2605.21988v1宣布类型：新摘要：视频大型语言模型（视频LLM）实现了很强的基准准确性，但通常通过单帧线索和语言先验等快捷方式而不是通过跟踪时空动态来回答视频问题。这个问题在RL后训练中变得更加严重，其中仅正确性奖励可以进一步强化无需跟踪视频动态即可获得高奖励的捷径策略。我们通过提出一个受控的反事实问题来解决这个问题：如果视觉世界发生了变化，而问题保持不变，那么答案应该改变还是保持不变？基于这一观点，我们提出了\textBF{反事实关系政策优化（CRPO）}，这是一个用于改善\ð {时空敏感性}的双分支RL框架。CRPO通过水平翻转和时间翻转构建反事实视频，训练原始和反事实分支，并在其答案之间引入\textBF{反事实关系奖励（SVR）}。MCR鼓励更改动态问题的答案，静态问题的答案保持不变。这种跨分支机构的限制使得捷径政策很难在两个分支机构之间获得一致的奖励。为了评估这一属性，我们引入了\textBF{DyBench}，这是一个配对反事实视频基准，包含3，014个视频，涵盖可逆动态、移动方向和事件序列，以及严格的配对准确性指标，可以防止固定答案快捷方式夸大分数。实验表明，CRPO在时空敏感评估方面优于先前的RL方法，同时保持有竞争力的一般视频性能。在Qwen 3-BL-8B上，CRPO将DyBench P-Acc提高了+7.7，TimeBlind I-Acc提高了+8.2，这表明时空敏感性得到了改善，而不是更强地依赖静态快捷方式。该项目的网址是https://ddz16.github.io/crpo.github.io/。

[阅读原文](https://arxiv.org/abs/2605.21988)

---

## 43. 教师代币什么时候可靠？位置加权按策略自蒸馏推理

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Xiaogeng Liu, Xinyan Wang, Yingzi Ma, Yechao Zhang, Chaowei Xiao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Position-Weighted On-Policy Self-Distillation (PW-OPSD) for reasoning, a new RL-like training recipe that uses trajectory-level position weights to improve teacher-token reliability in self-distillation.

**摘要**: arXiv：2605.21606v1宣布类型：新摘要：政策上的自我蒸馏（OPSD）使用特权教师对学生进行自己的部署，但其标准目标对所有生成的代币进行同等加权，隐含地将特权教师目标视为对每个学生访问的前置都同等可靠。现有的基于信息量的OPD方法通过用教师信息量调节代币级监督来放松这种一致性，但推理中的高教师信息量具有模糊的可靠性含义：它可以反映不可行的不确定性或良性解决方案的多样性。为了识别这种现象，我们引入了分支生存能力诊断。具体来说，我们记录来自默认答案老师提示的下一个令牌替代方案，在学生提示加上其政策主干前置之后强制每个替代方案，并测试生成的学生模板延续是否恢复正确答案。在Qwen 3 - 4 B上，我们发现定向序列内位置得分是教师令牌可靠性的最强测试预测因子，达到0.83的ROC曲线下面积（AUROC）;局部不确定性得分最多为0.57。受这种个体级结构的激励，我们提出了职位加权按政策自蒸馏（PW-OPSD），它应用不断增加的职位权重，同时保持与OPSD相同的学生推出、特权教师通行证和削减向前KL目标。在我们使用不同随机种子的综合评估中，诊断衍生的PW-OPSD将AIME 2024和AIME 2025 Avg@12提高了+1.0和+1.1个百分点，并且对来自不同家族的两个更大规模模型DeepSeek-R1-Distill-Lama-8B和Olmo-3- 7 B-Think的概括评估也表明了一致的总体Avg@12改进。这些结果表明，推理提炼中的教师标记可靠性是先验结构的，无需额外的教师计算即可使用。

[阅读原文](https://arxiv.org/abs/2605.21606)

---

## 44. DeferMem：通过强化学习进行长期记忆QA的查询时证据提取

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Jianing Yin, Tan Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DeferMem, a long-term memory QA framework with a reinforcement learning algorithm (DistillPO) for query-conditioned evidence distillation, directly matching RL for LLMs.

**摘要**: arXiv：2605.22411v1宣布类型：新摘要：大型语言模型（LLM）代理人仍然难以回答长期记忆问题，其中支持答案的证据通常散布在漫长的对话历史中，并隐藏在大量不相关的内容中。现有的存储器系统通常在未来的查询已知之前处理存储器，然后根据相似性而不是它们用于回答查询的实用性来检索结果单元。该工作流程让下游回答者对检索到的候选项进行降噪并重建特定于查询的证据。我们提出了DeferMem，这是一个长期记忆框架，它将这个问题分解为高召回率候选检索和查询条件证据提炼。DeferMem使用轻量级的段链接结构来组织原始历史并在查询时检索广泛的候选项。然后，它应用经过DistillPO训练的记忆蒸馏器，DistillPO是我们的强化学习算法，用于将高召回率但高噪音的候选者提炼成一组忠实、独立且受查询条件的证据。DistillPO将检索后证据提炼制定为一个结构化动作，包括消息选择和证据重写。它通过分解和门控的奖励管道和结构一致的优势分配来优化这一行动，门控从有效性到质量检查的奖励成分，同时尽早暴露任务级正确性反馈并将每个奖励分配给其负责的输出范围。在LoCoMo和LongMemEval-S上，DeferMem在QA准确性和存储系统效率方面超越了强大的基线，以最快的运行时间和零的存储操作商业API令牌成本实现了最高的QA准确性。

[阅读原文](https://arxiv.org/abs/2605.22411)

---

## 45. 关注代币加权直接偏好优化

**得分**: 相关性 (Rel): 7/10, 创新性 (Nov): 7/10

**作者**: Chengyu Huang, Zhuohang Li, Sheng-Yen Chou, Claire Cardie

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a token-weighted DPO variant (AttentionPO) that uses LLM attention for content-aware token weighting, directly improving RL-based alignment.

**摘要**: arXiv：2605.21883v1宣布类型：新摘要：直接偏好优化（DPO）将大型语言模型与人类偏好结合起来，而无需单独的奖励模型。然而，DPO在回应中平等对待所有代币，忽视了各个代币的不同重要性。现有的代币级PO方法使用基于代币位置的启发式函数或单独训练的模型给出的概率估计来计算代币权重，这缺乏稳健性并会产生额外的训练成本。相比之下，我们提出了令牌加权DPO（TwDPO）--一种基于令牌加权RL的新型训练目标--和AttentionPO --TwDPO的实例，使用LLM本身的注意力来估计令牌权重。AttentionPO提示LLM充当成对判断，并检查模型在比较响应时的位置。该设计使AttentionPO具有内容感知性，可以根据响应内容调整权重，并且高效，每个示例仅需要两次额外的前向传递。实验结果表明，AttentionPO显着提高了AlpacaEval、MT-Bench和ArenaHard的性能，超过了现有的偏好优化方法。

[阅读原文](https://arxiv.org/abs/2605.21883)

---

