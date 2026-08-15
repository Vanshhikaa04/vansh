"""Smoke test for snippets.lists.insertion_sort."""
import importlib


def test_insertion_sort_module_imports():
    module = importlib.import_module("snippets.lists.insertion_sort")
    assert module is not None
