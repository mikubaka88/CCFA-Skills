# Monitoring Workflow

## 1. Setup

- Identify target categories (e.g., cs.CV, cs.CL, cs.LG, stat.ML), venues, labs, authors, repositories, datasets, benchmarks, or keyword clusters.
- Determine time range: most recent period (last 7 days, 14 days, 30 days), or since a specific date.
- If the user wants novelty check, read the current idea from `ccfa.yaml` when available. Err on the side of inclusion for potential overlap: if a new paper has a similar problem, insight, mechanism, dataset, or claim, report it with uncertainty rather than hiding it.
- If the user's idea is private, transform it into public-safe query terms before searching.

## 2. Search Strategy

- Use arXiv API, OpenReview, official venue/proceedings pages, Semantic Scholar, OpenAlex, DBLP, Crossref, and project pages according to the shared source registry.
- Fetch recent papers in target categories or from the requested venues/labs.
- For each high-relevance candidate, read at least the title and abstract. Do not claim high overlap without checking the abstract and, when accessible, the introduction or method summary.
- If the user has specific keywords, add them to the search or use them as filters after the broad search.
- Deduplicate by DOI/arXiv identity and normalized title; distinguish a new paper from a new version. Compare with prior reports when available and record the actual scanned date window.

## 3. Overlap Detection

- Compare each new paper's research question and main claims with the user's idea.
- Check six axes:
  - problem/task,
  - claimed gap,
  - core mechanism,
  - evidence type,
  - dataset/benchmark,
  - venue positioning.
- Classify each overlap:
  - **None (RELAX):** different problem, method, and evaluation; no immediate action.
  - **Low (RESEARCH):** shared motivation or setting, but different method or claim; retrieve if relevant.
  - **Medium (RESEARCH):** overlapping mechanism, benchmark, or claim; deep search and differentiation are needed.
  - **High (FOLLOW-UP):** same problem, similar method, and similar evidence path; major novelty or positioning revision may be needed.
- Assign an overlap score only as a diagnostic:

```text
Overlap score (0-5):
0 = no relation
1 = same broad area
2 = same problem or dataset
3 = same problem plus related mechanism
4 = same problem plus similar mechanism or claim
5 = same problem, mechanism, and evidence path
```

## 4. Reporting

- Use the report template from `references/report-template.md`.
- Be honest about uncertainty: report what you don't know, not what you suspect.
- Format all high-relevance papers as a table with title, source, date, overlap score, overlap type, evidence basis, and recommended action.
- Include exact date range and source basis.

## 5. Follow-up and Persistence

- Store reports only when file output is requested or necessary within the authorized workflow; honor no-new-files. Preserve dated monitoring history when it serves the requested recurring watch. A report does not create a scheduler.
- Propose a summary for `ccfa.yaml` using existing monitoring fields such as `last_monitoring_report`; do not silently overwrite project state unless explicitly asked.
- Flag conflicting papers for next use: add them to the project literature cache.

## 6. Handoff Rules

- Send **RESEARCH** items to `ccf-literature-searcher` for deep retrieval and closest-work clustering.
- Send **FOLLOW-UP** items to `ccf-idea-reviewer` when the user needs a score impact or to `ccf-idea-optimizer` when the user wants a rescue/differentiation route.
- Send new citation/positioning candidates to `ccf-paper-writer` only after stable source links are available.
- Send attribution or already-cited-paper conflicts to `ccf-integrity-auditor`.
