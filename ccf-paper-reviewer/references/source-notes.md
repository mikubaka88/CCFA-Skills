# Source Notes

Use this file when explaining review-method provenance, official venue criteria, related-work search, or AI-review-tool inspiration.

## Shared Registry

The authoritative CCFA source inventory is:

```text
../ccf-common/references/source-registry.yaml
```

Do not duplicate long URL lists in this skill. Add or update public source records in the shared registry, then run:

```powershell
python ..\ccf-common\scripts\check_sources.py
```

## Use Rules

- Use official venue criteria for current-year review dimensions, page limits, anonymity, policy, ethics, and review forms.
- Use CSPaper, Agentic Reviewer, OpenAIReview, and related AI-review tools as workflow inspiration only; do not claim their exact calibration or hidden implementation.
- Use public-safe search queries for related work; never paste private manuscript wording into web search unless the user authorizes it.
- Apply the shared CCFA source-quality policy.
- Treat missing related work as searched, user-provided, or unverified.
- Never report exact acceptance probability or true venue percentile without a real calibrated comparison set.

## September 2026 Review Adaptation

Use registry IDs rather than loading whole external repositories at runtime:

- `cspaper-review`: public three-part report structure; concept review substitutes idea scope and research value for submission gates and acceptance readiness.
- `academic-research-skills-review`: stable concern IDs, evidence locations, and severity tied to the decision.
- `auto-claude-research-in-sleep`: verify primary artifacts and revisit changed or unresolved issues during revision.
- `ai-scientist-review-code`: explicit review fields and confidence separate from ratings; relevant to manuscript reports.
- `cmu-peerreview-bench`: check whether each finding is correct, consequential, and sufficiently grounded. No benchmark result is claimed.

Borrow workflow ideas and common field organization, not project code, long prompts, hidden calibration, or branded results. Do not import experiment-completeness criteria into default idea assessment. The public CSPaper source replaces the need to locate a private example file.
