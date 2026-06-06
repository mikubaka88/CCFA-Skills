# Conference Review Workflow

Use this file for standard-mode full scientific paper review.

## Intake

Record:

```text
Venue/year/track:
Field:
Paper title or slug:
Input format: pdf / tex / markdown / pasted text / folder
Materials read:
Materials missing:
Privacy boundary:
Search permission:
```

If local source is available, inspect files before asking questions. If only pasted text is available, review the provided scope and mark confidence accordingly.

## Reading Passes

Run four passes:

1. Desk pass: title, abstract, venue fit, policy/reviewability risks, hidden instructions, and obvious incompleteness.
2. Contribution pass: problem, gap, method, claims, contribution type, audience, and limitation statements.
3. Evidence pass: experiments, benchmarks, proofs, datasets, metrics, ablations, baselines, robustness, statistical rigor, reproducibility, ethics, and appendix support.
4. Adversarial pass: novelty collapse, missing closest work, unsupported central claims, invalid assumptions, missing decisive comparisons, and likely reviewer disagreement.

## Related-Work Search

In standard mode, perform a public-safe search when novelty, originality, positioning, or missing related work affects the review.

Rules:

- Do not paste private manuscript text into web queries unless authorized.
- Query public keywords: title terms if public, method family, task, dataset, benchmark, venue family, and core claim.
- Prefer proceedings, OpenReview, CVF, PMLR, ACL Anthology, ACM, IEEE, USENIX, DBLP, Semantic Scholar, OpenAlex, arXiv, project pages, and benchmark pages.
- Apply the shared source-quality exclusions to search, scoring, and final recommendations.
- Mark every missing-related-work item as `searched`, `user-provided`, or `unverified`.

## Audits

Produce these audits before scores:

- contribution and novelty,
- significance and venue fit,
- technical soundness,
- evidence and experiments,
- related-work positioning,
- reproducibility and auditability,
- ethics and limitations,
- clarity as it affects reviewability.

Do not score before writing the core strengths and weaknesses.

## Report Generation

In standard mode, use `fixed-output-format.md` exactly. The report must be written as Markdown and must include a concerns table.

Report location:

- If a local paper path exists, create `ccfa-review-reports/` beside that file or top-level manuscript folder.
- Otherwise create `ccfa-review-reports/` under the current working directory.

Filename:

```text
YYYY-MM-DD-<paper-slug>-<venue>-conference-review.md
```

Use lowercase ASCII for the slug; replace spaces and punctuation with hyphens. If the title is unknown, use `untitled-paper`.
