def shortestPath(N, M, edges):
    adj = [[] for i in range(N)]
    
    for i in range(M):
        u = edges[i][0]
        v = edges[i][1]
        wt = edges[i][2]
        adj[u].append((v, wt))
    
    # find the topo sort
    vis = [0]*N
    st = []
    # O(N + E)
    for i in range(N):
        if vis[i] == 0:
            topoSort(i, adj, vis, st)
            
    # step-2: do the distance thing
    dist = [float('inf')]*N
    dist[0] = 0
    # O(N + M)
    while st:
        node = st.pop()
        for v, wt in adj[node]:
            if dist[node] + wt < dist[v]:
                dist[v] = dist[node] + wt
    return dist
        
def topoSort(node, adj, vis, st):
    vis[node] = 1
    for v, wt in adj[node]:
        if vis[v] == 0:
            topoSort(v, adj, vis, st)
    st.append(node)

# Time Complexity: 
# Space Complexity: 

N = 7 # nodes
M = 8 # edges
edges = [[0,1,2], [1,3,1], [2,3,3], [4,0,3], [4,2,1], [5,4,1], [6,4,2], [6,5,3]] # [node,edge,weight]
print(shortestPath(N, M, edges))