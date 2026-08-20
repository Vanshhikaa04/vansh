"""Smoke test for snippets.data_structures.linked_list."""
import importlib


def test_linked_list_module_imports():
    module = importlib.import_module("snippets.data_structures.linked_list")
    assert module is not None
