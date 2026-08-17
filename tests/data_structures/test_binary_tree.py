"""Smoke test for snippets.data_structures.binary_tree."""
import importlib


def test_binary_tree_module_imports():
    module = importlib.import_module("snippets.data_structures.binary_tree")
    assert module is not None
