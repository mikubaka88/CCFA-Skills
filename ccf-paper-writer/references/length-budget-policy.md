# Length Budget Policy

Use this file whenever drafting, expanding, compressing, or submission-preparing a full manuscript.

## Core Rule

A venue-aware paper draft should target the venue's usable main-body budget, not merely compile. A short idea is not permission to produce a short paper when the user asked for a submission manuscript. Expand with evidence-bound content, `TBD` placeholders, and concrete experiment/analysis scaffolds rather than inventing results.

**Critical: "page limit" in most AI conferences (ICLR, NeurIPS, ICML, CVPR) means main text only. References, appendix, acknowledgements, and standalone limitations sections are EXCLUDED from the count.** Your main text should fill the full budget. Do not leave1-2 pages of unused budget "to be safe"---reviewers will notice an underfilled paper.

## Budget Setup

Before full-manuscript drafting, establish:

```text
Target venue:
Template / style:
Main-body page limit:
References counted? yes / no / unknown
Appendix counted? yes / no / unknown
Draft target:
Allowed draft tolerance:
Final submission target:
```

Use the venue guide first. If the local guide lacks a clear page limit, infer a draft target from the venue family and label it `policy-stale`; route final compliance to `ccf-submission-checker`.

Default draft targets:

- Strict page-limited submissions: aim for 85-100% of the main-body limit.
- Early internal drafts: aim for 70-90% unless the user asks for a short proposal.
- Demos, tutorials, or smoke tests: may be shorter only when the user explicitly says demo, sample, short, toy, or skeleton.
- Final submission: must be at or below the official limit after compression.

Slight mismatch is acceptable:

- Under target by <= 15%: acceptable for an internal draft if all required sections have substantive content.
- Under target by > 15%: run expansion before calling it a full manuscript.
- Over target by <= 10%: acceptable for a draft; schedule compression.
- Over target by > 10%: immediately run a standard compression pass or produce a cut plan before review.

## Section Budget

For AI/ML/CV/NLP-style 8-10 page main-body papers:

| Section | Typical share |
| --- | ---: |
| Abstract | 0.15-0.25 page |
| Introduction | 1.0-1.5 pages |
| Related Work / Background | 0.75-1.25 pages |
| Method | 2.0-3.0 pages |
| Experiments | 2.0-3.0 pages |
| Analysis / Ablation / Limitations | 0.75-1.5 pages |
| Conclusion | 0.2-0.4 page |

Adjust by venue family:

- Systems/networking/security papers usually need more method, system design, threat model, implementation, and evaluation detail.
- Theory papers need theorem statements, proof ideas, and technical overview in the main text.
- HCI papers need research questions, participants, procedure, measures, ethics, and analysis method.
- Database/mining papers need problem formalization, algorithm details, complexity, datasets, baselines, and scalability analysis.

## Expansion Before Compression

If a full manuscript is under target, expand in this order:

1. Sharpen the Introduction challenge chain and contribution/evidence preview.
2. Add a focused Related Work contrast with closest-work groups.
3. Make the Method auditable: notation, module motivation, algorithm/pipeline, complexity, assumptions.
4. Add experiment setup details: datasets, metrics, baselines, implementation, hyperparameters.
5. Add main-result, ablation, robustness, efficiency, and failure-analysis scaffolds.
6. Add limitations, ethics/reproducibility, and appendix pointers where expected.

Allowed expansion content:

- Mechanism explanations derived from the user's idea.
- `TBD` placeholders for missing results, figures, and citations.
- Experiment-table templates with empty cells.
- Evidence requirements and planned analyses.
- Clearly marked assumptions.

Forbidden expansion content:

- Invented numerical results.
- Invented citations or baselines.
- Unsupported claims of novelty, superiority, or reviewer reaction.
- Padding, generic field background, or repeated motivation.

## Expansion Content Order

When a manuscript is under target, expand in this priority order---each step adds substantive content, not filler:

1. **Introduction bottleneck exposition:** explain why existing methods fail structurally, not just empirically. Add concrete path-length, complexity, or capability arguments.
2. **Background/Preliminaries:** add formal problem definition, notation, and structural analysis (e.g., complexity tables, dependency path arguments).
3. **Method detail:** add per-component motivation (why this module, what gap it fills), forward equations, and connection to the global insight.
4. **Experiment setup:** add dataset statistics, preprocessing details, baselines with rationale, metric definitions, implementation notes.
5. **Results and analysis:** add result tables, complexity comparisons, ablation motivations (why each test matters), and caveat notes.
6. **Discussion:** add architecture-level analysis (why it works, regime of applicability, failure modes).
7. **Limitations and ethics:** add concrete scope boundaries, failure-mode analysis, and domain-specific impact notes.
8. **References:** ensure all cited works appear in the bibliography with complete metadata.

## Compile And Adjust Loop

When writing a TeX file and a LaTeX engine is available:

1. Compile once to measure pages.
2. If citations/labels/outlines changed, rerun until stable.
3. Compare the PDF page count with the target budget.
4. If under target, expand high-value sections.
5. If over target, run `references/compression-rules.md`.
6. Recompile after substantial expansion or compression.

If compilation is unavailable, estimate with section budgets and mark page count as `not compiled`.

## Output Status

For full manuscripts, include or record:

```text
Length budget:
Current length:
Status: underfilled / target-fit / draft-over / final-over / not compiled
Expansion or compression action:
Remaining evidence gaps:
```
