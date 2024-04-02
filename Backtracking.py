import time

start_time = time.time()


class Backtracking:
    def __init__(self, file_path):
        # Initialize the Backtracking solver with a Sudoku grid from a file
        self.grid = self.read_grid_from_file(file_path)

    def read_grid_from_file(self, file_path):
        # Read the Sudoku grid from a file
        with open(file_path) as my_file:
            content = my_file.readlines()
        # Parse the content to create a 2D grid
        return [list(line.strip()) for line in content]

    def verifNumber(self, row, column, number):
        # Check if placing a number in a certain position is valid
        # Check row
        for i in range(0, 9):
            if self.grid[row][i] == number:
                return False
        # Check column
        for i in range(0, 9):
            if self.grid[i][column] == number:
                return False
        # Check 3x3 subgrid
        x = (column // 3) * 3
        y = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y + i][x + j] == number:
                    return False
        return True

    def findEmptySpots(self):
        # Find all empty spots (positions with '_') in the grid
        empty_spots = []
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '_':
                    empty_spots.append((i, j))
        return empty_spots

    def solve_sudoku(self):
        # Backtracking algorithm to solve the Sudoku puzzle
        empty_spots = self.findEmptySpots()
        if not empty_spots:
            # If there are no empty spots left, puzzle is solved
            return True
        # Get the first empty spot
        row, col = empty_spots[0]
        # Try placing numbers from 1 to 9
        for num in range(1, 10):
            if self.verifNumber(row, col, str(num)):
                # If placing the number is valid, try solving recursively
                self.grid[row][col] = str(num)
                if self.solve_sudoku():
                    # If the puzzle is solved, return True
                    return True
                # If not, backtrack and try next number
                self.grid[row][col] = '_'
        # If no valid number can be placed, return False to backtrack
        return False

    def print_grid(self):
        # Print the Sudoku grid
        for row in self.grid:
            print(' '.join(row))


# Usage:
# Create a Backtracking solver instance with a Sudoku file
solver = Backtracking("sudoku2.txt")
# Solve the Sudoku puzzle
solver.solve_sudoku()
# Print the solved Sudoku grid
solver.print_grid()

end_time = time.time()
execution_time = end_time - start_time
print("Durée d'exécution:", execution_time, "secondes")