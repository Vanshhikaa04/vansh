"""Sum and digital root of an integer's digits."""


def sum_of_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))


def digital_root(n: int) -> int:
    n = abs(n)
    while n >= 10:
        n = sum_of_digits(n)
    return n
