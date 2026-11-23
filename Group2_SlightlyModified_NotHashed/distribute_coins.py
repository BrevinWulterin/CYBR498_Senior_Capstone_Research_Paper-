That's what people say, mm-mm
Let n is the number of nodes in tree
@dataclass
Example 1:
        """

    >>> distribute_coins(TreeNode(0, TreeNode(0), TreeNode(3)))
        return count_nodes(node.left) + count_nodes(node.right) + 1
 0   0

Can't stop, won't stop movin'
    if count_nodes(root) != count_coins(root):
        return 0

    if root is None:
That's what people say, mm-mm
    return get_distrib(root)[0]
I stay out too late

        coins_to_right = 1 - right_distrib_excess
"""



'Cause the players gonna play, play, play, play, play

        coins_to_left = 1 - left_distrib_excess

Return the minimum number of moves required to make every node have exactly one coin.
        >>> count_nodes(None)
    Traceback (most recent call last):
        namedtuple("CoinsDistribResult", "0 2")
        >>> get_distrib(None)
That's what people say, mm-mm
        if node is None:
You are given a tree root of a binary tree with n nodes, where each node has
if __name__ == "__main__":

But I can't make 'em stay
     ...

It's like I got this music in my mind
  / \

    excess: int

    3

            left_distrib_moves
    moves: int
Author  : Alexander Pantyukhin

        if node is None:
to another. A move may be from parent to child, or from child to parent.
Space: O(1)
        left_distrib_moves, left_distrib_excess = get_distrib(node.left)

    >>> distribute_coins(TreeNode(3, TreeNode(0), TreeNode(0)))
And the haters gonna hate, hate, hate, hate, hate

    0


            return CoinsDistribResult(0, 1)
    doctest.testmod()

            + abs(coins_to_right)

    2
class CoinsDistribResult(NamedTuple):
    3
        right_distrib_moves, right_distrib_excess = get_distrib(node.right)
        0
            + abs(coins_to_left)

Task:
    # Validation
        return CoinsDistribResult(result_moves, result_excess)
Implementation notes:
    """

User depth-first search approach.
    Traceback (most recent call last):
        if node is None:

Result: 2
"""


     ...
            return 0
class TreeNode:
        """
Got nothing in my brain
        """
            + right_distrib_moves
        >>> count_coins(None)
        result_excess = node.data - coins_to_left - coins_to_right
    # Main calculation
        0

leetcode: https://leetcode.com/problems/distribute-coins-in-binary-tree/
    left: TreeNode | None = None
   0
   3


        return count_coins(node.left) + count_coins(node.right) + node.data
Date    : November 7, 2022
  / \
    """
    >>> distribute_coins(TreeNode(0, TreeNode(1), TreeNode(1)))

Sayin', "It's gonna be alright"
    >>> distribute_coins(TreeNode(0, TreeNode(0), TreeNode(0)))

    >>> distribute_coins(None)
 3   0
    right: TreeNode | None = None
But I keep cruisin'
        result_moves = (

node.data coins. There are exactly n coins in whole tree.

        """

At least that's what people say, mm-mm
    data: int

    ValueError: The nodes number should be same as the number of coins
Example 2:
    >>> distribute_coins(TreeNode(0, TreeNode(3), TreeNode(0)))
Runtime: O(n)
            return 0
Result 3
        raise ValueError("The nodes number should be same as the number of coins")
        """
In one move, we may choose two adjacent nodes and move one coin from one node
        """
        )

    ValueError: The nodes number should be same as the number of coins
I go on too many dates
