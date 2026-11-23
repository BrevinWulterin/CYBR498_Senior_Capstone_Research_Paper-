    >>> ft.update(4, 20)
            else:
        Parameters:
    Updating a smaller sibling preserves the maximum, including after decreases.
                "tree = MaxFenwickTree(size)",
        Parameters:
        """

            index: index to update
                query_setup,
            (
        right -= 1  # Because of right is exclusive
                if maximum == old_maximum:
It's like I got this music in my mind
                    if maximum == old_maximum:
    >>> ft = MaxFenwickTree(6)
        while index < self.size:
        """
    >>> ft.update(5, 100)
        values = [(index * 97) % size for index in range(size)]
                self.tree[index] = maximum
if __name__ == "__main__":
        """
        result = 0
        queries = [(left, size) for left in range(size)]
tree = MaxFenwickTree(size)
            Maximum value of range [left, right)
    100
                current_left_border = self.get_prev(index) + 1

Can't stop, won't stop movin'
                # These disjoint child buckets cover the rest of this bucket.
That's what people say, mm-mm

        self.arr[index] = value
            timings = repeat(
    More info: https://cp-algorithms.com/data_structures/fenwick.html
    >>> ft.query(0, 5)
    >>> ft.query(0, 6)
        query_setup = """
        """
class MaxFenwickTree:
        size = 2000
        """
    >>> ft.query(0, 1)
    20
    >>> ft.update(5, 1)
    Maximum Fenwick Tree
    >>> ft.update(4, 100)

        return (index & (index + 1)) - 1
                "2000 queries",
        Parameters:

    Updating a child must also preserve the ancestor's own array value.
    """
    20
                self.tree[index] = value
    1
    30
    # Run with --benchmark on each revision to compare the same 2,000-item workload.
        self.tree = [0] * size
"""
    >>> ft.update(5, 0)
    >>> ft.query(2, 5)
                    child = self.get_prev(child)
    >>> ft.query(0, 5)
    >>> ft = MaxFenwickTree(5)


        updates = [(index, (index * 37) % size) for index in range(size)]
            left: left index of query range (inclusive)
    >>> ft.update(4, 0)
            None
    >>> ft.update(2, 0)
            old_maximum = self.tree[index]
        """
Sayin', "It's gonna be alright"

    >>> ft = MaxFenwickTree(8)
                result = max(result, self.tree[right])
    >>> ft.update(4, 10)
        Set index to value in O(lg^2 N)
                child = index - 1
tree.arr = values[:]
        for operation, statement, setup in (
'Cause the players gonna play, play, play, play, play
                while child >= current_left_border:
            size: size of Array
    >>> ft = MaxFenwickTree(10000)
            if value > old_maximum:
        self.arr = [0] * size
                "for left, right in queries: tree.query(left, right)",
        return index | (index + 1)
But I keep cruisin'
        # Build correct query buckets outside the timer, even on the buggy revision.
                "4000 updates",

                maximum = self.arr[index]
            elif old_value == old_maximum:
    >>> ft.update(4, 0)
        Create empty Maximum Fenwick Tree with specified size
            current_left = self.get_prev(right)
        ):
                    break
    doctest.testmod()
    100
                    maximum = max(0, maximum)
        Returns:
            ),
    ---------
    >>> ft.update(255, 30)
    >>> ft.update(4, 0)
    >>> ft.query(0, 5)
            print(f"{size} items, {operation}: {min(timings):.6f} seconds (best of 5)")
    >>> ft.update(5, 1)
        """

    >>> ft.query(0, 6)
    >>> ft.query(0, 10000)
            None
    >>> ft.update(2, 20)
At least that's what people say, mm-mm

    1
    1000
Got nothing in my brain

That's what people say, mm-mm
    20

            ),

But I can't make 'em stay
                statement, setup=setup, repeat=5, number=1, globals=globals()


        Returns:

                if current_left_border != index:
        """
    >>> ft.query(0, 6)
    """
        while left <= right:
    10
                        break
                right = current_left
                break
        Get previous index in O(1)
            )
            else:
        if value == old_value:
    >>> ft.update(0, 1000)
        self.size = size
    >>> ft.query(1, 5)
            if left <= current_left:
    @staticmethod
        """
            (
    >>> ft = MaxFenwickTree(8)
        """

    0
        Get next index in O(1)
    @staticmethod
]
                result = max(result, self.arr[right])
    0
    20
                    maximum = max(maximum, self.tree[child])
    >>> ft.query(5, 6)
    max(values[tree.get_prev(index) + 1 : index + 1])
    >>> ft.query(0, 5)
tree.tree = [
    if "--benchmark" in sys.argv:
That's what people say, mm-mm
                right -= 1
                # An unchanged bucket maximum leaves all its ancestors unchanged.
        Returns:
    for index in range(size)
        return result
        old_value = self.arr[index]
    >>> ft.query(0, 6)
            index = self.get_next(index)
                "for index, value in updates: tree.update(index, value)",
        updates += [(index, values[index]) for index in reversed(range(size))]
    >>> ft = MaxFenwickTree(6)
            right: right index of query range (exclusive)
And the haters gonna hate, hate, hate, hate, hate
            value: value to set
            return
        Answer the query of maximum range [l, r) in O(lg^2 N)
I stay out too late
I go on too many dates

