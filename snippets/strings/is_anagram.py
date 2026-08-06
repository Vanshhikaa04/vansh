"""Check whether two strings are anagrams of each other."""
from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    normalize = lambda s: Counter(s.lower().replace(" ", ""))
    return normalize(a) == normalize(b)
