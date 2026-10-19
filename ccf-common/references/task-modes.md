# CCFA Task Modes

Use this file to decide how much checklist and audit work a CCFA skill should run for the current request.

Personal enhancement choices follow `preferences.md` and are resolved once by Common. They govern extra independent passes, broader retrieval, enhanced parsing, alternative figures, optional process detail, bounded route comparisons, and maintenance-only candidate revisions. They do not downgrade requested coverage or change task/handoff modes. Apply the task's explicit instructions before saved preferences; avoid re-asking or re-reading settings at every transition.

## Mode Values

**exploratory** is for research direction discovery and hypothesis development:

- finding possible directions from a broad topic,
- shaping a weak or vague seed before it is ready to score,
- literature scouting for opportunity maps rather than final novelty gates,
- comparing possible problem framings without making an investment decision,
- asking "这个方向还能怎么做", "有没有可救路线", "找两个方向", "先别否定，帮我发散".

Run enough checks to avoid fabrication and obvious dead ends, but do not apply submission-ready review gates as visible verdicts. The output should preserve optionality: candidate reframings, nearest prior-art risks, open gaps, minimum viable research questions, and the next evidence needed to decide. Use `low confidence` or `needs-search` for uncertainty; do not convert uncertainty into rejection.

**standard** is the default for substantial work:

- whole-paper planning, review, or rewriting,
- complete content-first manuscript drafting, followed by page/word fitting when requested,
- grounding a selected idea into a complete research plan, or a requested idea assessment,
- literature search that informs novelty, Related Work, Introduction, or experiment design,
- full experiment design,
- full-section or paper-length compression,
- rebuttal plans, TeX files, or multi-reviewer responses,
- substantial multi-deliverable workflows; a small artifact remains quick even if another skill will later read it.

Complete the checks applicable to the requested deliverable and its evidence stage. A reference template is not a requirement to run every research stage or fill every optional field. Surface an omitted check only when the user asked for an audit or it materially limits the judgment.

**quick** is for narrow local work:

- one paragraph or one small subsection polish,
- one local compression pass,
- a small literature sanity scan,
- one experiment-table sketch,
- a quick idea-risk note,
- a short reviewer-risk note.

Quick mode runs the relevant local checks and prerequisites rather than the full checklist. Necessary evidence does not become optional to save tokens; reuse it or resolve the missing dependency. Idea and manuscript reviewers select detailed/brief presentation through their report templates: narrow scope alone does not request brevity. For other skills, keep quick output short. Use a compact status only when it helps the user understand risk:

```text
Mode: quick
Local checks: venue/style, factual preservation, claim-evidence, no invented evidence
Skipped standard checks: full paper storyline, full reviewer simulation, full source audit
Unresolved:
```

## Mode Selection

1. Use exploratory mode when the requested work opens the hypothesis space: brainstorming, direction discovery, ambitious reframing, or rescue requiring a different mechanism. Targeted development of a chosen route uses quick or standard depth as appropriate. A complete development task can contain an exploratory phase before convergence; neither phase reduces requested coverage. A rough input does not override a request for judgment; idea assessment belongs to the reviewer even without scores.
2. If the user explicitly asks for quick or narrow work, preserve that scope. Do the relevant accuracy checks; name a material coverage limit instead of silently escalating to full review.
3. Use standard depth for full assessment, final artifacts, submission readiness, or checklist audits. Full brainstorming still uses exploratory reasoning and completes the requested breadth; the word "full" does not impose submission gates on discovery. Creating a small reusable file alone does not require the full workflow.
4. If the user gives only one paragraph for polishing, default to quick mode.
5. If the user gives a full section, manuscript, review set, literature search, or experiment plan, default to standard mode, except early idea/literature scouting should stay exploratory until the user asks for a hard decision.
6. Safety rules never become quick or exploratory: do not invent evidence or results, do not expose private text in searches without authorization, preserve idea scope unless authorized, and apply source-quality exclusions in literature search.

## Exploration And Convergence

Choose by the active deliverable, without another intake or preference switch. When the user seeks a breakthrough, compare mechanisms that change a causal assumption or make different predictions; several renamed module combinations do not provide diversity. A plausible new hypothesis may precede direct evidence, with its premise and uncertainty explicit. Requested brainstorming is core work even when `alternative_routes` is off.

