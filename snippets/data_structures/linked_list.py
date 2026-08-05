"""A minimal singly linked list with append and to_list."""
from __future__ import annotations


class _Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: "_Node | None" = None


class LinkedList:
    def __init__(self) -> None:
        self._head: "_Node | None" = None

    def append(self, value) -> None:
        node = _Node(value)
        if self._head is None:
            self._head = node
            return
        current = self._head
        while current.next:
            current = current.next
        current.next = node

    def to_list(self) -> list:
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result
