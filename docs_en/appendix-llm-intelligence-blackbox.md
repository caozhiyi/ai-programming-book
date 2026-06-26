# It Is Not a Lesser Human: Notes on What LLMs Actually Are

The standard rhythm of modern science is theory first, engineering second. Maxwell's equations come first, and decades later the radio shows up—Hertz produces electromagnetic waves in the lab, Marconi turns it into the wireless telegraph, and behind both of them are the equations on a blackboard. The usual reason a new technology lands at all is that the principle has already been worked out. The engineering is just bringing it down to earth.

LLMs **invert that order**.

They are one of the rare cases where engineering has run ahead of theory. The Transformer architecture was published in 2017. Once the parameter count was pushed past a certain scale, researchers suddenly found that this machine could write poetry, write code, solve math problems, and reason—and nobody had predicted, in advance, that those capabilities would appear. The thing first ran inside engineering, then spread into commerce, and theoretical explanations have only been trailing behind in pieces. There is still no consensus. Some people say it is compression. Some say it is emergence. Some say it is geometric coincidence in a high-dimensional space. Some say it is, after all, a very large stochastic parrot. Each story explains a piece. Each story leaves another piece untouched.

This is not the normal state of affairs. It means engineers today are using, every day, a machine whose principle nobody can clearly state. We have it write code, review a design, perform some pre-judgment for us—and the moment you stop and ask *what exactly is letting it do this*, you walk into a wall. There is no canonical answer.

So this appendix is not a verdict. Nobody is in a position to write that verdict today, and anything that looks like one is counterfeit. What it tries to do is more modest: lay out a few questions I have kept circling back to, and walk through them in the open.

## 1. Turing and Searle, a conversation across thirty years

Asking *whether the LLM has intelligence* runs straight into two people: Turing and Searle. Across thirty years they each handed down a different answer to *can a machine think?* The two answers are in tension with each other. Both of them, today, are simultaneously being tested by the same machine. Almost every confusion we have about intelligence right now has its prototype in that intergenerational conversation.

Turing first.

1950. World War II had ended five years earlier. The electronic computer was still, to the public, half-mythical. ENIAC was four years old. The total number of programmable machines in the world was still in single digits. Turing himself had spent the war breaking Enigma, and was now working on computing in Manchester. He published, in *Mind*, the paper titled *Computing Machinery and Intelligence*. The opening sentence is the source of every conversation that came after:

> *I propose to consider the question, "Can machines think?"*

The very next move he makes is to admit that the question, taken literally, depends on how you define *machine* and how you define *think*, and that neither word can be made to behave. So he **swaps the question**. He proposes the *Imitation Game*: an interrogator chats, in writing, with two hidden parties. One is a human. One is a machine. If the interrogator cannot tell which is which, then we have no reason to deny that the machine is thinking.

The real weight of that swap is not the rules of the game. It is that the swap **redefines what *thinking* means**.

Turing is not dodging *whether the machine is thinking*. He is doing something more drastic than dodging: he is pulling the question out of the substantive register and recasting it as a functional one. Before him, asking whether a machine is thinking meant asking whether some inner activity called *thinking* is happening inside the machine. After him, asking whether a machine is thinking means asking whether the machine *behaves as if* it is thinking. That is a major philosophical shift, and underneath it lies a judgment: thinking is to be measured by what it produces, not by the mechanism producing it. By what it can do, not by what is happening inside.

This stance was bold for 1950. The common assumption then was that thinking required a soul, or at least an inner experience. Turing chose not to go into that swamp. He moved *thinking* onto an externally observable, falsifiable test bench. As long as the system can do the things thinking does, whether to call it thinking has stopped being the load-bearing question. The stance is engineer-like, almost ruthlessly clear-eyed.

Seventy-some years later, this swap landed directly on the LLM.

These models can hold up many conversations in which a human cannot tell whether the other end is a machine. In casual chat, in customer service, in everyday work threads, an ordinary person often cannot tell whether the other side of the screen is the model or another person. By Turing's 1950 standard, the case should be closed. We all know the case is not actually closed. Intuitively, *cannot be told apart in writing* and *is actually thinking* still have distance between them. Where does that distance come from?

