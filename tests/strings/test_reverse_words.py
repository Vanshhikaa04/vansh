"""Smoke test for snippets.strings.reverse_words."""
import importlib


def test_reverse_words_module_imports():
    module = importlib.import_module("snippets.strings.reverse_words")
    assert module is not None
