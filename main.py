import tkinter as tk

def read_bingo_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        bingo_values = [line.strip().split(',') for line in lines]
        # Remove quotation marks and strip whitespace
        bingo_values = [[val.replace('"', '').strip() for val in row] for row in bingo_values]
    return bingo_values

def create_bingo_board(window, values):
    global board_labels
    board_labels = [[None for _ in range(5)] for _ in range(5)]  # Initialize board labels

    for i in range(5):
        for j in range(5):
            text = values[i][j]
            if text == 'X':
                label = tk.Label(window, text=text, bg='yellow')  # Highlight the free space
            else:
                label = tk.Label(window, text=text, relief='ridge', width=10, height=5)
            label.grid(row=i, column=j)
            label.bind("<Button-1>", lambda event, r=i, c=j: on_cell_click(event, r, c))

            board_labels[i][j] = label  # Store the label widget

def on_cell_click(event, row, col):
    global marked_cells
    event.widget.config(bg='gray')  # Change color to indicate selection
    marked_cells[row][col] = True
    check_for_bingo()

marked_cells = [[False for _ in range(5)] for _ in range(5)]  # Initialize marked cells

def check_for_bingo():
    global board_labels
    bingo_count = 0
    # Check rows, columns and diagonals
    for i in range(5):
        if all(marked_cells[i]) or all([marked_cells[j][i] for j in range(5)]):
            bingo_count += 1

    # Check diagonals
    if all([marked_cells[i][i] for i in range(5)]) or all([marked_cells[i][4 - i] for i in range(5)]):
        bingo_count += 1

    # Update board based on bingo count
    if bingo_count > 0:
        update_bingo_board(bingo_count)

def update_bingo_board(bingo_count):
    msg = f"{['', 'Double ', 'Triple '][bingo_count - 1]}Bingo!"
    for row in board_labels:
        for label in row:
            label.config(text=msg, bg='lightblue')  # Apply a light blue color for simplicity

def main():
    # Main function to set up the GUI
    root = tk.Tk()
    root.title("Bingo Board")

    bingo_values = read_bingo_file("b_chart.txt")
    create_bingo_board(root, bingo_values)

    root.mainloop()

if __name__ == "__main__":
    main()
