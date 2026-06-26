# The Repriced Engineer: The Second Half of Software Engineering as a Profession

The software engineering profession has, for decades, sat on top of a stable capability list. Which language. What scale. Which domain. Each cell on that grid mapped to a slice of money the market was willing to pay. Over the last two years that list has started to come loose. Which cells get a premium and which ones no longer do is being reshuffled.

This is not a cyclical hiring tide. The shift is structural. The cause is not any one company or any one product. It is the trajectory described in the previous appendix—from rule-codification to token-based delivery. Once that trajectory is underway, the first thing it actually transmits to is not the product surface and not the infrastructure. It transmits to the supply side at both ends: **the people who write the software**.

Infrastructure (which the AI Gateway appendix walked through) has to grow along with system architecture, and that takes years. The supply-side transmission is much faster. It happens directly inside every JD (job description), every interview, every comp review.

## 1. A profession is never abstract dignity. It is a pricing of a specific bundle of capabilities.

To get this right, the framing has to change.

Most of the discussion these last two years on *will AI replace programmers* has, in the end, been about feelings. About dignity. About status. About whether someone who has written code for fifteen years is suddenly going to be useless. Discussions of that shape rarely conclude anything, because the fulcrum is mushy. Whether a profession is being replaced is not a feeling. It is something the market eventually settles in dollars.

What actually constitutes a profession is the market putting a stable price on a specific bundle of capabilities.

A profession exists durably when the bundle of capabilities it owns satisfies three conditions in the market at the same time: **scarce, identifiable, purchasable**. Scarce so the bundle has a price. Identifiable so the bundle can clear hiring. Purchasable so a stable supply-and-demand structure can form around it. Miss any one and the profession does not hold. *Typist* was a real profession in its era and supported many people, because typing in that era satisfied all three. Today it is gone—not because typing is gone, but because none of the three is still attached to it.

The reason software engineering has trended up steadily for decades is that all three properties have been compounding. People who can write software have stayed scarce. The capability shows up clearly in interviews. The whole digitization wave has produced a seemingly inexhaustible appetite for buying *the writing of software*.

But the capability list is not a natural thing. It is shaped by its era.

Knowing assembly is, if anything, scarcer today than in its heyday—but it can no longer hold the price it once held. Not because nobody needs it; because the set of situations that need it has narrowed sharply, retreating from the mainstream into kernels, embedded systems, and extreme-performance niches. Most business code no longer needs it. Market price is not set by scarcity alone. It is set on the demand side. *Knowing how to operate a mainframe* used to be worth real money in its day; today it is not, for the same reason. *Knowing how to design high-concurrency systems* was worth a lot of money for the past decade and is still worth money, but the premium is shrinking, because cloud vendors have productized that solution into a set of callable services. Most companies no longer need every team to maintain their own. The total demand is contracting. *Knowing how to do front-end layout* was once a scarce skill; today, for most businesses, *good enough* is the bar—not because the demand vanished, but because the supply-side bar dropped. Each capability whose market price drifts down can be cleanly attributed to one of those two mechanisms. Either the demand side contracted, or the supply side became saturated. Either way, the result is the same: the capability no longer holds a premium.

Engineers know this perfectly well. Anyone with ten or more years in this industry can name one or two capabilities they once took pride in that no longer command what they used to. That is not a personal decline. It is that the scarcity of that capability inside the overall supply has shifted.

The wording on a JD is the **delayed photographic exposure of this pricing mechanism**.

The market does not write a capability into a JD for no reason. Writing it in means the need has been sitting unfilled inside the company for some time, that HR has aligned with the hiring manager more than once, that this capability has hardened from *occasionally useful* into *cannot ship without it*. The market also does not pull a capability out of the JD without reason. Pulling it out means the company has discovered that this capability is no longer the binding constraint, that supply at the same price has gotten plentiful enough. That same lag is what makes the JD the most honest observation tool we have. It cannot predict the future. But it can tell you, very clearly, **which combinations of capability the market has actually settled on over the last stretch of time**.

