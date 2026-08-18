"""Smoke test for snippets.strings.dedupe_preserve_order."""
import importlib


def test_dedupe_preserve_order_module_imports():
    module = importlib.import_module("snippets.strings.dedupe_preserve_order")
    assert module is not None
