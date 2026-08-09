"""Reverse the order of words in a sentence."""


def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])
