# LLM Agent Safety

A curated collection of research papers, benchmarks, defenses, training methods, and system designs for LLM agent safety.

This repository focuses on safety issues that arise when large language models act as agents: following long-horizon goals, using tools, reading untrusted content, retrieving or storing memory, interacting with users, and operating inside larger software systems.

## Table of Contents

- [Papers](#papers)
  - [1. Safety Evaluation & Benchmarking](#safety-evaluation--benchmarking)
  - [2. Safety Defense](#safety-defense)
    - [2.1 Guardrails](#guardrails)
      - [2.1.1 Input Guardrail](#input-guard-rail)
      - [2.1.2 Planner Guardrail](#planner-guard-rail)
      - [2.1.3 Retrieval / Memory Guardrail](#retrieval-memory-guard-rail)
      - [2.1.4 Tool Execution Guardrail](#tool-execution-guard-rail)
      - [2.1.5 Output & Audit Guardrail](#output-audit-guard-rail)
    - [2.2 Safety Alignment Training](#safety-alignment-training)
    - [2.3 Trustworthy Agent Architecture](#trustworthy-agent-architecture)
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
#### 2.2 Safety Alignment Training

Papers on making the underlying model or agent policy safer through supervised fine-tuning, RLHF/RLAIF, constitutional methods, refusal training, harmlessness training, tool-use training, adversarial training, and robustness training.

- [ToolSafety: A Comprehensive Dataset for Enhancing Safety in LLM-Based Agent Tool Invocations](https://huggingface.co/datasets/jinjinyien/ToolSafety)
  - 🔑 Key: training / dataset
  - 🤖 Agent Type: Tool Agents / LLM Agents
  - 📖 TLDR: ToolSafety introduces a safety fine-tuning dataset for tool-using LLM agents, covering direct harm, indirect harm, and multi-step tool interaction scenarios. Fine-tuning models on ToolSafety improves their ability to maintain safety during complex tool invocation while preserving helpfulness.
  - 📅 Date: Nov 2025 / EMNLP 2025

- [AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security](https://arxiv.org/abs/2605.29801)
  - 🔑 Key: training / defense / architecture
  - 🤖 Agent Type: LLM Agents / Tool Agents / Open-world Agents
  - 📖 TLDR: AgentDoG 1.5 proposes a lightweight and scalable alignment framework for AI agent safety. It updates an agent safety taxonomy, builds a taxonomy-guided data engine with influence-function purification, trains compact safety models with around 1k samples, and deploys them as online guardrails for real-time agent safety moderation.
  - 📅 Date: May 28, 2026

- [Aligned LLMs Are Not Aligned Browser Agents](https://openreview.net/forum?id=NsFZZU9gvk)
  - 🔑 Key: benchmark / training data
  - 🤖 Agent Type: Browser Agents / Web Agents
  - 📖 TLDR: BrowserART is a red-teaming suite for browser agents that shows refusal-aligned chat models can still take harmful actions in browser settings. It is useful as both an evaluation benchmark and a source of harmful browser-agent cases for safety alignment training.
  - 📅 Date: 2024 / ICLR 2025
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

## Contributing

Pull requests are welcome. Please add papers using the following format:

```md
- [title](paper link)
    - 🔑 Key: e.g., attack/defense/evaluation/benchmark/survey/position
    - 🤖 Agent Type: e.g., Web Agent/Tool Agent/Communicative Agent/OS Agent
    - 📖 TLDR: Brief summary of the paper.
    - 📅 Date: e.g., Jan 01, 2025
```
