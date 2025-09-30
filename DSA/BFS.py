# BFS is a graph traversal algorithm.
# It explores nodes level by level from a given source node.
# First it visits all neighbors of the source node
# Then it visits neighbors of those neighbors, and so on.
# It uses a queue data structure(FIFO) to keep track of the order in which nodes should be visited.

# BFS: always expanding equally in all directions before going deeper.

# Steps of BFS:
# 1. Initialize:
    # A queue to hold nodes to explore.
    # A set (or list) of visited nodes to avoid revisiting.
# 2. Start with the source node:
    # Mark it visited and push it into the queue.
# 3. While queue is not empty:
    # Pop the first node.
    # Visit all of its unvisited neighbors.
    # Mark neighbors visited and push them into the queue.
# 4. Continue until the queue is empty.

# BFS characteristics:
# Time Complexity: O(V + E) where V=number of vertices, E=number of edges. Because each node and each edge is processed once.
# Space Complexity: O(V) due to the queue and visited set.
# Applications:
    # Shortest Path in unweighted graphs.
    # AI/game search (finding minimal moves).

from collections import deque   # deque is a double-ended queue that allows fast appends and pops from both ends.
from typing import List, Dict

def bfs(graph: Dict, start: str) -> List:
    """
    Perform BFS on a graph from a starting node.
    
    :param graph: Dictionary representing adjacency list {node: [neighbors]}
    :param start: Starting node
    :return: List of nodes in the order they are visited
    """
    visited = set() # empty set to keep track of visited nodes [USING A SET GIVES O(1) AVERAGE TIME COMPLEXITY FOR MEMBERSHIP CHECKS]
    queue = deque([start])  # initialize queue with the start node
    order = []  # to record the order of traversal

    # difference between popleft and pop: popleft removes and return the leftmost element, pop removes and return the rightmost element.
    while queue:    # loop while there are nodes waiting in the queue
        node = queue.popleft()  # remove/dequeue the front(left) node from the queue
        if node not in visited:
            visited.add(node)   # mark node as visited
            order.append(node)  # record the order of traversal

            # add all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # enqueue the neighbor
    return order

graph = {
    # key: node, value: list of neighbors
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(f"BFS TRAVERSAL: {bfs(graph, 'A')}")