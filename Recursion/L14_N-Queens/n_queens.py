def f(col,board,ans,n):
    if(col == len(board)): #base case
        ans.append([''.join(row) for row in board])
        return
    
    for row in range(len(board)):
        if isSafe(row,col,board,n):
            board[row][col] = 'Q'
            f(col+1,board,ans,n)
            board[row][col] = '.'
        
    return ans

# Helper Function
def isSafe(row,col,board,n):
    #check upper diagonal
    duprow = row
    dupcol = col
    while row>=0 and col>=0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1
    
    #check lower diagonal
    row = duprow
    col = dupcol
    while row<n and col>=0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1
        
    #check same row
    row = duprow
    col = dupcol
    while col>=0:
        if board[row][col] == 'Q':
            return False
        col -= 1
        
    return True
    
    # for i in range(col): #checking in the same row
    #     if board[row][i] == 'Q':
    #         return False
    # for i,j in zip(range(row,-1,-1),range(col,-1,-1)): #checking in the left diagonal
    #     if board[i][j] == 'Q':
    #         return False
    # for i,j in zip(range(row,n),range(col,-1,-1)): #checking in the right diagonal
    #     if board[i][j] == 'Q':
    #         return False
    # return True

n = 4
board = [['.' for _ in range(n)] for _ in range(n)]
ans = []
f(0,board,ans,n)
print(ans)