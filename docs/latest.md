# Daily AI Intelligence Digest

**Updated:** 2026-10-21 06:08 UTC  
**Window:** last 36 hours · **Stories in window:** 452 · **New database records:** 1401

> This page is replaced every run. Findings history is preserved in `data/findings.sqlite`.

## Robotics

### [Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning](https://arxiv.org/abs/2610.27039)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27039v1 Announce Type: new  Abstract: Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model

### [Evaluating Social Reasoning in Embodied Vision-Language Models](https://arxiv.org/abs/2610.27496)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27496v1 Announce Type: new  Abstract: Foundation models now serve as reasoning layers for robot teams, but it remains unclear whether embodiment-specialized vision-language models (VLMs) preserve the social-reasoning capabilities of general-purpose VLMs. We evaluate Gemini Robotics-ER on SHREC, a benchmark o

### [Training Controllable World Models via Action Influence Maximization](https://arxiv.org/abs/2610.27387)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27387v1 Announce Type: new  Abstract: Action-conditioned video generative models trained on successful, goal-directed demonstrations tend to ignore the commanded action, rendering a plausible expert-like future regardless of what is asked of them. We trace this failure to training data that lack sufficient a

### [Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with Autism Spectrum Disorder](https://arxiv.org/abs/2610.27162)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27162v1 Announce Type: new  Abstract: In robot-assisted education, a robot must understand how to complete a task in order to effectively guide a student through it. We present a novel method that enables a semi-autonomous, camera-equipped robot to recognise the task goal and plan actions to achieve it. Our 

### [Multi-View Latent Action Pretraining for Cross-Embodiment Robot Learning from Videos](https://arxiv.org/abs/2610.27794)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27794v1 Announce Type: new  Abstract: Action-free videos are an appealing substitute for costly teleoperated data. Latent action models (LAMs) turn videos into a supervision signal by inferring abstract actions between frames. Existing LAMs observe a single camera view, which resolves 6D robot actions only a

### [CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation](https://arxiv.org/abs/2610.27677)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27677v1 Announce Type: new  Abstract: In object goal navigation (ObjectNav), an embodied agent must find a target object (e.g., "find a bed") in a previously unseen environment, relying on spatial commonsense such as object co-occurrence. Large Language Models (LLMs) encode this commonsense, but deploying th

### [Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning](https://arxiv.org/abs/2610.27613)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27613v1 Announce Type: new  Abstract: Can embodied task agents use tactile experience to perform fine manipulation without task-specific model training? We investigate this capability through Tactile-ETA, a system that incorporates tactile experience into an embodied task agent through in-context learning. S

### [Real-Time Disturbance-Aware Koopman Model Predictive Control for Quadrotors in Spatially Varying Winds](https://arxiv.org/abs/2610.27414)

**Source:** arXiv Robotics · **Published:** 2026-10-21

arXiv:2610.27414v1 Announce Type: new  Abstract: Reliable quadrotor flight in disturbed environments requires predictive models that remain accurate as unmodeled aerodynamic effects change during deployment. We introduce a disturbance-aware Koopman Control Family (DA-KCF) framework that preserves an offline-identified 

## Security

### [After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents](https://arxiv.org/abs/2610.28425v1)

**Source:** arXiv Search: AI Security · **Published:** 2026-10-20

Modern LLM agents persist state across sessions via two channels: long-lived memory files silently prepended to the system prompt, and scheduled tasks waking the agent without user input. A one-time indirect prompt injection committed to either channel can re-fire across sessions long after the attacker leaves, threats

### [AgenticVulHunter: Bringing Local Agentic Vulnerability Hunting to Your Terminal](https://arxiv.org/abs/2610.27383)

**Source:** arXiv Security · **Published:** 2026-10-21

arXiv:2610.27383v1 Announce Type: new  Abstract: Finding vulnerabilities early, before they can affect the production system, is important for reducing the risk of any software attacks. However, detecting vulnerabilities during secure code review is still difficult because the vulnerable code logic may depend on lines 

### [When Models Know but Can't Linearly Say: Relational Encoding Limits Linear Vulnerability Classification in Code LLMs](https://arxiv.org/abs/2610.27257)

**Source:** arXiv Security · **Published:** 2026-10-21

arXiv:2610.27257v1 Announce Type: new  Abstract: Large language models can detect vulnerable code, yet the form of vulnerability encoding in their representations remains unclear. We analyze 8 code models spanning 6.7B-15B parameters on C programs using three datasets (DELTASECOMMITS, SVEN, and PRECISE-BUGS), comparing

