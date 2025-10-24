def bellman_ford(V, edges, src):

    dist = [float('inf') for i in range(V)]
    dist[src] = 0
    # V * E
    for i in range(V-1):
        for i in edges:
            u = i[0]
            v = i[1]
            wt = i[2]
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    
    # nth iteration to check for negative cycles
    for i in edges:
        u = i[0]
        v = i[1]
        wt = i[2]
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            return [-1]
    
    return dist
    
    

V = 5 
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0
print(bellman_ford(V, edges, src))
