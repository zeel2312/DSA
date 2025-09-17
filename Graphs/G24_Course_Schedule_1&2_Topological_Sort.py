def isPossible(V, prerequisites):
    adjList = [[] for i in range(V)]
    for i in prerequisites:
        adjList[i[1]].append(i[0])
    print(adjList)
        
    indegree = [0 for i in range(V)]
    for i in range(V): # calculate indegree
        for j in adjList[i]: # for each adjacent node
            indegree[j] += 1
    print(indegree)
    
    queue = []
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)
    
    topo = []
    while queue:
        node = queue.pop(0)
        topo.append(node)
        # node is in your topo sort
        # so please remove/decrease it/its count form your indegree
        for i in adjList[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    print(topo)
    if len(topo) == V:
        return True # in course schedule 2 we return the topo sort itself
    return False # in course schedule 2 we return an empty array if the topo sort did not exist
    

# Time Complexity: O(V+E)
# Space Complexity: O(V)

V = 6
prereq = [(2,3), (3,1), (4,0), (4,1), (5,0), (5,2)]
print(isPossible(V, prereq))