### [Model Exposure on One Device Endangers Others: Rethinking Edge Neural Network Security across Devices](https://arxiv.org/abs/2610.27152)

**Source:** arXiv Security · **Published:** 2026-10-21

arXiv:2610.27152v1 Announce Type: new  Abstract: Neural networks (NNs) are increasingly deployed on edge devices such as mobile and IoT platforms, offering low latency and improved privacy compared to cloud-based deployment. However, on-device models embedded in mobile applications can be unpacked and exposed to advers

### [Make the Adversary Spend More Energy: Generative Deception against Language-Model Attackers in Critical Infrastructure](https://arxiv.org/abs/2610.27739)

**Source:** arXiv Security · **Published:** 2026-10-21

arXiv:2610.27739v1 Announce Type: new  Abstract: Language-model attackers consume computational resources as they explore and interact with a target, creating an opportunity for cyber deception to impose costs. Whether such engagements favor the defender requires measuring both sides. We evaluate an autonomous language

### [A Unified Attack Framework against Statistical Generative Watermarks for Large Language Models](https://arxiv.org/abs/2610.27653)

**Source:** arXiv Security · **Published:** 2026-10-21

arXiv:2610.27653v1 Announce Type: new  Abstract: Watermarking has emerged as a key tool for identifying text generated by large language models (LLMs), with current schemes embedding statistical signals into the generation process to enable later detection. In this work, we identify a shared weakness across a broad cla

### [Adversarial Benchmarks and BenchDoor Attacks: Exploiting Benchmark Incentives for Backdoor Attacks](https://arxiv.org/abs/2610.27533)

**Source:** arXiv Security · **Published:** 2026-10-21

arXiv:2610.27533v1 Announce Type: new  Abstract: Machine learning benchmarks act as guideposts for model development and spur the creation of training datasets intended to improve benchmark scores. We introduce BenchDoor, a family of data poisoning attacks that exploits this incentive. Beyond preserving benign performa

### [Profile-DP: Differential Privacy for User-Controlled Profile Release in Personalized LLM Inference](https://arxiv.org/abs/2610.27213)

**Source:** arXiv Security · **Published:** 2026-10-21

arXiv:2610.27213v1 Announce Type: new  Abstract: Personalized large language models (LLMs) increasingly rely on profile-conditioned inference, pairing public requests with rich, user-specific facts. This paradigm exposes the user profile itself, together with the user's explicit sharing preferences. We introduce Profil

## Research

### [Vulnerability Analysis for Safe Multi-Agent Reinforcement](https://arxiv.org/abs/2610.27293)

**Source:** arXiv AI · **Published:** 2026-10-21

arXiv:2610.27293v1 Announce Type: new Abstract: Safe Multi-Agent Reinforcement Learning (SMARL) aims to learn cooperative control policies under prescribed safety constraints. Al- though existing SMARL methods focus on enforcing safety during policy optimization, their vulnerability remains largely unexplored. This pap

### [ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems](https://arxiv.org/abs/2610.27046)

**Source:** arXiv AI · **Published:** 2026-10-21

arXiv:2610.27046v1 Announce Type: new Abstract: As AI systems begin to resolve open research problems, reliable verification becomes increasingly important. Formal mathematics provides a trusted framework for mathematical reasoning, enabling agents to produce machine-checkable proofs while conducting mathematical explo

### [Diagnostic Analysis for Large Language Model Reasoning](https://arxiv.org/abs/2610.27245)

**Source:** arXiv Language Models · **Published:** 2026-10-21

arXiv:2610.27245v1 Announce Type: new Abstract: Reasoning structures (e.g., chains and graphs) are increasingly used for probabilistic inference, factuality verification, and uncertainty estimation, but their structural reliability is rarely evaluated directly. We test whether this reliability holds through a proposed 

### [LoWAgent: A Low-Resource Multilingual Benchmark for Web Agents](https://arxiv.org/abs/2610.27205)

**Source:** arXiv Language Models · **Published:** 2026-10-21

arXiv:2610.27205v1 Announce Type: new Abstract: Web agents are typically evaluated on English-language interfaces, leaving their ability to operate across the world's multilingual websites largely unexplored. This gap is especially significant for low-resource languages, where standardized resources for evaluating web 

