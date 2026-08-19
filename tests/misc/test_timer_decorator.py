"""Smoke test for snippets.misc.timer_decorator."""
import importlib


def test_timer_decorator_module_imports():
    module = importlib.import_module("snippets.misc.timer_decorator")
    assert module is not None
