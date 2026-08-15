"""Smoke test for snippets.strings.run_length_encoding."""
import importlib


def test_run_length_encoding_module_imports():
    module = importlib.import_module("snippets.strings.run_length_encoding")
    assert module is not None
