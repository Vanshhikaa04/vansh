"""Smoke test for snippets.lists.binary_search."""
import importlib


def test_binary_search_module_imports():
    module = importlib.import_module("snippets.lists.binary_search")
    assert module is not None
