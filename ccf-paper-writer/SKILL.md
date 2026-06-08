---
name: ccf-paper-writer
description: "Plan, draft, revise, polish, compress, and presentation-adapt CCF research paper text while preserving user-supplied idea scope and evidence. Use for paper writing, abstract/introduction/related work/method/experiment writing, polishing, page/word compression, slides/poster/talk/Q&A preparation, 润色论文, 写作, 压缩论文, 报告展示. Do not perform full review, evidence audit, submission-package checks, or rebuttal as the main task."
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

Do not invent results, baselines, experiments, reviewer impact, or missing evidence. For citations, never guess bib entries: search for the correct paper and obtain its bib entry before citing per 
eferences/citation-workflow.md. Unsupported claims must be weakened, marked as needing evidence, or left unchanged with a risk note.

## Core Rule

Write for the target CCF venue, not for a generic paper. Improve structure, section logic, paragraph roles, contribution framing, claim-evidence alignment, reviewer-facing clarity, and concise presentation. A submission manuscript should also target the venue's usable page budget: too short is a writing failure, not just a harmless demo choice; too long triggers compression. Do not use reference papers to copy wording, claims, examples, technical content, or distinctive phrasing.

The visible output should feel like useful writing, not a process report. Use planning tables and checklists internally; show them only when the user asks for planning, audit status, or rationale.

## Format And Output Policy

1. For polishing, rewriting, line editing, or compression of existing text, preserve the original format unless the user asks to restructure it. Keep LaTeX commands, section headings, citation keys, labels, equations, figure/table environments, Markdown headings, lists, and table shape intact whenever possible. Return the revised text in the same format first.
2. For one paragraph or one subsection, default to a direct improved version plus a short optional note only if a claim, number, citation, or meaning changed.
3. For a rough idea or "write from scratch" request, create the requested artifact rather than stopping at a plan. If the user asks for a paper/manuscript and names a target venue, read `references/venue-guides/index.md` and the specific venue guide, then draft in that venue's LaTeX style. Establish a page/word budget from the venue guide and `references/length-budget-policy.md`; if the venue is absent or no venue is provided, use the NeurIPS guide and `ccf-latex-templates/NeurIPS/neurips_2026.tex` as the fallback and label the assumption.
4. If the user requests Markdown, Chinese prose, English prose, an outline, a full LaTeX file, a diff-style rewrite, or a section-only output, follow that request. Do not force the default CCF paper storyline order when the user's format is intentional.
5. Be flexible outside review tasks. When a choice could improve the paper but changes direction, present it as a concise question or option, for example: "可以把贡献改成 benchmark 视角吗？这会降低方法新颖性风险，但需要补数据集定位。"
6. Never invent results, baselines, experiments, reviewer impact, or missing evidence. Obtain correct citations through literature search per step5; never guess a bib entry. When evidence is absent, use `TBD`, a cautious placeholder, or a clearly marked "needs evidence" sentence.
7. Do not block drafting because current venue policy is not freshly verified. Use the local venue guide for draft shape, add a freshness note when relevant, and route final compliance to `ccf-submission-checker`.
8. For full-paper requests, produce a full manuscript-level artifact: Abstract, Introduction, Background/Related Work or Preliminaries, Method, Experiments, Analysis/Ablation, Limitations, Ethics/Reproducibility when relevant, Conclusion, References, and Appendix/checklist placeholders if expected by the venue. Aim for the target venue's draft page budget, usually 85-100% of the main-body limit for submission-style drafts. Do not answer a full-paper request with only an abstract, outline, or short demo snippet.
9. If the manuscript is materially under target, expand before calling it complete. Expand with mechanism detail, related-work structure, experiment setup, analysis scaffolds, limitations, reproducibility notes, and `TBD` evidence placeholders; do not pad or invent evidence. If it is over target, use local compression mode and `references/compression-rules.md`.
10. Keep outputs information-dense. Avoid boilerplate disclaimers and empty headings; each visible section should contain concrete paper content, evidence status, or actionable revision information.

## Modes

