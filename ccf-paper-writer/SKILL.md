---
name: ccf-paper-writer
description: "Draft, revise, polish, compress, or presentation-adapt CCF manuscript prose. Use for 写作, 润色论文, research documents to complete papers, 完整初稿, 实验留空, 改写, 压缩论文, abstracts, sections, and slides. Draft content before fitting pages; preserve evidence and format. Assessment without rewriting belongs to ccf-paper-reviewer; rebuttal belongs to ccf-rebuttal-writer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Writer

## Preflight And Ownership

Apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md); reuse applicable active rules at handoffs. Both preflights remain required in every mode. Handoff mode is **PARTIAL**, under the preserved metadata and Common's [handoff rules](../ccf-common/references/handoff-modes.md).

Own manuscript prose, compression, and presentation text. Assessment without rewriting belongs to `ccf-paper-reviewer`; rebuttal belongs to `ccf-rebuttal-writer`. Preserve the supplied problem, mechanism, setting, measurements, citation keys, and conclusion unless research changes are authorized. Respect the user's format, markup, boundaries, no-browsing and no-new-files instructions. An inspection request alone does not authorize rewriting.

For file edits, reuse the canonical source and one stable working directory under [artifact-contracts.md](../ccf-common/references/artifact-contracts.md), default `ccfa-workfiles/<purpose>/<artifact-id>/`. Update in place; preserve inputs, includes, labels, citations, equations, and floats. Check UTF-8/Chinese text and requested exports. Do not create dated or `v2` manuscript copies for ordinary iterations.

## Writing Standard

Compose from the supplied scientific propositions and the reader's path through them. Develop computations, distinctions, implications, or interpretations according to the passage's purpose. Connect sentences through their actual reason, consequence, evidence, or comparison; internal readiness checks and imagined reviewer objections are not the narrative. Preserve necessary uncertainty, assumptions, negative findings, technical terms, and the author's sentence-final emphasis and broader significance. Do not invent mechanisms, citations, measurements, or empirical superiority.

Before polishing wording, recover the paragraph's main scientific point and how its sentences develop it. Compose in ordinary field language at the passage's level of abstraction; internal claim/support labels are not a default paper vocabulary. Preserve the author's strongest supported position and sentence-final significance. An ordinary clear local edit needs the active baseline, actual text, and relevant constraints. Read [humanization-policy.md](../ccf-humanization/references/humanization-policy.md) or [prose-quality-guardrails.md](references/prose-quality-guardrails.md) for an actual expression/logic problem or requested humanization; load the relevant sections rather than both full guides by default. Punctuation thresholds belong to Humanization. Supporting phrase checks never replace semantic reading or require removing correct technical language.

## Mode Navigation

| Requested work | Relevant guidance |
| --- | --- |
| `polish`: local passage | Revise directly in the source format; load a reference only for a specific factual, citation, logic, or style question. |
| `draft`: section | Relevant [section module](references/section-modules.md); [storyline-blueprint.md](references/storyline-blueprint.md) for substantial introduction/global argument work. |
| `draft`: complete manuscript | [materials-to-manuscript.md](references/materials-to-manuscript.md), storyline and relevant section/checklist guidance. Complete substantive explanations before length fitting; results-pending drafts remain valid. |
| `submission-fit` | The aligned content first, then target venue guide, [length-budget-policy.md](references/length-budget-policy.md) and [compression-rules.md](references/compression-rules.md); verify exact official year/track rules through `ccf-submission-checker`. |
| `compress` | [compression-rules.md](references/compression-rules.md); preserve scientific relationships, facts and numbers. |
| `presentation` | The source paper and presentation guidance in [section-modules.md](references/section-modules.md). |

Naming a venue alone does not trigger a page quota. Read `references/venue-guides/index.md` and the matched guide when audience/format affects the work; [output-style-policy.md](references/output-style-policy.md) preserves supplied templates and governs the disclosed NeurIPS fallback for new LaTeX without one. An abstract, caption, local edit, or exact JSON response does not require whole-paper planning, exemplar analysis, reviewer panels, or a venue guide.

For substantive drafting or expression rewriting, inspect relevant real passages through [exemplar-style-analysis.md](references/exemplar-style-analysis.md). `reference_style_search` defaults to **on**: reuse matched originals and search for additional good writing for the actual question, reusing completed applicable searches across paragraphs. `auto` limits extra discovery to gaps; `off` skips unrequested extra discovery, not supplied references or explicit searches. Choose quality and function without a paper-count quota. Reuse conventional language and technical terms, not distinctive source sentences or scientific claims; keep one author voice.

## Draft, Check, Deliver

1. Recover the requested artifact, evidence, argument and routine choices from existing context. Ask only for a missing decision that changes the science or deliverable; continue independent work. A long coordinated revision can use [writing-execution.md](references/writing-execution.md) and `scripts/writing_runtime.py` for current targets, necessary transitions, source positions and checked patches. Short edits stay direct; section IDs do not imply separate agents.
2. Resolve support before asserting dependent facts. Use [citation-workflow.md](references/citation-workflow.md) and `ccf-literature-searcher` for missing sources; use `ccf-integrity-auditor` for unresolved support/numerical conflicts. Reuse verified evidence and preserve bibliography keys. Reported comparisons use [experiment-discipline.md](../ccf-humanization/references/experiment-discipline.md) when identity/protocol matters; drafting a supplied design requires no new runs.
3. Draft the requested prose. [materials-to-manuscript.md](references/materials-to-manuscript.md) owns conflicting-material and result-status handling: retain supplied results and honor an entirely deferred experiment section. By default, leave missing values and dependent analysis unwritten. Only an explicit task request or `results_pending_draft=on` enables its marked, conditional results-pending completion mode, including the automatic whole-draft alignment pass. Missing details constrain relevant claims without becoming repeated progress disclaimers. Use [research-writing-patterns.md](references/research-writing-patterns.md) only when alternative explanations or structure help; [table-style-guide.md](references/table-style-guide.md) covers source tables, with visual redesign owned by `ccf-visual-composer`.
4. Check the resulting argument and factual preservation once. For a full section/paper run `scripts/check_prose_quality.py` when available, inspect real issues in context, and retain justified scientific language. Use `--strict` only for requested strict lint; rerun changed/unresolved content only. Substantial argument/evidence changes need a scoped `ccf-paper-reviewer` alignment check unless covered; carry the phase and missing-result status. Such a check does not start acceptance scoring or experiments. Reuse matching completed coverage; extra independent review follows its existing switch or explicit request.
5. For full LaTeX with an available engine, compile and inspect errors, references, and affected layouts; fix overflow and broken references. Keep builds in the established task directory, preserve includes/configuration, and export PDF after success. Page count is informational during content drafting. Recompile affected changes without chasing harmless warnings or looping to fill pages.

Return the actual text/artifact first in the user's format. Ordinary local edits need no status report. For full files give paths, substantive changes, actual checks, and concrete remaining author inputs. Draft completion is distinct from evidence completeness or submission readiness. Requested reviewer-driven edits use [review-driven-revision.md](references/review-driven-revision.md), without writer-owned rescoring or promised score gains.
