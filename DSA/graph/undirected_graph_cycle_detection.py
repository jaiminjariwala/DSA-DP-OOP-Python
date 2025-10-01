"""
Since the graph is undirected, the connections are bidirectional.
Time Complexity: O(V + E) where V=number of vertices, E=number of edges. Each node and edge is processed once.
Space Complexity: O(V) for the visited set and recursion stack.
"""

from typing import Dict

def has_cycle(graph: Dict) -> bool:
    visited = set() # to keep track of visited nodes

    def dfs(node: str, parent: str) -> bool:    # [A, None], [B, A], ...
        visited.add(node)   # mark node as visited, [A], [A, B], ...

        for neighbor in graph[node]: # neighbor of A: B, C in graph with cycle
            if neighbor not in visited: # if B not visited, [A not in visited, but A is visited], ...
                if dfs(neighbor, node): # explore neighbor, parent of B is A, dfs(B, A)
                    return True
            elif neighbor != parent:  # if neighbor is visited and not parent, we found a back edge -> cycle
                return True
        return False

    for node in graph:  # A, B, C, D
        if node not in visited:
            if dfs(node, None):  # start DFS with no parent, parent of A is None
                return True
            
    return False

graph_without_cycle = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C']
}   # this has no cycle, it's just a path A-B-C-D

graph_with_cycle = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}   # this has a cycle: A-B-D-C-A

print("Graph without cycle:", has_cycle(graph_without_cycle))
print("Graph with cycle:", has_cycle(graph_with_cycle))