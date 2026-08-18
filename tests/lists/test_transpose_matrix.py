"""Smoke test for snippets.lists.transpose_matrix."""
import importlib


def test_transpose_matrix_module_imports():
    module = importlib.import_module("snippets.lists.transpose_matrix")
    assert module is not None
