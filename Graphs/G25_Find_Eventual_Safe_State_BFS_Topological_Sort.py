def eventualSafeNodesTopo(V, adjList):
    adjRev = [[] for i in range(V)]
    indegree = [0 for i in range(V)]
    for i in range(V):
        for j in adjList[i]:
            adjRev[j].append(i) # reverse graph # 0 -> 1 to 1 -> 0
            indegree[i] += 1 # calculate indegree at the same time
    print(adjRev)
    print(indegree)
    
    queue = []
    for i in range(V): # find out terminal node
        if indegree[i] == 0:
            queue.append(i)
    
    safenodes = []
    while queue:
        node = queue.pop(0)
        safenodes.append(node)
        # node is in your topo sort
        # so please remove/decrease it/its count form your indegree
        for i in adjRev[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    safenodes.sort()
    return safenodes
    

# Time Complexity:
# Space Complexity:

V = 12
adjList = [[1],[2],[3,4],[4,5],[6],[6],[7],[],[1,9],[10],[8],[9]]
print(eventualSafeNodesTopo(V, adjList))