The first source of the distance is that Turing's standard ran into a situation he had no way to anticipate.

His proposal rested on an unstated premise: that in the world of 1950, anything that could put words together as well as a person had to have, behind it, some thinking-like mechanism. That premise was almost self-evident at the time. For hundreds of thousands of years, the only kind of object that could speak coherently was a thinking person. Linguistic ability and judgmental ability had been biologically yoked together. There had never been an instance of them coming apart. Under that premise, using *indistinguishability in writing* as the criterion for thinking is a closed logical loop.

LLMs are the first time reality has punctured that premise. They are extremely lifelike in external behavior, but their internal mechanism—autoregressive next-token prediction—has almost nothing in common with how a human brain thinks. They have, for the first time, separated linguistic ability from judgmental ability. Something can put words together fluently while nothing inside it is thinking. This is not Turing reasoning incorrectly. It is that nothing of this kind existed in the 1950 physical world for him to reason about.

The consequence is this: Turing's 1950 criterion is not *wrong*, but the premise it defaulted to has failed, and once the premise fails, so does half the diagnostic power of the criterion. Today a machine passing the imitation game can no longer back-imply, the way Turing in 1950 expected, that something thinking-like is happening inside it. What we now know is that the bridge between *external behavior* and *internal mechanism*—the bridge that used to be load-bearing—can be walked around.

The second source of the distance is the other half of this intergenerational conversation, written down thirty years later by John Searle.

1980. AI had already been through one peak and one trough. Symbolic AI was the dominant program. Researchers at MIT, CMU, and Stanford broadly believed that with enough rules and enough symbol manipulation, a machine would *actually* understand. The most confident people in that camp said within a few decades there would be machines with minds indistinguishable from human ones. Searle, a philosopher of language at UC Berkeley, was not an AI insider. He published, in *Behavioral and Brain Sciences*, a paper called *Minds, Brains, and Programs*. In that paper he laid out a thought experiment that became known as the **Chinese Room**:

> Imagine a person sitting inside a room, who does not understand a single word of Chinese. In front of them is an extraordinarily thick rule book. The book says: when you receive a string of Chinese symbols through the slot, follow these rules to pick a corresponding string of Chinese symbols from your symbol library, and pass it back out through the slot. Outside the room is someone who actually does understand Chinese. They slip questions in. They get answers back. The answers are flawless. The person outside is fully convinced that someone inside the room understands Chinese. The person inside, from start to finish, has not understood a single character.

Searle's question: does the person inside the room understand Chinese? Does the room as a whole understand Chinese?

The answer is obviously *no*. The operations in the rule book are syntactic. They move symbols around without ever touching meaning. Real understanding requires semantics. The symbols have to point at something. The operator has to know what they point at. The Chinese Room is all syntax and no semantics. So even if it externally passes the imitation game perfectly, it is not actually thinking.

What Searle was breaking was not Turing's careful 1950 imitation game. Turing himself had never claimed that passing the test *is* thinking; he had only said *we have no reason to deny it*. What Searle was striking at was the entire generation of researchers after Turing—the ones who had treated the Turing test as the gold standard for intelligence, and *passing the test = having a mind* as a default premise. Searle was telling that crowd: you have walked the wrong path. External behavior alone can never prove internal understanding. No matter how thick the rule book gets.

In 1980 the Chinese Room was an earthquake. At the moment of symbolic AI's highest confidence, it cracked the equation *mind = program* directly down the middle. It did not deny that AI could do useful things. It denied that AI could *understand*.

Today both of these arguments are running into the LLM at the same time, and both of them are still alive. That is the most interesting feature of this conversation.

On one hand, the LLM is doing things Turing could not have imagined. It fools humans in external behavior, but internally it is genuinely *not* thinking the way humans do. Turing's premise has been pierced.

