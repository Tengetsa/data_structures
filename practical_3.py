from typing import Any
import enum


class Color(enum.Enum):
    RED = True
    BLACK = False


class Node:
    def __init__(self, value: Any):
        self.val: Any = value
        self.color: Color = Color.RED
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node(val={self.val}, color={self.color.value}, left={self.left}, right={self.right})'


class RBT:
    def __init__(self):
        self.root = None

    def insert(self, value: Any) -> None:
        self.root = self.__insert(self.root, value)
        self.root.color = Color.BLACK

    def __insert(self, root: Node, val: Any) -> Node:
        if root is None:
            return Node(val)
        if val < root.val:
            root.left = self.__insert(root.left, val)
        elif val > root.val:
            root.right = self.__insert(root.right, val)
        else:
            root.val = val

        if self.is_red(root.right) and not self.is_red(root.left):
            root = self.rotate_left(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.rotate_right(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.flip_color(root)

        return root

    @staticmethod
    def is_red(node: Node) -> bool:
        if node is None:
            return False
        return node.color == Color.RED

    @staticmethod
    def flip_color(node: Node) -> None:
        node.color = Color.RED
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK

    def rotate_left(self, node: Node) -> Node:
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        new_root.color = node.color
        node.color = Color.RED
        print("Left Rotation !!")
        return new_root

    def rotate_right(self, node: Node) -> Node:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        new_root.color = node.color
        node.color = Color.RED
        print("Right Rotation !!")
        return new_root

    def inorder(self) -> None:
        self.__inorder(self.root)

    def __inorder(self, root: Node) -> None:
        if root is None:
            return
        self.__inorder(root.left)
        print(root.val, end=" ")
        self.__inorder(root.right)


rbt = RBT()
rbt.insert(15)
rbt.insert(22)
rbt.insert(37)
rbt.insert(42)
rbt.insert(59)
rbt.insert(25)
rbt.insert(60)
rbt.insert(2)
rbt.insert(46)

rbt.inorder()
