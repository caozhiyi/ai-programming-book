
# Appendix B — A 30-Day Practice Path

By the time you finish this book, you understand how an AI coding system actually runs. *Understanding* and *being able to use it well*, however, are still some distance apart. This appendix lays out a 30-day plan grounded in the principles of the book—not a tutorial, but a path to convert what you now know into something you do.

---

## Week 1 — Understand Your Tool

**Goal:** Build a mechanical understanding of the AI coding tool you actually use every day.

**Maps to:** Chapters 1–3.

### Day 1–2: Watch the Context Window

Run a small experiment. Open a fresh session, hand the agent a task that needs at least ten steps to finish—something like *refactor the error handling in this module*. Then watch carefully.

- [ ] At which step does *forgetting* start showing up? (Earlier decisions get dropped.)
- [ ] Once the context fills up, what does the tool actually do? Truncate? Compress? Error out?
- [ ] For the same task, does running it as one big request beat splitting it into three smaller ones, or the other way around?

**The principle you are testing:** the finite context window (Chapter 1), accumulated drift (Chapter 1), and how information piles up inside the ReAct loop (Chapter 3).

### Day 3–4: Watch Tool Calls

If your AI coding tool exposes a log or a debug panel, open it and walk through one full task end-to-end.

- [ ] Which tools does the agent call, and in what order?
- [ ] How much information comes back from each call, and how much of it is actually useful?
- [ ] Did the agent ever pick the *wrong* tool? Why?

**The principle you are testing:** the ReAct loop (Chapter 3), and why the description of a tool matters as much as the tool itself (Chapter 4).

### Day 5–7: Measure Non-Determinism

Take one task. Use the exact same prompt. Run it three times. Then compare.

- [ ] Across the three runs, is the core logic consistent?
- [ ] Where do the differences land—variable names, code style, the implementation strategy itself?
- [ ] Which differences can you live with, and which cross a line?

**The principle you are testing:** temperature and sampling (Chapter 1), and the fact that you are operating a non-deterministic system in the first place (Chapter 13).

---

## Week 2 — Establish a Spec

**Goal:** Write the first usable spec file for your project.

**Maps to:** Chapters 5 and 11.

### Day 8–9: Surface the Implicit Spec

Look back at the past week of working with the AI. Find the places you keep correcting it.

- [ ] *Don't use `fmt.Errorf`, use `errors.New`.*
- [ ] *Use `slog`, not the standard `log` package.*
- [ ] *Functions should not exceed 50 lines.*
- [ ] *Error messages in English.*

Collect those corrections into a list. That list *is* your implicit spec; it just hasn't been written down yet.

### Day 10–12: Write the First Spec File

Convert the implicit spec into a format your AI tool actually reads—`.cursorrules`, `CLAUDE.md`, or whatever format your tool of choice consumes.

```markdown
# Project Coding Spec

## Error handling
- Use errors.New to create errors; do not use fmt.Errorf
- Wrap context on every error: errors.Wrap(err, "what was being done")
- Silently dropping errors (`_ = someFunc()`) is not allowed

## Logging
- Use the slog package, not the standard log package
- Log levels: Info for business events, Error only for issues that need a human

## Code style
- A single function should not exceed 50 lines
- Error messages in English
- Exported functions must have a doc comment
```

Then check the spec against itself.

- [ ] Does each rule hold *across tasks*? (Generic enough to apply broadly, not bound to one task.)
- [ ] Are any two rules in conflict?
- [ ] Is each rule verifiable—can a linter or a test catch a violation?

### Day 13–14: Verify the Spec Actually Works

Take one task. Run it twice—once with the spec loaded, once without. Compare the output.

- [ ] With the spec, does the AI's output actually match your coding style?
- [ ] Are there rules the AI quietly ignores? Why? (Usually the wording is not specific enough.)
- [ ] Iterate on the wording until the AI follows the rule consistently, not just sometimes.

**The principle you are testing:** the four ingredients of a Skill (Chapter 5), and the evolution stages a spec goes through (Chapter 11).

---

## Week 3 — Build an Evaluation Capability

**Goal:** Stand up a minimum-viable evaluation set so you can put a number on output quality instead of *feeling* it.

