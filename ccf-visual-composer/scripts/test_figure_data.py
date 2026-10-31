#!/usr/bin/env python3
"""Check literal research observations survive table-to-figure bindings."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
import subprocess

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "ccf-visual-composer/resources/python"))
import ccfa_figure_data as d


class FigureDataTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.folder = Path(self.tmp.name) / "中文研究"
        self.folder.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text, bom=False):
        path = self.folder / name
        path.write_text(text, encoding="utf-8-sig" if bom else "utf-8", newline="\n")
        return path

    def spec(self, path="结果.csv", kind="dumbbell", data=None, table=None):
        return {"version": 1, "rows": 1, "columns": 1,
                "data_sources": {"results": {"path": path}},
                "panels": [{"id": "a", "kind": kind, "row": 0, "column": 0,
                    "table": table or {"source": "results"},
                    "data": data or {"labels": {"column": "id", "dtype": "string"},
                                     "before": {"column": "before"}, "after": {"column": "after"}}}]}

    def resolve(self, spec):
        return d.materialize(spec, self.folder)

    def test_csv_bom_filter_and_numeric_sort_preserve_all_pairings(self):
        self.write("结果.csv", "id,condition,step,before,after\n甲,use,10,0.71,0.82\n乙,omit,1,0.1,0.2\n丙,use,2,0.42,0.59\n", bom=True)
        spec = self.spec(table={"source": "results", "where": {"condition": "use"}, "order_by": "step"})
        before = copy.deepcopy(spec)
        result, paths = self.resolve(spec)
        self.assertEqual(result["panels"][0]["data"], {"labels": ["丙", "甲"], "before": [.42, .71], "after": [.59, .82]})
        self.assertEqual(spec, before)
        self.assertNotIn("table", result["panels"][0])
        self.assertNotIn("data_sources", result)
        self.assertEqual(paths, [(self.folder / "结果.csv").resolve()])

    def test_tsv_and_numeric_filter_use_identical_selected_rows(self):
        self.write("结果.tsv", "id\tbefore\tafter\n甲\t2\t3\n乙\t10\t12\n")
        result, _ = self.resolve(self.spec(path="结果.tsv", table={"source": "results", "where": {"before": 10}}))
        self.assertEqual(result["panels"][0]["data"]["labels"], ["乙"])
        self.assertEqual(result["panels"][0]["data"]["after"], [12])

    def test_json_records_wrapper_and_schema_read_protect_all_inputs(self):
        self.write("记录.json", json.dumps({"records": [{"id": "甲", "before": .1, "after": .3}]}), bom=True)
        spec = self.spec(path="记录.json")
        path = self.write("图稿.json", json.dumps(spec), bom=True)
        result, paths = d.load_composition(path)
        self.assertEqual(result["panels"][0]["data"]["before"], [.1])
        self.assertEqual(paths, [path.resolve(), (self.folder / "记录.json").resolve()])

    def test_layers_inherit_parent_selected_record_sequence_and_can_override(self):
        self.write("结果.csv", "id,step,before,after\n甲,10,.5,.7\n乙,2,.3,.4\n")
        spec = self.spec(data={"x": {"column": "step"}, "y": {"column": "before"}},
                         table={"source": "results", "order_by": "step"})
        spec["panels"][0]["layers"] = [
            {"kind": "line_band", "data": {"x": {"column": "step"}, "y": {"column": "after"}}},
            {"kind": "line_band", "table": {"source": "results", "where": {"id": "甲"}},
             "data": {"x": {"column": "step"}, "y": {"column": "after"}}}]
        result, _ = self.resolve(spec)
        panel = result["panels"][0]
        self.assertEqual(panel["data"]["x"], [2, 10])
        self.assertEqual(panel["layers"][0]["data"], {"x": [2, 10], "y": [.4, .7]})
        self.assertEqual(panel["layers"][1]["data"], {"x": [10], "y": [.7]})

    def test_groups_preserve_raw_observations_and_explicit_group_order(self):
        self.write("结果.csv", "method,score\nB,.7\nA,.4\nB,.8\nA,.5\n")
        spec = self.spec(data={"samples": {"groups": {"by": "method", "value": "score", "order": ["A", "B"]}}, "labels": ["A", "B"]})
        result, _ = self.resolve(spec)
        self.assertEqual(result["panels"][0]["data"]["samples"], [[.4, .5], [.7, .8]])
        spec["panels"][0]["data"]["samples"]["groups"]["order"] = ["A"]
        with self.assertRaisesRegex(d.DataBindingError, "exactly"):
            self.resolve(spec)

    def matrix_spec(self):
        return self.spec(data={"values": {"matrix": {"row": "dataset", "column": "method", "value": "score", "row_order": ["D2", "D1"], "column_order": ["B", "A"]}}, "row_labels": ["D2", "D1"], "col_labels": ["B", "A"]})

    def paired_spec(self, **contract):
        return self.spec(kind="paired_distribution", data={"labels": ["A", "B"], "paired": True,
            "violin": False, "values": {"groups": {"by": "method", "value": "score", "order": ["A", "B"], **contract}}})

    def test_subject_ids_align_shuffled_groups_and_the_actual_plotted_pairs(self):
        self.write("结果.csv", "method,subject,score\nA,s1,10\nA,s2,20\nB,s2,200\nB,s1,100\n")
        spec = self.paired_spec(pair_by="subject")
        before = copy.deepcopy(spec)
        resolved, _ = self.resolve(spec)
        self.assertEqual(resolved["panels"][0]["data"]["values"], [[10, 20], [100, 200]])
        self.assertEqual(spec, before)
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import ccfa_figure_library as figures
        fig = figures.compose(resolved)
        try:
            self.assertEqual([list(line.get_ydata()) for line in fig.axes[0].lines[:2]], [[10, 100], [20, 200]])
        finally:
            plt.close(fig)

    def test_paired_group_binding_requires_identity_or_explicit_matched_order(self):
        self.write("结果.csv", "method,score\nA,10\nA,20\nB,100\nB,200\n")
        with self.assertRaisesRegex(d.DataBindingError, "pair_by.*matched_order"):
            self.resolve(self.paired_spec())
        resolved, _ = self.resolve(self.paired_spec(matched_order=True))
        self.assertEqual(resolved["panels"][0]["data"]["values"], [[10, 20], [100, 200]])
        unpaired = self.paired_spec()
        unpaired["panels"][0]["data"]["paired"] = False
        self.assertEqual(self.resolve(unpaired)[0]["panels"][0]["data"]["values"], [[10, 20], [100, 200]])

    def test_pair_by_rejects_duplicate_and_missing_subjects_even_at_equal_lengths(self):
        for rows, message in [
            ("A,s1,10\nA,s1,20\nB,s1,100\nB,s2,200\n", "duplicate paired subject"),
            ("A,s1,10\nA,s2,20\nB,s1,100\nB,s3,300\n", "same subject identities"),
            ("A,s1,10\nA,s2,20\nB,s1,100\n", "same subject identities")]:
            with self.subTest(rows=rows):
                self.write("结果.csv", "method,subject,score\n" + rows)
                with self.assertRaisesRegex(d.DataBindingError, message):
                    self.resolve(self.paired_spec(pair_by="subject"))

    def test_matched_order_contract_rejects_unequal_lengths_and_ambiguous_flags(self):
        self.write("结果.csv", "method,subject,score\nA,s1,10\nA,s2,20\nB,s1,100\n")
        with self.assertRaisesRegex(d.DataBindingError, "equal group lengths"):
            self.resolve(self.paired_spec(matched_order=True))
        for contract in ({"matched_order": "true"}, {"matched_order": 1}, {"matched_order": True, "pair_by": "subject"}):
            with self.subTest(contract=contract), self.assertRaises(d.DataBindingError):
                self.resolve(self.paired_spec(**contract))

    def test_paired_template_and_overlay_bindings_cannot_bypass_pair_contract(self):
        self.write("结果.csv", "method,score\nA,10\nA,20\nB,100\nB,200\n")
        grouped = self.paired_spec()["panels"][0]["data"]
        template = {"version": 1, "template": "paired_effects", "data_sources": {"results": {"path": "结果.csv"}},
            "table": {"source": "results"}, "data": {"paired": {"labels": ["A", "B"], "values": grouped["values"]}}}
        with self.assertRaisesRegex(d.DataBindingError, "pair_by.*matched_order"):
            self.resolve(template)
        overlay = self.paired_spec()
        overlay["panels"][0]["data"] = {"values": [[10, 20], [100, 200]], "labels": ["A", "B"], "paired": True}
        overlay["panels"][0]["layers"] = [{"kind": "paired_distribution", "data": grouped}]
        with self.assertRaisesRegex(d.DataBindingError, "pair_by.*matched_order"):
            self.resolve(overlay)
        overlay["panels"][0].pop("layers")
        self.assertEqual(self.resolve(overlay)[0]["panels"][0]["data"]["values"], [[10, 20], [100, 200]])

    def test_matrix_places_values_by_explicit_axis_ids_not_file_order(self):
        self.write("结果.csv", "dataset,method,score\nD1,A,.1\nD2,B,.8\nD1,B,.3\nD2,A,.7\n")
        result, _ = self.resolve(self.matrix_spec())
        self.assertEqual(result["panels"][0]["data"]["values"], [[.8, .7], [.3, .1]])

    def test_matrix_rejects_duplicates_instead_of_averaging(self):
        self.write("结果.csv", "dataset,method,score\nD1,A,.1\nD1,A,.5\nD2,B,.8\n")
        with self.assertRaisesRegex(d.DataBindingError, "duplicate matrix"):
            self.resolve(self.matrix_spec())

    def test_matrix_rejects_missing_cells_instead_of_filling_zero(self):
        self.write("结果.csv", "dataset,method,score\nD1,A,.1\nD2,B,.8\nD1,B,.3\n")
        with self.assertRaisesRegex(d.DataBindingError, "missing matrix"):
            self.resolve(self.matrix_spec())

    def test_linked_layout_binds_top_level_data_and_nested_series(self):
        self.write("结果.csv", "position,observed,predicted\n10,3,4\n2,1,2\n")
        spec = {"version": 1, "layout": "aligned_tracks", "data_sources": {"r": {"path": "结果.csv"}},
                "table": {"source": "r", "order_by": "position"}, "data": {
                    "x": {"column": "position"}, "xlabel": "位置", "tracks": [{"label": "信号", "unit": "counts", "series": [
                        {"label": "观测", "y": {"column": "observed"}}, {"label": "预测", "y": {"column": "predicted"}}]}]}}
        before = copy.deepcopy(spec)
        result, _ = self.resolve(spec)
        self.assertEqual(result["data"]["x"], [2, 10])
        self.assertEqual(result["data"]["tracks"][0]["series"][1]["y"], [2, 4])
        self.assertEqual(before, spec)
        self.assertNotIn("table", result)

    def test_inline_data_and_literal_entity_colors_are_preserved(self):
        spec = {"version": 1, "panels": [{"id": "x", "data": {"x": [1, 2], "colors": {"column": "blue", "groups": "red"}}}]}
        result, paths = self.resolve(spec)
        self.assertEqual(result, spec)
        self.assertEqual(paths, [])

    def test_preserved_template_data_is_a_supported_container(self):
        spec={"version":1,"template":"sensitivity_dynamics","data":{"methods":["A"],"observations":[1,2,3]}}
        result,paths=self.resolve(spec)
        self.assertEqual(result,spec)
        self.assertEqual(paths,[])
        with self.assertRaisesRegex(d.DataBindingError,"Choose one"):
            self.resolve(dict(spec,layout="aligned_tracks"))

    def test_sources_are_deduplicated_but_all_declared_files_are_protected(self):
        self.write("结果.csv", "id,before,after\n甲,.1,.3\n")
        self.write("另表.tsv", "x\n2\n")
        spec = self.spec()
        spec["data_sources"].update(same={"path": "结果.csv"}, other={"path": "另表.tsv"})
        _, paths = self.resolve(spec)
        self.assertEqual(len(paths), 2)
        self.assertEqual({p.name for p in paths}, {"结果.csv", "另表.tsv"})

    def test_invalid_numeric_cells_never_become_zero_or_missing(self):
        for value in ("", "NaN", "Infinity", "1,000", "not-a-score", "1e999"):
            with self.subTest(value=value):
                self.write("结果.csv", 'id,before,after\n甲,"'+value+'",.3\n')
                with self.assertRaises(d.DataBindingError):self.resolve(self.spec())

    def test_boolean_json_values_are_not_numeric_scores(self):
        self.write("结果.json", '[{"id":"a","before":true,"after":0.3}]')
        with self.assertRaisesRegex(d.DataBindingError, "finite number"):
            self.resolve(self.spec(path="结果.json"))

    def test_duplicate_json_keys_and_nonfinite_literals_are_errors(self):
        for content in ('[{"id":"a","id":"b"}]', '[{"id":"a","before":NaN}]'):
            self.write("结果.json", content)
            with self.assertRaises(d.DataBindingError):self.resolve(self.spec(path="结果.json"))

    def test_bad_csv_header_and_record_width_are_errors(self):
        for content in ("id,before,before\na,.1,.2\n", "id,before,after\na,.1\n", "id,,after\na,.1,.2\n"):
            self.write("结果.csv", content)
            with self.assertRaises(d.DataBindingError):self.resolve(self.spec())

    def test_missing_columns_empty_filter_and_network_sources_are_errors(self):
        self.write("结果.csv", "id,before,after\na,.1,.2\n")
        spec=self.spec();spec["panels"][0]["data"]["after"]={"column":"missing"}
        with self.assertRaisesRegex(d.DataBindingError,"missing"):self.resolve(spec)
        with self.assertRaisesRegex(d.DataBindingError,"no records"):
            self.resolve(self.spec(table={"source":"results","where":{"id":"absent"}}))
        with self.assertRaisesRegex(d.DataBindingError,"local file"):
            self.resolve(self.spec(path="https://example.com/data.csv"))

    def test_invalid_layout_shapes_and_versions_are_errors(self):
        for spec in ({"version":True,"panels":[{}]}, {"version":1,"layout":"aligned_tracks","data":{},"panels":[{}]}, {"version":1,"layout":"aligned_tracks"}):
            with self.assertRaises(d.DataBindingError):self.resolve(spec)

    def test_data_binding_import_uses_only_standard_library(self):
        code="import sys;sys.path.insert(0,sys.argv[1]);import ccfa_figure_data;assert 'numpy' not in sys.modules;assert 'matplotlib' not in sys.modules;assert 'requests' not in sys.modules"
        result=subprocess.run([sys.executable,"-c",code,str(ROOT/"ccf-visual-composer/resources/python")],capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)

    def test_resolved_line_renders_exact_sorted_values_without_simulation(self):
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import ccfa_figure_library as figures
        self.write("结果.csv","step,score\n10,.9\n2,.4\n5,.7\n")
        spec=self.spec(kind="line_band",data={"x":{"column":"step"},"y":{"column":"score"}},table={"source":"results","order_by":"step"})
        resolved,_=self.resolve(spec)
        fig=figures.compose(resolved)
        try:
            self.assertEqual(list(fig.axes[0].lines[0].get_xdata()),[2,5,10])
            self.assertEqual(list(fig.axes[0].lines[0].get_ydata()),[.4,.7,.9])
            self.assertFalse(any("Simulated" in text.get_text() for text in fig.texts))
        finally:plt.close(fig)


if __name__ == "__main__":unittest.main()
