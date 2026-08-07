"""Flatten a nested dictionary into dotted-key form,
e.g. {"a": {"b": 1}} -> {"a.b": 1}."""


def flatten_dict(nested: dict, parent_key: str = "", sep: str = ".") -> dict:
    items: dict = {}
    for key, value in nested.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep=sep))
        else:
            items[new_key] = value
    return items
