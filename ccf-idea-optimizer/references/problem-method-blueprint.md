# Problem And Method Blueprint

Use this file when converting a rough direction into a CCF-A-ready problem and method plan.

## Problem Sharpening

A strong problem statement should answer:

```text
What is the task or phenomenon?
Who in the venue community cares?
What gap remains after the strongest prior work?
Why is the gap hard rather than merely unattempted?
What would become possible if it were solved?
What scope boundary prevents overclaiming?
```

Good CCF-A problems tend to have at least one of these properties:

- They expose a bottleneck that strong prior work cannot handle.
- They define a new setting that changes the technical requirements.
- They reveal a mismatch between common assumptions and real use.
- They connect two areas in a way that creates a new capability or question.
- They make a hidden evaluation gap measurable.

## Method Mechanism

Translate method labels into mechanisms:

```text
Input and output:
Key representation:
Main operation:
Optimization or inference objective:
Why the mechanism should address the root challenge:
Assumptions:
Failure modes:
Alternative designs rejected:
```

Then state the causal chain in one line:

```text
Intervention -> changed representation/optimization/inference behavior -> measurable intermediate effect -> task-level outcome
```

When a mechanism comes from prior work, record the source-supported primitive and the optimizer's new interaction separately. The source may justify that a primitive works under its original assumptions; it does not automatically justify transfer, compatibility, or the new paper's central claim.

If the method is a combination of known components, identify the non-obvious interaction, the compatibility condition, and the observation that would distinguish the combination from either component alone. If no such interaction exists, the idea is likely an engineering assembly and needs a sharper contribution or a stronger benchmark/evidence story.

## Coherence Filter

Before presenting an optimized idea, check:

- The problem setting and method assumptions are compatible.
- The proposed evidence can actually test the central claim.
- The contribution type matches the evidence type.
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

Avoid claiming all types. Pick the top one or two and make the evidence package serve them.

## Elegance Checks

An elegant idea usually has:

- One central insight that explains the method.
- A method whose parts are necessary, not decorative.
- A simple claim that can be tested directly.
- A failure mode that is understandable.
- A result that would teach the community something even if SOTA gains are modest.
- A design that removes a bottleneck or reveals a simpler formulation, not merely a longer pipeline.

## Fatal Idea Risks

Mark these early:

- The novelty collapses under a likely close paper.
- The problem is too narrow for the target venue.
- The method is a known trick with new terminology.
- The central claim cannot be tested with available resources.
- The evidence would require a dataset, proof, or system that cannot be built in time.
- The idea depends on hidden assumptions reviewers will reject.
