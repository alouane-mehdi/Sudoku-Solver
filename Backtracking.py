class Backtracking:
    def __init__(self, file_path):
        self.grid = self.read_grid_from_file(file_path)

    def read_grid_from_file(self, file_path):
        with open(file_path) as my_file:
            content = my_file.readlines()
        return [list(line.strip()) for line in content]

    def verifNumber(self, row, column, number):
        for i in range(0, 9):
            if self.grid[row][i] == number:
                return False
        for i in range(0, 9):
            if self.grid[i][column] == number:
                return False
        x = (column // 3) * 3
        y = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y + i][x + j] == number:
                    return False
        return True

    def findEmptySpots(self):
        empty_spots = []
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '_':
                    empty_spots.append((i, j))
        return empty_spots

    def test(self):
        empty_spots = self.findEmptySpots()
        if not empty_spots:
            return True
        row, col = empty_spots[0]
        for num in range(1, 10):
            if self.verifNumber(row, col, str(num)):
                self.grid[row][col] = str(num)
                if self.test():
                    return True
                self.grid[row][col] = '_'
        return False

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))


# Usage:
solver = Backtracking("sudoku2.txt")