### [Fluent but Fallible: Benchmarking Hallucination and Factual Reliability in Large Language Models](https://arxiv.org/abs/2610.27034)

**Source:** arXiv Language Models · **Published:** 2026-10-21

arXiv:2610.27034v1 Announce Type: new Abstract: Large Language Models (LLMs) have significantly advanced natural language processing and artificial intelligence applications through their capabilities in reasoning, text generation and knowledge retrieval. However, LLMs are still vulnerable to two important challenges: 

### [TxnQA: Benchmarking Analytical Reasoning and Evidence Grounding over Transaction Event Sequences](https://arxiv.org/abs/2610.27256)

**Source:** arXiv AI · **Published:** 2026-10-21

arXiv:2610.27256v1 Announce Type: new Abstract: Analyzing merchant transaction histories requires dynamic temporal filtering, entity resolution, and aggregation over irregular event streams--operations poorly captured by static tabular or time-series forecasting benchmarks. We introduce TxnQA, an analytical QA benchmar

### [PORA: Learning When More Reasoning Pays Off for LLM Agents](https://arxiv.org/abs/2610.27119)

**Source:** arXiv AI · **Published:** 2026-10-21

arXiv:2610.27119v1 Announce Type: new Abstract: LLM agents perform tasks over multiple steps and revise their actions based on feedback. As the total reasoning budget is often limited and must support future steps, the agent must choose between short and long reasoning before each action. Longer reasoning may improve t

### [MAMath-Bench: Process-Aware and Robust Evaluation of Multimodal Multi-Agent Mathematical Reasoning](https://arxiv.org/abs/2610.26943)

**Source:** arXiv AI · **Published:** 2026-10-21

arXiv:2610.26943v1 Announce Type: new Abstract: Mathematical reasoning is a fundamental capability for educational applications of Large Language Models (LLMs), where reliable problem solving requires not only correct answers but also coherent and verifiable reasoning processes. Multi-agent systems (MASs) have shown gr

## Community

### [KFlash: Benchmarks of newly released versions of Apple Silicon optimized engines: 1.4.0 Splash (DFlash2 ~ 50 tok/s) vs 0.2 Kapitsa (KFlash ~65 tok/s), MLX(MTP) & more on Qwen 3.8 27b/4b/35b 4Q on Macbook Pro M4 Pro 48 GB 2024, 48GB & Macboo](https://www.reddit.com/r/LocalLLaMA/comments/1xbdxg3/kflash_benchmarks_of_newly_released_versions_of/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-21

hey folks, its Ye, I work on an open source project called Kapitsa : its a fast Apple Silicon optimized inference engine built for Qwen and Nemotron models. this week two new releases landed in local inference: Inco shipped Splash 1.4.0 yesterday, and we shipped Kapitsa 0.2 today with a new speculative decoding method 

### [New Sota 27B local Decision model: Drex Max 2.0](https://www.reddit.com/r/LocalLLaMA/comments/1xbexic/new_sota_27b_local_decision_model_drex_max_20/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-21

submitted by /u/DotaMate [link] [comments]

### [Does anyone take requests to create heretic models? I want a heretic version of this qwen 3.8 27B finetune that says it’s better than swift!](https://www.reddit.com/r/LocalLLaMA/comments/1xbcir1/does_anyone_take_requests_to_create_heretic/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-21

This model is cool af! submitted by /u/Borkato [link] [comments]

### [I made a Pinokio app for Fish Audio's new TTS model "Drama 3", which fixes many of the issues people found (silent takes, missing words)](https://www.reddit.com/r/LocalLLaMA/comments/1xbc9og/i_made_a_pinokio_app_for_fish_audios_new_tts/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-21

submitted by /u/Thomas_Eric [link] [comments]

### [We built the AIM System One Index, a leaderboard for decision models (57 models ranked on accuracy, bias, cost and latency)](https://www.reddit.com/r/LocalLLaMA/comments/1xb73q4/we_built_the_aim_system_one_index_a_leaderboard/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-20

We’ve been testing “System One” models, also called decision models. Instead of generating text token by token, they return a typed decision with a probability for each option in a single pass. To compare them, we put together the AIM System One Index. It combines three benchmarks: Browser tasks: 50 tasks, one attempt 

### [Eagle-4 Released: Faster than DFlash2 & DSpark](https://www.reddit.com/r/LocalLLaMA/comments/1xb6zds/eagle4_released_faster_than_dflash2_dspark/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-20

