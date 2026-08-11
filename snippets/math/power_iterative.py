"""Compute base ** exponent using fast exponentiation (O(log n))."""


def power(base: float, exponent: int) -> float:
    if exponent < 0:
        return 1 / power(base, -exponent)
    result = 1.0
    while exponent:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result
