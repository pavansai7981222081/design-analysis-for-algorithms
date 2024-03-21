import heapq

def prim_mst(graph):
    visited = set()
    min_spanning_tree = []
    start_node = next(iter(graph.keys()))
    visited.add(start_node)
    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        weight, src, dest = heapq.heappop(edges)
        if dest not in visited:
            visited.add(dest)
            min_spanning_tree.append((src, dest, weight))
            for neighbor, weight in graph[dest]:
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, dest, neighbor))

    return min_spanning_tree

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2)]
}

print(prim_mst(graph))
