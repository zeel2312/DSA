# Shortest path in an Undirected Graph having unit distance

# You are given an Unidirected Graph having unit weights, find the shortest distance from 
# src to all the points, if path is not possible then put -1.

def shortestPath(N, M, edges, src):
    adj = [[] for i in range(N)]
    
    for i in edges:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
     
    # step-2: do the distance thing
    dist = [float('inf')]*N
    dist[src] = 0
    queue = []
    queue.append(src)
    
    # O(N + 2M)
    while queue:
        node = queue.pop()
        for i in adj[node]:
            if dist[node] + 1 < dist[i]:
                dist[i] = dist[node] + 1
                queue.append(i)
                
    ans = [-1]*N
    for i in range(N):
        if dist[i] != float('inf'):
            ans[i] = dist[i]
    return ans
    

# Time Complexity: 
# Space Complexity: 

N = 9 # nodes
M = 10 # edges
edges = [[0,1], [0,3], [3,4], [4,5], [5,6], [1,2], [2,6], [6,7], [7,8], [6,8]]
src = 0 # source
print(shortestPath(N, M, edges, src))
