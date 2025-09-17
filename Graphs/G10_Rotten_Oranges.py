from collections import deque

def orangesRotting(grid):
    n = len(grid)
    m = len(grid[0])
    queue = deque()
    visited = [[False for i in range(m)] for j in range(n)] # duplicate visited array
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
                visited[i][j] = 2
            else:
                visited[i][j] = 0
    
    tm = 0 # maximum time required
    delrow = [-1, 1, 0, 0] # top, bottom, left, right
    delcol = [0, 0, -1, 1]
    
    while(queue):
        r, c, t = queue.popleft() # pop from the queue
        for i in range(4):
            # traverse in the neightbours
            newrow = r + delrow[i] # newrow = 0 + (-1)
            newcol = c + delcol[i] # newcol = 0 + (0)
            # conditions: new row and col should be in the grid and the cell should be '1' and the cell should not be visited
            if newrow >= 0 and newrow < n and newcol >= 0 and newcol < m and grid[newrow][newcol] == 1 and visited[newrow][newcol] == False:
                visited[newrow][newcol] = 2
                queue.append((newrow, newcol, t+1))
                tm = max(tm, t+1)
    # check if all the oranges are rotten
    for i in range(n):
        for j in range(m):
            # conditions: cell should be '1' and the cell should not be visited
            if grid[i][j] == 1 and visited[i][j] != 2:
                return -1
    return tm

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))