Insane numbers, so far only Qwen3.8-27B is supported but wow those are some good numbers. Will watch closely when this lands in llama.cpp/vLLM ### Qwen 3.8 27B Benchmark Results Method Speedup over Vanilla MTP 2.22× DSpark 2.57× DFlash 2 2.80× EAGLE-4 3.59× submitted by /u/TKGaming_11 [link] [comments]

### [I built an RK3588 NPU runtime without any proprietary inference libraries: Qwen3.5-4B at ~10 tok/s, ~2x faster than vendor SDK.](https://www.reddit.com/r/LocalLLaMA/comments/1xb45bq/i_built_an_rk3588_npu_runtime_without_any/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-20

If you have an RK3588 board, here’s another way to put its NPU to work. I made open_rknpu2_lm_infer, a local LLM inference engine for the Rockchip RK3588 NPU. It runs without Rockchip’s proprietary userspace inference libraries. The upper part is written in Rust and the NPU operators are coded with C++. No black-box, y

### [qev-0.8b · New SOTA tiny local decision model](https://www.reddit.com/r/LocalLLaMA/comments/1xazrvd/qev08b_new_sota_tiny_local_decision_model/)

**Source:** Reddit LocalLLaMA · **Published:** 2026-10-20

submitted by /u/fajfas3 [link] [comments]

## Enterprise

### [Access OpenAI GPT models on Amazon Bedrock from Canada with cross-Region inference](https://aws.amazon.com/blogs/machine-learning/access-openai-gpt-models-on-amazon-bedrock-from-canada-with-cross-region-inference)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

Canadian organizations can now access OpenAI GPT-5.6, GPT-6, and GPT-6.1 models on Amazon Bedrock from the Canada (Central) and Canada West (Calgary) Regions using cross-Region inference. This post covers the models and inference profiles, how to set up permissions, and how to invoke them with the Responses, Chat Compl

### [Beyond the KV cache: Training and serving i14’s Laplace 3B linear attention model on AWS Trainium2 with native PyTorch](https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

Learn how i14 trained and served Laplace 3B, a linear attention model, on AWS Trainium2 using native PyTorch. Its recurrent state stays fixed at 29.5 MB per sequence regardless of context length, avoiding the growing key-value cache of transformer models and keeping serving memory predictable.

### [Work management context for AI agents with Smartsheet MCP on AWS](https://aws.amazon.com/blogs/machine-learning/work-management-context-for-ai-agents-with-smartsheet-mcp-on-aws)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

The Smartsheet Model Context Protocol (MCP) Server lets AI agents read, update, and act on live work management data. This post shows two ways to connect it on AWS: Amazon Quick for business teams and Kiro for developers, so your agents can work with Smartsheet without switching tools.

### [From data to decisions: Conversational supply chain intelligence with Amazon Quick and Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/from-data-to-decisions-conversational-supply-chain-intelligence-with-amazon-quick-and-amazon-bedrock-agentcore)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

Enterprise supply chains are data-rich but insight-poor, with the data to decide scattered across ERP, monitoring, procurement, and email. This post shows how Amazon Bedrock AgentCore exposes those systems as a governed tool layer, and how Amazon Quick turns them into one conversational experience for business users, w

### [Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

Learn how we fine-tuned GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod, and how to decide between supervised fine-tuning (SFT) and reinforcement learning with GRPO. SFT took reasoning-language accuracy from 22% to 100%, and GRPO added measurable gains where headroom existed.

### [Discover tools at runtime with AWS Agent Registry](https://aws.amazon.com/blogs/machine-learning/discover-tools-at-runtime-with-aws-agent-registry)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

Hardcoded tool wiring breaks down as an agent's catalog grows from a handful of tools to hundreds. This post walks through a runtime Discover, Instantiate, Execute loop built on AWS Agent Registry, where an orchestrator discovers MCP servers and A2A agents through semantic search at runtime instead of compiling every t

### [Securing AI agent identity with X.509 PKI on AWS](https://aws.amazon.com/blogs/machine-learning/securing-ai-agent-identity-with-x-509-pki-on-aws)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

Learn how to secure multi-agent AI systems with cryptographic identity using Keyfactor EJBCA and AWS services. This reference architecture combines signed request envelopes, user-signed delegation assertions, RFC 8693 audience-scoped tokens, and real-time OCSP revocation to prove agent identity and prevent request forg

