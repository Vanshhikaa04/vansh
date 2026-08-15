"""Smoke test for snippets.math.sum_of_digits."""
import importlib


def test_sum_of_digits_module_imports():
    module = importlib.import_module("snippets.math.sum_of_digits")
    assert module is not None
