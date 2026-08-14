"""Recursively flatten an arbitrarily nested list."""
from collections.abc import Iterable


def flatten_list(items: Iterable) -> list:
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
