"""Smoke test for snippets.lists.merge_sort."""
import importlib


def test_merge_sort_module_imports():
    module = importlib.import_module("snippets.lists.merge_sort")
    assert module is not None
