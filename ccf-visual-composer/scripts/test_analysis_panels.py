#!/usr/bin/env python3
"""Data and export regressions for the optional NumPy/Matplotlib panel library.

Run from any directory. Test artifacts live in the maintenance build directory
and each test removes only its own newly created temporary directory.
"""
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors, font_manager
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ccf-visual-composer/resources/python"))
import ccfa_analysis_panels as panels

BUILD = ROOT / "ccfa-workfiles/skill-maintenance/analytical-figures/build"
NS = {"s": "http://www.w3.org/2000/svg"}


class AnalysisPanelTests(unittest.TestCase):
    def setUp(self):
        BUILD.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="panel-test-", dir=BUILD)
        self.folder = Path(self.temporary.name).resolve()
        self.assertEqual(self.folder.parent, BUILD.resolve())
        self.style = panels.paper_style()
        self.style.__enter__()
        self.fig = panels.new_figure(120, 80)
        self.ax = self.fig.add_subplot()

    def tearDown(self):
        plt.close("all")
        self.style.__exit__(None, None, None)
        # The directory was created here and its resolved parent checked above.
        self.temporary.cleanup()

    def test_known_pareto_frontier_excludes_dominated_points_and_keeps_ties(self):
        x, y = [3, 1, 2, 2, 4], [3, 1, 2, 2, 2]
        result = panels.pareto_scatter(self.ax, x, y, list("abcde"), annotate=False)
        np.testing.assert_array_equal(result["frontier"], [True, True, True, True, False])
        np.testing.assert_array_equal(self.ax.lines[0].get_xdata(), [1, 2, 3])
        np.testing.assert_array_equal(self.ax.lines[0].get_ydata(), [1, 2, 3])
        np.testing.assert_array_equal(result["scatter"].get_offsets(), np.column_stack([x, y]))

    def test_pareto_respects_all_four_optimization_directions(self):
        for xd, yd, expected in (("min", "min", 0), ("min", "max", 1),
                                 ("max", "min", 2), ("max", "max", 3)):
            with self.subTest(x_direction=xd, y_direction=yd):
                mask = panels.pareto_mask([0, 0, 1, 1], [0, 1, 0, 1],
                                          x_direction=xd, y_direction=yd)
                self.assertEqual(np.flatnonzero(mask).tolist(), [expected])
        with self.assertRaises(ValueError): panels.pareto_mask([1], [2], x_direction="low")

    def test_supplied_estimates_and_intervals_preserve_zero_and_negative_values(self):
        result = panels.comparison_intervals(self.ax, ["A", "B"], [-2, 0],
                                             lower=[-3, -1], upper=[-1, 2])
        self.assertEqual([float(p.get_offsets()[0, 0]) for p in result["points"]], [-2, 0])
        np.testing.assert_array_equal(result["intervals"][0].get_xdata(), [-3, -1])
        np.testing.assert_array_equal(result["intervals"][1].get_xdata(), [-1, 2])
        self.assertEqual([t.get_text() for t in self.ax.get_yticklabels()], ["A", "B"])

    def test_jitter_is_reproducible_without_mutating_global_numpy_rng(self):
        before = np.random.get_state()
        for ax in (self.ax, self.fig.add_axes([0.2, 0.2, 0.5, 0.5])):
            panels.comparison_intervals(ax, ["A"], [2], runs=[[1, 2, 3]], seed=73)
        np.testing.assert_array_equal(self.fig.axes[0].collections[0].get_offsets(),
                                      self.fig.axes[1].collections[0].get_offsets())
        after = np.random.get_state()
        self.assertEqual(before[0], after[0]); np.testing.assert_array_equal(before[1], after[1])
        self.assertEqual(before[2:], after[2:])

    def test_invalid_intervals_are_rejected_instead_of_clamped(self):
        for low, high in (([1], [3]), ([-1], [-1]), ([-1], None), ([np.nan], [2])):
            with self.subTest(lower=low, upper=high), self.assertRaises(ValueError):
                panels.comparison_intervals(self.ax, ["A"], [0], lower=low, upper=high)

    def test_line_band_uses_supplied_bounds_and_never_infers_uncertainty(self):
        line = panels.line_band(self.ax, [0, 1, 2], [-2, 0, 1])
        self.assertEqual(len(self.ax.collections), 0)
        np.testing.assert_array_equal(line.get_ydata(), [-2, 0, 1])
        for x, y in (([1, 0], [1, 2]), ([1, 1], [2, 3]), ([1], [1, 2]), ([0, np.inf], [1, 2])):
            with self.subTest(x=x, y=y), self.assertRaises(ValueError):
                panels.line_band(self.ax, x, y)

    def test_heatmap_missing_cells_do_not_become_zero(self):
        mesh = panels.matrix_heatmap(self.ax, [[-2, 0, np.nan]], ["row"], ["X", "Y", "Z"],
                                      center=0, annotate=True)
        self.assertEqual(np.ma.count_masked(mesh.get_array()), 1)
        self.assertIn("×", [t.get_text() for t in self.ax.texts])
        self.assertIn("0.0", [t.get_text() for t in self.ax.texts])
        self.assertEqual(mesh.norm(0), 0.5)

    def test_shared_heatmap_range_maps_equal_values_equally(self):
        first = panels.matrix_heatmap(self.ax, [[0, 1]], ["A"], ["x", "y"], vmin=-2, vmax=2)
        second = panels.matrix_heatmap(self.fig.add_subplot(212), [[-2, 1]], ["A"], ["x", "y"], vmin=-2, vmax=2)
        np.testing.assert_array_equal(first.to_rgba(1), second.to_rgba(1))
        with self.assertRaisesRegex(ValueError, "clipping"):
            panels.matrix_heatmap(self.ax, [[3]], ["A"], ["x"], vmin=-2, vmax=2)

    def test_matrix_labels_shape_and_nonfinite_observations_are_checked(self):
        for values, rows, cols in (([[1]], ["A", "B"], ["X"]),
                                   ([[1, 2]], ["A"], ["X", "X"]),
                                   ([[np.inf]], ["A"], ["X"]),
                                   ([[np.nan]], ["A"], ["X"])):
            with self.subTest(values=values), self.assertRaises(ValueError):
                panels.matrix_heatmap(self.ax, values, rows, cols)
        mesh = panels.matrix_heatmap(self.ax, [[np.nan]], ["A"], ["X"], vmin=0, vmax=1)
        self.assertEqual(np.ma.count_masked(mesh.get_array()), 1)

    def test_dot_matrix_area_encodes_size_on_a_common_zero_based_scale(self):
        dots = panels.dot_matrix(self.ax, [[0, 1, 2]], [[0, 25, 100]], ["A"], ["x", "y", "z"],
                                  size_max=100, size_scale=80)
        np.testing.assert_array_equal(dots.get_sizes(), [0, 20, 80])
        for sizes in ([[0, -1, 2]], [[0, 1, 101]], [[0, np.nan, 2]]):
            with self.subTest(sizes=sizes), self.assertRaises(ValueError):
                panels.dot_matrix(self.ax, [[0, 1, 2]], sizes, ["A"], ["x", "y", "z"])
        with self.assertRaises(ValueError): panels.size_legend(self.ax, size_scale=-1)

    def test_paired_distribution_preserves_subject_pairs_and_observed_medians(self):
        result = panels.paired_distribution(self.ax, [[0, 2, 4], [5, 3, 1]], ["Before", "After"],
                                             paired=True, violin=False, seed=3)
        np.testing.assert_array_equal(result["median"], [2, 3])
        for index, expected in enumerate(([0, 5], [2, 3], [4, 1])):
            np.testing.assert_array_equal(self.ax.lines[index].get_ydata(), expected)
        with self.assertRaisesRegex(ValueError, "Paired"):
            panels.paired_distribution(self.ax, [[1, 2], [3]], ["A", "B"], paired=True)

    def test_constant_raincloud_groups_are_supported(self):
        result = panels.paired_distribution(self.ax, [[2, 2, 2], [0]], ["A", "B"])
        np.testing.assert_array_equal(result["median"], [2, 0])

    def test_embedding_reuses_group_colors_when_rows_are_shuffled(self):
        coords = np.array([[0, 2], [3, 1], [-1, 0]])
        groups = np.array(["B", "A", "B"]); colors = {"A": "red", "B": "blue"}
        first = panels.embedding_scatter(self.ax, coords, groups, order=["A", "B"], colors=colors)
        second = panels.embedding_scatter(self.fig.add_subplot(212), coords[::-1], groups[::-1],
                                           order=["A", "B"], colors=colors)
        for before, after in zip(first, second):
            self.assertEqual(before.get_label(), after.get_label())
            np.testing.assert_array_equal(before.get_facecolors(), after.get_facecolors())
            np.testing.assert_array_equal(before.get_paths()[0].vertices, after.get_paths()[0].vertices)
        self.assertNotIn("UMAP", self.ax.get_xlabel())
        with self.assertRaises(ValueError):
            panels.embedding_scatter(self.ax, coords, groups, order=["A"])

    def test_calibration_ece_is_count_weighted_and_ignores_empty_bins(self):
        result = panels.calibration(self.ax, [0.2, 0, 0.8], [0.4, 1, 0.7], [10, 0, 30],
                                     edges=[0, 0.4, 0.6, 1])
        self.assertAlmostEqual(result["ece"], 0.125)
        np.testing.assert_array_equal(result["line"].get_xdata(), [0.2, 0.8])
        np.testing.assert_array_equal(result["used_bins"], [True, False, True])

    def test_calibration_rejects_invalid_probabilities_counts_and_bin_order(self):
        for confidence, accuracy, counts in (([1.1], [0], [1]), ([0.5], [-0.1], [1]),
                                              ([0.5], [0.5], [0]), ([0.5], [0.5], [0.5]),
                                              ([0.8, 0.2], [0.5, 0.5], [1, 1])):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                panels.calibration(self.ax, confidence, accuracy, counts)
        with self.assertRaises(ValueError):
            panels.calibration(self.ax, [0.8], [0.7], [10], edges=[0, 0.5])

    def test_volcano_uses_supplied_statistics_and_exposes_zero_display_floor(self):
        with self.assertRaisesRegex(ValueError, "zero_floor"):
            panels.volcano(self.ax, [1, 2], [0.1, 0])
        scatter = panels.volcano(self.ax, [-2, 0, 2], [0.01, 0.5, 0], zero_floor=0.001,
                                  labels=["Gene A", "Gene B", "Gene C"],
                                  annotate_indices=np.array([2]), statistic="q")
        np.testing.assert_allclose(scatter.get_offsets()[:, 1], [2, -np.log10(0.5), 3])
        self.assertIn("q", self.ax.get_ylabel())
        self.assertTrue(any("Zero q displayed" in t.get_text() for t in self.ax.texts))
        self.assertTrue(any(t.get_text() == "Gene C" for t in self.ax.texts))

    def test_volcano_rejects_invalid_probabilities_and_unjustified_annotations(self):
        for probs in ([-0.1], [1.1], [np.nan]):
            with self.subTest(probs=probs), self.assertRaises(ValueError):
                panels.volcano(self.ax, [1], probs)
        with self.assertRaises(ValueError): panels.volcano(self.ax, [1], [0], zero_floor=0.2)
        with self.assertRaises(ValueError): panels.volcano(self.ax, [1], [0.1], annotate_indices=[0])

    def test_entity_encoding_is_explicit_and_palette_registry_is_reused(self):
        encoding = panels.entity_encoding(["A", "B"], "npg")
        self.assertEqual(encoding["A"]["color"], panels.PALETTES["npg"][0])
        self.assertNotEqual(encoding["A"]["marker"], encoding["B"]["marker"])
        with self.assertRaises(ValueError): panels.entity_encoding(["A", "A"])
        with self.assertRaises(ValueError): panels.entity_encoding(["A"], colors={"B": "red"})

    def test_style_restores_rcparams_and_does_not_override_layout_choice(self):
        old = list(matplotlib.rcParams["font.family"])
        with panels.paper_style("comic", 11):
            self.assertEqual(matplotlib.rcParams["font.size"], 11)
            self.assertEqual(matplotlib.rcParams["pdf.fonttype"], 42)
        self.assertEqual(matplotlib.rcParams["font.family"], old)
        self.assertIsNone(self.fig.get_layout_engine())
        with self.assertRaises(ValueError):
            with panels.paper_style(font_size=0.1): pass

    def test_export_has_live_text_vector_cells_and_true_physical_size(self):
        panels.matrix_heatmap(self.ax, [[-1, 1]], ["Feature"], ["Before", "After"], annotate=True)
        with matplotlib.rc_context({"svg.fonttype": "path", "pdf.fonttype": 3}):
            targets = panels.save_figure(self.fig, self.folder / "editable", formats=("svg", "pdf", "png"), metadata={"kind": "synthetic", "seed": 4})
            self.assertEqual(matplotlib.rcParams["svg.fonttype"], "path")
        svg = ET.fromstring(targets["svg"].read_text(encoding="utf-8"))
        self.assertTrue(svg.findall(".//s:text", NS))
        self.assertFalse(svg.findall(".//s:image", NS))
        self.assertAlmostEqual(float(svg.attrib["width"].removesuffix("pt")), 120 / 25.4 * 72, places=5)
        self.assertAlmostEqual(float(svg.attrib["height"].removesuffix("pt")), 80 / 25.4 * 72, places=5)
        self.assertIn(b"/FontFile2", targets["pdf"].read_bytes())
        self.assertTrue(targets["png"].read_bytes().startswith(b"\x89PNG"))
        self.assertIn('"synthetic"', targets["metadata"].read_text(encoding="utf-8"))

    def test_default_export_creates_png_only_and_preserves_existing_svg(self):
        svg = self.folder / "ordinary.svg"
        svg.write_text("Existing explicitly requested source", encoding="utf-8")
        panels.line_band(self.ax, [1, 2], [2, 3], label="Observed", xlabel="Time", ylabel="Score")
        self.ax.legend()
        result = panels.save_figure(self.fig, self.folder / "ordinary")
        self.assertEqual(set(result), {"png"})
        self.assertFalse((self.folder / "ordinary.pdf").exists())
        self.assertEqual(svg.read_text(encoding="utf-8"), "Existing explicitly requested source")

    def test_bold_type_and_dark_borders_keep_values_and_light_fills(self):
        from matplotlib.colors import to_rgba
        before = list(matplotlib.rcParams["font.family"])
        with panels.paper_style("serif", 9):
            self.assertEqual(matplotlib.rcParams["axes.labelweight"], "bold")
            self.ax.set_title("Comparison")
            result = panels.category_comparison(self.ax, ["A", "B"], [3, 5],
                [{"label": "Method", "values": [4, 6]}], bar_labels=True)
            self.ax.set_xlabel("Group")
        # Formatting still works after the rc context, including later legends.
        panels.finish_paper_style(self.fig)
        self.assertEqual(self.ax.get_title(), "Comparison")
        text = [self.ax.title, self.ax.xaxis.label, self.ax.yaxis.label,
                *self.ax.get_xticklabels(), *self.ax.get_yticklabels(),
                *self.ax.get_legend().get_texts()]
        self.assertTrue(all(item.get_fontweight() == "bold" for item in text))
        self.assertEqual([p.get_height() for p in result["bars"]], [3, 5])
        for bar in result["bars"]:
            self.assertEqual(bar.get_edgecolor(), panels.paired_edge(bar.get_facecolor()))
            self.assertGreaterEqual(bar.get_linewidth(), 1.1)
            self.assertLess(bar.get_facecolor()[3], 1)
        self.assertEqual(matplotlib.rcParams["font.family"], before)
        result = panels.binned_summary(self.ax, [[1, 2, 3, 4]], ["C"])
        for box in result["boxes"]["boxes"]:
            self.assertEqual(box.get_edgecolor(), panels.paired_edge(box.get_facecolor()))
            self.assertGreaterEqual(box.get_linewidth(), 1.1)
        for line in result["boxes"]["whiskers"] + result["boxes"]["caps"]:
            self.assertEqual(to_rgba(line.get_color()), panels.paired_edge(result["boxes"]["boxes"][0].get_facecolor()))
            self.assertGreaterEqual(line.get_linewidth(), 1.1)

    def test_paired_border_preserves_each_hue_and_repeated_finishing(self):
        import colorsys
        colors = ["#397EB5", "#D66B2C", "#2D8984"]
        bars = self.ax.bar([0, 1, 2], [1, 2, 3], color=colors, alpha=.24)
        panels.finish_paper_style(self.fig)
        edges = [bar.get_edgecolor() for bar in bars]
        for bar, color, edge in zip(bars, colors, edges):
            original_hls = colorsys.rgb_to_hls(*matplotlib.colors.to_rgb(color))
            edge_hls = colorsys.rgb_to_hls(*edge[:3])
            self.assertAlmostEqual(original_hls[0], edge_hls[0])
            self.assertLess(edge_hls[1], original_hls[1])
            self.assertAlmostEqual(bar.get_facecolor()[3], .24)
            self.assertEqual(edge[3], 1)
            self.assertGreaterEqual(bar.get_linewidth(), 1.1)
        self.assertEqual(len(set(edges)), 3)
        panels.finish_paper_style(self.fig)
        self.assertEqual(edges, [bar.get_edgecolor() for bar in bars])
        np.testing.assert_array_equal([bar.get_height() for bar in bars], [1, 2, 3])

    def test_aggregate_density_preserves_supplied_bin_counts(self):
        artist=panels.density_map(self.ax,[1,1,3],[1,1,3],counts=[2,3,7],gridsize=4)
        np.testing.assert_allclose(sorted(artist.get_array()),[5,7])
        with self.assertRaises(ValueError):
            panels.density_map(self.ax,[1,3],[1,3],counts=[1.5,2])

    def test_density_composes_conditional_region_and_count_aware_shares(self):
        artist=panels.density_map(self.ax,[1,30],[.05,1],counts=[3,7],yscale="log",xlim=[0,40],ylim=[.01,10],
            corridor={"x_max":20,"y_max":.1,"weights":[2,1],"weight_kind":"per_state"})
        self.assertAlmostEqual(artist.ccfa_corridor["state_share"],30)
        self.assertAlmostEqual(artist.ccfa_corridor["mass_share"],100*6/13)

    def test_curve_reference_fill_preserves_observations(self):
        line=panels.line_band(self.ax,[1,2,3],[2,4,3],fill_to=0)
        np.testing.assert_array_equal(line.get_ydata(),[2,4,3])
        self.assertEqual(len(self.ax.collections),1)

    def test_compact_legend_preserves_labels_and_explicit_columns(self):
        self.ax.plot([0,1],[0,1],label="One")
        self.ax.plot([0,1],[1,0],label="Two")
        legend=panels.compact_legend(self.ax,ncol=1)
        self.assertEqual([t.get_text() for t in legend.get_texts()],["One","Two"])
        self.assertEqual(legend._ncols,1)
        self.fig.canvas.draw()
        self.assertGreaterEqual(legend.get_window_extent().y0,self.ax.bbox.y1)
        explicit=panels.compact_legend(self.ax,loc="lower right")
        self.assertEqual(explicit._loc,4)

    def test_inset_inherits_bold_type_and_paired_borders(self):
        inset=self.ax.inset_axes([.2,.2,.5,.5])
        bars=inset.bar([1,2],[3,4],color="#82BFCB")
        inset.set_title("Zoom");inset.set_xlabel("Position")
        panels.finish_paper_style(self.ax.figure)
        self.assertEqual(inset.title.get_fontweight(),"bold")
        self.assertTrue(all(label.get_fontweight()=="bold" for label in inset.get_xticklabels()))
        self.assertTrue(np.allclose(bars.patches[0].get_edgecolor(),panels.paired_edge("#82BFCB")))

    def test_cjk_font_fallback_preserves_chinese_in_editable_svg(self):
        self.ax.set_title("中文图形 繁體測試")
        self.assertEqual(panels.audit_figure(self.fig)["missing_glyphs"], [],
            "Install a recognized CJK font (for example Noto Sans CJK) before running the release CJK check")
        target = panels.save_figure(self.fig, self.folder / "中文图", formats=("svg",))["svg"]
        svg = ET.fromstring(target.read_text(encoding="utf-8"))
        self.assertIn("中文图形 繁體測試", "".join(svg.itertext()))

    def test_native_mac_cjk_families_are_selected_without_changing_latin_type(self):
        for family in ("PingFang SC","PingFang TC","Songti SC","Songti TC"):
            fonts=[SimpleNamespace(name=name) for name in ("Times New Roman","DejaVu Sans",family)]
            with self.subTest(family=family),patch.object(font_manager.fontManager,"ttflist",fonts):
                selected=panels._font_families("serif")
                self.assertEqual(selected[0],"Times New Roman")
                self.assertIn(family,selected)

    def test_linux_and_windows_cjk_fallbacks_still_work_with_a_latin_fallback(self):
        for family in ("Microsoft YaHei","Noto Sans CJK SC","Noto Sans CJK TC",
                       "Noto Sans CJK JP","Noto Serif CJK JP","Noto Sans CJK KR","Noto Serif CJK KR"):
            fonts=[SimpleNamespace(name=name) for name in ("DejaVu Sans",family)]
            with self.subTest(family=family),patch.object(font_manager.fontManager,"ttflist",fonts):
                selected=panels._font_families("serif")
                self.assertEqual(selected[0],"DejaVu Sans")
                self.assertIn(family,selected)

    def test_export_protects_upstream_files_and_has_no_default_metadata_sidecar(self):
        source = self.folder / "source.svg"; source.write_text("KEEP", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "protected"):
            panels.save_figure(self.fig, source, formats=("svg",), protected_paths=[source])
        self.assertEqual(source.read_text(encoding="utf-8"), "KEEP")
        targets = panels.save_figure(self.fig, self.folder / "plain", formats=("svg",))
        self.assertEqual(list(targets), ["svg"])
        self.assertFalse((self.folder / "plain.metadata.json").exists())

    def test_invalid_export_contract_fails_before_creating_files(self):
        for kwargs in ({"formats": ("jpg",)}, {"formats": ("svg", "svg")},
                       {"dpi": 0}, {"metadata": {"value": float("nan")}}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                panels.save_figure(self.fig, self.folder / "invalid", **kwargs)
        self.assertEqual(list(self.folder.iterdir()), [])

    def test_render_failure_keeps_prior_versions_and_removes_temporary_files(self):
        target = self.folder / "existing.svg"; target.write_text("OLD", encoding="utf-8")
        original_save = self.fig.savefig
        def fail_pdf(*args, **kwargs):
            if kwargs.get("format") == "pdf": raise RuntimeError("Simulated renderer failure")
            return original_save(*args, **kwargs)
        with patch.object(self.fig, "savefig", side_effect=fail_pdf), self.assertRaises(RuntimeError):
            panels.save_figure(self.fig, target, formats=("svg", "pdf"))
        self.assertEqual(target.read_text(encoding="utf-8"), "OLD")
        self.assertEqual([p.name for p in self.folder.iterdir()], ["existing.svg"])

    def test_bounds_audit_reports_off_canvas_text_without_claiming_all_overlap_checks(self):
        self.fig.text(1.2, 0.5, "Outside canvas")
        report = panels.audit_figure(self.fig)
        self.assertIn("Outside canvas", report["text_outside_canvas"])
        self.assertAlmostEqual(report["width_mm"], 120)
        self.assertAlmostEqual(report["height_mm"], 80)

    def test_log_density_counts_every_original_observation(self):
        x = np.array([.01, .1, 1, 1, 1, 1, 10, 100])
        y = np.array([100, 10, 1, 1, 1, 1, .1, .01])
        before_x, before_y = x.copy(), y.copy()
        density = panels.density_map(self.ax, x, y, gridsize=12, xscale="log", yscale="log")
        self.assertEqual(float(density.get_array().sum()), len(x))
        self.assertTrue(np.all(density.get_array() >= 1))
        self.assertEqual(float(density.get_array().max()), 4)
        self.assertIsInstance(density.norm, mcolors.LogNorm)
        self.assertEqual((self.ax.get_xscale(), self.ax.get_yscale()), ("log", "log"))
        np.testing.assert_array_equal(x, before_x); np.testing.assert_array_equal(y, before_y)
        self.assertEqual(len(self.ax.lines), 0)  # No invented scientific threshold.

    def test_linear_density_keeps_zero_and_negative_observations(self):
        density = panels.density_map(self.ax, [-4, -1, 0, 0, 3], [-2, 0, 0, 0, 8])
        self.assertEqual(float(density.get_array().sum()), 5)
        self.fig.colorbar(density, ax=self.ax).set_label("Observations")
        self.fig.canvas.draw()

    def test_density_rejects_invalid_logs_dimensions_and_nonfinite_values(self):
        for x, y, kwargs in (([0, 1], [1, 2], {"xscale": "log"}),
                             ([1, 2], [-1, 2], {"yscale": "log"}),
                             ([1], [1, 2], {}), ([1, np.nan], [1, 2], {}),
                             ([1, 2], [1, 2], {"gridsize": 1}),
                             ([1, 2], [1, 2], {"xscale": "symlog"})):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                panels.density_map(self.ax, x, y, **kwargs)

    def test_binned_quantiles_are_observed_interpolations_not_means(self):
        samples = [[0, 10], [-5, -1, 3]]
        result = panels.binned_summary(self.ax, samples, ["Low", "High"], quantile=.95)
        np.testing.assert_allclose(result["quantiles"], [9.5, 2.6])
        np.testing.assert_allclose(result["quantile_line"].get_ydata(), [9.5, 2.6])
        np.testing.assert_array_equal(result["medians"], [5, -1])
        self.assertEqual(samples, [[0, 10], [-5, -1, 3]])
        legend = [text.get_text() for text in self.ax.get_legend().get_texts()]
        self.assertEqual(len(legend), 2)
        self.assertIn("95th percentile", legend)
        self.assertFalse(any("mean" in label.lower() for label in legend))

    def test_binned_boxes_show_iqr_whiskers_and_outliers_without_truncation(self):
        result = panels.binned_summary(self.ax, [[0, 1, 2, 3, 100], [-4, -4, -4]], ["A", "B"])
        boxes = result["boxes"]
        box_y = boxes["boxes"][0].get_path().vertices[:, 1]
        self.assertEqual((box_y.min(), box_y.max()), (1, 3))
        np.testing.assert_array_equal(boxes["medians"][0].get_ydata(), [2, 2])
        np.testing.assert_array_equal(boxes["whiskers"][1].get_ydata(), [3, 3])
        np.testing.assert_array_equal(boxes["fliers"][0].get_ydata(), [100])
        self.assertLessEqual(self.ax.get_ylim()[0], -4)
        self.assertGreaterEqual(self.ax.get_ylim()[1], 100)

    def test_binned_summary_rejects_empty_groups_and_invalid_quantiles(self):
        for samples, labels, quantile in (([[]], ["A"], .95), ([[1], [2]], ["A"], .95),
                                           ([[np.inf]], ["A"], .95), ([[1]], ["A"], 1.1),
                                           ([[1]], ["A"], np.nan)):
            with self.subTest(quantile=quantile), self.assertRaises(ValueError):
                panels.binned_summary(self.ax, samples, labels, quantile=quantile)

    def test_explicit_reference_quantiles_preserve_median_p90_p99_and_p95_semantics(self):
        summary = {"median": [.02, .1], "p90": [.08, .3], "p95": [.119, .319], "p99": [.2, .6]}
        result = panels.binned_summary(self.ax, None, ["Low", "High"], summary=summary, annotate=True,
                                       quantile_label="P95 displacement")
        np.testing.assert_array_equal(result["quantiles"], [.119, .319])
        self.assertEqual(result["quantile_line"].get_marker(), "D")
        for i, box in enumerate(result["boxes"]["boxes"]):
            y = box.get_path().vertices[:, 1]
            self.assertEqual(float(y.min()), summary["median"][i])
            self.assertEqual(float(y.max()), summary["p90"][i])
        self.assertEqual(float(result["boxes"]["whiskers"][1].get_ydata().max()), .2)
        self.assertEqual([text.get_text() for text in result["annotations"]], ["0.119", "0.319"])
        self.assertEqual([text.get_text() for text in self.ax.get_legend().texts],
                         ["Median–P90 range", "P99 whisker", "P95 displacement"])

    def test_reference_quantiles_from_samples_and_invalid_summaries(self):
        result = panels.binned_summary(self.ax, [[0, 1, 2, 3, 4]], ["A"], summary_mode="median_p90")
        np.testing.assert_allclose(result["summary"]["p90"], [3.6])
        np.testing.assert_allclose(result["summary"]["p99"], [3.96])
        summary = {"median": [1], "p90": [2], "p95": [3], "p99": [4]}
        for invalid in ({**summary, "p90": [5]}, {**summary, "p99": []}, {"median": [1]}):
            with self.subTest(summary=invalid), self.assertRaises(ValueError):
                panels.binned_summary(self.ax, None, ["A"], summary=invalid)
        with self.assertRaises(ValueError):
            panels.binned_summary(self.ax, [[1, 2]], ["A"], summary=summary)

    def test_reference_category_bands_and_sparse_labels_use_supplied_values(self):
        result = panels.category_comparison(self.ax, ["A", "B", "C"], [39.2, 40.1, 38.2],
            [{"label": "Mass", "values": [62, 64, 58], "lower": [60, 61, 56], "upper": [64, 67, 60],
              "marker": "s", "annotate": [1]}], bar_style="outlined", bar_labels=True)
        self.assertEqual(len(result["bands"]), 1)
        self.assertEqual(result["lines"][0].get_marker(), "s")
        self.assertEqual([text.get_text() for text in result["annotations"]], ["39.2", "40.1", "38.2", "64.0"])
        np.testing.assert_allclose([bar.get_height() for bar in result["bars"]], [39.2, 40.1, 38.2])
        self.assertLess(result["bars"][0].get_facecolor()[3], .2)
        self.assertEqual(result["bars"][0].get_edgecolor()[3], 1)
        with self.assertRaises(ValueError):
            panels.category_comparison(self.ax, ["A"], [1], [{"label": "B", "values": [2], "lower": [3], "upper": [4]}])

    def test_category_comparison_uses_one_unclipped_common_unit_axis(self):
        bars = [-3, 0, 130]
        series = [{"label": "A", "values": [-2, 0, 120], "color": "red", "marker": "s"},
                  {"label": "B", "values": [4, 5, 6], "color": "green", "marker": "^"}]
        result = panels.category_comparison(self.ax, ["X", "Y", "Z"], bars, series,
                                             bar_label="Difference", ylabel="Change (points)")
        self.assertEqual(len(self.fig.axes), 1)
        self.assertEqual([bar.get_height() for bar in result["bars"]], bars)
        np.testing.assert_array_equal(result["lines"][0].get_ydata(), [-2, 0, 120])
        self.assertEqual(result["lines"][0].get_marker(), "s")
        self.assertEqual(self.ax.get_ylabel(), "Change (points)")
        self.assertLessEqual(self.ax.get_ylim()[0], -3)
        self.assertGreaterEqual(self.ax.get_ylim()[1], 130)
        self.assertEqual(len(self.ax.get_legend().get_texts()), 3)
        self.assertEqual(series[0]["values"], [-2, 0, 120])

    def test_category_comparison_rejects_incompatible_lengths_and_invalid_values(self):
        for bars, series in (([1], [{"label": "A", "values": [1, 2]}]),
                              ([1, 2], [{"label": "A", "values": [1]}]),
                              ([1, 2], [{"label": "A", "values": [1, np.inf]}]),
                              ([1, 2], []),
                              ([1, 2], [{"label": "Occupancy", "values": [1, 2]}])):
            with self.subTest(bars=bars), self.assertRaises(ValueError):
                panels.category_comparison(self.ax, ["X", "Y"], bars, series)


if __name__ == "__main__":
    unittest.main(verbosity=2)