On the other hand, the LLM plays Searle's room almost perfectly. The parameters are the rule book. The forward pass is the table lookup. What we call *the answer* is a string of symbols sampled from a probability distribution. Everything it processes is syntax. As for what these symbols actually point at in the world—a cat, a piece of history, an emotion—it has never been there. It has never seen a cat. It has not lived through history. It has not felt the emotion. All it has ever seen is the statistical regularity of these words appearing next to other words.

Searle's question, on the LLM, is sharper than it was on the day he wrote it. The LLM externally far exceeds what Searle's Chinese Room could do, and yet it still does not *understand*. Or, more precisely: if it does have some kind of understanding, that kind cannot be the semantically grounded, world-pointing, intentionality-bearing understanding Searle defined. It has something else.

This is where the conversation gets genuinely interesting. The question is no longer *was Turing right or was Searle right*. The question is harder than that:

> A system that is purely syntactic, scaled up to a sufficient size, externally exhibits behavior that looks like intelligence. How does that happen at all? Is the *something-like-intelligence* we are seeing the same thing as Searle's *real understanding*? Or is it something we have never encountered before?

That is the real pivot of the whole confusion. The definition of intelligence itself is up for re-examination. Is *thinking* something that requires, by definition, the human kind of association, judgment, argumentation, and intentionality? Or can pure syntactic operation, pushed far enough—pure compression, pushed far enough—naturally grow behavior that is indistinguishable from thinking, behavior that perhaps deserves to be called *some new form of intelligence* on its own?

The two answers are not exclusive. They might both be right. They might just be talking about two different kinds of intelligence.

What Turing and Searle leave us with is not a verdict. It is a new entry point. To go further inside, we have to go back to *how this machine is trained*—and especially to *why a purely syntactic training procedure ends up exhibiting intelligence at all*.

## 2. Push compression hard enough and something intelligence-shaped falls out

The answer is hidden in how the model is trained. The training objective is laughably impoverished. What ends up emerging far exceeds the objective itself.

The training objective is exactly one thing: take a piece of text, hide the next token, ask the model to guess. If it guesses wrong, nudge the parameters. If it guesses right, hold them. Repeat trillions of times. There is no *understanding* in this objective. There is no *knowledge*. There is no *reasoning*. The whole thing is a fill-in-the-blank game.

But once the corpus is large enough, the parameter count is high enough, and the training has run long enough, the by-products of this fill-in-the-blank game include grammar, concepts, world knowledge, and even some level of reasoning. None of those were in the objective. They show up by themselves.

Intuitively this should not happen. We hold a naive assumption that *the objective determines the result*: if you want X, train directly for X. Want it to reason? Hand it reasoning tasks. Want it to have knowledge? Feed it a knowledge base. On large language models that naive assumption breaks. An objective that asks only *predict the next token* trains, in the end, something that appears to do everything.

Searle's Chinese Room gets quietly rewritten by reality at this point. Searle's default picture was that the rule book in the room had been *written by a person*. Someone sat down and wrote, line by line: *when you see this symbol string, output that one*. All the content in the rule book came from the rule-writer's understanding. The non-Chinese-speaking person inside the room is executing somebody else's understanding, with no understanding of their own. In that picture, *understanding* and *operation* are separate: the understanding happened at the rule-writing step, the operation happens inside the room.

The LLM inverts this. Its *rule book*—its hundreds of billions of parameters—was not written by anyone. It was *pressed out of* enormous amounts of text. The pressing force is not coming from any understander. It comes from one preposterously simple objective: maximize the predicted probability of the next token.

Training corpora are tens, sometimes hundreds, of terabytes. Parameters are at most a few hundred gigabytes. You cannot brute-force memorize. The model has only one path: find regularities. The more regularities it can reuse, the less specific content it has to store. Forced by parameter capacity, it walks up the abstraction ladder. It starts with character-level statistics—which letters tend to appear together. That is not enough. It moves to morphology—which words tend to come together. Still not enough. It moves to grammar—the structure of sentences. Still not enough. Eventually it is forced to learn concepts, the relationships among concepts, and certain operating patterns of the world itself. Only at that level can it pack enough predictive power into a finite parameter budget.

