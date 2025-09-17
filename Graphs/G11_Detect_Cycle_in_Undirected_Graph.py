from collections import deque

def isCycle(v,adj):
    visited = [0 for i in range(v)] # visited array
    for i in range(v): # traverse all nodes
        if(visited[i] == 0): # if not visited
            if(detectCycle(i,adj,visited)): # look if cycle exists
                return True
    return False

def detectCycle(src, adj, visited):
    visited[src] = 1 # mark visited
    q = deque()
    q.append((src,-1)) # node, parent
    while q:
        node, parent = q.popleft()
        for i in adj[node]: # traverse adjacent nodes
            if visited[i] == 0: # if not visited
                visited[i] = 1
                q.append((i,node))
            elif i != parent: # if not parent and is visited before
                return True # cycle found
    return False

# Test Case
n = 3
edges = [[0,1],[1,2],[2,0]]
print(isCycle(n,edges))