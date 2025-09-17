import numpy as np

def f(board):
    solve(board)
    
def solve(board):
    for i in range(9): #row
        for j in range(9): #col
            if board[i][j] == 0: #empty
                for k in range(1,10): #1-9
                    if isValid(i,j,k,board): #check
                        board[i][j] = k #place
                        solve(board) #recursion
                        board[i][j] = 0 #backtrack
                return
    print(np.matrix(board))

#check
def isValid(row, col, num, board):
    for i in range(9):
        if board[row][i] == num: #check the row
            return False
        if board[i][col] == num: #check the column
            return False
        if board[3*(row//3) + i//3][3*(col//3) + i%3] == num: #check the 3x3box
            return False
    return True

board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
f(board)