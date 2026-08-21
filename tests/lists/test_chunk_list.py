"""Smoke test for snippets.lists.chunk_list."""
import importlib


def test_chunk_list_module_imports():
    module = importlib.import_module("snippets.lists.chunk_list")
    assert module is not None
