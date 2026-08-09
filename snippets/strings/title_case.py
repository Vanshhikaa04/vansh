"""Title-case a sentence while keeping small connector words lowercase."""

_SMALL_WORDS = {"a", "an", "the", "and", "but", "or", "of", "in", "on", "to"}


def title_case(sentence: str) -> str:
    words = sentence.split()
    result = []
    for i, word in enumerate(words):
        lowered = word.lower()
        if i != 0 and lowered in _SMALL_WORDS:
            result.append(lowered)
        else:
            result.append(lowered.capitalize())
    return " ".join(result)
