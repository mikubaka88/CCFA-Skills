---
name: ccf-rebuttal-writer
description: "Write CCF rebuttals, author responses, revision ledgers, response letters, and conservative resubmission plans. Use for 审稿意见回复, rebuttal, revision ledger, and 重投迁移. Ground promises in feasible changes and actual evidence. Ordinary manuscript writing has a separate owner."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Rebuttal Writer

## Family File Contract

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

## Core Rule

Handle post-review communication and revision accountability. Responses must be calm, factual, evidence-grounded, and promise only feasible changes. Resubmission adaptation is conservative by default: no new experiments and no bibliography changes unless the user explicitly authorizes them. Follow the user's requested response format: plain text, TeX, reviewer-by-reviewer, issue-grouped, table-first, or short response.

## Modes

- `rebuttal`: reviewer/AC response under a word or time budget.
- `revision-ledger`: reviewer comment -> action -> manuscript location -> owner -> status.
- `response-letter`: revision summary or camera-ready response letter.
- `resubmission`: adapt an already written paper to a new venue with conservative defaults.

## Workflow

1. Identify venue, response format, word budget, deadline, review scores/confidence, and whether this is rebuttal, revision, or resubmission.
2. Parse comments into issue groups by reviewer, concern type, severity, available evidence, response strategy, and promised paper change.
3. Load `references/response-strategy.md` for substantial responses and apply `../ccf-paper-writer/references/prose-quality-guardrails.md`; answer actual high-impact concerns first: soundness, novelty, missing evidence, incorrect assumptions, and shared concerns.
4. Load `references/revision-ledger.md` whenever promised edits, manuscript locations, resubmission actions, review rounds, or cross-version score changes must be tracked. Update one canonical ledger in place; do not create a separate ledger per round unless the user requests snapshots.
5. For full rebuttals, load `references/tex-templates.md` and use the TeX templates in `assets/templates/` when useful.
6. For resubmission, map old reviewer concerns to the new venue's constraints through `ccf-submission-checker`; do not silently add experiments or bibliography changes.
7. Complete necessary contributions through their owners: paper writer for requested revisions, experiment designer for authorized evidence work, and submission checker for applicable venue/package rules. Use integrity auditor for unresolved claim/result conflicts and reviewer for a consequential unanswered criticism. Integrate returned evidence and verify actual changes before claiming completion in the response; a planned experiment or promised edit remains planned.

## Adaptive Output Contract

Put the requested response artifact first. For "write rebuttal", output the rebuttal text or TeX first. For "make a ledger", output the ledger first. Use the full structure below for standard multi-reviewer response planning or when the user asks for strategy plus draft:

```text
Mode:
Venue and constraints:
Issue table:
Response strategy:
Draft response or response file:
Promised paper changes:
Revision ledger:
Resubmission adaptation notes:
Claims/promises to avoid:
Next CCFA owner:
Checklist status:
```

## References

- `references/response-strategy.md`: response tactics.
- `references/response-checklists.md`: tone, evidence, promises, and word-budget checks.
- `../ccf-paper-writer/references/prose-quality-guardrails.md`: concise, non-defensive response prose and anti-pattern checks.
- `references/tex-templates.md`: reusable TeX response templates.
- `references/revision-ledger.md`: tracking reviewer comments and manuscript actions.
- `../ccf-paper-reviewer/references/version-comparison.md`: frozen scoring contract and issue provenance for cross-version review; rebuttal prose must not redefine that contract.

## Authorized Response Work

Follow `../ccf-common/references/handoff-modes.md` and `../ccf-common/references/task-modes.md`. A requested response plus revision authorizes both deliverables through their owners. Group duplicate comments while preserving reviewer attribution and answer coverage. Distinguish supplied results, planned experiments, promised revisions, and completed edits; verify an edit's location before claiming it was made. Preserve word budgets and respond to actual concerns without gratuitous apologies, imagined objections, or defensive repetition. A concise factual clarification is not a scientific concession. Reply drafting does not authorize posting or submission.
