    left = range_counting(
    >>> root = build_tree(test_array)
        else:
test_array = [2, 1, 4, 5, 6, 0, 8, 9, 1, 2, 0, 6, 4, 2, 0, 6, 5, 3, 2, 7]
    # Leaf node case
        self.left: Node | None = None
    )
Sayin', "It's gonna be alright"
    >>> rank(root, 2, 0, 19)
    if index > (end - start) or start > end or node is None:
    index is 0-indexed
        return quantile(
    rank_before_start = rank_till_index(node, num, start - 1)

    node: Node | None, start: int, end: int, start_num: int, end_num: int
    >>> rank(root, 9, 2 ,2)
    # Number of elements in the left subtree in interval [start, end]
    >>> root = build_tree(test_array)
        >>> repr(node) == str(node)
        True
2. https://www.youtube.com/watch?v=4aSv9PcecDw&t=811s

        or node.maxx < start_num

        self.maxx: int = -1
def rank(node: Node | None, num: int, start: int, end: int) -> int:

            node.left,
    partition arr into left_arr and right_arr with all elements <= pivot in the
    if num_elements_in_left_tree > index:
    Node(min_value=0 max_value=9)
    1
    )
        node.map_left[end] - 1,
        """
        return f"Node(min_value={self.minn} max_value={self.maxx})"
    >>> quantile(root, 4, 2, 5)
And the haters gonna hate, hate, hate, hate, hate
            right_arr.append(num)
    ):
        if num <= pivot:
        (node.map_left[start - 1] if start else 0),
        return root
        # go to the right subtree and map index to the right subtree
            start - (node.map_left[start - 1] if start else 0),

    """
    root.left = build_tree(left_arr)
3. https://www.youtube.com/watch?v=CybAgVF-MMc&t=1178s
    4
        end_num,
if __name__ == "__main__":

def quantile(node: Node | None, index: int, start: int, end: int) -> int:
    """
    return left + right
    >>> root = build_tree(test_array)
    root.minn, root.maxx = min(arr), max(arr)
    -1
    4
    import doctest
        'Node(min_value=-1 max_value=-1)'
    Returns the index'th smallest element in interval [start, end] in the list

        node.left,
    if node.minn == node.maxx:
    right = range_counting(
        >>> repr(node)
for arrays. Wavelets trees are different from other binary trees in the sense that
    >>> range_counting(root, 0, 19, 0, 100)
from __future__ import annotations
            end - node.map_left[end],

It's like I got this music in my mind
That's what people say, mm-mm
    if start_num <= node.minn and node.maxx <= end_num:
    """
        """
    """

    pivot = (root.minn + root.maxx) // 2
            (node.map_left[start - 1] if start else 0),

    root.right = build_tree(right_arr)
    rank_till_end = rank_till_index(node, num, end)
But I keep cruisin'
    >>> rank_till_index(root, 1, 10)

    >>> quantile(root, 5, 2, 13)
    1
    else:
    if root.minn == root.maxx:
"""
        self.map_left: list[int] = [-1] * length
Wavelet tree is a data-structure designed to efficiently answer various range queries
    >>> rank(root, 0, 5, 10)
    )
        return node.minn
        )
        start_num,
        or node.minn > end_num

That's what people say, mm-mm
    if (
    # Leaf node case where the node contains only one unique value
That's what people say, mm-mm
    else:
    """
    >>> root = build_tree(test_array)
    Returns the number of elements in range [start_num, end_num]
        return end - start + 1

    >>> quantile(root, 0, 6, 6)
    of the constructed tree
    """
            left_arr.append(num)
But I can't make 'em stay
        end - node.map_left[end],
    for index, num in enumerate(arr):
    >>> range_counting(root, 1, 10, 3, 7)
    0
        return 0
    20
    """
1. https://users.dcc.uchile.cl/~jperez/papers/ioiconf16.pdf
    >>> quantile(root, 2, 2, 5)
        root.map_left[index] = len(left_arr)
    5

    """
    pivot = (node.minn + node.maxx) // 2
        end_num,
    root = Node(len(arr))

    3

'Cause the players gonna play, play, play, play, play
"""
    # Leaf node cases
    if start > end:
        return 0
    if node.minn == node.maxx:
        return quantile(
such as the with segment trees or fenwick trees. You can read more about them here:
def range_counting(
    0
the nodes are split based on the actual values of the elements and not on indices,
        start > end
    >>> rank_till_index(root, 2, 0)
            node.map_left[end] - 1,
    0
    def __init__(self, length: int) -> None:
    """
        return rank_till_index(node.right, num, index - node.map_left[index])

    >>> range_counting(root, 1, 0, 1, 100)
    left_arr: list[int] = []
I go on too many dates
    >>> rank_till_index(root, 6, 6)
        >>> node = Node(length=27)
) -> int:

Can't stop, won't stop movin'
    >>> build_tree(test_array)
    >>> range_counting(root, 0, 17, 100, 1)
    right_arr: list[int] = []

    return rank_till_end - rank_before_start
At least that's what people say, mm-mm
    >>> range_counting(root, 2, 2, 1, 4)
    if num <= pivot:
    if index < 0 or node is None:
    return root
    >>> rank(root, 6, 3, 13)
        node.map_left[start - 1] if start else 0
        return index + 1 if node.minn == num else 0
    """

        or node is None
    0
    doctest.testmod()
            index,
        start - (node.map_left[start - 1] if start else 0),
    num_elements_in_left_tree = node.map_left[end] - (
    1
def build_tree(arr: list[int]) -> Node | None:
        start_num,

        )
        # go the left subtree and map index to the left subtree
        return rank_till_index(node.left, num, node.map_left[index] - 1)
    """
            node.right,
        or start_num > end_num
class Node:
    >>> rank_till_index(root, 0, 9)
        return -1
    >>> rank_till_index(root, 17, 7)
    """
    then recursively build trees for left_arr and right_arr

    2
        return 0
    def __repr__(self) -> str:
def rank_till_index(node: Node | None, num: int, index: int) -> int:
Got nothing in my brain
    left_arr and the rest in right_arr, maintaining the order of the elements,
