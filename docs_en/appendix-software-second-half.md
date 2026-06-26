# Software Ate Only Half the World: From Rule-Based to Token-Based

The market has felt creatively stuck for a while now. No new category-defining product, no fresh wave of breakout software. The needs that are easy to write down already have something running against them. The ones still left—every team knows they exist, but nobody can put them into a clean PRD. They have real business value, yet the moment you sit down to write rules for them, the whole problem turns gray. Every case feels like *this one we have to look at by hand*.

The easy explanation is that software has entered a stagnation phase, or that the era of mode innovation is over. I do not think that is what is going on. I think software, as a business, has been running on a single track for decades—the track of rule-codification—and that track has hit its ceiling.

Then LLMs showed up, and the picture started to change.

But the change is not what most people seem to think it is. It is not *AI makes software smarter*, and it is not *AI replaces a slice of programmers*. Something more fundamental is happening at the layer underneath: the rule-codified track that software has been riding all this time is being widened, and a second track is opening up next to it. What this appendix is about is that second track.

## 1. Software has only ever eaten half the world

Marc Andreessen wrote his now-canonical essay *Why Software Is Eating the World* in 2011. The thesis kept getting validated for the next decade as software ate one industry after another. But if you read it again today, the line is only half right.

Software has never actually eaten the whole world. What it has eaten is **the part of the world that can be cleanly described by rules**. The other half has, quietly, never been touched.

Engineers know this in their bones, even if they do not usually phrase it this way. Every system any of us has ever shipped rests on the same hidden precondition: the thing being modeled has to be decomposable into steps, definable as states, expressible as a set of conditions. The parts you can decompose, you can ship. The parts you cannot, you write *handled manually by an operator* into the spec doc and move on.

Take a step back and look at what the last few decades of software actually consumed:

- Bookkeeping went into ERP, because double-entry accounting had already split every possible financial movement into a finite set of well-defined rules.
- Communication went into IM, because *deliver this string from A to B* has nothing in it that requires a moment of judgment—who, when, read or unread, all of it is a deterministic state.
- Information retrieval went into search engines, because the human notion of relevance was reduced to a computable set of signals.
- Getting from place to place went into ride-hailing apps, because the core structure of *A to B* is extremely stable.

Every single one of those wins passed through the same gate first: **the activity had to become rule-codifiable**. Things that decomposed into steps, that defined into states, that wrote into conditions—those got eaten. Things that did not decompose cleanly stayed outside.

This is not a stylistic preference. It is the foundational color of software as an engineering artifact. Debuggability, testability, auditability, the ability to be trusted with real responsibility—every one of those properties only exists because behavior is described by rules. The reason a piece of code can be trusted is that it does not think one thing today and another thing tomorrow. It runs the logic that was written. Rule-codification is the precondition for software becoming infrastructure, not some arbitrary aesthetic choice.

So the *software eating the world* thesis came with an unstated qualifier from the beginning: it was eating the part of the world **that could be made to behave by rules**. Domains that rule-codified cleanly, software ate deeply. Domains that did not rule-codify cleanly, software stood outside and watched.

## 2. Rule-codification can only cover half of human demand

Once you accept that, the next question shows up immediately: what is the other half?

It is not far from us. It is in our own daily work.

A product manager finishes a proposal. What they actually want is not better Word formatting. What they want is for someone to look at it and tell them whether the logic holds, whether there is a gap they did not see themselves. A lawyer gets handed a contract. What they actually want is not nicer PDF annotations. What they want is for someone to tell them which clauses hide the real risk. A product owner sees a launch underperform. What they actually want is not a BI query. What they want is someone telling them why the users are not buying. An engineer finishes a piece of code. What they actually want is not just *tests pass*. What they want is for someone to tell them whether this control flow actually holds up under their company's specific business reality.

**None of those needs has ever really been solved by software.**

Not because nobody wanted to. Each of them sits on top of a giant market—consulting, law firms, product research. They are all served, just not by software. They are served by humans. And it is not for lack of trying, either. Over the last decade-plus we have had wave after wave of expert systems, rule engines, decision trees, knowledge graphs—each one trying to push *the moment of judgment* into a system. Each wave produced demos in some vertical, but none of them generalized. The reason was always the same: **they could not be rule-codified**. Behind every concrete situation there is a moment of *let me think about this*, and *thinking* is not something you can write into an `if/else`.

