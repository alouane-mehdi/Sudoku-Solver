class Sudoku:
    
    def __init__(self) :
        #read sudoku.txt to have the sudoku
        #same but we'll have line per line for row
        with open("sudoku.txt", "r") as f:
            self.row = f.readlines()
        with open("sudoku.txt") as my_file:
            self.grid = my_file.read()

            self.grid1 = []
            for i in self.grid:
                if i != '\n':
                    self.grid1.append(i)

            self.grid2 = []
            for i in range(0, 9):
                self.grid2.append(self.grid1[0:9])
                del self.grid1[0:9]

            for i in range(len(self.grid2)):
                for j in range(len(self.grid2[i])):
                    if self.grid2[i][j] == '_':
                        self.grid2[i][j] = '0'        
    
    def createGrid(self):
        print(self.grid2)

    def printGrid(self):
        print(self.grid)
    
    def returnRow(self,number):
        #take the row thanks to the indice number 
        self.line = self.row[number-1]
        return self.line

    def returnColumn(self,number):
        #take the column thank to the indice of each number
        column= []
        for i in range(0,9):
            column.append(self.row[i][number-1])
        return column    
    
    #method to verif the entities in a row
    def verifRow(self,number):
        # variable n to know wich case the program verif
        n=0
        # variable n to know when the program finish its verif
        end_verif=0
        #for each number in a row , we look if it's a number or not and what is the number
        for i in self.returnRow(number):
            n+=1
            numberHere=False
            for j in range(1,10):
                end_verif+=1
                if end_verif==9:
                    end_verif=0
                    if i == f"{j}":
                        print(f"num : {i} in case {n}")
                        numberHere=True
                    else:
                        if numberHere == False:
                            print(f"not num in case {n}")
                elif i == f"{j}":
                    print(f"num : {i} in case {n}")
                    numberHere=True

    #same method to verif but in column
    def verifColumn(self,number):
        # variable n to know wich case the program verif
        n=0
        # variable n to know when the program finish its verif
        end_verif=0
        #for each number in a row , we look if it's a number or not and what is the number
        for i in self.returnColumn(number):
            n+=1
            numberHere=False
            for j in range(1,10):
                end_verif+=1
                if end_verif==9:
                    end_verif=0
                    if i == f"{j}":
                        print(f"num : {i} in case {n}")
                        numberHere=True
                    else:
                        if numberHere == False:
                            print(f"not num in case {n}")
                elif i == f"{j}":
                    print(f"num : {i} in case {n}")
                    numberHere=True
    

    
sudo=Sudoku()
sudo.returnColumn(1)
sudo.verifColumn(1)
sudo.createGrid()