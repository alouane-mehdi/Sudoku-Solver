import random

class BruteForce:
    
    def __init__(self) :

        bruteforce=BruteForce()
        bruteforce.test()

        with open("evilsudoku.txt") as my_file:
            liste = my_file.read()

            liste1 = []
            for i in liste:
                if i != '\n':
                    liste1.append(i)

            self.grid = []
            for i in range(0, 9):
                self.grid.append(liste1[0:9])
                del liste1[0:9]

            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] == '_':
                        self.grid[i][j] = '0'

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
    
    def verifNumber(self,row, column, number):
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
    
    def findEmptySpots(self):
        empty_spots = []
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '0':
                    empty_spots.append((i, j))
        return empty_spots
    
    def solveSudokuTest(self):
        
        empty_spots = self.findEmptySpots()
        if not empty_spots:
            # Si aucune case vide n'est trouvée, le sudoku est déjà résolu
            return True

        # Sélectionnez la première case vide
        row, col = empty_spots[0]

        # Pour chaque chiffre de 1 à 9, essayez de le placer dans la case vide
        for num in range(1, 10):
            self.grid[row][col] = num
            if self.solveSudokuTest():
                print(self.grid)
                return True
            # Si la solution n'est pas possible, réinitialisez la case et essayez le prochain nombre
            self.grid[row][col] = '0'

        # Si aucun nombre ne fonctionne pour cette case, le sudoku est insoluble à partir de ce point
        return False


    def teste(self):
        empty_spot= []
        empty_spot.append(self.findEmptySpots())
        while self.is_grid_valid():
            for spots in empty_spot:
                print("spots ",spots)
                randomNumber=random.randint(1,9)
                self.grid[empty_spot[0][spots][0]][empty_spot[0][spots][1]]= f"{randomNumber}"
                print(random.randint(1,9))
                print(self.grid)
    
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

