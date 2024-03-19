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

    def possibility(self, number):
        for i in self.returnRow(1):
            if i == number:
                print("yessai")
            else:
                print("faux")

sudo=Sudoku()
sudo.possibility("7")