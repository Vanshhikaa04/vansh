"""Smoke test for snippets.math.is_armstrong_number."""
import importlib


def test_is_armstrong_number_module_imports():
    module = importlib.import_module("snippets.math.is_armstrong_number")
    assert module is not None
