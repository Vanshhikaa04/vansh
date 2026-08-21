"""Smoke test for snippets.lists.quick_sort."""
import importlib


def test_quick_sort_module_imports():
    module = importlib.import_module("snippets.lists.quick_sort")
    assert module is not None
