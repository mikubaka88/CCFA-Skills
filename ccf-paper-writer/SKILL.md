---
name: ccf-paper-writer
description: "Own text-changing deliverables for CCF papers: draft, rewrite, revise, polish, or compress manuscript and presentation prose while preserving supplied scope and evidence. Use for abstract/introduction/related work/method/experiment writing, paragraph edits, reviewer-motivated rewrites, rewrite based on review with no new review, slides/poster/talk/Q&A, 润色论文, 改写, 写作, 压缩论文. Do not use for assessment-only requests such as full review, scientific review, scoring, issue diagnosis, evidence audit, submission checks, or rebuttal, especially when the user says no rewrite."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Writer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

This is the manuscript text owner. It also owns local compression and presentation adaptation because both change paper wording or paper-derived communication. Keep idea scope, method mechanism, experiments, numbers, and conclusions unchanged unless the user explicitly authorizes a research-scope change. Follow `../ccf-common/references/task-modes.md`, especially the output-flexibility rule: user-requested output format comes before this skill's internal checklist shape.

Run `ccf-humanization` as the first manuscript-facing preflight and apply `../ccf-humanization/references/humanization-policy.md`. Write direct academic prose without defensive strategies, reviewer simulation, boilerplate disclaimers, repeated improbable cases, or internal engineering-status narration. Put concerns that require judgment in a separate user-review warning; do not inject warning prose or edit files solely to encode a warning. Verify internally that every method named in the paper is a confirmed full version under `../ccf-humanization/references/experiment-discipline.md`; never substitute a simplified, toy, proxy, reduced, approximate, or debug version. In the manuscript, state the actual method and scientifically relevant configuration naturally; do not write that it is confirmed, approved, or publication-ready.

Do not invent results, baselines, experiments, reviewer impact, or missing evidence. For citations, never guess bib entries: search for the correct paper and obtain its bib entry before citing `references/citation-workflow.md`. Handle unsupported claims through a narrower accurate claim or a separate user-review warning; do not insert defensive caveats into the manuscript without approval.

When running local writing self-review, score-risk checks, or reviewer-style revision loops, load `../ccf-common/references/review-output-standards.md`. Use scores as diagnostic feedback only; do not present them as acceptance probabilities.

## Core Rule

Write for the target CCF venue, not for a generic paper. Improve structure, section logic, paragraph roles, contribution framing, claim-evidence alignment, reviewer-facing clarity, and concise presentation. A submission manuscript should also target the venue's usable page budget: too short is a writing failure, not just a harmless demo choice; too long triggers compression. Do not use reference papers to copy wording, claims, examples, technical content, or distinctive phrasing.

The visible output should feel like useful writing, not a process report. Use planning tables and checklists internally; show them only when the user asks for planning, audit status, or rationale.

Scale reference loading to the requested artifact. For a bounded evidence-only task such as one abstract, one method synopsis, one caption, one paragraph, or an exact JSON response, read only this `SKILL.md`, the humanization policy, and `references/prose-quality-guardrails.md` unless the task itself requires another reference. Do not load venue guides, exemplar cards, citation workflows, storyline blueprints, section modules, length budgets, templates, or reviewer loops merely because they exist. Exact-output and supplied-evidence constraints take precedence over the full-manuscript workflow.

Apply `references/prose-quality-guardrails.md` to all manuscript-facing prose. Avoid defensive or incremental framing, label-heavy symbols such as `Q1`/`C1`, formula dumping, number-only abstracts, punctuation-driven structure, overlong compound sentences, strange shorthand, third-person narration about "the paper", and unsupported hype. Prioritize cohesive paragraph logic, stable terminology, evidence-bounded claims, and varied sentence rhythm.

Treat prose-pattern checks as writing-quality controls, not detector-evasion tactics. Use `../ccf-humanization/references/humanization-policy.md` as the single source for punctuation and pattern thresholds. Run `scripts/check_prose_quality.py` for full sections or papers when local execution is available, then fix the prose rather than merely reporting the count.

## Format And Output Policy

