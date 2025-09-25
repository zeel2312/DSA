from collections import deque
import heapq

def dijkstra(V, adj, S):
    pq = [] # priority queue
    dist = [float('inf')] * V
    dist[S] = 0
    heapq.heappush(pq,(0,S)) # store the distance and the node
    
    while pq:
        dis, node = heapq.heappop(pq)
        for adjNode, edgeWeight in adj[node]:
            if dis + edgeWeight < dist[adjNode]:
                dist[adjNode] = dis + edgeWeight
                heapq.heappush(pq, (dist[adjNode], adjNode))
    return dist
    
# Time Complexity: O(ElogV) # E is the number of edges, V is the number of nodes
# Space Complexity: O(V)
     
# Test Case
V = 6 # 0-5 nodes
adj = [
    [(1, 4), (2, 2)],       # 0
    [(2, 5), (3, 10)],      # 1
    [(4, 3)],               # 2
    [(5, 11)],              # 3
    [(3, 4)],               # 4
    []                      # 5
]
S = 0 # source
print(dijkstra(V, adj, S))