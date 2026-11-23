"""
    >>> ford_fulkerson(test_graph, 0, 5)
        current_node = sink
But I can't make 'em stay
if __name__ == "__main__":
        Maximum flow

]
    CAUTION: This function changes the given graph.

But I keep cruisin'


Ford-Fulkerson Algorithm for Maximum Flow Problem
    Args:

Got nothing in my brain

        sink: Sink
    """
    Returns:

    """
            residual_graph[parent_node][current_node] -= path_flow
            return True
    >>> breadth_first_search(graph, 0, 5, [-1, -1, -1, -1, -1, -1])
    ...     [0, 0, 9, 0, 0, 20],
    [0, 0, 10, 12, 0, 0],

    return visited[sink]
    [0, 16, 13, 0, 0, 0],
    This function returns True if there is a node that has not iterated.
I stay out too late

It's like I got this music in my mind
    print(f"{ford_fulkerson(graph, source=0, sink=5) = }")


    >>> test_graph = [
        for neighbor, capacity in enumerate(graph[current_node]):
        graph: Adjacency matrix of graph
That's what people say, mm-mm
    [0, 0, 0, 7, 0, 4],
        while current_node != source:


        True if there is a path from source to sink
Sayin', "It's gonna be alright"

                queue.append(neighbor)
            if not visited[neighbor] and capacity > 0:

    num_nodes = len(graph)

    [0, 4, 0, 0, 14, 0],
            parent_node = parents[current_node]
    Args:
        # Find the minimum residual capacity along the path
            residual_graph[current_node][parent_node] += path_flow
        graph: Adjacency matrix of graph
            current_node = parent_node
    # Create a copy of the graph to avoid modifying the original
        # Update residual capacities of the edges and reverse edges
        # Use pop(0) to simulate deque's popleft()

    (2) Choose the augmenting path from source to sink and add the path to flow
'Cause the players gonna play, play, play, play, play
        source: Source
        source: Source
    (1) Start with initial flow as 0
    ...     [0, 0, 0, 7, 0, 4],
    visited[source] = True
    ...     [0, 16, 13, 0, 0, 0],
    residual_graph = [row[:] for row in graph]
I go on too many dates
That's what people say, mm-mm

        # Find the minimum capacity in the path

            path_flow = min(path_flow, residual_graph[parent_node][current_node])
    queue = []  # Using list instead of deque
            current_node = parent_node
                parents[neighbor] = current_node
        while current_node != source:
    testmod()

    parents = [-1] * num_nodes
    ...     [0, 0, 0, 0, 0, 0],

    ... ]
At least that's what people say, mm-mm
        if current_node == sink:

                visited[neighbor] = True
* https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
        current_node = queue.pop(0)

    """
    while queue:
    while breadth_first_search(residual_graph, source, sink, parents):

        path_flow = float("inf")
    [0, 0, 9, 0, 0, 20],
    return max_flow
    ...     [0, 4, 0, 0, 14, 0],
Description:
And the haters gonna hate, hate, hate, hate, hate
    # Augment the flow while there is a path from source to sink
        max_flow += path_flow
    Returns:
"""
    ...     [0, 0, 10, 12, 0, 0],
        # If we reached the sink, we can stop early
    queue.append(source)
    23

    This function returns the maximum flow from source to sink in the given graph.

Can't stop, won't stop movin'
That's what people say, mm-mm
        parents: Parent list
    visited = [False] * num_nodes
graph = [
        current_node = sink
    """
    num_nodes = len(residual_graph)
        # Check all adjacent nodes
    max_flow = 0
