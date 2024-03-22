

# Define the method verifNumber
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


def findEmptySpots(grid):
    empty_spots = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == '_':
                empty_spots.append((i, j))
    return empty_spots


def solveSudoku(grid):
    empty_spots = findEmptySpots(grid)
    if not empty_spots:
        return True  # Puzzle solved
    row, col = empty_spots[0]  # Get the first empty spot
    for num in range(1, 10):  # Try numbers from 1 to 9
        if verifNumber(grid, row, col, str(num)):
            grid[row][col] = str(num)
            if solveSudoku(grid):
                return True  # If it leads to a solution, return True
            grid[row][col] = '_'  # If not a solution, backtrack
    return False  # If no number leads to a solution, return False



# Read the Sudoku grid from the file
with open("evilsudoku.txt") as my_file:
    content = my_file.readlines()

grid = [list(line.strip()) for line in content]

# Solve the Sudoku puzzle
if solveSudoku(grid):
    for row in grid:
        print(' '.join(row))
