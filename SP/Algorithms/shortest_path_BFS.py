from collections import deque


def shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                if neighbor == end:
                    return path + [current, neighbor]
                else:
                    queue.append((neighbor, path + [current]))

    return None


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

    start = 'A'
    end = 'F'
    shortest_path = shortest_path(graph, start, end)

    if shortest_path:
        print(f"Shortest path from {start} to {end}: {shortest_path}")
    else:
        print(f"There is no path from {start} to {end}.")

