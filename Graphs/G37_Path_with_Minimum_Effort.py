from collections import deque
import heapq

def minimumEffort(heights):
    n = len(heights)
    m = len(heights[0])
    
    pq = [] # priority queue
    dist = [[float('inf')] * m for i in range(n)]
    dist[0][0] = 0
    heapq.heappush(pq, (0, 0, 0)) # store the distance and the cell
    
    dr = [-1,0,1,0] # delta row in all 4 directions
    dc = [0,1,0,-1] # delta col in all 4 directions
    # E log V
    # n x m x 4 x log(n x m)
    while pq:
        diff, r, c = heapq.heappop(pq)
        if r == (n-1) and c == (m-1):
            return diff 
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m:
                newEffort = max(abs(heights[r][c] - heights[nr][nc]), diff)
                if newEffort < dist[nr][nc]:
                    dist[nr][nc] = newEffort
                    heapq.heappush(pq, (newEffort,nr,nc))
    return -1
    
# Time Complexity: O(N*M log(N*M))
# Space Complexity: O(N*M)
     
# Test Case
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(minimumEffort(heights))