"""Smoke test for snippets.lists.flatten_list."""
import importlib


def test_flatten_list_module_imports():
    module = importlib.import_module("snippets.lists.flatten_list")
    assert module is not None
