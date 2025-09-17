def f(node, color, graph, colors):
    if node == len(graph): #base case
        return True
    for color in colors:
        if isSafe(node,color,graph,colors):
            graph[node] = color
            if f(node+1,color,graph,colors) == True:
                return True
            graph[node] = -1
    return False

def isSafe(node, color, graph, colors):
    for i in range(len(graph)):
        if graph[i] == graph[node] and i != node:
            return False
    return True

def mColoring(graph, m):
    colors = [i for i in range(1,m+1)]
    return f(0,-1,graph,colors)

# Driver Code
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
print(mColoring(graph, m)) 