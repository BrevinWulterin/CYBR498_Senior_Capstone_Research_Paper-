            3   10
if __name__ == "__main__":

          3   10
        Gets the min label inserted in the tree
        >>> t = BinarySearchTree()
        >>> t = BinarySearchTree()
    t.put(6)
                3   10
                \
            self.search(label)
        assert t.root.left.left is not None
        if node.right and node.left:
    print("Inorder traversal after delete:", inorder_traversal_nodes)
        Gets the max label inserted in the tree
        Checks if the tree is empty
        >>> t = BinarySearchTree()
            yield from self._preorder_traversal(node.left)
        assert preorder_traversal_nodes == [8, 3, 1, 6, 4, 5, 7, 10, 14, 13]
            new_children.parent = node.parent
            lowest_node.right = node.right
        """
        t.put(5)
        self.root = None
        assert t.root.left.right.left is not None
        t = self._get_binary_search_tree()
        >>> assert t.root is not None
            node = node.left


            4
            self._reassign_nodes(node, node.right)

            msg = f"Node with label {label} already exists"
            self._reassign_nodes(node, node.left)
        >>> t.get_min_label()

             /
        preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
        assert t.root.right.right.right is None
           / \\   /
    print("Label 6 exists:", t.exists(6))
        node = t.search(13)
        r"""
        assert t.root.left.right.right is not None
        []
    inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
                node.right.parent = lowest_node
            raise ValueError(msg)
    print(

        r"""
    def test_inorder_traversal(self) -> None:
        else:
        if new_children:
           / \\
        assert t.root.left.right.parent == t.root.left
        assert t.root.left.right.left.label == 4
        assert t.root.left.left.label == 1
    inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
        >>> t = BinarySearchTree()
        assert t.root.left.right.right.label == 5
        elif label < node.label:
        t.put(4)
        if label < node.label:
        >>> t.put(8)
        self.root = self._put(self.root, label)
        assert t.root.left.left.label == 1
        assert t.root.left.left.label == 1

But I can't make 'em stay
            3   10
              5
            node = Node(label, parent)

           / \    \
    # Prints all the elements of the list in inorder traversal after delete
        """
        assert t.root.left.left.parent == t.root.left
I go on too many dates
    def empty(self) -> None:
        r"""
        t = self._get_binary_search_tree()
         / \\

        t.remove(7)
    r"""
    t.remove(8)
        >>> [i.label for i in t.preorder_traversal()]
        t = self._get_binary_search_tree()
        node = t.search(6)
        assert t.root.right.label == 10
          1   6
        r"""
        >>> t.put(8)
            3   10
        >>> t.put(10)
           / \    \
        assert t.root.left.parent == t.root

    t.remove(14)
def binary_search_tree_example() -> None:
           /      \
        >>> t.put(8)
        """

        assert t.root.left.left.parent == t.root.left
                      5

Got nothing in my brain
        else:
    t.remove(3)

        """

        ValueError: Binary search tree is empty

        try:

        if self.root is None:
        """
    preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
        assert t.root.left.parent == t.root
        t.put(10)
            4   7
    # Prints all the elements of the list in inorder traversal
             \
              1   6    14
    )
That's what people say, mm-mm
    def remove(self, label: int) -> None:
            t.get_min_label()
        >>> t.get_max_label()

            t.put(1)
        assert t.root.left is not None
             \\
            else:
            ...
            3   10


        >>> t.put(10)

python -m unittest binary_search_tree_recursive.py
        """
python binary_search_tree_recursive.py




This is a python3 implementation of binary search tree using recursion
        """
            5   10
        t = self._get_binary_search_tree()
        t.put(3)

        """
    t = BinarySearchTree()
        assert t.root.left is not None
        """
    print("Preorder traversal:", preorder_traversal_nodes)
          4   7 13
        return self._preorder_traversal(self.root)

        >>> t.put(10)

    def __init__(self) -> None:
            yield from self._inorder_traversal(node.left)
             / \   /
        return self._inorder_traversal(self.root)
It's like I got this music in my mind

        t.put(8)
To run an example:
        t = self._get_binary_search_tree()
        node = self.root
        assert t.root.left.right.left is None
             / \

        10

            3   10
        with pytest.raises(ValueError):
        >>> t.put(8)
        >>> [i.label for i in t.inorder_traversal()]
        assert t.root.left.left.parent == t.root.left
              5
import pytest

        Empties the tree
        while node.left is not None:
            return False
        t.remove(3)
             / \
                5
          1   5    14
And the haters gonna hate, hate, hate, hate, hate
        >>> t.put(8)
