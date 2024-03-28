import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set window size
WINDOW_SIZE = (450, 450)
CELL_SIZE = 50

# Set up the window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Solver")

# Font
font = pygame.font.SysFont(None, 40)

# Read the Sudoku grid from the file
with open("sudoku3.txt") as my_file:
    content = my_file.readlines()

grid = [list(line.strip()) for line in content]

# Function to draw the grid
def draw_grid():
    screen.fill(WHITE)
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (450, i * CELL_SIZE), thickness)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, 450), thickness)

# Function to fill the initial numbers
def fill_initial_numbers():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))

# Function to solve Sudoku
def solve_sudoku():
    empty_spots = find_empty_spots()
    if not empty_spots:
        return True  # Puzzle solved
    row, col = empty_spots[0]  # Get the first empty spot
    for num in range(1, 10):  # Try numbers from 1 to 9
        if verif_number(row, col, num):
            grid[row][col] = num
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            text = font.render(str(num), True, BLACK)
            screen.blit(text, (col * CELL_SIZE + 20, row * CELL_SIZE + 10))
            pygame.display.update()
            pygame.time.delay(100)  # Delay for visualization
            if solve_sudoku():
                return True  # If it leads to a solution, return True
            grid[row][col] = 0  # If not a solution, backtrack
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.display.update()
            #
    return False  # If no number leads to a solution, return False

# Function to check if number is valid
def verif_number(row, col, num):
    return (
        is_row_valid(row, num)
        and is_col_valid(col, num)
        and is_box_valid(row - row % 3, col - col % 3, num)
    )

def is_row_valid(row, num):
    return num not in grid[row]

def is_col_valid(col, num):
    return all(grid[i][col] != num for i in range(9))

def is_box_valid(start_row, start_col, num):
    return all(
        num != grid[start_row + i][start_col + j] for i in range(3) for j in range(3)
    )

# Function to find empty spots
def find_empty_spots():
    empty_spots = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty_spots.append((i, j))
    return empty_spots

# Main loop
running = True
draw_grid()
fill_initial_numbers()
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            solve_sudoku()

    

pygame.quit()
sys.exit()
