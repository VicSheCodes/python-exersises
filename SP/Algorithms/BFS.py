"""
a simple implementation of Breadth-First Search (BFS) for a graph represented using an adjacency dictionary
"""

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex])


# Example usage:
if __name__ == "__main__":
    # Define the graph as an adjacency dictionary
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Breadth-First Traversal starting from vertex 'A':")
    bfs(graph, 'A')
