import tkinter as tk
from tkinter import messagebox
from Bruteforce import Bruteforce
from Backtracking import Backtracking

class SudokuSolverGUI:
    def __init__(self, master, file_path_bruteforce,file_path_backtracking):
        self.master = master
        self.master.title("Sudoku Solver")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.file_path_bruteforce = file_path_bruteforce
        self.file_path_backtracking = file_path_backtracking

        self.method_var = tk.StringVar()
        self.method_var.set("Brute Force")

        self.label = tk.Label(self.frame, text="Select Sudoku Solver Method:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.method_menu = tk.OptionMenu(self.frame, self.method_var, "Brute Force", "Backtracking")
        self.method_menu.grid(row=0, column=1, padx=5, pady=5)

        self.solve_button = tk.Button(self.frame, text="Solve Sudoku", command=self.solve)
        self.solve_button.grid(row=1, columnspan=2, padx=5, pady=5)

        self.canvas = tk.Canvas(self.master, width=360, height=360)
        self.canvas.pack()

        self.bruteforce = False
        self.backtracking = False


    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(10):
            line_width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(40 * i, 0, 40 * i, 360, width=line_width)
            self.canvas.create_line(0, 40 * i, 360, 40 * i, width=line_width)

    def draw_numbers(self, grid):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                if grid[i][j] != '_':
                    self.canvas.create_text(20 + 40 * j, 20 + 40 * i, text=grid[i][j], font=("Arial", 20), tags="numbers")

    def solve(self):
        if not self.file_path_bruteforce:
            messagebox.showerror("Error", "Sudoku file path not specified.")
            return
        
        if self.method_var.get() == "Brute Force":
            self.bruteforce = True
            
            self.backtracking = False
            
        elif self.method_var.get() == "Backtracking":
            self.backtracking = True
            self.bruteforce = False
            
        else:
            messagebox.showerror("Error", "Invalid solver method selected.")
            return
        
        if self.bruteforce:
            solver = Bruteforce(self.file_path_bruteforce)
        elif self.backtracking:
            solver = Backtracking(self.file_path_backtracking)
        
        
        solver.solve_sudoku()

        self.draw_grid()
        self.draw_numbers(solver.grid)

        messagebox.showinfo("Sudoku Solved", "Sudoku solved successfully.")

def main():
    root = tk.Tk()
    file_path_bruteforce = "testsudoku.txt"  # Spécifiez le chemin du fichier ici
    file_path_backtracking = "sudoku2.txt"
    app = SudokuSolverGUI(root, file_path_bruteforce , file_path_backtracking)
    root.mainloop()

if __name__ == "__main__":
    main()


