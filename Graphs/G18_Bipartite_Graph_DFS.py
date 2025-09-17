def isBipartite(V, adjList):
    color = [-1 for i in range(V)]
    # now we will check for components
    for i in range(V):
        if color[i] == -1: # if not visited
            if dfs(i, 0, color, adjList) == False: # if any component is not bipartite
                return False
    return True
    
def dfs(node, col, color, adjList):
    color[node] = col # color the node
    for i in adjList[node]:
        if color[i] == -1: # if not visited
            if dfs(i, 1 - col, color, adjList) == False: # if any component is not bipartite
                return False
        elif color[i] == col: # if the adj node is previously colored with the same color
            return False
    return True
    
# Time Complexity: O(V+2E)
# Space Complexity: O(V)

V = 4
adjList = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(isBipartite(V, adjList))