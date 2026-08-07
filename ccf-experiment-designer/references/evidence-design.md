# Evidence Design

Use this file to design CCF-A evidence packages without fabricating results.

## Evidence Principle

Start from the claim, not the table. Each experiment should answer one of these reviewer questions:

- Does the method solve the stated problem?
- Why does the mechanism work?
- Is the comparison fair and current?
- Does the result generalize across settings?
- What fails, when, and why, only when observed or material to the claimed scope?
- Can the work be reproduced or audited?
- Does the evidence match the venue's expectations?

## Venue-Family Evidence

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

Use this before proposing experiments:

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
Metric affected:
Expected interpretation if it fails:
```

Useful ablations:

- Remove a module.
- Replace a specialized component with a generic alternative.
- Vary a key hyperparameter.
- Change data scale, workload, or domain.
- Test hard or failure cases only when plausible, observed, claim-relevant, or venue-required.
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

For most CCF-A submissions:

1. Main comparison against close and strong baselines.
2. Mechanism ablation or proof.
3. Robustness/generalization/stress test.
4. Claim-relevant robustness or failure analysis when needed.
5. Reproducibility details for the confirmed full method.

If this package is infeasible, narrow the central claim before adding weaker experiments.

Do not replace any publication method or baseline with a simplified, toy, approximate, proxy, reduced, or debug version. Do not add repeated smoke tests as evidence; retain only the smallest non-duplicative set that checks changed critical paths.
