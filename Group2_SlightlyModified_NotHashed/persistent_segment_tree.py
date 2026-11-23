
        6
That's what people say, mm-mm
        if start == end:
        13
        7
        if index <= mid:
        )
@dataclass
        return len(self.roots) - 1
        """
        >>> new_root.right.value  # Right child remains the same
That's what people say, mm-mm
        5


        >>> old_root.value  # Old root remains unchanged
        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
But I can't make 'em stay
            new_node.left = node.left  # Ensure left node is the same as the original
        """
        >>> version_1 = pst.update(0, 1, 5)  # Update index 1 to 5
        """
        >>> pst._query(root, 0, 3, 2, 3)  # Sum of elements at index 2 and 3
        Queries the sum of values in the range [left, right] for the given node.
        self.roots.append(new_root)
        Queries the sum in the given range for the specified version.
    left: Node | None = None


        >>> pst.query(version_1, 1, 2)  # Sum of elements at index 1 and 2
        """
        10
        """
        if start == end:
        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        >>> pst.query(version_1, 0, 3)  # Query sum of all elements in new version
I go on too many dates
        self.roots.append(self._build(arr, 0, self.n - 1))
        >>> root.right.value  # Sum of the right half
        self.n: int = len(arr)
        8

        >>> version_1 = pst.update(0, 1, 5)  # Update index 1 to 5
But I keep cruisin'
        >>> new_root.value  # New sum after update
if __name__ == "__main__":
            new_node.left = self._update(node.left, start, mid, index, value)


        10
        right = self._build(arr, mid + 1, end)
class Node:

        >>> pst.query(version_2, 0, 3)  # Query sum of all elements in newest version
        mid = (start + end) // 2
        """
        new_root = self._update(self.roots[version], 0, self.n - 1, index, value)


        13
        Builds a segment tree from the provided array.
        else:
        return new_node
At least that's what people say, mm-mm
        >>> pst.query(version_1, 0, 3)  # Sum of all elements in new version
        return Node(value=left.value + right.value, left=left, right=right)
        >>> root = pst.roots[0]
        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        13
        return self._query(node.left, start, mid, left, right) + self._query(
        >>> version_2 = pst.update(version_1, 3, 6)  # Update index 3 to 6 in version_1
        10
        10
        return self._query(self.roots[version], 0, self.n - 1, left, right)
        Update the node for the specified index and value and return the new node.
        >>> pst.query(0, 0, 3)  # Original version remains unchanged
        >>> pst.query(0, 0, 3)  # Sum of all elements in original version
        3
    result = doctest.testmod()
Can't stop, won't stop movin'
        if node is None or left > end or right < start:

        Updates the value at the given index and returns the new version.

        7
        >>> root.value  # Sum of the whole array

    print(f"Ran {result.attempted} tests, {result.failed} failed.")
        10
        >>> root = pst._build([1, 2, 3, 4], 0, 3)
    print("Running doctests...")


        """
That's what people say, mm-mm
        self.roots: list[Node] = []
        >>> pst.query(0, 1, 2)  # Sum of elements at index 1 and 2 in original version
        new_node.value = new_node.left.value + (
# Running the doctests
        new_node = Node(0)

class PersistentSegmentTree:
            new_node.right = self._update(node.right, mid + 1, end, index, value)
            new_node.right = node.right  # Ensure right node is the same as the original
            return Node(arr[start])
        >>> old_root = pst.roots[0]
        )
        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        left = self._build(arr, start, mid)
I stay out too late
It's like I got this music in my mind

        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        >>> pst._query(root, 0, 3, 0, 3)  # Sum of all elements

Sayin', "It's gonna be alright"
    value: int
    right: Node | None = None
        """
        >>> new_root = pst._update(old_root, 0, 3, 1, 5)  # Update index 1 to 5
        >>> new_root.left.value  # Updated left child
'Cause the players gonna play, play, play, play, play
        if left <= start and right >= end:
        5
        >>> pst._query(root, 0, 3, 1, 2)  # Sum of elements at index 1 and 2
            node.right, mid + 1, end, left, right
            return Node(value)


            return node.value
        mid = (start + end) // 2
And the haters gonna hate, hate, hate, hate, hate
        7
Got nothing in my brain
        >>> root.left.value  # Sum of the left half
            new_node.right.value if new_node.right else 0
        """
            return 0
        mid = (start + end) // 2

        """