### [How Eon built multi-cloud investigation with an MCP Gateway on Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/how-eon-built-multi-cloud-investigation-with-an-mcp-gateway-on-amazon-bedrock-agentcore)

**Source:** AWS Machine Learning · **Published:** 2026-10-20

Learn how Eon replaced per-tool credentials and local MCP processes across AWS, GCP, and Azure with a single authenticated Amazon Bedrock AgentCore gateway, giving more than 100 developers and autonomous agents unified access to production investigation and cutting new-engineer onboarding from two days to two minutes.

## News

### [Microsoft says AI agents are like insider threats as ‘frontier models can’t be trusted’](https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted)

**Source:** TechCrunch AI · **Published:** 2026-10-19

Microsoft wants enterprises to closely watch the agents that employees use with systems not controlled by AI labs like OpenAI and Anthropic.

### [OpenBSD 8.0 arrives with security record still intact](https://arstechnica.com/gadgets/2026/10/openbsd-8-0-lands-with-intel-arc-graphics-support/)

**Source:** Ars Technica · **Published:** 2026-10-20

OpenBSD 8.0 lands with Intel Arc support, ARM64 hibernation, and 64-vCPU guests

### [PHP warns it plans to release 2 emergency patches imminently](https://arstechnica.com/security/2026/10/php-maintainers-tell-web-devs-to-prepare-themselves-for-critical-security-patches/)

**Source:** Ars Technica · **Published:** 2026-10-21

Unconfirmed report claims PHP2Shell exploit remotely executes code on PHP sites.

### [Anthropic pitches AI safety bill that may block a model if 50+ people could be killed](https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed)

**Source:** TechCrunch AI · **Published:** 2026-10-20

The proposed policy seems to offer protections against AI running amok but actually forbids federal agencies from blocking a model's release without the permission of a judge.

### [Google has joined Amazon in attacking Nvidia’s stronghold with AI app developers](https://techcrunch.com/2026/10/20/google-has-joined-amazon-in-attacking-nvidias-stronghold-with-ai-app-developers)

**Source:** TechCrunch AI · **Published:** 2026-10-20

Google has joined Amazon in releasing a developer tool that makes it easy for PyTorch users to move their apps off Nvidia GPUs.

### [Plants can speak using electricity, so this startup built an AI model to decipher their language](https://techcrunch.com/2026/10/20/plants-can-speak-using-electricity-so-this-startup-built-an-ai-model-to-decipher-their-language)

**Source:** TechCrunch AI · **Published:** 2026-10-20

Electric Plant has built an AI-powered translator to help humans listen to what plants are saying with the subtle electricity coursing through their stems.

## Hardware

### [Profile-DP: Differential Privacy for User-Controlled Profile Release in Personalized LLM Inference](https://arxiv.org/abs/2610.27213v1)

**Source:** arXiv Search: Efficient Inference · **Published:** 2026-10-19

Personalized large language models (LLMs) increasingly rely on profile-conditioned inference, pairing public requests with rich, user-specific facts. This paradigm exposes the user profile itself, together with the user's explicit sharing preferences. We introduce Profile-DP, a policy-aware local differential privacy f

## Agents

### [GBClaw: An agentic AI framework for atomistic grain boundary research and mechanistic discovery](https://arxiv.org/abs/2610.28629v1)

**Source:** arXiv Search: AI Agents · **Published:** 2026-10-20

Agentic artificial intelligence (AI) systems hold immense potential for automating complex workflows in materials discovery and design, but extending them to domain-intensive mechanistic investigations remains challenging. Here, we present GBClaw, an agentic AI framework for investigating the structure and deformation 

### [TraceLite: Efficient Trace Reduction for SWE Agents via Optical Compression and Redundancy Removal](https://arxiv.org/abs/2610.28612v1)

**Source:** arXiv Search: AI Agents · **Published:** 2026-10-20

Software engineering agents solve repository-level tasks through iterative tool use, but their continuously growing interaction traces incur substantial token consumption and inference overhead. Existing compression approaches often require model training, auxiliary LLM calls, or assumptions about specific content such

### [MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems](https://arxiv.org/abs/2610.28397v1)

**Source:** arXiv Search: AI Agents · **Published:** 2026-10-20

Agentic AI extends large language models (LLMs) from generating responses to planning and executing complex workflows, substantially expanding their utility while exposing applications to unsafe actions, information leakage, and adversarial manipulation. Multi-agent systems further expand these capabilities through spe

