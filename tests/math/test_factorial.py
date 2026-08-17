"""Smoke test for snippets.math.factorial."""
import importlib


def test_factorial_module_imports():
    module = importlib.import_module("snippets.math.factorial")
    assert module is not None
