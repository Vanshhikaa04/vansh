"""Smoke test for snippets.strings.longest_common_prefix."""
import importlib


def test_longest_common_prefix_module_imports():
    module = importlib.import_module("snippets.strings.longest_common_prefix")
    assert module is not None
