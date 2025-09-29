from collections import deque
import heapq

def shortestPath(n, m, edges):
    adj = [[] for i in range(n+1)]
    
    for i in range(m):
        u = edges[i][0]
        v = edges[i][1]
        wt = edges[i][2]
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    print(adj)
    
    pq = [] # priority queue
    dist = [float('inf')] * (n+1)
    parent = [i for i in range(n+1)]
    dist[1] = 0
    heapq.heappush(pq,(0,1)) # store the distance and the node
    
    while pq:
        dis, node = heapq.heappop(pq)
        for adjNode, edgeWeight in adj[node]:
            if dis + edgeWeight < dist[adjNode]:
                dist[adjNode] = dis + edgeWeight
                heapq.heappush(pq, (dist[adjNode], adjNode))
                parent[adjNode] = node
    
    if dist[n] == float('inf'):
        return [-1]
        
    path = []
    node = n
    # Time complexity: O(n)
    while parent[node] != node:
        path.append(node)
        node = parent[node]
    path.append(1)
    path.reverse()
    
    return path
    
# Time Complexity: O(ElogV) + O(n) # E is the number of edges, V is the number of nodes
# Space Complexity: O(V)
     
# Test Case
n = 5 # 1-5 nodes
m = 6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
# adj = [
#     [(2, 2), (4, 1)],              # 1
#     [(1, 2), (3, 4), (5, 5)],      # 2
#     [(2, 4), (4, 3), (5,1)],       # 3
#     [(1, 1), (3, 3)],              # 4
#     [(2, 5), (3, 1)],              # 5
# ]
print(shortestPath(n,m,edges))