That is the real answer to a lot of the questions hanging over the industry. Why are software companies competing so hard on operations, growth, and user experience these days? Not because PMs got lazy. Because the pool of rule-codifiable demand is running dry. Whatever could be digitized has mostly been digitized; everything left is *somebody has to think about this*. Rule-codification cannot chew it, so the only move left is to grind harder on the half already eaten—optimize the UI, shorten the funnel, lift retention. That has value, but it is no longer expansion into new territory. It is intensifying farming on land that has already been cleared.

Why do SaaS companies hit a hard wall above some scale? Because the demand they can actually serve is bounded. Every customer runs through the same rules, and whatever those rules cannot cover gets pushed back to the customer to handle, or to a services team flown in on-site. Every additional non-standard customer adds a piece of specificity the product cannot absorb. That specificity is, at root, the part rule-codification cannot cover.

Why have consulting firms, law firms, therapy, and medicine been almost untouched by software? Because their core deliverable is *a moment of judgment*. A consultant's value is not the tool they use to produce the deck. It is that, faced with your specific company and your specific problem, they form a judgment in the moment. That judgment cannot be pre-written, because it is being thought through right now, in front of you.

The rule-codified track stops here. It is not just hitting a wall in some particular product. It is hitting a wall along an entire supply path. Everything still on the other side of that wall requires *someone to think about this*, and *thinking* has, until now, never been something you could supply at scale.

## 3. Tokens make "thinking" a schedulable resource for the first time

This is what LLMs actually change.

But the change is not the one most of the discussion is about. Yes, models are smarter. Yes, parameter counts are bigger. Yes, benchmarks are higher. Those are real technical facts, but they are not the load-bearing variable in this wave. The load-bearing variable is that, for the first time, software has a way to handle **domains that cannot be rule-codified**.

The word *token* is easy to mistake for an AI billing unit, like CPU-seconds or bandwidth. Its real meaning is bigger than that. Behind a single token sits one inference step. The model reads everything in its context, runs a piece of processing that cannot be fully described by rules, and turns it into an output. That output may be a piece of text, but it is also a judgment, a classification, a decision.

What that means is that a token is **a piece of thinking, sliced down to a small, measurable, purchasable unit**.

That was not possible before. If you wanted a piece of thinking embedded inside a digital workflow, the only option was to hire a human. Humans have shifts, moods, salary structures, and hiring overhead. *Thinking* could not be supplied on demand the way electricity is. The smallest deliverable unit of thinking was a whole human being joining the team.

Tokens come closer to on-demand thinking than anything we have had. Need one judgment? Make one API call. Need ten thousand judgments? Make ten thousand API calls. Need to embed a moment of thinking inside a sub-second response path? Possible. Need to call thinking repeatedly inside a long-running process? Also possible. The quality of that thinking may not match a senior expert, but its *schedulability* is something no previous form of thinking ever had.

For the last two years Jensen Huang has been narrating a layered compute stack on stage—electricity, datacenters, models, applications on top. The supply side of that stack is well-told: cheaper compute, stronger models, more applications. What does not get said as cleanly is what that stack ends up *producing*, what it actually changes. If we have to pin a destination on it, it is this: **what the stack ultimately outputs is a new kind of thinking, available on demand, callable from anywhere**.

So the *software eats the world* story now has a second track. It is just getting started, and it is not running on rule-codification. It runs on turning *the moment of judgment* directly into a schedulable resource, and through that, opening up the demand that rule-codification could never cover.

The two tracks do not replace each other. Whatever rule-codification can eat keeps existing in the rule-codified form, because there is no reason to switch. But **the half that rule-codification could not cover** is finally starting to give.

A lot of products used to leave *the judgment step* blank for the user to fill in. Resume screening is the canonical example. The HR system stored resumes and ran keyword filters; whether a candidate was actually a fit was something the human recruiter had to read and decide. That step can now be filled in. The system can produce an initial judgment about whether this candidate fits, and the recruiter makes the final call on top of that. The same pattern shows up in contract pre-review, in report summarization, in customer-service triage, in content moderation. The places where *judgment-cannot-be-codified* used to mean *push it back onto the human* are starting to have a software path.

