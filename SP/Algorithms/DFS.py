"""
a simple implementation of Depth-First Search (DFS) for a graph represented using an adjacency dictionary
"""


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


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

    print("Depth-First Traversal starting from vertex 'A':")
    dfs(graph, 'A')