**Maps to:** Chapter 13.

### Day 15–17: Collect Evaluation Cases

From your last two weeks of AI interaction, pick ten representative tasks.

- [ ] 3 tasks the AI handled well (your positive baseline).
- [ ] 3 tasks where the output was middling (room to improve).
- [ ] 2 tasks where the AI clearly fell short (failure modes).
- [ ] 2 edge cases—the kind of scenario where things tend to break.

For each case, record:

- the input you handed the AI;
- the *characteristics* of an acceptable output—not an exact match, but the properties it must satisfy;
- how you check it: does it compile, do the tests pass, does the linter stay clean, or is this one a human judgement call?

### Day 18–19: Define the Quality Bar

Set a pass criterion for the evaluation set across each dimension you care about.

| Dimension              | Verification method   | Pass criterion                  |
|------------------------|-----------------------|---------------------------------|
| Syntactic correctness  | Compiler              | Zero errors                     |
| Functional correctness | Unit tests            | All passing                     |
| Spec compliance        | Linter + spec checks  | No new warnings introduced      |
| Scope of change        | Diff size             | Touches only what is necessary  |

### Day 20–21: Run a Baseline

With your current setup—your spec, your tools, your context—run all ten cases through.

- [ ] Record pass/fail for each case.
- [ ] Compute the overall pass rate. That number is your baseline.
- [ ] For the failures, do a root-cause pass: is the spec under-specified, is context missing, or is the task itself genuinely too complex?

**The principle you are testing:** the shift from *assertion* to *evaluation* (Chapter 13), and the idea of an evaluation pipeline as a real engineering surface (Chapter 13).

---

## Week 4 — Establish a Team Process

**Goal:** Stand up the smallest version of a governance process that actually works.

**Maps to:** Chapter 14.

### Day 22–23: Check the Spec In

- [ ] Commit the spec file to the project repo (versioned alongside the code, not stored in someone's notes app).
- [ ] Write a commit message that explains what the spec is for and where it applies.
- [ ] Tell the team it exists.

### Day 24–25: Assign Owners

For each of these responsibilities, name the person who owns it. In a small team, one person can wear several hats; the point is that *some specific name* is attached.

- [ ] Spec maintainer — who updates the spec when the project's tech stack shifts?
- [ ] Evaluation lead — who keeps the evaluation set healthy when new failure modes show up?
- [ ] Model upgrade decision-maker — who has the authority to switch the underlying model?

### Day 26–27: Define Update Triggers

Decide, in advance, *when* the spec and evaluation set get touched. Once the trigger is written down, you stop arguing about timing later.

- [ ] Tech stack changes → update the spec.
- [ ] A new failure mode shows up → expand the evaluation set.
- [ ] Model upgrade → run the evaluation set as a regression before promoting.
- [ ] Every two weeks → a 15-minute spec review, even when nothing has obviously changed.

### Day 28–30: Retrospective and Iteration

Look back across the 30 days.

- [ ] How many revisions has your spec gone through? What changed in each one?
- [ ] How has the evaluation set's pass rate moved relative to the baseline?
- [ ] Are people on the team noticeably more satisfied with the AI's output, or only marginally?
- [ ] What is the single most important thing to improve next?

---

## After the 30 Days

By the end of this path, your team should have a working spec and a knowledge-injection setup in place, and the center of gravity should be visibly shifting toward evaluation and observability—moving from *the AI can produce it* to *what the AI produces can be continuously verified*.

**A sustainable cadence to keep going:**

| Cadence          | What you do                                                       |
|------------------|-------------------------------------------------------------------|
| Daily            | Watch the AI's output and notice new failure modes as they appear |
| Weekly           | Extend the evaluation set whenever a new failure mode is real     |
| Bi-weekly        | A 15-minute spec review                                           |
| Monthly          | Run the full evaluation set and look at the quality trend over time |
| On model upgrade | Canary → evaluate → promote (or roll back)                        |

**One thing to keep in mind:** none of this is a one-shot project. It is an ongoing operation. The quality of an AI system does not stay good on its own—like the code it writes for you, it has to be maintained.
