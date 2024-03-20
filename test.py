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
        return self.grid
    
    def returnNumber(self,x,y):
        #Get the number thanks to the position x and y (y for the the line and x for the number position)
        return self.grid[y-1][x-1]
    
    def returnRegion(self,row,column):
        region=[]
        print(region)
        row -=1
        column -=1
        x= column // 3 * 3
        y =row // 3 * 3
        for i in range(3):
            for j in range(3):
                region.append(self.grid[y+i][x+j])
        print(region)
                
    
    def verifNumber(self,row,column,number):
        #method to verif the entities in a row
        for i in range(0,9):
            if self.grid[row][i]==number:
                print("faux")
                return False
        #same method to verif but in column
        for i in range(0,9):
            if self.grid[i][column]==number:
                print("faux")
                return False
        #method to verif in region     
        x= (column // 3) * 3
        y= (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[y+i][x+j]==number:
                    print("faux")
                    return False 
        print("vrai")         
        return True
    
    def verifBoard(self):
        for row in range(9):
            for column in range(9):
                for number in range(1,10):
                    self.verifNumber(row,column,f"{number}")
                    if self.verifNumber(row,column,f"{number}") :
                        print("vrai")
                        return False
                    else:
                        print("nooo")  

    def emptyCase(self):
        self.empty_case=[]
        for i in range(0,9):
            for j in range(0,9):
                if self.grid[i][j] == "0":
                    self.empty_case.append((i+1, j+1))

        print("empty cases : ")
        for emplacement in self.empty_case:
            print(emplacement)

    
sudo=Sudoku()
sudo.verifBoard()