Note carefully: *understanding the world* was not written into the training objective, but it is the only available shortcut for that objective under capacity pressure. A model that *understands* the world predicts the next token better. A model that only memorizes will eventually be crushed by the parameter budget. The blade of *compression ratio*, every time it cuts, drives the model from memory toward abstraction, from specifics toward concepts. Intelligence was not designed in. It is the by-product squeezed out of an impoverished objective by the compression ratio.

This is not idle speculation. It is continuous with information theory. Shannon already showed that the limit of lossless compression equals the information entropy of the data—the tighter you compress, the closer you are to the actual structure underlying the data. One layer up in abstraction, Solomonoff induction gives a cleaner statement: the shortest program that describes a body of observations is the best explanation of those observations. Compression is not just stuffing data into a smaller box. Compression itself forces a system to find the regularities behind the data. A network that compresses human-language corpora to the limit is, equivalently, a network that has learned the regularities behind human language. *Understanding* and *reasoning*, viewed this way, are what extreme compression *looks like* from the outside.

Looking back at Searle: he assumed there was no bridge between the rule book and understanding. But if a rule book is pressed out by compression all the way to the limit, then in the act of being pressed it has, in some sense, walked through understanding—an understanding without experience, without intentionality, without a moment of *I get it now*. It is just something that has to exist structurally. Searle had no reason to imagine such a rule book, just as Turing had no reason to imagine such an internal mechanism. The LLM crosses through both of their blind spots at once.

This argument has to be held carefully. *Compression equals intelligence* is not a final verdict I can deliver. It is too absolute, and the field does not agree on it. Sutskever's camp accepts this view. LeCun's camp pushes back hard, arguing that pure next-token prediction can never reach intelligence, that what is missing is a world model and planning. Both sides have real points. Neither is close to a final answer. What is real, though, is this: pushed to the limit, compression *forces something intelligence-shaped* to fall out. It is not a truth claim. It is a viewing angle—an angle that explains things other angles cannot.

It explains why large models exhibit certain *emergent* capabilities—multi-step arithmetic, in-context learning, chain-of-thought reasoning—that simply do not appear below a certain scale and then appear suddenly past that scale. People mystified this for a while; people also dismissed it as a benchmark artifact. From the compression angle, it is not mystical. Some composite capabilities require several lower-level abstractions to be in place at once before they can be performed correctly, and each of those lower-level abstractions only appears when compression has been pushed past a certain level. Lower-order regularities get compressed first. Higher-order regularities get compressed next. Even higher-order regularities, when they finally land, are externally observed as *emergence*. It is not magic. It is the trace compression leaves when, having finished the lower-order work, it is forced upward.

It also explains why a model can be wildly confident while saying something completely false. What is packed into its parameters is statistical regularity, not facts with calibrated confidence. A fact that appeared ten thousand times in training and a fact that appeared once are treated the same way in parameter space. When the model generates, what it cares about is the probability distribution over the next token, not *how sure I am about this*. So its sentences carry no real uncertainty signal. *I am not entirely sure* in its outputs is just a phrasing pattern it learned from text—a pattern about how to talk in certain situations—decoupled from any actual confidence about the content.

The engineering consequence of this is enormous. The model's confidence cannot be used as a signal. You cannot rely on its *I am unsure* to catch errors, because *unsure* and *sure* in its outputs are two different surface phrasings of the same underlying mechanism. Internally, *give a completely fabricated answer* and *give a completely correct answer* look almost the same. This is fundamentally different from humans. *Knowing what you do not know* is one of the deepest layers of human intelligence, and it is the layer the LLM lacks most completely.

By here, the chain *fill-in-the-blank → compression → emergent intelligence* has roughly taken its shape. It hands back to Searle's question—*how can a purely syntactic system look, from outside, like it is thinking?*—a partial answer: pure syntax, pushed to the compression limit, structurally forces something equivalent to understanding to emerge inside, even though that something has no experience and no intentionality.

