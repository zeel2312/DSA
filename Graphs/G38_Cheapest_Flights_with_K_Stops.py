from collections import deque

def CheapestFlight(n, flights, src, dst, k):
    adj = [[] for i in range(n)]
    for i in flights:
        adj[i[0]].append((i[1], i[2]))
    print(adj)
    
    q = deque()
    q.append((0, src, 0)) # (stops, node, dist)
    dist = [float('inf')] * (n)
    dist[src] = 0
    # O(E) => len(flights)
    while q:
        stops, node, cost = q.popleft()
        if stops > k:
            continue
        for adjNode, edw in adj[node]:
            if cost + edw < dist[adjNode] and stops <=k:
                dist[adjNode] = cost + edw
                q.append((stops+1, adjNode, dist[adjNode]))
    
    if dist[dst] == float('inf'):
        return -1
    else:
        return dist[dst]
    
    
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(CheapestFlight(n, flights, src, dst, k))
