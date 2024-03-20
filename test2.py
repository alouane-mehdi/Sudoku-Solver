def est_valide(grille, ligne, colonne, nombre):

    # Vérifie si le nombre est valide dans le bloc 3x3
    bloc_ligne = ligne // 3 * 3
    bloc_colonne = colonne // 3 * 3
    for i in range(3):
        for j in range(3):
            if grille[bloc_ligne + i][bloc_colonne + j] == nombre:
                print(0)
            else:
                print(grille[bloc_ligne + i][bloc_colonne + j])

    return True

def trouver_case_vide(grille):
    # Trouve la prochaine case vide dans la grille
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:
                return i, j
    return None, None  # Aucune case vide trouvée

def resoudre_sudoku(grille):
    ligne, colonne = trouver_case_vide(grille)
    if ligne is None:
        return True  # Toutes les cases sont remplies, le Sudoku est résolu

    # Essayer différentes valeurs pour la case vide
    for nombre in range(1, 10):
        if est_valide(grille, ligne, colonne, nombre):
            grille[ligne][colonne] = nombre
            if resoudre_sudoku(grille):
                return True
            grille[ligne][colonne] = 0  # Backtrack si la solution n'est pas valide

    return False  # Aucune valeur ne convient, la grille est invalide

def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(map(str, ligne)))

# Exemple de grille Sudoku à résoudre (0 représente une case vide)
grille = [
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

print("Grille Sudoku à résoudre :")
afficher_grille(grille)
print("\nSolution :")
if resoudre_sudoku(grille):
    afficher_grille(grille)
else:
    print("Aucune solution n'est possible.")
est_valide(grille,1,3,0)
