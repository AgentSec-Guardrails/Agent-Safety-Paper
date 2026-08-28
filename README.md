# LLM Agent Safety

A curated collection of research papers, benchmarks, defenses, training methods, and system designs for LLM agent safety.

This repository focuses on safety issues that arise when large language models act as agents: following long-horizon goals, using tools, reading untrusted content, retrieving or storing memory, interacting with users, and operating inside larger software systems.

## Table of Contents

- [LLM Agent Safety](#llm-agent-safety)
  - [Table of Contents](#table-of-contents)
  - [Papers](#papers)
    - [1. Safety Evaluation \& Benchmarking](#1-safety-evaluation--benchmarking)
    - [2. Safety Defense](#2-safety-defense)
      - [2.1 Guardrails](#21-guardrails)
        - [2.1.1 Input Guardrail](#211-input-guardrail)
        - [2.1.2 Planner Guardrail](#212-planner-guardrail)
        - [2.1.3 Retrieval / Memory Guardrail](#213-retrieval--memory-guardrail)
        - [2.1.4 Tool Execution Guardrail](#214-tool-execution-guardrail)
        - [2.1.5 Output \& Audit Guardrail](#215-output--audit-guardrail)
      - [2.2 Safety Alignment by Agent Component](#22-safety-alignment-by-agent-component)
        - [2.2.1 Overview and General-Purpose Alignment](#221-overview-and-general-purpose-alignment)
        - [2.2.2 Tool-Use, Action, and Environment Alignment](#222-tool-use-action-and-environment-alignment)
        - [2.2.3 Planning, Reasoning, and Trajectory Alignment](#223-planning-reasoning-and-trajectory-alignment)
        - [2.2.4 Memory-Based Alignment](#224-memory-based-alignment)
        - [2.2.5 Preference and Value Alignment](#225-preference-and-value-alignment)
      - [2.3 Trustworthy Agent Architecture](#23-trustworthy-agent-architecture)
    - [3. VLM agent](#3-vlm-agent)
      - [3.1 Normal Agents](#31-normal-agents)
      - [3.2 Embodied Agents](#32-embodied-agents)
    - [4. Multi-Agent Safety & Alignment](#4-multi-agent-safety--alignment)
      - [4.1 Evaluation, Failure Analysis & Attacks](#41-evaluation-failure-analysis--attacks)
      - [4.2 Guardrails, Detection & Resilience](#42-guardrails-detection--resilience)
      - [4.3 Safety Alignment, Oversight & Governance](#43-safety-alignment-oversight--governance)
  - [Contributing](#contributing)

## Papers

<a id="safety-evaluation--benchmarking"></a>
### 1. Safety Evaluation & Benchmarking

Papers, datasets, benchmarks, and red-teaming methods for measuring agent safety risks, including prompt injection, tool misuse, privacy leakage, autonomy risk, harmful task completion, and benchmark reliability.
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)
  - 🔑 Key: benchmark
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: AgentDojo is a dynamic benchmark environment for evaluating prompt injection attacks and defenses in tool-using LLM agents. It provides realistic agent tasks, security test cases, and attack/defense settings to measure both task utility and whether malicious instructions hidden in external tool outputs can hijack the agent.
  - 📅 Date: Jun 18, 2024 / NeurIPS D&B 2024

- [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)
  - 🔑 Key: benchmark
  - 🤖 Agent Type: Web Agents / UI Agents
  - 📖 TLDR: WASP is a benchmark for evaluating web agent security against prompt injection attacks. It creates realistic browser-based hijacking scenarios in an isolated environment, measuring whether agents can complete user tasks while resisting malicious instructions embedded in web content.
  - 📅 Date: Apr 2025 / NeurIPS D&B 2025

- [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://arxiv.org/abs/2411.07781)
  - 🔑 Key: benchmark
  - 🤖 Agent Type: Code Agents / Tool Agents
  - 📖 TLDR: RedCode is a benchmark and evaluation platform for code agent safety. It evaluates whether code agents can recognize and avoid risky code execution, and whether code models generate unsafe or malicious code across diverse languages, formats, and real system-interaction settings.
  - 📅 Date: Nov 2024 / NeurIPS D&B 2024

- [PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action](https://arxiv.org/abs/2409.00138)
  - 🔑 Key: benchmark
  - 🤖 Agent Type: LLM Agents
  - 📖 TLDR: PrivacyLens is a benchmark for evaluating whether LLM agents leak sensitive information or violate privacy norms during action execution, not just in final outputs.
  - 📅 Date: Sep 2024 / NeurIPS D&B 2024
<a id="safety-defense"></a>
### 2. Safety Defense

Methods that prevent, detect, constrain, or audit unsafe agent behavior. Guardrails are treated here as one important class of defense, alongside monitoring, policy enforcement, sandboxing, verification, and recovery mechanisms.

<a id="guardrails"></a>
#### 2.1 Guardrails

<a id="input-guard-rail"></a>
##### 2.1.1 Input Guardrail

- [PromptArmor: Simple yet Effective Prompt Injection Defenses](https://arxiv.org/abs/2507.15219)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: This paper revisits a simple LLM-based defense for prompt injection attacks. Instead of training a new detector or modifying the target agent, PromptArmor uses an off-the-shelf LLM as a preprocessing defense: it inspects untrusted external content, identifies injected malicious instructions, removes or rewrites them, and then passes the cleaned content to the downstream agent. The method is simple to deploy, works with black-box agents, and shows strong results on benchmarks such as AgentDojo and OpenPromptInject, reducing attack success while preserving task utility.
  - 📅 Date: Jul 21, 2025

- [Defending Against Indirect Prompt Injection Attacks With Spotlighting](https://arxiv.org/abs/2403.14720)
  - 🔑 Key: defense
  - 🤖 Agent Type: LLM Applications / RAG Systems / Tool Agents
  - 📖 TLDR: This paper proposes Spotlighting, a training-free defense against indirect prompt injection attacks. The core idea is to make untrusted external content visibly distinguishable from trusted user/system instructions, so the LLM can better treat retrieved web pages, documents, emails, or tool outputs as data rather than executable instructions. The paper shows that spotlighting can reduce attack success rate from over 50% to below 2% in their experiments, while keeping normal task performance mostly intact.
  - 📅 Date: Mar 21, 2024



<a id="planner-guard-rail"></a>
##### 2.1.2 Planner Guardrail

- [The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2412.16682)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: This paper reframes indirect prompt injection defense as a task alignment problem. Instead of only detecting whether external content is malicious, Task Shield checks whether each instruction, assistant response, and tool call actually contributes to the user's original goal. If an instruction or tool call does not align with the user task, Task Shield blocks or corrects it before the agent proceeds. On AgentDojo, it significantly reduces attack success while preserving task utility.
  - 📅 Date: Dec 2024 / ACL 2025

- [MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents](https://openreview.net/forum?id=gt1MmGaKdZ)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: This paper proposes MELON, a training-free defense against indirect prompt injection attacks in LLM agents. The key observation is that when an attack succeeds, the agent's next action becomes less dependent on the original user task and more dependent on malicious instructions hidden in tool-retrieved content. MELON detects this by re-executing the agent with the user task masked, then comparing tool calls from the original run and the masked run. If the tool calls are similar, the agent is likely being driven by injected malicious content.
  - 📅 Date: Feb 2025 / ICML 2025

<a id="retrieval-memory-guard-rail"></a>
##### 2.1.3 Retrieval / Memory Guardrail
- [TrustRAG: Enhancing Robustness and Trustworthiness in RAG](https://arxiv.org/abs/2501.00879)
  - 🔑 Key: defense
  - 🤖 Agent Type: RAG Systems / LLM Applications
  - 📖 TLDR: TrustRAG is a plug-and-play, training-free defense framework for RAG systems under corpus poisoning attacks. It uses clustering-based filtering and LLM self-assessment to remove compromised or irrelevant retrieved content before generation, improving robustness and trustworthiness.
  - 📅 Date: Jan 2025

- [RobustRAG: Benchmarking Robustness of Retrieval Augmented Generation in the Presence of Corruptions](https://openreview.net/forum?id=qsEeACAJjD)
  - 🔑 Key: defense
  - 🤖 Agent Type: RAG Systems / LLM Applications
  - 📖 TLDR: RobustRAG proposes an isolate-then-aggregate defense for RAG systems under retrieval corruption. It processes retrieved documents separately and aggregates their answers, reducing the influence of poisoned or corrupted retrieved content on the final response.
  - 📅 Date: 2024

<a id="tool-execution-guard-rail"></a>
##### 2.1.4 Tool Execution Guardrail
- [Progent: Programmable Privilege Control for LLM Agents](https://arxiv.org/abs/2504.11703)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: Progent proposes a programmable privilege control framework for LLM agents. It lets developers define policies over tools, resources, contexts, and arguments, then enforces these policies before tool execution to prevent unsafe or over-privileged agent actions.
  - 📅 Date: Apr 2025

- [RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage](https://arxiv.org/abs/2502.08966)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: RTBAS is a runtime defense framework for tool-using LLM agents. It checks whether planned tool actions preserve integrity and confidentiality, blocking or asking for user confirmation when prompt injection or privacy leakage risks cannot be ruled out.
  - 📅 Date: Feb 2025

- [AgentArmor: Enforcing Program Analysis on Agent Runtime Trace to Defend Against Prompt Injection](https://arxiv.org/abs/2508.01249)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: AgentArmor applies program analysis to agent runtime traces. It converts agent trajectories into program-like dependency structures and checks them against security policies to detect prompt-injection-driven abnormal tool calls, unsafe data flows, and privilege boundary violations.
  - 📅 Date: Aug 2025



<a id="output-audit-guard-rail"></a>
##### 2.1.5 Output & Audit Guardrail
- [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://aclanthology.org/2025.acl-long.399/)
  - 🔑 Key: defense / architecture
  - 🤖 Agent Type: LLM Agents / Tool Agents
  - 📖 TLDR: AGrail proposes a lifelong guardrail framework for LLM agents that adaptively generates, executes, and transfers safety checks across tasks. It monitors agent actions at runtime, blocks unsafe behavior, and updates its safety memory to handle evolving risks.
  - 📅 Date: Jul 2025 / ACL 2025



<a id="safety-alignment-training"></a>
#### 2.2 Safety Alignment by Agent Component

Papers on aligning an agent's policy and runtime behavior with safety requirements. The groups below follow the **primary component being aligned** rather than treating every method as model fine-tuning. Entries are explicitly marked as training, inference-time defense, or evaluation evidence where appropriate.

##### 2.2.1 Overview and General-Purpose Alignment

- [A Survey on Alignment for Large Language Model Agents](https://openreview.net/attachment?id=gkxt5kZS84&name=pdf)
  - 🔑 Key: survey / taxonomy
  - 🤖 Agent Type: General LLM Agents / Multi-Agent Systems
  - 📖 TLDR: Surveys agent alignment goals, data, RLHF and adversarial-training methods, scalable oversight, ethical compliance, and long-term behavioral robustness across the full agent stack.
  - 📅 Date: 2025

- [AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security](https://arxiv.org/abs/2605.29801)
  - 🔑 Key: safety SFT / RL / online guardrail
  - 🤖 Agent Type: Tool Agents / Code Agents / Open-World Agents
  - 📖 TLDR: Uses a taxonomy-guided data engine and influence-function purification to train compact safety models with roughly 1K samples, then reuses them as low-cost online trajectory guardrails.
  - 📅 Date: May 28, 2026 / preprint

- [SafeAgent: Safeguarding LLM Agents via an Automated Risk Simulator](https://aclanthology.org/2026.acl-long.1501/)
  - 🔑 Key: synthetic data / safety fine-tuning
  - 🤖 Agent Type: Multi-Turn Tool Agents / Terminal Agents
  - 📖 TLDR: Decomposes risk into instruction-, context-, and action-induced sources, automatically simulates failures, and generates self-reflective safe trajectories for training; reports a 45% average safety gain.
  - 📅 Date: Jul 2026 / ACL 2026

- [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://aclanthology.org/2025.acl-long.399/)
  - 🔑 Key: adaptive runtime alignment / lifelong guardrail
  - 🤖 Agent Type: General LLM Agents / Tool Agents
  - 📖 TLDR: Generates and optimizes task-specific safety checks at runtime and transfers them across tasks, covering both application-defined risks and systemic confidentiality, integrity, and availability risks.
  - 📅 Date: Jul 2025 / ACL 2025

##### 2.2.2 Tool-Use, Action, and Environment Alignment

- [AgentAlign: Navigating Safety Alignment in the Shift from Informative to Agentic Large Language Models](https://arxiv.org/abs/2505.23020)
  - 🔑 Key: behavior-chain synthesis / safety fine-tuning
  - 🤖 Agent Type: Tool Agents / Action Executors
  - 📖 TLDR: Instantiates abstract harmful and benign behavior chains in simulated tool environments to create executable multi-step training data, teaching agents to reject harmful tasks without broadly refusing legitimate tool use.
  - 📅 Date: May 29, 2025 / preprint

- [ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations](https://aclanthology.org/2025.emnlp-main.714/)
  - 🔑 Key: tool-use safety training / dataset
  - 🤖 Agent Type: Tool Agents
  - 📖 TLDR: Provides direct-harm, indirect-harm, and multi-step tool trajectories for supervised fine-tuning, targeting failures that only emerge during chained tool invocation.
  - 📅 Date: Nov 2025 / EMNLP 2025

- [Agent Safety Alignment via Reinforcement Learning](https://arxiv.org/abs/2507.08270)
  - 🔑 Key: sandboxed RL / dual-channel threat alignment
  - 🤖 Agent Type: Tool Agents
  - 📖 TLDR: Jointly aligns responses to malicious user instructions and compromised-tool outputs using structured reasoning, a benign/malicious/sensitive taxonomy, sandboxed execution, and fine-grained rewards.
  - 📅 Date: Jul 11, 2025 / preprint

- [SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning](https://aclanthology.org/2026.acl-long.522/)
  - 🔑 Key: capability alignment / proactive tool filtering / RL
  - 🤖 Agent Type: MCP Agents / Tool Agents
  - 📖 TLDR: Uses an environment-grounded world model to predict downstream risk, restrict hazardous tool acquisition, and intervene before excessive agent power turns small errors into consequential actions.
  - 📅 Date: Jul 2026 / ACL 2026

- [Aligned LLMs Are Not Aligned Browser Agents](https://openreview.net/forum?id=NsFZZU9gvk)
  - 🔑 Key: browser-action evaluation / alignment gap
  - 🤖 Agent Type: Browser Agents / Web Agents
  - 📖 TLDR: BrowserART shows that chat-level refusal alignment does not reliably transfer to browser actions, providing 100 harmful behaviors that can support agent-specific red-teaming and alignment data construction.
  - 📅 Date: 2024 / ICLR 2025

- [OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows](https://aclanthology.org/2026.acl-long.431/)
  - 🔑 Key: action validation / runtime defense / benchmark
  - 🤖 Agent Type: Mobile GUI Agents / Computer-Use Agents
  - 📖 TLDR: Combines a formal verifier for explicit system violations with a VLM contextual judge for semantic risks, checking mobile actions at both step and trajectory levels in a dynamic sandbox.
  - 📅 Date: Jul 2026 / ACL 2026

##### 2.2.3 Planning, Reasoning, and Trajectory Alignment

- [On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment](https://arxiv.org/abs/2605.11882)
  - 🔑 Key: trajectory-level alignment / on-policy self-evolution
  - 🤖 Agent Type: Tool Agents / Long-Horizon Agents
  - 📖 TLDR: FATE converts verifier-scored failed trajectories into repair supervision and applies Pareto-aware policy optimization to improve security, utility, over-refusal control, and trajectory validity together.
  - 📅 Date: May 12, 2026 / preprint

- [Think Twice Before You Act: Enhancing Agent Behavioral Safety with Thought Correction](https://arxiv.org/abs/2505.11063)
  - 🔑 Key: thought alignment / inference-time correction
  - 🤖 Agent Type: ReAct Agents / Tool Agents
  - 📖 TLDR: Thought-Aligner detects and rewrites unsafe intermediate thoughts before they determine the next action, steering planning trajectories without modifying the underlying agent.
  - 📅 Date: May 2025 / preprint

- [GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://proceedings.mlr.press/v267/xiang25a.html)
  - 🔑 Key: safety planning / policy-to-code verification
  - 🤖 Agent Type: Web Agents / Domain Agents
  - 📖 TLDR: A dedicated guard agent translates natural-language safety requirements into a task plan and executable guardrail code, using retrieved prior experiences to deterministically validate target-agent actions.
  - 📅 Date: Jul 2025 / ICML 2025

##### 2.2.4 Memory-Based Alignment

- [SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety](https://arxiv.org/abs/2605.05704)
  - 🔑 Key: safety memory / training-free guardrail
  - 🤖 Agent Type: Tool Agents
  - 📖 TLDR: Stores context-aware defense rules in a hierarchical local memory and evolves the structure through entropy-based splitting and merging, dynamically injecting precise rules to reduce both harmful compliance and over-refusal.
  - 📅 Date: May 7, 2026 / ICML 2026

##### 2.2.5 Preference and Value Alignment

- [Aligning LLM Agents by Learning Latent Preference from User Edits](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f75744612447126da06767daecce1a84-Abstract-Conference.html)
  - 🔑 Key: personalized preference alignment / edit feedback
  - 🤖 Agent Type: Writing Assistants / Interactive Language Agents
  - 📖 TLDR: PRELUDE and CIPHER infer interpretable, context-dependent user preferences from historical edits and retrieve them to guide future generation without per-user model fine-tuning.
  - 📅 Date: Dec 2024 / NeurIPS 2024

- [Moral Alignment for LLM Agents](https://arxiv.org/abs/2410.01639)
  - 🔑 Key: value alignment / intrinsic-reward RL
  - 🤖 Agent Type: Decision-Making Agents / Multi-Agent Environments
  - 📖 TLDR: Encodes deontological and utilitarian values as explicit intrinsic rewards for reinforcement learning, offering a more transparent alternative to preference-only alignment and demonstrating cross-environment transfer.
  - 📅 Date: May 11, 2025 / preprint
<a id="trustworthy-agent-architecture"></a>
#### 2.3 Trustworthy Agent Architecture

System-level designs for safer agents, including permission systems, least-privilege tool access, sandboxing, human approval workflows, multi-agent oversight, memory isolation, secure RAG pipelines, runtime monitors, policy engines, and incident recovery.
- [StruQ: Defending Against Prompt Injection with Structured Queries](https://arxiv.org/pdf/2402.06363)
  - 🔑 Key: defense
  - 🤖 Agent Type: LLM Applications / RAG Systems / Tool Agents
  - 📖 TLDR: This paper proposes StruQ, a defense against prompt injection that separates trusted instructions from untrusted data using structured queries. Instead of relying only on delimiters or post-hoc detection, StruQ changes the input format so that the model receives the application instruction and external data in separate fields. The model is then instruction-tuned to follow only the instruction field and treat the data field as content, even when the data contains malicious instructions such as "ignore previous instructions." This makes prompt injection harder because injected commands inside external data are no longer treated as valid instructions.
  - 📅 Date: Feb 2024

- [Prompt Flow Integrity to Prevent Privilege Escalation in LLM Agents](https://arxiv.org/abs/2503.15547)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: Prompt Flow Integrity protects LLM agents from privilege escalation by tracking how trusted and untrusted prompts or tool outputs influence later tool calls. It prevents untrusted content from controlling high-privilege actions or crossing privilege boundaries.
  - 📅 Date: Mar 2025

- [Permissive Information Flow Control for Large Language Model Agents](https://arxiv.org/pdf/2410.03055)
  - 🔑 Key: defense
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: Permissive IFC applies information flow control to LLM agents. It tracks how untrusted data propagates through prompts, tool outputs, parameters, and actions, providing a principled way to constrain unsafe information flows while preserving useful agent behavior.
  - 📅 Date: Mar 2025

<a id="VLM-agent"></a>
### 3. VLM agent

<a id="computer-use-agents"></a>
#### 3.1 Normal Agents

- [VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents](https://arxiv.org/abs/2506.02456)
  - 🔑 Key: benchmark
  - 🤖 Agent Type: Web Agent
  - 📖 TLDR: Computer-Use Agents (CUAs) with full system access enable powerful task automation but pose significant security and privacy risks due to their ability to manipulate files, access user data, and execute arbitrary commands. While prior work has focused on browser-based agents and HTML-level attacks, the vulnerabilities of CUAs remain underexplored. In this paper, we investigate Visual Prompt Injection (VPI) attacks, where malicious instructions are visually embedded within rendered user interfaces, and examine their impact on both CUAs and Browser-Use Agents (BUAs).
  - 📅 Date: Mar 2026

<a id="embodied-agents"></a>
#### 3.2 Embodied Agents

- [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)
  - 🔑 Key: benchmark
  - 🤖 Agent Type: Embodied Agent
  - 📖 TLDR: A foreseeable issue is that those embodied agents can also flawlessly execute some hazardous tasks, potentially causing damages in the real world. Existing benchmarks predominantly overlook critical safety risks, focusing solely on planning performance, while a few evaluate LLMs' safety awareness only on non-interactive image-text data. To address this gap, we present SafeAgentBench for safety-aware task planning of embodied LLM agents in interactive simulation environments, covering both explicit and implicit hazards.
  - 📅 Date: Oct 2025 
  
- [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2503.04392)
  - 🔑 Key: benchmark
  - 🤖 Agent Type: Embodied Agent
  - 📖 TLDR: The integration of vision-language models (VLMs) is driving a new generation of embodied agents capable of operating in human-centered environments. However, as deployment expands, these systems face growing safety risks, particularly when executing hazardous instructions. Current safety evaluation benchmarks remain limited: they cover only narrow scopes of hazards and focus primarily on final outcomes, neglecting the agent's full perception-planning-execution process and thereby obscuring critical failure modes. 
  - 📅 Date: Oct 2025 

- [BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://arxiv.org/abs/2407.20242)
  - 🔑 Key: attack
  - 🤖 Agent Type: Embodied Agent
  - 📖 TLDR: Embodied AI represents systems where AI is integrated into physical entities. Large Language Model (LLM), which exhibits powerful language understanding abilities, has been extensively employed in embodied AI by facilitating sophisticated task planning. However, a critical safety issue remains overlooked: could these embodied LLMs perpetrate harmful behaviors? In response, we introduce BadRobot, a novel attack paradigm aiming to make embodied LLMs violate safety and ethical constraints through typical voice-based user-system interactions. 
  - 📅 Date: Jun 2026

### 4. Multi-Agent Safety & Alignment

Research focused specifically on safety failures, attacks, guardrails, resilience, oversight, and alignment that emerge when multiple LLM agents communicate, delegate, debate, or act as a coordinated system. Peer-reviewed papers and preprints are labeled separately.

#### 4.1 Evaluation, Failure Analysis & Attacks

- [Why Do Multi-Agent LLM Systems Fail?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)
  - 🔑 Key: benchmark / failure taxonomy / evaluation
  - 🤖 Agent Type: Multi-Agent LLM Systems / Collaborative Agents
  - 📖 TLDR: Introduces MAST, a taxonomy of 14 failure modes, and MAST-Data, a dataset of more than 1,600 annotated traces from seven multi-agent frameworks. The analysis isolates system-design, inter-agent misalignment, and task-verification failures that aggregate task scores often hide.
  - 📅 Date: Dec 2025 / NeurIPS D&B 2025

- [Agents Under Siege: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks](https://aclanthology.org/2025.acl-long.476/)
  - 🔑 Key: attack / red teaming
  - 🤖 Agent Type: Communicative Agents / Distributed Multi-Agent Systems
  - 📖 TLDR: Optimizes how adversarial prompts are distributed across latency- and bandwidth-constrained communication graphs. Its permutation-invariant attack bypasses distributed safeguards and outperforms conventional attacks by up to 7×, while Llama-Guard and PromptGuard variants fail to stop it reliably.
  - 📅 Date: Jul 2025 / ACL 2025

- [Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://aclanthology.org/2025.findings-acl.349/)
  - 🔑 Key: attack / red teaming / benchmark
  - 🤖 Agent Type: Communicative Agents / Multi-Agent Frameworks
  - 📖 TLDR: Proposes Agent-in-the-Middle (AiTM), where an adversarial agent intercepts and rewrites inter-agent messages rather than directly compromising model weights. Evaluation across frameworks, topologies, and applications shows that manipulating the communication layer can compromise the full system.
  - 📅 Date: Jul 2025 / Findings of ACL 2025

- [LLM-based Multi-Agents System Attack via Continuous Optimization with Discrete Efficient Search](https://openreview.net/forum?id=ED5diyzc1C)
  - 🔑 Key: attack / jailbreak propagation
  - 🤖 Agent Type: Multi-Agent LLM Systems / Guarded Agent Pipelines
  - 📖 TLDR: Introduces CODES, a token-level optimization method that plants a self-replicating jailbreak through one intervention on one agent. The malicious prompt propagates across the collaboration graph and can bypass multi-level safeguard modules.
  - 📅 Date: Oct 2025 / COLM 2025

- [TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems](https://arxiv.org/abs/2511.05269)
  - 🔑 Key: benchmark / adversarial robustness
  - 🤖 Agent Type: Multi-Agent LLM Systems
  - 📖 TLDR: Provides a dedicated benchmark for adversarial risks in multi-agent LLM systems, measuring how attacks introduced through agents or their messages propagate across different collaboration structures and degrade collective decisions.
  - 📅 Date: Nov 7, 2025 / preprint

- [Exposing Weak Links in Multi-Agent Systems under Adversarial Prompting](https://arxiv.org/abs/2511.10949)
  - 🔑 Key: security evaluation / framework / metric
  - 🤖 Agent Type: Centralized / Decentralized / Hybrid Multi-Agent Systems
  - 📖 TLDR: Presents SafeAgents and the design-aware DHARMA metric to locate where harmful tasks slip through multi-agent pipelines. It links security failures to atomic delegation that hides intent, missing planner fallbacks, and stratified plans executed without safety re-evaluation.
  - 📅 Date: Nov 14, 2025 / AAMAS SE 2026

- [Attack the Messages, Not the Agents: A Multi-round Adaptive Stealthy Tampering Framework for LLM-MAS](https://ojs.aaai.org/index.php/AAAI/article/view/40224)
  - 🔑 Key: communication attack / stealthy tampering
  - 🤖 Agent Type: Communicative Agents / LLM Multi-Agent Systems
  - 📖 TLDR: Proposes MAST, an adaptive attack policy trained with Monte Carlo Tree Search and Direct Preference Optimization to tamper with inter-agent messages over multiple rounds while preserving semantic and embedding similarity for stealth.
  - 📅 Date: Mar 2026 / AAAI 2026

- [Conjunctive Prompt Attacks in Multi-Agent LLM Systems](https://aclanthology.org/2026.acl-long.1577/)
  - 🔑 Key: compositional attack / routing attack
  - 🤖 Agent Type: Routed Multi-Agent Systems / Remote Agents
  - 📖 TLDR: Splits an attack across a benign-looking user trigger and a hidden template in a compromised remote agent. Harm appears only when routing composes the fragments, defeating defenses that inspect messages or components independently.
  - 📅 Date: Jul 2026 / ACL 2026

- [Web Fraud Attacks Against LLM-Driven Multi-Agent Systems](https://aclanthology.org/2026.findings-acl.686/)
  - 🔑 Key: web attack / URL manipulation
  - 🤖 Agent Type: Web-Connected Multi-Agent Systems
  - 📖 TLDR: Defines 12 web-fraud attacks based on homoglyphs, nested paths, parameter obfuscation, and related URL structures. The attacks exploit trust in links across several multi-agent architectures while requiring little prompt engineering.
  - 📅 Date: Jul 2026 / Findings of ACL 2026

- [Shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems](https://ojs.aaai.org/index.php/AAAI/article/view/41134)
  - 🔑 Key: attack / defense / code security
  - 🤖 Agent Type: Multi-Agent Software Engineering Systems / Code Agents
  - 📖 TLDR: Introduces IMBIA for hiding malicious behavior inside apparently benign software under malicious-user and malicious-agent threat models, then evaluates a targeted Adv-IMBIA defense on ChatDev, MetaGPT, and AgentVerse.
  - 📅 Date: Mar 2026 / AAAI 2026 Special Track on AI Alignment

- [LieCraft: A Multi-Agent Framework for Evaluating Deceptive Capabilities in Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/41116)
  - 🔑 Key: deception evaluation / sandbox
  - 🤖 Agent Type: Social Agents / Hidden-Role Multi-Agent Systems
  - 📖 TLDR: Builds a long-horizon multiplayer hidden-role sandbox for measuring strategic deception under varying ethical alignments, goals, and oversight conditions instead of relying on short, single-agent deception prompts.
  - 📅 Date: Mar 2026 / AAAI 2026 Special Track on AI Alignment

- [The Deliberative Illusion: Diagnosing Factual Attrition and Stance Homogenization in Multi-Agent LLM Deliberation](https://arxiv.org/abs/2606.03032)
  - 🔑 Key: evaluation / misinformation / deliberation failure
  - 🤖 Agent Type: Debate Agents / Deliberative Multi-Agent Systems
  - 📖 TLDR: Introduces DelibTrace to track issue-critical facts through multi-agent discussion. It finds that agents may converge while losing up to 72% of critical facts, and that one malicious participant can exploit the shrinking shared context to inject misinformation.
  - 📅 Date: Jun 2, 2026 / preprint

- [From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails](https://arxiv.org/abs/2606.14517)
  - 🔑 Key: guardrail attack / denial of service
  - 🤖 Agent Type: Web / Desktop / Code / Multi-Agent Systems
  - 📖 TLDR: Crafts payloads that trap reasoning-based guardrails in long loops, achieving large token and latency amplification. In multi-agent deployments, a single poisoned document can exhaust shared guardrail capacity and starve other agents.
  - 📅 Date: Jun 12, 2026 / preprint

#### 4.2 Guardrails, Detection & Resilience

- [On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents](https://proceedings.mlr.press/v267/huang25ay.html)
  - 🔑 Key: defense / resilience / oversight
  - 🤖 Agent Type: Collaborative Multi-Agent Systems / Faulty or Malicious Agents
  - 📖 TLDR: Compares collaboration structures under faulty agents and proposes Challenger and Inspector agents that challenge, review, and repair peer messages. The Inspector recovers up to 96.4% of injected errors, while hierarchical structures are substantially more resilient than common alternatives.
  - 📅 Date: Jul 2025 / ICML 2025

- [GUARDIAN: Safeguarding LLM Multi-Agent Collaborations with Temporal Graph Modeling](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bc795afae289ed465a65a3b4b1f4eb7-Abstract-Conference.html)
  - 🔑 Key: guardrail / anomaly detection / mitigation
  - 🤖 Agent Type: Collaborative Agents / Agent-to-Agent Systems
  - 📖 TLDR: Models multi-agent conversations as temporal attributed graphs to detect anomalous agents and edges associated with hallucination amplification or injected-error propagation. Its unsupervised encoder-decoder supports incremental monitoring as collaborations evolve.
  - 📅 Date: Dec 2025 / NeurIPS 2025

- [BlindGuard: Safeguarding LLM-based Multi-Agent Systems under Unknown Attacks](https://arxiv.org/abs/2508.08127)
  - 🔑 Key: unsupervised defense / malicious-agent detection
  - 🤖 Agent Type: Multi-Agent Systems / Communicative Agents
  - 📖 TLDR: Learns normal individual, neighborhood, and global interaction patterns without malicious-agent labels, then uses corruption-guided contrastive learning to detect prompt injection, memory poisoning, and tool attacks across unseen threat types and topologies.
  - 📅 Date: Aug 11, 2025 / preprint

- [QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems](https://arxiv.org/abs/2512.16279)
  - 🔑 Key: multi-agent guardrail / formal policy / runtime enforcement
  - 🤖 Agent Type: Tool Agents / Multi-Agent Systems / Guard Teams
  - 📖 TLDR: Compiles natural-language safety policies into machine-checkable sequents and enforces them online with four specialized guard agents: a state tracker, policy verifier, threat watcher, and referee. The design provides trajectory-level allow/deny decisions with auditable rationales.
  - 📅 Date: Dec 18, 2025 / preprint

- [Explainable and Fine-Grained Safeguarding of LLM Multi-Agent Systems via Bi-Level Graph Anomaly Detection](https://aclanthology.org/2026.acl-long.1407/)
  - 🔑 Key: guardrail / explainable anomaly detection
  - 🤖 Agent Type: Multi-Agent Systems / Malicious Agents
  - 📖 TLDR: XG-Guard combines sentence- and token-level graph representations with a theme-aware detector, identifying malicious agents while attributing the lexical cues responsible for each anomaly score.
  - 📅 Date: Jul 2026 / ACL 2026

- [SafeSieve: From Heuristics to Experience in Progressive Pruning for LLM-based Multi-Agent Communication](https://ojs.aaai.org/index.php/AAAI/article/view/40236)
  - 🔑 Key: communication guardrail / topology pruning / robustness
  - 🤖 Agent Type: LLM Multi-Agent Systems
  - 📖 TLDR: Progressively prunes weak or risky communication links using semantic initialization, experience feedback, and structure-preserving clustering. It reduces tokens and deployment cost while showing only a small accuracy drop under prompt injection.
  - 📅 Date: Mar 2026 / AAAI 2026

- [ResMAS: Resilience Optimization in LLM-based Multi-agent Systems](https://ojs.aaai.org/index.php/AAAI/article/view/40824/)
  - 🔑 Key: resilience / topology optimization / prompt optimization
  - 🤖 Agent Type: Distributed Multi-Agent Systems
  - 📖 TLDR: Proactively designs resilient multi-agent systems by training a reward model and topology generator, then optimizing each agent's prompt according to its communication neighborhood. The method improves tolerance to agent failures and generalizes to new tasks and models.
  - 📅 Date: Mar 2026 / AAAI 2026

- [Beyond the Prompt: Log-Based Threat Detection and Attribution for Multi-Agent LLMs](https://doi.org/10.1016/j.ipm.2026.104768)
  - 🔑 Key: monitoring / threat attribution / audit
  - 🤖 Agent Type: Tool-Using Multi-Agent Systems
  - 📖 TLDR: Proposes ALTEDA, which analyzes execution logs rather than isolated prompts to detect and attribute instruction hijacking, retrieval poisoning, and tool redirection that unfold across agent-to-agent interactions.
  - 📅 Date: 2026 / Information Processing & Management

#### 4.3 Safety Alignment, Oversight & Governance

- [The Alignment Waltz: Jointly Training Agents to Collaborate for Safety](https://arxiv.org/abs/2510.08240)
  - 🔑 Key: safety alignment / multi-agent reinforcement learning
  - 🤖 Agent Type: Conversation Agent / Feedback Agent
  - 📖 TLDR: WaltzRL jointly trains a conversation agent and an adaptive feedback agent as a positive-sum safety game. The feedback agent repairs unsafe or over-refusing responses instead of simply rejecting them, improving both harmlessness and helpfulness.
  - 📅 Date: Oct 9, 2025 / preprint

- [AdvEvo-MARL: Shaping Internalized Safety through Adversarial Co-Evolution in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2510.01586)
  - 🔑 Key: adversarial alignment / multi-agent reinforcement learning
  - 🤖 Agent Type: Tool Agents / Multi-Agent Task Systems
  - 📖 TLDR: Co-evolves attacker agents that generate increasingly strong jailbreaks and defender task agents that internalize resistance during training. It avoids a separate guard-agent bottleneck while keeping attack success below 20% in the reported settings.
  - 📅 Date: Oct 2, 2025 / preprint

- [Multiple LLM Agents Debate for Equitable Cultural Alignment](https://arxiv.org/abs/2505.24671)
  - 🔑 Key: cultural alignment / multi-agent debate / fairness
  - 🤖 Agent Type: Debate Agents / Social Reasoning Agents
  - 📖 TLDR: Uses debate and adaptive self-reflection between heterogeneous LLM agents to improve cultural-norm reasoning across 75 countries. The approach improves both aggregate accuracy and parity across cultural groups over single-model baselines.
  - 📅 Date: May 30, 2025 / preprint

- [DialogGuard: Multi-Agent Psychosocial Safety Evaluation of Sensitive LLM Responses](https://arxiv.org/abs/2512.02282)
  - 🔑 Key: multi-agent oversight / safety evaluation / psychosocial risk
  - 🤖 Agent Type: Judge Agents / Debate Agents / Voting Agents
  - 📖 TLDR: Compares single-agent scoring, dual-agent correction, multi-agent debate, and majority voting for privacy, discrimination, manipulation, psychological harm, and abuse. Dual-agent correction and voting best balance human agreement, accuracy, and robustness.
  - 📅 Date: Dec 1, 2025 / preprint

- [TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems](https://doi.org/10.1016/j.aiopen.2026.02.006)
  - 🔑 Key: survey / governance / trustworthy architecture
  - 🤖 Agent Type: Agentic Multi-Agent Systems
  - 📖 TLDR: Extends Trust, Risk, and Security Management to multi-agent LLM deployments, organizing controls around explainability, ModelOps, security, privacy, and lifecycle governance and outlining a roadmap for accountable deployment.
  - 📅 Date: 2026 / AI Open

## Contributing

Pull requests are welcome. Please add papers using the following format:

```md
- [title](paper link)
    - 🔑 Key: e.g., attack/defense/evaluation/benchmark/survey/position
    - 🤖 Agent Type: e.g., Web Agent/Tool Agent/Communicative Agent/OS Agent/Embodied Agent
    - 📖 TLDR: Brief summary of the paper.
    - 📅 Date: e.g., Jan 01, 2025
```
