"""Fibonacci sequence generators."""
from functools import lru_cache


def fibonacci_iterative(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    return n if n < 2 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