1. For polishing, rewriting, line editing, or compression of existing text, preserve the original format unless the user asks to restructure it. Keep LaTeX commands, section headings, citation keys, labels, equations, figure/table environments, Markdown headings, lists, and table shape intact whenever possible. Return the revised text in the same format first.
2. For one paragraph or one subsection, default to a direct improved version plus a short optional note only if a claim, number, citation, or meaning changed.
3. For a rough idea or "write from scratch" request, create the requested artifact rather than stopping at a plan. If the user asks for a paper/manuscript and names a target venue, read `references/venue-guides/index.md` and the specific venue guide, then draft in that venue's LaTeX style. Establish a page/word budget from the venue guide and `references/length-budget-policy.md`; if the venue is absent or no venue is provided, use the NeurIPS guide and `ccf-latex-templates/NeurIPS/neurips_2026.tex` as the fallback and label the assumption.
4. If the user requests Markdown, Chinese prose, English prose, an outline, a full LaTeX file, a diff-style rewrite, or a section-only output, follow that request. Do not force the default CCF paper storyline order when the user's format is intentional.
5. Be flexible outside review tasks. When a choice could improve the paper but changes direction, present it as a concise question or option, for example: "可以把贡献改成 benchmark 视角吗？这会降低方法新颖性风险，但需要补数据集定位。"
6. Never invent results, baselines, experiments, reviewer impact, or missing evidence. Obtain correct citations through literature search per step5; never guess a bib entry. When evidence is absent, use `TBD`, a cautious placeholder, or a clearly marked "needs evidence" sentence.
7. Do not block drafting because current venue policy is not freshly verified. Use the local venue guide for draft shape, add a freshness note when relevant, and route final compliance to `ccf-submission-checker`.
8. For full-paper requests, produce a full manuscript-level artifact: Abstract, Introduction, Background/Related Work or Preliminaries, Method, Experiments, Analysis/Ablation, Conclusion, References, and venue-required sections or appendix/checklist placeholders. Add limitations, ethics, or reproducibility prose only when required by the venue or scientifically material; route judgment-sensitive wording through `ccf-humanization` rather than padding the paper with generic caution. Aim for the target venue's draft page budget, usually 85-100% of the main-body limit for submission-style drafts. Do not answer a full-paper request with only an abstract, outline, or short demo snippet.
9. If the manuscript is materially under target, expand before calling it complete. Expand with mechanism detail, related-work structure, scientifically relevant method specification drawn from the internally confirmed configuration, experiment setup, and analysis scaffolds; do not pad with generic caveats, hypothetical failure cases, process-status language, or invented evidence. If it is over target, use local compression mode and `references/compression-rules.md`.
10. Keep outputs information-dense. Avoid boilerplate disclaimers and empty headings; each visible section should contain concrete paper content, evidence status, or actionable revision information.

## Modes

- `draft`: create or revise paper sections.
- `polish`: improve clarity, flow, terminology, and claim-evidence presentation.
- `compress`: shorten text to word/page limits using `references/compression-rules.md` without changing claims or numbers.
- `presentation`: convert a completed or near-completed paper into slides, poster, talk script, figure narration, and Q&A, without replacing submission review.

## Workflow

1. Run the `ccf-humanization` preflight, then identify mode, requested output format, target venue, paper type, draft state, available evidence, target length/page budget, and whether idea-scope changes are authorized. Load `references/output-style-policy.md` for source-format preservation, ambiguous output choices, or from-scratch LaTeX drafting. For an exact JSON/text schema, follow the user's schema directly without loading that reference.
2. If the user supplied an existing manuscript or canonical draft, preserve its format and revise that file in place unless the user asked for a new structure or snapshot. Follow `../ccf-common/references/artifact-contracts.md`: do not create `v2`, `revised`, dated, timestamped, or `final-final` copies for ordinary iterations. Use repository history for rollback and keep transient prompts, critiques, and attempts out of the project tree.
3. **Select venue and exemplars only when needed.** For a full manuscript, a from-scratch submission draft, or an explicit style/venue adaptation, load the venue guide and at most the matched exemplar cards from `references/exemplars/index.md`. If such a task has no venue, load `references/custom-format/default-user-format.md`; use NeurIPS only as the full-manuscript LaTeX fallback. Then load `references/length-budget-policy.md` and create a section-level length plan. Skip this entire step for bounded evidence-only artifacts, exact-format responses, ordinary polishing, captions, abstracts, or section snippets unless the user explicitly requests venue/exemplar adaptation.
4. Build or update the global story with `references/storyline-blueprint.md` for full manuscripts, substantial introductions, explicit storyline generation, narrative design, or research-insight framing. For a bounded evidence-only abstract or synopsis, use the compact arc already stated here without loading the blueprint: scientific origin -> knowledge gap -> core insight -> method mechanism -> evidence -> bounded claim. Keep this internal unless the user asked for a plan.
5. **Prepare citations** for full manuscripts and section drafts that need literature support: load `references/citation-workflow.md`, identify citation slots, obtain verified entries, and update the project bibliography. If the user explicitly limits the task to supplied evidence or forbids browsing/citations, honor that constraint and do not load the citation workflow or search for literature. If the closest-competitor literature is required but unknown, hand off to `ccf-literature-searcher` before continuing.
6. Always apply `references/prose-quality-guardrails.md`. Load `references/research-writing-patterns.md`, `references/section-modules.md`, and `references/writing-checklists.md` only for full-paper work, substantial section drafting, or explicit structure design. A bounded abstract, method synopsis, caption, paragraph edit, or exact JSON task should not trigger those references by default. For full manuscripts, compare the draft against the length budget and expand or compress as needed.
7. **Compile and check** (mandatory for full manuscripts when a LaTeX engine is available): compile the draft, measure the actual page count, and compare against the venue budget from step3. If under target by >15%, expand with mechanism detail, scientifically relevant method specification, experiment setup, and substantive analysis, not generic limitations, defensive prose, internal confirmation language, or invented results. If over target by >10%, compress with `references/compression-rules.md`. Recompile after any substantial change and repeat until the page count is within tolerance. Record the final status: `underfilled / target-fit / draft-over / final-over / not compiled`.
8. For compression, load `references/compression-rules.md`; return compressed text in the same format and include a cut log only when requested or when content was materially removed.
9. For presentation adaptation, derive slides/poster/talk/Q&A only from the manuscript and supplied evidence, in the user's requested slide/poster/script format.
10. If current literature, baselines, or experiments are missing, ask a targeted question or hand off to `ccf-literature-monitor` for recent-paper/competitor watch, `ccf-literature-searcher` for deep retrieval, or `ccf-experiment-designer` for experiment design. For publication-grade figure/table layout, visual contracts, palette choices, caption placement, or manuscript visual integration, hand off to `ccf-visual-composer`. Do not fill gaps by invention.
11. Before calling text ready, rerun `ccf-humanization`, verify that only confirmed full method versions appear, and run the final prose self-audit in `references/prose-quality-guardrails.md`. For a full section or paper, run `scripts/check_prose_quality.py` when local execution is available. Resolve all hard failures, especially a full-paper em-dash count above three. Keep any unresolved concern outside the manuscript as a user-review warning. Run a local score-risk check only when it adds concrete value; when scientific judgment is needed, hand off to `ccf-paper-reviewer`.

