Deux méthodes ont été utilisées pour ce sudoku solver : Le Backtracking et la Force Brute . 
La méthode la plus efficace est le backtracking car il utilise la récursivité pour explorer toutes les combinaisons qui sont possibles et qui ne violent pas le réglement , 
si la combinaison viole le reglement , elle retourne en arriere et teste avec une nouvelle combinaison possible.
Pour le force brute c'est un peu différent mais ça prends une éternité . La méthode rempli toutes les cases manquantes avec un chiffre aléatoire pour chaque case puis 
vérifie si la grille complète ne viole aucune regle du jeu . Si elle n'en viole pas , le script prend fin mais mais si elle en viole , de nouveaux chiffres aléatoire sont
testés jusqu'a que le sudoku soit compléter. 
Donc la Force Brute n'est pas la plus efficace (sauf si vous aimez attendre ) et le Backtracking est la plus optimal.

| Force Brute|                                                                                Backtracking
|------------                                                                                 |------------|
|Plus facile à comprendre et implémenter                                                      |Plus complexe à comprendre et implémenter            
|Explore toutes les possibilités, assure donc de trouve un résulat                            |Plus rapide          
|Mais presque inefficace pour les problèmes avec beaucoup de combinaison possibles            |Efficace sur les sudoku à plusieurs cases manquantes 
|Utilise moins d'espace mémoire,pas besoin de stocker les configurations précédentes          |Utilise plus d'espace mémoire car doit stocker les combinaisons précédentes          
Calculs de complexité:

- Complexité temporelle :  Il s'agit de mesurer le temps nécessaire à l'exécution de l'algorithme en fonction de la taille de l'entrée(notée grand 0)
- Complexité spatiale ; Il s'agit de mesurer la consomation de mémoire de l'algorithme toujours en fonction de la taille de l'entrée (notée grand 0)

  Pour la force brute, la complexité temporelle est exponentielle et varie en fonction du nombre de cases vides (soit souvent longue et imprévisible). La complexité spatiale est relativement faible puisque l'algorithme ne stocke pas une grande quantité d'information en mémoire, mais principalement la grille de sudoku et la méthode vérifGrid.

  Pour le BackTracking, la complexité temporelle est souvent plus courte que le bruteforce mais peut s'allonger si l'algorithme emprunte de nombreuse fois les mauvais chemin. La complexité spatiale est cependant plus importante puisque l'algorithme doit stocker les chemins empruntés.
