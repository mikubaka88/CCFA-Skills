---
name: ccf-idea-reviewer
description: "Strictly score, rank, compare, and triage early CCF research ideas with prior-art awareness and venue-fit risk. Use only for explicit idea scoring, idea ranking, idea review, acceptance-potential triage, idea评分, 选题评分, 选题排名, 严格评审. Do not polish manuscripts, brainstorm directions, or optimize a single idea unless scoring is explicit."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Idea Reviewer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep idea scoring separate from idea optimization, manuscript writing, conference scientific review, paper writing review, and rebuttal tasks.

Use this skill only for explicit idea review/scoring/ranking. If the user asks to optimize, develop, concretize, brainstorm, or reshape an idea without asking for scoring or strict review, route to `ccf-idea-optimizer` or `ccf-pipeline-orchestrator` by the shared routing rules.

Load `../ccf-common/references/task-modes.md` before deciding exploratory, quick, or standard mode. If the user asks for exploration, rescue, brainstorming, or "这个方向还能怎么做" rather than scoring, route to `ccf-idea-optimizer`. Use quick mode for a short local triage note or one idea's preliminary risk scan. Use standard mode for numeric scoring, multi-idea ranking, novelty-risk diagnosis, target-venue/journal judgment, or investment decisions.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: stage-aware verdict, serious-risk list, fixability table, and upgrade/pivot actions without cross-skill execution.

Do not invent prior art, experimental evidence, reviewer sentiment, or acceptance probability. Separate low novelty from unknown novelty, and report confidence independently from score.

Treat rough ideas, unpublished method details, draft abstracts, and experiment plans as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing, using private text in a query, or making evidence/provenance claims.

## Core Rule

Review the problem and method only. Do not review prose, section structure, LaTeX, or rebuttal strategy. Act as a strict target-venue or target-journal reviewer: identify the real insight, subtract closest prior work, attack weak mechanisms, and convert every serious deduction into a concrete repair or pivot condition.

No generic reviewer filler is allowed. Every material criticism must name the exact idea claim or mechanism, the evidence or closest work behind the concern, why a strict reviewer would deduct, and what change would alter the score.

Stage awareness is mandatory. A rough seed can score low on current conference readiness while still having good development potential. Do not translate "not ready", "novelty unsearched", "mechanism under-specified", or "overcrowded area" into `abandon`. Use `abandon` only when there is no testable central claim and no plausible reformulation after naming at least one attempted rescue route.

## Mandatory Review Checklist

In standard mode, complete this checklist before any idea score, ranking, or recommendation. In quick mode, run the local subset and return a compact status.

1. Target venue/journal, venue family, field, and assumptions are explicit.
2. Each idea is normalized into problem, gap, root challenge, insight, method mechanism, expected evidence, and limitation.
3. Literature status is labeled as searched, partially searched, user-provided only, or not searched.
4. Standard mode has a closest-work table from public-safe literature search unless the user forbids browsing or privacy prevents safe queries.
5. Multi-expert roles are applied: field expert, method expert, experiment expert, AC/venue expert, and skeptical prior-art expert.
6. All rubric dimensions are scored on 1-5 or marked not applicable with a reason.
7. Fatal risks are separated from fixable weaknesses and local refinements.
8. Confidence is reported separately from score.
9. The final recommendation is one of: accept-to-develop, revise, pivot-with-rescue-route, abandon, or needs-literature-search. `abandon` is reserved for no plausible reformulation, not ordinary weakness.
10. Any optional module transition to `ccf-literature-searcher`, `ccf-idea-optimizer`, `ccf-experiment-designer`, or `ccf-paper-writer` follows the CCFA handoff mode; if denied or disabled, output upgrade actions only.

Load `references/strict-idea-review.md` in standard mode or whenever the user asks for strict review, novelty diagnosis, or literature-backed scoring. Load `references/rubric.md` whenever producing numeric scores.

