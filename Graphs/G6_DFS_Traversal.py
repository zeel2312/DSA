def dfsOfGraph(n, adj):
    visited = [False] * n # visited array
    for i in range(n):
        if visited[i] == False: # if not visited
            dfs(i, adj, visited) # call dfs
    return

def dfs(node, adj, visited):
    visited[node] = True # mark visited
    print(node, end=" ") 
    for i in adj[node]: # traverse adjacent nodes
        if visited[i] == False: # if not visited
            dfs(i, adj, visited) # call dfs
    return

n = 5
adj = [[] for i in range(n)]
adj[0].append(1)
adj[0].append(2)
adj[1].append(0)
adj[1].append(3)
adj[2].append(0)
adj[2].append(4)
adj[3].append(1)
adj[4].append(2)
print(adj)

dfsOfGraph(n, adj)