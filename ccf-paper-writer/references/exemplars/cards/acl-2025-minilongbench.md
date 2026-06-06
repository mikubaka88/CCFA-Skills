# MiniLongBench

Venue/year: ACL 2025, Outstanding Paper.
Source: ACL Anthology `https://aclanthology.org/2025.acl-long.560/`.
Use when: writing benchmark, evaluation efficiency, long-context LLM, dataset pruning, or low-cost evaluation papers.

## Story Pattern

The paper targets the evaluation cost of long-context understanding. It argues that existing benchmarks contain redundancy, then introduces a compressed benchmark that preserves ranking behavior while dramatically reducing test size and cost. The key writing move is to make evaluation economy a scientific contribution.

## Abstract Moves

- Start from the importance of the capability and the cost barrier.
- Identify redundancy as the discovered root cause.
- Introduce the benchmark by its compression method and size.
- Prove usefulness through rank correlation with the full benchmark.
- End with the research-enabling implication.

## Introduction Moves

- Position evaluation cost as a bottleneck for model development.
- Distinguish "shorter benchmark" from "weaker benchmark" using correlation evidence.
- Explain sparse information as the reason pruning can work.

## Method Moves

- Describe the pruning or compression pipeline in auditable steps.
- Define what behavior must be preserved after compression.
- Keep benchmark categories visible so reviewers can judge coverage.

## Evidence Moves

- Use many models to support rank-preservation claims.
- Report cost reduction and correlation together.
- Include task-category analysis to avoid the appearance of cherry-picking.

## Reusable Techniques

- Convert evaluation expense into a first-class problem.
- Support small-data claims with preservation metrics, not only speedups.
- Phrase benchmark contributions around utility for future research.

## User Notes

Use this card when the user's paper proposes a cheaper evaluation protocol or compressed dataset.

## Do-Not-Copy Boundary

Do not borrow the LongBench pruning claim, exact cost numbers, or rank-correlation framing unless the user's evaluation validates them.
