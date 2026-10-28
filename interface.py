from tkinter import *
from A import astar    

root = Tk()
root.title("Tquin game")
root.geometry("400x580+500+100")
root.maxsize(400, 580)

state = [1, 2, 3,
         8, 0, 4,
         7, 6, 5]

labels = []    # the 9 labels of the board, in the same order as state


def afficher():
    """Redraw the board from the list state."""
    for i, value in enumerate(state):
        labels[i].config(text="" if value == 0 else str(value),
                         bg="#d9d9d9" if value == 0 else "#f5deb3")


def cliquer(i):
    """Called when the square number i is clicked."""
    vide = state.index(0)  
    if abs(i // 3 - vide // 3) + abs(i % 3 - vide % 3) == 1:
        state[vide], state[i] = state[i], state[vide]
        afficher()
        resultat.config(text="")           # clear the old result

def lancer_astar():
    """Called when the button 'Lancer A*' is clicked."""
    A = [state[0:3], state[3:6], state[6:9]]     # flat list to  3x3 matrix
    g, f = astar(A)                              # run the algorithm

  
    if g is None:
        texte = "No solution for this board!"
    elif g == 0:
        texte = "Already the goal (0 moves)."
    else:
        texte = f"Solved in {g} moves."
 
    resultat.config(text=texte)
    print(texte)

    state[:] = [1, 2, 3, 8, 0, 4, 7, 6, 5]     # reset the board
    afficher()


my_label = Label(master=root,
                 text="Welcome to the Tquin game!",
                 font=("Arial", 20))
my_label.pack(pady=(15, 10))

my_button = Button(master=root,
                   text="Lancer A*",
                   bd=5,
                   activeforeground="red",
                   cursor="dot",
                   width=13,
                   height=2,
                   font=("Arial", 14),
                   command=lancer_astar)

# big square
board = Frame(master=root, width=300, height=300, bd=4, relief="ridge")
board.pack()
board.pack_propagate(False)

# creating the 3x3 grid of squares
for i in range(9):
    cell = Frame(board, width=96, height=96)
    cell.grid(row=i // 3, column=i % 3)
    cell.pack_propagate(False)

    lbl = Label(cell,
                font=("Consolas", 28, "bold"),
                bd=3,
                relief="raised",
                cursor="hand2")
    lbl.pack(fill="both", expand=True)
    lbl.bind("<Button-1>", lambda event, i=i: cliquer(i))
    labels.append(lbl)

afficher()

my_button.pack(pady=(20, 10))

resultat = Label(master=root, text="", font=("Arial", 14))  
resultat.pack()

root.mainloop()