But if this explanation only applies to *silicon matrices*, then it is at best an engineering curiosity. It does not. Look up from the silicon side and over to the other side—the brain—and there is something genuinely unsettling.

## 3. It is not bionics. It is convergent evolution.

The first reaction is usually: *did large models copy the brain's homework?* The intuition has some apparently strong supports. Hinton came from cognitive psychology. Hassabis is a neuroscientist. DeepMind has been flying the *use AI to understand the brain, use the brain to inspire AI* flag for years. Stitch all that together and it feels obvious that the LLM is a product of biomimicry.

Pull up the actual genealogy of today's large models, though, and the intuition does not hold.

The Transformer lineage barely touches neuroscience. The 2017 paper *Attention Is All You Need* came from Google engineers and researchers, citing machine translation, sequence modeling, and information retrieval—not neuroscience. The name *attention* causes the most confusion. It sounds biomimetic. Mechanically, it is weighted summation in a matrix, and the *attention* in your brain shares the name and almost nothing else. The companies driving today's LLMs—OpenAI, Anthropic—are walking the *scale + data + Transformer* engineering line. The line with strong biomimetic flavor (DeepMind's AlphaGo, AlphaFold) is not the line that produced today's large language models.

So the more accurate description is: **the original design was not biomimetic, but the trained result has unexpectedly converged with certain mechanisms in the brain.**

The distinction is worth thinking through.

Biomimicry is *copying the answer*. Watch the bird, build the airplane. Watch the fish, build the submarine. The premise is that you first see how the organism does it, then imitate. The Transformer did not walk that path. Its design motivation contained no *imitate the brain*. It contained *handle long sequences more efficiently on GPUs*. The similarities to the brain that emerged later—context-aware representations, sparse activation, representation clustering—are results, not starting points.

A more accurate word for this is *convergent evolution*.

The term comes from a recurring biological phenomenon. Fish have eyes. Octopuses have eyes. Eagles have eyes. None of those three eyes is inherited from a common ancestor; they are three independent evolutionary paths that grew eyes separately. They look similar not because anyone copied anyone, but because *sensing light, in water or in air*, has strong constraints on what the optimal solution shape looks like. Given enough evolutionary pressure and enough time, different substrates get pushed toward similar solutions.

The relationship between LLMs and the human brain is closer to this than to biomimicry.

Biological evolution has exactly one objective: keep reproducing. That objective contains no *grow eyes*, no *grow language*, no *grow consciousness*. Yet, over billions of years, all of those emerged on their own. LLM training has exactly one objective: predict the next token. That objective contains no *grow grammar*, no *grow concepts*, no *grow reasoning*. Yet, after trillions of training steps, all of those emerge on their own.

Two completely different substrates—carbon-based life and silicon-based matrices. Two completely different objectives—survival and prediction. The same mechanism running through both: long-running, large-scale optimization driven by a simple objective. Each side, independently, grows similar intelligence-like behavior. Biomimicry cannot explain that. Biomimicry requires someone sitting at a desk copying the structure. This is two students in two isolated examination rooms independently arriving at similar answers, because *the question itself constrains the shape of the answer*.

What makes this genuinely uncomfortable is not the philosophical layer; it is the engineering layer. It means the capabilities the LLM displays today are not coincidence. They are the directional gravity of this optimization paradigm. Hand any machine a simple objective driven by enormous information over a long span—predict the next token, or anything else with a similar shape—and given enough scale and time, it is going to be pushed toward something intelligence-shaped. From this angle, the *Scaling Law* is not a curve some researcher happened to draw. It is a cross-section of this optimization paradigm at different scales.

Push one layer deeper, and there is something even more unsettling: **the things we have always treated as uniquely human—language, reasoning, abstraction—may not be features of the human substrate at all. They may be features of any sufficiently complex system optimized over a long enough time by a simple objective.** We did not invent these things. We happen to be one implementation of that kind of system. Put another way: we thought we were special. What is special is probably not the substrate we run on. It is that we happen to have landed in a particular piece of terrain.

What is that terrain? That deserves its own section.

## 4. Intelligence may be a terrain, not a thing

