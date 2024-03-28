import random
random.seed()

class Bruteforce():
    def __init__(self):
        
        # Read the Sudoku grid from the file
        with open("evilsudoku.txt" ,"r") as my_file:
            # self.content = []
            content = my_file.readlines()
            # test = self.content.append(content)

        self.grid = [list(line.strip()) for line in content]

        # self.gridClone = self.grid.copy()
        self.gridClone = []
        for row in self.grid:
            self.gridClone.append(row.copy())
        print(self.gridClone)
        # Solve the Sudoku puzzle
        # if solveSudoku(grid):
        #     for row in grid:
        #         print(' '.join(row))


        # Faire une fonction pour renvoyer les case vide dans une 'liste vide' et donc avoir les positions des case. La fonction return la liste
        # Faire une autre fonction qui récupére la longueur de la liste pour générer un nombre équivalent de random.randint(1-9)

    def verifGrid(self):
        # print(self.grid)
        # Test on row

        for row in self.grid:
            # the 'set' enable to delete duplicate number, then the 'len' enable to count the len of the row
            if not len(set(row)) == 9: # if its equal to 9, then alls the numbers are in the row
                return False
        
        # Test on column

        for i in range(9): # iterate on y
            column = []
            for j in range(9): # iterate on X
                column.append(self.grid[j][i])
            if not len(set(column)) == 9: # The same logic as for row, but for column
                return False
        
        # Test on area 3x3

        for y0 in [0, 3, 6]: # it means that the loop will start on each value for Y [0, 3, 6]
            for x0 in [0, 3, 6]: # it means that the loop will start on each value for X [0, 3, 6]
                subgrid = []
                for i in range(0,3): 
                    for j in range(0,3):
                        if self.grid[y0+i][x0+j] in subgrid: # if the number is already in the subgrid, return False
                            return False
                        subgrid.append(self.grid[y0+i][x0+j]) # else, add it to the list 'subgrid' and continue the loop

        for i in range(9): # iterate on y
            for j in range(9): # iterate on x
                if self.grid[i][j] == '_': # '_' is the symbol to means that a spot is empty
                    return False

        return True # if all the rules are respected, return True
    
    def return_empty_spots(self):
        empty_spots = []
        for i in range(9): # iterate on y
            for j in range(9): # iterate on x
                if self.grid[i][j] == '_': # '_' is the symbol to means that a spot is empty
                    empty_spots.append((i,j)) # add the coordonates of the spot in the list
        return empty_spots # return the list
    
    def generate_random_number(self):
        list_numbers = []
        len_empty_spots = len(self.return_empty_spots()) # get the len of the list 'empty_spots' from the previous method 'return_empty_spots'
        for i in range(len_empty_spots):
            
            nbr_possibilites = random.randint(1,9) # generate a random number for every empty spots in the grid
            list_numbers.append(nbr_possibilites) # add this number in the list 'list_possibilities'
        return list_numbers
    
    def solve_sudoku(self):
        
        while self.verifGrid() == False:
            self.grid = []
            for row in self.gridClone:
                self.grid.append(row.copy())
            # self.grid = self.gridClone.copy()
            # print(self.grid)
            random_numbers = self.generate_random_number()
            # print(random_numbers)
            empty_spots = self.return_empty_spots()
            for number, spot in enumerate(empty_spots):
            
                self.grid[spot[0]][spot[1]] = str(random_numbers[number])  
            

            for row in self.grid:
                print(' '.join(row))
            print()

            
            

                
                        
grid = [[],[]]

    

test = Bruteforce()
# print (test.verifGrid())
# test.return_empty_spots()
# print (test.generate_random_number())
test.solve_sudoku()