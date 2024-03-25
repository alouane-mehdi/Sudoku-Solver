
class Grid:
    def __init__(self) -> None:
        with open("evilsudoku.txt") as my_file:
            content = my_file.readlines()
        grid = [list(line.strip()) for line in content]
           
class Verif:
    def __init__(self) -> None:
        
        with open("evilsudoku.txt") as my_file:
            content = my_file.readlines()

        self.grid = [list(line.strip()) for line in content]

    def isRowValid(self,grid, row):
        """
        look at if the row is valid
        """
        num = set()
        for col in range(9):
            if self.grid[row][col] in num:
                return False
            if self.grid[row][col] != 0:
                num.add(self.grid[row][col])
        return True

    def isColValid(self,grid, column):
        """
        look at if the column is valid
        """
        num = set()
        for row in range(9):
            if self.grid[row][column] in num:
                return False
            if self.grid[row][column] != 0:
                num.add(self.grid[row][column])
        return True

    def isSquareValid(self,grid, square_row, square_column):
        """
        look at if the square 3x3 is valid
        """
        num = set()
        for row in range(3):
            for column in range(3):
                val = self.grid[square_row * 3 + row][square_column * 3 + column]
                if val in num:
                    return False
                if val != 0:
                    num.add(val)
        return True

    def isGridValid(self,grid):
        """
        look at if the grid is valid
        """
        for i in range(9):
            if not self.isRowValid(self.grid, i) or not self.isColValid(self.grid, i):
                return False

        for i in range(3):
            for j in range(3):
                if not self.isSquareValid(self.grid, i, j):
                    print("no")
                    return False

        return True

yeah=Verif()
yeah.isGridValid(Grid.grid)