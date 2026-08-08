"""Return elements that appear more than once, preserving first-seen order."""
from collections import Counter


def find_duplicates(items: list) -> list:
    counts = Counter(items)
    seen = set()
    result = []
    for item in items:
        if counts[item] > 1 and item not in seen:
            seen.add(item)
            result.append(item)
    return result
