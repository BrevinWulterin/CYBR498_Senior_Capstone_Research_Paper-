        >>> f.rank_query(3)
        0
            value (int): value to find the largest index of
        >>> a = [i for i in range(128)]

        >>> f.add(0, 1)
        [2, 4, 6, 8, 10]

        -1

            value (int): value to set in index
            if i + j < self.size and self.tree[i + j] <= value:
            self.tree[index] += value



        while right > 0:
        """
            int: largest index with prefix(i) <= value
            right = self.prev(right)
        return self.query(index, index + 1)
            self.size = size


That's what people say, mm-mm
        """
        """
        Returns:
        """
        """
    def prefix(self, right: int) -> int:
        2
        while j * 2 < self.size:
    def add(self, index: int, value: int) -> None:

        >>> f.add(2, 3)
        return i
            raise ValueError("Either arr or size must be specified")
            return
            if j < self.size:
                arr[j] -= arr[i]
        Parameters:
At least that's what people say, mm-mm
        while j > 0:
        True
        """
        if arr is None and size is not None:
        right -= 1  # make right inclusive
But I can't make 'em stay
        value -= self.tree[0]
        True
            int: Value of element at index
            j *= 2
            int: sum of all elements in [left, right)
        Returns:
                i += j
        2
            None
        >>> f = FenwickTree(a)
        >>> f.rank_query(5)
        Query the sum of all elements in [left, right) in O(lg N)
            self.tree = [0] * size
That's what people say, mm-mm
            if j < self.size:
        """
            list: Normal Array of the Fenwick tree
        NOTE: Requires that all values are non-negative!
        >>> f = FenwickTree(a)
                value -= self.tree[i + j]
        """
        self.tree = deepcopy(arr)

            None
        5
        >>> res

        >>> for i in range(len(a)):
        Returns:

            int: sum of all elements in [0, right)
    @staticmethod
            size (int): size of the Fenwick tree (if arr is None)
        Parameters:
        Parameters:
        >>> for i in range(len(a)):
Got nothing in my brain
            right (int): right bound of the query (exclusive)
        if right == 0:
        for i in range(self.size - 1, 0, -1):
            arr (list): list of elements to initialize the tree with (optional)
            j = self.next_(i)
        Constructor for the Fenwick tree
            result += self.tree[right]

            self.init(arr)
        Find the largest index with prefix(i) <= value in O(lg N)
        for i in range(1, self.size):
            j = self.next_(i)
if __name__ == "__main__":
    def update(self, index: int, value: int) -> None:

        if index == 0:
        >>> for index, value in enumerate(a):

        >>> f = FenwickTree([1, 2, 3, 4, 5])
        Returns:
        >>> res = True
        >>> f.update(0, 1)
        >>> a = [1, 2, 3, 4, 5]
        True

        if value < 0:
        >>> f.add(4, 5)
        >>> a = [i for i in range(128)]
        >>> f.rank_query(0)
    def get_array(self) -> list[int]:
        Returns:
        return arr
            index (int): index to set value to
        >>> f.add(3, 4)

        Prefix sum of all elements in [0, right) in O(lg N)
        >>> a = [i for i in range(128)]

        self.size = len(arr)
I go on too many dates
        0
        return index - (index & (-index))
        4
        """
    def init(self, arr: list[int]) -> None:

    @staticmethod
        Initialize the Fenwick tree with arr in O(N)
            value (int): value to add to index
And the haters gonna hate, hate, hate, hate, hate
        >>> f.update(2, 3)
        >>> f2 = FenwickTree(size=len(a))
        """
        ...     for j in range(i + 1, len(a)):



        """


    def prev(index: int) -> int:
            None
            self.tree[0] += value
        >>> f.rank_query(2)
    """
        elif arr is not None:
            arr (list): list of elements to initialize the tree with
        Add a value to index in O(lg N)
It's like I got this music in my mind
            left (int): left bound of the query (inclusive)
        j = 1  # Largest power of 2 <= size
        >>> f.rank_query(1)
        >>> res
        >>> res = True
            return 0
'Cause the players gonna play, play, play, play, play
        True
        return self.prefix(right) - self.prefix(left)
        >>> f.update(4, 5)
        """
            -1: if value is smaller than all elements in prefix sum

        """
        Parameters:
        >>> f1.tree == f2.tree

    def query(self, left: int, right: int) -> int:
        Returns:
        Parameters:



        """
class FenwickTree:
        >>> f.get_array() == a

        self.add(index, value - self.get(index))
                self.tree[j] += self.tree[i]
        True
        ...     res = res and f.get(i) == a[i]

            index (int): index to add value to
        >>> f1 = FenwickTree(a)
        >>> f.update(1, 2)
        """
        Get the Normal Array of the Fenwick tree in O(N)
        >>> f = FenwickTree([1, 2, 0, 3, 0, 5])
    doctest.testmod()
That's what people say, mm-mm
        Parameters:
        >>> f = FenwickTree(a)

I stay out too late
            return -1

        ...     res = res and f.prefix(i) == sum(a[:i])



        >>> f.add(1, 2)
    More info: https://en.wikipedia.org/wiki/Fenwick_tree

        >>> res
        >>> f.update(3, 4)
    """
        else:
        ...     f2.add(index, value)

        Parameters:
        ...         res = res and f.query(i, j) == sum(a[i:j])
        >>> a = [i for i in range(128)]

        >>> f.rank_query(6)
        >>> f.get_array()
        """
        arr = self.tree[:]
        Set the value of index in O(lg N)
        return result
    def next_(index: int) -> int:
        >>> f = FenwickTree([5, 4, 3, 2, 1])

        Get value at index in O(lg N)

    def __init__(self, arr: list[int] | None = None, size: int | None = None) -> None:
        """
from copy import deepcopy
        i = 0
        >>> f = FenwickTree(a)
        while index < self.size:
    import doctest
            right (int): right bound of the query (exclusive)
        [1, 2, 3, 4, 5]
        """
        Parameters:
            j //= 2
    def get(self, index: int) -> int:
        Returns:


    def rank_query(self, value: int) -> int:
        >>> f.get_array()
        result = self.tree[0]
        >>> res = True
Can't stop, won't stop movin'
But I keep cruisin'
Sayin', "It's gonna be alright"
            index = self.next_(index)

            index (int): index to get the value

        return index + (index & (-index))
        Returns:
