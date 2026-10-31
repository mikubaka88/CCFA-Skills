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
- Use original papers, proceedings, technical reports, and primary project artifacts for literature grounding; scholar pages help locate them. Inspect the relevant passage and its version before relying on a scientific claim.
- Do not treat source lists as proof of novelty. Novelty requires checking the specific idea against close work.
- Treat unsearched prior art as uncertainty, not as novelty.
- Avoid copying source wording. Extract evaluation structure, problem-framing questions, and research-taste signals only.
- Follow `../ccf-common/references/privacy-and-evidence.md` before using private idea text in any search query.
- Use the relevant records in the shared registry for workflow provenance. Distinguish an adapted retrieval or candidate-selection principle from a reproduced system, trained model, or measured improvement. GitHub popularity and reported benchmark performance do not establish the validity of a new research idea.
