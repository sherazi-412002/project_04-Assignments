import tkinter as tk

# Constants
CANVAS_SIZE = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="white")
        self.canvas.pack()

        self.cells = {}  
        self.create_grid()

        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")

        # Bind mouse event
        self.canvas.bind("<B1-Motion>", self.move_eraser)

        # Reset button
        tk.Button(root, text="Reset", command=self.create_grid).pack(pady=5)

    def create_grid(self):
        """Create a grid of blue cells."""
        self.canvas.delete("all")  # Clear the canvas
        self.cells = {}  # Reset grid data
        for row in range(0, CANVAS_SIZE, CELL_SIZE):
            for col in range(0, CANVAS_SIZE, CELL_SIZE):
                self.cells[(col, row)] = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")  # Recreate eraser

    def move_eraser(self, event):
        """Move eraser and erase cells."""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        """Erase overlapping cells by changing color to white."""
        for (col, row), cell in self.cells.items():
            if col < x + ERASER_SIZE and col + CELL_SIZE > x and row < y + ERASER_SIZE and row + CELL_SIZE > y:
                self.canvas.itemconfig(cell, fill="white")

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    EraserApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

        