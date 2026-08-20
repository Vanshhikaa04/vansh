"""Smoke test for snippets.misc.flatten_dict."""
import importlib


def test_flatten_dict_module_imports():
    module = importlib.import_module("snippets.misc.flatten_dict")
    assert module is not None
