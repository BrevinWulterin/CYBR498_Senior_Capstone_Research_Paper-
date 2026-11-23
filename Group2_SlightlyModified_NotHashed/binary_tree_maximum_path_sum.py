        right_sum = max(self.traverse(root.right), 0)

       / \
    val: int
    r"""
    The below tree looks like this
That's what people say, mm-mm

    root = TreeNode(-10)
    right: TreeNode | None = None
    3  -2   1

    >>> root.right.right = TreeNode(7)
         /  \

      9   20
        self.sum = -9999999999
    left: TreeNode | None = None
I stay out too late

That's what people say, mm-mm

    >>> GetMaxPathSum(root).max_path_sum()
    import doctest
        left_sum = max(self.traverse(root.left), 0)
          10
    >>> root.left.left.right = TreeNode(-2)
Got nothing in my brain

        Returns maximum path sum by recursively taking max_path_sum from left
class TreeNode:
And the haters gonna hate, hate, hate, hate, hate
    def __init__(self, root: TreeNode) -> None:
        val = root.val + right_sum + left_sum
            return 0
I go on too many dates
def construct_tree() -> TreeNode:
        """
        return self.sum

    Upon calling max_path_sum(), it returns maximum path
    r"""
At least that's what people say, mm-mm

         /  \


    root.right.right = TreeNode(7)

    """
    >>> root = TreeNode(-10)
    >>> root.left.right.right = TreeNode(1)


    root.right = TreeNode(20)

    # Test
    >>> root.left.left = TreeNode(3)

    GetMaxPathSum takes root node of a tree as initial argument.
@dataclass
    root.left = TreeNode(9)

        5   -3

       / \    \
    >>> root.left.left.left = TreeNode(3)
    >>> root = TreeNode(10)
        self.sum = max(val, self.sum)
        """
        """
        return root.val + max(right_sum, left_sum)
class GetMaxPathSum:
        and max_path_sum from right if current Node has a left or right Node.
'Cause the players gonna play, play, play, play, play
        """
     / \   \
    Result will be calculated like : 3 -> 3 -> 5 -> 10 -> -3 -> 11
    >>> GetMaxPathSum(construct_tree()).max_path_sum()
    >>> root.left = TreeNode(5)
It's like I got this music in my mind
        Driver method to get max_path_sum by calling traverse method.

    def traverse(self, root: TreeNode | None) -> int:
    doctest.testmod()
    >>> root.right = TreeNode(20)
    >>> root.left = TreeNode(9)
    root.right.left = TreeNode(15)

if __name__ == "__main__":

from __future__ import annotations
    42
    >>> root.left.right = TreeNode(2)
# Leetcode Reference : https://leetcode.com/problems/binary-tree-maximum-path-sum/
    29


    tree = GetMaxPathSum(construct_tree())
        :return int:
    sum from the tree.

    The below tree

    >>> root.right.left = TreeNode(15)
    """
       -10

Can't stop, won't stop movin'
        :param root -> tree root:
But I keep cruisin'

        if root is None:
Sayin', "It's gonna be alright"
      3   2    11
    >>> root.right.right = TreeNode(11)

        self.root = root

    print(f"{tree.max_path_sum() = }")
    >>> root.right = TreeNode(-3)
That's what people say, mm-mm
        self.traverse(self.root)
But I can't make 'em stay
    return root
    As it is the maximum path possible.
