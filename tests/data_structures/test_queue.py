"""Smoke test for snippets.data_structures.queue."""
import importlib


def test_queue_module_imports():
    module = importlib.import_module("snippets.data_structures.queue")
    assert module is not None
