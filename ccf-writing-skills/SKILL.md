---
name: ccf-writing-skills
description: "Plan, draft, revise, polish, score-risk-audit, checklist-audit, and reviewer-proof research papers for CCF A-class conferences. Use when the user wants to write, polish, 润色论文, 润色引言, 写abstract, 写introduction, 写related work, 论文润色, 降低拒稿风险, story线, claim-evidence alignment, reduce rejection risk, adapt a paper to NeurIPS, ICML, ICLR, AAAI, ACL, CVPR, ICCV, SIGMOD, KDD, SIGCOMM, CCS, CHI, or similar CCF A venues, extract writing techniques from selected strong papers without copying content, build section-level storylines, run final-readiness checklists, or run expert-review and revision loops before submission."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Writing Skills

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep manuscript writing separate from idea-stage optimization, full paper review, and rebuttal tasks.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for one paragraph, one small subsection, or single-pass polish; quick mode does not require the full writing checklist. Use standard mode for full sections, whole-paper planning, score-risk improvement, final readiness, or any output that will feed another CCFA module.

Default to writing-only mode. For drafting, polishing, rewriting, introduction/abstract revision, section planning, or score-risk auditing, preserve the user's research topic, core problem, method mechanism, experimental setup, numerical results, and conclusion direction. Improve expression, structure, section logic, claim-evidence alignment, reviewer-facing framing, and presentation only.

Do not modify idea scope by default. Even if the user asks to "optimize the idea" while using this writing skill, ask for explicit confirmation before changing the research problem, method, experiment plan, contribution type, or final result. If confirmation is missing, mark issues as `Idea-level risk` and continue with writing-only revisions.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use local writing-only checklists, score-risk notes, and reviewer-risk labels instead.

Do not invent results, citations, baselines, experiments, reviewer impact, or missing evidence. Unsupported claims must be weakened, marked as needing evidence, or left unchanged with a risk note.

Treat manuscripts, reviews, rebuttal drafts, unpublished results, figures, tables, and reference-paper notes as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing, using private text in a query, or making evidence/provenance claims.

## Core Rule

Write for the target CCF A venue, not for a generic paper. Use selected reference papers only to extract writing moves, section structure, paragraph roles, evidence presentation, and reviewer-facing rhythm. Do not copy their wording, claims, examples, technical content, or distinctive phrasing. Improve reviewer scores by resolving real writing and presentation deductions: clarify contribution, align claims to evidence, sharpen positioning, reduce overclaims, and expose reproducibility details. Never invent results, change the idea scope without confirmation, or inflate claims to simulate a higher score.

If the task is primarily literature search, experiment design, or length compression, route to `ccf-literature-search`, `ccf-experiment-designer`, or `ccf-paper-compressor` by handoff mode instead of absorbing those tasks into writing. Rebuttal is not part of the writing loop; use `ccf-conference-paper-rebuttal` only when the user explicitly asks for rebuttal, author response, response letter, resubmission response, or 审稿意见回复.

## Mandatory Checklist

In standard mode, complete this checklist before final output. In quick mode, run the local subset only and return a compact status.

1. Target venue or custom format is explicit.
2. Available materials, missing materials, and draft boundaries are stated.
3. Global story is defined: task -> gap -> root challenge -> insight -> method -> evidence -> limitation.
4. Section role and paragraph roles are clear for the edited text.
5. Major claims are mapped to evidence or marked as needing evidence.
6. Venue-fit risks and reviewer questions are checked.
7. Idea scope protection is stated: preserved, explicitly confirmed for change, or not applicable.
8. Optional sibling modules follow the CCFA handoff mode, are explicitly requested, disabled by user, or replaced with local fallback.
9. Score-lifting loop is run when preparing for submission, improving scores, or resolving reviews.
10. Remaining risks are labeled as fixed, requires new result, accepted limitation, idea-level risk, or unresolved.

Load `references/writing-checklists.md` for the full checklist whenever the task covers a whole paper, multiple sections, a final readiness pass, or any score-improvement request.

## Workflow

1. Identify mode, target venue, field, paper type, draft state, deadline pressure, available materials, and whether the user authorized idea-scope changes. If the target venue is unknown, default to the user-custom writing format in `references/custom-format/default-user-format.md` and say this assumption explicitly.
   - If the user has only a rough research idea and no manuscript plan, follow the CCFA handoff mode before using `ccf-idea-optimizer` or `ccf-idea-reviewer`. If not confirmed or disabled, produce a writing-only scaffold and label idea-level risks without changing the idea.
