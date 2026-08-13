"""Generate the Collatz sequence starting at n until it reaches 1."""


def collatz_sequence(n: int) -> list[int]:
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence
