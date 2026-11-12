# Problem And Method Blueprint

Use this file when converting a rough direction into a CCF-A-ready problem and method plan.

Treat the fields below as prompts for the current stage, not compulsory output headings. During exploration, explain the problem, proposed operation, and why it could matter. Inspect known contradictions and necessary assumptions; leave experiment design to a requested planning step or a concrete decision that needs it. Missing results are expected at this stage and do not require defensive wording or a smaller research goal.

## Problem Sharpening

A strong problem statement should answer:

```text
What is the task or phenomenon?
Who in the venue community cares?
What gap remains after the strongest prior work?
Why is the gap hard rather than merely unattempted?
What would become possible if it were solved?
Which conditions define the actual task?
```

Good CCF-A problems tend to have at least one of these properties:

- They expose a bottleneck that strong prior work cannot handle.
- They define a new setting that changes the technical requirements.
- They reveal a mismatch between common assumptions and real use.
- They connect two areas in a way that creates a new capability or question.
- They make a hidden evaluation gap measurable.

## Method Mechanism

For a model-capability question, first locate what prevents the requested behavior. Start from the supplied failure or a precisely stated hypothetical case; do not invent an observed failure. Compare the explanations that are plausible for this setting rather than filling every row:

| Possible limitation | Question that separates it from nearby explanations |
| --- | --- |
| Information unavailable | Can two cases require different answers while providing the same permitted observations? If so, which additional observation or assumption would distinguish them? |
| Representation loses a distinction | Does an encoding, compression, invariance, or state update merge cases that the task must distinguish? Which distinction must survive? |
| Objective rewards the wrong behavior | Can a shortcut satisfy the training objective while missing the desired capability? What would an objective or supervision change reward instead? |
| Learning or data coverage fails | Can the model express a suitable solution, but the data, gradients, optimization, or numerical behavior prevent learning it? What separates these causes? |
| Computation cannot use available information | Is the information present but inaccessible to the current retrieval, composition, memory update, or inference procedure? Which operation is missing? |
| Evaluation misses the behavior | Could the metric improve without the requested capability, or fail to recognize it? Which task distinction should the evaluation preserve? |

Use the smallest useful counterexample, limiting case, derivation, existing analysis, or diagnostic observation to distinguish these explanations. A proof is useful when the question is mathematical; it is not a mandatory artifact for every idea. Keep an untested diagnosis as a hypothesis. If the available material cannot separate causes, state what remains open and develop the plausible alternatives without pretending one is established.

For example, if a fixed representation maps two inputs to the same state but their correct answers differ, a predictor that sees only that state cannot distinguish them. Adding layers after that fixed state cannot recover the lost information. This argument identifies the encoding or available input as a possible intervention; it does not establish that a particular real model has this defect. If the representation is trainable or another input reaches the predictor, recheck the premise.

Keep the diagnosis distinct from the baseline's implementation. A convenient module, familiar benchmark or available codebase does not establish the cause of a failure. For a proposed improvement, explain what would still be impossible if that component were added while the suspected limitation remained unchanged; this can reveal an unchanged information loss, objective mismatch or missing distinction. Use a different explanation when that test undermines the proposed route, without silently replacing the user's goal with a smaller task.

Select a mechanism for the limitation it changes. State which information, operation, assumption, or objective changes, why this addresses the difficulty, and what would contradict that explanation. A performance failure alone does not identify its cause, and a named theoretical framework alone does not explain a mechanism. For non-model ideas, use the corresponding mathematical, empirical, systems, or human-centered objects instead of forcing this model-specific diagnosis.

Translate method labels into mechanisms:

```text
Input and output:
Key representation:
Main operation:
Optimization or inference objective:
Why the mechanism should address the root challenge:
Necessary assumptions:
Known contradiction or unresolved dependency, if any:
Relevant alternative and reason for choosing this mechanism, if a choice has been made:
```

Connect the proposed operation to the expected effect when that mechanism is part of the idea. For example:

```text
Intervention -> changed representation/optimization/inference behavior -> measurable intermediate effect -> task-level outcome
```

This is a proposed explanation until supported. Theory, measurement, and dataset ideas may instead need a logical relation or construction argument; do not invent an empirical causal chain for them. Describe the operation itself instead of calling it “可验证的机制” or “可实现的路径.” Retain those properties when the research actually studies verifiability or feasibility.

When a mechanism comes from prior work, record the source-supported primitive and the optimizer's new interaction separately. The source may justify that a primitive works under its original assumptions; it does not automatically justify transfer, compatibility, or the new paper's central claim.

If the method combines known components, identify the interaction and compatibility condition, and explain what changes when a component is absent. Without an interaction or another substantive contribution, adding components does not address the research question. A useful systems design, diagnostic finding, or simpler formulation may still be a contribution in its own right; judge its stated purpose rather than requiring a new module.

## Coherence Filter

Before presenting an optimized idea, check:

- The problem setting and method assumptions are compatible.
- Any proposed discriminator can distinguish the central explanation; it can be an observation, counterexample, proof, analysis, or test appropriate to the contribution.
- An evidence plan, when requested, matches the contribution type; it is not a completed-results gate for an early idea.
- The target venue audience would care about the problem, not only the technique.
- No module requires data, supervision, deployment access, or theoretical assumptions that conflict with another module.
- The idea does not rely on mutually exclusive claims such as "training-free" and "requires large fine-tuning" unless the distinction is scoped.

## Innovation Types

Classify the strongest honest contribution:

- New problem or setting.
- New method or architecture.
- New objective, inference procedure, or theoretical result.
- New dataset, benchmark, workload, or protocol.
- New system design or deployment insight.
- New empirical finding or diagnostic analysis.
- New synthesis that resolves a known tension.

Identify the contribution types actually present without forcing a quota or inflating labels. Preserve connected task, measurement, and method contributions when the idea needs them. Develop their support at the appropriate stage.

## Elegance Checks

An elegant idea usually has:

- One central insight that explains the method.
- A method whose parts are necessary, not decorative.
- A simple claim that can be tested directly.
- Necessary assumptions whose role is understandable, with known failure mechanisms explained when they matter.
- A result that would teach the community something even if SOTA gains are modest.
- A design that removes a bottleneck or reveals a simpler formulation, not merely a longer pipeline.

## Material Risks To Resolve

Identify the affected assumption and evidence before deciding how a risk changes development:

- Verified closest-work overlap may remove a claimed contribution; a suspected close paper calls for a targeted comparison, not an automatic rejection.
- A narrow problem may need a clearer important consequence or a different framing; audience fit and scientific value are distinct questions.
- Renaming an established mechanism does not create novelty; identify a real causal difference or filter that candidate.
- Missing resources, data, proof strategy, or time constrain execution. Separate that constraint from concept quality, and consider a different mechanism or discriminating analysis without silently reducing the user's goal.
- An untested assumption is a question to resolve. An assumption contradicted by the setting is a concrete defect; imagined reviewer preferences are not evidence against it.

Filter an impossible branch when the constraint is decisive. Repair valuable ingredients or explore a structurally different route when useful; do not require a rescue for every rejected branch or keep revisiting the same contradiction without new conditions.
