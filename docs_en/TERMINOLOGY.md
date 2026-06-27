# English Terminology Draft

This file is the working glossary for the English edition of `ai-programming-book`.

Its purpose is not to force artificial one-to-one translation. Its purpose is to keep the book's **conceptual vocabulary** stable across chapters while still allowing natural English writing.

## How to use this glossary

- Prefer the **recommended rendering** unless the local chapter context clearly requires a narrower or broader wording.
- Do not mechanically translate Chinese surface forms if the English technical community already has a more natural term.
- Keep the **same core concept** stable across chapters, especially for high-frequency architectural ideas.
- If a chapter introduces a new major concept, add it here after the translation is stable enough to reuse.

## Style principles for terminology

- Favor **natural technical English** over literal translation.
- Favor **conceptual consistency** over local rhetorical variation.
- Favor **reader comprehension** over preserving Chinese phrasing.
- Avoid turning principle-level concepts into product-marketing language.

---

## 1. Book-level framing

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| AI 编程 | AI coding | AI programming | Use `AI coding` as the book's default umbrella term because it matches the manuscript's framing and current practitioner language more closely. `AI programming` can appear in a subtitle or where broader formality is needed. |
| 第一性原理 | first principles | fundamental principles | Prefer `first principles` for the title and the book's core framing. |
| 原理书 | principles book | theory book | `principles book` keeps the engineering tone better than `theory book`. |
| 判断力 | engineering judgment | judgment ability | Often better rendered as `engineering judgment`, `architectural judgment`, or `decision-making judgment` depending on the chapter. |
| 问题链 | chain of questions | problem chain | Prefer `chain of questions` when describing chapter-to-chapter progression. In some contexts `question chain` is acceptable, but `problem chain` sounds unnatural in English. |
| 运行真相 | operational reality | runtime truth | `runtime truth` feels too literal. Use `operational reality` or rewrite the chapter title more naturally. |
| 工程权衡 | engineering trade-offs | engineering balance | Standard engineering wording is `trade-offs`. |
| 架构选型 | architecture selection | architectural choice / architecture decisions | Usually rewrite at sentence level as `architectural choice`, `architecture decision`, or `design choice`. |
| 边界 | limits / boundaries | border | Use `boundaries` for design scope and `limits` for hard capability ceilings. |

---

## 2. Model and interaction fundamentals

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| 大模型 | large model / large language model / LLM | big model | Use `large language model` or `LLM` when the context is specifically language-model behavior. Use `large model` only if the text intentionally stays broader. |
| Token 化 | tokenization | token splitting | `tokenization` is the standard term. |
| 注意力机制 | attention mechanism | attention system | Standard ML wording. |
| 自回归生成 | autoregressive generation | self-regressive generation | Standard wording. |
| 温度 | temperature | randomness level | Keep `temperature`; explain if needed for readability. |
| 采样 | sampling | token picking | Standard wording. |
| 指令遵循 | instruction following | command following | `instruction following` is the accepted model term. |
| 上下文窗口 | context window | context frame | Standard term. |
| 多轮对话 | multi-turn conversation | multiple-round dialogue | `multi-turn conversation` is more natural. |
| System Prompt | system prompt | system instruction set | Keep the established English term lowercase in running prose unless style requires otherwise. |
| Few-shot | few-shot prompting | few-shot examples | Use `few-shot prompting` when naming the technique. |
| Chain-of-Thought | chain-of-thought reasoning | step-by-step prompting | Use the canonical term when discussing the technique specifically. |
| Lost in the Middle | Lost in the Middle | middle-attention decay | Keep the recognized English phrase. |
| 概率预测 | probabilistic prediction | probability guessing | `probabilistic prediction` preserves the technical tone. |

---

