<div align="center">

# First Principles of AI Coding

### Not "how to use Cursor" — but how to derive AI coding systems from the ground up

<p>
  <a href="https://caozhiyi.cc/ai-programming-book/en/"><img src="https://img.shields.io/badge/📖_Read_Online-mkdocs-2196F3?style=for-the-badge" alt="Read Online"></a>
  <a href="#-table-of-contents"><img src="https://img.shields.io/badge/📚_Contents-5_parts_17_chapters-4CAF50?style=for-the-badge" alt="Contents"></a>
  <a href="#-about-the-author"><img src="https://img.shields.io/badge/✍️_Author-caozhiyi-FF9800?style=for-the-badge" alt="Author"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey?style=for-the-badge" alt="License"></a>
</p>

<p><strong>📖 A first-principles book for serious users of AI coding tools · Free to read online</strong></p>

<p><a href="README_cn.md">📄 中文版 README</a></p>

</div>

---

## 🤔 Do any of these sound familiar?

- The AI hands you confident-looking code, it compiles, it looks fine — and then **it just doesn't work at runtime**
- You ask it to fix the bug; it patches one place and breaks another, and you're **stuck in an "AI fixing AI" loop**
- You can't tell when to reach for RAG, when to fine-tune, when to just throw more context at the model — **everything is trial and error**
- Cursor, Claude Code, Copilot, a new agent framework every other week — **every new tool feels like learning from scratch again**
- Prompt writing feels like superstition: **the ones that work, you can't say why; the ones that don't, you can't say why either**
- You've read plenty of "AI coding tutorials" — **felt like you got it, then a slightly new situation throws you off again**

> If any of these landed, **this book was written for you**.

---

## 🎯 What this book actually does differently

Most AI coding content out there teaches you **how to use the tools** — how to write prompts, how to configure Cursor, how to call an API.

This book takes **a different path**:

> **Every concept here isn't a product feature dropped from the sky — it's a consequence derived, step by step, from underlying principles.**

| What typical tutorials teach | What this book makes you understand |
|---|---|
| How to configure the context window | Why the context window exists at all — as a **physical constraint of attention's O(n²) cost** |
| How to build an Agent | Why an Agent is **the inevitable architecture once tool calling becomes possible** |
| How to implement RAG | Why RAG is **an engineering trade-off shaped by the limits of context** |
| How to use the MCP protocol | Why MCP appeared, **and what would go wrong without it** |

**Once you understand the *why*, every new tool, every new concept, every new paradigm becomes a question you can answer:**

> What problem does it solve? What's the cost? Where does it stop working?

This is an **anti-tool-tutorial** book. Tools age out. Principles don't.

---

## 👥 Who this book is for

✅ **A good fit if you are**:
- An engineer already using AI coding tools, looking to move from "able to use" to "actually good with them"
- A tech lead responsible for choosing AI tooling or designing agent architectures for your team
- A developer who wants to understand the **underlying logic** behind RAG, Agents, MCP, Skills — not just the surface
- Someone tired of tutorials that go stale every time a tool updates

❌ **Probably not a good fit if you are**:
- A complete beginner with no programming background (build some real project experience first)
- An ML researcher looking for deep Transformer math (this is an engineering book, not a research one)
- Someone who just wants a copy-paste prompt and calls themselves an "AI user"

---

## 📖 Read online

