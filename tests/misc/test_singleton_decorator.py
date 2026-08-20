"""Smoke test for snippets.misc.singleton_decorator."""
import importlib


def test_singleton_decorator_module_imports():
    module = importlib.import_module("snippets.misc.singleton_decorator")
    assert module is not None
