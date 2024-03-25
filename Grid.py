class Grid:
    def __init__(self) -> None:
        pass

    def grid():
        with open("evilsudoku.txt", "r") as f:
            row = f.readlines()
        with open("evilsudoku.txt") as my_file:
            liste = my_file.read()

            liste1 = []
            for i in liste:
                if i != '\n':
                    liste1.append(i)

            grid = []
            for i in range(0, 9):
                grid.append(liste1[0:9])
                del liste1[0:9]

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '_':
                        grid[i][j] = '0'
        return grid
