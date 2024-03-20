class Sudoku():
        
        with open("t.txt") as my_file:
            tabl = my_file.read()

        tabl1 = []
        for i in tabl:
            if i != '\n':
                tabl1.append(i)

        tabl2 = []
        for i in range(0, 9):
            tabl2.append(tabl1[0:9])
            del tabl1[0:9]

        emplacements_vides = []

        for i in range(9):
            for j in range(9):
                if tabl2[i][j] == '_':
                    emplacements_vides.append((i, j))


        print("Emplacements vides:")
        for emplacement in emplacements_vides:
            print(emplacement)