Users used to translate themselves into the software's shape before talking to it. Want to search? Figure out the keywords first. Want to query data? Decompose the question into menu options first. Want the system to perform an action? Express it in the form the system understands. That translation step was always carried by the user, because the software had no way to handle a request that had not been pre-translated. Tokens can now do that translation. The user states the need in natural language, and the system runs a moment of thinking in the middle to convert it into something it can act on. On the surface this looks like a UI improvement, but what it actually opens up is the entire band of demand that used to be lost because *the user could not translate*.

The long tail used to be unreachable. Every user's specific situation was different, rules could not cover all of them, serving the big customers meant abandoning the small ones, serving the mainstream scenarios meant skipping the edge cases. Building a product meant cutting requirements, cutting the long tail, keeping only what one rule set could cover. The long tail is finally reachable, because tokens can **think a judgment for this specific situation in the moment**, instead of forcing you to enumerate every situation up front. That does not mean the long tail will all be eaten tomorrow. It means the path now exists.

## 4. Every AI product right now is using the LLM to simulate a person

Once you grant that this second track exists, the next question is: what should software *on* that track look like?

If you scan the current market, the answer is unanimous: an Agent.

Whether the marketing label is *AI assistant*, *agent*, *Copilot*, or *digital employee*, the underlying logic is the same. Give it a role definition. Give it a job description. Give it a set of tools. Then have it do what a human in that role would do—pick up tasks, think, call tools, produce output. AI customer service plays the support rep. AI programmer plays the engineer. AI sales plays the BD. AI researcher plays the analyst. The whole industry is acting as if the most natural thing to do with this new capability is to pour it into a virtual person.

If only one or two companies were doing this, it would be a product decision. When everybody is independently doing it, it is worth stopping to ask: **why a person?**

A big part of the answer is that, before LLMs, *thinking* only had one container we knew how to imagine—a human. We did not have another reference model. So the moment a new, schedulable form of thinking shows up, the first thing we reach for is the most familiar shape: a virtual person, with a role, a context, a task, an output.

This use is not wrong. It is the closest landing point that this new track can support today, and it does work in many scenarios.

But it is **almost certainly not the end state**. It looks more like the first form on this track—the one we, this generation, came up with under the constraint of our own mental habits. Look back at this in a few years and the screen full of *Agent products* today will probably look very far from what mature usage of this track ends up looking like.

There is a piece of not-too-distant history that makes the point.

## 5. It took electric motors forty years to stop being just a better steam engine

After the steam engine became widespread, factories still tended to be built next to rivers. That sounds backwards—the whole point of a steam engine was that it freed you from water. The reason was that for the previous few hundred years, factories had only one organizational shape: built around a waterwheel. The wheel sat on the river. Power came out of it through a central drive shaft, and belts distributed that power to each individual machine. When the steam engine showed up, the first thing factory owners did was *not* redesign the factory. They put the steam engine where the waterwheel used to be, drove the same central shaft, ran the same belts. **The steam engine was used as a better waterwheel.**

Then came electric motors. Physically, an electric motor is nothing like a steam engine. It can be made small. It can be deployed in a distributed way. Every motor can run independently. So what did factories do the first time they got electric motors? They put one in the middle of the factory, drove the same familiar central drive shaft, and ran the same belts out to the workstations. **The electric motor was used as a better steam engine.**

The factory owners were not stupid. They had simply never seen any organization other than *central power source plus belt distribution*. New energy got dropped into the old usage pattern, and the productivity gain was modest.

The real shift took something like forty years. Someone started installing a small motor on each machine tool individually. That step looks tiny, but it opens up an entirely different possibility: power no longer has to be centralized and then distributed; **it can sit directly at the place that needs it**. Once that pattern took hold, the physical layout of the factory was suddenly free. Machines no longer had to line up along a drive shaft; they could be arranged according to the process flow itself. The assembly line became possible. Ford's assembly line and the entire order of modern manufacturing all start from this step.

