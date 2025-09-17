def countDistinctIslands(grid):
    n = len(grid)
    m = len(grid[0])
    vis = [[False for j in range(m)] for i in range(n)]
    shapes = set() # to store unique shapes
    
    for i in range(n):
        for j in range(m):
            if vis[i][j] == False and grid[i][j] == 1: # if not visited and is an island
                vec = [] # to store the shape
                dfs(i, j, vis, grid, vec, i, j)
                shapes.add(tuple(vec)) # add to set
    return len(shapes) # number of unique islands

def dfs(row, col, vis, grid, vec, row0, col0):
    vis[row][col] = True
    vec.append((row - row0, col - col0)) # store the shape by subtracting the starting point(base)
    
    delrow = [-1, 0, 1, 0]
    delcol = [0, -1, 0, 1]
    for i in range(4):
        nr = row+delrow[i]
        nc = col+delcol[i]
        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and vis[nr][nc] == False and grid[nr][nc] == 1:
            dfs(nr, nc, vis, grid, vec, row0, col0)
    return

    
# T.C = N x M x log(NxM) + (N X M X 4) # for loop + dfs
# S.C = N X M
    
grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,1,1],[1,1,0,1,0]]
a = countDistinctIslands(grid)
print(a)