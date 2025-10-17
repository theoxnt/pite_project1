# tests/test_usefullFunctions.py
import pytest
from pite_project1.usefullFunctions import _coerce_value, filter_ok, compute

# -------------------------
# Tests pour _coerce_value
# -------------------------
def test_coerce_value_int():
    assert _coerce_value("3") == 3
    assert _coerce_value("0") == 0
    assert _coerce_value(5) == 5  # int input

def test_coerce_value_float():
    assert _coerce_value("3.5") == 3.5
    assert _coerce_value("0.0") == 0.0
    assert _coerce_value(2.0) == 2.0  # float input

def test_coerce_value_invalid():
    assert _coerce_value("abc") == 0
    assert _coerce_value(None) == 0
    assert _coerce_value([]) == 0

# -------------------------
# Tests pour filter_ok
# -------------------------
def test_filter_ok_basic():
    data = [
        {"status": "ok", "value": 5},
        {"status": "bad", "value": 2},
        {"STATUS": "OK", "value": "7"},
        {"status": "ok", "value": "abc"}  # invalid value
    ]
    filtered = filter_ok(data, threshold=5)
    assert len(filtered) == 2
    assert all(d["status"] == "ok" for d in filtered)
    assert all(d["value"] >= 5 for d in filtered)

def test_filter_ok_empty_and_malformed():
    data = [
        "not a dict",
        {"value": 10},  # missing status
        {"status": "ok"}  # missing value
    ]
    filtered = filter_ok(data)
    assert len(filtered) == 1
    assert filtered[0]["value"] == 0  # missing value defaults to 0

# -------------------------
# Tests pour compute
# -------------------------
def test_compute_basic():
    items = [{"value": 2}, {"value": 4}, {"value": 6}]
    res = compute(items)
    assert res["count"] == 3
    assert res["sum"] == 12
    assert res["avg"] == 4

def test_compute_empty():
    res = compute([])
    assert res["count"] == 0
    assert res["sum"] == 0
    assert res["avg"] == 0

def test_compute_missing_value():
    items = [{"value": 2}, {}, {"value": 6}]
    res = compute(items)
    assert res["count"] == 3
    assert res["sum"] == 8  # missing value defaults to 0
    assert res["avg"] == pytest.approx(8/3)
