import pygame
import sys

class SudokuSolver:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.WINDOW_SIZE = (500, 550)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Sudoku Solver")

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)

        # Read the Sudoku grid from the file
        with open("sudoku4.txt") as my_file:
            content = my_file.readlines()

        self.grid = [list(line.strip()) for line in content]

        # Solve the Sudoku puzzle
        self.solving = False

    def verifNumber(self, row, column, number):
        # Method to check entities in a row
        for i in range(0, 9):
            if self.grid[row][i] == number:
                return False
        # Method to check in the column
        for i in range(0, 9):
            if self.grid[i][column] == number:
                return False
        # Method to check in the region
        x = (column // 3) * 3
        y = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y + i][x + j] == number:
                    return False
        return True

    def findEmptySpot(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '_':
                    return i, j
        return None

    def solveSudoku(self):
        empty_spot = self.findEmptySpot()
        if not empty_spot:
            return True  # Puzzle solved
        row, col = empty_spot
        for num in range(1, 10):  # Try numbers from 1 to 9
            if self.verifNumber(row, col, str(num)):
                self.grid[row][col] = str(num)
                if self.solveSudoku():
                    return True  # If it leads to a solution, return True
                self.grid[row][col] = '_'  # If not a solution, backtrack
        return False  # If no number leads to a solution, return False

    def draw_grid(self):
        # Draw the Sudoku grid
        cell_size = 50
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(self.screen, self.WHITE, (j*cell_size, i*cell_size, cell_size, cell_size))
                pygame.draw.rect(self.screen, self.BLACK, (j*cell_size, i*cell_size, cell_size, cell_size), 1)
                if self.grid[i][j] != '_':
                    font = pygame.font.SysFont(None, 40)
                    text = font.render(self.grid[i][j], True, self.BLUE)
                    self.screen.blit(text, (j*cell_size + 20, i*cell_size + 10))

    def run(self):
        # Main loop
        solving = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if solve_button.collidepoint(mouse_pos):
                        self.solveSudoku()
                        solving = True

            self.screen.fill(self.WHITE)
            self.draw_grid()

            # Draw Solve Button
            solve_button = pygame.Rect(200, 500, 100, 40)
            pygame.draw.rect(self.screen, self.BLUE, solve_button)
            font = pygame.font.SysFont(None, 30)
            text = font.render("Solve", True, self.WHITE)
            self.screen.blit(text, (215, 510))

            pygame.display.update()

        # Quit Pygame
        pygame.quit()
        sys.exit()

# Run the SudokuSolver
if __name__ == "__main__":
    solver = SudokuSolver()
    solver.run()
