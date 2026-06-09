# Expert Panel

Use this file for role-specific idea review. Keep roles independent before aggregating.

Each expert must write as a strict reviewer, not as a generic coach. Do not use generic praise or generic concern. Every role must name a concrete claim, mechanism, closest-work risk, evidence gap, or venue criterion. After the strict concern, each role must name the smallest repair or evidence test that would change its judgment; if no repair exists, explain why.

Do not force roles to disagree, praise, or reject. A role may say that the idea is plausible on its axis, but it must state the evidence that supports that view. A role may also say `insufficient evidence` when the idea or search basis is too incomplete for a fair judgment.

## Required Roles

### Field Expert

Checks:

- Importance of the problem to the target community.
- Relationship to closest known work.
- Whether the claimed gap is real, current, and specific.
- Whether the idea teaches the field something beyond a local improvement.
- Whether the insight would still look interesting after the obvious related-work paragraph is written.

### Method Expert

Checks:

- Mechanism clarity.
- Technical soundness.
- Assumptions and failure modes.
- Elegance: whether the method has necessary parts and a coherent insight.
- Whether the contribution is more than combining known modules.
- Whether any components optimize incompatible objectives or make contradictory assumptions.

### Experiment Expert

Checks:

- Whether the central claim can be tested.
- Baselines, ablations, metrics, datasets, workloads, proofs, or studies.
- Feasibility under time, compute, data, and implementation constraints.
- Whether negative results or failure cases would still be informative.
- Which single missing comparison would most likely cause rejection.

### AC / Venue Expert

Checks:

- Venue fit and audience.
- Whether the idea matches the venue's contribution taste.
- Desk-reject or reviewer-mismatch risk.
- Whether the idea is likely to survive discussion after mixed reviews.
- Whether the contribution would be read as main-track substance, workshop novelty, benchmark engineering, or application-only work.

### Skeptical Prior-Art Expert

Checks:

- Novelty collapse risk.
- Obvious close papers, systems, benchmarks, or theory lines to search.
- Whether the new terminology hides a known method.
- Whether the idea should be marked `needs-literature-search`.
- The strongest "this is already known" objection a reviewer could make.

## Optional Roles

Add only when relevant:

- Ethics/reproducibility expert.
- Systems builder.
- User-study expert.
- Theory/proof expert.
- Security threat-model expert.
- Dataset/benchmark curator.
- Domain practitioner.
- Resource and implementation feasibility reviewer.

## Per-Expert Output

```text
Role:
Score tendency:
Best possible argument for the idea:
Strict rejection-grade concern:
Anchor:
Why this matters:
Fatal risk if any:
Most valuable repair or pivot:
Development-potential note:
Confidence:
```

If a role cannot find a rejection-grade concern, say why and identify the evidence that supports that confidence. Do not fill the field with generic encouragement.

## Panel Synthesis

After all independent role notes, synthesize without averaging away fatal risks:

```text
Agreement:
Disagreement:
Strongest accept argument:
Strongest reject argument:
Score-relevant uncertainty:
Most valuable next evidence:
Panel-calibrated recommendation:
```
