def bfsOfGraph(n, adj): # adjacency list = [[],[],[],[],[]]
    visited = [False for i in range(n)] # visited array
    queue = []
    queue.append(0) # starting node
    visited[0] = True # mark starting node as visited
    while queue:
        node = queue.pop(0)
        print(node, end=" ") # print node # 0
        for i in adj[node]: # traverse adjacent nodes
            if visited[i] == False: # if not visited
                visited[i] = True # mark visited
                queue.append(i) # add to queue
                
# Time Complexity: O(V+E)
# Space Complexity: O(V)

n = 5
adj = [[] for i in range(n)]
adj[0].append(1)
adj[0].append(2)
adj[1].append(0)
adj[1].append(3)
adj[2].append(0)
adj[2].append(4)
adj[3].append(1)
adj[4].append(2)

bfsOfGraph(n, adj)