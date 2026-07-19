
# Appendix A — Quick Reference

This appendix compresses the core judgement frameworks from all fifteen chapters into a set of lookup tables you can pull up in the middle of real work.

---

## 1. Three Rules for Organizing Context (Chapter 9)

| Position                          | What goes here                                            | Why                                                                         |
|-----------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| **Front** (System Prompt)         | Behavioral constraints, role definition, core rules       | Strongest attention here, and friendly to prompt caching                    |
| **Middle** (conversation history) | Background, reference material, prior turns               | Weakest attention—park supporting information here                          |
| **End** (user message)            | The instruction for *this* task and its key details       | Second-strongest attention, and the closest thing to the model's output     |

**Rule of thumb:** *constraints up front, background in the middle, instructions at the end.*

---

## 2. Layered Compression Strategy (Chapter 9)

| Context layer        | Compression strategy       | Intensity  | Why                                                       |
|----------------------|----------------------------|:----------:|-----------------------------------------------------------|
| System Prompt        | 🔒 Do not compress         | None       | Every token here changes behavior                         |
| Tool descriptions    | ✂️ Selective injection      | Low        | Inject only the tools relevant to the current task        |
| Conversation history | 📝 Summarize                | Medium     | Keep decisions and conclusions; drop the deliberation     |
| Tool results         | 🗜️ Aggressive compression   | High       | Keep only the parts tied to what the agent is doing now   |
| Memory injection     | 📊 Cap the count            | Medium     | Top-K relevant memories, with a hard cap on how many      |

**The core idea:** *different layers carry different information density, so the room you have to compress them differs too. The system prompt is worth every token; tool results are usually the most redundant thing on the wire.*

---

## 3. Three Rules of Spec Design (Chapter 11)

1. **Cross-task generality** — a spec rule should hold across many tasks, not be glued to one specific task.
2. **Composability** — multiple specs should stack without contradicting each other.
3. **Verifiability** — compliance with the spec should be machine-checkable: a linter, a test, or LLM-as-judge.

**How the three kinds of specs stack together:**

| Dimension            | Persistent Behavioral Preferences        | Change-Level Spec                                 | Capability-Level Spec                                     |
|----------------------|------------------------------------------|---------------------------------------------------|-----------------------------------------------------------|
| Granularity          | Cross-cutting: affects every task        | Vertical slice: one change                        | Vertical slice: one capability                            |
| Lifecycle            | Long-lived, stable, occasionally updated | Single-shot, frozen on archive                    | Lives as long as the code, evolves continuously           |
| Entry point          | Occasional manual review and update      | Written, then frozen; new changes go in new files | Spec first, then code                                     |
| Typical form         | `.cursorrules`, `AGENTS.md`              | OpenSpec proposals under `changes/`               | Specs under `specs/` in OpenSpec                          |

**The judgement:** *cross-cutting behavioral base color goes into behavioral preferences; single-shot decision archives go into change-level specs; long-lived capability truth goes into capability-level specs. Three layers, none of them a substitute for another.*

---

## 4. The Four-Layer Security Model (Chapter 12)

| Layer | Name                  | Mechanism                                                          | What it stops                                  |
|:-----:|-----------------------|--------------------------------------------------------------------|------------------------------------------------|
| L1    | Input filtering       | Regex matching · keyword denylists · semantic classifiers          | Known attack patterns                          |
| L2    | Structural isolation  | XML/JSON tag separation · role marking · data quoting              | Prompt injection                               |
| L3    | Output validation     | Sensitive-data regex · dangerous-action allowlists · LLM-as-judge  | Information leakage and dangerous actions      |
| L4    | Least privilege       | Read / write / dangerous tiers · sandboxes · path allowlists       | Containing the blast radius of the worst case  |

**The math:** P(successful attack) = product of per-layer pass-through rates ≈ 0.5⁴ = 6.25%.

**The design principle:** *each layer assumes every other layer has already failed.*

---

## 5. When to Reach for Multi-Agent (Chapter 6)

**✅ Multi-agent fits when:**

- The task naturally decomposes into independent subtasks (for example, writing tests for several modules in parallel).
- The task needs distinct roles (writing code on one side, reviewing it on the other).
- A single agent's context window simply isn't enough.

**❌ Multi-agent does not fit when:**

- The task isn't actually that complex—writing one function, fixing one bug.
- The subtasks are tightly coupled.
- Consistency requirements are extreme (an atomic, all-or-nothing refactor).
- Your debugging and observability story isn't mature yet.

**The judgement:** *if you're not sure whether to use multi-agent, don't.*

---

## 6. Choosing an Evaluation Strategy (Chapter 13)

| Task determinism | Examples                            | Verification method            | Cost |
|:----------------:|-------------------------------------|--------------------------------|:----:|
| High             | Format conversion, regex generation | Exact assertions               | $0   |
| Medium-high      | Algorithm implementation, bug fixes | Unit-test suite                | $0   |
| Medium-low       | Refactoring, architecture design    | Property checks + human review | $    |
| Low              | Creative coding, document drafting  | LLM-as-judge + human review    | $$   |

**The principle:** *filter with the cheapest gate first; reserve expensive verification for the few outputs that survive the early stages.*

---

## 7. Quick Token-Cost Math (Chapter 9)

| Scenario                       | Estimation formula                                       | Worked example                       |
|--------------------------------|----------------------------------------------------------|--------------------------------------|
| Single call                    | (System + tools + history + new message) × unit price    | 14K tokens × $2.5/M = $0.035         |
| N-turn dialogue (no caching)   | N(N+1)/2 × per-turn delta + N × fixed overhead           | 50 turns ≈ 1.82M tokens ≈ $4.56      |
| N-turn dialogue (with caching) | Roughly 30%–40% of the un-cached cost                    | 50 turns ≈ $1.5–$1.8                 |

**Conditions for prompt caching to actually kick in:**

1. The prefix matches token-for-token.
2. The prefix is at least 1024–2048 tokens long.
3. The gap between calls stays under the cache TTL—usually 5–10 minutes.

---

## 8. Reference Allocation of the Context Window (Chapter 9)

| Region                         | Relative share  | What lives here                                            |
|--------------------------------|:---------------:|------------------------------------------------------------|
| System Prompt + spec           | Small           | Role definition, core rules, OpenSpec                      |
| Skill instructions             | Medium          | The capability packs loaded for the current scenario       |
| Tool descriptions              | Small to medium | Schemas of the tools currently available                   |
| Memory injection               | Small           | Relevant long-term memory fragments                        |
| RAG knowledge                  | Medium          | Retrieved code and document snippets                       |
| Conversation history           | Medium to large | Compressed prior turns                                     |
| **Remaining (task workspace)** | **Keep enough** | **Reserved for the current task's input and output**       |

**The judgement:** *everything that is not the task workspace—spec + Skills + tools + memory + RAG + history—has to leave the task workspace enough room to breathe. There is no universal split; it depends on the task. But once the workspace is visibly squeezed and output quality starts to slip, that is the signal to rebalance the allocation, not to keep stuffing more background into the window.*
