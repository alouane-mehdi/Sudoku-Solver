import pygame
import random
import time

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Police de caractères
FONT = pygame.font.SysFont(None, 40)

# Temps de départ
start_time = time.time()

class Bruteforce():
    def __init__(self, file_path):
        with open(file_path, "r") as my_file:
            content = my_file.readlines()

        self.grid = [list(line.strip()) for line in content]
        self.gridClone = [row.copy() for row in self.grid]

    def verifGrid(self):
        # Vérification des lignes
        for row in self.grid:
            if not len(set(row)) == 9:
                return False
        
        # Vérification des colonnes
        for i in range(9):
            column = [self.grid[j][i] for j in range(9)]
            if not len(set(column)) == 9:
                return False
        
        # Vérification des zones 3x3
        for y0 in [0, 3, 6]:
            for x0 in [0, 3, 6]:
                subgrid = []
                for i in range(3):
                    for j in range(3):
                        if self.grid[y0+i][x0+j] in subgrid:
                            return False
                        subgrid.append(self.grid[y0+i][x0+j])

        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '_':
                    return False

        return True
    
    def return_empty_spots(self):
        empty_spots = []
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '_':
                    empty_spots.append((i, j))
        return empty_spots
    
    def generate_random_number(self):
        list_numbers = []
        len_empty_spots = len(self.return_empty_spots())
        for i in range(len_empty_spots):
            nbr_possibilites = random.randint(1, 9)
            list_numbers.append(nbr_possibilites)
        return list_numbers
    
    def solve_sudoku(self):
        # Boucle principale de résolution du sudoku
        while not self.verifGrid():
            self.grid = [row.copy() for row in self.gridClone]  # Réinitialisation de la grille
            random_numbers = self.generate_random_number()      # Génération de nombres aléatoires
            empty_spots = self.return_empty_spots()             # Obtention des emplacements vides
            for index, spot in enumerate(empty_spots):
                self.grid[spot[0]][spot[1]] = str(random_numbers[index])  # Remplissage des emplacements vides

            # Affichage de la grille
            self.draw_grid()

            # Pause pour visualiser chaque itération (facultatif)
            pygame.time.delay(500)
            pygame.display.update()

    def draw_grid(self):
        screen.fill(WHITE)
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(screen, BLACK, (60 * i, 0), (60 * i, 540), 4)
                pygame.draw.line(screen, BLACK, (0, 60 * i), (540, 60 * i), 4)
            else:
                pygame.draw.line(screen, BLACK, (60 * i, 0), (60 * i, 540), 2)
                pygame.draw.line(screen, BLACK, (0, 60 * i), (540, 60 * i), 2)

        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != '_':
                    text = FONT.render(self.grid[i][j], True, BLACK)
                    screen.blit(text, (j * 60 + 20, i * 60 + 20))


# Création de la fenêtre Pygame
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Résolveur de Sudoku")

# Initialisation de la grille
test = Bruteforce("evilsudoku.txt")
test.solve_sudoku()

# Calcul du temps d'exécution
end_time = time.time()
execution_time = end_time - start_time
print("Durée d'exécution:", execution_time, "secondes")

# Boucle principale Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