### [VisualEvolve: A Skill Self-Evolution Framework for Visual Reasoning](https://arxiv.org/abs/2610.28386v1)

**Source:** arXiv Search: AI Agents · **Published:** 2026-10-20

Visual tool use enables vision-language models (VLMs) to acquire task-relevant evidence, but its effectiveness can be limited by predefined visual operations and the tool-use strategies learned during training. Representing these operations and strategies as reusable external skills allows them to be refined through se

### [Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design](https://arxiv.org/abs/2610.28380v1)

**Source:** arXiv Search: AI Agents · **Published:** 2026-10-20

Agent harnesses are executable code that specifies the prompts, tools, and control flow around a language model. A single global harness can struggle with heterogeneous tasks that require different execution strategies. In this work, we introduce Object-Oriented Harness (OO-Harness), a harness optimization framework th

## Quantum

### [Local-Channel Stability of Classical $\mathbb Z_2$ Lattice Gauge Models](https://arxiv.org/abs/2610.27939)

**Source:** arXiv Quantum · **Published:** 2026-10-21

arXiv:2610.27939v1 Announce Type: new  Abstract: We establish sufficient conditions for two-way local quantum-channel stability in classical $\mathbb Z_2$ lattice gauge models with spins on $m$-dimensional cells of a $d$-dimensional lattice. Each interaction multiplies the spins on the boundary of an $(m+1)$-cell. This

### [Cavity models of non-Abelian gauge theories](https://arxiv.org/abs/2610.27070)

**Source:** arXiv Quantum · **Published:** 2026-10-21

arXiv:2610.27070v1 Announce Type: new  Abstract: In quantum optics and related fields, cavity quantum electrodynamics provides a powerful framework for modeling the low-energy properties of bound charges coupled to electromagnetic fields, using a minimal set of atomic levels and isolated photonic modes. Here, we develo

## Governance

### [Humans Correct Their Judgments Through Debate, but Weaker AI Models Do Not](https://arxiv.org/abs/2610.28539v1)

**Source:** arXiv Search: AI Governance · **Published:** 2026-10-20

How can we effectively oversee AI systems that surpass human intelligence? AI Safety via Debate proposes that two AI systems argue opposing positions and a judge, either a human or a weaker model, decides which is correct. By facilitating supervisors in providing high-quality training signals, debate aims to encourage 

## Engineering

### [Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG](https://arxiv.org/abs/2610.28364v1)

**Source:** arXiv Search: RAG and Retrieval · **Published:** 2026-10-20

Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-secureRAG, a roughly 0.5B-parameter small language model that acts as a semantic firewall between re

### [DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge](https://arxiv.org/abs/2610.28340v1)

**Source:** arXiv Search: RAG and Retrieval · **Published:** 2026-10-20

Reliable retrieval-augmented generation (RAG) requires recognizing when neither retrieved documents nor parametric knowledge supports an answer. We introduce DeclineCraft, a dynamic abstention benchmark whose unanswerable questions target Minecraft feature additions after a corpus cut-off, with audits of possible param

### [A Multimodal Engineering GraphRAG Framework for Post-Wind-Event Building Assessment and Recovery Inference](https://arxiv.org/abs/2610.28216v1)

**Source:** arXiv Search: RAG and Retrieval · **Published:** 2026-10-20

Post-event building assessment requires linking observed physical damage to its consequences for safety, habitability, functionality, and recovery. Yet post-disaster evidence is often heterogeneous, incomplete, and distributed across images and reconnaissance reports, while recovery models typically require structured 

## Open source

### [microsoft/DeepSpeed: v0.19.8 Patch Release](https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.19.8)

**Source:** GitHub: microsoft/DeepSpeed · **Published:** 2026-10-20

## What's Changed * Deprecate leftovers of compression library by @hwchen2017 in https://github.com/deepspeedai/DeepSpeed/pull/8535 * Update version.txt after 0.19.7 release by @loadams in https://github.com/deepspeedai/DeepSpeed/pull/8555 * Deprecate loco zero++ by @hwchen2017 in https://github.com/deepspeedai/DeepSpe

### [ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model](https://huggingface.co/blog/ibm-research/altk-evolve-bc)

**Source:** Hugging Face Blog · **Published:** 2026-10-20

Read the original source for details.

---

Generated automatically. The primary source should be consulted before relying on any finding.

**Distinct headline clusters:** 59. Some headlines may cover the same event.
