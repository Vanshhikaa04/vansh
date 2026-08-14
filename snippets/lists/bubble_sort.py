"""Bubble sort: simple O(n^2) in-place sort, returns a new sorted list."""


def bubble_sort(items: list) -> list:
    result = list(items)
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result
