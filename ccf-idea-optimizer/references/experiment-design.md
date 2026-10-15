# Experiment Design

Use this file when the requested idea-development deliverable includes an evidence plan for a CCF-A submission. Concept-only idea assessment does not activate experiment planning.

For a full experiment plan, dataset/baseline search, benchmark protocol, or result-fill table, use `ccf-experiment-designer` through the CCFA handoff mode. This file is the local lightweight evidence planner for idea optimization.

## Evidence Principle

Design experiments to answer the scientific question, "Does the evidence test the central claim?" Do not add experiments for volume. Every experiment should resolve a specific hypothesis, comparison, mechanism, or material scope question.

When literature is available, start from compatible protocol anchors in the idea-grounding packet. Do not produce a generic benchmark list that is disconnected from the closest work, and do not treat reported public numbers as newly measured results.

## Experiment Matrix

For each major claim, use the applicable fields; omit irrelevant categories rather than filling them with speculative tests:

```text
Claim:
Evidence needed:
Dataset / benchmark / workload / proof / study:
Baselines:
Metrics:
Ablations:
Stress or robustness tests:
Failure analysis:
Scientific question answered:
```

Add two links for each new method claim:

```text
Closest protocol anchor:
Discriminating test: what result would separate the proposed mechanism from the closest alternative?
```

## Baseline Rules

- Include the strongest close prior work when feasible.
- Separate reproduced baselines, reported numbers, and incompatible settings.
- Explain why any missing baseline cannot be run.
- Avoid unfair adaptation, extra data, or hidden tuning advantages.
- Add simple baselines that test whether the core mechanism is necessary.
- Prefer mechanism-level competitors and public methods that address the same gap over comparisons dominated by a weaker foundation model.

## Ablation Rules

Use ablations to test mechanism, not only performance drops:

- Remove a core component when this distinguishes its proposed mechanism from an alternative explanation.
- Replace the proposed component with a plausible generic alternative.
- Vary the key hyperparameter or threshold.
- Examine failure conditions when they resolve a claim or project decision and follow an observed issue or plausible mechanism; do not invent failure cases to fill a category.
- Include qualitative or diagnostic evidence when numeric metrics hide behavior.
- For transferred or combined mechanisms, test the named compatibility condition rather than ablating components mechanically.

## Venue-Specific Evidence

- ML/AI: ablations, seeds/statistics, data splits, robustness, compute, scaling, and diagnostic analysis.
- CV: visual comparisons, per-category or hard-case analysis, fair image/video settings, and failure cases.
- NLP: data quality, annotation agreement, leakage checks, human or automatic evaluation validity, and error taxonomy.
- DB/KDD/IR: scale, latency, memory, throughput, ranking metrics, workload realism, and deployment constraints.
- Systems: end-to-end evaluation, microbenchmarks, overhead, sensitivity, resource use, and operational failure cases.
- Security: threat model tests, bypass attempts, adaptive attacks, guarantees, responsible disclosure, and limitations.
- HCI: participant recruitment, tasks, measures, statistics, qualitative coding, ethics, and claim scope.
- Theory: theorem statement, proof sketch, examples, relation to known results, and limits of assumptions.

## Minimum Convincing Package

Choose evidence appropriate to the actual claim and paper type. These roles do not impose a fixed experiment package:

1. Comparisons against relevant close baselines for comparative claims.
2. Mechanism evidence through an ablation, analysis, or proof when required by the claim.
3. Robustness, generalization, stress, or failure analysis only when it resolves a specific claim or project decision grounded in observations or a plausible mechanism, or satisfies a verified venue requirement.
4. Reproducibility details for the planned or reported method, protocol, or proof as applicable.

If necessary evidence is infeasible under the user's constraints, identify the specific gap and feasible alternatives. Do not automatically narrow the research goal, change the venue, or pivot the idea to satisfy a generic package. A proposed route change must follow concrete evidence or a changed constraint and remain within the authorized development scope. Keep planned claims distinct from completed empirical conclusions, and continue unaffected work.
