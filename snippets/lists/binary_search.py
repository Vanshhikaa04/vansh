"""Binary search over a sorted list; returns the index or -1."""


def binary_search(sorted_items: list, target) -> int:
    low, high = 0, len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
