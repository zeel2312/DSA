from collections import deque

def shortestPath(grid, source, destination):
    n = len(grid)
    m = len(grid[0])
    
    q = deque() # queue
    dist = [[float('inf')] * m for i in range(n)]
    dist[source[0]][source[1]] = 0
    q.append((0,source[0],source[1])) # store the distance and the cell
    
    dr = [-1,0,1,0] # delta row in all 4 directions
    dc = [0,1,0,-1] # delta col in all 4 directions
    
    while q:
        dis, r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 1 and dist[nr][nc] > dis + 1:
                dist[nr][nc] = 1 + dis
                if nr == destination[0] and nc == destination[1]:
                    return dis + 1
                q.append((1+dis,nr,nc))
    return -1
    
# Time Complexity: O(N*M)
# Space Complexity: O(N*M)
     
# Test Case
source = [0,1]
destination = [2,2]
grid = [[1,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,0,0],[1,0,0,1]]
print(shortestPath(grid, source, destination))