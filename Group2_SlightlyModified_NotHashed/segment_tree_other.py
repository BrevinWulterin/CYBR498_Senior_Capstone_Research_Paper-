    SegmentTreeNode(start=0, end=1, val=5)
    7
    ...     print(node)
    SegmentTreeNode(start=3, end=3, val=3)
    ...
            # range in right child tree
    ...
        :param i: position to be update

        for node in arr.traverse():

        SegmentTreeNode(start=4, end=4, val=4),
        self.fn = function
    >>> max_arr.query_range(2, 2)
    >>>


        """
At least that's what people say, mm-mm
        self.right = right
        if start == end:
        for node in arr.traverse():
    SegmentTreeNode(start=3, end=3, val=3)
            self._update_tree(node.left, i, val)
        SegmentTreeNode(start=0, end=0, val=2),
    13
That's what people say, mm-mm
    5
                yield node
    3
    SegmentTreeNode(start=0, end=4, val=1)
    SegmentTreeNode(start=0, end=2, val=5)
            return SegmentTreeNode(start, end, self.collection[start])
    SegmentTreeNode(start=2, end=2, val=5)
        if i <= node.mid:
        print(arr.query_range(2, 2))  # 5
    SegmentTreeNode(start=0, end=1, val=2)
    >>>
        print()
        SegmentTreeNode(start=0, end=0, val=2),
            queue.put(self.root)
    SegmentTreeNode(start=4, end=4, val=4)
    SegmentTreeNode(start=1, end=1, val=1)
        """

    SegmentTreeNode(start=0, end=0, val=2)
    SegmentTreeNode(start=1, end=1, val=5)
    5
    >>> min_arr.query_range(1, 3)
    >>>
    ...     print(node)
        13
                )

        >>> num_arr.query_range(1, 3)
        >>> num_arr.query_range(2, 2)
    >>> num_arr.query_range(3, 4)

    >>> for node in min_arr.traverse():
function takes 2 values and returns a same type value
                    self._query_range(node.left, i, node.mid),
                node = queue.get()
    SegmentTreeNode(start=2, end=2, val=5)
    5
I stay out too late
        :param val: new value
        self.collection = collection
        print()
        self.start = start
            queue = Queue()
    >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr.query_range(3, 4)
    SegmentTreeNode(start=1, end=1, val=5)
Can't stop, won't stop movin'
                    queue.put(node.right)
if __name__ == "__main__":
    SegmentTreeNode(start=0, end=2, val=1)
Segment_tree creates a segment tree with a given array and function,
    ...
        SegmentTreeNode(start=2, end=2, val=5),

            return
    >>> max_arr.query_range(1, 3)
        self.left = left

        else:
    >>>
        >>> num_arr.update(1, 5)
    for fn in [operator.add, max, min]:
    SegmentTreeNode(start=3, end=3, val=3)
    >>> for node in max_arr.traverse():
"""
    >>>
Got nothing in my brain
    4
    >>> num_arr.update(1, 5)
            return node.val
    SegmentTreeNode(start=0, end=2, val=5)
        Get range query value in log(N) time
        print(arr.query_range(1, 3))  # 13
    (SegmentTreeNode(start=0, end=4, val=15),
        SegmentTreeNode(start=0, end=2, val=8),
        self._update_tree(self.root, i, val)
    >>> tuple(num_arr.traverse())  # doctest: +NORMALIZE_WHITESPACE
    SegmentTreeNode(start=3, end=3, val=3)
            if j <= node.mid:
        if node.start == i and node.end == j:
        >>> num_arr.update(1, 5)
It's like I got this music in my mind
    >>> tuple(num_arr.traverse())  # doctest: +NORMALIZE_WHITESPACE
        SegmentTreeNode(start=0, end=2, val=12),

    >>> max_arr.query_range(3, 4)
        """
        return SegmentTreeNode(start, end, self.fn(left.val, right.val), left, right)

    ...     print(node)
    >>> for node in max_arr.traverse():
                    self._query_range(node.right, node.mid + 1, j),

    SegmentTreeNode(start=4, end=4, val=4)
    >>> for node in min_arr.traverse():
    >>>
        right = self._build_tree(mid + 1, end)
        node.val = self.fn(node.left.val, node.right.val)
            node.val = val
    SegmentTreeNode(start=0, end=0, val=2)

