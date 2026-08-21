"""Smoke test for snippets.math.power_iterative."""
import importlib


def test_power_iterative_module_imports():
    module = importlib.import_module("snippets.math.power_iterative")
    assert module is not None
