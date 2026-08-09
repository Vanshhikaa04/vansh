"""Iterative and recursive factorial implementations."""


def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    return 1 if n <= 1 else n * factorial_recursive(n - 1)
