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
  - **Medium (RESEARCH):** overlapping mechanism, benchmark, or claim; identify the distinction still unresolved and whether it matters to the current task.
  - **High (FOLLOW-UP):** same problem, similar method, and similar evidence path; identify the affected contribution before recommending a change.
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

- Use `references/report-template.md` for a full report; honor the user's format and use compact findings for short updates or internal contributions.
- Be honest about uncertainty: report what you don't know, not what you suspect.
- For full reports, use the template's high-relevance table; a short answer retains the relevant sources and changes without mandatory scores or extra sections.
- Include exact date range and source basis.

## 5. Follow-up and Persistence

- Store reports only when file output is requested or necessary within the authorized workflow; honor no-new-files. Preserve dated monitoring history when it serves the requested recurring watch. A report does not create a scheduler.
- When project-state maintenance is requested, propose a summary for `ccfa.yaml` using existing monitoring fields such as `last_monitoring_report`; do not silently overwrite project state unless explicitly asked.
- Reuse the existing literature cache when persistence is authorized and useful; a short update or internal finding does not itself require another file.

## 6. Handoff Rules

- Use `ccf-literature-searcher` for a specific unresolved source question needed by the current deliverable; a **RESEARCH** label alone does not require deeper retrieval.
- Use `ccf-idea-reviewer` for a needed concept judgment or `ccf-idea-optimizer` for authorized development; a **FOLLOW-UP** label does not authorize a new assessment or redesign deliverable.
- Pass verified citation/positioning candidates to `ccf-paper-writer` when writing is already requested or needed within scope.
- Use `ccf-integrity-auditor` for an unresolved attribution or existing-citation conflict that affects the current task; return its evidence to the integrating owner.
