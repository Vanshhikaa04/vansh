"""Smoke test for snippets.lists.find_duplicates."""
import importlib


def test_find_duplicates_module_imports():
    module = importlib.import_module("snippets.lists.find_duplicates")
    assert module is not None
