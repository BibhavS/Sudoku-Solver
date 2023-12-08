N = 9
def puzzle(a):
    for i in range(N):
        for j in range(N):
            print(a[i][j],end = " ")
        print()

def solveSudoku(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    sRow = row - row % 3
    sCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + sRow][j + sCol] == num:
                return False
    return True
 
def sudoku(grid, row, col):
 
    if (row == N - 1 and col == N):
        return True
    if col == N:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1): 
     
        if solveSudoku(grid, row, col, num):
         
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
game  = [[1, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
 
if (sudoku(game, 0, 0)):
    puzzle(game)
else:
    print("No Solution")