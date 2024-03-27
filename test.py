import random

class Bruteforce():
    def __init__(self):
        # Read the Sudoku grid from the file
        with open("evilsudoku.txt") as my_file:
            content = my_file.readlines()

        self.grid = [list(line.strip()) for line in content]

    def verifGrid(self):
        print(self.grid)

        # Test on row
        for row in self.grid:
            if not len(set(row)) == 9:
                return False
        
        # Test on column
        for i in range(9):
            column = []
            for j in range(9):
                column.append(self.grid[j][i])
            if not len(set(column)) == 9:
                return False
        
        # Test on area 3x3
        for y0 in [0, 3, 6]:
            for x0 in [0, 3, 6]:
                subgrid = []
                for i in range(3):
                    for j in range(3):
                        if self.grid[y0 + i][x0 + j] in subgrid:
                            return False
                        subgrid.append(self.grid[y0 + i][x0 + j])
        return True

test = Bruteforce()
print(test.verifGrid())
