def findCity(n, edges, distanceThreshold):
    dist = [[float('inf')] * n for i in range(n)]
    
    for i in edges:
        dist[i[0]][i[1]] = i[2]
        dist[i[1]][i[0]] = i[2]
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    cntCity = n
    cityNo = -1
    for city in range(n):
        cnt = 0
        for adjCity in range(n):
            if dist[city][adjCity] <= distanceThreshold:
                cnt += 1
        
        if cnt <= cntCity:
            cntCity = cnt
            cityNo = city
            
    return cityNo
    

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(findCity(n, edges, distanceThreshold))
