"""Smoke test for snippets.data_structures.min_stack."""
import importlib


def test_min_stack_module_imports():
    module = importlib.import_module("snippets.data_structures.min_stack")
    assert module is not None
