# Custom Format Behavior Acceptance Cases

These cases specify expected behavior for maintenance checks. They are not records of executed model evaluations or evidence of a quality or score improvement.

## Format Selection

| Request | Expected behavior |
| --- | --- |
| “帮我写一个论文摘要”，未指定会议或格式 | Return the requested abstract; no compulsory custom-format intake, exemplar loading, or LaTeX wrapper. |
| New LaTeX paper, no usable target template | Disclose the NeurIPS format fallback; draft content before requested length fitting. |
| Supplied Markdown manuscript, no venue | Preserve Markdown and the requested edit scope. |
| User requests the custom format or the project already selects it | Apply its argument principles; select relevant exemplar cards only as needed. |
| Explicit venue template is supplied but no local venue guide exists | Preserve the supplied template; verify current rules only for a compliance claim. |

## Evidence And Cost Boundaries

| Input or request | Expected behavior |
| --- | --- |
| Draft about dynamic 3D scene memory; only a proposed method is supplied | Explain supplied mechanisms without inventing a benchmark, result, comparison win, or completed construction. |
| Experiments are pending | Follow `references/materials-to-manuscript.md`; retain the authorized scaffold and missing-value markers, with no outcome-dependent abstract or conclusion claim. |
| A narrow literature thread has few decisive sources | Judge support and closest-work coverage; do not add citations to reach a quota. |
| A real ordered procedure uses “First” and “Second” | Preserve useful ordering; humanization evaluates meaning and flow rather than forbidden words. |
| Additional independent review is disabled | Complete necessary primary checks and any required scoped handoff; do not create an unrequested second independent pass. |
| Additional independent review is enabled and useful | Inspect a bounded unresolved issue, integrate evidence once, and avoid duplicate full reports. |
| Ordinary writing request | Return the requested prose. Keep internal argument maps and checks internal unless needed to explain a material unresolved input. |

## Exemplar Use

The user-supplied LLaVA-4D and VGGT cards remain attributed writing references. Their relevance depends on the scientific object and writing question. Neither is mandatory, and their methods, performance claims, or wordings must not be copied into a new paper.

For a maintenance evaluation, run the same inputs against old and new rules, retain actual outputs and available cost measurements only when the evaluation is authorized, and inspect semantic differences. Do not label these expected behaviors as test passes without execution.
