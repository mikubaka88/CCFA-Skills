# Exemplar Index

Use this index when the user asks for CCF A-level paper writing, best-paper style, venue-specific adaptation, default user-custom writing, or examples from strong papers. Load only the cards that match the target paper. Do not load every card by default.

## Default Custom Format

When the target venue is not specified, load `references/custom-format/default-user-format.md` first. That format currently uses the user's two custom exemplar cards:

| Role | Venue | Card | Use when |
| --- | --- | --- | --- |
| User custom exemplar | ICLR family | `cards/llava-4d.md` | 4D scene understanding, spatiotemporal prompts, dataset plus model papers |
| User custom exemplar | CVPR | `cards/vggt.md` | feed-forward geometry, multi-task visual prediction, simple model versus optimization |

These two cards are user-custom writing-format sources. Do not treat them as ordinary venue best-paper cards unless the user explicitly asks to compare against ICLR/CVPR best-paper style.

## Selection Rule

Pick at most 2-4 cards:

- Use the custom-format cards first when no target venue is specified.
- Use same venue or venue family first when a target venue is specified.
- Use same evidence type second: theorem, benchmark, user study, system, dataset, or ablation-heavy model.
- Use same story shape third: new task, new benchmark, new model family, new capability, or new evaluation economy.
- Add one contrast card only when it improves reviewer-proofing.

Use cards to borrow writing moves, not claims, wordings, examples, or technical content.

## ICLR And CVPR Recent Best-Paper Cards

Use these cards when the user explicitly asks for ICLR/CVPR best-paper or outstanding-paper style.

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
| SIGCOMM / networking systems | `cards/sigcomm-2024-l25gc-plus.md` | network systems, 5G core, latency/throughput, realistic deployment workloads |
| USENIX Security / security systems | `cards/usenix-security-2024-inspectre-gadget.md` | attack/defense papers, threat models, exploit chains, security evaluation |
| POPL / programming languages | `cards/popl-2024-megalibm.md` | program synthesis, numerical libraries, PL/tool papers with formal and empirical evidence |
| CHI / HCI | `cards/chi-2024-constrained-highlighting.md` | user-study papers, interaction technique evaluation, human-centered evidence |
| STOC/FOCS / theory | `cards/stoc-2024-theory-best-paper.md` | theorem-first papers, lower/upper-bound stories, proof roadmap and technical barrier framing |

## Recommended Bundles

- Default unspecified-venue paper: load `references/custom-format/default-user-format.md`; it will select `llava-4d.md` and `vggt.md`.
- 4D embodied AI paper: `llava-4d.md`, `vggt.md`, `neurips-2025-1000-layer-ssl-rl.md`.
- ICLR-style theory or LLM paper: one ICLR recent best-paper card plus one same-topic card.
- CVPR-style vision paper: one CVPR recent best-paper card plus `vggt.md` if the paper involves 3D geometry or multi-task prediction.
- LLM collaboration or agent paper: `icml-2025-collabllm.md`, `acl-2025-minilongbench.md`.
- Generative multimodal system: `iccv-2025-brickgpt.md`, `acmmm-2024-speaker-to-dubber.md`, `icml-2024-videopoet.md`, `neurips-2024-var.md`.
- Data-efficient or cost-efficient evaluation: `acl-2025-minilongbench.md`, `aaai-2025-every-bit-helps.md`.
- Hardware or system paper: `eccv-2024-minimalist-vision.md`, `vggt.md`.
- Open-vocabulary robotics paper: `acmmm-2025-aff3dfunc.md`, `iccv-2025-brickgpt.md`.
- Database system paper: `sigmod-2024-polardb-mp.md` plus one DB/IR/KDD source found through `ccf-literature-searcher`.
- Network/system paper: `sigcomm-2024-l25gc-plus.md` plus a venue-specific baseline/evaluation source.
- Security paper: `usenix-security-2024-inspectre-gadget.md` plus a threat-model or artifact-evaluation source.
- HCI paper: `chi-2024-constrained-highlighting.md` plus the user's target population/study-method reference.
- PL/theory paper: `popl-2024-megalibm.md` or `stoc-2024-theory-best-paper.md` depending on whether the contribution is tool/proof or theorem/barrier.

## Style And Citation Guides

When loading exemplar cards, also follow the writing style and citation rules established in the main skill references:

- `references/research-writing-patterns.md` (Natural Writing Style section): prose flow, forbidden patterns (no bold labels, no citation dumps), citation weaving.
- `references/citation-workflow.md`: search-bib-cite workflow, citation density per section, natural citation patterns.
- `references/output-style-policy.md` (Citation Format Rules): claim-first citation style, no author-name subjects, bib file as source of truth.

The exemplar cards provide structural patterns. The style guides provide execution rules. Use both.

## Output Reminder

After loading cards, produce:

1. Chosen exemplar set and why each card fits.
2. Transferable writing moves.
3. Drafting warnings where an exemplar's confidence would not be supported by the user's evidence.
4. A section plan or revision that is original to the user's paper.
