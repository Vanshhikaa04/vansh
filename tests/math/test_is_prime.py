"""Smoke test for snippets.math.is_prime."""
import importlib


def test_is_prime_module_imports():
    module = importlib.import_module("snippets.math.is_prime")
    assert module is not None
