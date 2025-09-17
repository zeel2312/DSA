def numIsLands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    visited = [[False for i in range(cols)] for j in range(rows)] # duplicate visited array
    for i in range(rows):
        for j in range(cols):
            # conditions: cell should be '1' and the cell should not be visited
            if grid[i][j] == '1' and visited[i][j] == False:
                count += 1
                bfs(i, j, visited, grid)
    return count

def bfs(row, col, visited, grid):
    queue = []
    queue.append([row, col])
    visited[row][col] = True
    while queue:
        row, col = queue.pop(0) # pop from the queue
        # traverse in the neightbours and mark them visited
        for delrow in range(-1, 2): # if we want to find neighbors we have to traverse in all 4 directions
            for delcol in range(-1, 2):
                newrow = row + delrow
                newcol = col + delcol
                # conditions: new row and col should be in the grid and the cell should be '1' and the cell should not be visited
                if newrow >= 0 and newrow < len(grid) and newcol >= 0 and newcol < len(grid[0]) and grid[newrow][newcol] == '1' and visited[newrow][newcol] == False:
                    visited[newrow][newcol] = True
                    queue.append([newrow, newcol]) # if not visited, add to queue      
    return

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid1 = [["0"]]
grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIsLands(grid2))