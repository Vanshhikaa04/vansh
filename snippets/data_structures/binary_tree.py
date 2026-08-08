"""A minimal binary search tree with insert and in-order traversal."""
from __future__ import annotations


class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None

    def insert(self, value) -> None:
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder(self) -> list:
        left = self.left.inorder() if self.left else []
        right = self.right.inorder() if self.right else []
        return left + [self.value] + right