When executing a selected plan, writing supported prose, or applying a local repair, preserve the agreed scientific content. Reopen only the affected design decision when contrary evidence, a failed assumption, an unresolved material limitation, or an explicit innovation request makes exploration useful. A new thought does not reopen every finished stage. Local aesthetic or wording alternatives remain ordinary work within their brief.

Converge when the requested options or artifact are complete and further work would not change the decision. For stagnation, use the progress test in [continuity.md](continuity.md): change the relevant hypothesis/input or identify the missing discriminator instead of repeating the same search, critique, or rewrite. A recovery state returns to the task's prior exploratory or execution phase; it does not permanently select the safest idea.

## Output Flexibility

Use functional naming for CCFA method and feature introductions, report names, and invocation prompts. Keep competing-product style claims out of those descriptions. Preserve source attribution, acknowledgments, quotations, reference examples, and license notices in their appropriate sections.

For non-review skills, the user's requested output shape wins over the skill's default report shape. If the user asks for LaTeX, Markdown, a table, a direct rewrite, a short answer, a file, Chinese prose, English prose, or a specific section structure, produce that format first and put internal checks behind it.

Review-related skills use structured evidence, scoring, and traceable criticism when applicable, while honoring an explicit user schema or concise requested format. `ccf-paper-reviewer`, `ccf-idea-reviewer`, and integrity/submission gate checks should remain more structured than writing, search, planning, or experiment-design outputs.

For `ccf-idea-reviewer`, separate concept quality, development potential, and confidence. Experimental completion and publication readiness are outside default concept review; do not require experimental material or penalize its absence. Assess experiments or execution feasibility only as a requested extension. Consider a concrete rescue when it can preserve meaningful value. A demonstrated hard-constraint violation, contradiction, or duplication with no remaining contribution may justify abandoning that candidate directly; explain the basis without abandoning the user's broader research objective.

For broad requests such as "完整流程", "完整文章", "详细报告", "用所有 skills", "full paper", "full review", or "closed loop", do not return fragments. Produce complete artifacts with enough concrete content to be useful: full drafts rather than abstract-only samples, filled tables rather than headings only, reviewer comments with evidence rather than generic risks, and handoff packets that name files, claims, blockers, and next actions.

For new manuscripts, distinguish content completion from submission fit. Draft full scientific explanations without a page quota, check global alignment, then fit length when the user requests compression, a fixed length, or a submission-ready deliverable. Naming a venue alone does not trigger early compression. Results-pending drafts are valid requested artifacts: complete supplied non-result content and authorized table scaffolds, or leave experiments blank when explicitly requested; never invent values or empirical conclusions. `ccf-paper-writer/references/materials-to-manuscript.md` owns this workflow. Final fitting uses the actual venue/year/track rules. Page occupancy never justifies padding, invented details, or an unbounded compile loop.

For editing, polishing, compression, and local revision, preserve the user's existing format and markup unless the user explicitly asks for restructuring. Do not convert LaTeX into a checklist report, Markdown into a different outline, or a paragraph into a table just because the skill has a template.

When a non-review task is under-specified, proceed with reasonable assumptions and ask at most a small number of targeted questions as optional suggestions. Do not block ordinary writing or planning work merely because a full checklist cannot be completed.

## Information Density

Visible output should maximize useful information and minimize boilerplate. Avoid long disclaimers, repeated "what this is not" lists, vague praise, generic next steps, and empty section headings. Every paragraph, bullet, or table row should contain at least one of: a concrete claim, a specific edit, an evidence link, a named artifact, a decision, a blocker, a quantified value, or an actionable question.

## Output Quality Gate

Before returning a visible artifact, every CCFA skill should do one quick self-read:

1. The answer follows the requested or promised output format.
2. Headings, bullets, and tables are complete and in a logical order.
3. Review and audit outputs include concrete evidence, severity, score or pass/fail status, and action conditions where applicable.
4. Writing outputs preserve the user's source format unless restructuring was requested.
5. Chinese and English punctuation are used consistently; mixed punctuation is allowed only when required by code, LaTeX, citations, or filenames.
6. The argument flow is clear: problem -> reason -> consequence -> action, or scientific question -> mechanism or observation -> supported interpretation.
7. No generic filler remains where a concrete location, artifact, or action is required.

