def isCyclic(V, adjList):
    vis = [0 for i in range(V)]
    pathVis = [0 for i in range(V)]
    # now we will check for components
    for i in range(V):
        if vis[i] == 0:
            if dfs(i, adjList, vis, pathVis) == True:
                return True
    return False
    
def dfs(node, adjList, vis, pathVis):
    vis[node] = 1
    pathVis[node] = 1
    
    for i in adjList[node]:
        if vis[i] == 0: # when the node is not visited
            if dfs(i, adjList, vis, pathVis) == True:
                return True
        elif pathVis[i] == 1: # if the adj node is previously visited and is on the same path
            return True
    
    pathVis[node] = 0 # unmark the path when going back
    return False
    
# Time Complexity: O(V+E)
# Space Complexity: O(V)

V = 8
adjList = [[1], [2], [3], [4], [5], [6], [7], [0]]
print(isCyclic(V, adjList))