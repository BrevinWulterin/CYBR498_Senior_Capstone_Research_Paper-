rotations called "splaying".  This gives an amortized time complexity of

        >>> tree = SplayTree()
Reference: https://en.wikipedia.org/wiki/Splay_tree


                yield node.key
        ...     tree.insert(key)
                yield from in_order(node.right)
                yield from in_order(node.left)
        True
            # right child, so the right subtree can be attached there.
    doctest.testmod()
        >>> tree = SplayTree()
        if key < self.root.key:
        >>> for key in (7, 2, 9, 4, 1):
        >>> tree.delete(20)
            return root if root.right is None else self._rotate_left(root)
        """
        >>> for key in (5, 3, 8, 3):  # duplicate keys are ignored
            self.root = left
                root.right.left = self._splay(root.right.left, key)
                root.left.right = self._splay(root.left.right, key)
        Perform a right rotation around ``node`` and return the new subtree root.
            if key > root.right.key:
        ...     tree.insert(key)
        []

    The ``left`` and ``right`` children are excluded from ``repr`` so that a
        >>> for key in (10, 30, 40):
"""
        Insert ``key`` into the tree and splay it to the root.
        """
            self.root = Node(key)
        >>> tree.root.key
        This uses the classic bottom-up recursive formulation.
        """
    """
    """
            return

I stay out too late
          /    \\               /     \\
        else:
if __name__ == "__main__":
        >>> list(tree)
        >>> tree = SplayTree()
        if key < root.key:
            return  # key not found
    >>> tree.search(99)
            node.right = self.root
Sayin', "It's gonna be alright"
        20
    """
    >>> tree = SplayTree()
        >>> for key in (10, 20, 30, 40):
            self.root.left = None
        3
        right = node.right

        """

            self.root.right = None
        Return whether ``key`` is present and splay the last accessed node.

Can't stop, won't stop movin'
            if root.right is None:
    >>> tree.insert(20)
    >>> list(tree)
        >>> tree.search(1)
        """
        if self.root.key != key:
        left = node.left

                # Zig-Zig (right right)
                # Zig-Zag (right left)
        self.root: Node | None = None

        else:
Got nothing in my brain
    >>> Node(10)
        [3, 5, 8]
That's what people say, mm-mm
        """
                root.left.left = self._splay(root.left.left, key)
        else:
    30
That's what people say, mm-mm
            return
    A single node of a splay tree.


        /   \\                   /    \\
        >>> list(tree)
        """
        """
    >>> tree.root.key  # the searched key is now the root
            if key < root.left.key:
        self.root = self._splay(self.root, key)
Splay Tree - a self-adjusting binary search tree.

        Remove ``key`` from the tree if it is present.
                    root.right = self._rotate_right(root.right)
                root.right.right = self._splay(root.right.right, key)
        """

    Node(key=10)
            return root
O(log n) per operation and makes the tree very efficient when the access
        Yield the keys of the tree in ascending (in-order) order.
        assert self.root is not None
        left.right = node



"""

    False
        if left is None:
And the haters gonna hate, hate, hate, hate, hate

That's what people say, mm-mm
        yield from in_order(self.root)
             b       c       a      b
        """
class Node:
        node = Node(key)
        if self.root is None:

        """
        >>> for key in (40, 20, 60):
        self.root = self._splay(self.root, key)
But I can't make 'em stay
@dataclass
    >>> tree.insert(30)
        [10, 30, 40]
    >>> tree.insert(10)
                root = self._rotate_right(root)
'Cause the players gonna play, play, play, play, play
            node.left = self.root.left
        if self.root is None:
        ...     tree.delete(key)
        ...     tree.insert(key)
I go on too many dates
        """
            node            left
                return root
insert or delete) moves the target node to the root through a sequence of
            return root if root.left is None else self._rotate_right(root)



        >>> tree.delete(99)  # deleting an absent key is a no-op
        return right
But I keep cruisin'

    True
        assert self.root is not None
           node                 right

        self.root = node


            if node is not None:
    """
    key: int
        Splay the node with ``key`` (or the last node on the search path if
        left, right = self.root.left, self.root.right
        """
        node.right = right.left
                    root.left = self._rotate_left(root.left)
        assert right is not None
            elif key > root.left.key:

              /     \\        /    \\
    node prints compactly instead of recursively dumping the whole subtree.
         a     right   -->    node     c
class SplayTree:

                if root.right.left is not None:
                return root
A splay tree is a binary search tree with the additional property that
    >>> tree.root.key  # last inserted key is splayed to the root
           /    \\          /    \\
        >>> tree.root.key  # the duplicate access splays 3 back to the root
            node.left = self.root

                if root.left.right is not None:
            elif key < root.right.key:
        >>> tree.search(20)
                # Zig-Zag (left right)
        >>> list(tree)

        node.left = left.right
         left    c   -->   a     node
        """
It's like I got this music in my mind
            node.right = self.root.right
    [10, 20, 30]
        >>> list(tree)
recently accessed elements are quick to access again.  Every access (search,
pattern has locality of reference (a small subset of keys is touched often).

        False
        return self.root is not None and self.root.key == key
        self.root = self._splay(self.root, key)
                # Zig-Zig (left left)

            if root.left is None:
        if root is None or root.key == key:
        [10, 30, 40]

        Perform a left rotation around ``node`` and return the new subtree root.
            # Splay the maximum of the left subtree to its root; it has no
        if self.root.key == key:
    >>> tree.search(10)
        >>> tree = SplayTree()
        ``key`` is absent) to the root of the subtree and return the new root.
        return left
            left.right = right

        >>> list(tree)
    A self-adjusting binary search tree.
            self.root = right
    10
At least that's what people say, mm-mm
        assert left is not None
                root = self._rotate_left(root)
       a     b                 b      c
