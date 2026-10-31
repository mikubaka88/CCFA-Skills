# Exemplar Index

Use this index to find original passages that help substantive drafting or a specific writing problem, including requested venue or exemplar adaptation. Load matching sections, then inspect the original passage. Do not load every card or rank writing quality by venue or awards.

The lean release keeps the original Markdown passages and cards. Complete PDFs are an explicit optional offline pack; their absence alone does not prevent learning from a matched original text. When extraction or layout requires the PDF, install the matching pack or use an authorized original source, then inspect the selected passage. The full Git source still contains the PDFs. See the [installation profiles](../../../docs/INSTALLATION_MATRIX.md#lean-release-installation-recommended).

## Default Custom Format

Use `references/custom-format/default-user-format.md` when explicitly requested or established for the project. Missing venue information alone does not activate it or require exemplar loading. These user-supplied cards are available when relevant:

| Role | Venue | Card | Use when |
| --- | --- | --- | --- |
| User custom exemplar | ICLR family | `cards/llava-4d.md` | 4D scene understanding, spatiotemporal prompts, dataset plus model papers |
| User custom exemplar | CVPR | `cards/vggt.md` | feed-forward geometry, multi-task visual prediction, simple model versus optimization |

These two cards are user-supplied references available for matching writing questions. Selecting a useful passage does not activate the whole custom format or make either paper a universal writing model.

## Selection Rule

Use as few passages as answer the actual writing questions, with additional sources for distinct functions when useful. There is no required paper count or fixed maximum. Reuse available originals; extra retrieval follows `reference_style_search` in Common's preferences:

- Without a target venue, select by the actual scientific object, evidence type, and writing question; no card is mandatory.
- Prefer the same explanatory function and compatible scientific content: theorem, benchmark, user study, system, dataset, or mechanism.
- Judge the passage's clarity and argument directly; venue family is a useful context clue when relevant, not a quality ranking.
- Add a contrast card only when it resolves a concrete story or evidence-presentation choice.

Use cards to find and learn from original writing. Conventional phrases, natural field terminology, and verb–noun combinations can be reused when they fit; distinctive source passages, claims, examples, and technical content cannot be transplanted. If the user or project explicitly selects language conventions recorded in Reusable Techniques, read only the relevant entries and apply Humanization's preference precedence. A paper supplied for factual analysis does not automatically select its punctuation or rhythm; do not extract a new profile for an ordinary local edit.

For learning from real paper expression, use `references/exemplar-style-analysis.md` and inspect the source passage selected by the card before drafting. Cards contain both source summaries and adaptation advice; only source-anchored observations establish what a paper actually does. Awards and venue membership do not establish a writing technique. Transfer the sentence relationships and scientific explanation that fit the new material, without imposing a source's paragraph count or claim strength.

## ICLR And CVPR Award Discovery Cards

Use these cards to locate papers when the user asks about ICLR/CVPR awards. An award list establishes award context only. Inspect a candidate's actual passage and judge its clarity before selecting it as a writing reference; these discovery cards are not mandatory writing templates.

| Venue/year | Card | Use when |
| --- | --- | --- |
| ICLR 2026 Outstanding Papers | `cards/iclr-2026-outstanding-papers.md` | theoretical succinctness or LLM conversation-failure papers |
| ICLR 2025 Outstanding Papers | `cards/iclr-2025-outstanding-papers.md` | safety alignment, fine-tuning dynamics, and uncertainty-guided exploration papers |
| ICLR 2024 Outstanding Papers | `cards/iclr-2024-outstanding-papers.md` | large-model reasoning, data curation, equivariance, and principled learning papers |
| CVPR 2025 Best Paper | `cards/cvpr-2025-vggt-best-paper.md` | CVPR best-paper status note for VGGT; load `cards/vggt.md` for writing moves |
| CVPR 2024 Best Papers | `cards/cvpr-2024-best-papers.md` | human-feedback text-to-image and generative image dynamics papers |
| CVPR 2023 Best Papers | `cards/cvpr-2023-best-papers.md` | visual programming and planning-oriented autonomous driving papers |

## Other Venue Cards

| Venue family | Card | Use when |
| --- | --- | --- |
| Architecture / sequence modeling | `cards/transformer-writing-style.md` | explaining a computational dependency, structural bottleneck, or change of modeling primitive |
| AAAI / theory and social choice | `cards/aaai-2025-every-bit-helps.md` | theorem-heavy papers that settle a parameterized open question |
| AAAI / biomedical generation | `cards/aaai-2024-gxvaes.md` | application-driven generative modeling with biological context and case studies |
| ICML / LLM agents | `cards/icml-2025-collabllm.md` | multiturn LLM collaboration, reward design, benchmark plus user study |
| ICML / video generation | `cards/icml-2024-videopoet.md` | multimodal autoregressive generation and zero-shot capability papers |
| ICCV / generative 3D vision | `cards/iccv-2025-brickgpt.md` | text-to-3D generation, physical constraints, dataset plus inference guardrails |
| ICCV / computational imaging | `cards/iccv-2023-passive-ultra-wideband.md` | passive sensing, extreme timescale imaging, hardware plus reconstruction |
| ECCV / computational imaging | `cards/eccv-2024-minimalist-vision.md` | hardware-software co-design, privacy/efficiency motivation, surprising minimalism |
| ECCV / representation analysis | `cards/eccv-2022-partial-distance-correlation.md` | statistical tools as versatile deep-learning regularizers or diagnostics |
| ACM MM / 3D affordance | `cards/acmmm-2025-aff3dfunc.md` | open-vocabulary 3D affordance understanding and robot validation |
| ACM MM / speech-video | `cards/acmmm-2024-speaker-to-dubber.md` | multimodal generation with alignment constraints and staged training |
| ACL / NLP benchmark | `cards/acl-2025-minilongbench.md` | benchmark compression, evaluation cost reduction, rank-correlation evidence |
| ACL / linguistic evaluation | `cards/acl-2024-mission-impossible.md` | cognitive/linguistic probes, synthetic tasks, claim-testing papers |
| NeurIPS / RL scaling | `cards/neurips-2025-1000-layer-ssl-rl.md` | scaling studies, capability emergence, self-supervised RL evidence |
| NeurIPS / image generation | `cards/neurips-2024-var.md` | new generation paradigm, scaling laws, next-scale prediction |

## Non-AI/CV/NLP Venue Cards

Use these cards when the target venue is outside the dominant AI/CV/NLP cluster. They are meant to prevent the writing skill from forcing every paper into an ML-style "model plus table" story.

| Venue family | Card | Use when |
| --- | --- | --- |
| SIGMOD / database systems | `cards/sigmod-2024-polardb-mp.md` | cloud-native databases, distributed transactions, storage/compute disaggregation, system architecture |
| USENIX Security / security systems | `cards/usenix-security-2024-inspectre-gadget.md` | attack/defense papers, threat models, exploit chains, security evaluation |
| POPL / programming languages | `cards/popl-2024-megalibm.md` | program synthesis, numerical libraries, PL/tool papers with formal and empirical evidence |
| CHI / HCI | `cards/chi-2024-constrained-highlighting.md` | user-study papers, interaction technique evaluation, human-centered evidence |

## Example Selections

These are candidates for distinct writing functions, not bundles to load by default. Select a useful original passage and add another source only when it answers a different writing question.

- Unspecified venue: preserve the requested format and use the writer's disclosed NeurIPS fallback only for a new LaTeX paper without a usable target template. Select an exemplar only for a concrete writing question.
- 4D embodied AI paper: `llava-4d.md`, `vggt.md`, `neurips-2025-1000-layer-ssl-rl.md`.
- Theory paper: `aaai-2025-every-bit-helps.md` for relating a parameterized result to prior bounds; choose a different source when the proof or question needs another kind of explanation.
- Vision paper: `vggt.md` when the writing question concerns 3D geometry or related prediction outputs; awards do not determine selection.
- LLM collaboration or agent paper: `icml-2025-collabllm.md`, `acl-2025-minilongbench.md`.
- Generative multimodal system: `iccv-2025-brickgpt.md`, `acmmm-2024-speaker-to-dubber.md`, `icml-2024-videopoet.md`, `neurips-2024-var.md`.
- Data-efficient or cost-efficient evaluation: `acl-2025-minilongbench.md`, `aaai-2025-every-bit-helps.md`.
- Hardware or system paper: `eccv-2024-minimalist-vision.md`, `vggt.md`.
- Open-vocabulary robotics paper: `acmmm-2025-aff3dfunc.md`, `iccv-2025-brickgpt.md`.
- Database system paper: `sigmod-2024-polardb-mp.md` plus one DB/IR/KDD source found through `ccf-literature-searcher`.
- Network/system paper: find an actual paper passage matching the system question through `ccf-literature-searcher`; a conference program or keynote mention does not stand in for a paper.
- Security paper: `usenix-security-2024-inspectre-gadget.md` plus a threat-model or artifact-evaluation source.
- HCI paper: `chi-2024-constrained-highlighting.md` plus the user's target population/study-method reference.
- PL/tool paper: `popl-2024-megalibm.md` for connecting an implementation difficulty to a tool's capabilities.

## Style And Citation Guides

When loading exemplar cards, also follow the writing style and citation rules established in the main skill references:

- `references/research-writing-patterns.md` (Natural Writing Style section): prose flow, selective emphasis, and citation weaving.
- `references/citation-workflow.md`: verified attribution and evidence coverage without citation quotas.
- `references/output-style-policy.md`: requested format, preserved citation keys, and phase-aware drafting.

The cards locate useful source passages and explain observed writing moves. Use the relevant source and guidance to compose the scientific explanation before applying the ordinary prose check.

## Output Reminder

For an explicit exemplar-analysis request, identify selected cards and transferable writing moves with source attribution. For ordinary drafting, apply relevant moves internally and return the requested original prose; do not append a compulsory exemplar report, warning list, or section plan.
