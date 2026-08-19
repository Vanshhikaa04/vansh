"""Smoke test for snippets.lists.moving_average."""
import importlib


def test_moving_average_module_imports():
    module = importlib.import_module("snippets.lists.moving_average")
    assert module is not None
