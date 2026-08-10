"""Count word frequency in a block of text."""
import re
from collections import Counter


def word_frequency(text: str) -> Counter:
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words)
