"""A perfect number equals the sum of its proper divisors (e.g. 28)."""


def is_perfect_number(n: int) -> bool:
    if n < 2:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n
