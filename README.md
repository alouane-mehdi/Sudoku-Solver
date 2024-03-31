Deux méthodes ont été utilisées pour ce sudoku solver : Le Backtracking et la Force Brute . 
La méthode la plus efficace est le backtracking car il utilise la récursivité pour explorer toutes les combinaisons qui sont possibles et qui ne violent pas le réglement , 
si la combinaison viole le reglement , elle retourne en arriere et teste avec une nouvelle combinaison possible.
Pour le force brute c'est un peu différent mais ça prends une éternité . La méthode rempli toutes les cases manquantes avec un chiffre aléatoire pour chaque case puis 
vérifie si la grille complète ne viole aucune regle du jeu . Si elle n'en viole pas , le script prend fin mais mais si elle en viole , de nouveaux chiffres aléatoire sont
testés jusqu'a que le sudoku soit compléter. (pour 5 cases manquante ça prends aproximativement 50secondes mais pour 6 cases manquante ça en prends 6 minutes et 10 secondes) 
Donc la Force Brute n'est pas la plus efficace (sauf si vous aimez attendre ) et le Backtracking est la plus optimal.

| Force Brute|                                                                                Backtracking
|------------                                                                                 |------------|
|Plus facile à comprendre et implémenter                                                      |Plus complexe à comprendre et implémenter            
|Explore toutes les possibilités, assure donc de trouve un résulat                            |Pas de garantit de trouver une solution            
|Mais presque inefficace pour les problèmes avec beaucoup de combinaison possibles            |Efficace sur les problèmes de taille raisonable            
|Utilise moins d'espace mémoire,pas besoin de stocker les configurations précédentes          |Utilise plus d'espace mémoire car doit stocker les combinaisons précédentes          