Structural change always passes through a hidden phase before it shows up in any externally visible form. Which is why *will AI replace programmers* is the wrong size of question. It is too big to answer usefully.

The more precise question is: **how is the capability list of software engineering being reshuffled in the token-based era? What is being marked up? What is being marked down? Which previously implicit abilities, scattered across senior engineers' heads, are about to be pulled out and named as a separate, premium-bearing capability of their own?**

## 2. In the rule-codified era, the market paid a seventy-year premium for "doing"

Before figuring out where this goes next, it helps to be clear on what the market has actually been paying for over the last seventy years.

Software engineering, counting from the assembly era, is about seventy years old. Its surface has changed many times—punch cards, time-sharing, the PC, the internet, mobile, cloud-native, Kubernetes. Every wave has bumped the market price of some cohort of engineers up a notch. Stack the waves on top of each other, though, and there is one main line that never changes underneath:

**The market has been paying a premium for "doing" the whole time.**

*Doing* here is not abstract capability. It is very concrete: *can write a particular language*, and on top of that, two axes of depth—*scale* and *domain*.

Writing a particular language is the foundation. In the era when C took off, fluent C writers were scarce. In the era when Java took over enterprise development, fluent Java writers commanded a premium. In the era when Go entered the cloud-native main stage, fluent Go writers were the new scarcity. Every language's rise pulls forward a cohort that figured it out early. By the time the language goes mainstream, that cohort is sitting on the scarcest end of supply.

Working at a given **scale** is the depth axis on the engineering side. Plenty of people can write Java; not many have written Java systems that hold up under tens of millions of concurrent users. Plenty of people can write Go; not many have written Go services that survive years of repeated production iteration. Scale is not something documentation teaches. It is hammered out in real projects. How big a system an engineer has lived inside, how severe the production incidents they have handled, how complex the evolution they have carried—those are themselves scarce supply, and they cannot be acquired by short-term study.

Working in a given **domain** is the depth axis on the domain side. Two backend engineers, one who has worked on payments and one who has worked on recommendations, are two different supplies. The first one is fluent in reconciliation, idempotency, risk control, and compliance. The second one is fluent in features, recall, ranking, and A/B experiments. Neither set of knowledge can substitute for the other, and the market is happy to pay distinct premiums for each. Behind every vertical sits a whole stack of problems that only recur inside that vertical. The people who can dispatch those problems cleanly hold a price inside that vertical.

These three layers of scarcity, stacked, hold up the entire pricing mechanism for the engineer market over the past seventy years.

There is a deeper assumption underneath: **the tech stack itself is scarce, and the people who master the stack are scarce supply**. The complexity of any given stack is high enough and stable enough that learning it deeply is a worthwhile long-term investment, with stable enough payoff to be worth the bet. An engineer who puts three or five years into a particular stack is reasonably betting that the market will keep paying for that investment over the next decade.

This pricing mechanism has run stably for seventy years. It shaped the entire engineer growth path. Junior engineers were told to *go deep on the stack*, then *go big on scale*, then *go fluent in a domain*. A clear, plannable, copyable career curve. It also shaped how the industry recognizes talent—what stacks the resume lists, what scale the projects ran at, which domains the candidate has worked in are the first things any interviewer looks at. It even shaped what we mean by *senior*. A senior engineer was, more or less, *someone who has done a lot more than other people have done*. **Senior = has done a lot.** For seventy years, those two have been almost interchangeable.

This is the same axis the previous appendix was on. The half of the world software has eaten requires, at every step, *doing*. A world that decomposes cleanly into steps, into states, into rules, needs people who will actually write those steps, those states, those rules. The market has paid a premium for that *doing*, and paid it willingly, because there has been no other way to supply it.

The mechanism has worked so stably for so long that those of us who have spent careers running inside it have a hard time imagining it ever cracking.

## 3. In the token-based era, the scarcity of "doing" is structurally falling

Saying *programmers will be replaced* is both inaccurate and dishonest. It compresses a complex structural shift into a clickable line. But it also cannot be dodged: the scarcity of *doing* is structurally falling, and it is happening inside every engineer's daily work.

**Doing, for the first time, is no longer scarce.**

