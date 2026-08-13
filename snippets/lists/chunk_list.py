"""Split a list into fixed-size chunks."""


def chunk_list(items: list, size: int) -> list[list]:
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]
