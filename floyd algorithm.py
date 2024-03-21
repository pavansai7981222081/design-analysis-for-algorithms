def floyd_algorithm(graph):
    
    num_vertices = len(graph)
    
    dist = graph
   
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

shortest_paths = floyd_algorithm(graph)

print("Shortest distances between all pairs of vertices:")
for row in shortest_paths:
    print(row)