The tech stack used to be a scarce resource. Learning one cost time, scars, project anchors, and repeated grinding inside real engineering. That scarcity was *physical*—it depended on human learning time, and human learning time is finite and incompressible. Mastering one mainstream stack a year, becoming fluent in several over a decade—this was a hard supply-side constraint. The market paid a premium for stack-mastery precisely because of that constraint.

Today the LLM has changed the supply curve of *doing*. It can write usable code in most mainstream stacks—clean enough, stylistically consistent, covering common patterns. An engineer who has never written Go can, with an LLM, produce passable Go in a short window. Someone who has never used a particular framework can, with an LLM, get its common usage patterns running in days. These steps used to require time-paid-as-learning. Now they can be routed around by spending tokens.

This does not mean people no longer need to learn, and it does not mean that LLM-written code is automatically good enough. Often what it produces only counts as *runs*; *runs in production for a year* is a different bar. But the supply curve of *doing* has clearly flattened. Supply used to depend on human learning time. Now, as long as you are willing to spend, the *doing* of almost any mainstream stack can be bought. Once the supply curve flattens, scarcity drops, and the premium the market is willing to pay starts to shrink.

The impact is not uniform.

The more general, mainstream, and well-documented a stack is, the more deeply it is hit—because that is where the LLM has the richest training signal and produces the most plausible code. The more obscure, closed-source, and experience-bound a stack is, the more lightly it is hit—because the LLM has less to learn from. So the change does not happen overnight. It propagates along this gradient, layer by layer, from the outer ring of the most general stacks toward the inner ring of the most specialized ones. Reaching the innermost layers may take several years, but the direction is stable.

More subtly: the ability to *write the code* can be outsourced to tokens. The ability to *judge what was produced* cannot.

Which means: **the devaluation of *doing* is not the devaluation of the engineer.** It just means that the *doing* line on the engineer's value sheet is shrinking, while other lines on the same sheet are appreciating. The market, however, takes time to register this. The transmission chain—from *capability has actually shifted* to *new wording in the JD* to *interviewers actually evaluating against that wording* to *the comp system actually relocating the premium to the new line*—has its own pace.

This curve will not break in a single moment. It will travel along different stacks, different scales, and different industries at different speeds, year by year. Look back ten years from now and certain phrases that fill JDs today will be almost gone, while certain phrases that sound unfamiliar today will be sitting at the top.

## 4. The new scarcity is a few capabilities that used to live, undeclared, in senior engineers' heads

The price of *doing* shrinks, but the total pool of money is not shrinking. It is being redistributed. The other side of the redistribution sits on a few capabilities that have always existed but were never explicitly labeled.

Any genuinely senior engineer already has some of these. They were just scattered through daily work, glued onto the *doing*, never named separately, never hired against separately. Now they are being pulled out, one by one.

### Defining a piece of work clearly

The first capability is *defining a piece of work clearly*.

This used to be silently completed. A vague task lands on the team. Someone experienced fills in the gaps in their head—they know what the requirement is actually trying to solve, they know which boundaries were not written down, they know which cases need to be confirmed with the PM and which can be handled by convention. None of that completion was recorded. None of it was billed. It happened inside the senior engineer's head, in the few questions they walked over and asked product, and in the small judgments they made while writing code.

Once the LLM enters the loop, that silent completion stops working.

Hand a vague task directly to the LLM and it does not push back, it does not chase the missing pieces, it does not stop because *something does not feel right*. It will follow the vagueness all the way through and produce something that looks reasonable but is, in fact, off-target. This used to happen occasionally with junior engineers, but their drift was bounded—a senior could pull it back with one review pass. The LLM drifts differently. The code it writes looks professional. Each line, in isolation, is fine. But on the whole it is *off* by some quiet amount, and that amount is not visible without careful reading.

So the ability to define work has to move from implicit to explicit.

The book's chapter on specification-driven development covered exactly this: why writing specs has, for the first time, become a core engineering practice in the LLM era—not because of some engineering aesthetic preference, but because the executor at the other end has changed from a human into something that does not push back. Specs used to be optional, fillable by team rapport. Specs are now mandatory, captured in documents, captured in spec files, captured in a form another Agent can read.

