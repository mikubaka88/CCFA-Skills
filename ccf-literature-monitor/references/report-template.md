# Monitoring Report Template

This is the canonical structure for full monitoring reports. Honor a requested short answer or other user format, keeping the time range, source basis, and relevant changes; internal contributions return findings to the owner without a separate report. Full reports retain the fields below as applicable, without inventing counts, scores, or actions to fill them.

## Report Header

```markdown
## Literature Monitoring Report: [Monitoring Mode] - [Topic/Category]

**Date:** [YYYY-MM-DD]
**Time Range:** [from] to [to]
**Sources Scanned:** [arXiv categories / OpenReview venues / proceedings / labs / project pages]
**Query Basis:** [public-safe keywords or user-approved query text]
**Papers Scanned:** [count]
**High-Relevance Papers:** [count]
**Overall Signal:** RELAX / RESEARCH / FOLLOW-UP
**Confidence:** [1-5 with reason]
```

## Source Coverage

```markdown
| Source | Scope | Count | Notes |
|:---|:---|---:|:---|
| arXiv | [categories/queries] | [count] | [coverage limits] |
| OpenReview / venue | [venues] | [count] | [coverage limits] |
| Labs / competitors | [names] | [count] | [coverage limits] |
```

## Executive Summary

One paragraph summary of the monitoring result, including total papers scanned, number of high-relevance papers, overlap distribution, and the action supported by the findings. Do not claim that an idea is novel solely because no overlap appeared in the scanned window.

## High-Relevance Papers

Table of papers that show potential overlap with the user's idea.

| # | Title | Source | Date | Overlap Score (0-5) | Overlap Level | Overlap Type | Evidence Basis | Recommended Action |
|:---:|:---|:---|:---:|:---:|:---:|:---|:---|:---:|
| 1 | [Title] | [arXiv/OpenReview/Venue] | [YYYY-MM-DD] | [0-5] | None/Low/Medium/High | Problem/Method/Evidence/Benchmark | [abstract/intro/result] | RELAX/RESEARCH/FOLLOW-UP |
| 2 | ... | ... | ... | ... | ... | ... | ... | ... |

## Detailed Findings

For each high-relevance paper, provide:

- **Title:** [full title]
- **URL:** [arXiv, OpenReview, proceedings, DOI, or project link]
- **Source/date:** [source and publication/preprint date]
- **Key contribution:** [what the paper claims or contributes]
- **Overlap rationale:** [why this overlaps or differs from the user's idea]
- **Uncertainty:** [what was not checked]
- **Action:** [RELAX | RESEARCH | FOLLOW-UP with reasoning]

## Trend Map

Summarize emerging trends and open gaps in the scanned sources. Separate observed trends from inferred opportunities.

## Flags for Other Skills

Include only useful flags with the specific gap or requested action: `RELAX` means no material overlap found in the scanned window, `RESEARCH` means partial overlap needing clarification when it affects the task, and `FOLLOW-UP` means substantial overlap with a decision to resolve. Neither label automatically starts another workflow. Relevant handoff fields are:

- `@ccf-literature-searcher`: [papers or clusters to retrieve deeply]
- `@ccf-idea-reviewer`: [novelty implications for idea score]
- `@ccf-idea-optimizer`: [differentiation or rescue routes]
- `@ccf-paper-writer`: [related-work or positioning updates]
- `@ccf-integrity-auditor`: [potential dependency or attribution issues]

## Output Self-Check (Internal Unless Requested Or Material To Coverage)

```text
Date range explicit:
Source basis stated:
Private text avoided or user-approved:
Table columns valid:
No unsupported novelty conclusion:
Handoff flags concrete:
```
