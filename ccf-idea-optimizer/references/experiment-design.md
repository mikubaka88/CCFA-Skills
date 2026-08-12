# Experiment Design

Use this file when turning an optimized idea into a minimum convincing evidence package for a CCF-A submission.

For a full experiment plan, dataset/baseline search, benchmark protocol, or result-fill table, use `ccf-experiment-designer` through the CCFA handoff mode. This file is the local lightweight evidence planner for idea optimization.

## Evidence Principle

Design experiments to answer the reviewer question, "Does the evidence test the central claim?" Do not add experiments for volume. Every experiment should defend novelty, soundness, significance, generalization, efficiency, or scope.

When literature is available, start from compatible protocol anchors in the idea-grounding packet. Do not produce a generic benchmark list that is disconnected from the closest work, and do not treat reported public numbers as newly measured results.

## Experiment Matrix

For each major claim, create:

```text
Claim:
Evidence needed:
Dataset / benchmark / workload / proof / study:
Baselines:
Metrics:
Ablations:
Stress or robustness tests:
Failure analysis:
Expected reviewer concern answered:
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

- Remove each core component.
- Replace the proposed component with a plausible generic alternative.
- Vary the key hyperparameter or threshold.
- Show when the method fails.
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

The minimum package should include:

1. Main result against close baselines.
2. Mechanism ablation or proof of why the method works.
3. Robustness, generalization, or stress test.
4. Limitation or failure analysis.
5. Reproducibility details sufficient for audit.

If this package cannot be built under the user's constraints, recommend narrowing the claim, changing venue, or pivoting the idea.
