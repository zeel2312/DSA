def topSort(V, adjList):
    vis = [0 for i in range(V)]
    stack = []
    # now we will check for components
    for i in range(V):
        if vis[i] == 0:
            dfs(i, vis, adjList, stack)
    
    ans = []
    while stack: # store from stack to a list in linear order (LIFO: stack)
        ans.append(stack.pop())
    return ans
    
def dfs(node, vis, adjList, stack):
    vis[node] = 1
    
    for i in adjList[node]:
        if vis[i] == 0: # when the node is not visited
            dfs(i, vis, adjList, stack)
    stack.append(node)

# Time Complexity: O(V+E)
# Space Complexity: O(V)

V = 6
adjList = [[], [], [3], [1], [0,1], [0,2]]
print(topSort(V, adjList))