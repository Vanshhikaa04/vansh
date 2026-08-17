"""Smoke test for snippets.strings.is_anagram."""
import importlib


def test_is_anagram_module_imports():
    module = importlib.import_module("snippets.strings.is_anagram")
    assert module is not None
