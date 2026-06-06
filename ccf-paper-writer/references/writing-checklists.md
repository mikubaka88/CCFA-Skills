# Writing Checklists

Use this file to prevent omissions during planning, drafting, revision, score-risk auditing, and final readiness checks. Load `../../ccf-common/references/task-modes.md` when deciding quick versus standard mode. For small paragraph edits in quick mode, run only the relevant subset and state what was intentionally skipped.

## Quick Mode Checklist

Use this for one paragraph, one small subsection, or single-pass polish:

- Venue or style assumption is clear enough for the local edit.
- Paragraph or subsection role is identified.
- Technical meaning, results, datasets, baselines, and conclusion direction are preserved.
- Local claims are supported, softened, or flagged.
- No citation, result, experiment, or reviewer impact is invented.
- Full paper storyline, full score-risk loop, and final-readiness checks are skipped unless the user requests standard mode.

Compact status:

```text
Mode: quick
Local checks:
Skipped standard checks:
Unresolved:
```

## Standard Mode Checklist

Use the remaining checklist sections for full sections, whole papers, score-risk work, final readiness, literature-linked writing, or output that feeds another CCFA module.

## Intake Checklist

- Target venue, track, and paper type are known, or the user-custom format is explicitly assumed.
- Deadline pressure and desired output granularity are known: plan, rewrite, line edit, review, or final check.
- Available materials are listed: manuscript, appendix, figures, tables, reviews, code, experiments, references, style exemplars.
- Missing materials that affect confidence are named.
- Claims that cannot be verified from provided materials are not treated as facts.

## Venue And Style Checklist

- Venue family is mapped with `ccf-a-venue-map.md` when a CCF-A target is named.
- Venue expectations are selected from `venue-adapters.md`.
- If no venue is named, `custom-format/default-user-format.md` is used and labeled.
- Exemplar cards are used only for writing moves, not wording or technical content.
- Venue-specific evidence package is visible: baselines, ablations, proof, user study, systems evaluation, security threat model, visual evidence, or theory proof as appropriate.

## Global Story Checklist

Every major output must preserve this chain:

```text
task -> gap -> root challenge -> insight -> method mechanism -> evidence -> limitation
```

Check:

- The problem is concrete enough for the venue's audience.
- The gap explains why prior work is insufficient.
- The root challenge is technical, scientific, empirical, or human-centered, not just "existing methods fail."
- The insight explains why the proposed method should work.
- The method mechanism connects to the insight.
- The evidence package tests the central claim.
- The limitation bounds the claim honestly.

## Section Revision Checklist

- The section role is named before revision.
- Each paragraph has one main message.
- The first sentence of each paragraph signals that message.
- Terminology is stable across sections.
- Transitions show cause, contrast, consequence, refinement, or example.
- Figures and tables are introduced before interpretation.
- Captions state what the reviewer should learn.
- The section ends with the intended next-step logic when appropriate.

## Claim-Evidence Checklist

For every major Abstract, Introduction, and Conclusion claim:

```text
Claim:
Location:
Evidence:
Evidence type:
Support level: strong / adequate / weak / absent
Required action:
```

Rules:

- Supported claims may be sharpened.
- Weakly supported claims must be narrowed or tied to stronger evidence.
- Unsupported claims must be removed, weakened, or marked as requiring new evidence.
- Evidence hidden only in the appendix must be signposted in the main text.

## Reviewer-Risk Checklist

Scan for:

- unclear contribution,
- weak novelty positioning,
- missing or stale related work,
- significance unclear for the venue,
- unsupported central claim,
- weak baseline,
- missing ablation, proof, user study, or system evaluation,
- unfair protocol or metric,
- reproducibility gap,
- figure/table readability issue,
- overclaim,
- generic limitation,
- ethics or responsible-research issue,
- venue mismatch.

## Score-Lifting Checklist

Use with `score-lifting-loop.md` and, only when explicitly requested or allowed by the CCFA handoff mode, `ccf-scientific-reviewer` for full scientific review or `ccf-writing-reviewer` for writing-only review. Use `ccf-literature-searcher`, `ccf-experiment-designer`, or `ccf-paper-compressor` through the same handoff rule when the blocker is missing prior art, evidence design, or page-limit pressure.

- Current likely score or stance is stated.
- Target score or readiness threshold is stated.
- Top score blockers are ranked by severity.
- Each blocker has a fix class: writing-fixable, analysis-fixable, citation/positioning, figure/table, reproducibility, requires-new-result, accepted-limitation, or venue-mismatch.
- Literature-search, experiment-design, and compression blockers are separated from ordinary prose fixes.
- Writing-only fixes are separated from fixes requiring new experiments, proofs, studies, or baselines.
- Conditional review-risk effect is attached only to concrete changes.
- After revision, the same reviewer concern is re-tested.

## Final Readiness Checklist

Do not call a paper or section ready until:

- The target venue/custom format is clear.
- The global story is internally consistent.
- Central claims have visible support.
- Closest prior work and strongest baselines are handled.
- Venue-specific evidence is visible in the main paper.
- Limitations are honest and bounded.
- Reproducibility and ethics details are present where relevant.
- No high-severity issue remains unlabeled.
- The final answer states passed checks, skipped checks, and unresolved risks.

## Minimal Checklist Status

Use this compact status when output space is limited:

```text
Checklist status:
- Venue/style:
- Storyline:
- Section roles:
- Claim-evidence:
- Reviewer risks:
- Score-risk:
- Final readiness:
- Unresolved:
```