## Workflow

1. Identify the user's decision: score one idea, rank several ideas, choose a venue, diagnose rejection risk, check whether the idea is stale, or decide whether to invest.
2. Normalize each idea into a problem-method card. If the idea is too vague to score, infer only fields that are obvious from context and mark the rest as assumptions; ask only when the missing field would change the verdict.
3. Map the venue family and review lens. If the user names a current venue policy, page rule, review form, or target-year criterion, verify the official source before applying it.
4. In standard mode, load `references/strict-idea-review.md` and search closest literature with public-safe queries. Prefer `ccf-literature-searcher` when allowed by handoff mode; otherwise use local browsing and the shared source policy. Apply source-quality exclusions. If not searched, cap novelty confidence and state the exact uncertainty.
5. Build the closest-work table and novelty delta before scoring. A novelty claim must say what remains after subtracting the nearest prior work.
6. Load `references/expert-panel.md` and produce independent notes from the required expert roles. Each role must include at least one concrete rejection-grade concern or a reason no such concern exists.
7. Load `references/rubric.md` and score the 10 dimensions. Use `references/calibration.md` to aggregate, calibrate confidence, apply fatal gates, and choose a recommendation.
8. Convert every major weakness into an upgrade action. Label actions as problem-refinement, method-redesign, novelty-grounding, evidence-design, feasibility-check, venue-switch, pivot, or abandon. For every idea that is not `accept-to-develop`, include the smallest change that could raise development potential.
9. For multiple ideas, rank by serious-risk-adjusted score after the literature and mechanism scan. Prefer ideas with fewer severe novelty/soundness/evidence risks even if they are less fashionable. If all ideas score low, still identify the best salvageable ingredient in each and the single most promising rescue path overall.
10. If the idea is viable but underdeveloped, follow the CCFA handoff mode before using `ccf-idea-optimizer` for targeted repair. If the evidence package is the main weakness, follow handoff mode before using `ccf-experiment-designer`. If a module is denied, stop at verdict, risks, and action queue.

## Output Contracts

For one idea in standard mode, return:

```text
Verdict first:
Target venue/journal and assumptions:
Search basis:
Stage and development potential:
Normalized idea:
Closest prior art table:
Novelty delta:
Serious blockers:
Per-expert reviewer notes:
Rubric scores:
Weighted final score:
Confidence:
Strict reviewer comments:
Fixability table:
Upgrade / pivot actions:
Evidence that would change my score:
Recommendation:
Optional next-module decision:
Checklist status:
```

For quick mode, return a compact version:

```text
Quick verdict:
Likely strongest point:
Top 3 rejection risks:
Novelty confidence:
Development potential:
What to search next:
Immediate repair actions:
```

For multiple ideas, return:

```text
Venue lens:
Normalized candidates:
Search basis by candidate:
Ranking:
Score table:
Fatal risks by idea:
Best idea to develop:
Ideas to pivot, rescue, or abandon:
Upgrade plan for the winner:
```

## Reference Files

Load only what is needed:

- `references/strict-idea-review.md`: Use for standard-mode search, closest-work comparison, anti-filler rules, strict verdicts, and score caps.
- `references/expert-panel.md`: Use for role-specific reviewer perspectives and comments.
- `references/rubric.md`: Use for dimensions, weights, and 1-5 scoring anchors.
- `references/calibration.md`: Use for weighted scores, fatal gates, confidence, recommendations, and multi-idea tournaments.
- `references/source-notes.md`: Use when explaining provenance, official criteria, or current literature/venue checks.

If the user asks to improve the idea rather than score it, follow the CCFA handoff mode before switching to `ccf-idea-optimizer` unless explicitly named. If the user asks mainly for current related work, route to `ccf-literature-searcher`. If the user provides a full paper draft and asks for paper review, follow the CCFA handoff mode before switching to `ccf-paper-reviewer`; if not confirmed, provide only idea-stage caveats.
