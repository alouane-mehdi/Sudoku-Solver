def est_valide(sudoku, ligne, colonne, chiffre):
    """
    Vérifie si le chiffre peut être placé à la position donnée sans violer les règles du Sudoku.
    """
    for i in range(9):
        if sudoku[ligne][i] == chiffre or sudoku[i][colonne] == chiffre:
            return False

    debut_ligne, debut_colonne = 3 * (ligne // 3), 3 * (colonne // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[debut_ligne + i][debut_colonne + j] == chiffre:
                return False

    return True

def resoudre_sudoku_brute_force(sudoku):
    """
    Résout le Sudoku en utilisant la méthode de brute force.
    """
    for ligne in range(9):
        for colonne in range(9):
            if sudoku[ligne][colonne] == 0:
                for chiffre in range(1, 10):
                    if est_valide(sudoku, ligne, colonne, chiffre):
                        sudoku[ligne][colonne] = chiffre
                        if resoudre_sudoku_brute_force(sudoku):
                            return True
                        sudoku[ligne][colonne] = 0
                return False
    return True

# Exemple d'utilisation
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if resoudre_sudoku_brute_force(sudoku):
    print("Solution du Sudoku :")
    for row in sudoku:
        print(row)
else:
    print("Aucune solution trouvée pour ce Sudoku.")
