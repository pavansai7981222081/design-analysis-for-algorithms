def is_valid(vertex, graph, path, pos):
    if graph[path[pos - 1]][vertex] == 0:
        return False
    if vertex in path:
        return False
    return True

def hamilton_circuit_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, len(graph)):
        if is_valid(v, graph, path, pos):
            path[pos] = v
            if hamilton_circuit_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False

def hamilton_circuit(graph):
    path = [-1] * len(graph)
    path[0] = 0

    if not hamilton_circuit_util(graph, path, 1):
        print("No Hamiltonian circuit exists")
        return False

    print("Hamiltonian circuit exists:")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0])

    return True

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamilton_circuit(graph)
