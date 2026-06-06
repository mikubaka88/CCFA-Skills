# Paper Writing Review Rubric

Use this rubric when reviewing a manuscript from the perspective of writing quality, reviewer readability, format discipline, and idea presentation. This file is not a replacement for scientific validation; it diagnoses how the paper communicates its scientific value.

## Review Dimensions

Score each dimension on 1-5 when enough text is available.

| Dimension | What To Inspect |
| --- | --- |
| Storyline and motivation | Whether the paper makes the problem, gap, and stakes unavoidable before presenting the method. |
| Contribution display | Whether contributions are specific, non-overlapping, evidence-backed, and visible in abstract/introduction/conclusion. |
| Paragraph logic | Whether each paragraph has one job, a clear topic sentence, causal flow, and no mixed objectives. |
| Claim-evidence alignment | Whether every strong claim is supported by experiment, proof, citation, example, or qualified language. |
| Method readability | Whether notation, modules, algorithm steps, assumptions, and design choices are introduced in the right order. |
| Experiment narration | Whether tables/figures are introduced before interpretation and whether the text explains what each result proves. |
| Related-work positioning | Whether closest work is compared on technical axes rather than listed chronologically. |
| Terminology and notation consistency | Whether key terms, symbols, dataset names, model names, and claims stay stable across sections. |
| LaTeX and format discipline | Whether the manuscript follows venue style, references, captions, labels, equations, algorithms, and page/line constraints. |
| Reviewer-facing risk | Whether the writing creates avoidable rejection risks: hidden contribution, exaggerated claim, missing limitation, unclear baseline, or inconsistent story. |

## Score Anchors

### 5

The section or paper reads like a strong venue submission: the story is precise, claims are supported, transitions are natural, figures/tables carry evidence, and formatting does not distract.

### 4

Readable and mostly reviewer-proof, but one or two issues still weaken emphasis, evidence alignment, or consistency.

### 3

Understandable but not review-ready. A strict reviewer can follow the work, yet the presentation leaves avoidable doubts about contribution, motivation, evidence, or scope.

### 2

Hard to review fairly. The writing hides the actual contribution, mixes claims, breaks logical order, or leaves major claims unsupported.

### 1

Submission-risk level. The manuscript is incoherent, format-noncompliant, internally inconsistent, or impossible to evaluate from the provided text.

## No-Filler Deduction Format

Every material issue must use:

```text
Location:
Problem:
Why a reviewer deducts:
Concrete edit:
Expected effect:
```

Do not write "improve clarity", "strengthen motivation", "add details", or "polish language" without naming the exact sentence/paragraph role, missing information, and edit action.

## Writing-Only Boundaries

- Do not invent results, citations, baselines, or theorem claims.
- Do not silently rewrite the idea. When a scientific claim is too strong for the evidence, recommend weakening, qualifying, moving, or requesting evidence.
- Do not give acceptance probabilities. Report writing risk and likely reviewer confusion.
- If the user asks for actual rewriting, follow CCFA handoff mode before using `ccf-paper-writer`.
