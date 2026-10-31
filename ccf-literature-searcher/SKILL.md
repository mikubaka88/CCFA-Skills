---
name: ccf-literature-searcher
description: "Find and verify external literature, prior art, datasets, benchmarks, and citation candidates. Use for 文献检索, 相关工作, benchmark搜索, and research opportunity maps. Recurring recent-paper watch belongs to ccf-literature-monitor; existing-citation audits, manuscript assessment, and result schemas have separate owners."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Literature Searcher

## Preflight And Scope

Apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md); reuse active applicable rules. Handoff mode remains **PARTIAL** under metadata and Common's [handoff rules](../ccf-common/references/handoff-modes.md). This owner finds literature, prior art, datasets, benchmarks, citation candidates and opportunity maps. Recent-paper/competitor watch belongs to `ccf-literature-monitor`; judgment, drafting and existing-citation audits retain their respective owners.

Before browsing, apply [privacy-and-evidence.md](../ccf-common/references/privacy-and-evidence.md). Convert private research into public-safe terms rather than copying draft sentences or unpublished results into queries. Preserve no-browsing and supplied-evidence-only limits. Apply shared source exclusions, including default MDPI exclusion; a named user-directed source is a scoped exception, not permission for unrelated recommendations. Keep routine screening internal.

Use Common's [task modes](../ccf-common/references/task-modes.md): exploratory for direction/opportunity scouting, quick for a small lookup, standard for substantial related-work/novelty/benchmark retrieval. A helper's scope does not become a full standalone search merely because another skill will use it. The user's requested breadth wins; planning ranges are not quotas.

## Retrieve And Verify

Read [search-and-scoring.md](references/search-and-scoring.md) for source roles, query/reuse strategy, taxonomy, relevant scoring anchors and standalone search guidance. Ground substantive claims in inspected original papers or primary artifacts. Indexes and stable landing pages establish identity; snippets, citation counts, institutional prestige and awards do not establish scientific findings. Include relevant technical reports, conference/journal papers and arXiv originals according to their content, version and status.

1. Identify the actual search question and use public-safe query clusters. Batch independent discovery and metadata lookups; request only needed fields. Resolve ambiguous identities and deduplicate by stable identifier plus normalized title before deeper reading; retain distinct versions and supplements.
2. Verify decisive method/result/overlap claims in original passages, inspecting uncertain PDF pages when necessary. Reuse current source caches and locations; an unchanged PDF does not prove that no newer version exists. Record source/version, inspected coverage, type, relevance and stable link. Inaccessible sources can remain explicit retrieval leads, not scored findings or evidence of absence.
3. Compare what closest work already establishes and the meaningful remaining difference. Keep closest comparators, mechanism-bearing inspirations and counterexamples distinct. An unsearched/crowded topic is uncertain, not automatically dead; a weak result does not erase prior existence. Do not invent a rescue module or abandon the broader user goal when one candidate is covered.
4. Score only when requested or useful and supported by inspected text. Keep insight/completeness/numerical support separate from relevance and novelty overlap; use contribution-appropriate `N/A` and `not assessed` instead of penalizing unavailable or inapplicable experiments. Benchmark papers use the reference's benchmark-quality note. No acceptance probabilities.
5. Stop when the requested questions/clusters are covered and further retrieval adds no material information; broaden for a specific remaining gap. Reuse verified work rather than searching per paragraph or filling a paper quota. Return source passages and locations separately from model interpretation.

## Deliver And Hand Off

Return the user's requested list, clusters, opportunity map, BibTeX candidates, benchmark table or compact handoff first. Include material coverage limits where they change the conclusion, without empty score/status sections. For idea development, pass source-backed observations, mechanism primitives, assumptions, relevant relations and protocol anchors; older or analogous-field work can be useful beyond recent nearest neighbors. For writing/review, pass the exact support or overlap needed and its source location, not repeated full abstracts. [search-and-scoring.md](references/search-and-scoring.md) provides the detailed handoff guidance.

Create files only for requested/necessary reusable output under [artifact-contracts.md](../ccf-common/references/artifact-contracts.md); preserve inputs, UTF-8/Chinese text and the established folder. Otherwise a helper returns evidence in context without a report. Use [report-template.md](references/report-template.md) for a new default `ccfa-workfiles/literature/<topic-slug>/`: current `papers.md`, optional structured `papers.csv`, separate notes only when needed, and `idea-grounding.md` when useful. Derive views from one screened source set, update in place, and keep dates/versions inside rather than generating iteration folders. Required prerequisite work continues through its owner under existing authorization.
