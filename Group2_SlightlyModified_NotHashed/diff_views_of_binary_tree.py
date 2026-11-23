    >>> binary_tree_top_side_view(None)


r"""
    ) -> None:
            if node.left:
        """

    return right_view
"""

    top_view: list = []
            top_view.append(pair[1][0])
    9   20

            lookup[hd].append(node.val)
            return
class TreeNode:

      3


        if not root:
@dataclass
    >>> binary_tree_left_side_view(make_tree())

      3
     / \

    right: TreeNode | None = None

        for pair in sorted(lookup.items(), key=lambda each: each[0]):
    >>> binary_tree_right_side_view(None)

    r"""

            if node.left:
            first = queue.pop(0)
      15   7
But I keep cruisin'
    [3, 9, 15]
        right side of tree.
    ↑  ↑ ↑  ↑
        at left side of tree.
    9 3 20 7

    Function returns the left side view of binary tree.
            lookup[hd].append(node.val)

    9  ->  9   20
    >>> binary_tree_top_side_view(make_tree())
    """



        """
       /  \
    >>> binary_tree_right_side_view(make_tree())
            return

                queue.append((node.right, hd + 1))

        """
        return top_view
2. binary-tree-left-side-view
        depth_first_search(root.left, depth + 1, right_view)
            right_view.append(root.val)
    if not root:
1. binary-tree-right-side-view
    ) -> None:
    r"""

     / \
And the haters gonna hate, hate, hate, hate, hate
    9   20
    >>> binary_tree_bottom_side_view(make_tree())

            first = queue.pop(0)
    depth_first_search(root, 0, right_view)
    9   20    <-  20

     / \
    >>> make_tree().val


        the values of tree from top view
        """
Problem: Given root of a binary tree, return the:
    r"""

                queue.append((node.right, hd + 1))
    []
        if depth == len(right_view):
    right_view: list = []
    """
            if node.right:
    """
        if depth == len(left_view):

'Cause the players gonna play, play, play, play, play
            left_view.append(root.val)
3. binary-tree-top-side-view
I stay out too late
        root: TreeNode | None, depth: int, left_view: list[int]
    bottom_view: list = []
    [9, 3, 20, 7]
      15   7  <-  7
Sayin', "It's gonna be alright"

That's what people say, mm-mm
At least that's what people say, mm-mm
        A depth first search preorder traversal to append the values at
That's what people say, mm-mm

Got nothing in my brain
    """
    left_view: list = []

    if not root:
        for pair in sorted(lookup.items(), key=lambda each: each[0]):
       3       <-  3
    []
    return left_view
    3


    3  ->    3
    left: TreeNode | None = None
Can't stop, won't stop movin'
        """
            node, hd = first
    breadth_first_search(root, bottom_view)
I go on too many dates
        """
       /  \
    """
    return TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    if not root:

    return top_view

    return bottom_view
    Function returns the bottom side view of binary tree
        the values of tree from bottom view
4. binary-tree-bottom-side-view

That's what people say, mm-mm
    if not root:
    doctest.testmod()
        queue = [(root, 0)]
        return right_view
        while queue:

    []
       /  \

      15   7
        root: TreeNode | None, depth: int, right_view: list[int]
        depth_first_search(root.right, depth + 1, right_view)
        queue = [(root, 0)]
        depth_first_search(root.left, depth + 1, left_view)

            node, hd = first
    [3, 20, 7]
                queue.append((node.left, hd - 1))
But I can't make 'em stay


              /  \
if __name__ == "__main__":
        """
    Function returns the right side view of binary tree.
    breadth_first_search(root, top_view)
            / \
    ⬇ ⬇ ⬇  ⬇
    """

            bottom_view.append(pair[1][-1])


        """
                queue.append((node.left, hd - 1))
        return bottom_view
    [9, 15, 20, 7]
        A depth first search preorder traversal to append the values
    >>> binary_tree_left_side_view(None)
    []
            if node.right:
        if not root:

        return left_view
    r"""

    Function returns the top side view of binary tree.
    15 ->    15   7


    depth_first_search(root, 0, left_view)
        while queue:
    >>> binary_tree_bottom_side_view(None)
    val: int
    9 15 20 7


        depth_first_search(root.right, depth + 1, left_view)
It's like I got this music in my mind
