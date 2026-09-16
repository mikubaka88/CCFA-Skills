# Conference Review Workflow

Use this file for standard-mode full scientific paper review.

## Intake

Record:

```text
Venue/year/track:
Contribution type:
Field:
Paper title or slug:
Input format: pdf / tex / markdown / pasted text / folder
Materials read:
Materials missing:
Privacy boundary:
Search permission:
```

If local source is available, inspect files before asking questions. If only pasted text is available, review that scope and state coverage separately from confidence in the actual local findings.

## Reading Passes

Cover these four reading purposes while reusing the extracted source and exact locations; they do not require four full rereads:

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
- Search only to resolve material novelty/positioning questions; reuse verified sources. Do not require a minimum number of searches, papers, annotations, or tool calls.

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

Use the canonical scientific dimensions in `calibration-and-rank.md`; the audits above are evidence-gathering lenses, not additional scores. Before scoring, revisit every major/critical criticism and inspect the strongest passage, proof, appendix, or source that could answer it. Record the countercheck in the finding, narrow or withdraw a refuted concern, and preserve unresolved uncertainty as a question. Reuse extracted evidence and check only the passages needed; do not mandate another full-paper pass.

## Report Generation

Use the detailed structure in `fixed-output-format.md` by default, or its brief version for an explicit brevity request; an exact user format takes precedence. Consolidate consequential findings under stable concern IDs and verify their correctness, significance, and source support. Use that reference's fixed finding fields and bracketed ID references. Scientific findings require evidence; a question or missing input is not automatically a defect. Preserve concern IDs when checking a revision.

Report location:

- Resolve an existing requested report path first. If file output is in scope and a local paper path exists, use `ccfa-review-reports/` beside that file or top-level manuscript folder.
- Otherwise return the review in the conversation unless the user requests a saved report. Honor no-new-files and exact-output constraints.

Canonical filename:

```text
<paper-slug>-<venue>-review.md
```

Use lowercase ASCII for the slug; replace spaces and punctuation with hyphens. If the title is unknown, use `untitled-paper`. Put review date, manuscript version, and review round in report metadata. Overwrite the canonical report on ordinary reruns and rely on version control for rollback. Create snapshots only when the user requests them or an external process requires an immutable record.

Validate a saved default-format report with the existing Markdown checker described in `fixed-output-format.md` after substantive evidence review. A structural pass is not a claim of scientific correctness.
