def is_safe(graph, vertex, color, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and c == color[i]:
            return False
    return True

def graph_coloring_backtrack(graph, num_colors, colors, vertex=0):
    if vertex == len(graph):
        return True

    for c in range(1, num_colors+1):
        if is_safe(graph, vertex, colors, c):
            colors[vertex] = c
            if graph_coloring_backtrack(graph, num_colors, colors, vertex+1):
                return True
            colors[vertex] = 0

    return False

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
num_colors = 3
colors = [0] * len(graph)

if graph_coloring_backtrack(graph, num_colors, colors):
    print("Graph can be colored with", num_colors, "colors.")
    print("Vertex colors:", colors)
else:
    print("Graph cannot be colored with", num_colors,"colors.")
