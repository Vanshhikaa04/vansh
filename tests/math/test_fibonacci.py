"""Smoke test for snippets.math.fibonacci."""
import importlib


def test_fibonacci_module_imports():
    module = importlib.import_module("snippets.math.fibonacci")
    assert module is not None
