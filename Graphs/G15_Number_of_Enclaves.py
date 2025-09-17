from collections import deque

def numberOfEnclaves(grid):
    queue = deque()
    n = len(grid)
    m = len(grid[0])
    vis = [[False for j in range(m)] for i in range(n)]
    # Traverse to find boundary 1's
    for i in range(n):
        for j in range(m):
            # first row, first col, last row, last col
            if i==0 or j==0 or i==n-1 or j==m-1:
                if grid[i][j] == 1 and vis[i][j] == False:
                    queue.append((i,j))
                    vis[i][j] = True
    while queue:
        row, col = queue.popleft()
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        for dr,dc in dirs:
            nr, nc = row+dr, col+dc
            if 0<=nr<n and 0<=nc<m and vis[nr][nc]==False and grid[nr][nc]==1:
                queue.append((nr,nc))
                vis[nr][nc] = True
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and vis[i][j] == 0: # the 1's that were not touched by boundary
                count += 1
    return count
    
# T.C = N x M
# S.C = N X M
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
a = numberOfEnclaves(grid)
print(a)