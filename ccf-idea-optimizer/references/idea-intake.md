# Idea Intake

Use this file when the idea is rough, underspecified, scattered across several bullets, or when multiple idea drafts must be compared.

## Intake Fields

Collect or infer:

```text
Target venue / family:
Field and subfield:
Track or paper type:
Raw idea:
Problem owner / audience:
Closest known work:
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

Convert every idea into this structure before optimizing:

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

Hard rule: if the root challenge is only "existing methods perform poorly", refine it into a technical, scientific, empirical, human-centered, or systems bottleneck.

For fuzzy ideas, produce several normalized cards before choosing one. Do not collapse the search space too early.

For early directions, attach a development label instead of a verdict:

- `seed`: interesting but still missing problem, mechanism, or evidence.
- `salvageable`: weak in current form, but a clear narrowing or reframing exists.
- `needs-search`: promising enough to search before judging novelty.
- `needs-mechanism`: problem may matter, but the mechanism is not yet credible.
- `near-pivot`: keep only one ingredient unless the user can supply hidden evidence or constraints.

## Missing-Input Labels

Use these labels instead of guessing:

- `needs-literature-search`: closest work is unknown or likely fast-moving.
- `needs-frontier-grounding`: the idea may be stale or crowded and needs current paper search.
- `needs-feasibility-check`: data, compute, implementation complexity, or timeline is unclear.
- `needs-domain-constraint`: the real-world setting, threat model, user group, or workload is underspecified.
- `needs-evidence-design`: the paper claim is clearer than the experiment plan.
- `needs-venue-selection`: the idea may be good, but the audience is not yet obvious.

## Multi-Idea Intake

For several drafts, normalize all ideas first, then compare optimization routes. Do not optimize the first idea prematurely. Prioritize optimizer attention by:

1. Strongest problem-method fit.
2. Most defensible novelty after likely prior art.
3. Best evidence feasibility.
4. Best CCF-A venue fit.
5. Lowest serious-risk count after one realistic iteration.

Do not produce numeric scores, investment recommendations, winner labels, or strict rankings here. Prefer "best development route" and "backup route" over "winner/loser" language. If the user explicitly asks to score, rank, select, or strictly review ideas, route to `ccf-idea-reviewer`.
