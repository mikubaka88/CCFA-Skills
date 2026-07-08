# Paragraph Review Protocol

Use this file for full-paper, section-level, or "逐段审稿" requests. The output must show that the manuscript was read paragraph by paragraph.

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

## Required Table

For standard mode, include a table like:

```text
ID:
Current role:
Reviewer takeaway:
Main problem:
Concrete edit:
Severity: high / medium / low
```

Do not replace this table with a generic section summary.

## High-Severity Paragraph Problems

Mark high severity when:

- the paragraph claims the central contribution but does not specify the novelty;
- the paragraph makes a strong empirical claim without a result/table/figure reference;
- terminology changes in a way that changes the meaning of the contribution;
- the paragraph breaks the paper's story line or contradicts another section;
- the paragraph relies on `Q1`/`C1`-style labels, dense formulas, or punctuation chains instead of natural logic;
- the paragraph uses third-person manuscript narration or defensive phrasing that weakens the contribution;
- a related-work paragraph omits the closest comparison axis;
- a method paragraph introduces notation after using it;
- an experiment paragraph reports numbers without interpreting what they prove;
- a limitation or assumption is hidden after a broad claim.

## Output Discipline

When the manuscript is long, prioritize all abstract/introduction/conclusion paragraphs, all contribution paragraphs, all method-definition paragraphs, and all experiment-result paragraphs. For lower-risk paragraphs, use compact grouped comments but still identify IDs.
