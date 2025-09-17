def floodFill(sr, sc, newColor, image):
    iniColor = image[sr][sc] # initial color # 1
    ans = image # [[1,1,1],[1,1,0],[1,0,1]]
    dfs(sr, sc, ans, newColor, iniColor, image) # dfs(1,1,[[1,1,1],[1,1,0],[1,0,1]],2,1,[[1,1,1],[1,1,0],[1,0,1]])
    return ans
    
def dfs(row, col, ans, newColor, iniColor, image):
    delRow = [-1,0,1,0] # top, right, bottom, left
    delCol = [0,1,0,-1]
    
    ans[row][col] = newColor # changing the color # ans[1][1] = 2
    for i in range(4): # traverse in all 4 directions
        newRow = row + delRow[i] # newRow = 1 + (-1)
        newCol = col + delCol[i] # newCol = 1 + (0)
         # print(newRow, newCol) # (0,1)
        # conditions: new row and col should be in the grid and the cell should be equal to 'iniColor' and the cell should not be visited before
        if newRow>=0 and newRow<len(ans) and newCol>=0 and newCol<len(ans[0]) and image[newRow][newCol] == iniColor and ans[newRow][newCol] != newColor: # Yes
            dfs(newRow, newCol, ans, newColor, iniColor, image) # dfs(0,1,[[1,1,1],[1,2,0],[1,0,1]],2,1,[[1,1,1],[1,1,0],[1,0,1]])
            
sr = 1
sc = 1
newColor = 2
image = [[1,1,1],[1,1,0],[1,0,1]]
print(floodFill(sr, sc, newColor, image))
    