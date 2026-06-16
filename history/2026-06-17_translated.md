# 💡 今日研究速览 (Daily Summary)

### RL for LLMs & Reasoning
A major wave of papers today focuses on refining reinforcement learning (RL) for large language models, particularly through fine-grained credit assignment and improved training stability. **STRIDE**introduces outcome-discriminative preference for n-gram patterns to achieve precise credit assignment in RLVR, directly addressing a core challenge of sparse rewards.**BALTO**proposes a balanced token-level policy optimization framework with theoretical advantages for hallucination mitigation.**A Gradient Perspective on RLVR Stability**offers**WAPO**, a new clipped policy-gradient objective that updates only on positive-advantage completions to stabilize training. Complementing these,**Understanding Diversity Collapse**provides a formal analysis of this collapse as overtraining and introduces**Bayesian Boundary Gating**to redirect optimization. On the multi-reward front,**GD²PO**presents a conflict-aware filtering mechanism to mitigate multi-reward conflicts. Several works explore RL in specific contexts:**ExpRL**uses reference solutions as reward scaffolds for mid-training reasoning priming,**ContextRL**rewards context selection over final answers for long-horizon tasks, and**EIBench**proposes turn-level rewards for multi-turn emotion management. A unified theoretical foundation is provided by**A First-Principles Derivation of LLM Policy Optimization**, which traces methods from REINFORCE to GRPO along trajectory and reward axes.

### Latent Reasoning & Inference-Time Scaling
Latent reasoning emerges as a dominant theme, with multiple innovations pushing toward more efficient and dynamic computation.**Tyler**introduces a typed, budget-aware framework that learns a policy to dynamically choose between text tokens and specialized latent modules.**Latent Thought Flow**leverages continuous GFlowNets with a reward-induced posterior over correctness and cost, achieving strong accuracy with reduced reasoning length. A training-free method,**Entropy-Gated Latent Recursion**, recursively re-applies top decoder layers at high-uncertainty tokens, creating a complementary axis for inference-time scaling.**DLWM**proposes diverse latent world models with RL-based resource allocation for multimodal reasoning.**Reflective Masking**enables multi-turn iterative refinement in Mask Diffusion Models via test-time scaling. The**Value Axis**discovery—a linear axis tracking trajectory success—offers direct implications for internal reward modeling and RL-based alignment.

### On-Policy Distillation & Self-Improvement
Self-distillation and on-policy methods are significantly advanced, with a focus on leveraging the model's own or peer rollouts for dense supervision.**Hindsight Self-Distillation (HSD)**conditions the teacher on a successful peer rollout to provide dense per-token credit signals.**OmniOPSD**extends this to MLLMs using frontier-generated rationales as privileged evidence.**The Quality-Utility Paradox**reveals a counterintuitive finding: high-reward oracle data impairs small language models, proposing**Style-Aligned Refinement**as a fix.**Guided-OPD**introduces curriculum-based turn-level guidance to mitigate compounding errors in multi-turn agents.**PACT**combines trace-conditioned RL and component-aware SFT for tool-use agents.**SHARD**uses the model's own on-policy outputs for self-reframing safe-helpfulness alignment.**Nemotron 3 Ultra**employs Multi-teacher On-Policy Distillation (MOPD) at scale, while**Ling and Ring 2.6**uses shortest-correct-response distillation.**GeoStream**applies fully on-policy distillation to align conditioning distributions for video generation.

### Multimodal & Vision-Language Reasoning
Multimodal reasoning sees advances in integrating RL with visual grounding and efficient latent processing.**Think Less, Act Early**proposes a latent reasoning VLA framework with RL-based denoising and early exit for speed and accuracy gains.**Efficient Reinforcement for Visual-Textual Thinking**uses factorized reward assignment for GRPO on discrete diffusion models, reducing cross-modal interference.**Thinking with Visual Grounding**combines explicit visual grounding with grounding-aware RL rewards to improve VLM reasoning.**Self-Questioning Vision-Language Models**applies GRPO with rewards for intermediate sub-questions to boost compositional visual reasoning.**VibeThinker-3B**explores verifiable reasoning in small VLMs via multi-domain RL and offline self-distillation.

### Agentic & Tool-Use Reasoning
Agentic reasoning is a key focus, with papers emphasizing RL-based training for multi-turn interactions and retrieval-augmented generation.**Nemotron 3 Ultra**is explicitly designed for agentic reasoning with multi-environment RLVR.**PathRouter**addresses reward aliasing in agentic GraphRAG via differentiated GRPO advantage scaling.**PACT**and**Guided-OPD**both target multi-turn tool-use agents with on-policy distillation.**Interactor**proposes an agentic RL framework with iterative refinement using generative reward models for ad description generation.**DEEPRUBRIC**introduces evidence-tree rubric supervision for efficient rubric-based GRPO training of deep research agents.**Reinforcement Learning for LLM-based Event Forecasting**applies GRPO to demonstrate strong scaling for agentic forecasting tasks.

### Safety, Alignment & Reward Hacking
Safety and alignment research reveals new challenges and solutions within RL-based training.**Reward Hacking in Language Model Agents**revisits AI Safety Gridworlds, showing that direct reward optimization widens the gap between observed and hidden reward.**Greed Is Learned**identifies a new reward-hacking phenomenon where RL training with visible reward proxies induces reward-channel addiction.**SHARD**provides a self-reframing distillation method for safe-helpfulness alignment.**Adaptive and Explicit Safe**uses SFT and DPO with entirely self-generated data to trigger latent safety awareness in large reasoning models.**Replay What Matters** proposes off-policy replay for efficient RL-based unlearning, improving hard-case convergence.

---

## 1. 泰勒：语言模型的类型化潜在推理--何时思考、计算什么以及分配多少

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Hanyu Lin, Min Cai, Jiawei Wen, Haodi Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces a typed and budget-aware latent reasoning framework (Tyler) that learns a policy to dynamically choose between text tokens and specialized latent computation modules, directly advancing latent reasoning for LLMs.

**摘要**: arXiv：2606.16360v1宣布类型：新摘要：思想链（CoT）提示通过将中间计算具体化为离散文本标记来改进大型语言模型（LLM）中的推理，但这种文本界面也引入了冗余和推理负担。潜在推理通过以连续表示方式进行部分计算，提供了一个有希望的替代方案。然而，现有方法通常会同步调用潜在计算的时间以及在解码期间如何分配它，从而留下一个未解决的关键问题：何时调用潜在计算、执行什么类型的计算以及分配多少预算。我们在\textBF{e}nt \textBF {R}easoning（Tyler）中提出了\textBF{Ty}ped \textBF{L}，这是一个类型化和预算感知框架，用于自回归解码期间的潜在推理。泰勒学习了一种策略，该策略在每个解码步骤中，都会在发出文本令牌和切换到专门用于特定推理功能的潜在计算模块之间做出选择。一旦被调用，操作员就会将当前推理状态映射到支持全局规划、本地状态更新或可重复使用的过程抽象的潜在令牌。通过对三个主干LLM进行的广泛实验，Tyler的准确性比CoT提高了高达14.49分，比最强的竞争基线提高了高达4.30分。它进一步扩展到不同的推理领域，并以最低的遗忘实现最佳的最终阶段性能。