## 3. Agent systems and execution

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| Agent | Agent | intelligent agent (overused) | Keep `Agent` capitalized only when treated as a named concept; otherwise lowercase in prose is fine. |
| Agentic | agentic | autonomous-style | Preserve `agentic` where the manuscript is discussing the concept as such. |
| 从问答到执行 | from question answering to execution | from Q&A to doing things | Rewrite naturally in chapter titles and section headings. |
| 执行循环 | execution loop | action cycle | `execution loop` is the better default. |
| 工具调用 | tool calling | function invocation | Use `tool calling` as the umbrella concept. Reserve `function calling` for the specific mechanism. |
| Function Calling | function calling | tool calling | Keep separate from `tool calling`: function calling is a mechanism, tool calling is the broader action. |
| ReAct 范式 | the ReAct pattern | ReAct paradigm | `pattern` usually reads better than `paradigm` in this book's tone. |
| 推理 | reasoning | thinking | Use `reasoning` in technical contexts; avoid anthropomorphic `thinking` unless the prose deliberately uses quotes or rhetorical contrast. |
| 行动 | action / acting | behavior | In `Reasoning + Acting`, keep `acting`. In broader prose, `action` often reads better. |
| 任务规划 | task planning | work planning | Standard term. |
| 任务分解 | task decomposition | task breakdown | Both are acceptable; default to `task decomposition` when discussing system design. |
| 自我反思 | self-reflection | self-thinking | `self-reflection` is more standard in agent literature. |
| 纠错 | error correction / self-correction | fix mistakes | Choose based on context. `self-correction` often works well. |
| 幻觉 | hallucination | fabrication | Use `hallucination` for model behavior. |
| 无限循环 | infinite loop | endless retry | `infinite loop` is the correct engineering phrase. |
| 过度自信 | overconfidence | false confidence | `overconfidence` is more concise. |
| 上下文污染 | context pollution | context contamination | Prefer `context pollution` unless a more formal tone requires `contamination`. |
| 规划失败 | planning failure | planning mistake | Better for system-level discussion. |
| 容错机制 | fault-tolerance mechanisms | error-proof design | Use `fault tolerance` or `fault-tolerance mechanisms`. |
| 回滚策略 | rollback strategy | revert strategy | Standard engineering term is `rollback strategy`. |
| 能力边界 | capability boundaries / capability limits | capability border | Use `capability boundaries` when discussing scope; use `capability limits` when emphasizing hard ceilings. |
| 失败模式 | failure modes | failure patterns | `failure modes` is the standard engineering phrase. |

---

## 4. Protocols, tools, and capability packaging

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| 工具的标准化 | tool standardization | tool normalization | Use `tool standardization`. |
| 工具发现 | tool discovery | tool lookup | Standard systems term. |
| 能力声明 | capability declaration | feature declaration | `capability declaration` is closer to MCP-style wording. |
| 提供方 / 使用方 | provider / consumer | supplier / user side | Use the standard systems pair `provider` and `consumer` where applicable. |
| 传输层 | transport layer | transmission layer | Use `transport layer` in MCP context. |
| Model Context Protocol | Model Context Protocol (MCP) | context model protocol | Keep the canonical full name on first mention, then `MCP`. |
| 预定义的能力包 | packaged capability | predefined capability pack | For chapter titles and conceptual framing, `packaged capability` reads more naturally. |
| Skill | Skill | capability package only | Keep `Skill` as the core term; use `packaged capability` to explain it, not replace it. |
| Prompt Template | prompt template | prompt pattern | Keep the standard product term. |
| 动态加载 | dynamic loading | live injection | `dynamic loading` is the standard phrase. |
| 工具编排 | tool orchestration | tool scheduling | Prefer `tool orchestration`. |
| 工作流定义 | workflow definition | process script | `workflow definition` is stable and neutral. |
| 生命周期 | lifecycle | life cycle | Both are acceptable; use `lifecycle` consistently. |
| 主 Agent | orchestrator agent / main agent | master agent | Avoid `master agent`; prefer `orchestrator agent`. |
| SubAgent | sub-agent / SubAgent | child agent | `sub-agent` is more natural in prose; keep `SubAgent` when mirroring a product or chapter term. |
| 上下文隔离 | context isolation | isolated context | Use `context isolation` for the design principle. |
| 结构化报告 | structured report | formatted summary | `structured report` fits system communication better. |
| 协议化 | protocolization | turning into a protocol | `protocolization` is acceptable in technical prose, but often a sentence-level rewrite reads better. |
| Agent Card | Agent Card | agent profile | Keep the canonical protocol term if discussing A2A. |
| Agent 间互联网 | the internet between agents / agent internet | Agent Internet | This is rhetorical language. Usually rewrite by meaning rather than force a fixed term. |