- `draft`: create or revise paper sections.
- `polish`: improve clarity, flow, terminology, and claim-evidence presentation.
- `compress`: shorten text to word/page limits using `references/compression-rules.md` without changing claims or numbers.
- `presentation`: convert a completed or near-completed paper into slides, poster, talk script, figure narration, and Q&A, without replacing submission review.

## Workflow

1. Identify mode, requested output format, target venue, paper type, draft state, available evidence, target length/page budget, and whether idea-scope changes are authorized. Load `references/output-style-policy.md` whenever output format, source-format preservation, or from-scratch LaTeX drafting matters.
2. If the user supplied existing text, preserve its format and revise in place unless the user asked for a new structure.
3. **Select venue and exemplars.** If the user names a target venue (e.g., "投CVPR", "for NeurIPS"): load the venue guide from `references/venue-guides/index.md` and the matched exemplar cards from `references/exemplars/index.md`. If no venue is specified, load `references/custom-format/default-user-format.md` which selects the user custom exemplars. If neither venue nor custom exemplars exist, use NeurIPS as the LaTeX fallback and the most relevant general-purpose exemplars. Then load `references/length-budget-policy.md` and create a section-level length plan. A short seed idea must still become a full submission-shaped manuscript; do not produce a short article because the input was short. Target85--100% of the venue main-body page budget.
4. Build or update the global story with `references/storyline-blueprint.md`: task -> gap -> root challenge -> insight -> method -> evidence -> limitation. Keep this internal unless the user asked for a plan.
5. **Prepare citations** (mandatory for full manuscripts and section drafts): load `references/citation-workflow.md`. Identify citation slots by section, search for literature for each slot, obtain correct bib entries, save them to the project `.bib` file, and insert cites naturally per the workflow. Do not draft a section without first identifying what it needs to cite. If the closest-competitor literature is unknown, hand off to `ccf-literature-searcher` before continuing.
6. For full-paper, abstract, introduction, method, experiment, conclusion, or exemplar-pattern tasks, load `references/research-writing-patterns.md` and then draft or revise section by section using `references/section-modules.md` and `references/writing-checklists.md`. For full manuscripts, compare the draft against the length budget and expand or compress as needed.
7. **Compile and check** (mandatory for full manuscripts when a LaTeX engine is available): compile the draft, measure the actual page count, and compare against the venue budget from step3. If under target by >15%, expand with mechanism detail, experiment setup, analysis, limitations, and `TBD` placeholders---not padding or invented results. If over target by >10%, compress with `references/compression-rules.md`. Recompile after any substantial change and repeat until the page count is within tolerance. Record the final status: `underfilled / target-fit / draft-over / final-over / not compiled`.
8. For compression, load `references/compression-rules.md`; return compressed text in the same format and include a cut log only when requested or when content was materially removed.
9. For presentation adaptation, derive slides/poster/talk/Q&A only from the manuscript and supplied evidence, in the user's requested slide/poster/script format.
10. If current literature, baselines, or experiments are missing, ask a targeted question or hand off to `ccf-literature-searcher` or `ccf-experiment-designer`; do not fill gaps by invention.
11. Before calling text ready, run a local score-risk check and, when needed, hand off to `ccf-paper-reviewer`.

## Post-Writing Coordination

After producing a complete manuscript, always inform the user which CCFA skills are available for the next stage. Do not silently stop.

State concisely what was produced and which skills can pick up from here:

``text
Next CCFA skills available:
- ccf-paper-reviewer: scientific review, score prediction, reviewer simulation, venue-fit check
- ccf-integrity-auditor: citation existence, claim-evidence consistency, bibtex correctness
- ccf-submission-checker: venue template compliance, page/anonymity limits, LaTeX compilation
- ccf-experiment-designer: missing experiments, baseline design, ablation planning
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
- `references/storyline-blueprint.md`: whole-paper story.
- `references/section-modules.md`: section drafting.
- `references/writing-checklists.md`: readiness checks.
- `references/score-lifting-loop.md`: score-risk improvement loop.
- `references/expert-review-loop.md`: reviewer-style self-check.
- `references/compression-rules.md`: page/word compression.
- `references/table-style-guide.md`: LaTeX table beautification: booktabs rules, number precision, narrow-column fixes, caption style, and placement.
- `references/exemplars/`: style-move references; never copy content.
