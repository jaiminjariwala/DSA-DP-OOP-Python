"""
1. What is DFS?
    Depth First Search (DFS) is a graph traversal algorithm.
    Instead of exploring nodes level by level like BFS, DFS goes deep along one branch before backtracking.

2. How DFS Works (Logic)
    * Start from the source node.
    * Visit it (mark as visited).
    * Pick one of its neighbors and go there (recursively or using a stack).
    * Continue exploring deeper until you cannot go further.
    * Backtrack and explore the next unvisited neighbor.
    * Repeat until all reachable nodes are visited.

3. Characteristics
    Time Complexity: O(V+E), same as BFS.
    Space Complexity:
        * Recursive DFS → O(V) (stack frames).
        * Iterative DFS → O(V) (explicit stack).
    Applications:
        * Detecting cycles in graphs.
        Topological sorting (DAGs).
        Pathfinding in mazes.
        Connected components in graphs.
"""

from typing import List, Dict

# recursive DFS implementation
def dfs_recursive(graph: Dict, node: str, visited=None, order=None) -> List:
    """
    Perform DFS on a graph using recursion.
    
    :param graph: Dictionary representing adjacency list {node: [neighbors]}
    :param node: Current node of type str
    :param visited: Set of visited nodes
    :param order: List to record the order of traversal
    :return: List of nodes in the order they are visited
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if node not in visited:
        visited.add(node)
        order.append(node)

        # Explore neighbors
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited, order)
    return order

# iterative DFS implementation
def dfs_iterative(graph: Dict, start: str) -> List:
    """
    Perform DFS on a graph using an explicit stack
    :param graph: Dictionary representing adjacency list {node: [neighbors]}
    :param start: Starting node
    :return: List of nodes in the order they are visited
    """
    visited = set() # to keep track of visited nodes
    stack = [start] # initialize stack with the start node
    order = []  # to record the order of traversal
    while stack:
        node = stack.pop()  # pop the top node from the stack
        if node not in visited:
            visited.add(node)
            order.append(node)
            # add neighbors to stack (reverse order to maintain original order)
            # if not reversed, the last neighbor in ['B', 'C'] will be processed first, which is 'C' and the order will be ['A', 'C', 'F', 'B', 'E', 'D'] but we want ['A', 'B', 'D', 'E', 'F', 'C']
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
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

print("DFS Recursive: ", dfs_recursive(graph=graph, node='A'))
print("DFS Iterative: ", dfs_iterative(graph=graph, start='A'))