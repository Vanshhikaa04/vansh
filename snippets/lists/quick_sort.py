"""Quick sort using the Lomuto partition scheme (not in-place, for clarity)."""


def quick_sort(items: list) -> list:
    if len(items) <= 1:
        return list(items)
    pivot = items[len(items) // 2]
    lesser = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]
    return quick_sort(lesser) + equal + quick_sort(greater)