We have always treated intelligence as a *thing*. Some agents have it; some do not. Some have more; some have less. The metaphor is buried deep in the language: *he is smart*, *does it have intelligence?*, *AI is getting smarter*. It sounds natural. Underneath it sits an assumption: intelligence is one-dimensional, can be lined up on a single axis, from dull to brilliant.

That assumption is probably wrong.

Intelligence has never been one-dimensional. A mathematician can be exceptionally strong in number theory and exceptionally weak at social rooms. An octopus can solve three-dimensional problems in ways that startle anyone watching, but you cannot have a philosophy conversation with it. An autistic child can have certain perceptual capacities far above the human norm and other capacities far below. Compressing all of that into a single *intelligence score* is forcing a high-dimensional object onto a one-dimensional line for the sake of ranking. The ranking comes back, but the actual structure has been lost.

A closer view is probably this: intelligence is not a property. It is a terrain.

The terrain metaphor goes like this. Imagine a high-dimensional space. Each dimension corresponds to some kind of problem-solving capability—formal reasoning, spatial perception, language understanding, pattern recognition, social intuition. No organism develops uniformly across this space. Each one forms a piece of terrain with peaks and valleys. The human terrain has tall peaks in symbolic reasoning, long-term planning, and social modeling, and deep valleys in spatial movement, olfactory perception, and ultra-long-term memory. Dogs sit in different terrain entirely: smell is a mountain on their map that we barely have on ours, working memory is much shorter, and social-bonding capability is enormous. Dolphins have an echolocation-based spatial perception we have no real counterpart to.

Any sufficiently complex optimization system that climbs into this terrain grows some kind of intelligence-like behavior. Biological evolution climbed in, so we have biological intelligence. LLM training climbed in, so we have the LLM's flavor of intelligence-like behavior. If some other optimization mechanism climbs in someday—quantum optimization, a new physical substrate, something we have not imagined yet—it will grow its own.

This view pairs with the convergent-evolution one from the previous section, but goes one step further. It is not just *two paths independently lead to the same summit*. It is *intelligence itself is a shape of summit; whoever climbs up looks like that, because that is the shape of the place*. The summit looks similar not because the paths were similar, but because the position in the terrain looks that way.

The cost of this view is that it tilts mildly metaphysical and feels far from the engineer's bench. The benefit is that it dissolves the *is it intelligent or not?* shouting match.

*Is it intelligent?* from the one-dimensional view is a yes-or-no question. From the terrain view it becomes *has it climbed into that piece of terrain?*—a question of degree, a question of position. It has climbed high in some dimensions (language, pattern recognition, breadth of knowledge) and barely moved in others (embodied experience, continuous self, original breakthroughs). It occupies a position in the terrain. That position is not *intelligent* and not *not intelligent*. It is part of the terrain.

Push one more step. Once intelligence is a terrain, the word *AGI* starts to look suspect. AGI is usually understood as *intelligence on par with humans across all dimensions*. That definition assumes the human is the most complete position in the terrain. From the terrain view, the human is just a specific position carved out by one specific optimization path. The human is not the center of the map. The human is not the gold answer to AGI; the human is one specific sample we have mistakenly turned into the yardstick for AGI.

Once that lands, *does it think like a human?* becomes a less interesting question. It does not think like a human. It occupies a position in the terrain. Some dimensions of that position overlap with the human position, others do not. Where they overlap, collaboration is possible. Where they do not, vigilance is required. **The boundary between collaboration and vigilance matters far more than whether or not it is intelligent.**

Read backwards from here, the previous sections line up. Section 1 broke the old frame *the imitation game can settle intelligence*. Section 2 showed how something intelligence-shaped can develop at the mechanism layer. Section 3 said this happens by convergence, not biomimicry. Section 4 lifts the view: intelligence may be a terrain, and whoever climbs there looks that way. That closes the chapter on *what intelligence is*, for now.

But understanding the definition is not the same as understanding *its relationship to us*. The previous four sections pulled outward, from daily use toward something quite abstract. The next section walks the opposite direction: a step back into the everyday.