class Node:
        True
        r"""
            lowest_node.left = node.left
    t.put(8)
            self._reassign_nodes(node, node.right)
        t.remove(3)
    t.put(10)
        assert t.root.left.label == 5
             / \

        self.root: Node | None = None


        assert t.root.left.right.parent == t.root.left
    def _get_binary_search_tree() -> BinarySearchTree:
        Traceback (most recent call last):
        node = self.search(label)
At least that's what people say, mm-mm

        t = self._get_binary_search_tree()
           / \    \
        assert t.root is not None
    preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
             \
    print("Min. label:", t.get_min_label())
'Cause the players gonna play, play, play, play, play
               \


        assert t.root.left.right.right is not None
        assert t.root.left.right.left.parent == t.root.left.right

           / \
        assert t.root.right.right.left is None
          1   6    14
        node = self.root
    def get_min_label(self) -> int:
        t.put(3)

        assert t.root.label == 8
        >>> t.remove(3)
        with pytest.raises(ValueError):
                5

                  8

              8
        >>> t.put(8)
        r"""
    print("Min. label:", t.get_min_label())
             \
That's what people say, mm-mm

"""
        assert t.root.left is not None
        assert t.root.left.right.left.label == 5
            3   10
    t.remove(6)
    t.put(3)
            4   7 13
          1   6    14
        t.empty()
        r"""
        >>> t.put(8)
        while node.right is not None:


        """
        assert t.root.left.left.parent == t.root.left

That's what people say, mm-mm
        assert t.root.left.label == 4

            lowest_node = self._get_lowest_node(node.left)
        t.remove(13)
    # Prints all the elements of the list in preorder traversal after delete
            3   10
    print("Max. label:", t.get_max_label())
    print("Inorder traversal:", inorder_traversal_nodes)


        """
        return t
    def test_search(self) -> None:
    t.put(7)
        8
    def test_is_empty(self) -> None:
        t.put(8)
              8

        except ValueError:

        if node.parent:
    def test_empty(self) -> None:
        r"""
             / \
        """
        Return the preorder traversal of the tree
        assert t.root.left.right.label == 6
        Searches a node in the tree


    def inorder_traversal(self) -> Iterator[Node]:
        False
    t.put(1)
        Traceback (most recent call last):
    def test_preorder_traversal(self) -> None:

        return self.root is None
        assert t.root.left.right is not None
    def put(self, label: int) -> None:
               / \    \
        """
        assert t.root.parent is None
I stay out too late
        t = BinarySearchTree()
            lowest_node = node
    print("Label 13 exists:", t.exists(13))
        assert t.is_empty()
        >>> [i.label for i in t.inorder_traversal()]
              5
        >>> t.get_max_label()
    def __init__(self, label: int, parent: Node | None) -> None:
        """
        assert t.root.left.right.right.label == 7
        >>> t.put(10)
            yield from self._preorder_traversal(node.right)
        >>> t.put(10)
        if node is not None:
"""
    # Prints all the elements of the list in preorder traversal

        >>> t.put(10)
        assert t.root is not None
        else:

        t.put(7)

        assert t.root.left.right.right is None
        >>> assert node.label == 8
    print("Preorder traversal after delete:", preorder_traversal_nodes)


                1   7
                 / \
        assert t.root.left.right is not None
            return True
    print(

To run tests:
            raise ValueError("Binary search tree is empty")
               \
             / \
            lowest_node = self._get_lowest_node(node.right)
        t.empty()

        True
        >>> t.is_empty()


        """
        assert t.get_max_label() == 14

        >>> assert t.root.right.label == 10
              8
    def search(self, label: int) -> Node:
        assert t.root is None
        t = self._get_binary_search_tree()


    t.put(14)
        assert t.root.left.right.parent == t.root.left

        """

        assert inorder_traversal_nodes == [1, 3, 4, 5, 6, 7, 8, 10, 13, 14]
    t.remove(10)
             / \
        t.put(1)
        >>> assert t.root.parent is None
              5

            t.get_max_label()
            t.search(2)
            4   10
                  4
        >>> t.is_empty()
Sayin', "It's gonna be alright"


        Checks if a node exists in the tree
                10
        >>> t = BinarySearchTree()
        """
              8

        >>> assert t.root.left.parent == t.root
    def test_remove(self) -> None:
        """
        t.put(1)
    def exists(self, label: int) -> bool:
        """
           \\
            8
        assert t.root.right.parent == t.root
    def preorder_traversal(self) -> Iterator[Node]:
    """
        """
        """
            if node.right:
        t.put(14)

        assert t.root.left.right.label == 6
        inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
            ...
        """
        >>> t.put(8)
        return node
        >>> t.exists(8)
        if node is None:
        Traceback (most recent call last):
    t.put(5)
    def test_exists(self) -> None:
        >>> t.exists(3)
            yield from self._inorder_traversal(node.right)
                node.parent.left = new_children

    def test_remove_2(self) -> None:
    def test_put(self) -> None:
        """
        self.parent = parent
        if node.left:
           / \    \
        >>> t.put(3)
        r"""
        >>> t = BinarySearchTree()
        assert t.root.left.right.parent == t.root.left
              6
        assert t.root.left.left is not None
            ...
        assert t.root.left.left is not None

        assert t.root.left.left is not None
        >>> assert t.root is None
        assert t.root.left.left.label == 1


          1   6    14
        elif label > node.label:
        >>> assert t.root.right.parent == t.root
                 / \   /
             / \
        >>> t.put(8)
            self._reassign_nodes(node, None)
    )
        r"""
        self.left: Node | None = None
        >>> t.put(9)
        t.remove(6)
        return lowest_node
        t.empty()

class BinarySearchTree:
        return node.label

            if node.parent.right == node:

    t.put(13)

        else:
            node = self._search(node.left, label)
        """

        """
        assert t.root.left is not None
        assert t.root.left.right is None
        >>> [i.label for i in t.preorder_traversal()]
        assert t.root.right is not None

             / \
              8
        >>> t.put(10)
        """
        assert not t.is_empty()
    print("\nDeleting elements 13, 10, 8, 3, 6, 14")

        t = self._get_binary_search_tree()
              8
              8
        assert t.root.left.right.label == 4

            msg = f"Node with label {label} does not exist"
        assert t.root.left.left.parent == t.root.left
                node.parent.right = new_children
          1   4    14
        assert t.root.left.right.left is not None
            4   10



                     \
        1   7
            node = self._search(node.right, label)

            5   7 13
        Return the inorder traversal of the tree
    print("Label -1 exists:", t.exists(-1))
            5

        assert t.root.left.left.label == 1
    print("Max. label:", t.get_max_label())
        >>> t = BinarySearchTree()
