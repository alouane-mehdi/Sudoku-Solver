from Verification import Verif
from Grid import Grid


class Sudoku:
    
    def __init__(self) :
        gridClass=Grid()
        self.verif=Verif()

        self.grid = gridClass.grid()

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

    def solveSudoku(self):
        # Iterating through all cells of the grid
        for row in range(9):
            for col in range(9):
                # If the cell is empty
                if self.grid[row][col] == '0':
                    # Try every possible number from 1 to 9
                    for num in range(1, 10):
                        num = str(num)
                        # Place the number and continue solving
                        self.grid[row][col] = num
                        if self.solveSudoku():
                            return True
                        self.grid[row][col] = '0'
                    # If no number works, return False
                    return False
        # If all cells are filled, puzzle is solved
        
        for row in self.grid:
            print(' '.join(row))
        return True
    
    def solveSudokuTest(self):
        empty_spot= []
        empty_spot.append(self.findEmptySpots())
        for spots in empty_spot[0]:
            for num in range(1,10):
                self.grid[spots[0]][spots[1]]=str(num)
                if self.verif.is_grid_valid():
                    print(" c'est bon ")
                    print(self.grid)
                    return True

            # print("c'est pas bon")
            # for spots in empty_spot:
            #     for num in range(1,10):
            #         self.grid[spots[0]][spots[1]]='0'
            # self.solveSudokuTest()


    def printGrid(self):
        print(self.grid)
        # empty_spot= []
        # empty_spot.append(self.findEmptySpots())
        # print(empty_spot)
        # for i in empty_spot[0]:
        #     print(i[0],i[1])
    # def SolveSudokuTest():
    #     for i in findEmptySpots():

sudoku=Sudoku()
# sudoku.solveSudokuTest()
sudoku.printGrid()