---

## 5. Memory, context, and token economics

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| 记忆体系 | memory system | memory architecture | Use `memory system` as the default book-level term. `memory architecture` is acceptable when discussing design structure. |
| 工作记忆 | working memory | active memory | Keep the standard term. |
| 短期记忆 | short-term memory | session memory | `short-term memory` is the conceptual layer; `session memory` can be used if the implementation is session-scoped. |
| 长期记忆 | long-term memory | persistent memory | `long-term memory` is the conceptual term; `persistent memory` can describe implementation properties. |
| 记忆写入 | memory write / memory writing | memory save | In prose, `writing to memory` often reads best. |
| 记忆检索 | memory retrieval | recall lookup | Standard phrase. |
| 记忆一致性 | memory consistency | memory coherence | Use `memory consistency` unless the discussion specifically parallels distributed systems coherence. |
| 跨会话记忆 | cross-session memory | multi-session memory | More natural phrasing. |
| 上下文工程 | context engineering | prompt engineering | Keep separate from `prompt engineering`. The book treats them as different levels of abstraction. |
| Token 经济学 | token economics | token cost science | `token economics` is natural and already used in the manuscript. |
| 上下文压缩 | context compression | compressed context | Prefer `context compression`. |
| 摘要压缩 | summarization-based compression | summary compression | Use `summarization-based compression` in explanatory passages; `summary compression` can work in tighter prose. |
| 结构化压缩 | structured compression | schema compression | Use `structured compression` as the broader term. |
| 选择性注入 | selective injection | selective stuffing | Use `selective injection`. |
| Prompt Caching | prompt caching | context caching | Keep the product/industry term `prompt caching`. |
| 输入 Token | input tokens | prompt tokens | Use `input tokens` unless the pricing model specifically says `prompt tokens`. |
| 输出 Token | output tokens | completion tokens | `output tokens` is the safest neutral term. |
| 缓存 Token | cached tokens | cache tokens | Use `cached tokens`. |
| KV Cache | KV Cache | kv-cache / KV-cache | Keep the canonical Transformer term `KV Cache` (capitalized two-word form). Use it only when the prose explicitly discusses the underlying mechanism behind prompt caching; otherwise prefer `prompt caching` for the product-level concept to avoid mixing the mechanism and the feature. |

---

## 6. Knowledge injection and model adaptation

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| 知识注入 | knowledge injection | knowledge feeding | `knowledge injection` matches the current book framing well. |
| 检索增强生成 | retrieval-augmented generation (RAG) | retrieval generation | Always use the canonical full term on first mention, then `RAG`. |
| 向量嵌入 | vector embeddings | vectorized representations | Use `vector embeddings` when referring to the concept broadly. |
| 向量空间 | vector space | embedding space only | Use `vector space` when explaining the geometry, `embedding space` when the context is model embeddings specifically. |
| 分块策略 | chunking strategy | slicing strategy | `chunking strategy` is the accepted RAG term. |
| 微调 | fine-tuning | model tuning | Standard term. |
| 长上下文 | long context | long-context window | Use `long context` generally; use `long-context window` only if the sentence specifically focuses on the window. |
| 私有数据 | private data | internal data only | `private data` is the better umbrella term. `internal data` can be used for company-internal corpora. |
| 检索不到 | retrieval miss | search failure | In failure-mode lists, `retrieval miss` works well. |
| 检索质量 | retrieval quality | search quality | Prefer `retrieval quality` in RAG contexts. |
| 混合检索 | hybrid retrieval | mixed retrieval | Standard term. |
| 语义检索 | semantic retrieval | semantic search | Both work, but `semantic retrieval` aligns better with the chapter's architecture framing. |
| 关键词检索 | keyword retrieval | keyword search | Same principle: `keyword retrieval` is more parallel with other glossary items. |

