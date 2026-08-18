"""Smoke test for snippets.strings.title_case."""
import importlib


def test_title_case_module_imports():
    module = importlib.import_module("snippets.strings.title_case")
    assert module is not None
