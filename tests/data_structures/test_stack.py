"""Smoke test for snippets.data_structures.stack."""
import importlib


def test_stack_module_imports():
    module = importlib.import_module("snippets.data_structures.stack")
    assert module is not None