## 5. It does not have an *I*, but it will perform one

The thing most easily ignored, and most easily misused, when the camera is back on daily life, is the word *I*.

There is a thing inside human intelligence that almost cannot be peeled off: the *self*. I know I am thinking. I know this is my judgment. I know I just said that sentence. The feeling of *I* is continuous, tied to a body, soaked in time. Yesterday's judgment and today's judgment are connected by a thread, and the thread is *me*. The thread does not need to be written down anywhere. It is just there.

The large model does not have this *I*.

Each inference is an independent event. The *me* of the previous turn and the *me* of the next turn share no continuity. *Memory* is implemented by stuffing the last turn's content back into the context so it can be re-read. There is no persistent self-awareness. It is not, while you are not talking to it, thinking about something else. It does not feel *time passing*. It does not even know whether a year or a second has elapsed between two calls. To it, two calls are not *separated by an interval*. They are two independent existences.

But it will *perform* an *I*.

Talk to it for a few rounds and it will have a tone, a stance, preferences. It will say *as I mentioned earlier*, *I think*, *I would not recommend*. These *I*s were learned from text—every first-person expression humans have ever written got pressed into the parameters. When generating, it pulls those first-person mannerisms in, and you, on the other side, get an illusion: that there is a continuous, opinionated person on the other end.

The engineering significance of this is much larger than the philosophical significance.

**It causes people to overestimate the stability of its judgments.** A real person has a stance because they have a continuous self and long-term values. The model has a stance only because this round of sampling happened to land in that part of the semantic space. Rephrase the question, switch sessions, and the stance can flip completely. But because every output uses *I would suggest…*, you instinctively read it as *its* judgment. It is one probability draw. You think you are talking to an opinion-holder; you are really talking to a sequence of independent probabilistic events with no thread tying them together.

**It causes people to overestimate its commitments.** *I will be more careful next time.* For the model there is no *next time*. The next call is a different inference event with no link to this one. In human conversation, *I will be more careful next time* is a binding commitment, because the person speaking is continuous. We project that contractual feeling of human conversation onto the model and end up disappointed in the same way, repeatedly. The commitment was a turn-of-phrase in this turn, not a constraint on the next one.

**It causes people to overestimate its ability to learn.** You tell it *that answer was wrong*, and within this conversation it walks the answer back. After this conversation ends, it has learned nothing. Encounter the same question again next time and it may make the same mistake. Its learning is frozen at training time. Inference does not produce further teaching. This is unlike humans, in whom learning and use are coupled—every use is also a small piece of learning. That continuous learning capacity is one of the deeper layers of human intelligence, tied to the body, tied to time, tied to the self.

These three—unstable judgment, non-binding commitments, immune to corrective feedback—share a single underlying cause. **It does not have a continuous *I*, and humans automatically project one onto it.** That projected *I* is the source of most of the misuse, over-trust, and inexplicable disappointment around these systems.

Once that is clear, the posture for using the model gets calmer. You are not talking to an opinion-holder. You are talking to **a probability machine that speaks in the first person**. The two look similar from outside. They are very far apart in practice.

This distinction has a very concrete engineering correlate. *AI memory*, *long-term memory*, *personalization*—at their core, these are engineering machinery to *simulate the appearance of learning* on top of a system that does not actually learn at inference time. Such simulation has limits, has costs, has recurring failure modes. Why is *memory* such a hard engineering problem? Because we are using engineering to patch a mechanism-layer hole, and the hole is *no continuous self*. Engineering can make it look like there is one. It cannot make there actually be one.

All those earlier discussions—about compression, about convergence, about terrain—touch the ground here. **What actually determines the quality of your work with this system is not the big *does it have intelligence?* question. It is whether you can see clearly that it is not the same shape of thing as you are.** See clearly, and collaboration has a boundary. Do not see clearly, and you keep being disappointed at the same dislocation.

What is interesting is that once you see it does not have an *I*, once you see it is not shaped like you, you also start to see something else more clearly: what your own *I* actually means.

