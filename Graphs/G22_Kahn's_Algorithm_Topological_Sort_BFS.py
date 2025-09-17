def topoSort(V, adjList):
    indegree = [0 for i in range(V)]
    for i in range(V): # calculate indegree
        for j in adjList[i]: # for each adjacent node
            indegree[j] += 1 
    
    queue = []
    for i in range(V): # push all nodes with 0 indegree to the queue
        if indegree[i] == 0:
            queue.append(i)
    
    topo = [] # topological sort
    while queue:
        node = queue.pop(0) # pop from the queue
        topo.append(node) # add to topological sort
        # node is in your topo sort
        for i in adjList[node]:
            indegree[i] -= 1 # so please decrease its neighbours count form your indegree
            if indegree[i] == 0: # if the neighbour count is 0
                queue.append(i) # push to the queue
    return topo
    
    

# Time Complexity: O(V+E)
# Space Complexity: O(V)

V = 6
adjList = [[], [], [3], [1], [0,1], [0,2]]
print(topoSort(V, adjList))