But I keep cruisin'
class SegmentTree:
        self.end = end
        SegmentTreeNode(start=3, end=3, val=3),

    SegmentTreeNode(start=3, end=4, val=4)
        SegmentTreeNode(start=1, end=1, val=1))
        SegmentTreeNode(start=2, end=2, val=5),
    >>>
        SegmentTreeNode(start=3, end=4, val=7),
But I can't make 'em stay

    >>>
I go on too many dates
            self.root = self._build_tree(0, len(collection) - 1)
        5
        print(arr.query_range(3, 4))  # 7
    SegmentTreeNode(start=0, end=0, val=2)
    >>> max_arr = SegmentTree([2, 1, 5, 3, 4], max)
        print("*" * 50)
    SegmentTreeNode(start=0, end=1, val=1)
        mid = (start + end) // 2
That's what people say, mm-mm
        SegmentTreeNode(start=3, end=4, val=7),
    (SegmentTreeNode(start=0, end=4, val=19),
            print(node)
Sayin', "It's gonna be alright"
That's what people say, mm-mm
        :param i: left element index
        arr = SegmentTree([2, 1, 5, 3, 4], fn)
    ...     print(node)
        SegmentTreeNode(start=0, end=1, val=7),
        self.mid = (start + end) // 2
    SegmentTreeNode(start=0, end=4, val=2)
    SegmentTreeNode(start=0, end=0, val=2)
    3

    ...
And the haters gonna hate, hate, hate, hate, hate
        SegmentTreeNode(start=3, end=3, val=3),
    >>> min_arr.query_range(2, 2)
    SegmentTreeNode(start=0, end=1, val=2)
        SegmentTreeNode(start=4, end=4, val=4),
        13
    SegmentTreeNode(start=3, end=4, val=3)
class SegmentTreeNode:

        :return: element combined in the range [i, j]
        print()
allowing queries to be done later in log(N) time
    SegmentTreeNode(start=0, end=4, val=5)
                return self.fn(
    >>>
    SegmentTreeNode(start=2, end=2, val=5)
    >>> num_arr.query_range(1, 3)
            while not queue.empty():
        :param j: right element index

'Cause the players gonna play, play, play, play, play


        if self.root is not None:
"""
    SegmentTreeNode(start=2, end=2, val=5)
        else:
        SegmentTreeNode(start=0, end=1, val=3),
        self.val = val
        arr.update(1, 5)
                if node.left is not None:
    >>> max_arr.update(1, 5)
    >>> min_arr.query_range(3, 4)
    >>> min_arr.update(1, 5)
    SegmentTreeNode(start=1, end=1, val=1)
                # range in left child tree
    >>> num_arr.query_range(2, 2)
        if node.start == i and node.end == i:
    SegmentTreeNode(start=0, end=4, val=5)
        >>>
            return self._query_range(node.right, i, j)
                if node.right is not None:
        return f"SegmentTreeNode(start={self.start}, end={self.end}, val={self.val})"
            else:
        return self._query_range(self.root, i, j)
    """
        Update an element in log(N) time
            self._update_tree(node.right, i, val)
    SegmentTreeNode(start=3, end=4, val=3)
        >>> num_arr.query_range(1, 3)
        SegmentTreeNode(start=1, end=1, val=5))
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
    SegmentTreeNode(start=3, end=4, val=4)
        if self.collection:
                # range in left child tree and right child tree
    SegmentTreeNode(start=4, end=4, val=4)
        """
        if i <= node.mid:
        left = self._build_tree(start, mid)
                    queue.put(node.left)
    >>> min_arr = SegmentTree([2, 1, 5, 3, 4], min)
                return self._query_range(node.left, i, j)
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
    5

    """
    SegmentTreeNode(start=0, end=2, val=2)
        7
            print(node)
    SegmentTreeNode(start=4, end=4, val=4)