The real revolution of the electric motor was not that it replaced steam. It was that someone finally figured out that *power can be installed wherever it is needed*.

What we are doing with Agents right now is fundamentally building thinking-virtual-employees. One Agent per workstation, one role per job description, tasks come in one end and outputs go out the other. This structure maps almost one-to-one onto a human org chart. It works, but it does not actually take advantage of what tokens are: **thinking that can be sliced down to tiny units, embedded in any position, supplied on demand**. The Agent re-packages all of that back into the container called *a person*.

This is not a knock on Agents. They are clearly useful today, and they will keep being useful for a long time, the same way central-motor factories ran for decades. But almost certainly they are not the final form.

## 6. Further out, software may stop looking like a person

If Agents are not the destination, what is? Nobody can say for sure, the same way nobody in 1890 could have pictured Ford's assembly line. But pushing on the analogy, you can faintly see a few directions.

**First, thinking may go from packaged to distributed.** Today we package tokens into an Agent because we need a complete role to plug into a real-world job. Once the engineering practice matures, tokens can sit directly where small motors sit—on every individual judgment point in the software. Behind every `if/else`, behind every place that today says *handled manually by an operator*, you can hang a fresh in-the-moment judgment. Software is no longer *rules in the core, Agent strapped on the side*. Rules and judgment are deeply interleaved, and you can no longer cleanly point at where the code ends and the model begins.

**Second, the line between mainstream flow and long tail may dissolve.** Building a product used to mean cutting requirements, because the cost of rule-codification was fixed and could only cover the mainstream; the long tail had to go. Agents softened this a bit—you could let an Agent backstop the requests rules did not cover. But it is still essentially a layered structure: *mainstream on rules, long tail on Agent*. Further out, if judgment really can be diffused into every individual node, the engineering cost gap between mainstream and long tail starts to flatten. The long tail no longer has to be treated specially, because it is already absorbed in the in-the-moment judgments scattered across the system. The range of customers a single product can serve could open up dramatically.

**Third, rule-codified infrastructure is not going away, but its role gets reorganized.** Databases, message queues, config systems, rule engines—none of that disappears because of tokens. They are still the substrate that makes software trustworthy. But their role in the new paradigm shifts: from *carrying the main flow* to *carrying the deterministic skeleton*, while the layer above is reorganized by distributed judgment units. Rules backstop. Tokens reason through. The two interleave into a new shape of software. That shape does not have a clean name yet, but it is being felt out, piece by piece, in the wild right now.

These are directional guesses, not predictions. The actual form, the actual timing, the actual people who will build it first—nobody knows. The thing not to do is treat today's Agent as the end. The current product surface is not the same thing as the trajectory of the track.

## 7. The next decade has just started

Back to where this started. *Software eats the world*, as it was said in 2011, was only ever half right. Software has never eaten the whole world. It has eaten the part of the world that could be cleanly described by rules. The other part—the demands that need *a moment of judgment* before they can be handled—has been sitting outside the whole time, because it could not be rule-codified. That is not a failure of software. It is the limit of software as an engineering artifact. Rule-codification is where its power comes from, and where its ceiling sits.

What LLMs change is exactly that ceiling. Not by making software smarter, but by giving software a second path: eat the demand that rules cannot digest, and eat it through tokens. The new path does not replace the old one. They will run side by side, each handling what each can handle. But the territory software can reach into starts expanding, for the first time, beyond rules.

This is not going to happen quickly. The road from *can be digitized* to *willing to use it*, from *willing to use it* to *willing to entrust it*, from *willing to entrust it* to *able to audit it*—rule-codified software took decades to walk it. Token-based software will probably walk a similar shape, and we are at the very beginning of that road. Every AI product visible today, no matter how dazzling, is still an extremely early form. To actually push this path through requires not just stronger models, but the entire engineering discipline around the model: evaluation, guardrails, observability, audit trails, accountability. Every constraint, every architecture, every engineering practice this book has been working through is, underneath, paving exactly this road.

The trajectory described here also has a direct consequence for the people who make software for a living. If half the world that software could not previously eat is finally getting a path in, then the kinds of capability the industry pays for are going to shift along the same line. That is the subject of the next appendix.
