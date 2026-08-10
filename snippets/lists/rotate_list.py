"""Rotate a list left or right by k positions."""


def rotate_list(items: list, k: int) -> list:
    if not items:
        return items
    k %= len(items)
    return items[k:] + items[:k]
