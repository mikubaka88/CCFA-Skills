#!/usr/bin/env python3
"""Editable, data-driven multi-panel scientific figures.

Run --list, or --demo all --out <task-directory>. Real data requires --data.
Synthetic examples are generated only by an explicit --demo request.
Dependencies: NumPy and Matplotlib; the original SVG library stays standalone.
"""
from __future__ import annotations

import argparse
import json
from math import erfc, sqrt
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from matplotlib.ticker import MaxNLocator

import ccfa_analysis_panels as p
from ccfa_plot_recipes import PALETTES


CATALOG = {
    "mechanism_overview": ("Mechanism and supporting analyses", 143, "ccfa"),
    "benchmark_atlas": ("Benchmark, distribution and resource trade-offs", 145, "npg"),
    "ablation_interactions": ("Component ablations and interactions", 145, "aaas"),
    "scaling_robustness": ("Scale, budget and robustness curves", 140, "tol_bright"),
    "representation_diagnostics": ("Embedding, attention and representation diagnostics", 150, "tol_muted"),
    "biological_atlas": ("Cell groups, expression and effect screening", 145, "nejm"),
    "paired_effects": ("Paired observations and subgroup effects", 140, "lancet"),
    "calibration_errors": ("Calibration, confusion and error structure", 145, "jco"),
    "sensitivity_dynamics": ("Density, perturbation, state evolution and category composition", 142, "ccfa"),
}


def _vector(values, name, *, nonnegative=False):
    values = np.asarray(values, dtype=float)
    if values.ndim != 1 or not len(values) or not np.isfinite(values).all():
        raise ValueError(f"{name} must be a nonempty finite vector")
    if nonnegative and (values < 0).any():
        raise ValueError(f"{name} must be nonnegative")
    return values


def _encoding(data, palette):
    ids = data["methods"]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError("methods must be nonempty unique IDs in the intended order")
    return p.entity_encoding(ids, palette=palette, colors=data.get("entity_colors"))


def _colors(ids, enc):
    return [enc[key]["color"] for key in ids]


class _PanelGrid:
    def __init__(self, outer, ratios):
        self.rows = {i: outer[i, 0].subgridspec(1, 3, width_ratios=ratios) for i in [1, 2]}

    def __getitem__(self, key):
        row, column = key
        return self.rows[row][0, column]


def _figure(data, enc, width, height, *, ratios=(1, 1, 1)):
    fig = p.new_figure(width_mm=width, height_mm=height)
    fig.set_layout_engine("constrained", w_pad=.025, h_pad=.03,
                          wspace=.09, hspace=.09, rect=(0, .04, 1, .96))
    outer = fig.add_gridspec(3, 1, height_ratios=[.09 if enc else .001, 1, 1])
    grid = _PanelGrid(outer, ratios)
    legend_ax = fig.add_subplot(outer[0, 0])
    legend_ax.axis("off")
    if enc:
        handles = [Line2D([], [], color=v["color"], marker=v["marker"],
                          linewidth=1.25, markersize=4, label=k) for k, v in enc.items()]
        legend_ax.legend(handles=handles, loc="center", ncol=min(len(handles), 5),
                         frameon=False, handlelength=1.6, columnspacing=1.2)
    if data.get("_meta", {}).get("synthetic"):
        fig.text(.995, .008, "Simulated data · layout demonstration", ha="right",
                 va="bottom", fontsize=8, color="#69737d")
    return fig, grid


def _panel(fig, spec, letter, title):
    ax = fig.add_subplot(spec)
    p.panel_label(ax, letter, title)
    return ax


def _lines(ax, block, enc):
    if not block["series"]:
        raise ValueError("A curve panel needs at least one supplied series")
    for series in block["series"]:
        key = series["method"]
        if key not in enc:
            raise ValueError(f"Unknown method ID {key!r}")
        p.line_band(ax, block["x"], series["y"], lower=series.get("lower"),
                    upper=series.get("upper"), color=enc[key]["color"],
                    marker=enc[key]["marker"], label=key,
                    xlabel=block["xlabel"], ylabel=block["ylabel"])
    scale = block.get("xscale", "linear")
    if scale == "log" and (np.asarray(block["x"], dtype=float) <= 0).any():
        raise ValueError("Log axes require strictly positive x values")
    ax.set_xscale(scale)
    if "ylim" in block:
        bounds = _vector(block["ylim"], "ylim")
        if len(bounds) != 2 or bounds[0] >= bounds[1]:
            raise ValueError("ylim needs two increasing bounds")
        for s in block["series"]:
            observed = np.concatenate([np.ravel(s.get(k, [])) for k in ["y", "lower", "upper"]])
            if len(observed) and ((observed < bounds[0]).any() or (observed > bounds[1]).any()):
                raise ValueError("ylim would hide supplied observations or uncertainty")
        ax.set_ylim(*bounds)
    ax.xaxis.set_major_locator(MaxNLocator(4)) if scale == "linear" else None


def _heatmap(fig, ax, block, *, label=None):
    image = p.matrix_heatmap(ax, block["values"], block["rows"], block["columns"],
                             cmap=block.get("cmap", "viridis"),
                             vmin=block.get("vmin"), vmax=block.get("vmax"),
                             center=block.get("center"), annotate=block.get("annotate", False),
                             fmt=block.get("fmt", ".1f"))
    bar = fig.colorbar(image, ax=ax, fraction=.045, pad=.035, shrink=.9)
    bar.solids.set_rasterized(False)
    bar.set_label(label or block["unit"])
    return image


def _comparison(ax, block, enc):
    if block.get("runs") is not None:
        run_means = [np.mean(_vector(row, "runs")) for row in block["runs"]]
        if len(run_means) != len(block["mean"]) or not np.allclose(run_means, block["mean"], atol=1e-6, rtol=1e-5):
            raise ValueError("Supplied means must agree with the plotted runs; retain unrounded data")
    p.comparison_intervals(ax, block["labels"], block["mean"],
                           lower=block.get("lower"), upper=block.get("upper"),
                           runs=block.get("runs"), colors=_colors(block["labels"], enc),
                           xlabel=block["xlabel"], seed=31)
    ax.set_ylim(len(block["labels"])-.5, -.5)