## Post-Writing Coordination

After producing a complete manuscript, inform the user which CCFA skills are relevant to the next stage unless the user requested an exact output shape, JSON-only response, direct file edit, or no process commentary. Do not append handoff material that would violate the requested format.

State concisely what was produced and which skills can pick up from here:

``text
Next CCFA skills available:
- ccf-paper-reviewer: scientific review, score prediction, reviewer simulation, venue-fit check
- ccf-integrity-auditor: citation existence, claim-evidence consistency, bibtex correctness
- ccf-submission-checker: venue template compliance, page/anonymity limits, LaTeX compilation
- ccf-experiment-designer: missing experiments, baseline design, ablation planning
- ccf-visual-composer: publication-grade figures/tables, palette, caption, layout, visual QA
- ccf-literature-monitor: recent-paper tracking, competitor monitoring, novelty-threat alerts
- ccf-literature-searcher: missing related work, closest-competitor search
- ccf-rebuttal-writer: reviewer response, rebuttal drafting, revision ledger
- ccf-pipeline-orchestrator: full-project planning, stage gates, next-skill routing
``

Only list skills that are actually relevant to the paper current state. Do not suggest a skill that would have nothing to do.

## Adaptive Output Contract

- Polish/rewrite/compress existing text: output the revised text first, in the same format. Add brief notes only for changed meaning, unsupported claims, or user-requested rationale.
- Draft from idea: output the requested artifact. For a manuscript request, default to a LaTeX draft with venue assumptions, page budget, and `TBD` evidence placeholders. If no target venue guide exists, use NeurIPS fallback. A short seed should become a full submission-shaped manuscript unless the user explicitly asked for a short demo or skeleton.
- Section planning: output the section plan or paragraph roles only when the user asks for planning or the input is too incomplete to draft responsibly.
- Presentation: output slides, poster copy, talk script, or Q&A in the requested format.
- Full standard work may include a compact status block: mode, venue assumption, evidence gaps, and next CCFA owner.

## Reference Files

- `references/venue-guides/index.md` and `references/venue-guides/<venue>.md`: venue writing and format constraints.
- `references/output-style-policy.md`: user-format priority, edit-format preservation, and NeurIPS fallback behavior.
- `references/length-budget-policy.md`: venue page/word budget, underfilled draft expansion, compile-adjust loop, and compression trigger.
- `references/research-writing-patterns.md`: section-level patterns, dense output rules, and exemplar-mode adaptation.
- `references/prose-quality-guardrails.md`: anti-defensive prose rules, paragraph cohesion, terminology consistency, evidence-bounded claims, sentence rhythm, and final prose self-audit.
- `scripts/check_prose_quality.py`: deterministic, non-mutating prose-pattern check for em dashes, opening filler, repetitive structure, punctuation density, and sentence rhythm.
- `references/storyline-blueprint.md`: whole-paper story, multi-expert storyline generation, scientific storytelling structure, and claim construction.
- `references/section-modules.md`: section drafting.
- `references/writing-checklists.md`: readiness checks.
- `references/score-lifting-loop.md`: apply evidence-backed reviewer deductions without creating a second score.
- `references/expert-review-loop.md`: compatibility bridge from reviewer findings to writing-owned edits.
- `../ccf-common/references/review-output-standards.md`: quantitative feedback, reviewer-panel discipline, score-change conditions, and final output self-check.
- `references/compression-rules.md`: page/word compression.
- `references/table-style-guide.md`: LaTeX table beautification: booktabs rules, number precision, narrow-column fixes, caption style, and placement.
- `references/exemplars/`: style-move references; never copy content.
- `../ccf-humanization/references/humanization-policy.md`: priority rules for direct academic prose, warning-only issues, non-injection, unfavorable information, and generic SHA-256/checksum removal.
- `../ccf-humanization/references/experiment-discipline.md`: confirmed full method identities and the prohibition on simplified publication variants.
