"""Check whether a number equals the sum of its digits raised to the
power of the digit count (e.g. 153 = 1**3 + 5**3 + 3**3)."""


def is_armstrong_number(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)
