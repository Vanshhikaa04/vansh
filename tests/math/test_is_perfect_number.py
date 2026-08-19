"""Smoke test for snippets.math.is_perfect_number."""
import importlib


def test_is_perfect_number_module_imports():
    module = importlib.import_module("snippets.math.is_perfect_number")
    assert module is not None
