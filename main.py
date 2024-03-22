class Sudoku:
    
    def __init__(self) :
        #read sudoku.txt to have the sudoku
        #same but we'll have line per line for row
        with open("sudoku.txt", "r") as f:
            self.row = f.readlines()
        with open("sudoku.txt") as my_file:
            self.liste = my_file.read()

            self.liste1 = []
            for i in self.liste:
                if i != '\n':
                    self.liste1.append(i)

            self.grid = []
            for i in range(0, 9):
                self.grid.append(self.liste1[0:9])
                del self.liste1[0:9]

            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] == '_':
                        self.grid[i][j] = '0'        
    
    def printGrid(self):
        print(self.grid)
    
    def returnNumber(self,x,y):
    #Get the number thanks to the position x and y (y for the the line and x for the number position)
        return self.grid[y-1][x-1]
    

sudo = Sudoku()
sudo.printGrid()