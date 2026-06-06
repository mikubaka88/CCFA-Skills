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
