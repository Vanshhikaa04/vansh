"""Smoke test for snippets.misc.memoize_decorator."""
import importlib


def test_memoize_decorator_module_imports():
    module = importlib.import_module("snippets.misc.memoize_decorator")
    assert module is not None
