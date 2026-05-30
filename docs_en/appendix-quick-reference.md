
# Appendix A — Quick Reference

This appendix compresses the core judgement frameworks from all seventeen chapters into a set of lookup tables you can pull up in the middle of real work.

---

## 1. Three Rules for Organizing Context (Chapter 9)

| Position                          | What goes here                                            | Why                                                                         |
|-----------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| **Front** (System Prompt)         | Behavioral constraints, role definition, core rules       | Strongest attention here, and friendly to prompt caching                    |
| **Middle** (conversation history) | Background, reference material, prior turns               | Weakest attention—park supporting information here                          |
| **End** (user message)            | The instruction for *this* task and its key details       | Second-strongest attention, and the closest thing to the model's output     |

**Rule of thumb:** *constraints up front, background in the middle, instructions at the end.*

---

## 2. The Stack Selection Decision Tree (Chapter 11)

```
Does your task need to interact with tools?
├── No  → Use Chat (pure dialogue)
└── Yes → Does it need multi-step autonomous execution?
    ├── No  → Use Tool-Augmented Chat
    └── Yes → Does it need distinct specialist roles?
        ├── No  → Use a Single Agent
        └── Yes → Are the subtasks tightly coupled?
            ├── Yes → Use a Single Agent with role switching
            └── No  → Use Multi-Agent
```

**How to read each branch:**

- *Needs tool interaction* — the task requires reading or writing files, executing commands, or calling APIs.
- *Multi-step autonomous execution* — more than one step, with real dependencies between them.
- *Distinct specialist roles* — the subtasks need mutually exclusive Skill sets or independent contexts.

---

## 3. Layered Compression Strategy (Chapter 9)

| Context layer        | Compression strategy       | Ratio   | Why                                                       |
|----------------------|----------------------------|:-------:|-----------------------------------------------------------|
| System Prompt        | 🔒 Do not compress         | 1:1     | Every token here changes behavior                         |
| Tool descriptions    | ✂️ Selective injection      | ~3:1    | Inject only the tools relevant to the current task        |
| Conversation history | 📝 Summarize                | ~5:1    | Keep decisions and conclusions; drop the deliberation     |
| Tool results         | 🗜️ Aggressive compression   | ~20:1   | Keep only the parts tied to what the agent is doing now   |
| Memory injection     | 📊 Cap the count            | ~8:1    | Top-K relevant memories, with a hard cap on how many      |

---

## 4. Three Rules of Spec Design (Chapter 12)

1. **Cross-task generality** — a spec rule should hold across many tasks, not be glued to one specific task.
2. **Composability** — multiple specs should stack without contradicting each other.
3. **Verifiability** — compliance with the spec should be machine-checkable: a linter, a test, or LLM-as-judge.

**The four evolutionary stages of a spec:**

| Stage | Form                          | Character                               | Where it fits         |
|-------|-------------------------------|-----------------------------------------|-----------------------|
| 1     | Natural-language prompt       | Flexible, but vague                     | Solo exploration      |
| 2     | Structured Skill              | Has shape, but is not verifiable        | Early team adoption   |
| 3     | Declarative spec              | Verifiable, but needs maintenance       | Mature team           |
| 4     | Executable spec               | Auto-verified and auto-repaired         | Operating at scale    |

---

## 5. The Four-Layer Security Model (Chapter 14)

| Layer | Name                  | Mechanism                                                          | What it stops                                  |
|:-----:|-----------------------|--------------------------------------------------------------------|------------------------------------------------|
| L1    | Input filtering       | Regex matching · keyword denylists · semantic classifiers          | Known attack patterns                          |
| L2    | Structural isolation  | XML/JSON tag separation · role marking · data quoting              | Prompt injection                               |
| L3    | Output validation     | Sensitive-data regex · dangerous-action allowlists · LLM-as-judge  | Information leakage and dangerous actions      |
| L4    | Least privilege       | Read / write / dangerous tiers · sandboxes · path allowlists       | Containing the blast radius of the worst case  |

**The math:** P(successful attack) = product of per-layer pass-through rates ≈ 0.5⁴ = 6.25%.

**The design principle:** *each layer assumes every other layer has already failed.*

---

## 6. Maturity Self-Assessment Checklist (Chapter 16)

| Tier | The question to ask                                       | What "yes" looks like                                                       |
|:----:|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| L0   | Is anyone on the team using AI for coding at all?         | Someone is using Chat-style assistance during coding                        |
| L1   | Can the AI execute multi-step tasks on its own?           | An agent environment is wired in; it can read/write files and run commands  |
| L2   | Is the AI's output style consistent across the team?      | Shared Skills/specs are in place; there is a project knowledge base         |
| L3   | Can you *quantify* the AI's output quality?               | An evaluation set, monitoring metrics, and a way to trace incidents         |
| L4   | Is there a regression process when the model is upgraded? | Versioned assets, with a canary/rollback path                               |

**The honest read:** *most teams capture most of the value somewhere between L0 and L2.*

---

## 7. When to Reach for Multi-Agent (Chapter 6)

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

## 8. Choosing an Evaluation Strategy (Chapter 15)

| Task determinism | Examples                            | Verification method            | Cost |
|:----------------:|-------------------------------------|--------------------------------|:----:|
| High             | Format conversion, regex generation | Exact assertions               | $0   |
| Medium-high      | Algorithm implementation, bug fixes | Unit-test suite                | $0   |
| Medium-low       | Refactoring, architecture design    | Property checks + human review | $    |
| Low              | Creative coding, document drafting  | LLM-as-judge + human review    | $$   |

**The principle:** *filter with the cheapest gate first; reserve expensive verification for the few outputs that survive the early stages.*

---

## 9. Quick Token-Cost Math (Chapter 9)

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

## 10. Reference Allocation of the Context Window (Chapter 13)

| Region                         | Suggested share | What lives here                                            |
|--------------------------------|:---------------:|------------------------------------------------------------|
| System Prompt + spec           | ~10%            | Role definition, core rules, OpenSpec                      |
| Skill instructions             | ~12%            | The capability packs loaded for the current scenario       |
| Tool descriptions              | ~10%            | Schemas of the tools currently available                   |
| Memory injection               | ~8%             | Relevant long-term memory fragments                        |
| RAG knowledge                  | ~15%            | Retrieved code and document snippets                       |
| Conversation history           | ~25%            | Compressed prior turns                                     |
| **Remaining (task workspace)** | **~20–30%**     | **Reserved for the current task's input and output**       |

**Warning:** *once the task workspace is squeezed below 15%, output quality drops noticeably.*
