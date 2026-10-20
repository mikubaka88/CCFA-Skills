# Evidence Design

Use this file to design CCF-A evidence packages without fabricating results.

## Evidence Principle

Start from the research claim or decision, not the table. Each experiment should resolve a relevant question such as:

- Does the method solve the stated problem?
- Why does the mechanism work?
- Is the comparison fair and current?
- Does the result generalize across settings?
- What fails, when, and why, when the question is material to the claimed scope and grounded in observations or a plausible mechanism?
- Can the work be reproduced or audited?
- Does the evidence match the venue's expectations?

## Venue-Family Evidence

These are candidate evidence forms, not mandatory packages. Select only what the contribution, actual claim, or verified venue rule calls for. A venue label alone does not justify every listed experiment.

AI/ML:

- Strong close baselines, simple baselines, ablations, seeds/statistics, compute, hyperparameters, robustness, scaling, and diagnostic analysis.

CV/multimedia/graphics:

- Visual comparison, qualitative failure cases, per-category or hard-case analysis, fair image/video settings, user or perceptual studies when needed.

NLP:

- Data quality, annotation agreement, leakage checks, automatic and human evaluation validity, error taxonomy, ethics, and task assumptions.

DB/KDD/IR:

- Realistic workload, scale, latency, throughput, memory, ranking metrics, indexing or pipeline cost, ablations, and deployment constraints.

Systems/networks/architecture/storage:

- Real bottleneck, implementation detail, end-to-end results, microbenchmarks, sensitivity, overhead, workload variation, operational boundaries.

Security/crypto:

- Threat model, attacker capabilities, adaptive attacks, bypass tests, guarantees, false positives/negatives, disclosure, ethics, and assumptions.

HCI/CSCW/UbiComp:

- Research questions, participants, procedure, tasks, measures, statistics, qualitative coding, triangulation, ethics, and claim scope.

SE/PL/FM:

- Tool benchmarks, real programs, formal statements, proof sketches, soundness/completeness tradeoffs, threats to validity, usability where relevant.

Theory:

- Formal model, theorem statement, proof roadmap, examples, lower/upper-bound relationship, relation to barriers and open problems.

## Baseline Matrix

Use the relevant fields for proposed comparative studies; a formal or noncomparative question does not need a baseline matrix:

```text
Baseline:
Why included:
Source / citation needed:
Implementation source:
Fairness constraints:
Expected metric:
Can run? yes / no / unknown
If missing, reason:
```

Baseline categories:

- Closest prior method.
- Current strong method.
- Simple sanity baseline.
- Ablated version of the user's method.
- Human, oracle, random, heuristic, or classical baseline when meaningful.
- Deployed or default system baseline for systems/HCI/security tasks.

## Ablation Logic

Each ablation should test a mechanism:

```text
Component or assumption:
Why it matters:
Replacement or removal:
Observation or metric:
How the competing outcomes change the explanation or next decision:
```

Useful ablations:

- Remove a module.
- Replace a specialized component with a generic alternative.
- Vary a key hyperparameter.
- Change data scale, workload, or domain.
- Test hard or failure cases only when they resolve a claim or project decision and follow an observed issue or plausible mechanism, or satisfy a verified venue requirement.
- Analyze compute, memory, latency, or cost.

## Benchmark Or Dataset Design

For a new benchmark:

```text
Task definition:
Data source:
Annotation or generation process:
Splits:
Metrics:
Baseline suite:
Leakage checks:
Difficulty and diversity:
Human or expert validation:
License and ethics:
Maintenance plan:
```

Benchmark papers should be evaluated as benchmarks, not only as methods. Do not score them as weak because they lack a method, and do not invent adoption claims.

## Minimum Convincing Package

Select the smallest sufficient package for the actual claims and paper type. These are evidence roles, not compulsory experiments:

1. A fair comparison against relevant close and strong baselines when the work makes comparative claims.
2. Mechanism evidence such as an ablation, analysis, or proof when the claim depends on that mechanism.
3. Robustness, generalization, stress, or failure analysis only when it resolves a specific claim or project decision grounded in observations or a plausible mechanism, or satisfies a verified venue requirement.
4. Reproducibility details for the reported method, protocol, or proof as applicable.

