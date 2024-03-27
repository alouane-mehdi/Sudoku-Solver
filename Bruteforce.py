import random

class Bruteforce():
    def __init__(self):
        
        # Read the Sudoku grid from the file
        with open("evilsudoku.txt") as my_file:
            # self.content = []
            content = my_file.readlines()
            # test = self.content.append(content)

        self.grid = [list(line.strip()) for line in content]


        # Solve the Sudoku puzzle
        # if solveSudoku(grid):
        #     for row in grid:
        #         print(' '.join(row))


        # Faire une fonction pour renvoyer les case vide dans une 'liste vide' et donc avoir les positions des case. La fonction return la liste
        # Faire une autre fonction qui récupére la longueur de la liste pour générer un nombre équivalent de random.randint(1-9)

    def verifGrid(self):

        print (self.grid)

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
            list_number.append(nbr_possibilites) # add this number in the list 'list_possibilities'
        print(list_possibilities)
        # print (len_empty_spots)
    


        

test = Bruteforce()
print (test.verifGrid())
# test.return_empty_spots()
# test.generate_random_number()