# Compression Rules

Use this file to reduce length while preserving the paper's story, evidence, and venue fit.

Compression applies when the user requests it, specifies a word/page limit, or requests a submission-ready deliverable. For a new manuscript, complete the content and alignment check in `materials-to-manuscript.md` before fitting. Exceeding an eventual venue limit does not trigger compression during an unconstrained first draft. Use `length-budget-policy.md` for the active fitting constraint; expand only real explanatory gaps, not empty page area.

## Mode Selection

Quick mode:

- One paragraph, one subsection, local polish, or a simple word-count reduction.
- Do not require a full checklist.
- Preserve facts and numbers exactly.
- Return the compressed text; keep routine risk status internal.

Standard mode:

- Full section, multi-section, full manuscript, page-limit, or camera-ready compression.
- Use an internal content inventory or cut plan when substantive changes need coordination; show it only when requested or needed for an unresolved choice.
- Check claim-evidence preservation.
- Remove redundant wording within the existing compression authorization. Ask only when moving or deleting important scientific content leaves a strategic choice that the user's instructions do not resolve.

If a draft is only slightly over budget (<= 10%), first compress wording, repeated motivation, and low-value background. If it is substantially over budget (> 10%), create a section-level cut plan before rewriting.

## Compression Hierarchy

Cut in this order:

1. Repeated motivation.
2. Generic field background.
3. Unnecessary adjectives and promotional phrasing.
4. Duplicate definitions.
5. Overlong transitions.
6. Implementation details that can move to appendix.
7. Secondary experiments or extended analyses that can move to appendix.
8. Low-impact related work sentences after the closest work is covered.
9. Optional caveats that duplicate the Limitations section.

Protect:

- Central problem and root challenge.
- Core insight and method mechanism.
- Claims tied to contributions.
- Numbers, metrics, datasets, and baseline names.
- Limitations that bound overclaiming.
- Reproducibility details required by the venue.
- Ethics, threat model, or user-study details when required.

## Appendix/Delete Decision

Move to appendix when:

- The material is important for audit but not needed for first-pass understanding.
- It is extended derivation, proof detail, extra tables, hyperparameters, implementation detail, or secondary analysis.
- The main text already states the takeaway.

Delete when:

- The material repeats an earlier point.
- The claim is unsupported and not essential.
- The wording is generic venue boilerplate.
- The citation is background-only and not needed for positioning.
- The sentence increases confidence without adding evidence.

Ask once for a material unresolved choice after completing unaffected compression, for example:

```text
The two main comparisons cannot both fit at readable size. Which should remain in the main text, [comparison A] or [comparison B], with the other preserved in the appendix?
```

Reuse any applicable prior choice or authorization, including aggressive deletion, appendix-only compression, or camera-ready condensation. Removing repeated wording needs no new permission; preserve essential science and required disclosures.

## Venue Style

AI/ML/CV/NLP:

- Keep the problem, insight, method mechanism, and evidence summary visible.
- Compress background and low-impact related work first.
- Keep ablation and baseline rationale clear enough to interpret the comparisons.

DB/systems/networks:

- Keep workload, deployment assumptions, architecture, bottleneck, and end-to-end results.
- Move lower-level implementation and extra sensitivity studies to appendix if needed.

Security:

- Keep threat model, assumptions, guarantees, and ethics/disclosure scope.
- Do not compress away boundary conditions.

HCI:

- Keep research questions, participant/procedure essentials, analysis method, and claim scope.
- Move instrument details or long coding examples to appendix.

Theory/PL/FM:

- Keep theorem statement, assumptions, proof idea, and relation to prior bounds.
- Move proof details but not proof roadmap.

## Sentence-Level Moves

- Replace broad openings with specific problem statements.
- Merge citations that support the same contrast.
- Convert repeated clauses into one scoped claim.
- Use one term consistently rather than alternating synonyms.
- Prefer "because" and "therefore" relations over long rhetorical bridges.
- Replace verbose contribution bullets with claim + evidence pairs.
- Remove defensive hedges, unexplained labels, punctuation-heavy chains, and third-person manuscript narration before cutting substantive content.
- Preserve sentence rhythm; do not compress every sentence into the same short template.

## Risk Labels

Use these labels internally to check preservation; expose only a material unresolved consequence or a requested change record:

- `preserved`: claim/evidence still intact.
- `weakened`: claim was narrowed to match evidence.
- `moved-to-appendix`: detail removed from main flow but still available.
- `deleted`: removed because redundant or unsupported.
- `risk`: compression may harm clarity or auditability.