For each proposed test, state which claim or decision it resolves, why existing evidence is insufficient, and how materially different outcomes would affect the interpretation or next step. Put this in the existing plan; no separate justification report is needed. If a necessary test is infeasible, identify the remaining evidence gap and feasible alternatives. Adjust a reported conclusion only when its support requires it; a generic checklist or resource constraint alone does not authorize changing the research goal. Keep a proposed mechanism, a planned comparison, and a completed finding distinct, and continue unaffected work.

For reported comparisons and executable changes, apply `../../ccf-humanization/references/experiment-discipline.md`: preserve full-method identity and configuration, label ablations, and separate development smoke checks from scientific evidence. An authorized minimal system or controlled study can answer its own stated question using its actual protocol; it cannot stand in for an unexecuted full-method comparison. This gate does not require executed results before designing an experiment.

## Protocols For Autonomous Research

Use this section only for the experiment stage of an explicitly requested research loop. `ccf-pipeline-orchestrator` owns coordination under [autonomous-research.md](../../ccf-pipeline-orchestrator/references/autonomous-research.md); this skill owns the scientific comparison and interpretation. A concept-only idea review remains outside this stage.

Resolve these items from existing artifacts and authorization, recording only what the next experiment needs:

| Item | Required meaning |
| --- | --- |
| Scientific question | The competing explanations and the observation that would distinguish them. A candidate is a hypothesis, not a predicted success presented as fact. |
| Comparison | Baseline and candidate versions, controlled inputs/resources, metric meaning and direction, material constraints, and the rule for deciding whether a difference matters. Include uncertainty or repeats when they could change that decision. |
| Executable specification | Inspected or supplied command and arguments, working directory, environment, data/split, seed or relevant randomization, output paths, and resource estimate. A missing command or dataset is an execution dependency, not an excuse to invent results. |
| Evidence | Where actual measurements, configurations, logs, and failures will be found, and which subset is needed to interpret the result. Retain enough source evidence to reproduce the comparison without copying whole datasets. |
| Budget and stop | The applicable per-run allowance, stopping conditions, and remaining resources supplied by the orchestrator. Count failed runs, evaluation, retries, and other charged work, not only successful experiments. |

Before a comparable run, keep the evaluation definition separate from editable candidate methods and search strategies. During development, use development evidence to select candidates. Preserve independent evaluation material when available; once its feedback informs optimization, it is no longer an unseen final check. If an evaluator or data definition is demonstrably wrong, correct and version it, then repeat affected baseline and candidate comparisons. Do not weaken a criterion because a candidate failed it.

Read actual feedback before proposing the next action:

| Observation | Interpretation and next action |
| --- | --- |
| Command failed, output missing, or execution identity uncertain | Diagnose the failed dependency. Retry only after a relevant condition changes or a justified transient failure is addressed. This is not evidence against the scientific hypothesis. |
| Data, budget, split, or evaluator differs materially | Mark the comparison invalid or explicitly scoped to the changed setting; repair and rerun affected comparisons before selection. |
| Valid result contradicts the prediction | Record the failed assumption and the observation. Suggest a mechanism or strategy change that predicts something different; do not automatically add another module. |
| Candidate improves a measured dimension but violates a hard constraint | Preserve the measurement, explain the tradeoff, and do not promote it as meeting the original goal. |
| Difference is inconclusive | Identify the smallest additional observation that can distinguish the explanations within the remaining allowance; do not launch a full ablation suite by habit. |
| Comparison supports the candidate under the current contract | Return the supported scope and evidence to the integrating owner for retention or promotion. Distinguish a useful development candidate from a verified publication claim. |

Interpretation may support keeping a candidate for further study, discarding it, branching to a different mechanism, repairing execution, or stopping with a negative/unresolved result. The orchestrator integrates this with the current goal, other constraints, and remaining budget. Do not make one higher metric stand in for the whole research objective, or require every unsuccessful branch to produce a rescue.