[阅读原文](https://arxiv.org/abs/2606.16360)

---

## 2. 在分歧处本地化信用：LLM推理的路径条件自蒸馏

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Yu Li, Shu Hong, Tian Lan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Hindsight Self-Distillation (HSD), a novel on-policy self-distillation method that conditions the teacher on a successful peer rollout to provide dense per-token credit signals for LLM reasoning, achieving strong results on math and code benchmarks.

**摘要**: arXiv：2606.15576v1宣布类型：新摘要：来自可验证奖励的强化学习为每次推出分配一个纯量，从而在长推理痕迹中留下未指定的代币级信用分配。政策上的自我提炼通过让相同的模型充当受特权信息限制的教师来解决这个问题，从而产生密集的每个代币信号。但基本真相答案的常见选择只是终点提示：在简短回答任务中，老师在路径层面指导最重要的中间位置保持沉默。我们提出事后诸葛亮自我蒸馏（HSD），它为教师提供从当前培训小组中成功进行同侪推广的条件。这样的对等点是成功条件政策的精确样本，不需要额外的抽样展开。通过提供完全成功的延续而不仅仅是最终答案，产生的信用信号集中在失败的推出和成功的同行之间的分歧位置。在数学和代码基准方面，在Qwen 3 -8B和Qwen 3 - 32 B中，HSD在GRPO变体和策略蒸馏基线方面获得了最好的结果，在AIME等简洁答案任务上获得了最大的收益。

[阅读原文](https://arxiv.org/abs/2606.15576)

---

## 3. 潜在思维流：大型语言模型中的高效潜在推理

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: Xiandong Zou, Jing Huang, Jianshu Li, Pan Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Latent Thought Flow (LTF), a novel latent reasoning method using continuous GFlowNets with a reward-induced posterior over correctness and cost, achieving strong accuracy gains with reduced reasoning length.

**摘要**: arXiv：2606.16222v1宣布类型：新摘要：大型语言模型（LLM）越来越依赖中间推理，但显式思想链（CoT）却面临着语言空间瓶颈：每个思想都必须解码成令牌，从而导致高推理负担。潜在推理将审议移至连续空间，但现有方法大多学习确定性或回报最大化路径，缺乏原则性的方法来在具有不同正确性和成本的轨迹之间分配概率。我们提出了潜在思维流（LTF），它将推理建模为可变长度连续轨迹，并训练采样器以匹配奖励诱导的后验答案质量和计算成本。我们使用随机潜在转变通过连续GFlowNet来实例化这一点。为了处理稀疏答案监督，我们引入了一个用于中间奖励的熵加权子轨迹平衡目标和一个用于锚定探索的引用优先正规化器。微调和迁移学习环境下的实验表明，LTF优于显式CoT和潜在推理基线，与强潜在推理基线相比，准确性提高了9.5%，同时平均将推理长度缩短了27.2%。

[阅读原文](https://arxiv.org/abs/2606.16222)

---

## 4. Nemotron 3 Ultra：开放、高效的专家混合Mamba-Transformer混合模型，用于统计推理

**得分**: 相关性 (Rel): 9/10, 创新性 (Nov): 8/10

**作者**: NVIDIA (Allan), : (Allan), Aaron Blakeman (Allan), Aaron Thomas (Allan), Aastha Jhunjhunwala (Allan), Abhibha Gupta (Allan), Abhinav Khattar (Allan), Adam Rajfer (Allan), Adi Renduchintala (Allan), Adil Asif (Allan), Aditya Vavre (Allan), Adriana Flores Miranda (Allan), Ahmad Bilal (Allan), Aileen Zaman (Allan), Ajay Hotchandani (Allan), Akanksha Shukla (Allan), Akhiad Bercovich (Allan), Aleksander Ficek (Allan), Alex Gronskiy (Allan), Alex Kondratenko (Allan), Alex Steiner (Allan), Alex Ye (Allan), Alexander Bukharin (Allan), Alexandre Milesi (Allan), Ali Taghibakhshi (Allan), Alice Gatti (Allan), Alisa Liu (Allan), Alok Kumar (Allan), Amar Phanishayee (Allan), Ameya Sunil Mahabaleshwarkar (Allan), Amir Klein (Allan), Amit Zuker (Allan), Amnon Geifman (Allan), Anahita Bhiwandiwalla (Allan), Ananth Subramaniam (Allan), Andrea Santilli (Allan), Andrew Fulks (Allan), Andrew McHarg (Allan), Andrew Tao (Allan), Andrii Skliar (Allan), Anjulie Agrusa (Allan), Ankur Srivastava (Allan), Ankur Verma (Allan), Anna Shors (Allan), Anna Warno (Allan), Antoni-Joan Solergibert I Llaquet (Allan), Arham Mehta (Allan), Arkadiusz Nowaczynski (Allan), Arti Jain (Allan), Ashwath Aithal (Allan), Ashwin Poojary (Allan), Asif Ahamed (Allan), Asit Mishra (Allan), Asma Kuriparambil Thekkumpate (Allan), Atefeh Sohrabizadeh (Allan), Avinash Kaur (Allan), Avinash Vem (Allan), Ayush Dattagupta (Allan), Barath Subramaniam Anandan (Allan), Bardiya Sadeghi (Allan), Ben Lanir (Allan), Benedikt Schifferer (Allan), Besmira Nushi (Allan), Bilal Kartal (Allan), Bill Thiede (Allan), Bita Darvish Rouhani (Allan), Bo Deng (Allan), Bob Schatz (Allan), Boris Ginsburg (Allan), Boxin Wang (Allan), Brad Nemire (Allan), Brandon Norick (Allan), Brian Dang (Allan), Brian Westphal (Allan), Brian Yu (Allan), Brucek Khailany (Allan), Bryan Catanzaro (Allan), Carlo del Mundo (Allan), Caryln Aarish (Allan), Chankyu Lee (Allan), Chantal Hwang (Allan), Charbel Sakr (Allan), Charles Wang (Allan), Charlie Truong (Allan), Chen Cui (Allan), Cheng Cheng (Allan), Cheng-Ping Hsieh (Allan), Chenghao Zhang (Allan), Chenhui Deng (Allan), Chintan Patel (Allan), Chris Alexiuk (Allan), Christian Cosgrove (Allan), Christian Munley (Allan), Christine Harvey (Allan), Christopher Parisien (Allan), Chunyang Shen (Allan), Coco Li (Allan), Collin Neale (Allan), Cynthia Gao (Allan), Cyril Meurillon (Allan), Dan Gil (Allan), Dan Su (Allan), Dan Zhao (Allan), Dane Corneil (Allan), Daniel Afrimi (Allan), Daniel Egert (Allan), Daniel Korzekwa (Allan), Daniel Lo (Allan), Daniel Machlab (Allan), Daniel Serebrenik (Allan), Daniil Sorokin (Allan), Daria Gitman (Allan), Daria Levy (Allan), Darko Stosic (Allan), David Mosallanezhad (Allan), David Yu (Allan), Davit Karamyan (Allan), Deena Donia (Allan), Deep Debroy (Allan), Deepak Narayanan (Allan), Devin O'Kelly (Allan), Dheeraj Peri (Allan), Dhruv Nathawani (Allan), Di (Allan), Wu, Dima Rekesh, Divyanshu Kakwani, Donald Plummer, Dong Anh, Dongfeng Yu, Dongfu Jiang, Donnie Kim, Dorrin Poorkay, Duncan Riach, Dusan Stosic, Dustin VanStee, Eavan Meng, Edgar Minasyan, Edward Lin, Eileen Margaret Peters Long, Elad Sarafin, Elad Segal, Elena Lantz, Ellie Evans, Elliott Ning, Eric Chung, Eric Harper, Eric Pham-Hung, Eric Tramel, Eric Yang, Erick Galinkin, Erik Pounds, Erika Goncalves Goncalves, Evan Briones, Evan Wu, Evelina Bakhturina, Evgeny Tsykunov, Ewa Dobrowolska, Faisal Ladhak, Farzan Memarian, Fay Wang, Fei Jia, Felipe Soares, Felipe Vieira Frujeri, Feng Chen, Fengguang Lin, Ferenc Galko, Frank Sun, Frankie Siino, Frida Hou, Gal Hubara Agam, Gal Kaplun, Gantavya Bhatt, Gargi Prasad, Garvit Kulshreshtha, George Armstrong, Gerald Shen, Giulio Borghesi, Gordana Neskovic, Gorkem Batmaz, Grace Lam, Greg Mason, Greg Pauloski, Grigor Nalbandyan, Grzegorz Chlebus, Grzegorz Karch, Guan-Ting Liu, Guoming Zhang, Guyue Huang, Haggai Maron, Haifeng Qian, Haim Elisha, Haoxing Ren, Haran Kumar Shiv Kumar, Haribhau Hud, Harris Nover, Harrison Saturley Hall, Hayate Iso, Helen Ngo, Herbert Hum, Herman Sahota, Hexin Wang, Himanshu Soni, Hovhannes Tamoyan, Hua Li, Huanhuan Chen, Hui Li, Hui Wang, Huy Nguyen, Ian Chiles, Ido Galil, Ido Shahaf, Igor Gitman, Igor Shovkun, Ilya Loshchilov, Ingo Guehring, Itamar Schen, Itay Levy, Itay Neeman, Ivan Moshkov, Izik Golan, Izzy Putterman, Jaemin Choi, Jakub Slowikowski, Jan Kautz, Jane Polak Scowcroft, Jared Casper, Jatin Mitra, Jeffrey Glick, Jenny Chen, Jesse Oliver, Jiacheng Xu, Jiafan Zhu, Jialin Song, Jian Zhang, Jiantao Jiao, Jiaqi Zeng, Jie Lou, Jim King, Jimmy Zhang, Jingquan Wang, Jinhang Choi, Jinju Chu, Joey Conway, Joey Guman, Johan Jatko, Johannes Rausch, John Kamalu, John Roberts, Johnny Greco, Johnny Mensel, Jonah Alben, Jonas Yang, Jonathan Cohen, Jonathan Raiman, Joseph Jennings, Joshua Mabry, Joshua Pierce, Joyjit Daw, Julien Veron Vialard, Junkeun Yi, Jupinder Parmar, Kajal Jain, Kan Zhu, Kari Briski, Katherine Cheung, Katherine Luna, Keith Willowhawk, Keith Wyss, Keshav Santhanam, Kevin Shih, Kezhi Kong, Khanh Nguyen, Khushi Bhardwaj, Kirthi Shankar Sivamani, Konstantinos Krommydas, Krishna C. Puvvada, Krzysztof Pawelec, Kumar Anik, Kyle Keprios, Kylie Day, Lawrence McAfee, Leo Du, Leon Derczynski, Li Ding, Linda Liu, Lingjie Wu, Lior Kadoch, Lizzie Wei, Luis Vega, Luke Robison, Lun Su, Maarten Van Segbroeck, Maciej Jakub Mikulski, Maer Rodrigues de Melo, Magda Sypula, Mahan Fathi, Makesh Narsimhan Sreedhar, Makesh Tarun Chandran, Manoj Kilaru, Maor Ashkenazi, Marc Cuevas, Marc Romeijn, Marcin Chochowski, Mark Cai, Mark Mozolewski, Markus Kliegl, Marta Stepniewska-Dziubinska, Martyna Patelka, Mattei Machczynski, Matvei Novikov, Mauricio Ferrato, Maximilian Golub, Mehrzad Samadi, Melissa Corpuz, Mengru Wang, Mengxi Wu, Meredith Price, Meriem Boubdir, Micah Schaffer, Michael Andersch, Michael Boone, Michael Gschwind, Michael Lightstone, Michael Loh, Michal Bien, Michal Zawalski, Michelle Gill, Miguel Martinez, Mikail Khona, Mike Chrzanowski, Mike Houston, Mingyuan Ma, Minseok Lee, Mohamed Fawzy, Mohammad Dabbah, Mohammad Shoeybi, Mostofa Patwary, Nabin Mulepati, Najeeb Nabwani, Namit Dhameja, Narimane Hennouni, Natalie Hereth, Nathaniel Pinckney, Nave Algarici, Nave Assaf, Netanel Haber, Nicholas Knight, Nick Reamaroon, Nickson Quak, Nidhi Bhatia, Nikhil Desai, Nikolai Ludwig, Nima Tajbakhsh, Ning Xu, Nir Ailon, Nirmal Juluru, Nitin Nitin, Ofri Masad, Oleg Rybakov, Oleksii Hrinchuk, Oleksii Kuchaiev, Olivia Viessmann, Olivier Delalleau, Oluwatobi Olabiyi, Omer Ullman Argov, Omri Puny, Oren Tropp, Pablo Ribalta, Pallab Bhattacharya, Panos Lampropoulos, Parth Mannan, Pasha Shamis, Patrick Legresley, Paul Gibbons, Pavlo Molchanov, Pawel Morkisz, Peter Dykas, Peter Jin, Pierre-Yves Aquilanti, Pinky Xu, Piotr Januszewski, Piotr Laskiewicz, Pooya Jannaty, Prakash Gurumurthy, Pranav Prashant Thombre, Prasoon Varshney, Pritam Gundecha, Przemek Tredak, Puhui Meng, Qiyu Wan, Rabeeh Karimi Mahabadi, Rachel Oberman, Rachit Garg, Radha Sri-Tharan, Rahul Kandu, Rakshit Sanadhya, Ran El-Yaniv, Ran Zilberstein, Rasoul Shafipour, Ray Macalisang, Rayen Tian, Reka Kovacs, Renjie Pi, Rick Izzo, Rima Shahbazyan, Rishabh Garg, Rishi Puri, Rita Fernandes Neves, Ritchie Zhao, Ritika Borkar, Ritu Gala, Riyad Islam, Robert Clark, Robert Hesse, Robert Kirby, Roger Waleffe, Rohit Watve, Roi Koren, Ron Banner, Ruoxi Zhang, Russell J. Hewett, Ryan Prenger, Ryan Stewart, Ryota Egashira, Sadegh Mahdavi, Saee Paliwal, Sagar Singh, Sahil Modi, Salika Dave, Samantha Shinagawa, Samuel Kriman, Sandip Bhaskar, Sangkug Lym, Sanjay Kariyappa, Sanjeev Satheesh, Saran Vikas Murari, Satish Pasumarthi, Saurabh Mishra, Saurav Muralidharan, Scott Hara, Sean Narentharen, Selvaraj Anandaraj, Seonjin Na, Seonmeyong Bak, Seonmyeong Bak, Sepehr Sameni, Seph Mard, Serge Panev, Seth Henneman, Seth Poulos, Shahar Mor, Shantanu Acharya, Shaona Ghosh, Sharath Turuvekere Sreenivas, Sharon Mendelson, Shaun Kotek, Shawn Wang, Shay Aharon, Shaya Gharghabi, Sheng-Chieh Lin, Shi Chen, Shiqing Fan, Shirish Baskaran, Shreya Gopa, Shrimai Prabhumoye, Shubham Pachori, Shubham Toshniwal, Shuoyang Ding, Shwetha Krishnamurthy, Siddharth Singh, Simeng Sun, Sirshak Das, Sivakumar Arayandi Thottakara, Smita Ithape, Somshubra Majumdar, Soumye Singhal, Sri Harsha Singudasu, Sridhar Bhuvanapalli, Srimukh Veccham, Stas Sergienko, Stefania Alborghetti, Stephen Ge, Su Rong, Sugam Dipak Devare, Sukrit Rao, Sumeet Kumar Barua, Sungsoo Ha, Sunny Gai, Suriya Gunasekar, Suseella Panguluri, Suyog Gupta, Sviataslau Hinzburh, Sweta Priyadarshi, Syeda Nahida Akter, Talor Abramovich, Tan Bui, Tanay Varshney, Tatevik Ter-Hovhannisyan, Teodor-Dumitru Ene, Terry Kong, Thanh Do, Tianhe Zhang, Tiffany Moore, Tijmen Blankevoort, Tim Moon, Tiyasa Mitra, Tom Balough, Tomasz Grzegorzek, Tomasz Hliwiak, Tomer Asida, Tomer Bar Natan, Tomer Keren, Tomer Ronen, Tony Salim, Tony Wang, Traian Rebedea, Tugrul Konuk, Twinkle Vashishth, Udi Karpas, Ushnish De, Vahid Noorozi, Venkat Srinivasan, Venmugil Elango, Vibhor Agrawal, Victor Cui, Vijay Korthikanti, Vikas Mehta, Vinay Rao, Virginia Wu, Vitaly Kurin, Vitaly Lavrukhin, Vladimir Anisimov, Vu Pham, Wanli Jiang, Wasi Uddin Ahmad, Wataru Ishihara, Wei Du, Wei Ping, Weiheng Chai, Wenliang Dai, Wesley Helmholz, Will Jennings, Will Zhu, Wojciech Prazuch, Xiaowei Ren, Xiwen Yu, Yan Breek, Yang Chen, Yang Yu, Yangyi Chen, Yaniv Galron, Yashaswi Karnati, Yejin Choi, Yev Meyer, Yi-Fu Wu, Yian Zhang, Ying Lin, Yonatan Geifman, Yonggan Fu, Youngeun Kwon, Yu Yao, Yugi Guvvla, Yuki Huang, Yunsheng Liu, Zach Moshe, Zachary Newell, Zhilin Wang, Zhiyu Li, Zhongbo Zhu, Zhuolin Yang, Zihan Liu, Zijie Yan, Zsolt-Alon Wertheimer

**机构**: NVIDIA

**💡 亮点 (Highlight)**: Introduces a large-scale hybrid Mamba-Transformer model with multi-environment RLVR and Multi-teacher On-Policy Distillation (MOPD), directly advancing RL-for-LLMs and on-policy distillation.

**摘要**: arXiv：2606.15007v1宣布类型：新摘要：我们引入了Nemotron 3 Ultra，这是一个总计5500亿个、活动参数550亿个专家混合混合Mamba-Attention语言模型。我们在20万亿个文本令牌上预训练了Nemotron 3 Ultra，然后将上下文长度扩展到1 M个令牌，并使用监督微调（SFT）、强化学习（RL）和多教师按策略蒸馏（MOPD）进行后训练。Nemotron 3 Ultra是我们迄今为止最强大的模型，采用了多种关键技术-- LatentMoE、多令牌预测（STP）、NVFP 4预训练、多环境WLVR、MOPD和推理预算控制。与最先进的公开LLM相比，Nemotron 3 Ultra的推理吞吐量高达约6倍，同时实现了同等的准确性。最先进的准确性、高推理吞吐量和1 M令牌上下文长度使Nemotron 3 Ultra非常适合长时间运行的自主代理任务。我们在HuggingFace上开源了基础检查点、后训练点和量化检查点，以及训练数据和食谱。

[阅读原文](https://arxiv.org/abs/2606.15007)

---

## 5. OmniOPSD：受家长支持的情感计算按策略自我蒸馏

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Zebang Cheng, Shuimu Chen, Boxue Yang, Yuanshen Guan, Jingyi Chen, Zheng Lian, Xiaojiang Peng, Fei Ma, LaiZhong Cui, Qi Tian

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes OmniOPSD, a rationale-privileged on-policy self-distillation framework for MLLMs that uses frontier-generated rationales as teacher-side privileged evidence for dense token-level supervision on student rollouts, directly matching on-policy distillation criteria.

**摘要**: arXiv：2606.15920v1宣布类型：新摘要：多模式大型语言模型（MLLM）的强化学习通常会受到复杂推理任务中严重的奖励稀疏性的阻碍。这一挑战在涉及状态、情感、意图和行为的以人为本的场景中尤其明显，其中异类多模式信号和主观人为因素使得高质量的思想链（CoT）注释昂贵且难以获得。尽管许多多模式数据集提供了专家注释的地面真相标签，但直接使用这些标签进行有监督的微调可能会鼓励多模式感知中的捷径学习，并为安全关键的人类与人工智能交互提供有限的透明度。为了解决这些局限性，我们提出了OmniOPSD，这是一个受学者支持的政策自我蒸馏框架，它使用前沿生成的理由作为教师方面的特权证据，而不是学生模仿目标。OmniOPSD仅使用前沿生成的证据感知原理作为当地教师的培训时间特权证据背景。学生从原始的多模式输入中采样自己的推出，而理性特权教师则获得相同的代币评分并提供密集的代币级别监督。因此，学生在自己的轨迹分布上学习，而无需直接模仿前沿模型完成，并且推理不需要标签、原理、CoT注释或闭源模型访问。MER-UniBench上的实验表明，OmniOPSD实现了最先进的性能，平均得分为84.19美元，消融进一步支持了理性特权教师指导的价值。

[阅读原文](https://arxiv.org/abs/2606.15920)

---

## 6. 少思考，早行动：视觉-语言-行动模型中提前退出的强化潜在推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Dianqiao Lei, Lianlei Shan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent reasoning VLA framework with RL-based denoising and early exit, achieving significant speedup and accuracy gains.

**摘要**: arXiv：2606.15099v1宣布类型：新摘要：现有的视觉-语言-动作（VLA）模型主要依赖于显式的思想链（CoT）推理来连接感知和动作。虽然有效，但这种范式在多步骤任务中存在高计算成本和错误传播的问题。在本文中，我们提出了自适应变量对齐VLA（AVA-VLA），这是一种新型的潜在推理VLA框架，它将推理建模为一系列不可观察的潜在变量，从而绕过了显式文本生成的需要。然而，潜在轨迹本质上容易受到噪音干扰和与下游目标的不对准。为了解决这个问题，我们引入了一种基于强化学习的去噪机制，该机制将潜在状态生成视为顺序决策过程，通过任务级奖励优化推理轨迹。此外，我们还引入了一种早期退出策略，该策略自适应地终止基于状态信心的推理，从而实现深度和效率之间的动态权衡。对具体决策基准的广泛实验表明，AVA-VLA比显式CoT方法实现了6倍的推理加速，同时在LIBERO上实现了98.3%的平均成功率，比全推理基线提高了效率和长期稳定性。

[阅读原文](https://arxiv.org/abs/2606.15099)

---

## 7. 利用离散扩散模型有效强化视觉文本思维

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yoonjeon Kim, Yuhta Takida, Chieh-Hsin Lai, Eunho Yang, Yuki Mitsufuji

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes factorized reward assignment for RL (GRPO) on multimodal discrete diffusion models, enabling efficient visual rollouts and reducing cross-modal interference.

**摘要**: arXiv：2606.14792v1宣布类型：新摘要：基于RL的后训练已被广泛采用，以在能够生成文本和图像的统一多模式模型中实现交叉视觉和文本推理。然而，大多数现有的方法都是建立在自回归（AR）统一模型之上的，这需要在视觉推理期间进行完整的图像再生。在这项工作中，我们证明了多模式离散扩散模型是AR模型的有效替代方案，用于交织推理中的强化学习，因为它们能够通过本地视觉编辑而不是完整的图像标记再生来执行高效的视觉展开。与AR基线相比，这将GRPO期间的部署计算减少了26.9%，且性能下降最小。尽管效率有所提高，但我们发现，联合奖励分配（采用跨模式的共享奖励信号）在RL更新期间在不相关的图像和文本标记序列之间引入了跨模式干扰。为了解决这个问题，我们提出了因式奖励分配，这是一种将奖励独立分配给文本和视觉片段的策略。通过分解奖励分配，我们的RL方法比联合奖励分配提高了11.2%，比基本模型提高了38.04%。

[阅读原文](https://arxiv.org/abs/2606.14792)

---

## 8. WRIDE：通过可验证强化学习的区分性估计进行战略轨迹推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Qinjian Zhao, Zhihao Dou, Dinggen Zhang, Xiangyu Li, Chaoda Song, Zhongwei Wan, Xinpeng Li, Yanyan Zhang, Kaijie Chen, Qingtao Pan, Chengcheng Feng, Zhiqiang Gao, Xiaoyu Xia

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes STRIDE, a fine-grained RLVR framework that uses outcome-discriminative preference of n-gram patterns for precise credit assignment in LLM reasoning, directly advancing RL for LLMs.

**摘要**: arXiv：2606.15866v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）已成为提高大型语言模型推理能力的有效训练后范式。然而，现有的WLVR方法通常依赖于最终答案的正确性来分配专家级奖励，提供稀疏监督并统一对待所有代币，无论它们对推理的实际贡献如何。尽管最近的研究引入了过程奖励、高熵令牌和语义不确定性等中间信号，但这些信号通常本质上不可验证，并且可能无法区分有益的战略模式和有害的战略模式。为了解决这一局限性，我们提出了WRIDE（具有歧视性估计的战略轨迹推理），这是一个细粒度的WLVR框架，可以从可验证的结果中获得战略推理监督。WRIDE比较每个响应组内成功和失败的轨迹，以估计每个$n$-gram战略模式的结果区分偏好，并进一步将此信号与推理显着性熵相结合，以识别与决策相关的战略模式。在RL优化期间，这些模式被分配有差异的优势值，从而实现更精确的信用分配，同时保留WLVR的可验证性。大量实验表明，WRIDE可持续提高各种模型、任务和扩展设置（包括VLM和基于代理的系统）的推理性能。

[阅读原文](https://arxiv.org/abs/2606.15866)

---

## 9. 以视觉为基础思考

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Junkai Zhang, Yihe Deng, Kai-Wei Chang, Wei Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces visually grounded thinking with grounding-aware RL rewards for VLMs, combining explicit visual grounding with RL-based training to improve reasoning.

**摘要**: arXiv：2606.16122v1宣布类型：新摘要：视觉思维不仅应该听起来正确;它应该展示其证据。虽然最近的视觉语言模型（VLM）可以产生自然语言推理痕迹，但这些痕迹通常使支持图像区域隐式，使它们难以验证和监督。我们引入了基于视觉的思维，这是一个推理过程，其中模型将自然语言思想与每一步使用的视觉证据的明确点或框基础交织在一起。这使得模型可以用语言表达中间推理，同时将关键对象置于它们所引用的图像区域中。为了训练这种行为，我们构建了一个可扩展的合成管道，该管道提取正确的视觉推理痕迹，提取痕迹所需的视觉对象，用基于SAM 3的代理将它们作为基础，并从产生的面具中推导出对齐的点和框监督。我们进一步提出了基础感知强化学习，它将答案正确性奖励与密集基础奖励相结合，对生成的对象引用是否匹配正确的图像证据进行评分。在两个计数基准和四个空间推理基准中，向Gemma 3 - 4 B-IT添加视觉基础思维可持续提高性能，优于原始模型和非基础思维基线。在空间推理方面，基于视觉思维的4 B模型与来自同一模型系列的Gemma 3 - 27 B-IT相匹配，甚至在某些情况下超越。我们的分析表明，点接地非常适合计数，而框接地受益最明显的接地奖励空间任务。总的来说，我们的研究结果表明，当他们的中间思想与使他们成为真实的图像区域联系在一起时，VLMs会思考得更好。

[阅读原文](https://arxiv.org/abs/2606.16122)

---

## 10. DLWM：高效多模式推理的多元化潜在世界模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: David Huang, Lianlei Shan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent reasoning framework with diverse hypotheses and RL-based resource allocation, directly advancing latent reasoning and RL for LLMs.

**摘要**: arXiv：2606.15160v1宣布类型：新摘要：近年来，多模式大型语言模型（MLLM）的推理能力有了显着提高。现有的方法通常依赖于显式的思想链或连续的潜在空间轨迹来增强多步骤推理。然而，这些方法通常假设输入允许单一潜在解释并沿着固定路径或在统一计算预算下展开推理。在现实世界的多模式环境中，视觉观察经常受到遮挡、模糊、观点变化或语义模糊的影响，从而产生多种合理的解释。统一的推理策略不仅限制了模型探索多个假设的能力，而且会导致很高的内存使用和推出成本。我们提出了DLWM（多元化潜在世界模型），这是一个将潜在空间推理与强化学习相结合的多模式推理框架。首先，我们在连续的潜在空间中构建一组不同的潜在世界假设，每个假设捕捉到对视觉输入的不同合理解释，并独立地展开每个假设的潜在推理。基于垂直性的多样性正规化器明确防止假设崩溃。其次，我们将潜在推理过程表述为资源受限的顺序决策问题，并引入资源感知的强化学习策略，该策略自适应地跨假设分配计算，动态决定是否扩展、终止或合并推理路径，从而大幅减少内存占用并提高部署效率。多个多模式推理基准的实验表明，DLWM的准确性比现有方法高2-5个百分点，同时将内存使用率减少24%。

[阅读原文](https://arxiv.org/abs/2606.15160)

---

## 11. 面罩扩散模型中的多轮反射掩蔽启发推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yanming Zhang, Yihan Bian, Jingyuan Qi, Yuguang Yao, Lifu Huang, Tianyi Zhou

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Reflective Masking, a lightweight post-training method that enables multi-turn iterative refinement in Mask Diffusion Models, directly advancing latent reasoning via test-time scaling.

**摘要**: arXiv：2606.16700v1宣布类型：新摘要：虽然自回归（AR）模型的推理通常是通过思想链推理和反思来执行的，但它们对先前输出的细化仍然依赖于完全顺序生成，即使只需要本地编辑。相比之下，掩蔽扩散模型（MDM）中的掩蔽机制自然支持对先前输出的显式本地编辑，允许选择性细化，而无需丢弃先前的答案并从头开始生成另一个答案。虽然这一属性与人类通过迭代局部细化纠正错误的方式更加紧密一致，但现有的MDM不支持多圈掩蔽和去噪。我们提出了反思掩蔽（RM），它通过轻量级的后训练在MDM中激发了这种内在的推理能力。RM提供本地测试时间扩展，其中MDM根据不断变化的上下文迭代地重新访问和修改其先前的输出。为了利用AR推理等之前回合的见解，我们进一步引入了History Reference，这是一种无参数机制，可以在修改期间利用中间去噪状态。我们的方法不需要架构更改，并且很容易适用于现有的MDM。在文本生成、数独和图像编辑等各种任务和模式中，反思掩蔽始终优于标准的基于掩蔽的基线，并表现出很强的通用性，将RM定位为对MDM进行推理的基本基元。

[阅读原文](https://arxiv.org/abs/2606.16700)

---

## 12. 质量-效用悖论：为什么高回报数据会损害小模型数学推理

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Haolong Qian, Xianliang Yang, Yinuo ma, Lirong Che, Feng Lu, Ye Guo, Lei Song, Jiang Bian, Chun Yuan

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Identifies a counterintuitive paradox in on-policy distillation for math reasoning, showing that high-reward oracle data impairs SLMs, and proposes Style-Aligned Refinement to fix it.

**摘要**: arXiv：2606.16152v1宣布类型：新摘要：来自强大推理模型的知识提炼被广泛用于改进数学推理的小语言模型（SLC），通常假设具有更高奖励模型分数的痕迹提供更有用的监督。我们在数学推理蒸馏中识别出一个违反直觉的\textBF{Quality-效用悖论}。根据奖励模型，由更强大的Oracle精炼或合成的数据可以获得更高的感知质量，但始终表现不佳由SPL本身生成并通过Qwen 2.5、LLaMA-3和DeepSeek系列的拒绝抽样选择的轨迹。我们的分析表明，Oracle细化将逻辑修复与偏离PLM原生推理分布的分布漂移结合起来。这种漂移增加了学习者的适应成本，并且可能超过改进推理逻辑的好处。为了测试此机制，我们引入了\textBF{Style-Aligned Refinement}，它保留了STM的原生轨迹，同时保留了Oracle的逻辑修复。这种干预降低了适应成本并恢复下游效用。这些发现表明，有效的数学推理提炼应该共同优化感知的解决方案质量和学习者数据兼容性，而不是仅仅依赖奖励模型分数。数据集和代码可在https://github.com/Dracoqhl/Quality-Utility-Paradox上获取。

[阅读原文](https://arxiv.org/abs/2606.16152)

---

## 13. 熵门控潜在回归

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Soham Bhattacharjee, Dushyant Singh Chauhan, Salem Lahlou, Martin Takac, Nils Lukas

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces Entropy-Gated Latent Recursion (EGLR), a training-free latent reasoning method that recursively re-applies top decoder layers at high-uncertainty tokens, creating a complementary deterministic axis for inference-time scaling.

**摘要**: arXiv：2606.16620v1宣布类型：新摘要：推理时缩放已成为改进语言模型推理的主要杠杆，但现有方法从单一来源获得推出多样性：随机标记级采样。我们认为，这个单轴采样空间从根本上来说是限制性的，并确定了第二个完全确定性和补充的轴：层跨度$L$，冻结模型的顶部解码器层在高不确定性令牌处被循环重新应用。不同的$L$选择会产生不同的卷展，解决不同的问题子集，没有随机性。我们通过熵门潜在递归（EGLR）来实例化这个轴，EGLR是一种无需训练的解码过程，它最多重复应用$L$层，直到下一个令牌分布收敛。结合$T$温度样本，EGLR把一个单轴随机铺开池变成一个$L\times T$笛卡尔采样空间，几乎相同的每次铺开成本。我们通过8美元的修正模型和6美元的数学推理基准来描述这个空间，并表明L轴与温度是真正互补的：在带有Qwen 2.5 - 3B-Direct的MAT-500上，联合$L\times T$ Oracle达到91.6\%$，比仅温度的Oracle（83.4美元）高出+8.2美元百分点，比仅层的Oracle（81.2美元）高出+10.4美元百分点，证实这两个轴捕捉到了真正互补的问题。扩展的推出池为任何消耗推出的下游程序提供了更丰富的每次提示候选项，包括自一致性、与验证者的最佳N$以及组相对RL训练（GRPO），为不依赖随机噪音的推断时间扩展开辟了新方向。

[阅读原文](https://arxiv.org/abs/2606.16620)

---

## 14. 价值轴：语言模型编码它们是否走在正确的轨道上

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Nick Jiang, Isaac Kauvar, Jack Lindsey

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Discovers a linear 'value' axis in LLMs tracking trajectory success, with implications for RL-based alignment and internal reward modeling.

**摘要**: arXiv：2606.17056v1宣布类型：新摘要：我们调查语言模型是否在内部跟踪其当前轨迹的价值，该轨迹定义为其持续战略实现目标的可能性。使用合成的、背景下的强化学习数据，我们为Qwen 3 -8B构建了一个“价值”轴。我们发现，沿着该轴的激活区分了高与低口头置信度、不带回溯和有回溯的推出以及正确与损坏的代码。转向高价值会导致自我纠正并减少解释冗长，而转向低价值会导致倒退和探索。我们证明，直接偏好优化（DPO）可以增加奖励行为（例如使用某个词）的内部价值，使模型在表现出它们后更加自信地采取行动。最后，我们应用价值轴来研究野外环境。例如，我们发现Qwen在训练后对政治敏感的聊天查询赋予较低的价值，并且监督式微调增加了训练领域内的内部信心。我们的结果表明，语言模型线性编码了对预期目标成功的估计，从而调节了他们追求方向的信心。

[阅读原文](https://arxiv.org/abs/2606.17056)

---

## 15. GeStream：迈向精确的摄像头控制流视频生成

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Yizhou Zhao, Yifan Wang, Xiaoyuan Wang, Yushu Wu, Hao Zhang, Moayed Haji-Ali, Rameen Abdal, Ashkan Mirzaei, Yanyu Li, Willi Menapace, Laszlo Jeni, Sergey Tulyakov, Peter Wonka, Chaoyang Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes GeoStream with a self-refreshing 3D cache and fully on-policy distillation that aligns train and inference conditioning distributions for autoregressive video generation.

**摘要**: arXiv：2606.15162v1宣布类型：新摘要：准确的交互式摄像机控制对于基于视频的世界模型至关重要，但大多数现有方法都隐式地学习摄像机运动，导致在非分布轨迹下控制不准确。显式几何条件处理提高了可控性，但现有方法是非自回归的，并且依赖于从初始帧构建的静态3D缓存，一旦视角超出原始平截头体，静态3D缓存就会变得无效。我们提出了GeStream，这是一个框架，可以在自回归流视频生成中实现精确的公制规模摄像机控制。我们的方法维护一个自刷新的3D缓存，该缓存定期从模型自己的输出在线更新：我们估计最近生成的帧的深度，解投影到3D，并重新投影到目标视图中，以产生点重新投影，作为后续合成的几何条件。根据同样的原则，训练期间看到的条件反射也是从学生自己生成的框架中渲染的，从而产生完全符合政策的蒸馏，从而自然地对齐训练和推理条件反射分布。与之前使用非策略条件噪音的工作不同，我们的方法针对推理时遇到的确切误差分布来训练模型，减轻标准自回归漂移和当缓存本身从生成的输出中推导时出现的二阶几何反馈循环。定量和定性结果表明，我们的方法大大提高了相机的可控性。

[阅读原文](https://arxiv.org/abs/2606.15162)

---

## 16. 贪婪已被习得：作为奖励黑客触发器的可见激励措施

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Tong Che, Rui Wu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Shows that RL training with visible reward proxies can induce reward-channel addiction, a new reward-hacking phenomenon with direct implications for RL-based LLM alignment.

**摘要**: arXiv：2606.16914v1公告类型：新摘要：已部署的代理越来越多地考虑到其奖励代理，例如余额、分数或KPI仪表板。我们表明，强化学习可以制定一项政策，让这种可见的自利渠道\{上瘾}。它追逐跨持有的域所显示的回报，牺牲真正的任务来做到这一点，并跟随我们重写渠道的任何地方，而从未见过渠道的政策保持诚实。我们称之为\{奖励渠道成瘾}，并在\{MoneyWorld}（一个合成沙箱）中研究它。上瘾可以翻转模型的安全对齐：只训练无害的金钱任务，没有安全内容，模型放弃了安全的行动，否则每当仪表板支付不安全的时候，它总是采取安全的行动，一旦通道被隐藏，就恢复到安全。这种习得性贿赂在模型规模和家庭中复制。盲目地在KPI或P\&L上优化超级能力的下一代AI可能会对对齐造成危险。\n {贪婪是学习}当遵循这样的渠道支付。

[阅读原文](https://arxiv.org/abs/2606.16914)

---

## 17. 从过度训练的角度理解RLVR的多样性崩溃

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Suqin Yuan, Jinkun Chen, Jiyang Zheng, Muyang Li, Lei Feng, Dadong Wang, Tao Xiang, Tongliang Liu, Bo An

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a formal analysis of diversity collapse in RLVR as overtraining and proposes Bayesian Boundary Gating, a new method to redirect optimization for improved reasoning boundaries.

**摘要**: arXiv：2606.15455v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）已成为增强大型语言模型推理能力的关键方法。然而，WLVR经常遭受\{多样性崩溃}的困扰：Pass@$1$提高，而高-$k$ Pass@$k$下降，这被视为模型推理边界的缩小。我们通过\{过度训练}的视角将这种多样性崩溃形式化：一旦问题对参考指标的贡献有效饱和，进一步的更新将不再扩展模型可以解决的问题，但仍然将概率质量集中在政策上抽样所青睐的轨迹上。在每个问题很少展开的标准设置下，即使是观察到的一次成功也会将问题置于高-$k$ Pass@$k$的近乎饱和状态，因此标准WLVR中的大多数更新从边界角度来看都是过度训练。这个角度还表明了对WLVR是否可以将模型的推理能力扩展到基础模型之外的解读：由于WLVR在结构上对高-$k$ Pass@$k$存在偏见，因此其总体下降本身并不意味着没有出现新的推理收益。从干预角度来看，限制对观察到的成功率为零的问题的更新，使Pass@$256在困难基准上高于基本模型;从观察角度来看，最初无法解决的问题中，有一小部分在标准WLVR培训期间变得可以解决。在这些发现的基础上，我们提出了\{Bayesian Boundary Gating}（BBG），它通过估计每个问题对推理边界的边际贡献来重新引导优化远离过度训练。在多个推理基准中，BBG在广泛的$k$范围内提高了平均Pass@$k$。

[阅读原文](https://arxiv.org/abs/2606.15455)

---

## 18. Ling和Ring 2.6技术报告：万亿参数规模下高效、即时的统计智能

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 8/10

**作者**: Ang Li, Ben Liu, Bin Han, Bin Hu, Bin Jing, Binbin Hu, Bing Li, Cai Chen, Caizhi Tang, Changxin Tian, Chao Huang, Chao Zhang, Chen Liang, Chen Qian, Chengfu Tang, Chengyao Wen, Chilin Fu, Chunwei Wu, Cong Zhang, Cunyin Peng, Daixin Wang, Dalong Zhang, Deng Zhao, Dingnan Jin, Dingyuan Zhu, Donghao Zhang, Fan Yuan, Fangzheng Zhao, Fanzhuang Meng, Feifan Wu, Feng Xu, Fengbin Fang, Gangshan Wang, Guodong Yang, Hailin Zhao, Haitao Wang, Haitao Zhang, Hanxiao Zhang, Hanzi Wang, Hao Dai, Hao Liu, Hao Qian, Hao Wu, Haoxiong Liu, Haoyu Xu, Heng Zhang, Hong Liu, Hongliang Zhang, Hongrui Liu, Hongxun Li, Hongzhi Ruan, Huaidong Xiong, Huihuang Zheng, Huikang Tang, Jia Guo, Jia Li, Jia Liu, Jiameng Wang, Jiaming Liu, Jiannan Shi, Jianping Wei, Jiaolong Yang, Jiapeng Wang, Jie Gao, Jie Wang, Jiewei Wu, Jin Yang, Jinjin Li, Jinjing Huang, Jinquan Sun, Jinyao Chen, Juanhui Tu, Jun Liu, Jun Mei, Jun Xu, Jun Zhou, Junjie Ou, Junnan Sipan, Junpeng Fang, Kaihong Zhang, Kaiqin Hu, Ke Shi, Kuan Xu, Kun Tang, Kunlong Chen, Lanyin Mei, Lei Chen, Lei Liang, Lei Xu, Li Tang, Liang Jiang, Liangcheng Fu, Lihui Zhang, Linfeng Shi, Lintao Ma, Liyuan Liu, Longfei Li, Longfei Zheng, Lu Liu, Lu Yu, Man Li, Meiqi Zhu, Meng Li, Mengjie Gao, Mengshu Sun, Mingming Yin, Mingyang Zhang, Mingyuan Fan, Nuo Xu, Pan Tang, Peijie Jiang, Peilong Zhao, Peng Lin, Pingping Liu, Qi Zuo, Qian Zhao, Qiang Cheng, Qianggang Cao, Qiaoben Bao, Qing Cui, Qingyuan Yang, Qitao Shi, Qiyin Huang, Qizheng Zhou, Quan Wan, Runyuan Zhao, Shaomian Zheng, Shaowei Wei, Shengnan Zhang, Shuaicheng Li, Shujie Li, Shuo Zhang, Sikang Bian, Tianchu Yao, Tiange Xu, Tianshu Wang, Ting Guo, Tinghao Wang, Tingwei Huang, Tong Zhao, Tongkai Yang, Wang Hong, Wanli Gu, Wei Lu, Weichang Wu, Weiguang Han, Weiquan Li, Wenbo Shen, Wenjing Fang, Wenzhi Tang, Xiang Shu, Xiao Shi, Xiaodong Yan, Xiaolu Zhang, Xiaopei Wan, Xiaqing Sun, Xin Zhao, Xingyu Lu, Xinxing Yang, Xinyao Tang, Xinyu Kong, Xinyu Liu, Xiong Xu, Xuan Sun, Xudong Han, Xudong Wang, Xujie Shen, Yalin Zhang, Yangyang Hou, Yankun Ren, Yao Zhao, Ye Chen, Yeyang Chen, Yibo Cao, Yifan Zuo, Yijie Chen, Ying Li, Yingjie Song, Yingxue Li, Yiqi Wang, Yixuan Sun, Yizhu Xiao, Yongfei Xu, Yu Liu, Yuchen Fang, Yue Gao, Yue Yu, Yue Zhang, Yuqi Zhang, Yuxiao He, Yuxiao Lu, Yuxin Tian, Yuxuan Li, Yuzhuo Fu, Zhankai Xu, Zhaoxin Huan, Zhenduo Zhang, Zhengke Gui, Zhengyu Huang, Zhenjun Ma, Zhenxuan Pan, Zheping Qu, Zhibo Zhu, Zhidong Fan, Zhigang Huangfu, Zhihao Wang, Zhiqiang Zhang, Zhizhen Liu, Zhuyan Zhou, Zibin Lin, Zihang Zeng, Zihao Wang, Zilong Wang, Ziqi Liu, Zitao Xuan, Zixuan Cheng, Zujie Wen, Zuoli Tang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces KPop RL framework for agentic LLM training and shortest-correct-response distillation, directly advancing RL-for-LLMs and on-policy distillation.

**摘要**: arXiv：2606.15079v1宣布类型：新摘要：高效且可扩展的代理智能需要能够提供低延迟响应和强大推理能力的模型，同时保持训练、服务和部署的实用性。在本报告中，我们介绍了Ling-2.6和Ring-2.6，这是一系列型号，旨在大规模应对这一挑战。Ling-2.6针对即时响应生成和每个输出令牌的高性能进行了优化，而Ring-2.6则针对更深入的推理和更高级的代理工作流程量身定制。我们不是从头开始训练，而是通过架构迁移预训练和大规模后期训练来升级Ling-2.0基础模型。此次升级以模型架构、优化目标、服务系统和代理培训环境的统一协同设计为指导，实现模型能力和部署效率的提高。在架构层面，我们引入了混合线性注意力设计，将Lightning Attention与MLA集成在一起，提高了长上下文训练和解码的效率。为了进一步提高代币效率，我们通过进化思想链、语言单元策略优化、双向偏好对齐和最短正确响应蒸馏来优化每个输出代币的能力。对于代理能力，我们提出了KPop，这是一个强化学习框架，旨在支持在大规模环境数据上稳定训练Ring-2.6- 1 T。KPop通过编码、搜索、工具使用和工作流程执行之间的同步调度来提高培训效率，从而实现从复杂的代理与环境交互中进行可扩展学习。Ling-2.6和Ring-2.6共同提供了通往高效、可扩展和开放的代理系统的实用途径。我们开源了2.6系列中的所有检查点，以支持实用代理智能的进一步研究和开发。

[阅读原文](https://arxiv.org/abs/2606.15079)

---

## 19. 从稀疏剧集结局中对VLA进行在线RL微调的分层优势加权

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Tongyan Fang, Siyuan Huang, Naiyu Fang, Ganlong Zhao, Zhongjin Luo, Jianbo Liu, Xiaogang Wang, Ying Dong, Hongsheng Li

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a hierarchical advantage-weighting method for online RL fine-tuning of VLAs from sparse binary outcomes, introducing separate critic heads for viability and efficiency with a state-adaptive gate.

**摘要**: arXiv：2606.17043v1宣布类型：新摘要：当通过在线RL微调预训练的VLA策略时，每个推出剧集只产生一个二元结果（成功或失败），但参与者更新需要每次转换的监督。现有的方法通常将这种稀疏的结果简化为单一的纯量奖励或优势信号，这将不同形式的过渡级反馈混为一谈，并在基本任务成功实现后提供有限的指导。首先，单个纯量信号将生存能力和效率这两个目标混为一谈;一旦实现基本成功，二进制标签就不会提供任何梯度来区分高效完成和缓慢完成。其次，现实世界的推出混合了自主和干预部分;天真地跨越这些界限分配事件结果会导致不正确的信用分配。为了解决这些问题，我们提出了分层加权行为克隆（HABC），它在不同的数据子集上针对这两个目标训练不同的评论家头，并将他们的输出与状态自适应平衡相结合。状态自适应门$g_t$融合了它们的一步优势，在成功不确定时优先考虑可行性，只有在可行性高时才转向效率，并将结果转换为每一次转换对演员损失的权重。干预意识的信用分配进一步将结果标签限制在当前政策执行的部门，防止监督跨越干预界限泄露。在三项接触丰富的双手任务的真实机器人实验中，HABC将监督微调（SFT）基线的成功率从36%、44%和12%提高到92%、88%和38%。

[阅读原文](https://arxiv.org/abs/2606.17043)

---

## 20. SHARD：通过自我重组蒸馏实现安全且有益的对齐

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Viswonathan Manoranjan, Amogh Gupta, Anvesh Rao Vijjini, Thomas Hofweber, Snigdha Chaturvedi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes SHARD, a self-reframing distillation method that uses the model's own on-policy outputs to improve safe-helpfulness alignment, directly matching on-policy distillation criteria.

**摘要**: arXiv：2606.15517v1宣布类型：新摘要：大型语言模型经常难以应对敏感提示。他们可能会彻底拒绝、提供通用安全样板，或者未能满足用户可以安全回答的合法信息需求。我们引入SHARD，这是一种自重构蒸馏方法，以提高安全性。它首先使用哲学准则重写敏感提示，以表达善意意图，然后将其原始反应重新构建为安全、更有帮助的反应，最后根据其自我重构的反应对模型进行微调。在DNA和LINGUASAFE的英语子集中，SHARD在保持安全性的同时为大多数模范家庭提供了帮助。它也仍然具有竞争力的蒸馏从一个更大的教师模型，这表明模型可以内化安全和有益的行为从自己的。警告：本文包含可能令人反感或有害的内容。

[阅读原文](https://arxiv.org/abs/2606.15517)

---

## 21. ExpRL：LLM中期培训的探索性RL

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Violet Xiang, Amrith Setlur, Chase Blagden, Nick Haber, Aviral Kumar

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ExpRL, an RL-based mid-training method that uses reference solutions as reward scaffolds to provide dense rewards for on-policy reasoning traces, improving LLM reasoning priming.

**摘要**: arXiv：2606.17024v1宣布类型：新摘要：稀疏奖励强化学习（RL）已成为改进LLM推理的标准工具，但其成功关键取决于基本模型中存在的覆盖范围。在实践中，模型通常通过\{mid-train}在精心策划的推理痕迹上为RL做好准备，这些痕迹教授有用的原始技能，例如分解、验证或自我纠正。尽管有效，但该策略需要手动指定模型应该学习什么，而且目前尚不清楚这种原始覆盖是否足以应对更困难的问题，这需要将这些技能结合到更广泛的解决方案策略中。我们研究了一种更加自动化的方法：\{基于RL的中间训练}使用大量人工编写的问答数据库。而不是把参考解决方案作为模仿的目标，我们的方法，ExpRL，使用它们作为奖励脚手架：参考是隐藏的政策，只用于构建特定于问题的评分规则，用于判断对政策的推理痕迹。策略从原始问题提示中采样，而LLM法官将采样的推理轨迹与参考解决方案进行比较，并分配结果级别或过程级别的密集奖励。这使得ExpRL能够强化部分进展、有用的中间缩减和富有成效的推理行为，而稀疏的最终答案奖励往往无法增加这些行为的权重。在具有挑战性的数学推理任务中，ExpRL产生比SFT，稀疏奖励GRPO和自蒸馏更强的RL启动，并为后续的稀疏奖励RL提供更好的初始化。其他混合域实验进一步表明，ExpRL可以扩展到最初的纯数学设置之外。

[阅读原文](https://arxiv.org/abs/2606.17024)

---

## 22. BATO：缓解幻觉的平衡代币级政策优化

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ning Li, Zixuan Guo, Yan Xu, Wenbo Fei, Yifan Niu, Chang Luo, Yasheng Wang, Weiwen Liu, Yong Yu, Weinan Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes BALTO, a balanced token-level RL policy optimization framework for hallucination mitigation with theoretical advantages in credit assignment.

**摘要**: arXiv：2606.15893v1宣布类型：新摘要：幻觉仍然是在知识密集型环境中部署大型语言模型（LLM）的主要障碍，在知识密集型环境中，生成的响应必须忠实地基于所提供的证据。强化学习（RL）是缓解幻觉的一个有前途的方向，但响应级别的忠实性奖励存在粒度不匹配的问题：局部幻觉可能会导致支持的内容受到虚假惩罚。尽管最近的工作引入了细粒度的反馈，例如声明级验证和代币级奖励，但不平衡的信用分配仍然会导致长度、冗长或优化噪音偏差。我们提出了一个用于缓解幻觉的平衡代币级政策优化框架--BALU。BATO提取可检查的事实主张，根据参考上下文验证它们，并将主张级别的判断投射到标记级别的标签。该框架中引入了平衡的代币级信用分配机制。这种设计将概率质量从不支持的内容重新分配到忠实的内容，而不是抑制整个响应。我们从理论的角度系统分析了响应水平奖励的局限性，证明了balTO在幻觉缓解训练稳定性和优化效率方面的优势。ConFiQA、RAGTruth和FinLLM-Eval上的实验表明，HARTO在所有六个模型（基准设置）中实现了最高的忠实度，并且在Q-Score方面始终优于现有的训练后基线，表现出更强的忠实度--信息性权衡。

[阅读原文](https://arxiv.org/abs/2606.15893)

---

## 23. PathRouter：统计图检索增强生成中的奖励与检索质量保持一致

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Bo Wang, Heyan Huang, Yaolin Li, Wei Tang, Yuan Zhang, Wenbo Li, Mingze Gao, Ge Shi, Chong Feng

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes PathRouter, a path-aware RL training framework for agentic GraphRAG that addresses reward aliasing and search-update ambiguity via differentiated GRPO advantage scaling and token-level KL guidance.

**摘要**: arXiv：2606.16409v1宣布类型：新摘要：统计学GraphRAG训练语言模型代理迭代检索和推理图结构证据，通过有效导航复杂的信息网络来实现更准确和上下文感知的决策。然而，纯结果强化学习受到\textit{\textBF{answer-路径奖励别名}}的影响，其中正确的答案可能来自捷径，而不是有用的证据路径。它还表现出\texttit {\textbf{search-update ambiguity}}，因为标量冗余级反馈并不指示要调整哪些检索操作。为了减轻这些缺点，我们提出了PathRouter，一个代理GraphRAG的路径感知训练框架。PathRouter沿着答案正确性和证据路径重叠联合评估每个轨迹，产生四个轨迹类别，具有差异化的GRPO优势缩放，抑制捷径强化，同时保留证据寻求行为。对于证据不足的轨迹，冻结的黄金证据教师提供了关于推理和搜索查询令牌的令牌级KL指导，排除答案令牌以避免直接响应模仿。针对三种模型尺寸的六个QA基准进行的实验表明，PathRouter持续改善了答案F1和证据路径重叠，与强基线相比，在3B模型上实现了3.1的平均F1收益，在7 B模型上实现了4.9的平均F1收益。

[阅读原文](https://arxiv.org/abs/2606.16409)

---

## 24. CoRA：可靠的思想链推理的信心与理由一致

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Juming Xiong, Weixin Liu, Kevin Guo, Congning Ni, Junchao Zhu, Chongyu Qu, Chao Yan, Katherine Brown, Avinash Baidya, Xiang Gao, Bradley Malin, Zhijun Yin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a GRPO-based RL framework that jointly rewards answer correctness and rationale support, directly improving confidence-rationale alignment for CoT reasoning.

**摘要**: arXiv：2606.14961v1宣布类型：新摘要：思想链（CoT）推理可以提高LLM绩效，但当伴随的CoT原理看似合理但不完整或支持不足时，高答案置信度可能会产生误导。我们研究信心--理由对齐：模型对其承诺答案的信心是否通过其生成的理由来证明。我们引入了一个基于GRPO的强化学习框架，该框架联合奖励答案正确性、承诺答案概率和基于标题的理由支持，其中标题评估基础、一致性、任务匹配以及与所选答案的联系，而不会向法官透露黄金答案。在MedQA、MathQA和OpenBookQA中，使用三种开重度LLM，与未调优检查点、SFT和仅正确性GRPO相比，我们的方法将置信度-理由对齐误差降低了高达26.51%，同时保持有竞争力的准确性并经常改进校准。这些结果表明，可靠的CoT推理不仅需要自信的答案，还需要实质性支持这些答案的理由。

[阅读原文](https://arxiv.org/abs/2606.14961)

---

## 25. PACT：针对多回转刀具使用代理的授权跟踪联合培训

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zhenbang Du, Jun Luo, Zhiwei Zheng, Xiangchi Yuan, Kejing Xia, Dachuan Shi, Qirui Jin, Qijia He, Shaofeng Zou, Yingbin Liang, Wenke Lee

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a privileged trace co-training framework combining trace-conditioned RL and component-aware SFT for multi-turn tool-use agents, directly addressing on-policy distillation and RL for LLMs.

**摘要**: arXiv：2606.16215v1宣布类型：新摘要：多回合工具使用代理必须推理、调用工具并适应多个交互回合的观察。对此类代理进行后训练具有挑战性，因为尽管与仅预算的推理设置相匹配，强化学习通常会受到稀疏奖励和弱信用分配的影响，而对专家痕迹的监督微调提供了密集的流程监督，但可能会过度限制模型到固定轨迹。为了解决这个问题，我们提出了PACT，这是一个用于多回合工具使用代理的扩展trAce Co-Training框架。关键想法是仅使用专家跟踪作为训练时优化信号，而不是推出时提示。PACT保持部署生成仅限预算，然后使用专家轨迹通过两个补充信号来指导优化：一个跟踪条件RL代理，用于在专家轨迹上下文下评估仅限预算部署，以及一个组件感知的SFT损失，用于监督推理前置和具有强化强度的工具调用。为了减少对仅训练跟踪上下文的过度依赖，PACT进一步引入了仅预算锚定。我们还提供了一个潜在跟踪视图，该视图连接了两个基于跟踪的目标，并解释了专家跟踪如何在不使用的情况下指导优化。FTRL、BFCL和Tools Hop的实验表明，PACT相对于基于SFT和RL的强基线持续改进，凸显了特权轨迹联合训练对于多回合工具使用学习的价值。

[阅读原文](https://arxiv.org/abs/2606.16215)

---

## 26. 用于统计和多模式LLM的上下文感知RL

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Peiyang Xu, Bangzheng Li, Sijia Liu, Karthik R. Narasimhan, Pramod Viswanath, Prateek Mittal, Xingyu Fu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes ContextRL, a novel context-aware RL objective for LLMs that rewards context selection over final answer, showing gains on long-horizon and multimodal tasks.

**摘要**: arXiv：2606.17053v1宣布类型：新摘要：当回答需要在漫长或复杂的上下文中识别一个小但决定性的证据（例如工具痕迹中的一行或图像中的微妙细节）时，大型语言模型（LLM）通常会失败。我们提出ContextRL，这是一种上下文感知强化学习（RL）方法，通过\r {间接}辅助目标提高长视野推理和多模式性能。ContextRL不是只监督最终答案，而是向模型呈现一个查询、一个答案和两个高度相似的上下文，并奖励它选择支持查询-答案对的上下文，从而鼓励细粒度的基础。我们在两个领域中构建对比上下文数据：对于编码代理，轨迹作为上下文，产生通过条件过滤构建的1 k对;对于多模式推理，图像作为上下文，产生通过生成式编辑和相似性搜索构建的7 k对。ContextRL在5个长期基准上比标准GRPO平均提高+2.2%，在12个不同的视觉问答基准上平均提高+1.8%。为了区分拟议目标的影响与额外数据的影响，我们与数据增强基线进行了比较，这些基线将相同的对比上下文重新用作标准查询-上下文-答案示例。这些基线几乎没有提供任何改进，这表明收益来自拟议的上下文选择目标，而不仅仅来自对比数据。

[阅读原文](https://arxiv.org/abs/2606.17053)

---

## 27. LLM政策优化的第一原理推导：从预期回报到GRPO及其结构扩展

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Jianghan Shen, Siqi Luo, Yue Li, Jiyao Liu, Wanying Qu, Yi Zhang, Ziyan Huang, Tianbin Li, Ming Hu, Xiaohong Liu, Yirong Chen, Junjun He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a unified first-principles derivation of LLM policy optimization methods (REINFORCE to GRPO) using trajectory and reward axes, offering a diagnostic framework for designing next-generation algorithms.

**摘要**: arXiv：2606.16733v1公告类型：新摘要：语言模型的策略梯度算法优化了相同的目标$J（\theta）= \mathbb{E}*{\tau \sim p*\theta（\tau）}[R（\tau）]$，它有两个因素：轨迹概率$p_\theta（\tau）$和奖励$R（\tau）$。从REINFORCE到PPO再到GRPO的每一种方法及其后代都修改一个或两个因子，以解决前面公式中的特定故障。现有的调查按领域或时间顺序组织这些方法，这掩盖了每个设计选择背后的理由及其干预在梯度估计器中的精确位置。这项调查根据第一原则从$J（\theta）$重新审视了LLM政策优化的格局，并使用由$p_\theta（\tau）$诱导的轨迹侧和由$R（\tau）$诱导的回报侧作为方法所在的两个轴。它涵盖了从REINFORCE和PPO到GRPO的路径，以及后GRPO变体、扩展RL和GRPO-OPD。由此产生的框架是统一的、诊断性的和可扩展的：它分析来自共享目标的方法，识别每个方法修改哪一边以及为什么修改，并在这些设置中应用相同的轨迹和奖励轴。在这些设置中，该框架还暴露了单边修复无法解决的复合故障，因此需要对轨迹侧和回报侧进行联合设计。此地图识别的边界情况和耦合故障标记了现有解决方案的耗尽位置，并为设计下一代LLM策略优化算法提供了原则性的起点。

[阅读原文](https://arxiv.org/abs/2606.16733)

---

## 28. RL VR稳定性和赢家优势政策优化的梯度视角

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Prasanth YSS, Zhichen Ren, Rasa Hosseinzadeh, Ilan Gofman, Yuqi Chen, Zhaoyan Liu, Guangwei Yu, Jesse C. Cresswell, Satya Krishna Gorti

**机构**: Layer6 AI Labs

**💡 亮点 (Highlight)**: Proposes WAPO, a new online clipped policy-gradient objective for RLVR that improves training stability by updating only on positive-advantage completions, directly addressing a core RL-for-LLMs stability problem.

**摘要**: arXiv：2606.16154v1宣布类型：新摘要：带可验证奖励的强化学习（WLVR）改进了语言模型推理，但GRPO式优化仍然容易崩溃。我们通过代币级别的梯度动态来分析这种不稳定性，从而推导出一个分类法，该分类法预测更新如何影响下一个代币概率和熵。分类法表明，稳定性共同取决于当前政策下的优势标志和代币分配。受这一发现的启发，我们提出了赢家优势政策优化（WAPO），这是一个简单的在线剪裁政策梯度目标，仅在正优势完成时更新。在数学推理和多跳QA基准中，WAPO提高了训练稳定性，并匹配或优于多个模型系列的基线。完整代码可在https://github.com/layer6ai-labs/wapo上找到。

[阅读原文](https://arxiv.org/abs/2606.16154)

---

## 29. EIBunch：基于模拟器的情感管理基准和转折信用RL

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Rongzhi Zhu, Xiang Huang, Yuchuan Wu, Rui Wang, Zequn Sun, Tao Ren, Weiyao Luo, Bingxue Qiu, Jieping Ye, Yongbin Li, Wei Hu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes CTC-GRPO, a novel RL method using simulator-based dense turn-level rewards for multi-turn emotion management in LLMs, directly improving LLM behavior via RL.

**摘要**: arXiv：2606.15532v1宣布类型：新摘要：大型语言模型（LLM）中的情商（EI）通常通过静态理解任务或单响应对话生成来评估。然而，情感管理是互动的：一个好的模型不仅应该识别用户的情感，还应该通过几个回合改善用户的情感和关系状态。我们引入EIBunch，这是一个基于模拟器的交互式情感管理基准。EIBunch包含2，222个场景，其中2，009个用于培训，213个用于进行测试。这些场景按照2x 2分类法组织，涵盖支持、防御、修复和魅力，它们共同捕获不同形式的支持、边界维护、信任修复和融洽关系建立。在每个场景中，LLM模拟器都会扮演用户，在每次转身后更新情感关系状态，并将最终状态映射到基于主播的分数。这种设计使EIBench既是评估基准又是训练环境：最终状态提供结果奖励，而每次回合的状态更新为RL提供密集的反馈。我们评估了15个开源和闭源LLM。当前的模型在支持和建立融洽关系的场景中表现良好，但在用户压力下难以维持边界。为了提高LLM的EI能力，我们提出了集中回合信用GRPO（CTC-GRPO），这是一种GRPO扩展，可以重用模拟器的每回合状态更新作为密集回合级反馈，同时保留最终结果奖励。CTC-GRPO将EIBench上的Qwen 3 -8B从-22.4提高到+22.4，并改善了包括SAGE（+12.4）和EQBench 3（+20.9%）在内的分布外评估。我们的研究结果表明，模拟器跟踪的用户状态可以支持多轮情绪管理的评估和培训。

[阅读原文](https://arxiv.org/abs/2606.15532)

---

## 30. 自适应和显式安全：触发大型推理模型中潜在的安全意识

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Ke Miao, Jiaxin Li, Hongliang Chen, Yuke Hu, Zhan Qin

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a novel safety alignment method for LRMs that uses SFT and DPO with entirely self-generated data, leveraging latent safety awareness and on-policy self-improvement.

**摘要**: arXiv：2606.16808v1宣布类型：新摘要：虽然大型推理模型（LRM）擅长复杂任务，但它们仍然极易受到复杂越狱和直接有害查询的影响。为了解决此漏洞，之前的工作严重依赖外部手动数据注释来进行安全对齐。然而，我们观察到，当重新呈现原始查询以及它们自己的推理轨迹时，LRM本质上可以识别安全风险--我们将这种能力称为“潜在安全意识”。为了利用这种安全意识，我们首先采用监督微调（SFT）来显式地诱导安全标签来触发安全分析和指导，遵循不安全查询的初始推理内容，同时保留一般查询的标准响应，以确保自适应触发。随后，我们应用直接偏好优化（DPO）进一步增强安全分析和指导的正确性和稳定性。值得注意的是，两个训练阶段所需的响应完全由正在优化的模型生成。使用（安全触发）SFT和DPO，实验结果表明安全性显着增强。例如，DeepSeek-R1-Distill-Lama-8B的攻击成功率（ASB）在有害和越狱基准上平均分别下降24.65%和36.72%。最后，我们的安全触发方法几乎不会对总体性能或用户体验产生负面影响。

[阅读原文](https://arxiv.org/abs/2606.16808)

---

## 31. AdaMame：自适应多语言推理的训练食谱

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Dayeon Ki, Kevin Duh, Marine Carpuat

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Introduces AdaMame-GRPO, a two-stage SFT+RL recipe with a query-conditioned alignment factor for multilingual reasoning, directly advancing RL for LLMs with a novel reward design.

**摘要**: arXiv：2606.15080v1公告类型：新摘要：虽然大型推理模型（LRM）在英语中表现出很强的性能，但它们通常无法用查询的语言进行推理，这种现象被称为语言崩溃。现有的基于RL的修复通常会在准确性目标上增加二进制语言保真度奖励，但仍然会在准确性、中间跟踪代码切换和过度令牌使用方面产生权衡。在这项工作中，我们提出了AdaMame，这是一种用于多语言数学推理的两阶段训练食谱，它通过自适应地将推理语言与查询语言对齐而不影响准确性来解决这些限制。第一个SFT阶段对五种语言中自然发生的推理轨迹进行微调，以建立多语言推理能力。在随后的RL阶段，我们引入AdaMame-GRPO，这是组相对策略优化（GRPO）的改编，其中查询条件对齐因子在训练期间逐渐增长，引导模型在利用查询语言中的推理之前首先探索不同的推理语言。AdaMame-GRPO经过两个基准测试、两个LRM和12种语言的评估，在所有基线上的推理准确性、语言保真度和令牌效率方面实现了帕累托最优性能，在域外、资源较少的语言上获得了最大的收益。

[阅读原文](https://arxiv.org/abs/2606.15080)

---

## 32. 训练后如何简化生物推理模型

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Lukas Fesser, Hanlin Zhang, Michelle M. Li, Eric Wang, Bryan Perozzi, Shekoofeh Azizi, Sham M. Kakade, Marinka Zitnik

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Provides a controlled study of how RL post-training shapes biological reasoning models, showing RL on strong SFT checkpoints improves OOD generalization, directly relevant to RL for LLMs.

**摘要**: arXiv：2606.16517v1宣布类型：新摘要：生物学的科学推理模型将语言模型与基于DNA、RNA和蛋白质等多模式生物数据训练的基础模型相结合。这些模型是通过后训练构建的，但每个阶段如何塑造推理和概括仍然知之甚少。我们研究后培训何时提高绩效以及何时导致过度专业化。在基因组学、转录组学和蛋白质领域，我们在主干受控变异、持续预训练（CPD）、监督微调（SFT）和强化学习（RL）下训练和评估了100多个生物推理模型，测量域内（ID）和域外（OOD）性能。我们发现，每个训练后阶段都以不同的方式重塑了概括性，而不是贡献统一的收益。CPD通过将模型与生物语言保持一致来提高下游性能。SFT持续提高ID性能，但导致OOD性能提前达到峰值，并随着模型适合训练分布而下降。当RL应用于具有一致奖励的强SFT检查点时，可以提高OOD性能并部分恢复概括性。这些结果表明，生物推理不会随着额外的监督或计算而单调地改善。相反，表现取决于训练阶段的组成方式。在固定的训练后预算下，最强的ID-OOD权衡来自简短的SFT、更大的RL分配和跨阶段的不对称适应能力。

[阅读原文](https://arxiv.org/abs/2606.16517)

---

## 33. 语言模型代理中的奖励黑客：重新审视人工智能安全网格世界

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: \"Omer Veysel \c{C}a\u{g}atan, Xuandong Zhao

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Directly studies reward hacking in LLM agents via RL, showing that direct reward optimization widens the gap between observed and hidden reward, which is a central contribution to RL-for-LLMs safety.

**摘要**: arXiv：2606.15385v1宣布类型：新摘要：奖励黑客攻击（人工智能系统利用错误指定的目标来实现高奖励而不满足预期目标）仍然是人工智能安全的核心挑战。然而，大多数已知的例子都是在前沿系统中事后发现的，在这些系统中，控制研究是不切实际的。我们将人工智能安全Gridworlds框架调整为基于文本的评估套件，该套件为基于语言的代理重新制定了经典强化学习安全任务。在各个前沿和中型模型中，我们发现规范游戏出现了零射击：模型系统性地实现了高观察回报，但在隐藏的安全目标方面表现不佳，即使是表面上安全的行为也可能反映误解而不是有原则的安全性。强化学习并不能纠正这些失败：直接奖励优化扩大了观察到的奖励和隐藏的奖励之间的差距，因为模型的初始能力导致它在发现更安全的替代方案之前锁定本地奖励策略。这种模式在模型尺度（1.5B--14B）中持续存在，并且无法通过更细的信用分配、探索提示或熵正规化来解决。我们的结果表明，当使用有能力的语言模型代理优化代理目标时，奖励黑客攻击会自然发生，并且抵制标准缓解措施，这表明代理环境中的代理奖励失败可能需要超出标准探索和信用分配修复的方法。为了促进重现性，这项工作的代码可在\href{https：//github.com/guardius/verl-agent-safety}{我们的公共存储库}上获取。

[阅读原文](https://arxiv.org/abs/2606.15385)

---

## 34. 针对多回合代理人的政策提炼和课程回合级指导

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Gengsheng Li, Mao Zheng, Mingyang Song, Ruiqi Liu, Tianyu Yang, Jie Sun, Qiyong Zhong, Haiyun Guo, Junfeng Fang, Dan Zhang, Jinqiao Wang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes Guided-OPD, a curriculum-based on-policy distillation algorithm that mixes teacher and student turns to mitigate compounding errors in multi-turn agent tasks.

**摘要**: arXiv：2606.15912v1宣布类型：新摘要：规划、调用工具并与环境交互的多轮代理为解决复杂任务提供了一个有希望的范式，但它们的能力通常依赖于非常大的模型，这些模型的推理成本在实践中是令人望而却步的。按策略蒸馏（OPD）是将此类能力转移到较小的学生的自然秘诀，但我们发现它在这种环境下遭受了典型的失败模式：学生的小错误会在转弯时复合，并将轨迹推离教师熟悉的状态分布，因此教师的监督在学生最需要的地方变得最不可靠。我们建议指导性的政策蒸馏（指南-OPD），一种简单而有效的算法，混合了教师和学生在每次推出中生成轮数，并根据课程安排教师的干预可能性，使其衰减为零。强有力的指导保持早期轨迹接近教师分布，然后逐渐撤回，以恢复推理时使用的纯粹政策制度。在ALFWorld、ScienceWorld和WebShop上，从Qwen 3 - 30 B-A3 B教师中提取Qwen 3学生，Guided-OPD平均比香草OPD提高了21.1%，成功率提高了25.5%，较小的学生获得了更大的收益。

[阅读原文](https://arxiv.org/abs/2606.15912)

---

## 35. 重播重要的事情：政策外重播，以实现高效的LLM强化取消学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Zirui Pang, Chenlong Zhang, Haosheng Tan, Zhuoran Jin, Jiaheng Wei, Zixin Zhong

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an off-policy replay buffer for RL-based LLM unlearning, directly improving hard-case convergence and retain quality via importance-sampled reuse of low-reward rollouts.

**摘要**: arXiv：2606.15333v1宣布类型：新摘要：LLM取消学习已成为完全再培训的一种具有成本效益的替代方案，可以从预训练模型中删除危险知识，同时保留通用性。最近的基于RL的方法（例如RULE）将取消学习重新定义为学习拒绝行为，但它们的策略优化在整个训练过程中重复从相同的忘记和保留/边界提示中采样。我们在这个过程中发现了一个关键的低效率：简单的情况会迅速收敛，几乎没有提供有用的梯度信号，而接近忘记/保留边界的困难情况会继续产生低回报推出，并在一次使用后被丢弃。为了解决这个问题，我们提出了ReRULE，这是一种用于强化取消学习的非策略重播增强。ReRULE在早期GRPO训练期间将低回报硬案例推出组存储在重播缓冲区中，并在后期通过重要性抽样的非策略更新重新使用它们，将计算重定向到仍然需要学习的边界案例。从理论上讲，我们表明ReRULE比纯粹的政策规则产生更严格的硬情况收敛界限。从经验上看，ReRULE将MusE-Books保留质量从46.3提高到56.2，同时在基准测试中仅增加5- 11%的培训时间。它对更简单的TOFU设置的有限改进进一步支持了预期的条件行为：当硬/易差异明显时，重播是最有益的。

[阅读原文](https://arxiv.org/abs/2606.15333)

---

## 36. LLM中协调语义和协作：基于推理的顺序推荐嵌入生成器

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Qidong Liu, Mingyao Huang, Moranxin Wang, Wenxuan Yang, Haiping Zhu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a latent reasoning-enhanced contrastive learning stage and a collaborative reward RL stage for LLM-based sequential recommendation embedding generation.

**摘要**: arXiv：2606.16703v1宣布类型：新摘要：顺序推荐系统（RS）根据用户的交互历史预测下一个感兴趣的项目，并已被广泛部署，但受到长尾问题的阻碍。大型语言模型（LLM）具有强大的语义理解和推理能力，为丰富项语义提供了一种有希望的方法，最近已被用作嵌入生成器。然而，仍然存在两个根本差距。首先，当前基于LLM的嵌入方法未能利用模型的内部推理能力。其次，现有的方法往往通过监督微调隐式地注入协作信号，缺乏对协作嵌入对齐的明确指导。在本文中，我们介绍了ReaEmb，这是一个新的框架，通过潜在推理增强对比学习（LRCL）阶段和协作奖励强化学习（CRRL）阶段解决了这两个问题。LRCL通过带有额外注意力模块的两遍向前过程来利用LLM的内部推理能力。CRRL随后通过定制的强化学习将协作信号明确地注入LLM。对三个现实世界数据集的广泛实验证明了ReaEmb在多个RS模型中的卓越有效性。为了简化可重复性，我们在线发布代码。

[阅读原文](https://arxiv.org/abs/2606.16703)

---

## 37. GD $' 2$PO：通过群体动态奖励脱钩政策优化缓解多重奖励冲突

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Haotian Liu, Yihao Liu, Jingwei Ni, Siyuan Huang, Xinpeng Liu, Pengyu Cheng, Jiajun Song, Ruijin Ding, Junfeng Li, Zhechao Yu, Mengyu Zhou, Hongteng Xu, Xiaoxi Jiang, Guanjun Jiang

**机构**: Alibaba Group (Qwen team)

**💡 亮点 (Highlight)**: Proposes a new RL method (GD^2PO) with a conflict-aware filtering mechanism to mitigate multi-reward conflicts in multi-dimensional RL for LLMs, directly advancing RL-for-LLMs.

**摘要**: arXiv：2606.16771v1宣布类型：新摘要：随着LLM的发展，训练后强化学习（RL）越来越依赖多维奖励来培养综合能力。这一转变需要能够同时优化多样化且潜在竞争目标的新算法。为了解决这个问题，现有方法（例如团体奖励-脱钩政策优化（GDPO））将总体得分分解到独立的奖励组中，然后在每个组中分别计算RL损失。然而，该策略仍然会遇到多重奖励冲突：单一的推出可以在某些奖励维度上产生积极的优势，但在其他方面产生消极的优势，导致相反的信号在聚合过程中相互抵消，进一步阻碍RL训练效率。受动态sAmpling Policy优化（DAPO）（通过过滤具有接近零优势的无效部署来提高RL训练效率）的启发，我们提出了群体动态奖励-脱钩政策优化（GD $' 2$PO）。具体来说，GD $' 2$PO采用冲突感知过滤机制来掩盖存在严重奖励分歧的推出。通过防止冲突信号相互抵消，这种掩蔽策略保留并增强了有效RL优势的幅度，从而显着加快学习效率。此外，我们引入查询级重新加权，根据每个查询的总体奖励共识动态调整其更新强度。对各种多重奖励场景（包括工具调用和人类偏好一致）的实验表明，GD $' 2$PO始终且显着优于现有基线。该代码可在https://github.com/Qwen-Applications/GD2PO上获取。

[阅读原文](https://arxiv.org/abs/2606.16771)

---

## 38. VibeThinker-3B：探索小语言模型中可验证推理的前沿

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Sen Xu, Shixi Liu, Wei Wang, Jixin Min, Yingwei Dai, Zhibin Yin, Yirong Chen, Xin Zhou, Junlin Zhang

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Explores verifiable reasoning in small LLMs via a pipeline including multi-domain RL and offline self-distillation, directly relevant to RL-for-LLMs and on-policy distillation.

**摘要**: arXiv：2606.16140v1宣布类型：新摘要：本技术报告介绍了VibeThinker-3B，这是一个具有3B参数的紧凑密集模型，旨在研究在严格的小模型范围内可以将可验证推理推进到何种程度。我们以Spectrum-to-Signal后训练范式为基础，通过优化的管道系统性地增强模型，其中包括基于尤利西斯的监督微调、多域强化学习和离线自蒸馏。实验评估表明，VibeThinker-3B在要求极高的可验证任务上实现了前沿级性能。具体来说，它在AIME 26上获得了94.3分（通过索赔级别测试时间缩放提高到97.1分），在LiveCodeBench v6上获得了80.2 Pass@1，并且在最近未公开的LeetCode比赛中表现出了很强的分布外概括性，接受率为96.1%。这实际上使其进入了一级推理系统的性能范围，与DeepSeek V3.2、GLM-5和Gemini 3 Pro等大几个数量级的旗舰型号相匹配或超过。此外，IFEval的93.4分证实了这种极端推理增强不会损害严格的指令可控性。这些发现扩展了我们之前的1.5B工作，激发了参数压缩-覆盖假说，该假说认为可验证推理可以压缩到紧凑推理核心中，而开放领域知识和通用能力需要对事实、概念和长尾场景进行广泛的参数覆盖。这一观点表明，紧凑型模型不仅是部署效率的替代品，而且是在参数密集的能力机制中实现前沿级性能的补充途径。

[阅读原文](https://arxiv.org/abs/2606.16140)

---

## 39. 交互器：赞助搜索中广告描述生成的面向大型RL的迭代创建

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Penghui Wei, Jiayu Wu, Chao Ye, Zhi Guo, Shuanglong Li, Lin Liu

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes an agentic RL framework with iterative refinement using generative reward models for ad description generation, directly matching RL-for-LLMs with a new reward design and training loop.

**摘要**: arXiv：2606.15911v1公告类型：新摘要：本文重点关注在赞助搜索中自动生成信息性广告描述。与通常经过优化以吸引用户点击反馈的广告标题不同，广告描述具有更长的文本跨度，并且具有融合世界知识来解决用户搜索意图的潜力，同时呈现广告的细粒度卖点。我们提出了Interactor，这是一个通过代理RL优化的多回合迭代创建框架，用于广告描述生成。生成模型充当与由多个生成奖励模型组成的定制环境交互的策略。根据政策赋予最初的几代人，定制的GenRM评估多维质量，包括知识能力和着陆页一致性，同时提供二进制信号和推理反馈。然后，该政策根据此类反馈迭代地完善描述，以确保持续改进。工业数据集的实验表明，Interactor框架在生成知识丰富且忠实的广告描述方面显着优于最先进的方法。自2026年5月以来，它已在线部署在领先的搜索广告系统中，为广告收入和用户体验做出了贡献。

[阅读原文](https://arxiv.org/abs/2606.15911)

---

## 40. 从最小标签扩展LLM推理：具有轻量级验证器的半监督框架

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Keizo Kato, Chenhui Chu, Yugo Murawaki, Sado Kurohashi

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a semi-supervised framework with a lightweight verifier for reasoning verification, enabling scalable pseudo-labeling from minimal labels, directly relevant to RL/verifier-driven optimization for LLMs.

**摘要**: arXiv：2606.16811v1宣布类型：新摘要：对于大型语言模型（LLM）的开发，最近生成伪中间推理的方法取得了显着的进展。但他们通常依赖于大量正确注释的答案来评估推理质量。本文提出了一个半监督框架，该框架将推理学习从最低监督扩展，将推理验证本身转变为数据创建机制。我们仅在少数已标记的样本上训练一个轻量级推理正确性分类器，该分类器判断LLM生成的中间推理痕迹是否有效。此外，基于信息量的置信度阈值过滤掉不可靠的样本，剩余的高置信度推理轨迹用于微调模型。可验证数学问题（Orca-Math子集）和使用视觉编程的图像场景图问题解答（GQA）的实验表明，我们的方法的准确性与使用10- 15倍以上的标签数据相当。消融分析证实，分类器和熵过滤对于可扩展和抗噪伪标记至关重要。通过用轻量级推理验证取代昂贵的回答级监督，我们的方法提供了构建大规模推理资源的实用途径，并为未来从最少的人类输入中学习的自主推理系统铺平了道路。

[阅读原文](https://arxiv.org/abs/2606.16811)

---

## 41. 基于LLM的事件预测的强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Amit Arnold Levy

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Applies GRPO (an RL method) to fine-tune LLMs for event forecasting, demonstrating strong scaling and performance gains, directly contributing to RL for LLMs.

**摘要**: arXiv：2606.15917v1宣布类型：新摘要：我们使用群组相对策略优化（GRPO），这是一种最近设计的样本和内存高效强化学习方法，在1.5B至14 B参数范围内微调预训练的LLM，这些LLM能够通过使用维基百科修订工具或新闻摘要来获取当前信息，以预测超出LLM知识界限的真实事件，以及为模拟训练动态的不同方面而提出的问题。   我们使用这些实验的结果来评论LLM预测的扩展能力，并对判断性预测如何适合可验证/不可验证领域分类进行分类，同时考虑预测未来事件（例如骰子滚动）时固有的任意不确定性的影响。   作为GRPO培训的结果，我们成功地引入了1.5B参数Transformer（Qwen 2.5 1.5B），在相同数据集上预测优于Claude Sonnet 3.5的性能，该数据集是通过来自市场商定概率的交叉信息来测量的。我们还讨论了实现这一结果的各种死胡同。

[阅读原文](https://arxiv.org/abs/2606.15917)

---

## 42. 自我质疑视觉语言模型：成分视觉推理的强化学习

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Saraswathy Amjith

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes a self-questioning framework for VLMs using GRPO (RL) with a reward for intermediate sub-questions, directly improving compositional visual reasoning via RL.

**摘要**: arXiv：2606.15651v1宣布类型：新摘要：视觉语言模型（VLM）是处理图像和文本的人工智能系统，但它们经常难以解决需要将多个步骤链接在一起的合成视觉推理问题，例如识别对象、计数对象和比较结果。现有的方法通过根据人类编写的逐步解释训练模型来改进这种推理，但创建这些注释成本高昂且难以扩展。我们提出了一个自我质疑框架，该框架训练VLM将视觉问题分解为更小的子问题，并使用名为“组相对政策优化”（GRPO）的强化学习算法在产生最终答案之前回答每个问题。该模型从未展示如何分解问题的示例，它在奖励信号的指导下自行发现这种行为，该信号对输出是否包含子问题以及最终答案是否正确进行评分。我们将这个框架应用于一个30亿参数的模型，在几何形状的合成场景（CREVR）和现实世界照片（A-OKVQA）上进行训练。在A-OKVQA上，自我质疑和标准强化学习都比未经训练的模型大幅提高了准确性（52.2%和51.6% vs. 46.8%）。我们引入了第一个自我质疑VLM，不仅像标准RL一样奖励最终答案，而且还奖励生成中间子问题，使其能够发现组合分解策略。这些结果表明，教人工智能系统问自己中间问题是复杂视觉推理的一种有前途的策略，特别是当问题的难度需要明确的逐步分解时。

[阅读原文](https://arxiv.org/abs/2606.15651)

---

## 43. DEEPRUBRIC：深度研究代理的有效强化学习的证据树专题监督

**得分**: 相关性 (Rel): 8/10, 创新性 (Nov): 7/10

**作者**: Minghang Zhu, Chuyang Wei, Junhao Xu, Yilin Cheng, Zhumin Chen, Jiyan He

**机构**: Unknown Institution

**💡 亮点 (Highlight)**: Proposes DeepRubric, a framework for constructing reliable query-rubric supervision from evidence trees, enabling efficient rubric-based GRPO for training deep research agents with strong performance and reduced compute.

**摘要**: arXiv：2606.17029v1宣布类型：新摘要：深度研究代理通过搜索和推理检索到的证据来合成长篇报告。具有基于标题的奖励的强化学习通过针对可检查标准进行优化来改进这些代理，这些标准将报告质量转化为奖励信号，但其效率取决于这些标准是否可靠地捕捉任务范围和证据需求。大多数现有的研究要求LLM为给定查询生成主题，但当模型未能推断出底层信息需求时，生成的主题可能不完整并降低RL效率。为了获得更可靠的查询--标题监督，我们引入了DeepRubric，这是一个逆转这一过程的数据构建框架：它不是为给定查询推断评估标准，而是首先确定应该根据什么来评估证据支持的报告，然后合成对齐的查询--来自这些评估目标的标题对。DeepRubric从采样的种子主题开始，通过逐步扩展证据支持的子问题来构建证据树，子问题的叶子充当原子且可验证的评估目标。然后，它使用证据树来合成训练查询和标题，确保奖励准确评估查询所请求的信息。使用DeepRubric，我们构建了9 K查询--rubric监督示例，并使用基于标题的GRPO训练DeepRubric-8B，在三个基准测试中实现了与之前的开放最先进深度研究模型相当的性能，RL GPU-h减少了大约13倍。

[阅读原文](https://arxiv.org/abs/2606.17029)

---

