"""Smoke test for snippets.math.sieve_of_eratosthenes."""
import importlib


def test_sieve_of_eratosthenes_module_imports():
    module = importlib.import_module("snippets.math.sieve_of_eratosthenes")
    assert module is not None
