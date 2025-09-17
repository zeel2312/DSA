def isCycle(v, adj):
    visited = [0 for i in range(v)] # visited array
    for i in range(v): # traverse all nodes # To check if there is a cycle in a connected-components graph
        if(visited[i] == 0): # if not visited
            if(dfs(i, -1, adj, visited)): # look if cycle exists
                return True
    return False
    
def dfs(node, parent, adj, visited):
    visited[node] = 1
    for i in adj[node]: # traverse adjacent nodes
        if visited[i] == 0: # if not visited
            dfs(i, node, adj, visited)
        elif i != parent: # if not parent and is visited before
            return True
    return False

v = 5
adj = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]]
print(isCycle(v, adj))