"""Run-length encode/decode a string, e.g. "aaab" <-> "3a1b"."""
from itertools import groupby


def run_length_encode(text: str) -> str:
    return "".join(f"{len(list(group))}{char}" for char, group in groupby(text))


def run_length_decode(encoded: str) -> str:
    result = []
    count = ""
    for char in encoded:
        if char.isdigit():
            count += char
        else:
            result.append(char * int(count))
            count = ""
    return "".join(result)
