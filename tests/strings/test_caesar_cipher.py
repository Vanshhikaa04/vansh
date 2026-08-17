"""Smoke test for snippets.strings.caesar_cipher."""
import importlib


def test_caesar_cipher_module_imports():
    module = importlib.import_module("snippets.strings.caesar_cipher")
    assert module is not None
