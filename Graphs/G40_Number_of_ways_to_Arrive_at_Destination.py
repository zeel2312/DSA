import heapq

def countPaths(n, roads):
    adj = [[] for i in range(n)]
    for i in roads:
        adj[i[0]].append((i[1], i[2]))
        adj[i[1]].append((i[0], i[2]))
        
    pq = [] # priority queue
    dist = [float('inf') for i in range(n)]
    ways = [0 for i in range(n)]
    dist[0] = 0
    ways[0] = 1
    heapq.heappush(pq, (0, 0)) # store the distance and the cell
    mod = 10**9 + 7
    
    # E(log V)
    while pq:
        dis, node = heapq.heappop(pq)
        for adjNode, edW in adj[node]:
            # this is the first time I am reaching with a short distance
            if dis + edW < dist[adjNode]:
                dist[adjNode] = dis + edW
                heapq.heappush(pq, (dist[adjNode], adjNode))
                ways[adjNode] = ways[node]
            elif dis + edW == dist[adjNode]:
                ways[adjNode] = (ways[adjNode] + ways[node]) % mod
                
    return ways[n-1] % mod
    
    

roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
n = 7
print(countPaths(n, roads))
