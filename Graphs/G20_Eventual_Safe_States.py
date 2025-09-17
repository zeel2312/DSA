def eventualSafeStates(V, adjList):
    vis = [0 for i in range(V)]
    pathVis = [0 for i in range(V)]
    check = [0 for i in range(V)]
    safenodes = [] # safestates array
    # now we will check for components
    for i in range(V):
        if vis[i] == 0:
            dfs(i, adjList, vis, pathVis, check)
    
    for i in range(V):
        if check[i] == 1:
            safenodes.append(i)
    
    return safenodes
    
def dfs(node, adjList, vis, pathVis, check):
    vis[node] = 1
    pathVis[node] = 1
    check[node] = 0
    
    for i in adjList[node]:
        if vis[i] == 0: # when the node is not visited
            if dfs(i, adjList, vis, pathVis, check):
                check[node] = 0 # cycle found from this node
                return True
        elif pathVis[i] == 1: # if the adj node is previously visited and is on the same path
            check[node] = 0 # cycle found from this node
            return True
    check[node] = 1 # no cycle from this node
    pathVis[node] = 0 # unmark the path when going back
    return False
    
# Time Complexity: O(V+E)
# Space Complexity: O(V)

V = 7
adjList = [[1,2],[2,3],[5],[0],[5],[],[]]
print(eventualSafeStates(V, adjList))