Deux methodes ont été utilisées pour ce sudoku solver : Le backtracking et la force brute . 
La meilleure est le backtracking car il utilise la récursivité pour explorer toutes les combinaisons qui sont possibles et qui ne violent pas le reglement , 
si la combinaison viole le reglement , elle retourne en arriere et teste avec une nouvelle combinaison possible.
Pour le force brute c'est un peu différent mais ça prends une éternité . La méthode rempli toutes les cases manquantes avec un chiffre aléatoire pour chaque case puis 
vérifie si la grille complète ne viole aucune regle du jeu . Si elle n'en viole pas , le scriot prend fin mais mais si elle en viole , de nouveaux chiffres aléatoire sont
testés jusqu'a que le sudoku soit bon. (pour 5 cases manquante ça prends aproximativement 50secondes mais pour 6 cases manquante ça en prends 6 minutes et 10 secondes) 
Donc la Brute force n'est pas la fonctionnel (sauf si vous aimez attendre ) et le backtracking est la meilleure methode.
