# Paragraph Review Protocol

Use this file to inspect paragraphs during full-paper or section-level writing review, and for explicit "逐段审稿" requests. The default report follows the selected profile in `../fixed-output-format.md`; paragraph inspection does not require a second report or a complete paragraph ledger.

## Segmentation

Assign stable IDs before reviewing:

```text
Abstract-P1
Intro-P1
Intro-P2
Related-P1
Method-P1
Experiments-P1
Conclusion-P1
Appendix-P1
```

If line numbers are available, include them. If the user provides TeX source, use section commands and blank lines to identify paragraphs. If the user provides pasted text, segment by headings and paragraph breaks.

## Per-Paragraph Review

For each paragraph, inspect:

1. Role: hook, problem, gap, claim, method overview, evidence, limitation, transition, related-work contrast, result interpretation, or summary.
2. Main message: what one sentence should the reviewer retain?
3. Fit: whether the paragraph belongs in this section and whether its position is correct.
4. Logic: whether sentences follow a cause-effect, general-to-specific, claim-to-evidence, or contrast structure.
5. Evidence: whether claims are supported or need citation/result/qualification.
6. Redundancy: whether content repeats earlier material or belongs in appendix.
7. Prose discipline: whether the paragraph uses defensive framing, label-heavy symbols, formula dumping, third-person manuscript voice, punctuation-driven structure, unsupported hype, or overly uniform sentence rhythm.
8. Edit action: keep, reorder, split, merge, cut, move, qualify, expand, or rewrite.

## Explicit Paragraph Review Table

When the user explicitly requests paragraph-by-paragraph output, include a table like:

```text
ID:
Current role:
Reviewer takeaway:
Main problem:
Concrete edit:
Severity: critical / major / minor, or no issue
```

For that explicit request, do not replace the table with a generic section summary. Otherwise, place consequential located findings in the fixed writing profile and do not append an extra per-paragraph table.

## Severity By Consequence

Use the same `critical / major / minor` scale as the fixed finding record. `critical` means an established problem defeats the central argument or makes its essential meaning unreliable; `major` means it materially obstructs understanding or support for an important claim; `minor` means a local clarity or presentation issue. A sound paragraph has no issue, not a compulsory minor finding. In writing-only review, do not infer a scientific defect from wording alone; state the observed communication problem and keep scientific judgments within the requested scope.

Inspect these signals in context and assign severity only after establishing their actual consequence:

- the paragraph claims the central contribution but does not specify the novelty;
- the paragraph makes a strong empirical claim without a result/table/figure reference;
- terminology changes in a way that changes the meaning of the contribution;
- the paragraph breaks the paper's story line or contradicts another section;
- labels, dense formulas, or punctuation chains obscure the actual logic; useful defined labels and necessary mathematics are not defects;
- third-person manuscript narration or defensive phrasing displaces a concrete argument; conventional voice or an evidence-backed qualification is not automatically a problem;
- a related-work paragraph omits the closest comparison axis;
- a method paragraph introduces notation after using it;
- an experiment paragraph reports numbers without interpreting what they prove;
- a limitation or assumption is hidden after a broad claim.

Do not promote a phrase match or material outside the supplied reading scope into a major or critical concern. A verified unsupported claim in the inspected manuscript can still be consequential; missing inputs alone establish a coverage limit. For consequential findings, inspect relevant supplied appendices and use the fixed finding record's evidence and countercheck requirements before retaining the concern.

## Output Discipline

When the manuscript is long, prioritize all abstract/introduction/conclusion paragraphs, all contribution paragraphs, all method-definition paragraphs, and all experiment-result paragraphs. For explicit paragraph reviews, lower-risk paragraphs may receive compact grouped comments with IDs. For default reviews, report the consequential findings once in the fixed profile and keep routine checklist completion internal. State the actual reading scope when coverage is incomplete.
