# Literature Search Report Template

Use this file when writing a literature-search folder.

## Folder Layout

Default:

```text
output/literature-search/<topic-slug>/
  papers.md
  papers.csv        # only for requested structured export or downstream reuse
  search-notes.md    # only when provenance must persist separately
  idea-grounding.md  # only when feeding idea optimization
```

Resolve the project root through `../../ccf-common/references/artifact-contracts.md`. Reuse an existing search folder, including older dated names, and update its current report in place. Store the date and paper versions inside the report. Keep needed downloads/extractions under its `cache/`; do not create a new dated folder for each retry. If file writing is unavailable or prohibited, return the requested evidence in context.

The sections and columns below are a menu for the requested report. Omit unrequested scoring and empty sections. Keep one screened source set and derive a CSV only when useful; do not repeat the complete paper table and abstracts in search notes or downstream handoffs.

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

## idea-grounding.md

Create this optional file only when the search feeds `ccf-idea-optimizer`. Keep it compact and decision-relevant.

```md
# Idea-Grounding Packet

## Scope And Evidence Boundary

- Topic / seed:
- Search date:
- Source-supported facts:
- Searcher inferences:
- Unknowns:

## Evidence Cards

| Source | Supported observation | Reported limitation | Mechanism primitive | Protocol anchor | Transfer condition | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | dataset / baseline / metric / setting |  | direct / inferred / unknown |

## Cross-Source Relations

| Source pair / cluster | Relation | Open gap or conflict | Why it matters | Evidence needed next |
| --- | --- | --- | --- | --- |
|  | supports / conflicts-with / leaves-open / depends-on / evaluated-by |  |  |  |

## Idea Constraints

- Already covered central claims:
- Transferable mechanism primitives:
- Protocols suitable for direct comparison:
- Stale or overcrowded routes:
- Minimum viable research questions:
```

Limit the normal packet to eight evidence cards. Include a source only when it changes a problem boundary, mechanism choice, comparison set, or experiment protocol.
