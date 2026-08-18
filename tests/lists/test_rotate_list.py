"""Smoke test for snippets.lists.rotate_list."""
import importlib


def test_rotate_list_module_imports():
    module = importlib.import_module("snippets.lists.rotate_list")
    assert module is not None
