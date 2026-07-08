#!/usr/bin/env python3
"""Generate CCFA visual-composer demo figures from verified Transformer data."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "ccf-visual-composer" / "resources" / "python"))

from ccfa_plot_recipes import (  # noqa: E402
    PALETTES,
    Theme,
    heatmap_matrix,
    lollipop_rank,
    save_svg,
    small_multiple_lines,
    slopegraph,
)


OUT = Path(__file__).resolve().parent / "figures"


def build() -> list[Path]:
    outputs: list[Path] = []
    note = "Source: demo/artifacts/official-data.md; values are official Transformer paper excerpts."

    outputs.append(
        save_svg(
            lollipop_rank(
                rows=[
                    {"task": "WMT14 EN-DE", "bleu": 28.4},
                    {"task": "WMT14 EN-FR", "bleu": 41.0},
                ],
                value_key="bleu",
                label_key="task",
                title="Transformer headline translation results",
                subtitle="Direct-labeled lollipop chart for the two official BLEU values.",
                note=note,
                unit=" BLEU",
                palette=[PALETTES["ccfa"][0], PALETTES["ccfa"][1]],
                theme=Theme(width=880, height=460),
            ),
            OUT / "translation_bleu_lollipop.svg",
        )
    )

    outputs.append(
        save_svg(
            slopegraph(
                rows=[
                    {"metric": "step time (s)", "base": 0.4, "big": 1.0},
                    {"metric": "training steps (100K)", "base": 1.0, "big": 3.0},
                    {"metric": "duration (12h units)", "base": 1.0, "big": 7.0},
                ],
                left_key="base",
                right_key="big",
                label_key="metric",
                title="Base-to-big training schedule shift",
                left_label="Base",
                right_label="Big",
                subtitle="Slightly normalized units keep the paired-change story visible.",
                note=note,
                palette=PALETTES["npg"],
                theme=Theme(width=860, height=520),
            ),
            OUT / "training_schedule_slopegraph.svg",
        )
    )

    outputs.append(
        save_svg(
            heatmap_matrix(
                matrix=[
                    [1.0, 1.0, 1.0, 1.0, 1.0],
                    [1.0, 2.0, 2.0, 2.0, 3.0],
                ],
                row_labels=["Base", "Big"],
                col_labels=["N", "d_model", "d_ff", "heads", "steps"],
                title="Transformer configuration ratios",
                subtitle="Column values are ratios relative to the base configuration.",
                note=note,
                palette=PALETTES["sequential_mint"],
                theme=Theme(width=820, height=390),
            ),
            OUT / "configuration_ratio_heatmap.svg",
        )
    )

    outputs.append(
        save_svg(
            small_multiple_lines(
                panels=[
                    {"title": "step time (s)", "x": [0, 1], "y": [0.4, 1.0]},
                    {"title": "training steps (100K)", "x": [0, 1], "y": [1.0, 3.0]},
                    {"title": "duration (12h units)", "x": [0, 1], "y": [1.0, 7.0]},
                    {"title": "attention heads", "x": [0, 1], "y": [8, 16]},
                ],
                title="Small-multiple view of base-to-big scaling",
                subtitle="Each panel keeps a local scale and direct labels the evidence shape.",
                note=note,
                palette=PALETTES["ccfa"],
                theme=Theme(width=900, height=560),
            ),
            OUT / "base_big_small_multiples.svg",
        )
    )
    return outputs


if __name__ == "__main__":
    for path in build():
        print(path.relative_to(ROOT).as_posix())
