---
name: ccf-literature-searcher
description: "Search and screen literature, related work, datasets, benchmarks, and citation evidence for CCF research workflows. Use for literature search, related work, prior art, benchmark search, 文献检索, 相关工作, benchmark搜索. Do not audit only already-cited references or write the manuscript as the main task."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Literature Searcher

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep literature search separate from idea optimization, manuscript writing, experiment design, paper review, and rebuttal.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for a narrow related-work scan or a small set of candidate citations. Use standard mode for Related Work, Introduction, idea novelty grounding, benchmark discovery, experiment design, or any task that will feed another CCFA module.

Treat user ideas, draft text, unpublished results, and private manuscripts as private material. Load `../ccf-common/references/privacy-and-evidence.md` before browsing. Search with public keywords, public titles, venue names, method names, public abstracts, or user-approved query text. Do not paste private draft sentences into a search query unless the user explicitly authorizes it.

Source-quality exclusion: do not search, cite, recommend, or include policy-excluded venues, journals, URLs, or PDFs. The shared policy includes MDPI sources in this exclusion set; record exclusions only in internal screening or the search-notes file.

## Core Rule

Ground novelty and positioning using high-quality, inspectable sources. Prefer influential conferences, strong journals, official proceedings pages, archival repositories, and public paper pages. Do not invent papers, citations, venues, links, acceptance status, benchmark status, or numerical results. Separate searched evidence from inference. Follow the user's requested output shape: short list, related-work clusters, BibTeX candidates, benchmark table, search folder, or handoff summary.

## Mandatory Search Checklist

In standard mode, complete this checklist before final output. In quick mode, run the relevant subset and return a compact checklist status.

1. The user's topic is converted into safe public search queries.
2. Shared source-quality exclusions are applied to search domains, candidates, and final outputs.
3. Sources prioritize primary or high-confidence venues: official proceedings, arXiv/OpenReview when appropriate, ACL Anthology, CVF, PMLR, ACM, IEEE, USENIX, DBLP, Semantic Scholar, OpenAlex, Crossref, and venue or project pages.
4. Candidate papers are deduplicated by title and linked to a stable URL.
5. Each included paper has venue/year/source status, paper type, and relevance rationale.
6. Paper quality is scored on insight, completeness, and experimental numeric evidence. Pure benchmark papers skip the numeric-results score and receive a benchmark-quality note instead.
7. Paper type is one of `pure benchmark`, `pure method`, `method + benchmark`, `survey`, `system/tool`, `theory/proof`, or `other`.
8. Every claim about a paper is traceable to the linked source or marked as inferred.
9. A literature-search folder is written when file access is available.
10. Optional handoff to `ccf-paper-writer`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-experiment-designer`, or `ccf-paper-reviewer` follows CCFA handoff mode.

## Workflow

1. Identify the search purpose: Related Work, Introduction support, novelty check, idea optimization, idea review, experiment design, benchmark/dataset discovery, or reviewer-risk diagnosis.
2. Create public queries from the user's topic. If the topic is too private or underspecified, ask only for non-sensitive keywords or infer broad keywords with lower confidence.
3. Load `references/search-and-scoring.md`. Search breadth depends on mode:
   - Quick: 6-10 screened candidates, 3-6 final papers.
   - Standard: 15-30 screened candidates, 8-15 final papers unless the user requests another size.
4. Search discovery indexes first, then verify candidates through stable paper pages or official proceedings when possible. Use broad web search only to find primary links; do not rely on snippets for final claims.
5. Filter by influence and fit. Prefer CCF-A/B conferences, top-field conferences, strong journals, widely used benchmarks, or recent high-signal preprints from credible groups. Exclude low-quality, predatory, inaccessible, or policy-excluded sources.
6. Classify each paper with the paper-type taxonomy and score it:
   - `insight`: how clear and non-obvious the central idea is.
   - `completeness`: method/evaluation/proof/dataset/reproducibility coverage.
   - `experimental numeric evidence`: strength and relevance of reported numerical evidence; mark `N/A benchmark` for pure benchmark papers.
7. Write the search folder using `references/report-template.md`. Default folder name:

```text
literature-search-YYYYMMDD-<topic-slug>/
  papers.md
  papers.csv
  search-notes.md
```

8. If the search feeds another module, provide a handoff summary:
   - For writing: closest-work groups, novelty gaps, citation cautions.
   - For idea optimization: stale/overcrowded directions, open gaps, timely pivots.
   - For idea review: novelty confidence and likely prior-art risks.
   - For experiment design: datasets, baselines, metrics, benchmark protocols.
   - For paper review: missing related work and baseline risks.

## Adaptive Output Contracts

Return the requested artifact first. If the user asks for a list of papers, output the list/table directly. If they ask for Related Work material, output clusters and positioning notes. If they ask for a folder, write the folder and summarize it. Use the following defaults for standard or quick search reports.

For standard search, return:

```text
Search purpose:
Queries used:
Source policy:
Folder written:
Top paper table:
Excluded source notes:
Closest-work clusters:
Quality-score rationale:
Benchmark/dataset candidates:
Novelty and positioning risks:
Recommended next module:
Checklist status:
```

For quick search, return:

```text
Quick search scope:
Top candidates:
High-risk missing literature:
Folder written:
Compact checklist status:
```

## Reference Files

Load only what is needed:

- `references/search-and-scoring.md`: Use for source policy, source-quality exclusions, source tiers, paper-type taxonomy, and scoring anchors.
- `references/report-template.md`: Use when writing the literature-search folder files.