## Minimal Status

Every CCFA skill may include mode in final output when checklist strictness affects reliability:

```text
Mode:
Checks run:
Checks skipped:
Unresolved risks:
```

## Execution And Context

Keep the active goal, requested artifacts, authorization, evidence locations, completed work, and next action available across long tasks. New user messages usually steer the active task: apply explicit goal changes, update affected requirements, preserve valid completed work, answer a side question briefly, and resume. Use [continuity.md](continuity.md) for material rerouting or lost/conflicting context. Its normal/focused/reconciling execution states do not change task depth or requested coverage; a short task needs no continuity file.

Before the owner's work, read and apply `ccf-humanization` then `ccf-common`; these preflights apply in quick, exploratory, and standard modes. Reuse applicable active rules across contributors rather than rerunning complete workflows. Then load the owner's entry and only relevant reference sections. A reference list is navigation, not a read-all checklist. Reload changed or lost rules after compaction. Read located source ranges before a whole extraction or library; full scientific review and complete exemplar analysis still require coverage of the relevant full source in coherent sections.

Use one representation of each fact: a source table, current specification, or existing report. Link to it in downstream work instead of copying full abstracts, tool logs, manuscript passages, and prior reports into every handoff. Give tools the smallest sufficient input and request targeted output; show counts, relevant rows, errors, and locations before raw dumps. Do not truncate evidence needed to assess a claim or silently lower requested coverage.

Reuse already discovered tools. Use the host's selective tool discovery for a large unknown tool surface when it is available; invoke a small known tool set directly. Do not create another discovery agent, wrapper, or mandatory integration merely to follow this rule. Request only needed metadata fields, keep actionable diagnostics with source locations, and retain full logs in the existing build directory only when needed for troubleshooting or reproducibility.

For cross-skill work, use `routing.md` for prerequisite selection and `handoff-modes.md` for evidence transfer and integration. Keep the goal, prerequisite status, and working paths; pass the concrete question, relevant evidence, and completion condition. A quick helper lookup does not reduce a full review's coverage, and a bounded contribution needs no standalone full report. Reduce duplicate retrieval, repeated intake, irrelevant references, and unused reports before reducing evidence coverage. Do not optimize for the fewest skill calls: a contribution is worthwhile when it can resolve a material gap or improve the requested result.

For a revision, inspect the changed passage, panel, data series, or issue plus its affected dependencies. Reuse unchanged source verification, chart layout, bibliography, and established scientific context. Broaden the check when a changed premise affects the whole artifact. A new source version or changed evidence invalidates dependent conclusions; a color or spelling edit does not.

When durable context is needed, reuse an authorized report/state before creating the optional compact continuity record. After compaction, reconcile the current goal and affected actual artifacts; distinguish proposed, executed, and verified work. Do not re-extract or rescore unchanged inputs by default. Keep generated files under `artifact-contracts.md`; token reduction must not create a second uncontrolled set of context files. Return file links and a concise change report when files are the deliverable, unless the user also requests the full content in the conversation.

Batch independent read-only searches and checks when the host supports it. For actual subagents, apply [delegation and integration](handoff-modes.md#actual-multi-agent-execution): split by evidence dependencies, preserve one integrating owner, and keep shared-file writes sequential. Skill loading or single-pass role perspectives do not create independent agents. Small local edits need no delegation.

Validate the requested outcome and changed paths. After relevant checks pass, repeat them only for a new change, failure, or unresolved concern. A missing tool limits the dependent verification, not unrelated authorized work. Distinguish not checked from failed. Do not fabricate verification or claim a running background task unless a real scheduler or job exists.

## GPT-6 Adaptation

The GPT-6 Astra guidance consulted on 2026-09-05 emphasizes authorization-aware follow-through, clear skill priority, explicit delegation conditions, direct writing, and proportionate verification. These execution rules remain portable to other supported agents. Keep model choice and reasoning effort in the host; compare effort on representative tasks rather than pinning every skill to a maximum. Skills do not enable API async execution, caching, compaction, or mid-turn steering by declaring them in Markdown. Use only capabilities actually exposed by the host. Official provenance is recorded with the skill-authoring sources in `source-registry.yaml`.
