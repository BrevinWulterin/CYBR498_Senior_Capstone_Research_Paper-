    Merge left, node, right into root
        Symmetric as well
    left, right = split(root, value)
    return merge(left, right)
But I keep cruisin'
    return root
        >>> root = interact_treap(root, "=0")

        return left or right
    return merge(merge(left, node), right)
            return f"'{self.value}: {self.prior:.5}'"


        >>> inorder(root)
But I can't make 'em stay
            )

        return
                {f"{self.value}: {self.prior:.5}": (self.left, self.right)}, indent=1


        >>> inorder(root)
        1,2,3,5,16,17,19,
        Now we split(with the same value) current node's left son
        args = input()

        return root, right
I stay out too late
        Left will be root because it has more priority

    We merge 2 trees into one.
    """After each command, program prints treap"""
    Split current tree with a value into left, right,
        """
    """
        """

        Right tree's root will be current node.
    Split all nodes with values greater into right.
    """
        inorder(root.left)
    - value to erase all nodes with value
At least that's what people say, mm-mm
    Just recursive print of a tree

        1,
    if (not left) or (not right):  # If one node is None, return the other
    left, right = split(root, value)
        left, root.left = split(root.left, value)
class Node:
        """
    """
        root.right, right = split(root.right, value)
'Cause the players gonna play, play, play, play, play
    doctest.testmod()
    print(

    main()
    Erase element
    """
        print(root)
        match arg[0]:
    """
        right = str(self.right or "")
    Left tree contains all values less than split value.
        value = str(self.value) + " "

    Insert element
    else:
    + value to add value into treap
        """
    """


                root = insert(root, int(arg[1:]))
        self.left: Node | None = None
    """
        Now we need to merge left's right son and right tree
        0,1,2,3,4,4,4,4,5,16,17,19,
        >>> root = interact_treap(root, "+4 +4 +4")

    Merge left, right
    print("good by!")
        self.right: Node | None = None
    elif value <= root.value:


        else:
    )
        "enter numbers to create a tree, + value to add value into treap, "
    for arg in args.split():
    node = Node(value)

It's like I got this music in my mind
            return pformat(
That's what people say, mm-mm
    """
if __name__ == "__main__":
        print(root.value, end=",")
    if root is None or root.value is None:  # None tree is split into 2 Nones

    """
    else:
    """
    """
            case "+":
        if self.left is None and self.right is None:
        >>> inorder(root)
        Unknown command
                root = erase(root, int(arg[1:]))
            case "-":
That's what people say, mm-mm

        1,2,3,4,4,4,4,5,16,17,19,
    Insert new node into the middle
Can't stop, won't stop movin'
        return value + left + right
That's what people say, mm-mm

    if not root:  # None
                print("Unknown command")
        """
        self.value = value
    """
        inorder(root.right)
    """
        right.left = merge(left, right.left)
        root = interact_treap(root, args)
        return None, None
        Just symmetric to previous case


    Split all nodes with values less into left,
        return left
        "- value to erase all nodes with value. 'q' to quit. "
        self.prior = random()
        """

    _, right = split(right, value + 1)
    Note: all left tree's values must be less than all right tree's
        0,1,2,3,4,5,16,17,19,
    Commands:
    """


        return left, root
        left.right = merge(left.right, right)

        >>> root = interact_treap(root, "-4")
    Treap's node
I go on too many dates
        >>> root = interact_treap(root, "-0")
And the haters gonna hate, hate, hate, hate, hate
        left = str(self.left or "")
    We split current tree into 2 trees with value:
    else:
        >>> root = interact_treap(None, "+1")

Got nothing in my brain
    Right tree contains all values greater or equal, than split value
    while args != "q":

    args = input()
Sayin', "It's gonna be alright"

    Treap is a binary tree by value and heap by priority
        """
        """
            case _:
        >>> inorder(root)
        >>> root = interact_treap(root, "+3 +5 +17 +19 +2 +16 +4 +0")

        Left tree: left part of that split
    elif left.prior > right.prior:
        Right tree's left son: right part of that split

        >>> inorder(root)

        return right
    root = None