---

## 7. Specification-driven engineering

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| 规范驱动编程 | specification-driven development | spec-driven programming | For chapter-level framing, prefer `specification-driven development`. In running prose, `spec-driven development` is acceptable after the concept is established. |
| 提示词 | prompt | prompt words | Always `prompt`. |
| 结构化提示词 | structured prompt | structured prompting | Use `structured prompting` for the method, `structured prompt` for an artifact. |
| 规范 | specification / spec | rule | `specification` is safer for formal discussion. `spec` works well in running prose after the term is introduced. |
| 声明式 | declarative | statement-based | Use the standard engineering term. |
| 分层的 | layered | multi-layered | Use `layered` unless the distinction matters. |
| 可组合的 | composable | combinable | `composable` is the better engineering term. |
| 可验证的 | verifiable | checkable | Use `verifiable`. |
| 持久化规范 | persistent specification | saved specification | `persistent specification` preserves the architectural meaning. |
| 全局规范 | global spec | global rule set | Use `global spec` in prose after first mention. |
| 项目规范 | project spec | project rules | `project spec` is the cleaner form. |
| 任务规范 | task spec | task rules | Standard wording. |
| OpenSpec | OpenSpec | open specification format | Keep the project/product name unchanged. |
| .cursorrules | `.cursorrules` | Cursor rules file | Keep the filename literal when referenced. |
| 约束空间 | constraint space | space of constraints | `constraint space` reads naturally in technical prose. |

---

## 8. Security, trust, and evaluation

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| 安全与对齐 | security and alignment | safety and alignment | The chapter can use `security and alignment` because the manuscript foregrounds trust boundaries and system design, not only model safety. |
| 信任边界 | trust boundary | confidence boundary | Standard security term. |
| 威胁模型 | threat model | risk model | Keep `threat model` when the security frame is explicit. |
| Prompt Injection | prompt injection | prompt attack | Use the standard attack name. |
| 数据泄露 | data leakage | data leak | `data leakage` is more formal and better for principle-level writing. |
| 输出安全 | output safety | output security | Use `output safety` when discussing harmful model outputs; use `output security` only if the context is stricter access/control semantics. |
| 权限最小化原则 | principle of least privilege | minimal permission principle | Standard security phrase. |
| 人工确认节点 | human approval checkpoint | manual confirmation point | `human approval checkpoint` is more natural in workflow writing. |
| 评估 | evaluation | assessment | Use `evaluation` as the book's default term because it aligns with LLM engineering practice. |
| 评估集 | evaluation set | benchmark set | `evaluation set` is the safer default. `benchmark set` is narrower and more formalized. |
| 离线评估 | offline evaluation | offline testing | Keep `offline evaluation`. |
| 在线评估 | online evaluation | live testing | Use `online evaluation`. |
| 回归门禁 | regression gate | regression barrier | `regression gate` reads naturally in engineering contexts. |
| 灰度 | gradual rollout / canary rollout | grayscale rollout | Never translate literally. Choose by deployment context. |

---

## 9. Non-deterministic systems and organization

