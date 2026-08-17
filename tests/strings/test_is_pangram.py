"""Smoke test for snippets.strings.is_pangram."""
import importlib


def test_is_pangram_module_imports():
    module = importlib.import_module("snippets.strings.is_pangram")
    assert module is not None
