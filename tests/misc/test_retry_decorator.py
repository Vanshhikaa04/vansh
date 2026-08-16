"""Smoke test for snippets.misc.retry_decorator."""
import importlib


def test_retry_decorator_module_imports():
    module = importlib.import_module("snippets.misc.retry_decorator")
    assert module is not None
