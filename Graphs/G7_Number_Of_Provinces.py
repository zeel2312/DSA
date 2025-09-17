def numProvinces(v, adj):
    adjList = [[] for i in range(v)] # adjacency list
    # create adjacency list from adjacency matrix
    for i in range(v):
        for j in range(v):
            if adj[i][j] == 1 and i != j:
                adjList[i].append(j)
                print(adjList, i, j)
                adjList[j].append(i)
                print(adjList, i, j)
    
    visited = [False for i in range(v)] # visited array
    provinces = 0 # number of provinces counter
    for i in range(v):
        if visited[i] == False: # if not visited
            provinces += 1 # increment counter
            dfs(i, visited, adjList) # call dfs
    return provinces

def dfs(node, visited, adjList):
    visited[node] = True
    for i in adjList[node]:
        if visited[i] == False:
            dfs(i, visited, adjList)
    return

n = 4
adj = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
print(numProvinces(n, adj))