def _pareto(ax, block, enc):
    return p.pareto_scatter(ax, block["x"], block["y"], block["labels"],
                            colors=_colors(block["labels"], enc),
                            x_direction=block.get("x_direction", "min"),
                            y_direction=block.get("y_direction", "max"),
                            xlabel=block["xlabel"], ylabel=block["ylabel"],
                            annotate=False)


def _mechanism(ax, block, enc):
    labels = block["stages"]
    if len(labels) != 3:
        raise ValueError("mechanism_overview expects three supplied stage labels")
    ax.set(xlim=(0, 1), ylim=(0, 1)); ax.axis("off")
    positions = [.025, .365, .705]
    colors = list(enc.values())
    for i, (left, label) in enumerate(zip(positions, labels)):
        color = colors[i % len(colors)]["color"]
        ax.add_patch(FancyBboxPatch((left, .17), .27, .63,
                     boxstyle="round,pad=0.006,rounding_size=0.018",
                     facecolor=color, alpha=.09, edgecolor="none"))
        ax.text(left + .135, .72, label, ha="center", va="center", fontweight="bold")
        if i == 0:
            for j in range(3):
                ax.add_patch(Rectangle((left + .045 + j*.025, .32 + j*.05), .135, .20,
                             facecolor="white", edgecolor=color, linewidth=.9))
        elif i == 1:
            for row in range(3):
                for col in range(5):
                    ax.add_patch(Rectangle((left+.04+col*.038, .30+row*.065), .029, .045,
                                 facecolor=color, alpha=.3 + .15*row, edgecolor="none"))
        else:
            for j in range(4):
                cc = colors[j % len(colors)]["color"]
                ax.add_patch(FancyBboxPatch((left+.035+j*.052, .34), .038, .17,
                             boxstyle="round,pad=.003,rounding_size=.01",
                             facecolor=cc, alpha=.75, edgecolor="none"))
        if i < 2:
            ax.add_patch(FancyArrowPatch((left+.28, .46), (positions[i+1]-.015, .46),
                         arrowstyle="-|>", mutation_scale=10, linewidth=1, color="#43515e"))
    ax.text(.5, .035, block["note"], ha="center", va="bottom", color="#4c5966", fontsize=8)


def mechanism_overview(data, enc, width, height):
    fig, g = _figure(data, enc, width, height)
    _mechanism(_panel(fig, g[1, :2], "a", "Representation flow"), data["mechanism"], enc)
    _lines(_panel(fig, g[1, 2], "b", "Memory growth"), data["memory_curve"], enc)
    _comparison(_panel(fig, g[2, 0], "c", "Task performance"), data["performance"], enc)
    _pareto(_panel(fig, g[2, 1], "d", "Resource trade-off"), data["tradeoff"], enc)
    _heatmap(fig, _panel(fig, g[2, 2], "e", "Where gains occur"), data["gain_matrix"])
    return fig


def benchmark_atlas(data, enc, width, height):
    fig, g = _figure(data, enc, width, height)
    _heatmap(fig, _panel(fig, g[1, :2], "a", "Cross-task benchmark"), data["benchmark"])
    _comparison(_panel(fig, g[1, 2], "b", "Repeated runs"), data["performance"], enc)
    _pareto(_panel(fig, g[2, 0], "c", "Accuracy versus cost"), data["tradeoff"], enc)
    ax = _panel(fig, g[2, 1], "d", "Sample-level spread")
    p.paired_distribution(ax, data["samples"], data["methods"], colors=_colors(data["methods"], enc),
                           ylabel=data["sample_unit"], seed=17)
    ax.set_xticks(range(len(data["methods"])), [name.replace(" ", "\n", 1) for name in data["methods"]])
    _lines(_panel(fig, g[2, 2], "e", "Data efficiency"), data["sample_curve"], enc)
    return fig


def ablation_interactions(data, enc, width, height):
    variants = data["variants"]
    matrix = np.asarray(data["enabled"])
    if matrix.shape != (len(variants), len(data["components"])) or not np.isin(matrix, [0, 1]).all():
        raise ValueError("enabled must be a binary variant-by-component matrix")
    if data["score"]["labels"] != variants or data["effects"]["labels"] != variants[:-1]:
        raise ValueError("Ablation scores and effects must follow variant order; the last variant is the full reference")
    fig, g = _figure(data, enc, width, height, ratios=(1.15, 1.1, 1))
    ax = _panel(fig, g[1, 0], "a", "Component settings")
    xx, yy = np.meshgrid(np.arange(matrix.shape[1]), np.arange(matrix.shape[0]))
    ax.scatter(xx.ravel(), yy.ravel(), c=np.where(matrix.ravel(), "#286c80", "#e0e5e9"), s=32)
    ax.set(xticks=np.arange(matrix.shape[1]), xticklabels=data["components"],
           yticks=np.arange(len(variants)), yticklabels=variants,
           ylim=(len(variants)-.5, -.5), xlim=(-.5, matrix.shape[1]-.5))
    ax.tick_params(axis="x", labelrotation=25); p.clean_axes(ax, grid=None)
    ax.spines[["left", "bottom"]].set_visible(False)
    ax = _panel(fig, g[1, 1], "b", "Task score")
    colors = ["#aab4bd"]*(len(variants)-1) + [list(enc.values())[-1]["color"]]
    p.comparison_intervals(ax, variants, data["score"]["mean"],
                           lower=data["score"]["lower"], upper=data["score"]["upper"],
                           runs=data["score"]["runs"], colors=colors, xlabel=data["score"]["unit"], seed=9)
    ax.set_yticklabels([])
    ax.set_ylim(len(variants)-.5, -.5)
    effect = data["effects"]
    ax = _panel(fig, g[1, 2], "c", "Change from full")
    p.forest_intervals(ax, effect["labels"], effect["mean"], effect["lower"], effect["upper"],
                       colors=colors[:-1], xlabel=effect["unit"])
    ax.set_ylim(len(variants)-.5, -.5)
    _heatmap(fig, _panel(fig, g[2, :2], "d", "Pairwise component interaction"), data["interactions"])
    _lines(_panel(fig, g[2, 2], "e", "Training trajectory"), data["learning_curve"], enc)
    return fig


