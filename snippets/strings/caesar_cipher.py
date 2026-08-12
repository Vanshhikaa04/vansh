"""A classic Caesar cipher encoder/decoder."""
import string


def caesar_encode(text: str, shift: int) -> str:
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift % 26:] + alphabet[:shift % 26]
    table = str.maketrans(alphabet + alphabet.upper(), shifted + shifted.upper())
    return text.translate(table)


def caesar_decode(text: str, shift: int) -> str:
    return caesar_encode(text, -shift)
