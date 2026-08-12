# Source Notes

Use this file when the user asks why the idea-optimization workflow is structured this way, asks for provenance, or needs current official policy checks.

## Shared Registry

The authoritative CCFA source inventory is:

```text
../ccf-common/references/source-registry.yaml
```

Do not duplicate long URL lists in this skill. Add or update public source records in the shared registry, then run:

```powershell
python ..\ccf-common\scripts\check_sources.py
```

## Idea-Optimizer Use Rules

- Use official venue pages for current review forms, policies, tracks, anonymity, artifacts, ethics, and page limits.
- Use papers, proceedings, official project pages, and credible scholar pages for literature grounding.
- Do not treat source lists as proof of novelty. Novelty requires checking the specific idea against close work.
- Treat unsearched prior art as uncertainty, not as novelty.
- Avoid copying source wording. Extract evaluation structure, problem-framing questions, and research-taste signals only.
- Follow `../ccf-common/references/privacy-and-evidence.md` before using private idea text in any search query.
- For literature-grounded idea evolution, use the public-system records in the shared registry as workflow provenance only. Current relevant records include `ai-scientist-v2`, `rd-agent`, `storm`, `gpt-researcher`, `paper-qa2`, `ai-researcher`, and `arbor-agent`. Do not present their GitHub popularity or claimed benchmark performance as evidence that an idea is scientifically valid.
