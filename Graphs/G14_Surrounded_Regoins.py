def solve(board):
    n = len(board)
    m = len(board[0])
    visited = [[False for i in range(m)] for j in range(n)]
    
    for j in range(m):# Traverse first row and last row
        if visited[0][j] == False and board[0][j] == "O": # first row
            dfs(0, j, visited, board)
        if visited[n-1][j] == False and board[n-1][j] == "O": # last row
            dfs(n-1, j, visited, board)
    for i in range(n): # Traverse first column and last column
        if visited[i][0] == False and board[i][0] == "O": # first col
            dfs(i, 0, visited, board)
        if visited[i][m-1] == False and board[i][m-1] == "O": # last col
            dfs(i, m-1, visited, board)
    print(visited)
    for i in range(n): # the "O"s that were not touched by bfs
        for j in range(m):
            if visited[i][j] == False and board[i][j] == "O":
                board[i][j] = "X"
    return board
    
def dfs(row, col, visited, board):
    visited[row][col] = True
    # check for top, right, bottom, left
    dr = [-1,0,+1,0]
    dc = [0,1,0,-1]
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if nr>=0 and nr<len(board) and nc>=0 and nc<len(board[0]) and visited[nr][nc] == False and board[nr][nc] == "O":
            print("YES")
            dfs(nr, nc, visited, board)
    

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solve(board))