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

def solveSudoku(grid):
    # Iterating through all cells of the grid
    for row in range(9):
        for col in range(9):
            # If the cell is empty
            if grid[row][col] == '_':
                # Try every possible number from 1 to 9
                for num in range(1, 10):
                    num = str(num)
                    # If the number is valid in this position
                    if verifNumber(grid, row, col, num):
                        # Place the number and continue solving
                        grid[row][col] = num
                        if solveSudoku(grid):
                            return True
                        # If it doesn't lead to a solution, backtrack by removing the number
                        grid[row][col] = '_'
                # If no number works, return False
                return False
    # If all cells are filled, puzzle is solved
    return True

# Read the Sudoku grid from the file
with open("evilsudoku.txt") as my_file:
    content = my_file.readlines()

grid = [list(line.strip()) for line in content]

# Solve the Sudoku puzzle
if solveSudoku(grid):
    for row in grid:
        print(' '.join(row))