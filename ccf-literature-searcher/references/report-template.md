# Literature Search Report Template

Use this file when writing a literature-search folder.

## Folder Layout

Default:

```text
literature-search-YYYYMMDD-<topic-slug>/
  papers.md
  papers.csv
  search-notes.md
```

If the user provides a project directory, write the folder there. Otherwise use the current workspace. If file writing is unavailable, return the same sections in the final answer.

## papers.md

```md
# Literature Search: <topic>

Date: YYYY-MM-DD
Search purpose:
Target venue/family:
Source-quality policy: applied

## Summary

- Closest-work clusters:
- Opportunity map:
- Strongest baselines:
- Benchmark/dataset candidates:
- Novelty risks:
- Recommended next action:

## Paper Table

| # | Title | Year | Venue/source | Link | Type | Insight | Completeness | Numeric evidence | Overall | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  | pure method / pure benchmark / method + benchmark |  |  |  |  |  |

## Clusters

### Cluster 1: <name>

- Representative papers:
- What this cluster already solves:
- Remaining gap:
- Possible rescue or differentiation route:
- How it affects the user's paper:

## Opportunity Map

| Cluster | Status | Open gap | Possible direction | Evidence needed | Risk |
| --- | --- | --- | --- | --- | --- |
|  | crowded but open / covered central claim / benchmark gap / mechanism gap / deployment-system gap / theory-analysis gap / negative-result opportunity |  |  |  |  |

## Benchmark And Dataset Candidates

| Name | Link | Task | Metrics | Baselines | Fit | Risks |
| --- | --- | --- | --- | --- | --- | --- |

## Citation And Positioning Cautions

- Claims that need direct citation:
- Papers that may weaken novelty:
- Papers that only support background:
```

## papers.csv

Use these columns:

```csv
title,year,venue_or_source,link,paper_type,insight_score,completeness_score,numeric_evidence_score,overall_label,relevance_note,quality_note
```

For pure benchmark papers, set `numeric_evidence_score` to `N/A benchmark`.

## search-notes.md

```md
# Search Notes

## Safe Queries Used

-

## Sources Checked

-

## Excluded Sources

- Policy-excluded or low-quality sources: noted in screening notes only.
- Other exclusions:

## Unknowns

- Papers not accessible:
- Venue status not verified:
- Missing benchmark details:

## Handoff Notes

- For writing:
- For idea optimization:
- For direction scouting:
- For experiment design:
- For review:
```