The person who can do this consistently—break a vague business requirement into a clear execution spec, foresee the boundary cases, and write down *what counts as done correctly*—is scarce supply. This capability used to be distributed across several experienced people on the team, each of them filling in a piece. Now it has to consolidate, from distributed silent completion into a single identifiable, hireable, premium-bearing capability.

### Reviewing AI output

The second capability is *judging what the AI produced*.

This is not the same activity as code review. Reviewing code is reviewing an implementation that was already thought through by a person. You are checking whether there is a better way to write it, whether boundaries were missed, whether anything could be refactored. The author is presumed to understand the business, the code, and what they wrote. None of that presumption survives with an LLM. The LLM does not know your company's specific business constraints, does not know the actual reality of the upstream and downstream of this path, does not know why you picked this approach over another one in the past. It can produce code that looks reasonable. Whether it actually *is* reasonable is something only the reviewer can know.

The review capability here breaks down into a few concrete pieces:

- Being able to judge, *with all the tests passing*, whether the design holds up. Tests can falsify; they cannot verify. AI-written code passing every test does not mean it is actually correct. It may have drifted somewhere the tests never reach.
- Being able to find the root cause of a non-reproducible drift. LLM-written code fails differently from human-written code. Its drift is rarely *one line is wrong*. It is more often *the whole understanding is tilted*. Spotting that tilt requires a real understanding of the business.
- Being able to recognize *looks right but is actually off*. This is the hardest. It requires the reviewer to have real domain judgment—to see that, yes, this piece of logic is clean and well-formed, but the problem it is solving is not the actual problem in this specific business context.

This capability has one defining property: **it cannot be outsourced back to the same LLM**. You cannot have one LLM review another LLM's output, because that LLM does not have your specific business constraints. Its reviewing and its writing run on the same judgment system; it cannot surface the real problems. So this work has to be done by a person. The market is still early in recognizing this, but the direction is clear: it will move from *a side product hidden inside code review* into *something hireable on its own*.

### Backstopping non-determinism

The third capability is *backstopping non-determinism*.

This is what is quietly redefining *senior*.

The book has covered Agent failure modes: when an Agent runs, it will drift. The question is not how to make it stop drifting. The question is whether the system holds when it drifts. And it has covered the organizational side of AI engineering: when part of the system's behavior is non-deterministic, how the organization adjusts to absorb that non-determinism. Both have one thing in common: **they require the ability to keep engineering discipline intact in front of non-determinism**, and that ability used to live, unlabeled, inside senior engineers' experience.

Senior engineers were expensive in the rule-codified era largely because they knew when things were going to break, why they would break, and what to do once they did. That judgment was never named, because rule-based systems' drift was locatable. Check the logs. Read the stack trace. Replay the case. The root cause usually surfaces. The senior engineer's backstop ability was scattered across debugging, tuning, refactoring—glued onto *doing*.

Token-based systems are different. Their drift is more subtle and harder to localize. The work-shape of debugging itself shifts: you are no longer hunting for *which line is wrong*, you are building a judgment, inside a fog, of *roughly where this thing tilted*.

That shift turns *backstopping* from an implicit ability into a market-recognizable one. Drawing failure boundaries for an Agent. Reconstructing the scene of a non-deterministic moment of thinking after the system has drifted. Knowing when to give the loop back to a human. This used to be experience. Now it is being pulled out as a capability of its own, and it is the core of the new senior.

### Designing the Agent workflow

The fourth capability is *designing the Agent's working chain*.

The book has walked through the evolution from a single Agent to multi-Agent. From the market's angle, the equivalent is this: *knowing how to use a particular AI tool* is not going to be the line on the JD that earns a premium, because that quickly becomes the floor for everyone. What gets a premium is *being able to design an Agent workflow and knowing exactly which checkpoints hand control back to the human*. The first is consumer-side capability. The second is producer-side capability.