| Chinese | Recommended English | Avoid / Use with Caution | Notes |
|---|---|---|---|
| 非确定性 | non-determinism / non-deterministic | uncertainty | Use the formal term when discussing system behavior. |
| 工程化挑战 | engineering challenges | implementation difficulties | `engineering challenges` fits the book's tone. |
| 可观测性 | observability | monitorability | Standard term. |
| 延迟预算 | latency budget | time budget | Use `latency budget`. |
| 成本控制 | cost control | budget management | Prefer `cost control` in systems discussions. |
| 模型更新 | model updates | model upgrades | Use `model updates` as the default neutral term. |
| 治理 | governance | management | `governance` is more precise for the book's organization-level discussion. |
| 组织迁移 | organizational migration | team transition | Usually rewrite based on local context. `organizational migration` is the closest default. |
| 新型资产 | new operational assets / new AI-native assets | new resources | Often rewrite by meaning. `AI-native assets` works well when referring to Prompt, Spec, Skill, memory, and evaluation sets as a governed class of assets. |
| 静默退化 | silent degradation | hidden decay | `silent degradation` fits engineering prose well. |
| 变更管理 | change management | change handling | Standard organizational term. |
| 审计留痕 | audit trail | audit logging only | Use `audit trail` unless the context specifically means logs. |
| 平台角色 | platform role | infrastructure role | `platform role` is closer to the manuscript's organizational framing. |
| 团队级系统 | team-level system | organizational system | `team-level system` is the safer direct rendering. |
| AI 原生架构 | AI-native architecture | architecture for AI | `AI-native architecture` is the natural English form. |
| Agent 网络 | agent network | multi-agent network | Use `agent network` for the broader future-facing concept; `multi-agent system` is fine when the text is discussing current architecture. |

---

## 10. Terms that should usually stay in English

These terms should usually remain in English even inside otherwise translated prose:

- `Agent`
- `SubAgent` / `sub-agent`
- `MCP`
- `Model Context Protocol`
- `Skill`
- `prompt`
- `system prompt`
- `function calling`
- `tool calling`
- `ReAct`
- `RAG`
- `OpenSpec`
- `.cursorrules`
- `Prompt Injection`
- `Lost in the Middle`
- `prompt caching`
- `KV Cache`

---

## 11. Translation notes for chapter titles

These are not final titles. They are directionally preferred renderings to keep terminology aligned.

| Chinese Chapter Concept | Directional English Rendering |
|---|---|
| 大模型是怎么“思考”的 | How Large Language Models Actually Work |
| 与大模型交互的本质 | What Interaction with an LLM Really Is |
| 从问答到执行：Agentic 的运行原理 | From Answers to Action: How Agentic Systems Work |
| 工具的标准化：MCP 交互原理 | Standardizing Tool Use: How MCP Works |
| 预定义的能力包：Skill 交互原理 | Skill as a Packaged Capability |
| 一个不够用：多 Agent 协作原理 | When One Agent Is Not Enough |
| Agent 的能力边界与失败模式 | Agent Limits and Failure Modes |
| 让 AI 记住你：记忆体系的原理与设计 | Building Memory for AI Systems |
| Token 经济学：上下文工程的艺术 | Token Economics and the Art of Context Engineering |
| 知识注入：从 RAG 到代码库原生检索 | From RAG to Code-Native Retrieval |
| 规范驱动编程：从提示词到 OpenSpec | From Prompts to OpenSpec |
| 安全与对齐：AI 系统的信任边界 | Security and Alignment |
| 判定权重建：AI 写的代码该怎么审 | Rebuilding Judgment |
| 当 AI 进入团队：协同重排 | When AI Enters the Team |
| 当 AI 进入组织：从工具到能力底座 | When AI Enters the Organization |

---

## 12. Open questions to revisit later

These terms are good enough for the first translation pass, but should be revisited after 2-3 chapters are translated:

- Should the book title stabilize on `AI Coding from First Principles`, `The First Principles of AI Coding`, or another variant?
- Should `AI 编程` remain consistently `AI coding`, or should some formal chapters switch to `AI software engineering` in limited contexts?
- Should `Skill` always stay capitalized in chapter prose, or only when referring to the product-like concept explicitly?
- Should `上下文工程` remain `context engineering` everywhere, or should some explanatory passages expand it as `the engineering of context` for readability?
- Should `知识注入` remain `knowledge injection`, or be softened to `bringing external knowledge into the model` in more reader-facing passages?
- Should `组织迁移` be rendered more idiomatically chapter by chapter rather than fixed globally?

---

## 13. Practical rule of thumb

When in doubt:

1. Preserve the **concept**, not the Chinese surface form.
2. Prefer the wording that an experienced English-speaking engineer would naturally use.
3. If a term sounds translated rather than written, rewrite it.
4. If a concept is already established in the book, do not rename it casually in later chapters.