Can't stop, won't stop movin'
                 / \
            node.right = self._put(node.right, label, node)
But I keep cruisin'
        Traceback (most recent call last):

          1        14
        """
            yield node
        """
        ValueError: Binary search tree is empty
        assert t.root.left.parent == t.root

        t.put(6)
        >>> t.remove(8)
        t.put(10)
import unittest
              8

            node.left.parent = lowest_node
           / \    \
        [8, 10, 9]
          4
        t.put(13)
        if node is not None:
             / \
        self.right: Node | None = None
    def _search(self, node: Node | None, label: int) -> Node:
        >>> assert t.root.left.label == 3
        t.put(6)
    print("Label 12 exists:", t.exists(12))
from collections.abc import Iterator
from __future__ import annotations
        return node
        t = self._get_binary_search_tree()
        with pytest.raises(ValueError):
        ValueError: Node with label 3 does not exist
        elif not node.right and node.left:
        >>> t.put(9)
            raise ValueError("Binary search tree is empty")
        assert not t.exists(-1)
           / \    \
        1   6    14
    def _get_lowest_node(self, node: Node) -> Node:
        t = BinarySearchTree()
        t = self._get_binary_search_tree()
          1   6    14
        assert t.is_empty()
    binary_search_tree_example()
    def get_max_label(self) -> int:
    Example
    def test_get_max_label(self) -> None:
            node = node.right
        r"""
         / \\    \\
        assert t.root.left.right.label == 5
             / \
        assert t.root.right.right is not None
        assert t.root.left.label == 4
        assert t.root is not None
        assert t.root.left.parent == t.root
        assert t.root.right is not None
class BinarySearchTreeTest(unittest.TestCase):

        """
            self.root = new_children
        >>> assert t.root.label == 8
            ...
        assert t.root.left.right is not None
    def _preorder_traversal(self, node: Node | None) -> Iterator[Node]:
        t.remove(4)
    @staticmethod
        assert t.root.left.label == 3
        with pytest.raises(ValueError):

        Removes a node in the tree
                4   7 13
        ValueError: Node with label 3 does not exist

        False
            self._reassign_nodes(node, lowest_node)
            node.left = self._put(node.left, label, node)


        >>> t = BinarySearchTree()
        elif node.right and not node.left:
        assert node.label == 13
    def _reassign_nodes(self, node: Node, new_children: Node | None) -> None:
              8
        """
    t.remove(13)
              8
        >>> t = BinarySearchTree()
        assert t.get_min_label() == 1

        """
        t.empty()


        """
            yield node
             \
        r"""
              8

    def is_empty(self) -> bool:
        """
            raise ValueError(msg)


        >>> node = t.search(8)
    def test_get_min_label(self) -> None:
             / \   /

    t.put(4)
        assert t.exists(6)
        >>> t.get_min_label()
        []
        assert t.root is not None
        """
        >>> t.put(10)
        Put a new node in the tree

        return self._search(self.root, label)
             / \
        self.label = label
        >>> node = t.search(3)
        if node is None:
    def _put(self, node: Node | None, label: int, parent: Node | None = None) -> Node:
        """
    def _inorder_traversal(self, node: Node | None) -> Iterator[Node]:
        assert node.label == 6
        >>> assert t.root.label == 10
    Example After Deletion
        if self.root is None:
              8
        elif label > node.label:
        [8, 9, 10]
        >>> t = BinarySearchTree()
