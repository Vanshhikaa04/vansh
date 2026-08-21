"""Smoke test for snippets.math.collatz_sequence."""
import importlib


def test_collatz_sequence_module_imports():
    module = importlib.import_module("snippets.math.collatz_sequence")
    assert module is not None
