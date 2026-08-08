"""Check whether a string reads the same forwards and backwards,
ignoring case, spaces, and punctuation."""
import re


def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]