> **🌐 Recommended: [Online edition (mkdocs)](https://caozhiyi.cc/ai-programming-book/en/)**
> Full navigation, dark mode, syntax highlighting, and the full set of structural diagrams.

Or click into the table of contents below to jump straight to the Markdown files on GitHub.

---

## 📚 Table of contents

The book is organized into **5 parts and 17 chapters**, along a strictly progressive logical line. Each part is a prerequisite for the next.

### 📘 Part I — How large language models actually work

> Without understanding the model itself, every higher-level discussion floats in the air.

- **Chapter 1** — [How Large Language Models Actually Work](docs_en/01.How%20Large%20Language%20Models%20Actually%20Work.md) — tokenization, attention, sampling: the full pipeline
- **Chapter 2** — [What Interaction with an LLM Really Is](docs_en/02.What%20Interaction%20with%20an%20LLM%20Really%20Is.md) — context windows, "lost in the middle", and the physical reality of multi-turn dialogue

### 📗 Part II — From answering to acting

> What exactly do you cross when you go from "you ask, it answers" to an Agent that executes tasks on its own?

- **Chapter 3** — [From Answering to Acting: How Agentic Systems Work](docs_en/03.From%20Answering%20to%20Acting%20How%20Agentic%20Systems%20Work.md)
- **Chapter 4** — [Standardizing Tool Use: How MCP Works](docs_en/04.Standardizing%20Tool%20Use%20How%20MCP%20Works.md)
- **Chapter 5** — [Skill as a Packaged Capability](docs_en/05.Skill%20as%20a%20Packaged%20Capability.md)
- **Chapter 6** — [When One Agent Is Not Enough: Multi-Agent Collaboration](docs_en/06.When%20One%20Agent%20Is%20Not%20Enough.md)
- **Chapter 7** — [Agent Limits and Failure Modes](docs_en/07.Agent%20Limits%20and%20Failure%20Modes.md) ⭐

### 📙 Part III — Memory and context engineering

> How does an AI system "remember" you? And why is the token a unit of economics?

- **Chapter 8** — [Building Memory for AI Systems](docs_en/08.Building%20Memory%20for%20AI%20Systems.md)
- **Chapter 9** — [Token Economics and the Art of Context Engineering](docs_en/09.Token%20Economics%20and%20the%20Art%20of%20Context%20Engineering.md)
- **Chapter 10** — [Three Paths to Knowledge Injection: RAG, Fine-tuning, and Long Context](docs_en/10.Three%20Paths%20to%20Knowledge%20Injection.md) ⭐

### 📕 Part IV — Judgment in architectural choice

> Once the toolbox is full, knowing **which tool fits which situation** is the real skill.

- **Chapter 11** — [Choosing the Right Stack for the Job](docs_en/11.Choosing%20the%20Right%20Stack%20for%20the%20Job.md)
- **Chapter 12** — [From Prompts to OpenSpec: Spec-driven Programming](docs_en/12.From%20Prompts%20to%20OpenSpec.md)
- **Chapter 13** — [The End-to-End Blueprint of an AI Coding System](docs_en/13.The%20End-to-End%20Blueprint%20of%20an%20AI%20Coding%20System.md)
- **Chapter 14** — [Security and Alignment: Where AI Systems Should and Shouldn't Be Trusted](docs_en/14.Security%20and%20Alignment.md)

### 📔 Part V — Engineering and the road ahead

> Turning "I can use AI" into "our team ships continuously with AI" takes a whole engineering methodology.

- **Chapter 15** — [Engineering for Non-Deterministic Systems](docs_en/15.Engineering%20for%20Non-Deterministic%20Systems.md)
- **Chapter 16** — [The Organizational Side of AI Engineering: Governance, Evaluation, Team Migration](docs_en/16.The%20Organizational%20Side%20of%20AI%20Engineering.md)
- **Chapter 17** — [The Limits and Future of AI Coding](docs_en/17.The%20Limits%20and%20Future%20of%20AI%20Coding.md)

### 📎 Appendix

- [Appendix A — Quick Reference Cards](docs_en/appendix-quick-reference.md) — fast lookup for key concepts
- [Appendix B — A 30-Day Practice Path](docs_en/appendix-30-day-path.md) — an executable plan from beginner to comfortable
- [Terminology](docs_en/TERMINOLOGY.md) — glossary of recurring terms

---

## 💡 A few things that make this book different

### 1. **Every conclusion is derived from prior principles**
You won't find sentences like "the industry recommends RAG". You'll find: **context windows are limited → so external knowledge has to come from somewhere → there are several retrieval trade-offs → RAG is the optimum under a particular set of constraints**.

### 2. **Original structural diagrams throughout**
The key mechanisms — attention, the ReAct loop, MCP architecture, layered memory, the knowledge-injection decision tree, and so on — all come with hand-drawn SVG diagrams. **Half the understanding comes from looking at the picture.**

### 3. **Failure modes get their own real estate**
The book doesn't only explain "why you need X" — it also explains "what happens when X is misused". Chapter 7 is dedicated to Agent failure modes, the part most other books quietly skip.

### 4. **A strong sense of where things stop working**
Every technique has a boundary. The book is explicit about it: **what to use it for, what not to use it for, and where the edge actually is.**

### 5. **Built to age slowly**
There's no tutorial for any specific tool. Only the underlying principles. Cursor may be replaced tomorrow, but the nature of tokens, attention, context, and Agents won't be.

---

## 🚀 How to read it

### 🍱 If you have time (recommended): read it cover to cover
Each chapter naturally raises the question that the next chapter answers. That logical chain itself is the best path through AI coding systems.

### ⚡ If you're in a hurry: read the part introductions first
Each part opens with a short introduction — what it sets out to solve, what the core takeaway is. Read those first, then decide which chapters to go deep on.

### 🎯 If you're coming with a question: jump straight in
- Trying to figure out **why your Agent fails** → go straight to Chapter 7
- Choosing between **RAG vs. fine-tuning** → go straight to Chapter 10
- Designing an **enterprise-grade AI coding system** → go straight to Chapter 13
- Building the case for **AI adoption to leadership** → go straight to Chapter 16

---

## 🛠️ Local build (optional)

If you'd like to run the mkdocs site locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Start the local server (defaults to http://127.0.0.1:8000)
mkdocs serve

# Build the static site
mkdocs build
```

---

## 🌟 About the author

I'm **caozhiyi**, an engineer with a long stretch of years on infrastructure and systems architecture. This book didn't come out of thin air — it grew out of the concrete confusions I ran into while using AI coding tools, and the methodology I distilled from working through them.

If the book was useful to you, feel free to follow my WeChat Official Account (**煮码宝藏**). I will continue to share:
- Reflections on AI coding from the trenches
- System design and architecture methodology
- Network protocols, QUIC, and other low-level work

> 📮 *gmail**: `caozhiyi5@gmail.com`

---

## 🤝 Contribution and feedback

The book is still being polished. Any kind of involvement is welcome:

- 🐛 Found a typo or a technical mistake? → [open an Issue](https://github.com/caozhiyi/ai-programming-book/issues)
- 💡 Think a derivation could be tightened? → [send a PR](https://github.com/caozhiyi/ai-programming-book/pulls) or open an Issue
- ❓ Got stuck on something? → [ask in Discussions](https://github.com/caozhiyi/ai-programming-book/discussions)
- ⭐ Found it useful? **A Star is the best support an author can get.**

I read and reply to every Issue.

---


## 📜 License

This book is released under [**CC BY-NC-SA 4.0**](https://creativecommons.org/licenses/by-nc-sa/4.0/).

In plain words:
- ✅ You can **read, copy, and share** the content freely
- ✅ You can **adapt and build on it** (with attribution, and under the same license)
- ❌ **No commercial use** (no selling it as a printed book, no putting it inside a paid course, etc.)

---

<div align="center">

**If this book helped you, please drop a ⭐ Star — it's the most encouraging signal an author can get.**

<a href="https://star-history.com/#caozhiyi/ai-programming-book&Date">
  <img src="https://api.star-history.com/svg?repos=caozhiyi/ai-programming-book&type=Date" alt="Star History" width="600">
</a>

</div>
