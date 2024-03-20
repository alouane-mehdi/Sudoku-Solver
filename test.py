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
    
    def returnRegion(self,x,y):
        region=[]
        x = x //3
        print(x)
        for i in range(x,x+3):
            for j in range(0,3):
                print(i)
                region.append(self.returnRow(i)[j])
        print(region)
        
    
    #method to verif the entities in a row
    def verifNumber(self,row,column):
        for i in range(0,9):
            if self.grid[row-1][i]==0:
                print(0)
            else :
                print(self.grid[row-1][i])

    #same method to verif but in column
        for i in range(0,9):
            if self.grid[i][column-1]==0:
                print(0)
            else :
                print(self.grid[i][column-1])

    #method to verif in region     
        x0= column // 3 * 3
        y0=row // 3 * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[y0+i][x0+j]==0:
                    print(0)
                else :
                    print(self.grid[y0+i][x0+j])  
    

    
sudo=Sudoku()
# sudo.returnRegion(4,1)
sudo.verifNumber(1,1)