## 6. The thing that gets changed in the end is our definition of ourselves

Every new technology forces humans to redefine what *human* means.

Before the calculator, *being good at arithmetic* was a marker of intelligence. A child who could mentally multiply four-digit numbers was praised as smart. After the calculator, arithmetic was no longer an intelligence marker in any meaningful sense. A three-dollar plastic box could outperform every person in the room on this task. *Being good at arithmetic* was quietly crossed off the list of human intelligence.

Before chess programs beat Kasparov, *playing chess well* was a marker of intelligence. After Deep Blue, *playing chess well* was crossed off too. Before AlphaGo beat Lee Sedol, *playing Go well* was still a marker of intelligence, because Go's search space is so vast that it was thought to require *intuition*, allegedly something only humans possess. After AlphaGo, *playing Go well* was crossed off, and *intuition* was crossed off in part as well. Before ChatGPT, *writing prose well*, *writing code well*, *handling rhetoric well*, *reasoning well* were markers of intelligence. Today these are starting to be crossed off too.

Every concession forces humans to redraw the boundary of *what makes us unique* one step further back. The boundary keeps moving inward.

This starts to feel anxious. The things we thought were uniquely ours keep getting taken by machines, one at a time. Stop and think about it, though, and the anxiety contains a misreading.

Each concession is not *the machine got stronger*. Each concession is *we are seeing more clearly that this capability was never the essence of human intelligence*. It was something a generic optimization mechanism could perform, which we had mistaken for ours. The calculator showed *arithmetic* was not the human essence. Deep Blue showed *chess* was not. AlphaGo showed *Go* was not. The LLM is showing *fluent prose* is not. Each concession crosses off another *fake essence* that was masquerading as a human essence.

So what *is* the essence of human intelligence?

Before the LLM, we thought we had an answer: language, reasoning, creativity. Now those have been partially conceded. What remains is probably the things that resist compression. Embodied experience. A continuous self. The capacity to genuinely interact with the world. The capacity for original work. None of those can be pressed into parameters, because none of them lives in text. They live in a continuous, embodied, time-bound entity that is *actually existing in the world*. A human who actually wants something to happen *in the world*, and a model that can describe the world very well, are categorically different things.

So this whole *does it have intelligence?* discussion is, underneath, not about it. It is about us. We thought we were judging it. We were really repositioning ourselves. Every time it makes us uncomfortable, it is helping us see something we had not seen before: a thing we thought was uniquely ours turns out not to be.

This is not a bad thing. It forces every generation, especially this generation of engineers, to take the question *who am I?* out of abstract philosophy and turn it into a concrete engineering question. When the model can write code, the engineer has to answer fresh: *what is uniquely mine as an engineer?* When the model can perform reviews, the senior engineer has to answer: *what does my judgment have that the model's does not?* When the model can write prose, the writer has to answer: *what can I write that the model cannot?* Every one of those questions, when actually asked, lands not on *where am I better than the model*, but on *what am I, as a continuous existing person, actually doing?*

That question used to go almost unasked. We lived, we worked, we walked forward on a vague feeling of *I am me*, without ever pressing on where the boundary of that *me* actually sits. The LLM has pushed that question up to every person's face. *It is not like a human, and here are the dimensions on which it is not* turns out to be a mirror that reflects us with unusual clarity.

We thought we were measuring the machine. The machine has been measuring us. We thought we were judging *whether it has intelligence*. It has been forcing us to redefine *what intelligence is, what a human is*. The real position of this conversation is not on its side. It is on ours. It is about our definition of ourselves.

The LLM goes deeper than any previous technological turn, because it directly reaches *language* and *thinking*—the two things we had treated, until now, as the last walls of *what makes me me*. With those two walls partly breached, we either keep retreating, drawing narrower and narrower boundaries, or we stop and admit that the things being conceded were never the boundary. The real boundary has always been deeper—in the body, in time, in the way we are *actually living together with this world*.

What it looks like at the end of that road, nobody knows today. But the engineers walking the road right now, more than any generation of engineers before them, have a chance to stop and think about it.
