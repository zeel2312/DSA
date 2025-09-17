def isBipartite(start, colors, V, adjList):
    queue = []
    queue.append(start)
    colors[start] = 0
    while queue:
        node = queue.pop(0)
        for i in adjList[node]:
            # if the color of the adjacent node is not set yet
            # you will give the opposite color of the node
            if colors[i] == -1:
                colors[i] = 1 - colors[node]
                queue.append(i)
            # does the adjacent node have the same color
            # someone did color it on some another path
            elif colors[i] == colors[node]:
                return False
    return True

def checkBipartite(V, adjList):
    colors = [-1 for i in range(V)]
    for i in range(V): # just to check if the graph is connected via components
        if colors[i] == -1:
            if not isBipartite(i, colors, V, adjList):
                return False
    return True

# Time Complexity: O(V+2E)
# Space Complexity: O(V)

V = 4
adjList = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(checkBipartite(V, adjList))