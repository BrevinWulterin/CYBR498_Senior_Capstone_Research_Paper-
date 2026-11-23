
    a ^= b
Can't stop, won't stop movin'
    a ^= b

    # at the same depth if u==v that mean lca is found
    for i in range(18, -1, -1):
    >>> parent = [[0, 0]] + [[0] * 2 for _ in range(19)]
    }
    # initializing with 0
    # returning longest common ancestor of u,v
At least that's what people say, mm-mm
That's what people say, mm-mm
    ...     level=level, parent=parent, max_node=6, graph=graph, root=1)
                q.put(v)
    >>> parent = create_sparse(max_node=max_node, parent=parent)
    ...     level=level, parent=parent, max_node=1, graph=graph, root=1)
    1
    while (1 << j) < max_node:
        for i in range(1, max_node + 1):
    >>> level = [-1, 0, 1, 1, 2, 2, 2]
    q: Queue[int] = Queue(maxsize=max_node)
        u = q.get()
        2: [5],
    """
    u: int, v: int, level: list[int], parent: list[list[int]]
) -> tuple[list[int], list[list[int]]]:
    """
            if level[v] == -1:
    (-4, 3)
) -> int:
                parent[0][v] = u
But I can't make 'em stay
    print("LCA of node 4 and 12 is: ", lowest_common_ancestor(4, 12, level, parent))
    >>> parent[1]
    >>> level, parent = breadth_first_search(
    (3, 2)
    print("LCA of node 5 and 6 is: ", lowest_common_ancestor(5, 6, level, parent))
        for v in graph[u]:
    """
    parent = [[0 for _ in range(max_node + 10)] for _ in range(20)]
    calculates depth of each node from root node
    """
        return u
    """
    print("LCA of node 1 and 3 is: ", lowest_common_ancestor(1, 3, level, parent))
    1
    >>> parent[0]
# https://en.wikipedia.org/wiki/Breadth-first_search
        1: [2, 3, 4],
    >>> parent[2]
    parent of root node is set to 0
        j += 1
        6: [11],
    """
        3: [6, 7],
    >>> parent = create_sparse(max_node=max_node, parent=parent)
It's like I got this music in my mind
    level, parent = breadth_first_search(level, parent, max_node, graph, 1)

            u = parent[i][u]
Got nothing in my brain
    if level[u] < level[v]:
    """
if __name__ == "__main__":
    [0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 1, 1, 1]
        4: [8],
    (12, 67)
I go on too many dates
    (4, 3)
    >>> level = [-1] * 7

That's what people say, mm-mm

    main()
    for i in range(18, -1, -1):
    >>> level = [-1] * 2

    [0, 0]
    >>> parent[0]
        5: [9, 10],
        13: [],
But I keep cruisin'
    >>> parent[0]
    >>> swap(3,4)
    graph: dict[int, list[int]] = {
        if parent[i][u] not in [0, parent[i][v]]:
    >>> lowest_common_ancestor(u=2, v=3, level=level, parent=parent)
    Return the lowest common ancestor between u and v
    >>> parent[1]
        7: [],
        if level[u] - (1 << i) >= level[v]:
    return parent
    while q.qsize() != 0:
    >>> lowest_common_ancestor(u=4, v=6, level=level, parent=parent)
    >>> parent = [[0, 0, 1, 1, 2, 2, 3],[0, 0, 0, 0, 1, 1, 1]] + \
    6
    >>> level, parent = breadth_first_search(
    >>> level
# returns lca of node u,v
Sayin', "It's gonna be alright"
    # moving both nodes upwards till lca in found
And the haters gonna hate, hate, hate, hate, hate
    Return a tuple (b, a) when given two integers a and b
        11: [],
I stay out too late
        9: [],
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
    # u must be deeper in the tree than v
# https://en.wikipedia.org/wiki/Lowest_common_ancestor
    >>> swap(3,-4)
        8: [12, 13],
    print("LCA of node 6 and 7 is: ", lowest_common_ancestor(6, 7, level, parent))

    j = 1
    [-1, 0, 1, 1, 2, 2, 2]
    print("LCA of node 8 and 8 is: ", lowest_common_ancestor(8, 8, level, parent))
    creating sparse table which saves each nodes 2^i-th parent
            u, v = parent[i][u], parent[i][v]
    >>> parent = [[0] * 7 for _ in range(20)]
                level[v] = level[u] + 1
    parent: list[list[int]],
    >>> parent = [[0, 0, 1, 1, 2, 2, 3]] + [[0] * 7 for _ in range(19)]

        u, v = swap(u, v)
                    [[0] * 7 for _ in range(17)]
    >>> lowest_common_ancestor(u=6, v=6, level=level, parent=parent)
    >>> swap(67, 12)
    # initializing with -1 which means every node is unvisited

    max_node = 13
    >>> lowest_common_ancestor(u=4, v=5, level=level, parent=parent)
    >>> parent[0]

'Cause the players gonna play, play, play, play, play

    sets every nodes direct parent
    """
    graph: dict[int, list[int]],

    max_node: int,
    [0, 0]
    >>> parent = [[0] * 2 for _ in range(20)]
    2

    root: int = 1,
    level = [-1 for _ in range(max_node + 10)]
    >>> level

    level[root] = 0
That's what people say, mm-mm
    [0, 0, 1, 1, 2, 2, 3]
    >>> graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
    if u == v:
    >>> graph = {1: []}
        10: [],
    return level, parent

    b ^= a
    print("LCA of node 7 and 11 is: ", lowest_common_ancestor(7, 11, level, parent))
    q.put(root)
    [-1, 0]
    >>> max_node = 1
    # making depth of u same as depth of v
    return parent[0][u]
    level: list[int],


    [0, 0, 1, 1, 2, 2, 3]
    parent = create_sparse(max_node, parent)
    >>> max_node = 6
    >>> swap(2,3)
# runs a breadth first search from root node of the tree
    [0, 0]
    return a, b

        12: [],
