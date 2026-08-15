"""Smoke test for snippets.math.gcd_lcm."""
import importlib


def test_gcd_lcm_module_imports():
    module = importlib.import_module("snippets.math.gcd_lcm")
    assert module is not None
