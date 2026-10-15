# Writing Checklists

Use this file to prevent omissions during planning, drafting, revision, score-risk auditing, and final readiness checks. Load `../../ccf-common/references/task-modes.md` when deciding quick versus standard mode. For writing tasks, this checklist is usually internal. Show checklist status only when the user asks for audit/rationale, when the output feeds another CCFA skill, or when an unresolved risk affects reliability.

## Quick Mode Checklist

Use this for one paragraph, one small subsection, or single-pass polish:

- Venue or style assumption is clear enough for the local edit.
- Paragraph or subsection role is identified.
- Technical meaning, results, datasets, baselines, and conclusion direction are preserved.
- Local claims accurately express supplied evidence; retain justified uncertainty without reflexively softening every result.
- No citation, result, experiment, or reviewer impact is invented.
- Prose follows `prose-quality-guardrails.md`: no defensive framing, label-heavy symbols, number-only abstract style, third-person manuscript voice, or punctuation-driven structure.
- Short edited prose has no avoidable em dash, throat-clearing opener, forced triad, synonym cycling, or repeated sentence template.
- Full paper storyline, full score-risk loop, and final-readiness checks are skipped unless the user requests standard mode.

Visible output default: put the revised text first and preserve the user's original Markdown/LaTeX/citation format. Use this compact status only when useful:

```text
Mode: quick
Local checks:
Skipped standard checks:
Unresolved:
```

## Standard Mode Checklist

Use applicable remaining sections for substantial writing, score-risk work, or final readiness. Passing a bounded contribution to another CCFA skill does not by itself require the whole checklist; retain the actual scope and relevant dependencies.

## Intake Checklist

- Draft phase is explicit: content-first, alignment, or requested submission fit. A named venue has not silently imposed an initial page quota.
- Supplied research documents have been read by their actual roles; proposed designs, confirmed procedures, examples, target statistics, and observed results are distinguished.
- Results-pending scope is honored: complete the supplied experimental scaffold unless the user explicitly requests an empty experimental section.
- Target venue, track, and paper type are known when relevant. Preserve a supplied format; for a new LaTeX paper without a venue use the disclosed NeurIPS format fallback. Apply the custom format only when requested or established.
- Deadline pressure and desired output granularity are known: plan, rewrite, line edit, review, or final check.
- Available materials are listed: manuscript, appendix, figures, tables, reviews, code, experiments, references, style exemplars.
- Missing materials that affect confidence are named.
- Claims that cannot be verified from provided materials are not treated as facts.

## Venue And Style Checklist

- Venue family is mapped with `ccf-a-venue-map.md` when a CCF-A target is named.
- Venue expectations are selected from `venue-adapters.md`.
- Preserve non-LaTeX prose, supplied templates, and requested custom formats. Activate `custom-format/default-user-format.md` only when requested or established; non-LaTeX output alone does not select it.
- For a new LaTeX manuscript without a usable target template, use the disclosed NeurIPS format fallback. A missing local venue guide does not override a supplied template; route final rule verification to `ccf-submission-checker` when compliance is requested.
- Exemplar cards are used only for writing moves, not wording or technical content.
- Venue-specific evidence package is visible: baselines, ablations, proof, user study, systems evaluation, security threat model, visual evidence, or theory proof as appropriate.

## Global Story Checklist

Every major output must preserve this chain:

```text
task -> gap -> root challenge -> insight -> method mechanism -> evidence -> supported implication
```

Check:

- The problem is concrete enough for the venue's audience.
- The gap explains why prior work is insufficient.
- The root challenge is technical, scientific, empirical, or human-centered, not just "existing methods fail."
- The insight explains why the proposed method should work.
- The method mechanism connects to the insight.
- The evidence package tests the central claim.
- Material assumptions and observed limitations are retained at the relevant location; no generic caveat is required.
- Related motivations and observations form a coherent theme without being collapsed into one module or mechanically forced into one insight.

## Section Revision Checklist

- The section role is named before revision.
- Each paragraph has one main message.
- The first sentence of each paragraph signals that message.
- Terminology is stable across sections.
- Previously defined concepts are not repeated without adding new logic.
- Transitions show cause, contrast, consequence, refinement, or example.
- Sentence lengths vary naturally; the paragraph does not repeat the same syntactic template.
- Figures and tables are introduced before interpretation.
- Captions state what the reviewer should learn.
- The section ends with the intended next-step logic when appropriate.

