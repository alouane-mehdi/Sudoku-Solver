import tkinter as tk
from Bruteforce import BruteForce

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        # Create Sudoku grid
        self.grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(master, textvariable=self.grid[i][j], width=2, font=('Arial', 16, 'bold'))
                entry.grid(row=i, column=j)
                entry.config(justify="center")

        # Button to solve Sudoku
        solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, columnspan=9)

    def solve_sudoku(self):
        solver = BruteForce("evilsudoku.txt")
        solver.test()
        solution = solver.grid
        for i in range(9):
            for j in range(9):
                self.grid[i][j].set(solution[i][j])

def main():
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
