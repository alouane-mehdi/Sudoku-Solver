import random

class BruteForce:
    
    def __init__(self,file_path) :
        self.grid = self.read_grid_from_file(file_path)

    def read_grid_from_file(self, file_path):
        with open(file_path) as my_file:
            content = my_file.readlines()
        return [list(line.strip()) for line in content]

    def is_row_valid(self, row):
        """
        Check if the row is valid.
        """
        num = set()
        for col in range(9):
            if self.grid[row][col] in num:
                return False
            if self.grid[row][col] != '_':
                num.add(self.grid[row][col])
        return True

    def is_col_valid(self, column):
        """
        Check if the column is valid.
        """
        num = set()
        for row in range(9):
            if self.grid[row][column] in num:
                return False
            if self.grid[row][column] != '_':
                num.add(self.grid[row][column])
        return True

    def is_square_valid(self, square_row, square_column):
        """
        Check if the 3x3 square is valid.
        """
        num = set()
        for row in range(3):
            for column in range(3):
                val = self.grid[square_row * 3 + row][square_column * 3 + column]
                if val in num:
                    return False
                if val != '_':
                    num.add(val)
        return True
    
    def is_grid_full(self):
        for i in range(9):
            for j in range(9):
                if not self.grid[i][j] == '0' or '_' :
                    print("not full grid")
                    print(i,j)
                    return False
        print("full")
        return True

    def is_grid_valid(self):
        """
        Check if the entire grid is valid.
        """
        
        for i in range(9):
            if not self.is_row_valid(i) or not self.is_col_valid(i):
                print("not valid column or row")
                return False

        for i in range(3):
            for j in range(3):
                if not self.is_square_valid(i, j):
                    print("not valid square")
                    return False
        print("valid")
        print(self.grid)
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
        print(empty_spots)
        while empty_spots:
            for spot in empty_spots:
                row, col = spot
                randomNumber = random.randint(1, 9)
                self.grid[row][col] = str(randomNumber)
            if not self.is_grid_valid():
                self.test()
            else:
                break
        for i in range(9):
            print(self.grid[i])
        

    def printGrid(self):
        print(self.grid)

bruteforce=BruteForce("evilsudoku.txt")
bruteforce.test()