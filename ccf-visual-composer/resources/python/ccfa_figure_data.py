#!/usr/bin/env python3
"""Resolve explicit CSV/TSV/JSON table bindings into a figure composition.

Uses only the standard library. Reads local paths declared by the caller;
never discovers files, contacts services, generates samples or aggregates rows.
The returned composition contains materialized values and no table bindings.
"""
from __future__ import annotations

import copy
import csv
import json
import math
from pathlib import Path
import re


class DataBindingError(ValueError):
    """An explicit data source or binding cannot be used as declared."""


def _fail(message):
    raise DataBindingError(message)


def _pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            _fail(f"Duplicate JSON key: {key!r}")
        result[key] = value
    return result


def _json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=_pairs,
                          parse_constant=lambda value: _fail(f"Non-finite JSON number: {value}"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise DataBindingError(f"Cannot read UTF-8 JSON file {path.name!r}: {exc}") from exc


def _name(value, context):
    if not isinstance(value, str) or not value.strip():
        _fail(f"{context} must be a nonempty column or source name")
    return value


def _number(value, context):
    if isinstance(value, bool) or value is None:
        _fail(f"{context} requires a finite number, received {value!r}")
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if math.isfinite(value):
            return value
    elif isinstance(value, str):
        text = value.strip()
        if re.fullmatch(r"[+-]?\d+", text):
            return int(text)
        if re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", text):
            result = float(text)
            if math.isfinite(result):
                return result
    _fail(f"{context} requires a finite number, received {value!r}")


def _string(value, context):
    if value is None or isinstance(value, (dict, list, tuple)):
        _fail(f"{context} requires a scalar string value")
    if isinstance(value, float) and not math.isfinite(value):
        _fail(f"{context} contains a non-finite value")
    return str(value)


def _column(rows, name, context):
    name = _name(name, context)
    for number, row in enumerate(rows, 1):
        if name not in row:
            _fail(f"{context}: column {name!r} is missing from selected row {number}")
    return [row[name] for row in rows]


def _table_file(path, fmt, alias):
    if fmt == "json":
        rows = _json(path)
        if isinstance(rows, dict) and set(rows) == {"records"}:
            rows = rows["records"]
        if not isinstance(rows, list):
            _fail(f"Source {alias!r} must be a JSON array of records or {{'records': [...]}}")
    else:
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as stream:
                reader = csv.reader(stream, delimiter="\t" if fmt == "tsv" else ",", strict=True)
                header = next(reader, None)
                if not header or any(not name.strip() for name in header) or len(set(header)) != len(header):
                    _fail(f"Source {alias!r} needs nonempty, unique column headers")
                rows = []
                for number, values in enumerate(reader, 2):
                    if not values:
                        continue
                    if len(values) != len(header):
                        _fail(f"Source {alias!r}, row {number}: field count differs from its header")
                    rows.append(dict(zip(header, values)))
        except (OSError, UnicodeError, csv.Error) as exc:
            raise DataBindingError(f"Cannot read UTF-8 {fmt.upper()} source {alias!r}: {exc}") from exc
    if not rows:
        _fail(f"Source {alias!r} contains no records")
    for number, row in enumerate(rows, 1):
        if not isinstance(row, dict) or not row or any(not isinstance(k, str) or not k.strip() for k in row):
            _fail(f"Source {alias!r}, row {number}: expected a record with named columns")
    return rows


def _sources(declarations, base_dir):
    if not isinstance(declarations, dict):
        _fail("data_sources must map source aliases to local file declarations")
    loaded, paths, cache = {}, [], {}
    for alias, source in declarations.items():
        _name(alias, "Source alias")
        if not isinstance(source, dict) or set(source) - {"path", "format"}:
            _fail(f"Source {alias!r} supports only path and optional format")
        value = source.get("path")
        if not isinstance(value, str) or not value.strip() or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", value):
            _fail(f"Source {alias!r} requires an explicit local file path")
        path = Path(value).expanduser()
        path = (base_dir / path if not path.is_absolute() else path).resolve()
        fmt = source.get("format", path.suffix.lstrip(".").lower())
        if not isinstance(fmt, str) or fmt.lower() not in {"csv", "tsv", "json"}:
            _fail(f"Source {alias!r} format must be csv, tsv or json")
        fmt = fmt.lower()
        if not path.is_file():
            _fail(f"Source {alias!r} file does not exist: {path.name!r}")
        key = (path, fmt)
        if key not in cache:
            cache[key] = _table_file(path, fmt, alias)
        loaded[alias] = cache[key]
        if path not in paths:
            paths.append(path)
    return loaded, paths


def _matches(actual, expected):
    if isinstance(expected, bool):
        return isinstance(actual, bool) and actual == expected
    if isinstance(expected, (int, float)):
        target = _number(expected, "where value")
        try:
            return _number(actual, "where cell") == target
        except DataBindingError:
            return False
    if expected is None:
        return actual is None
    if not isinstance(expected, str):
        _fail("where values must be scalar strings, numbers, booleans or null")
    return isinstance(actual, str) and actual == expected


def _select(table, sources, context):
    if not isinstance(table, dict) or set(table) - {"source", "where", "order_by"}:
        _fail(f"{context}.table supports source, where and order_by")
    alias = _name(table.get("source"), f"{context}.table.source")
    if alias not in sources:
        _fail(f"{context}: unknown data source {alias!r}")
    rows = sources[alias]
    where = table.get("where", {})
    if not isinstance(where, dict):
        _fail(f"{context}.table.where must map columns to scalar values")
    for column, expected in where.items():
        values = _column(rows, column, context)
        rows = [row for row, value in zip(rows, values) if _matches(value, expected)]
    if not rows:
        _fail(f"{context}: no records match the declared table selection")
    order = table.get("order_by", [])
    order = [order] if isinstance(order, str) else order
    if not isinstance(order, list) or any(not isinstance(c, str) or not c for c in order) or len(set(order)) != len(order):
        _fail(f"{context}.table.order_by must be a column name or list of distinct column names")
    keys = []
    for column in order:
        values = _column(rows, column, context)
        try:
            values = [_number(value, f"{context}.order_by.{column}") for value in values]
        except DataBindingError:
            if not all(isinstance(value, str) for value in values):
                _fail(f"{context}: ordering column {column!r} must contain comparable numbers or strings")
        keys.append(values)
    if keys:
        indices = sorted(range(len(rows)), key=lambda i: tuple(column[i] for column in keys))
        rows = [rows[i] for i in indices]
    return rows


def _category(value, context):
    if value is None or isinstance(value, (dict, list, tuple)):
        _fail(f"{context} requires non-null scalar category identifiers")
    if isinstance(value, float) and not math.isfinite(value):
        _fail(f"{context} contains a non-finite category")
    return (type(value).__name__, value)


def _order(values, context):
    if not isinstance(values, list) or not values:
        _fail(f"{context} must be a nonempty explicit axis order")
    keys = [_category(value, context) for value in values]
    if len(set(keys)) != len(keys):
        _fail(f"{context} contains duplicate category identifiers")
    return keys


def _groups(binding, rows, context, *, require_pairs=False):
    if not isinstance(binding, dict) or set(binding) - {"by", "value", "order", "pair_by", "matched_order"}:
        _fail(f"{context}.groups supports by, value, order, pair_by and matched_order")
    matched_order = binding.get("matched_order", False)
    if not isinstance(matched_order, bool):
        _fail(f"{context}.groups.matched_order must be true or false")
    if "pair_by" in binding and matched_order:
        _fail(f"{context}.groups chooses pair_by or matched_order, not both")
    if require_pairs and "pair_by" not in binding and not matched_order:
        _fail(f"{context}: paired grouped observations need pair_by or an explicit matched_order=true contract")
    names = _column(rows, binding.get("by"), context)
    values = _column(rows, binding.get("value"), context)
    grouped = {}
    for name, value in zip(names, values):
        key = _category(name, context)
        grouped.setdefault(key, []).append(_number(value, context))
    order = _order(binding["order"], context + ".groups.order") if "order" in binding else list(grouped)
    if set(order) != set(grouped):
        _fail(f"{context}.groups.order must cover exactly the observed groups")
    if "pair_by" in binding:
        subjects = _column(rows, binding["pair_by"], context + ".groups.pair_by")
        paired = {key: {} for key in order}
        for name, subject, value in zip(names, subjects, values):
            group = paired[_category(name, context)]
            identity = _category(subject, context + ".groups.pair_by")
            if identity in group:
                _fail(f"{context}: duplicate paired subject {subject!r} in group {name!r}")
            group[identity] = _number(value, context)
        reference = list(paired[order[0]])
        if any(set(group) != set(reference) for group in paired.values()):
            _fail(f"{context}: paired groups must contain exactly the same subject identities")
        return [[paired[key][subject] for subject in reference] for key in order]
    if matched_order and len({len(group) for group in grouped.values()}) != 1:
        _fail(f"{context}: matched_order requires equal group lengths")
    return [grouped[key] for key in order]


def _matrix(binding, rows, context):
    required = {"row", "column", "value", "row_order", "column_order"}
    if not isinstance(binding, dict) or set(binding) != required:
        _fail(f"{context}.matrix needs row, column, value, row_order and column_order")
    row_keys = _order(binding["row_order"], context + ".matrix.row_order")
    column_keys = _order(binding["column_order"], context + ".matrix.column_order")
    row_values = _column(rows, binding["row"], context)
    column_values = _column(rows, binding["column"], context)
    values = _column(rows, binding["value"], context)
    cells = {}
    for row, column, value in zip(row_values, column_values, values):
        key = (_category(row, context), _category(column, context))
        if key[0] not in row_keys or key[1] not in column_keys:
            _fail(f"{context}: matrix axis orders omit an observed category")
        if key in cells:
            _fail(f"{context}: duplicate matrix cell at {row!r}, {column!r}; provide an explicit aggregate instead")
        cells[key] = _number(value, context)
    missing = [(r, c) for r in row_keys for c in column_keys if (r, c) not in cells]
    if missing:
        _fail(f"{context}: missing matrix cell at {missing[0][0][1]!r}, {missing[0][1][1]!r}")
    return [[cells[(r, c)] for c in column_keys] for r in row_keys]


def _bind(value, rows, context, *, require_pairs=False):
    if isinstance(value, dict):
        # Entity color maps are literal label-to-color values, even when an
        # entity happens to be named "column", "groups", or "matrix".
        if context.endswith(".colors"):
            return copy.deepcopy(value)
        markers = set(value) & {"column", "groups", "matrix"}
        if markers:
            if rows is None:
                _fail(f"{context}: a table selection is required for a column/groups/matrix binding")
            if "column" in value:
                if set(value) - {"column", "dtype"}:
                    _fail(f"{context}: column bindings support only column and dtype")
                dtype = value.get("dtype", "number")
                if dtype not in {"number", "string"}:
                    _fail(f"{context}: dtype must be number or string")
                converter = _number if dtype == "number" else _string
                return [converter(cell, context) for cell in _column(rows, value["column"], context)]
            if set(value) == {"groups"}:
                return _groups(value["groups"], rows, context, require_pairs=require_pairs)
            if set(value) == {"matrix"}:
                return _matrix(value["matrix"], rows, context)
            _fail(f"{context}: each binding must choose exactly one of column, groups or matrix")
        return {key: _bind(item, rows, f"{context}.{key}", require_pairs=require_pairs) for key, item in value.items()}
    if isinstance(value, list):
        return [_bind(item, rows, f"{context}[{i}]", require_pairs=require_pairs) for i, item in enumerate(value)]
    return value


def _node(node, sources, context, inherited_rows=None):
    if not isinstance(node, dict):
        _fail(f"{context} must be an object")
    rows = _select(node.pop("table"), sources, context) if "table" in node else inherited_rows
    if "data" in node:
        if not isinstance(node["data"], dict):
            _fail(f"{context}.data must map renderer arguments to values or bindings")
        paired = node.get("kind") == "paired_distribution" and node["data"].get("paired", False)
        if node.get("kind") == "paired_distribution" and not isinstance(node["data"].get("paired", False), bool):
            _fail(f"{context}.data.paired must be true or false")
        node["data"] = {key: _bind(value, rows, f"{context}.data.{key}",
            require_pairs=(paired and key == "values") or (node.get("template") == "paired_effects" and key == "paired"))
            for key, value in node["data"].items()}
    if "layers" in node:
        if not isinstance(node["layers"], list) or not node["layers"]:
            _fail(f"{context}.layers must be a nonempty list")
        for i, layer in enumerate(node["layers"]):
            _node(layer, sources, f"{context}.layers[{i}]", rows)


def materialize(spec, base_dir):
    """Return a separate resolved spec and all explicitly declared source paths.

    Relative data paths use ``base_dir``. Columns retain one common selected and
    stably sorted record sequence. Numeric-looking ordering columns sort
    numerically; other string columns sort lexically. Group order defaults to
    first occurrence when omitted; matrix axes always require explicit orders.
    """
    if not isinstance(spec, dict) or spec.get("version") != 1 or isinstance(spec.get("version"), bool):
        _fail("A composition must declare version=1")
    container_keys = [key for key in ("layout", "template") if key in spec]
    if len(container_keys) > 1:
        _fail("Choose one linked layout or preserved template")
    container = spec.get(container_keys[0]) if container_keys else None
    if container_keys:
        if not isinstance(container, str) or not container.strip() or "panels" in spec:
            _fail("A linked layout or preserved template needs a nonempty name and no panels list")
        if not isinstance(spec.get("data"), dict):
            _fail("A linked layout or preserved template requires a data object")
    elif not isinstance(spec.get("panels"), list) or not spec["panels"]:
        _fail("A composition must contain a nonempty panels list")
    result = copy.deepcopy(spec)
    sources, paths = _sources(result.pop("data_sources", {}), Path(base_dir).resolve())
    if container_keys:
        _node(result, sources, container_keys[0])
    else:
        if "table" in result:
            _fail("Panel compositions declare table selections on panels or layers")
        for i, panel in enumerate(result["panels"]):
            _node(panel, sources, f"panels[{i}]")
    return result, paths


def load_composition(path):
    """Read a UTF-8/BOM composition and protect it together with its data files."""
    path = Path(path).expanduser().resolve()
    result, sources = materialize(_json(path), path.parent)
    return result, [path] + [source for source in sources if source != path]
