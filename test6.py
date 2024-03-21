def est_rangee_valide(sudoku, ligne):
    """
    Vérifie si une ligne du sudoku est valide.
    """
    chiffres = set()
    for col in range(9):
        if sudoku[ligne][col] in chiffres:
            return False
        if sudoku[ligne][col] != 0:
            chiffres.add(sudoku[ligne][col])
    return True

def est_colonne_valide(sudoku, colonne):
    """
    Vérifie si une colonne du sudoku est valide.
    """
    chiffres = set()
    for ligne in range(9):
        if sudoku[ligne][colonne] in chiffres:
            return False
        if sudoku[ligne][colonne] != 0:
            chiffres.add(sudoku[ligne][colonne])
    return True

def est_carre_valide(sudoku, carre_ligne, carre_colonne):
    """
    Vérifie si un carré 3x3 du sudoku est valide.
    """
    chiffres = set()
    for ligne in range(3):
        for colonne in range(3):
            val = sudoku[carre_ligne * 3 + ligne][carre_colonne * 3 + colonne]
            if val in chiffres:
                return False
            if val != 0:
                chiffres.add(val)
    return True

def est_sudoku_valide(sudoku):
    """
    Vérifie si un sudoku est valide.
    """
    for i in range(9):
        if not est_rangee_valide(sudoku, i) or not est_colonne_valide(sudoku, i):
            return False

    for i in range(3):
        for j in range(3):
            if not est_carre_valide(sudoku, i, j):
                return False

    return True

# Exemple d'utilisation
sudoku_termine = [
    [1 ,3 ,9, 4 ,6 ,7, 8 ,5 ,2],
    [6, 8, 7, 3, 2, 5, 9, 1, 4],
    [2, 4, 5, 8, 1 ,9 ,3, 7, 6],
    [5 ,9 ,3 ,6, 7 ,8, 2, 4 ,1],
    [4 ,6, 1, 9 ,3 ,2, 7 ,8, 5],
    [7 ,2 ,8 ,1 ,5, 4, 6, 3, 9],
    [9, 5, 6, 7 ,4 ,3 ,1 ,2, 8],
    [8 ,7 ,4 ,2 ,9, 1, 5, 6, 3],
    [3 ,1, 2, 5, 8, 6 ,4, 9 ,7]
]

if est_sudoku_valide(sudoku_termine):
    print("Le Sudoku est correctement résolu.")
else:
    print("Le Sudoku n'est pas correctement résolu.")