class Sudoku:
    
    def __init__(self) :
        #read sudoku.txt to have the sudoku
        with open("sudoku.txt", "r") as f:
            self.grid = f.read()  
        #same but we'll have line per line for row
        with open("sudoku.txt", "r") as f:
            self.row = f.readlines()
    
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
            column.append(self.row[i][0])
        print(column[3])    
    
    def verifRow(self):
        # variable n to know wich case the program verif
        n=0
        # variable n to know when the program finish its verif
        end_verif=0
        #for each number in a row , we look if it's a number or not and what is the number
        for i in self.returnRow(1):
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
    
    # def verifColumn(self):


    
sudo=Sudoku()
sudo.returnColumn(1)