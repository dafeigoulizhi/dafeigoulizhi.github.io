Agentic Search
==============

*Last updated: 2026-02-28*

Introduction
------------

Agentic search refers to the paradigm where large language models (LLMs) are empowered to autonomously plan, execute, and refine search strategies—going beyond passive retrieval to actively interact with information environments. This literature review surveys key works that shape the field.

Core Foundations
----------------

**1. ReAct: Synergizing Reasoning and Acting in Language Models**
   *Yao et al., 2022*
   
   `[Paper] <https://arxiv.org/abs/2210.03629>`_ | `[Code] <https://react-lm.github.io>`_
   
   ReAct (Reason + Act) pioneered the idea of interleaving reasoning traces with actionable steps. By prompting LLMs to generate thought sequences followed by actions (e.g., API calls, tool usage), it demonstrated that reasoning can guide exploration, and actions can provide new information to fuel further reasoning.

**2. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**
   *Wei et al., 2022*
   
   `[Paper] <https://arxiv.org/abs/2201.11903>`_
   
   Though not originally about agents, CoT established that prompting LLMs to output intermediate reasoning steps significantly improves complex task performance. This became the foundation for many agentic systems.

**3. Toolformer: Language Models Can Teach Themselves to Use Tools**
   *Schick et al., 2023*
   
   `[Paper] <https://arxiv.org/abs/2302.04761>`_ | `[Code] <https://github.com/lucidrains/toolformer-pytorch>`_
   
   Toolformer introduced self-supervised learning for tool adoption. The model learns to decide *when* to call external tools (calculators, search engines, calendars) and formats inputs/outputs accordingly—laying groundwork for tool-augmented agents.

Agent Architectures
-------------------

**4. Generative Agents: Interactive Simulacra of Human Behavior**
   *Park et al., 2023 (Stanford)*
   
   `[Paper] <https://arxiv.org/abs/2304.03442>`_ | `[Project] <https://buildyouragent.github.io>`_
   
   This landmark paper introduced 25 autonomous agents living in a virtual town. Each agent has memory streams and reacts to others in real-time. It showcases emergent social behaviors and long-horizon planning—key for complex search/retrieval scenarios.

**5. AgentBench: Evaluating LLMs as Agents**
   *Liu et al., 2023*
   
   `[Paper] <https://arxiv.org/abs/2310.02660>`_ | `[GitHub] <https://github.com/AGI-Eval/AgentBench>`_
   
   AgentBench created a multi-environment benchmark (OS, DB, Knowledge Graph, etc.) to systematically evaluate LLM agents. It revealed significant gaps between models and highlighted which capabilities matter most for agentic performance.

**6. Reflexion: Language Agents with Verbal Reinforcement Learning**
   *Shinn et al., 2023*
   
   `[Paper] <https://arxiv.org/abs/2303.11366>`_ | `[GitHub] <https://github.com/nicklashansen/reflexion>`_
   
   Reflexion adds a self-reflection mechanism: after failed tasks, agents articulate what went wrong in language, then retry with this feedback. This "verbal reinforcement" improves success rates without gradient updates.

**7. AutoGPT & BabyAGI: Early Autonomous Agent Prototypes**
   *Significant AI Agent Projects, 2023*
   
   `[AutoGPT] <https://github.com/Significant-Gravitas/AutoGPT>`_ | `[BabyAGI] <https://github.com/yoheinakajima/babyagi>`_
   
   These open-source projects demonstrated the power of LLM-driven loops: generate a task list, execute each step, re-evaluate, and iterate. While not peer-reviewed, they influenced how practitioners think about agentic search.

Search & Retrieval Focus
------------------------

**8. Self-Discover: LLMs Self-compose Reasoning Structures**
   *Zhou et al., 2024*
   
   `[Paper] <https://arxiv.org/abs/2310.05721>`_ | `[GitHub] <https://github.com/htw/prover9>`_ (project page)
   
   Self-Discover allows LLMs to *find* their own reasoning structures (like CoT, ReAct) for a given task, rather than being prompted with a fixed approach. This meta-cognitive ability is crucial for adaptive search strategies.

**9. Search-Augmented Language Models (SALM)**
   *Various works, 2023-2024*
   
   - **RETRO** (DeepMind): `[Paper] <https://arxiv.org/abs/2112.04426>`_
   - **In-Context RAG**: Dynamically pulling relevant documents during generation
   
   These are the technical backbone for agentic search systems.

**10. Agentic RAG Systems**
    *Industry & Research, 2024*
    
    `[LangChain Agents] <https://python.langchain.com/docs/modules/agents>`_ | `[LlamaIndex Query Engines] <https://docs.llamaindex.ai/en/stable/module_guides/querying/agents/>`_
    
    Recent systems combine RAG (Retrieval-Augmented Generation) with agentic loops—allowing the model to decide *what* to retrieve, *when* to re-retrieve, and *how* to synthesize across multiple sources.

Datasets & Benchmarks
---------------------

As the field matures, several benchmarks have been introduced to evaluate agents' search and reasoning capabilities:

**SimpleQA (OpenAI, 2024)**

`[Paper] <https://arxiv.org/abs/2408.03314>`_ | `[GitHub] <https://github.com/openai/simple-eval>`_

- **Focus**: Evaluating factuality in short-form answers
- **Key characteristics**:
  - Questions require factual, specific answers
  - Designed to test whether models know what they don't know
  - Measures calibration: confidence vs. accuracy
  - Strict correctness criteria — minor errors lead to wrong answers
  
**SimpleQA Verified (DeepMind, 2025)**

`[Paper] <https://arxiv.org/abs/2501.09326>`_

- **Focus**: Addressing reliability issues in SimpleQA
- **Improvements over SimpleQA**:
  - All answers verified by human annotators with access to Wikipedia
  - Stricter answer validation criteria
  - Better coverage of uncertainty scenarios
  - More balanced difficulty distribution
  
**DeepSearchQA (DeepMind, 2025)**

`[Paper] <https://arxiv.org/abs/2503.09517>`_

- **Focus**: Multi-step search and reasoning over long contexts
- **Improvements over SimpleQA Verified**:
  - Requires **multiple search steps** to gather information
  - Questions demand synthesis across multiple sources
  - Tests **planning** and **iterative refinement** of search strategy
  - Includes questions where initial search queries need refinement based on intermediate results
  - Longer answer contexts (multi-sentence vs. short phrases)

Evolution Summary
"""""""""""""""""

- **SimpleQA** → established the baseline for factual QA
- **SimpleQA Verified** → improved reliability and annotation quality
- **DeepSearchQA** → extended to **agentic, multi-step search** scenarios

This progression mirrors the shift from passive retrieval to active, planning-based agentic search.

Future Directions
-----------------

- **Multi-agent collaboration**: Multiple agents debating and partitioning search tasks
- **Continuous learning**: Agents that improve their search strategies over time
- **Safety & alignment**: Ensuring agentic search doesn't produce harmful or misleading outputs

---

*This is a living document. More papers will be added as the field evolves.*
