"""Smoke test for snippets.strings.is_palindrome."""
import importlib


def test_is_palindrome_module_imports():
    module = importlib.import_module("snippets.strings.is_palindrome")
    assert module is not None
