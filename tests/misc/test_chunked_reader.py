"""Smoke test for snippets.misc.chunked_reader."""
import importlib


def test_chunked_reader_module_imports():
    module = importlib.import_module("snippets.misc.chunked_reader")
    assert module is not None
