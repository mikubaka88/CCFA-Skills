#!/usr/bin/env python3
"""Meaningful real-data, domain, reproducibility and CLI template regressions."""
from __future__ import annotations

import copy
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ccf-visual-composer/resources/python"))
import ccfa_analysis_templates as templates

BUILD = ROOT / "ccfa-workfiles/skill-maintenance/analytical-figures/build"


class AnalysisTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.examples = templates.demo_data(17)

    def setUp(self):
        BUILD.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="template-test-", dir=BUILD)
        self.folder = Path(self.temporary.name).resolve()
        self.assertEqual(self.folder.parent, BUILD.resolve())

    def tearDown(self):
        plt.close("all")
        self.temporary.cleanup()

    def data(self, name):
        data = copy.deepcopy(self.examples[name])
        data.pop("_meta", None)
        return data

    def render(self, name, data=None):
        return templates.render_template(name, self.data(name) if data is None else data)

    def test_all_nine_templates_preserve_every_input_value_and_label(self):
        self.assertEqual(len(templates.CATALOG), 9)
        for name in templates.CATALOG:
            with self.subTest(template=name):
                data = self.data(name)
                before = json.dumps(data, sort_keys=True, allow_nan=False)
                fig = self.render(name, data)
                self.assertEqual(json.dumps(data, sort_keys=True, allow_nan=False), before)
                self.assertAlmostEqual(fig.get_figwidth() * 25.4, 183)
                self.assertFalse(any("Simulated data" in text.get_text() for text in fig.texts))
                plt.close(fig)

    def test_real_renderer_never_calls_demo_generator_or_fills_missing_data(self):
        data = self.data("benchmark_atlas")
        data["performance"]["mean"] = [-2, 0, 2, 4]
        for key in ("runs", "lower", "upper", "uncertainty"):
            data["performance"].pop(key, None)
        with patch.object(templates, "demo_data", side_effect=AssertionError("No synthetic fallback")):
            fig = self.render("benchmark_atlas", data)
            ax = next(a for a in fig.axes if a.get_title(loc="left") == "Repeated runs")
            observed = [float(c.get_offsets()[0, 0]) for c in ax.collections]
            self.assertEqual(observed, [-2, 0, 2, 4])
            data.pop("tradeoff")
            with self.assertRaisesRegex(ValueError, "tradeoff"):
                self.render("benchmark_atlas", data)

    def test_demo_generation_is_seeded_and_keeps_global_rng_unchanged(self):
        before = np.random.get_state()
        first = templates.demo_data(9)
        second = templates.demo_data(9)
        third = templates.demo_data(10)
        self.assertEqual(first, second)
        self.assertNotEqual(first, third)
        self.assertTrue(all(d["_meta"]["synthetic"] for d in first.values()))
        after = np.random.get_state()
        self.assertEqual(before[0], after[0])
        np.testing.assert_array_equal(before[1], after[1])
        self.assertEqual(before[2:], after[2:])

    def test_demo_seed_changes_do_not_make_fixed_color_ranges_hide_observations(self):
        for seed in (2, 3, 13):
            with self.subTest(seed=seed):
                data = templates.demo_data(seed)["mechanism_overview"]
                fig = self.render("mechanism_overview", data)
                self.assertTrue(any("Simulated data" in text.get_text() for text in fig.texts))
                plt.close(fig)

    def test_demo_paired_intervals_are_derived_from_the_same_observations(self):
        block = self.examples["paired_effects"]
        before, after = np.asarray(block["paired"]["values"])
        diff = np.asarray(block["differences"])
        np.testing.assert_allclose(after - before, diff)
        self.assertAlmostEqual(float(diff.mean()), block["subgroups"]["mean"][0])
        self.assertLess(block["subgroups"]["lower"][0], diff.mean())
        self.assertGreater(block["subgroups"]["upper"][0], diff.mean())

    def test_paired_differences_cannot_disagree_with_within_subject_changes(self):
        data = self.data("paired_effects")
        data["differences"][0] += 20
        with self.assertRaises(ValueError): self.render("paired_effects", data)
        data = self.data("paired_effects")
        data["differences"] = data["differences"][:-1]
        with self.assertRaises(ValueError): self.render("paired_effects", data)

    def test_two_group_change_template_rejects_an_ambiguous_third_group(self):
        data = self.data("paired_effects")
        data["methods"].append("Followup")
        data["paired"]["labels"].append("Followup")
        data["paired"]["values"].append(data["paired"]["values"][-1][:])
        with self.assertRaises(ValueError): self.render("paired_effects", data)

    def test_difference_panel_names_the_actual_supplied_contrast(self):
        data = self.data("paired_effects")
        data["methods"] = ["Control", "Treatment"]
        data["paired"]["labels"] = ["Control", "Treatment"]
        for series, method in zip(data["response_curve"]["series"], data["methods"]):
            series["method"] = method
        fig = self.render("paired_effects", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Paired differences")
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], ["Treatment − Control"])

    def test_repeated_run_mean_cannot_conflict_with_plotted_runs(self):
        data = self.data("benchmark_atlas")
        data["performance"]["mean"][0] += 0.5
        # The altered estimate still lies inside the supplied interval, so this
        # specifically catches inconsistent summary and raw observations.
        with self.assertRaises(ValueError): self.render("benchmark_atlas", data)

    def test_empty_required_series_and_observation_lists_are_rejected(self):
        data = self.data("scaling_robustness")
        data["panels"][0]["series"] = []
        with self.assertRaises(ValueError): self.render("scaling_robustness", data)
        for key in ("calibration", "errors"):
            with self.subTest(block=key):
                data = self.data("calibration_errors"); data[key] = []
                with self.assertRaises(ValueError): self.render("calibration_errors", data)

    def test_uncertainty_pair_is_optional_but_half_empty_or_invalid_pairs_fail(self):
        data = self.data("scaling_robustness")
        for block in data["panels"]:
            for series in block["series"]:
                series.pop("lower"); series.pop("upper")
        fig = self.render("scaling_robustness", data)
        self.assertFalse(any(ax.collections for ax in fig.axes))
        for low, high in (([], []), (None, []), ([0], [1])):
            invalid = copy.deepcopy(data)
            invalid["panels"][0]["series"][0].update(lower=low, upper=high)
            with self.subTest(lower=low, upper=high), self.assertRaises(ValueError):
                self.render("scaling_robustness", invalid)

    def test_curves_cannot_hide_outlying_uncertainty_or_use_invalid_log_x(self):
        data = self.data("scaling_robustness")
        block = data["panels"][0]
        lows = [min(s["y"]) for s in block["series"]]
        highs = [max(s["y"]) for s in block["series"]]
        block["ylim"] = [min(lows), max(highs)]
        with self.assertRaisesRegex(ValueError, "hide"):
            self.render("scaling_robustness", data)
        data = self.data("scaling_robustness")
        data["panels"][0]["xscale"] = "log"
        data["panels"][0]["x"][0] = 0
        with self.assertRaises(ValueError): self.render("scaling_robustness", data)

    def test_calibration_confidence_histogram_respects_probability_and_count_domains(self):
        for field, values in (("edges", [-0.1, 0.125, .25, .375, .5, .625, .75, .875, 1]),
                              ("edges", [0, .125, .25, .375, .5, .625, .75, .875, 1.1]),
                              ("counts", [0.5] * 8)):
            data = self.data("calibration_errors"); data["confidence_histogram"][field] = values
            with self.subTest(field=field, values=values), self.assertRaises(ValueError):
                self.render("calibration_errors", data)

    def test_failure_and_confusion_sample_counts_cannot_be_negative_or_fractional(self):
        for value in (-1, 0.5):
            with self.subTest(value=value):
                data = self.data("calibration_errors"); data["failure_counts"]["counts"][0] = value
                with self.assertRaises(ValueError): self.render("calibration_errors", data)
                data = self.data("calibration_errors"); data["confusion"]["values"][0][0] = value
                with self.assertRaises(ValueError): self.render("calibration_errors", data)

    def test_pearson_range_cannot_be_bypassed_by_changing_color_limits(self):
        data = self.data("representation_diagnostics")
        block = data["correlation"]
        block["values"][0][1] = block["values"][1][0] = 1.5
        block.update(vmin=-2, vmax=2)
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)

    def test_correlation_identity_and_symmetry_are_checked_at_the_template_boundary(self):
        data = self.data("representation_diagnostics")
        data["correlation"]["values"][0][1] = 0.9
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)
        data = self.data("representation_diagnostics")
        data["correlation"]["columns"][0] = "Unknown feature"
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)

    def test_attention_weights_cannot_be_negative_even_with_a_diverging_palette(self):
        data = self.data("representation_diagnostics")
        block = data["attention"]; block["values"][0][0] = -0.1
        block.update(vmin=-1, vmax=1, cmap="RdBu_r")
        with self.assertRaises(ValueError): self.render("representation_diagnostics", data)

    def test_more_embedding_groups_than_palette_colors_keep_all_group_ids(self):
        data = self.data("representation_diagnostics")
        ids = [f"Group {i}" for i in range(len(templates.PALETTES["tol_muted"]) + 1)]
        data["embedding"] = {"coordinates": [[i, i % 3] for i in range(len(ids))],
                             "groups": ids, "order": ids}
        fig = self.render("representation_diagnostics", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Representation geometry")
        self.assertEqual([collection.get_label() for collection in ax.collections], ids)

    def test_missing_heatmap_observations_remain_missing_and_do_not_change_source(self):
        data = self.data("benchmark_atlas")
        data["benchmark"]["values"][0][0] = float("nan")
        fig = self.render("benchmark_atlas", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Cross-task benchmark")
        self.assertEqual(np.ma.count_masked(ax.collections[0].get_array()), 1)
        self.assertTrue(np.isnan(data["benchmark"]["values"][0][0]))
        self.assertIn("×", [text.get_text() for text in ax.texts])

    def test_pareto_template_keeps_supplied_directions_and_excludes_dominated_points(self):
        data = self.data("benchmark_atlas")
        block = data["tradeoff"]
        block.update(x=[0, 0, 1, 1], y=[0, 1, 0, 1], x_direction="max", y_direction="min")
        fig = self.render("benchmark_atlas", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Accuracy versus cost")
        line = next(line for line in ax.lines if line.get_label() == "Pareto frontier")
        np.testing.assert_array_equal(line.get_xdata(), [1])
        np.testing.assert_array_equal(line.get_ydata(), [0])
        np.testing.assert_array_equal(ax.collections[0].get_offsets(), np.column_stack([block["x"], block["y"]]))

    def test_biological_template_forwards_explicit_zero_probability_display_floor(self):
        data = self.data("biological_atlas")
        block = data["volcano"]; block["probability"][0] = 0
        positive = np.asarray(block["probability"])[np.asarray(block["probability"]) > 0]
        block["zero_floor"] = float(positive.min() / 10)
        fig = self.render("biological_atlas", data)
        ax = next(a for a in fig.axes if a.get_title(loc="left") == "Effect-size screening")
        self.assertTrue(any("Zero q displayed" in text.get_text() for text in ax.texts))
        self.assertEqual(block["probability"][0], 0)

    def test_invalid_data_reports_error_without_leaking_figures(self):
        for name, data in (("benchmark_atlas", {}), ("benchmark_atlas", {"methods": ["A"]})):
            before = set(plt.get_fignums())
            with self.subTest(data=data), self.assertRaises(ValueError): self.render(name, data)
            self.assertEqual(set(plt.get_fignums()), before)

    def test_real_cli_exports_are_editable_and_preserve_the_exact_source_file(self):
        data = self.data("paired_effects")
        source = self.folder / "observations.json"
        source.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        original = source.read_bytes()
        out = self.folder / "figures-task"
        with contextlib.redirect_stdout(io.StringIO()):
            code = templates.main(["--data", str(source), "--template", "paired_effects",
                                   "--out", str(out), "--formats", "svg"])
        self.assertEqual(code, 0); self.assertEqual(source.read_bytes(), original)
        manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["synthetic"])
        self.assertIsNone(manifest["seed"])
        self.assertFalse((out / "source/demo-data.json").exists())
        svg = ET.parse(out / manifest["figures"]["paired_effects"]["exports"]["svg"])
        self.assertTrue(svg.findall(".//{http://www.w3.org/2000/svg}text"))

    def test_cli_never_overwrites_input_named_like_the_output_manifest(self):
        out = self.folder / "collision-task"; out.mkdir()
        source = out / "manifest.json"
        source.write_text(json.dumps(self.data("paired_effects")), encoding="utf-8")
        original = source.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()), self.assertRaises((ValueError, SystemExit)):
            templates.main(["--data", str(source), "--template", "paired_effects", "--out", str(out), "--formats", "svg"])
        self.assertEqual(source.read_bytes(), original)

    def test_cli_requires_explicit_real_or_demo_mode(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            templates.main(["--out", str(self.folder)])
        self.assertEqual(list(self.folder.iterdir()), [])

    def test_sensitivity_summary_and_threshold_share_come_from_the_supplied_observations(self):
        data = self.data("sensitivity_dynamics")
        data["density"].update(x=[0, 1, 2, 3], y=[.1, .2, .25, .5], threshold=.25)
        data["sensitivity"].update(samples=[[0, 10], [-5, -1, 3]], labels=["Low", "High"], quantile=.95)
        before = copy.deepcopy(data)
        fig = self.render("sensitivity_dynamics", data)
        density_ax = next(ax for ax in fig.axes if ax.get_title(loc="left") == "State-space exposure")
        self.assertEqual(float(density_ax.collections[0].get_array().sum()), 4)
        self.assertTrue(any("75.0% at or below 0.25" == text.get_text() for text in density_ax.texts))
        sensitivity_ax = next(ax for ax in fig.axes if ax.get_title(loc="left") == "Perturbation by group")
        quantile_line = next(line for line in sensitivity_ax.lines if "percentile" in line.get_label())
        np.testing.assert_allclose(quantile_line.get_ydata(), [9.5, 2.6])
        self.assertEqual(data, before)

    def test_each_sensitivity_pair_has_two_main_axes_and_needs_only_its_own_blocks(self):
        full = self.data("sensitivity_dynamics")
        for pair, blocks in (("sensitivity", ("density", "sensitivity")),
                             ("dynamics", ("dynamics", "categories"))):
            with self.subTest(pair=pair):
                data = {"methods": full["methods"][:], "panel_pair": pair,
                        **{key: copy.deepcopy(full[key]) for key in blocks}}
                before = copy.deepcopy(data)
                fig = self.render("sensitivity_dynamics", data)
                main_axes = [ax for ax in fig.axes if ax.get_title(loc="left")]
                self.assertEqual(len(main_axes), 2)
                self.assertEqual(len(fig.axes), 3 if pair == "sensitivity" else 2)
                self.assertEqual(data, before)
                plt.close(fig)

    def test_sensitivity_domain_checks_do_not_hide_percentage_intervals_or_invalid_thresholds(self):
        data = self.data("sensitivity_dynamics")
        series = data["dynamics"]["series"][0]
        series["lower"] = [value - 1 for value in series["y"]]
        series["upper"] = [value + 1 for value in series["y"]]
        with self.assertRaises(ValueError): self.render("sensitivity_dynamics", data)
        data = self.data("sensitivity_dynamics"); data["categories"]["bars"][0] = -1
        with self.assertRaises(ValueError): self.render("sensitivity_dynamics", data)
        data = self.data("sensitivity_dynamics"); data["density"]["threshold"] = 0
        with self.assertRaises(ValueError): self.render("sensitivity_dynamics", data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
