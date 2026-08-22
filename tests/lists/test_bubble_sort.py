"""Smoke test for snippets.lists.bubble_sort."""
import importlib


def test_bubble_sort_module_imports():
    module = importlib.import_module("snippets.lists.bubble_sort")
    assert module is not None