Designing an Agent workflow demands a capability list that does not overlap much with *doing*. It requires: decomposing the task, picking the right model, placing human approval checkpoints at the right nodes, anticipating the ways the Agent will drift, and designing backstops for those drifts. None of this lives in the traditional engineer's skill library. The traditional engineer was trained to write rules correctly. Agent design trains for keeping a system that *thinks for itself* inside a sane boundary.

Stack these four together and the direction becomes visible: **the market is repricing, line by line, the judgments that the AI cannot make for the engineer**. It is not that judgment suddenly became valuable. It is that judgment has, for the first time, been pulled out of *doing* and given its own slot on the JD.

## 5. The word "senior" is being split into two layers

The old definition of senior is being split.

The first layer of senior is *has done a lot*. Stacks done. Scale done. Domains done. The scarcity of all three is shrinking. The stacks—LLMs do them, more or less, with better recall than humans. Scale—after cloud vendors productized it, most companies no longer need every team to have personally carried billion-request days. Vertical-domain knowledge—is being slowly rolled into models, layer by layer. This layer of seniority is still real, but the premium on it is shrinking.

The second layer of senior is *has judged a lot*. Has judged, many times, when to stop, when to rewrite, when to trust the tests, when not to trust the tests. This kind of judgment cannot be reproduced and cannot be outsourced. It is forged in real failures and real postmortems. It is sharpened in real costs and real returns. It grows in real responsibility and real consequences. It cannot be substituted by an LLM, because it is not knowledge. It is judgment.

AI flattens *has done a lot*. A junior engineer with an LLM can, in a short stretch of time, brush up against scenarios that used to take many years to encounter. Three years in, the stacks they have touched, the volume of code they have moved through, the styles of code they have seen could exceed what someone with ten years of experience saw a decade ago. The threshold for *has done a lot* has been pushed down.

But *has judged a lot* is, for now, not substitutable. A junior engineer who has *seen* many scenarios through the LLM has not actually *carried responsibility* in those scenarios. They have not been on call for a production incident, have not been pulled out of bed at 3 a.m. to roll something back, have not paid a real price for a wrong call. That kind of forging only happens through time, inside real business. AI does not flatten this layer. If anything, growing system non-determinism is going to make it scarcer.

What this means is that *senior* will not be eliminated. It will be **reclassified**.

Whether an engineer recognizes which layer their seniority comes from is going to matter more and more. The ones who recognize it can move up into the upper layer in this repricing. The ones who do not will stand where they are and feel that the era cheated them.

The engineering capability of the AI era does not jump over the engineering capability of the rule-codified era. It **evolves out of it**. Without the solid engineering experience built up in the rule-codified era, judgment in the token-based era has nothing to stand on. This is exactly what the book has kept arguing: the past decade-plus of solid software engineering experience is, in fact, the most important capital for entering this new phase.

The problem is not that senior engineers' experience is going stale. The problem is whether they can recognize *the judgment piece* of their experience separately from the rest, weight it deliberately, and bring it back to the market for repricing. That is not the market's job. That is homework every senior engineer has to do for themselves.

## 6. Back to the engineer on the ground

For a working engineer, the way to see this clearly is not anxiety, not chasing tools, not racing to keep up with every new release. It is to take your own capability list off the shelf and recalibrate it against the new pricing mechanism.

Which lines are *I can do X*, where the next LLM release will also be able to do X? The premium on this line is shrinking. That does not mean drop it tomorrow. It means recognize that it can no longer be the largest piece of your value.

Which lines are *I can define a piece of work clearly*, *I can review*, *I can backstop drift*, *I can design the workflow*? The premium on this line is rising. It used to live invisibly inside daily work and was never separately named. Now it has to be recognized, named, and deliberately developed. The weight you put on the second line is what determines where, in two or three years, you can still stand in the market.

This is not a push to switch careers tomorrow. It is not a reason to throw away a decade of accumulation. It is an instruction to look at every day's work again. When you finish a piece of code, do you stop at *it works*, or do you stop at *I have written down a judgment about this work that another reviewer can audit, another teammate can backstop, another Agent can reuse*? The difference between those two stopping points is, on a five-year horizon, the difference between two kinds of engineers.
