# Research Taste

Use this file when the user asks what kind of research is good, elegant, important, or more likely to survive CCF-A review.

## Good Research Signals

Strong research usually has:

- An important problem, not only a popular technique.
- A precise gap against strong prior work.
- A simple insight that changes how the problem is attacked.
- A method whose mechanism is inspectable.
- Evidence that tests the claim rather than decorating it.
- Honest scope and limitations.
- A result that would still teach something if the headline number were smaller.

## Research Questions

Adapt these questions during idea optimization:

```text
What are you trying to do?
How is it done today?
What is new in your approach?
Who cares, and why?
What are the risks?
How much will it cost or require?
How will progress and success be measured?
```

## Intellectual Merit

Use intellectual merit as the core idea test:

- Does the idea advance knowledge, capability, method, data, theory, system design, or evaluation?
- Are the team, resources, and approach credible?
- Are the claims grounded in evidence that can be produced?

Use broader impact only when it is real and venue-relevant. Do not add vague societal claims to compensate for weak technical contribution.

## Problem Choice

Prefer important problems where the user's current position offers a credible angle. Seek an attackable mechanism or decisive question within a difficult problem; do not automatically shrink its scientific ambition. Review readiness is one consideration, not a substitute for whether the result would advance understanding.

## Paper-Story Taste

Borrow the writing lesson from strong paper-writing advice: the idea should be explainable as one story:

```text
problem -> gap -> challenge -> insight -> method -> evidence -> limitation
```

If this story cannot be stated before drafting, the manuscript will likely become a list of components and experiments.

## Acceptance-Oriented Taste

CCF-A acceptance is not just "novel plus works". The idea should reduce reviewer uncertainty:

- Why this problem?
- Why this method?
- Why now?
- Why should I believe it?
- Why this venue?
- What would fail if the central assumption is false?

Use a missing answer to identify the affected question. Resolve material conceptual gaps during idea development; authorized writing can continue on supported content without repeatedly restarting ideation. Do not optimize indefinitely for imagined reviewer objections.

## Frontier And Staleness Taste

For fast-moving topics, a good idea should survive a current related-work scan. Treat these as warnings:

- The idea is a direct extension of a crowded benchmark trend with no new bottleneck.
- The method is "add LLM/VLM/diffusion/agent" without a mechanism tied to the problem.
- The claimed gap is likely solved by recent workshop, arXiv, OpenReview, or proceedings papers.
- The evidence package would only show small leaderboard gains without explaining why.
- The idea depends on an obsolete dataset, baseline, threat model, workload, or user scenario.

Prefer directions that:

- expose a new measurable failure mode,
- simplify an overcomplicated paradigm,
- connect a strong method to a neglected but important constraint,
- create a benchmark/protocol that changes what can be measured,
- turn an empirical observation into a mechanism, theorem, or system design.

## Acknowledgments

The question framework draws on Heilmeier's research questions, NSF's intellectual-merit criteria, and Hamming's discussion of important problems. Their source records remain in the [shared registry](../../ccf-common/references/source-registry.yaml). These acknowledgments preserve provenance without naming CCFA's methods after another framework.