## Prose Quality Checklist

Use with `prose-quality-guardrails.md` before calling a draft polished:

- The manuscript speaks from the authors' scientific position, not from a third-person report about "the paper" or imagined reviewers.
- The abstract contains task, gap, insight or method, evidence, and scope; it is not a column of numbers in sentence form.
- `Q1`, `Q2`, `C1`, `C2`, `RQ1`, and similar labels are absent from running prose unless explicitly required.
- Equations, theorems, and symbols are introduced with their scientific purpose and do not appear as dense blocks without narration.
- Quotation marks, colons, dashes, slashes, arrows, and bracketed labels are not used as substitutes for logical transitions.
- Authored prose prefers zero em dashes and contains no more than three across the full paper, excluding direct quotations.
- Throat-clearing openers are removed when the following clause can stand directly.
- Contributions and arguments use their natural number of parts instead of forced three-item lists.
- Canonical technical terms remain stable; near-synonyms are not rotated for surface variety.
- Nearly uniform sentence runs have been reviewed for readability; keep justified procedural or comparative parallelism.
- Long compound sentences are split when they mix motivation, mechanism, evidence, and conclusion.
- Canonical terms are used consistently across abstract, introduction, method, experiments, and conclusion.
- Strong claims avoid hype and are scoped to available evidence.
- Each paragraph progresses by cause, contrast, refinement, example, or consequence.
- Literal sentence and paragraph links are readable; nouns, variables, references, and comparators do not appear without introduction.
- Manuscript narration expresses actual relationships, preserves useful procedure numbering, and avoids uncommon synonym substitutions, empty execution narration, and ambiguous technical promises.

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

Use only for requested review-related revision or concrete evidence gaps, not as a source of hypothetical objections for ordinary writing. Scan applicable issues:

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

Use with `score-lifting-loop.md` and, only when explicitly requested or allowed by the CCFA handoff mode, `ccf-paper-reviewer` for scientific or writing review. Use `ccf-literature-searcher`, `ccf-experiment-designer`, or `ccf-paper-writer` compression mode through the same handoff rule when the blocker is missing prior art, evidence design, or page-limit pressure.

- Current likely score or stance is stated.
- Target score or readiness threshold is stated.
- Top score blockers are ranked by severity.
- Each blocker has a fix class: writing-fixable, analysis-fixable, citation/positioning, figure/table, reproducibility, requires-new-result, accepted-limitation, or venue-mismatch.
- Literature-search, experiment-design, and compression blockers are separated from ordinary prose fixes.
- Writing-only fixes are separated from fixes requiring new experiments, proofs, studies, or baselines.
- Conditional review-risk effect is attached only to concrete changes.
- After revision, the same reviewer concern is re-tested.

## Final Readiness Checklist

For a content-first draft, use `materials-to-manuscript.md` to check substantive completeness and alignment. Intentionally absent results do not block drafting, but must not be represented as evidence. Inspect summaries, contributions, captions, and conclusion for dependent claims; use `\emptycell` values without fabricated trends, ranks, or analysis. Keep specific missing inputs in the delivery note. Do not invoke page fitting or submission scores for this check.

For a final submission-readiness request, do not call the paper ready until:

- The target venue/custom format is clear.
- The global story is internally consistent.
- The prose quality checklist has no high-risk pattern remaining.
- `scripts/check_prose_quality.py` candidate locations have been reviewed in context. Correct defensive prose and punctuation violations; keep justified scientific language. A warning-free `--strict` run is not required for publication readiness.
- Central claims have visible support.
- Closest prior work and strongest baselines are handled.
- Venue-specific evidence is visible in the main paper.
- Limitations are honest and bounded.
- Reproducibility and ethics details are present where relevant.
- No high-severity issue remains unlabeled.
- Return the requested prose or files first. Mention only material unresolved evidence or requested validation; omit routine process reports.

## Minimal Checklist Status

Use this compact status when output space is limited:

```text
Checklist status:
- Venue/style:
- Storyline:
- Section roles:
- Prose quality:
- Claim-evidence:
- Reviewer risks:
- Score-risk:
- Final readiness:
- Unresolved:
```
