"""A stack that supports retrieving the minimum element in O(1)."""


class MinStack:
    def __init__(self) -> None:
        self._items: list = []
        self._minimums: list = []

    def push(self, item) -> None:
        self._items.append(item)
        current_min = min(item, self._minimums[-1]) if self._minimums else item
        self._minimums.append(current_min)

    def pop(self):
        self._minimums.pop()
        return self._items.pop()

    def get_min(self):
        if not self._minimums:
            raise IndexError("get_min from empty stack")
        return self._minimums[-1]