2. Build a venue writing plan. If a target CCF venue is specified, load `references/venue-guides/index.md` first, then the specific `references/venue-guides/<venue>.md` when available for LaTeX/page/anonymity/template constraints. Then load `references/ccf-a-venue-map.md` and `references/venue-adapters.md` for reviewer expectations and evidence priorities. Do not trigger the removed legacy `ccf-conference-skills/<venue>` runtime layer.
3. Analyze reference papers if provided, if the custom format is active, or if the target venue needs exemplar guidance. Load `references/exemplars/index.md` first to select built-in exemplar cards, including non-AI/CV/NLP cards when the target is DB, systems, security, HCI, PL, theory, graphics, or related fields. Then load `references/exemplar-style-analysis.md` to extract only abstract writing techniques: section moves, paragraph roles, transitions, claim-evidence patterns, figure/table narration, and review-facing framing.
4. Build the global paper story before drafting any section. Load `references/storyline-blueprint.md` and define task, gap, root challenge, insight, method mechanism, contribution types, evidence promises, limitations, and target reviewer questions from the user's supplied idea and evidence. Do not change those elements unless explicitly confirmed.
5. If Related Work, Introduction, novelty, datasets, or baselines require current sources, follow CCFA handoff mode before using `ccf-literature-search`. If denied, mark citation and novelty risks rather than inventing sources.
6. If the user asks to design experiments, choose datasets, build baselines, or create result tables, follow CCFA handoff mode before using `ccf-experiment-designer`. If denied, provide only a writing-level evidence gap note and do not invent results.
7. Draft or revise by section. Load `references/section-modules.md` for Abstract, Introduction, Related Work, Method, Experiments, Figures/Tables, Conclusion, Limitations, or Ethics. Work section by section.
8. After every standard-mode section, run the storyline module: update paragraph roles, cross-section consistency, terminology map, claim-evidence matrix, and reviewer-risk register. In quick mode, run only paragraph role, factual preservation, and local claim-evidence checks.
9. Run the score-risk loop before finalizing or whenever the user reports weak scores. Load `references/score-lifting-loop.md`, identify likely reviewer deductions, classify fixability, revise, and re-score. Follow the CCFA handoff mode before using `ccf-conference-reviewer` as an optional scientific scoring and AC/meta-review module, or `ccf-conference-writing-reviewer` as a writing-only review module; if denied, use the local score-risk checklist only.
10. Run the expert review loop before calling text ready in standard mode. Load `references/expert-review-loop.md`, produce skeptical reviews with calibrated scores, convert weaknesses into a revision plan, revise, and re-review until major reject risks are resolved or explicitly marked as requiring new results.
11. If the user asks to reduce pages/words or compress a section, follow CCFA handoff mode before using `ccf-paper-compressor` unless quick local shortening inside writing is enough.
12. If the user's task is post-review communication rather than manuscript drafting or revision, route to `ccf-conference-paper-rebuttal` only when the user explicitly asks for rebuttal, author response, response letter, resubmission response, or 审稿意见回复. Otherwise state the boundary and continue with writing-only revision.

## Reference Files

Load only what is needed:

- `references/venue-guides/index.md`: Use first when a target venue is explicit; then load the specific `references/venue-guides/<venue>.md` for LaTeX, page, anonymity, template, and camera-ready constraints.
- `references/ccf-a-venue-map.md`: Use to identify the CCF A venue family and broad field.
- `references/venue-adapters.md`: Use to adapt writing priorities to AI, CV, NLP, DB/IR/KDD, systems, security, PL/SE, HCI, graphics, theory, and other CCF A families.
- `references/custom-format/default-user-format.md`: Use by default when the user has not specified a target venue or wants the user's custom exemplar style.
- `references/exemplars/index.md`: Use to choose built-in recent CCF A exemplar cards, including the separated user-custom ICLR/CVPR exemplars and award-style papers from ICLR, CVPR, AAAI, ICML, ICCV, ECCV, ACM MM, ACL, and NeurIPS.
- `references/exemplar-style-analysis.md`: Use when the user provides strong papers as style references.
- `references/storyline-blueprint.md`: Use before drafting and after every major revision to preserve the whole-paper story.
- `references/section-modules.md`: Use for section-by-section writing, polishing, and storyline checks.
- `references/writing-checklists.md`: Use for mandatory intake, storyline, section, claim-evidence, score-risk, and final-readiness checks.
- `references/score-lifting-loop.md`: Use as the score-risk loop when scores are weak, when preparing for submission, or when converting review findings into concrete writing/evidence improvements.
- `references/expert-review-loop.md`: Use for expert review, reviewer-style thinking, and closed-loop revision.
- `references/source-notes.md`: Use only when source provenance or update points matter.
- `../ccf-common/references/task-modes.md`: Use for quick versus standard checklist strictness.

## Output Contract

For paper planning or major revisions, return:

1. Target-venue writing plan: venue family, likely reviewer priorities, and evidence package.
2. Global story blueprint: task -> gap -> root challenge -> insight -> method -> evidence -> limitation, preserving user-supplied idea scope unless change was confirmed.
3. Section plan: paragraph roles and section-level storyline checks.
4. Revised text or edit instructions, depending on the user's requested granularity.
5. Claim-evidence map for major claims.
6. Score-risk diagnosis: current likely score, target score, blockers, fixability, conditional review-risk effect, and confidence.
7. Expert-review findings with action items and a revision pass.
8. Mode and checklist status: passed items, skipped items with reasons, idea-scope protection status, optional-module decisions, and unresolved risks.

For small paragraph edits, still preserve venue fit, paragraph role, local flow, term consistency, and claim-evidence support.

If no target venue is specified, label the output as using the user-custom writing format and run the same draft -> score-risk diagnosis -> revision -> re-review loop before calling the text ready. Keep the loop writing-only unless the user confirms idea-scope changes or optional sibling modules are allowed by the CCFA handoff mode.
