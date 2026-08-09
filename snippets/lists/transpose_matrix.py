"""Transpose a 2D matrix represented as a list of lists."""


def transpose_matrix(matrix: list[list]) -> list[list]:
    return [list(row) for row in zip(*matrix)]
