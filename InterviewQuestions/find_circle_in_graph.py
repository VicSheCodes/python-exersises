counter = 0
vertices = [0, 1, 2, 3, 4, 5]
# graph = {
#     0: [1, 2],
#     1: [2, 3],
#     2: [3, 4],
#     3: [4, 5],
#     4: [5, 0],
#     5: [0]
# }

# graph = {
#     0: [1, 4],
#     1: [2],
#     2: [3],
#     3: [4, 5, 0],
#     4: [5, 0],
#     5: [0]
# }

graph = {
    0: [1],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 1, 2]
}

visited = {vertex: False for vertex in vertices}
# print(visited)
# print(graph.get(0))


def find_circle(vertex):
    global counter
    if visited.get(vertex):
        counter += 1
        return

    visited[vertex] = True

    for i in graph.get(vertex):
        find_circle(i)
    visited[vertex] = False



print(find_circle(0))
print("Number of circles:", counter)