def scaling_robustness(data, enc, width, height):
    blocks = data["panels"]
    if len(blocks) != 6:
        raise ValueError("scaling_robustness requires six supplied curve panels")
    fig, g = _figure(data, enc, width, height)
    for i, block in enumerate(blocks):
        _lines(_panel(fig, g[1+i//3, i%3], chr(97+i), block["title"]), block, enc)
    return fig


def representation_diagnostics(data, enc, width, height):
    attention = np.asarray(data["attention"]["values"], dtype=float)
    correlation = np.asarray(data["correlation"]["values"], dtype=float)
    if attention.ndim != 2 or not np.isfinite(attention).all() or (attention < 0).any() or (attention > 1).any():
        raise ValueError("Attention weights must be finite values in [0, 1]")
    if data["correlation"]["rows"] != data["correlation"]["columns"] or correlation.ndim != 2 or correlation.shape[0] != correlation.shape[1] or not np.allclose(correlation, correlation.T, equal_nan=True) or (np.abs(correlation[np.isfinite(correlation)]) > 1).any():
        raise ValueError("Pearson correlation must be a symmetric square matrix in [-1, 1]")
    block = data["embedding"]
    group_enc = p.entity_encoding(block["order"], palette=data.get("group_palette", "tol_muted"))
    fig, g = _figure(data, group_enc, width, height)
    ax = _panel(fig, g[1, :2], "a", "Representation geometry")
    p.embedding_scatter(ax, block["coordinates"], block["groups"], order=block["order"],
                        colors={key: value["color"] for key, value in group_enc.items()}, size=10)
    ax.set(xlabel="Projection 1", ylabel="Projection 2")
    _comparison(_panel(fig, g[1, 2], "b", "Linear-probe score"), data["performance"], enc)
    _heatmap(fig, _panel(fig, g[2, 0], "c", "Temporal attention"), data["attention"])
    _heatmap(fig, _panel(fig, g[2, 1], "d", "Feature correlation"), data["correlation"])
    ax = _panel(fig, g[2, 2], "e", "Local agreement")
    p.paired_distribution(ax, data["samples"], data["methods"], colors=_colors(data["methods"], enc),
                           ylabel=data["sample_unit"], seed=23)
    ax.set_xticks(range(len(data["methods"])), [name.replace(" ", "\n", 1) for name in data["methods"]])
    return fig


def biological_atlas(data, enc, width, height):
    block = data["embedding"]
    groups = block["order"]
    group_enc = p.entity_encoding(groups, palette=data.get("group_palette", "tol_muted"))
    group_colors = {key: value["color"] for key, value in group_enc.items()}
    fig, g = _figure(data, group_enc, width, height, ratios=(1.2, 1, 1))
    ax = _panel(fig, g[1, 0], "a", "Cell-state landscape")
    p.embedding_scatter(ax, block["coordinates"], block["groups"], order=groups, colors=group_colors, size=8)
    ax.set(xlabel="Projection 1", ylabel="Projection 2")
    _heatmap(fig, _panel(fig, g[1, 1:], "b", "Gene expression by group"), data["expression"])
    ax = _panel(fig, g[2, 0], "c", "Effect-size screening")
    v = data["volcano"]
    p.volcano(ax, v["effect"], v["probability"], labels=v["labels"],
              statistic=v["statistic"], annotate_indices=v.get("annotate_indices", []),
              effect_threshold=v["effect_threshold"], probability_threshold=v["probability_threshold"], zero_floor=v.get("zero_floor"))
    ax = _panel(fig, g[2, 1:], "d", "Pathway activity and prevalence")
    block = data["dot_matrix"]
    dots = p.dot_matrix(ax, block["values"], block["sizes"], block["rows"], block["columns"],
                        cmap="viridis", vmin=block["vmin"], vmax=block["vmax"],
                        size_max=100, size_scale=90)
    bar = fig.colorbar(dots, ax=ax, fraction=.035, pad=.025)
    bar.solids.set_rasterized(False)
    bar.set_label(block["color_unit"])
    # The marker area encodes percentage; show actual reference sizes explicitly.
    handles = [ax.scatter([], [], s=value/100*90, facecolor="#586976", edgecolor="none",
                          label=f"{value}%") for value in [25, 50, 100]]
    ax.legend(handles=handles, title=block["size_unit"], frameon=False, ncol=3,
              loc="upper center", bbox_to_anchor=(.5, -.18), handletextpad=.25, columnspacing=.8)
    return fig


def paired_effects(data, enc, width, height):
    paired = data["paired"]
    if len(paired["values"]) != 2 or len(paired["labels"]) != 2:
        raise ValueError("Paired differences require exactly two matched groups")
    before, after = [_vector(row, "paired values") for row in paired["values"]]
    differences = _vector(data["differences"], "differences")
    if len(before) != len(after) or len(differences) != len(before) or not np.allclose(differences, after-before):
        raise ValueError("Differences must equal the supplied second group minus the first, in matched order")
    fig, g = _figure(data, enc, width, height)
    ax = _panel(fig, g[1, :2], "a", "Within-subject change")
    p.paired_distribution(ax, paired["values"], paired["labels"],
                           colors=_colors(paired["labels"], enc), paired=True, seed=4,
                           ylabel=paired["unit"], violin=False)
    ax = _panel(fig, g[1, 2], "b", "Paired differences")
    p.paired_distribution(ax, [data["differences"]], [f"{paired['labels'][1]} − {paired['labels'][0]}"],
                           colors=[list(enc.values())[-1]["color"]], ylabel=data["difference_unit"], seed=4)
    ax.axhline(0, color="#8b969f", linestyle="--", linewidth=.7)
    effect = data["subgroups"]
    p.forest_intervals(_panel(fig, g[2, :2], "c", "Subgroup effect estimates"),
                       effect["labels"], effect["mean"], effect["lower"], effect["upper"],
                       colors=[list(enc.values())[-1]["color"]]*len(effect["labels"]), xlabel=effect["unit"])
    _lines(_panel(fig, g[2, 2], "d", "Temporal response"), data["response_curve"], enc)
    return fig


def calibration_errors(data, enc, width, height):
    if not data["calibration"] or not data["errors"]:
        raise ValueError("Calibration and error panels need observed series")
    confusion = np.asarray(data["confusion"]["values"], dtype=float)
    if not np.isfinite(confusion).all() or (confusion < 0).any() or (confusion != np.floor(confusion)).any():
        raise ValueError("Confusion samples must be nonnegative integer counts")
    fig, g = _figure(data, enc, width, height)
    ax = _panel(fig, g[1, 0], "a", "Reliability")
    for block in data["calibration"]:
        result = p.calibration(ax, block["confidence"], block["accuracy"], block["counts"],
                               edges=block["edges"], color=enc[block["method"]]["color"], label=block["method"])
        result["line"].set_marker(enc[block["method"]]["marker"])
    ax = _panel(fig, g[1, 1], "b", "Confidence counts")
    block = data["confidence_histogram"]
    edges = _vector(block["edges"], "histogram edges")
    counts = _vector(block["counts"], "histogram counts", nonnegative=True)
    if len(edges) != len(counts)+1 or (np.diff(edges) <= 0).any() or edges[0] < 0 or edges[-1] > 1 or (counts != np.floor(counts)).any():
        raise ValueError("histogram edges must increase and bracket all supplied counts")
    ax.bar(edges[:-1], counts, width=np.diff(edges)*.92, align="edge", color=list(enc.values())[-1]["color"], alpha=.75)
    ax.set(xlabel="Confidence", ylabel="Samples"); p.clean_axes(ax)
    ax = _panel(fig, g[1, 2], "c", "Residual structure")
    block = data["residuals"]
    x = _vector(block["prediction"], "predictions"); y = _vector(block["residual"], "residuals")
    if len(x) != len(y):
        raise ValueError("Predictions and residuals must have matching lengths")
    ax.scatter(x, y, s=8, color=list(enc.values())[-1]["color"], alpha=.4, linewidths=0)
    ax.axhline(0, color="#747f89", linestyle="--", linewidth=.7)
    ax.set(xlabel=block["xlabel"], ylabel=block["ylabel"]); p.clean_axes(ax)
    confusion_ax = _panel(fig, g[2, 0], "d", "Confusion structure")
    _heatmap(fig, confusion_ax, data["confusion"])
    confusion_ax.set(xlabel=data["confusion"].get("xlabel", "Predicted class"), ylabel=data["confusion"].get("ylabel", "Actual class"))
    ax = _panel(fig, g[2, 1], "e", "Error distribution")
    for block in data["errors"]:
        vals = np.sort(_vector(block["values"], "absolute errors", nonnegative=True))
        key = block["method"]
        ax.step(vals, np.arange(1, len(vals)+1)/len(vals), where="post",
                color=enc[key]["color"], label=key, linewidth=1.3)
    ax.set(xlabel=data["error_unit"], ylabel="Cumulative fraction", ylim=(0, 1)); p.clean_axes(ax)
    ax = _panel(fig, g[2, 2], "f", "Failure categories")
    block = data["failure_counts"]
    vals = _vector(block["counts"], "failure counts", nonnegative=True)
    if len(vals) != len(block["labels"]) or (vals != np.floor(vals)).any():
        raise ValueError("Failure labels and counts must align")
    ax.barh(block["labels"], vals, color="#8b9daa", height=.55)
    ax.invert_yaxis(); ax.set_xlabel("Samples"); p.clean_axes(ax, grid="x")
    return fig


def sensitivity_dynamics(data, enc, width, height):
    """Four linked analyses, or either two-panel pair at a paper-friendly size."""
    pair = data.get("panel_pair", "all")
    if pair not in ("all", "sensitivity", "dynamics"):
        raise ValueError("panel_pair must be all, sensitivity or dynamics")
    fig = p.new_figure(width, height if pair == "all" else height * .56)
    fig.set_layout_engine("constrained", w_pad=.04, h_pad=.055, wspace=.10,
                          hspace=.10, rect=(0, .04, 1, .95))
    grid = fig.add_gridspec(2 if pair == "all" else 1, 2)
    if data.get("_meta", {}).get("synthetic"):
        fig.text(.995, .008, "Simulated data · layout demonstration", ha="right", va="bottom", fontsize=8, color="#69737d")
    if pair in ("all", "sensitivity"):
        block = data["density"]
        ax = _panel(fig, grid[0, 0], "a", block.get("title", "State-space exposure"))
        density = p.density_map(ax, block["x"], block["y"], gridsize=block.get("gridsize", 30),
                                xscale=block.get("xscale", "linear"), yscale=block.get("yscale", "log"),
                                cmap=block.get("cmap", "viridis"), xlabel=block["xlabel"], ylabel=block["ylabel"])
        bar = fig.colorbar(density, ax=ax, fraction=.04, pad=.035)
        bar.solids.set_rasterized(False)
        bar.set_label("Samples per bin")
        if "threshold" in block:
            threshold = float(block["threshold"])
            if not np.isfinite(threshold) or (block.get("yscale", "log") == "log" and threshold <= 0):
                raise ValueError("Density threshold must be finite and valid for its axis")
            observed = _vector(block["y"], "density y")
            share = 100 * float(np.mean(observed <= threshold))
            ax.axhline(threshold, linestyle="--", color="#ce6a36", linewidth=.9)
            ax.text(.97, .045, f"{share:.1f}% at or below {threshold:g}", transform=ax.transAxes,
                    ha="right", va="bottom", fontsize=8, color="#9d4d24",
                    bbox={"facecolor":"white", "edgecolor":"none", "alpha":.88, "pad":2})
        block = data["sensitivity"]
        ax = _panel(fig, grid[0, 1], "b", block.get("title", "Perturbation by group"))
        p.binned_summary(ax, block["samples"], block["labels"], color="#80b5ca",
                         line_color="#d86a38", quantile=block.get("quantile", .95), ylabel=block["ylabel"])
        ax.set_xlabel(block["xlabel"])
    if pair in ("all", "dynamics"):
        row = 1 if pair == "all" else 0
        block = data["dynamics"]
        for series in block["series"]:
            for field in ("y", "lower", "upper"):
                if series.get(field) is not None:
                    values = _vector(series[field], "state share")
                    if (values < 0).any() or (values > 100).any():
                        raise ValueError("State shares and their bounds must be percentages in [0, 100]")
        ax = _panel(fig, grid[row, 0], "c" if pair == "all" else "a", block.get("title", "Regime evolution"))
        _lines(ax, block, enc)
        ax.set_ylim(0, 100)
        if block.get("fill_method") is not None:
            matches = [s for s in block["series"] if s["method"] == block["fill_method"]]
            if len(matches) != 1:
                raise ValueError("fill_method must identify one supplied state series")
            selected = matches[0]
            ax.fill_between(block["x"], 0, selected["y"], alpha=.10, color=enc[selected["method"]]["color"])
        ax.legend(loc="lower right", fontsize=p.mpl.rcParams["font.size"]-1, handlelength=1.5)
        block = data["categories"]
        bar_values = _vector(block["bars"], "category percentages")
        series = []
        for entry in block["series"]:
            values = _vector(entry["values"], "category percentages")
            if (values < 0).any() or (values > 100).any():
                raise ValueError("Category shares must be percentages in [0, 100]")
            code = enc[entry["method"]]
            series.append({"label":entry["method"], "values":entry["values"], **code})
        if (bar_values < 0).any() or (bar_values > 100).any():
            raise ValueError("Category shares must be percentages in [0, 100]")
        ax = _panel(fig, grid[row, 1], "d" if pair == "all" else "b", block.get("title", "Variation across edits"))
        p.category_comparison(ax, block["labels"], block["bars"], series,
                              bar_label=block["bar_method"], bar_color=enc[block["bar_method"]]["color"], ylabel="Share (%)")
        ax.set_ylim(0, 110)
        ax.set_xlabel(block["xlabel"])
        ax.legend(loc="upper center", ncol=1, fontsize=p.mpl.rcParams["font.size"]-1)
    return fig


BUILDERS = {name: globals()[name] for name in CATALOG}


def render_template(name, data, *, palette="ccfa", font="serif", font_size=8.5,
                    width_mm=183, height_mm=None):
    """Render real supplied data; this function never fills missing data with demos."""
    if name not in BUILDERS:
        raise ValueError(f"Unknown template {name!r}; choose {', '.join(CATALOG)}")
    if palette not in PALETTES:
        raise ValueError(f"Unknown palette {palette!r}")
    if not isinstance(data, dict):
        raise ValueError("Template data must be a JSON object")
    with p.paper_style(font=font, font_size=font_size):
        previous_figures = set(plt.get_fignums())
        try:
            enc = _encoding(data, palette)
            fig = BUILDERS[name](data, enc, width_mm, CATALOG[name][1] if height_mm is None else height_mm)
        except KeyError as error:
            raise ValueError(f"{name}: missing required data field {error.args[0]!r}; see the demo schema") from error
        except Exception:
            for number in set(plt.get_fignums()) - previous_figures:
                plt.close(number)
            raise
        finally:
            if 'fig' not in locals():
                for number in set(plt.get_fignums()) - previous_figures:
                    plt.close(number)
        return fig


def _interval_block(rng, methods, means, *, unit="Score (%)", n=8):
    runs = [rng.normal(value, .8, n).tolist() for value in means]
    center = np.mean(runs, axis=1); spread = np.std(runs, axis=1, ddof=1)
    return {"labels":methods, "mean":center.tolist(), "lower":(center-spread).tolist(),
            "upper":(center+spread).tolist(), "runs":runs, "xlabel":unit,
            "uncertainty":"mean ± 1 sample SD", "n_runs":n}


def _curve(methods, x, ys, xlabel, ylabel, *, spread=.8, title=None):
    block = {"x":np.asarray(x, dtype=float).tolist(), "xlabel":xlabel, "ylabel":ylabel,
             "uncertainty":"illustrative mean ± 1 SD", "series":[]}
    if title: block["title"] = title
    for method, yy in zip(methods, ys):
        y = np.asarray(yy, dtype=float)
        block["series"].append({"method":method, "y":y.tolist(),
                                 "lower":(y-spread).tolist(), "upper":(y+spread).tolist()})
    return block


def _matrix(values, rows, columns, unit, **kwargs):
    return {"values":np.asarray(values).tolist(), "rows":list(rows), "columns":list(columns), "unit":unit, **kwargs}


def demo_data(seed=17):
    """Generate explicit synthetic fixtures, never used by real-data rendering."""
    rng = np.random.default_rng(seed)
    methods = ["Baseline", "Memory bank", "Sparse read", "Object slots"]
    base = {"methods":methods, "_meta":{"synthetic":True, "seed":seed,
            "note":"Random illustrative data; not results from any cited paper."}}
    x = np.array([1, 2, 4, 8, 16, 32])
    means = [70, 74, 77, 81]
    performance = _interval_block(rng, methods, means)
    tradeoff = {"labels":methods, "x":[2.4, 6.1, 4.2, 5.2], "y":means,
                "xlabel":"Peak memory (GB)", "ylabel":"Accuracy (%)", "x_direction":"min", "y_direction":"max"}
    datasets = ["Spatial", "Temporal", "Objects", "Events", "Long-range", "Composition"]
    benchmark = np.array(means)[:,None] + rng.normal(0, 2, (4, 6))
    examples = {}
    examples["mechanism_overview"] = {**base,
        "mechanism":{"stages":["Frames", "Local tokens", "Object states"], "note":"Current observations → compact state → persistent scene memory"},
        "memory_curve":_curve(methods, x, [1+.4*x, 1+.3*x, 1+.13*x, 1.5+.035*x], "Windows", "Memory (GB)", spread=.12),
        "performance":performance, "tradeoff":tradeoff,
        "gain_matrix":_matrix(rng.uniform(.1, 6.9, (4, 4)), ["Near", "Medium", "Far", "Very far"],
                               ["Spatial", "Time", "Object", "Event"], "Gain (points)", cmap="YlGnBu", vmin=0, vmax=7)}
    samples = [rng.normal(m, 3, 35).tolist() for m in means]
    sample_curve = _curve(methods, x*100, [52+i*2+(5+i)*np.log2(x+1) for i in range(4)], "Training samples", "Accuracy (%)")
    examples["benchmark_atlas"] = {**base, "benchmark":_matrix(benchmark, methods, datasets, "Accuracy (%)", cmap="YlGnBu", annotate=True, vmin=60, vmax=90),
        "performance":performance, "tradeoff":tradeoff, "samples":samples, "sample_unit":"Score (%)", "sample_curve":sample_curve}
    variants = ["Base", "+ States", "+ Time", "+ Routing", "+ Updates", "Full"]
    score = _interval_block(rng, variants, [69, 72, 73, 75, 78, 81]);score["unit"]="Score (%)"
    differences = np.asarray(score["runs"][:-1])-np.asarray(score["runs"][-1])
    effect_mean = differences.mean(axis=1);effect_sd=differences.std(axis=1, ddof=1)
    interaction = rng.uniform(-.5, 2.2, (4,4));interaction=(interaction+interaction.T)/2;np.fill_diagonal(interaction, 0)
    examples["ablation_interactions"] = {**base, "variants":variants, "components":["State", "Time", "Route", "Update"],
        "enabled":[[0,0,0,0],[1,0,0,0],[1,1,0,0],[1,1,1,0],[1,0,1,1],[1,1,1,1]], "score":score,
        "effects":{"labels":variants[:-1], "mean":effect_mean.tolist(), "lower":(effect_mean-effect_sd).tolist(),
                   "upper":(effect_mean+effect_sd).tolist(), "unit":"Difference (points)", "uncertainty":"mean ± 1 sample SD of paired seed differences"},
        "interactions":_matrix(interaction, ["State","Time","Route","Update"], ["State","Time","Route","Update"],
                               "Interaction (points)", cmap="RdBu_r", vmin=-2.5, vmax=2.5, center=0, annotate=True),
        "learning_curve":_curve(methods, [0,10,20,30,40,50], [50+i*2+(20+i*2)*(1-np.exp(-np.arange(6)/1.6)) for i in range(4)], "Epoch", "Score (%)")}
    xx=np.linspace(0, 1, 6)
    panels=[sample_curve,
        _curve(methods, x, [45+i*3+(6+i*.7)*np.log2(x+1) for i in range(4)], "Context (k tokens)", "Score (%)"),
        _curve(methods, xx, [82+i*2-(22-i*4)*xx for i in range(4)], "Noise level", "Accuracy (%)"),
        _curve(methods, xx, [83+i*2-(25-i*4)*xx for i in range(4)], "Missing fraction", "Accuracy (%)"),
        _curve(methods, x, [.7+(1.4-i*.25)*x for i in range(4)], "Sequence (k frames)", "Latency (ms)", spread=.2),
        _curve(methods, [8,16,32,64,128,256], [66+i*2+10*(1-np.exp(-np.arange(6)/2)) for i in range(4)], "Memory slots", "Score (%)")]
    for title, block in zip(["Data scaling","Context scaling","Noise robustness","Missing observations","Inference cost","Capacity sensitivity"],panels):block["title"]=title
    examples["scaling_robustness"]={**base,"panels":panels}
    group_order=["State A","State B","State C","State D","State E"]
    centers=np.array([[-2,0],[0,2.3],[2.2,.3],[.5,-2.1],[-2.3,-2]])
    coordinates=np.concatenate([rng.normal(c, [.55,.42], (85,2)) for c in centers])
    groups=[label for label in group_order for _ in range(85)]
    embedding={"coordinates":coordinates.tolist(),"groups":groups,"order":group_order,"method":"Synthetic 2D coordinates, not a fitted UMAP/t-SNE"}
    attention=np.exp(-np.abs(np.arange(8)[:,None]-np.arange(8)[None,:])/1.7);attention/=attention.sum(axis=1,keepdims=True)
    features=rng.normal(size=(150,6));features[:,1]+=.8*features[:,0];features[:,4]-=.7*features[:,2]
    corr=np.corrcoef(features,rowvar=False)
    examples["representation_diagnostics"]={**base,"embedding":embedding,"performance":performance,
        "attention":_matrix(attention,[str(i) for i in range(1,9)],[str(i) for i in range(1,9)],"Attention weight",cmap="magma",vmin=0,vmax=1),
        "correlation":_matrix(corr,["F1","F2","F3","F4","F5","F6"],["F1","F2","F3","F4","F5","F6"],"Pearson r",cmap="RdBu_r",vmin=-1,vmax=1,center=0),
        "samples":[rng.beta(5+i,3,30).tolist() for i in range(4)],"sample_unit":"Neighbor agreement"}
    gene_labels=[f"Gene {i:02d}" for i in range(1,13)]
    expression=rng.normal(0,.8,(12,5));expression[np.arange(12),np.arange(12)%5]+=2.3
    expression=(expression-expression.mean(axis=1,keepdims=True))/expression.std(axis=1,keepdims=True)
    effects=rng.normal(0,.75,480);effects[:30]+=2;effects[30:60]-=2
    stderr=rng.uniform(.2,.6,len(effects));pv=np.array([erfc(abs(z)/sqrt(2)) for z in effects/stderr])
    order=np.argsort(pv);q=np.empty_like(pv);q[order]=np.minimum(1,np.minimum.accumulate((pv[order]*len(pv)/np.arange(1,len(pv)+1))[::-1])[::-1])
    examples["biological_atlas"]={**base,"embedding":embedding,
        "expression":_matrix(expression,gene_labels,group_order,"Row z-score",cmap="RdBu_r",vmin=-2.5,vmax=2.5,center=0),
        "volcano":{"effect":effects.tolist(),"probability":q.tolist(),"labels":[f"G{i}" for i in range(len(q))],"statistic":"q",
                   "effect_threshold":1,"probability_threshold":.05,"annotate_indices":np.argsort(q)[:3].tolist()},
        "dot_matrix":{"values":rng.uniform(0,2,(6,5)).tolist(),"sizes":rng.uniform(10,95,(6,5)).tolist(),
                      "rows":["Response","Metabolism","Transport","Repair","Signaling","Cycle"],"columns":group_order,
                      "vmin":0,"vmax":2,"color_unit":"Mean activity","size_unit":"Positive cells"}}
    before=rng.normal(55,8,32);after=before+rng.normal(8,5,32);difference=after-before
    subgroup_labels=["All", "Group 1", "Group 2", "Group 3", "Group 4"]
    split=[difference]+list(np.array_split(difference,4));ests=[];los=[];his=[]
    for vals in split:
        boot=rng.choice(vals,size=(1000,len(vals)),replace=True).mean(axis=1)
        ests.append(float(np.mean(vals)));lo,hi=np.percentile(boot,[2.5,97.5]);los.append(float(lo));his.append(float(hi))
    pair_methods=["Before","After"]
    examples["paired_effects"]={**base,"methods":pair_methods,"paired":{"values":[before.tolist(),after.tolist()],"labels":pair_methods,"unit":"Response (a.u.)"},
        "differences":difference.tolist(),"difference_unit":"Change (a.u.)",
        "subgroups":{"labels":subgroup_labels,"mean":ests,"lower":los,"upper":his,"unit":"Mean change (bootstrap 95% CI)"},
        "response_curve":_curve(pair_methods,[0,1,2,3,4,5],[[50,52,53,54,55,56],[50,55,60,64,67,69]],"Time (days)","Response (a.u.)",spread=1.4)}
    edges=np.linspace(0,1,9);confidence=(edges[:-1]+edges[1:])/2
    cals=[]
    for i,key in enumerate(methods):
        cals.append({"method":key,"confidence":confidence.tolist(),"accuracy":(confidence**(1.9-.28*i)).tolist(),
                     "counts":rng.integers(30,150,8).tolist(),"edges":edges.tolist()})
    prediction=rng.uniform(0,10,250);residual=rng.normal(0,.5+.045*prediction,250)
    confusion=rng.integers(0,12,(5,5));np.fill_diagonal(confusion,rng.integers(55,85,5))
    examples["calibration_errors"]={**base,"calibration":cals,
        "confidence_histogram":{"edges":edges.tolist(),"counts":cals[-1]["counts"]},
        "residuals":{"prediction":prediction.tolist(),"residual":residual.tolist(),"xlabel":"Prediction (a.u.)","ylabel":"Residual (a.u.)"},
        "confusion":_matrix(confusion,["A","B","C","D","E"],["A","B","C","D","E"],"Samples",cmap="Blues",annotate=True,fmt=".0f",vmin=0,vmax=90),
        "errors":[{"method":key,"values":abs(rng.normal(0,1.6-.25*i,150)).tolist()} for i,key in enumerate(methods)],
        "error_unit":"Absolute error (a.u.)","failure_counts":{"labels":["Temporal","Identity","Spatial","Other"],"counts":[42,31,18,9]}}
    angle = rng.beta(2.2, 2.0, 7000) * 120
    distance = 10 ** (-2 + .032 * angle + rng.normal(0, .35, len(angle)))
    step = np.arange(0, 33, 2)
    corridor = 100 / (1 + np.exp(-(step-21)/2.4))
    drift = 94 / (1 + np.exp(-(step-20.5)/2.8))
    alignment = 14 + 86 * (1-np.exp(-step/4.2))
    states = ["Corridor occupancy", "High-drift share", "Near-aligned state"]
    examples["sensitivity_dynamics"] = {**base, "methods":states,
        "density":{"x":angle.tolist(),"y":distance.tolist(),"yscale":"log", "threshold":.25,
                   "xlabel":"Branch separation (degrees)", "ylabel":"State distance"},
        "sensitivity":{"samples":[rng.lognormal(-2+i*.47,.65,80).tolist() for i in range(4)],
                       "labels":["Low","Medium","High","Highest"], "quantile":.95,
                       "xlabel":"Predicted sensitivity group", "ylabel":"Feature displacement"},
        "dynamics":{"x":step.tolist(),"series":[{"method":key,"y":value.tolist()} for key,value in zip(states,[corridor,drift,alignment])],
                    "xlabel":"Integration step", "ylabel":"State share (%)", "fill_method":states[0],
                    "note":"Three overlapping state criteria, not a mutually exclusive partition."},
        "categories":{"labels":["Object","Action","Color","Material","Layout","Style"],
                      "bars":[34,32,29,38,35,31], "bar_method":states[0], "xlabel":"Editing type",
                      "series":[{"method":states[1],"values":[51,55,50,48,57,53]},
                                {"method":states[2],"values":[72,78,74,71,83,77]}]}}
    # JSON-compatible serialization rejects nonfinite fixture values.
    json.dumps(examples,allow_nan=False)
    return examples


def palette_atlas(*, font="serif", keys=None):
    keys = keys or ["ccfa","npg","aaas","nejm","lancet","jco","tol_bright","tol_muted","ccfa_ceramic","ccfa_orchid","ccfa_arctic","ccfa_wine"]
    with p.paper_style(font=font,font_size=9):
        fig=p.new_figure(width_mm=183,height_mm=112)
        ax=fig.add_axes([.16,.12,.81,.80]);ax.axis("off")
        ax.set(xlim=(0,10),ylim=(-.6,len(keys)-.1))
        for i,key in enumerate(keys):
            y=len(keys)-1-i;ax.text(-.15,y+.19,key,ha="right",va="center",fontsize=9)
            for j,color in enumerate(PALETTES[key]):
                ax.add_patch(FancyBboxPatch((j+.025,y),.9,.42,boxstyle="round,pad=.02,rounding_size=.05",facecolor=color,edgecolor="none"))
        fig.text(.985,.025,"Palette preview · journal-inspired names are not venue requirements",ha="right",fontsize=8,color="#64717e")
        return fig


def _caption_notes(value, path=""):
    notes = {}
    if isinstance(value, dict):
        for key, item in value.items():
            location = f"{path}.{key}" if path else key
            if key in ("uncertainty", "n_runs", "statistic", "method", "note") and not isinstance(item, (list, dict)):
                notes[location] = item
            elif isinstance(item, (list, dict)):
                notes.update(_caption_notes(item, location))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            if isinstance(item, (list, dict)):
                notes.update(_caption_notes(item, f"{path}[{index}]"))
    return notes


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list",action="store_true")
    choice=parser.add_mutually_exclusive_group()
    choice.add_argument("--demo",choices=["all",*CATALOG])
    choice.add_argument("--data",type=Path)
    parser.add_argument("--template",choices=CATALOG)
    parser.add_argument("--out",type=Path)
    parser.add_argument("--palette",choices=sorted(PALETTES),default="ccfa")
    parser.add_argument("--palette-showcase",action="store_true",help="Explicitly use different palettes for independent demo examples only")
    parser.add_argument("--panel-pair", choices=["all", "sensitivity", "dynamics"], default="all", help="Show either two-panel pair of sensitivity_dynamics")
    parser.add_argument("--font",choices=["serif","sans","comic"],default="serif")
    parser.add_argument("--font-size",type=float,default=8.5)
    parser.add_argument("--width-mm",type=float,default=183)
    parser.add_argument("--seed",type=int,default=17)
    parser.add_argument("--formats",nargs="+",choices=["svg","pdf","png"],default=["svg","pdf","png"])
    parser.add_argument("--dpi",type=int,default=220)
    args=parser.parse_args(argv)
    if args.list:
        print(json.dumps({k:{"purpose":v[0],"height_mm":v[1]} for k,v in CATALOG.items()},indent=2));return 0
    if not (args.demo or args.data) or args.out is None:
        parser.error("Choose --demo or --data, and provide one task-owned --out directory")
    if args.palette_showcase and not args.demo:
        parser.error("--palette-showcase applies only to independent synthetic examples")
    if args.data and not args.template:
        parser.error("--data requires --template")
    if args.data and args.data.resolve() == (args.out/"manifest.json").resolve():
        parser.error("The manifest path must not overwrite source data")
    if args.panel_pair != "all" and (args.template or args.demo) != "sensitivity_dynamics":
        parser.error("--panel-pair requires the sensitivity_dynamics template")
    if args.demo:
        all_data=demo_data(args.seed);names=list(CATALOG) if args.demo=="all" else [args.demo]
        source=args.out/"source"/"demo-data.json";source.parent.mkdir(parents=True,exist_ok=True)
        source.write_text(json.dumps({k:all_data[k] for k in names},ensure_ascii=False,allow_nan=False,indent=2)+"\n",encoding="utf-8")
    else:
        raw=json.loads(args.data.read_text(encoding="utf-8-sig"));names=[args.template]
        all_data={args.template:raw[args.template] if args.template in raw else raw};source=args.data
    manifest={"synthetic":bool(args.demo),"seed":args.seed if args.demo else None,
              "font":args.font,"font_size_pt":args.font_size,"width_mm":args.width_mm,
              "data_file":source.relative_to(args.out).as_posix() if args.demo else str(source.resolve()),
              "independent_palette_examples":args.palette_showcase,"panel_pair":args.panel_pair,"figures":{}}
    for name in names:
        palette=CATALOG[name][2] if args.palette_showcase else args.palette
        plot_data = dict(all_data[name])
        if args.panel_pair != "all": plot_data["panel_pair"] = args.panel_pair
        fig=render_template(name,plot_data,palette=palette,font=args.font,font_size=args.font_size,width_mm=args.width_mm)
        try:
            paths=p.save_figure(fig,args.out/"figures"/name,formats=tuple(args.formats),dpi=args.dpi,protected_paths=(source,))
            manifest["figures"][name]={"palette":palette,"exports":{k:v.relative_to(args.out).as_posix() for k,v in paths.items()},
                "caption_notes":_caption_notes(all_data[name]),"qa":p.audit_figure(fig)}
        finally:
            plt.close(fig)
    if args.demo:
        fig=palette_atlas(font=args.font)
        try:
            p.save_figure(fig,args.out/"figures"/"palette_atlas",formats=tuple(args.formats),dpi=args.dpi)
        finally:plt.close(fig)
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,allow_nan=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"figures":len(names),"synthetic":bool(args.demo),"manifest":str(args.out/"manifest.json")},ensure_ascii=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
