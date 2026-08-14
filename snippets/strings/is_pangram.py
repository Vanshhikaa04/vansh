"""Check whether a sentence uses every letter of the alphabet at least once."""
import string


def is_pangram(sentence: str) -> bool:
    return set(string.ascii_lowercase) <= set(sentence.lower())
