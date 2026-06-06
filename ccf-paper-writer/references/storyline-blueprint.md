# Storyline Blueprint

Use this before drafting and after every major section edit. CCF A writing should make the full paper story easy for reviewers to reconstruct.

## Global Story Fields

Fill these first:

```text
Target venue:
Venue family:
Paper type:
Task/problem:
Application or scientific value:
Existing methods:
Unresolved gap:
Root technical reason for the gap:
Core insight:
Proposed method:
Contribution type(s):
Key evidence:
Known limitations:
Likely reviewer doubts:
```

## Core Story Arc

Use this arc unless the target venue or contribution type requires a different structure:

1. The task matters because of a concrete scientific, technical, or practical need.
2. Existing methods are insufficient under a specific condition.
3. The insufficiency has a root technical reason, not just weak results.
4. The paper introduces an insight or design that addresses that root reason.
5. The method implements the insight through clear modules or formal steps.
6. Experiments/proofs/studies validate each claimed contribution.
7. Limitations are bounded honestly and do not undercut the main claim.

## Contribution Types

Identify which contribution types are actually present:

- New task or benchmark.
- New problem formulation.
- New theoretical result.
- New algorithm or model.
- New system architecture.
- New module in an existing pipeline.
- New empirical finding.
- New dataset, evaluation protocol, or measurement.
- New interface, workflow, or user study insight.

Do not imply a stronger contribution type than the evidence supports.

## Section Story Roles

| Section | Main role | Story check |
| --- | --- | --- |
| Abstract | Compress the entire story | Does it include task, gap, contribution, and evidence without overclaiming? |
| Introduction | Build motivation and reviewer curiosity | Does the challenge naturally lead to the method? |
| Related Work | Position novelty | Does each topic explain the gap the paper fills? |
| Method | Make mechanism auditable | Can reviewers reproduce the method and see why it addresses the challenge? |
| Experiments | Prove claims | Does every major claim have evidence? |
| Figures/Tables | Make evidence inspectable | Does each visual have one clear message? |
| Limitations | Bound claims | Are limitations honest but not self-defeating? |
| Conclusion | Leave final takeaway | Does it restate insight and evidence succinctly? |

## Storyline Checks After Each Section

Run these after writing or revising a section:

1. Paragraph roles:
   - Assign each paragraph one role.
   - Remove or merge paragraphs with unclear roles.
2. Claim-evidence map:
   - List every major claim.
   - Point to evidence in experiments, theorem, analysis, user study, or figure.
   - Mark as `supported`, `needs evidence`, or `overclaim`.
3. Term map:
   - List key terms and abbreviations.
   - Ensure the same concept keeps the same name.
   - Define terms before reuse.
4. Cross-section continuity:
   - Check whether Abstract, Introduction, Method, and Experiments tell the same story.
   - Ensure contributions in Introduction are validated in Experiments.
   - Ensure limitations do not contradict contribution claims.
5. Reviewer-risk register:
   - Record likely objections.
   - Mark each as addressed by writing, evidence, new experiment, or limitation.

## Claim-Evidence Matrix

Use this format:

```text
Claim:
Where stated:
Evidence source:
Evidence strength:
Reviewer risk:
Status: supported / needs evidence / overclaim / unclear
Revision action:
```

## Storyline Failure Signals

Revise when you see:

- The method appears before the reader understands the problem.
- The paper sells a module but experiments validate only the whole pipeline.
- The Abstract claims broad improvement but experiments cover a narrow setting.
- Related Work hides the strongest competitor.
- Experiments introduce claims never promised earlier.
- The conclusion adds new claims.
- Figures show many details but no clear message.
