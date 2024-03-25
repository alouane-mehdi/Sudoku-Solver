import pygame
import sys

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

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Solver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Read the Sudoku grid from the file
with open("evilsudoku.txt") as my_file:
    content = my_file.readlines()

grid = [list(line.strip()) for line in content]

# Solve the Sudoku puzzle
solveSudoku(grid)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the Sudoku grid
    cell_size = 50
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, WHITE, (j*cell_size, i*cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (j*cell_size, i*cell_size, cell_size, cell_size), 1)
            if grid[i][j] != '_':
                font = pygame.font.SysFont(None, 40)
                text = font.render(grid[i][j], True, BLUE)
                screen.blit(text, (j*cell_size + 20, i*cell_size + 10))

    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

