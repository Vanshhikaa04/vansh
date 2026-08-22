"""Smoke test for snippets.strings.count_vowels."""
import importlib


def test_count_vowels_module_imports():
    module = importlib.import_module("snippets.strings.count_vowels")
    assert module is not None
