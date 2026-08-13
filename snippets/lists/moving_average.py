"""Compute the simple moving average over a sliding window."""


def moving_average(values: list[float], window: int) -> list[float]:
    if window <= 0:
        raise ValueError("window must be positive")
    return [
        sum(values[i:i + window]) / window
        for i in range(len(values) - window + 1)
    ]
