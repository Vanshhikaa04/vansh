"""Smoke test for snippets.strings.word_frequency."""
import importlib


def test_word_frequency_module_imports():
    module = importlib.import_module("snippets.strings.word_frequency")
    assert module is not None
