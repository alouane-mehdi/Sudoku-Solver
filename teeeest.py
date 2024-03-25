with open("evilsudoku.txt") as my_file:
    content = my_file.readlines()

grid = [list(line.strip()) for line in content]

def isGridFull(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == '_':
                break
            else:
                return True
            
def verifGrid(grid):
    if isGridFull(grid)==True:
        for row in range(9):
            for col in range(9):
                for num in range(9):
                    if verifNumber(grid,row,col,num):
                        print("c'est bon")
    else : 
        print("noon") 

def verifNumber(grid, row, column, number):
    # Method to check entities in a row
    for i in range(0, 9):
        if grid[row][i] == number:
            return False
    # Method to check in the column
    for i in range(0, 9):
        if grid[i][column] == number:
            return False
    # Method to check in the region
    x = (column // 3) * 3
    y = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y + i][x + j] == number:
                return False
    return True

verifGrid(grid)