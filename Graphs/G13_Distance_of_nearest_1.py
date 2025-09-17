from collections import deque

def nearest1(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[0 for i in range(m)] for j in range(n)] # duplicate visited array
    distance = [[0 for i in range(m)] for j in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                visited[i][j] = 1 # mark visited
            else:
                visited[i][j] = 0 # mark not visited
                
    while queue:
        row, col, steps = queue.popleft() # pop from the queue
        distance[row][col] = steps
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dr,dc in directions: # traverse in all 4 directions
            nr = row + dr
            nc = col + dc
            # conditions: new row and col should be in the grid and the cell should not be visited
            if nr >= 0 and nr < n and nc >= 0 and nc < m and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append((nr, nc, steps+1)) # if not visited, add to queue
    return distance
    
grid = [[0,0,0],[0,1,0],[1,0,1]]
print(nearest1(grid))