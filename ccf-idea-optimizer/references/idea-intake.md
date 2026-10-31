# Idea Intake

Use this file when the idea is rough, underspecified, scattered across several bullets, or when multiple idea drafts must be compared.

## Intake Fields

Collect or infer:

```text
Target venue / family:
Field and subfield:
Track or paper type:
Raw idea:
Affected community or unresolved scientific question:
Closest known work:
Available literature packet / source set:
Available data / code / compute:
Expected method ingredients:
Expected evidence:
Deadline and resource constraints:
Non-goals:
```

For fuzzy ideas, also collect or infer:

```text
Seed direction:
What should stay fixed:
What may vary:
Desired novelty risk: conservative / balanced / exploratory
Preferred method taste: simple / elegant / theoretical / system-building / empirical / interdisciplinary
Fields to avoid:
```

If a field is unknown, infer it from the method and venue names. If the target venue is unknown, assume a generic CCF-A target and mark venue-specific advice as lower confidence.

## Normalized Idea Card

Recover the relevant parts of the idea from the supplied material. Use this card only when it helps compare or develop the ideas; do not turn a short request into a compulsory intake form:

```text
Task:
Gap:
Root challenge:
Core insight:
Proposed mechanism:
Contribution type:
Expected evidence:
Why now:
Main risk:
Best venue fit:
```

When a literature packet is present, retain the useful observation, assumption, contradiction, or mechanism and its source location. Include a protocol anchor only when relevant. A reported limitation is one possible inspiration; do not reduce the task to fixing the first paper's limitation. Keep source facts separate from the proposed idea's inferred gap.

Hard rule: if the root challenge is only "existing methods perform poorly", refine it into a technical, scientific, empirical, human-centered, or systems bottleneck.

For a fuzzy direction, consider different explanations of the difficulty before choosing a mechanism. Preserve requested breadth; neither a fixed number of cards nor a single early winner is required.

For early directions, attach a development label instead of a verdict:

- `seed`: a question or observation whose explanation or mechanism is still open.
- `salvageable`: the current formulation has a specific defect and useful ingredients that a revision could preserve.
- `needs-search`: promising enough to search before judging novelty.
- `needs-mechanism`: problem may matter, but the mechanism is not yet credible.
- `near-pivot`: a central assumption or mechanism needs changing; preserve whichever ingredients remain relevant to the user's objective, without a component quota.

## Missing-Input Labels

Use these labels instead of guessing:

- `needs-literature-search`: closest work is unknown or likely fast-moving.
- `needs-frontier-grounding`: the idea may be stale or crowded and needs current paper search.
- `needs-feasibility-check`: data, compute, implementation complexity, or timeline is unclear.
- `needs-domain-constraint`: the real-world setting, threat model, user group, or workload is underspecified.
- `needs-evidence-design`: the paper claim is clearer than the experiment plan.
- `needs-venue-selection`: the idea may be good, but the audience is not yet obvious.

## Multi-Idea Intake

For several drafts, understand their central questions before committing to one. During exploration, direct attention toward:

1. A consequential problem or unexplained phenomenon.
2. A changed assumption that opens a substantive difference from known work.
3. An explanation that connects the proposed operation to the missing capability.
4. Different predictions or implications that help separate competing explanations.
5. What the work could teach even if the first implementation does not improve the headline metric.

Use verified prior work to identify real overlap, not to require every new hypothesis to have precedent. A known hard resource or setting constraint excludes incompatible routes; unknown cost, unfinished experiments, and uncertain venue fit do not by themselves make an idea scientifically weak. When the task moves to allocating effort or planning execution, compare the next useful step's cost and dependencies separately from conceptual value. Do not silently change the user's objective to favor the easiest route.

Do not produce numeric scores, investment recommendations, winner labels, or strict rankings here. Prefer "best development route" and "backup route" over "winner/loser" language. If the user asks to judge, score, rank, select, or review ideas, including “靠谱吗”, “值得做吗”, or “创新够不够” without numeric scores, route that assessment to `ccf-idea-reviewer`.
