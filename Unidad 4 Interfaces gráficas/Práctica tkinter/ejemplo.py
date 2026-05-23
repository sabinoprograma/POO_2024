import tkinter as tk
from tkinter import messagebox
import random

class SimonGame(tk.Tk):
    __score: int

    def __init__(self):
        super().__init__()
        self.title('PySimon-Game')
        self.resizable(False, False)

        # Initialize score
        self.__score = 0

        # Define canvas buttons
        self.canvas1 = self.create_canvas("#0000FF")
        self.canvas2 = self.create_canvas("#FFA500")
        self.canvas3 = self.create_canvas("#FF0000")
        self.canvas4 = self.create_canvas("#008000")

        # Define labels
        self.label_score_text = tk.Label(self, text="Puntaje")
        self.label_score = tk.Label(self, text=str(self.__score))

        # Layout options
        opts = {'padx': 5, 'pady': 5, 'ipadx': 50, 'ipady': 80, 'rowspan': 4, 'columnspan': 2}

        # Position widgets
        self.label_score_text.grid(row=0, column=1, ipadx=5, ipady=5)
        self.label_score.grid(row=0, column=3, ipadx=5, ipady=5)
        self.canvas1.grid(row=1, column=0, **opts)
        self.canvas2.grid(row=5, column=0, **opts)
        self.canvas3.grid(row=1, column=2, **opts)
        self.canvas4.grid(row=5, column=2, **opts)

        # Game state
        self.sequence = []
        self.user_sequence = []

        # Start the game
        self.next_round()

    def create_canvas(self, color):
        canvas = tk.Canvas(self, width=100, height=100, bg=color, highlightthickness=5)
        canvas.bind("<Button-1>", lambda event, clr=color: self.user_click(clr))
        return canvas

    def get_score(self):
        return self.__score

    def set_score(self, value):
        self.__score = value
        self.label_score.config(text=str(self.__score))

    def next_round(self):
        self.user_sequence = []
        self.sequence.append(random.choice([self.canvas1, self.canvas2, self.canvas3, self.canvas4]))
        self.play_sequence()

    def play_sequence(self):
        for i, canvas in enumerate(self.sequence):
            self.after(i * 600, lambda c=canvas: self.highlight_canvas(c))

    def highlight_canvas(self, canvas):
        original_color = canvas.cget("bg")
        canvas.config(bg="white")
        self.after(400, lambda: canvas.config(bg=original_color))

    def user_click(self, color):
        for canvas in [self.canvas1, self.canvas2, self.canvas3, self.canvas4]: #Canvas en esta lista
            if canvas.cget("bg") == color:
                self.user_sequence.append(canvas)
                self.highlight_canvas(canvas)
                break

        if self.user_sequence == self.sequence[:len(self.user_sequence)]:
            if len(self.user_sequence) == len(self.sequence):
                self.set_score(self.get_score() + 1)
                self.after(1000, self.next_round)
        else:
            messagebox.showinfo("PySimon-Game", "Secuencia incorrecta. ¡Juego terminado!")
            self.reset_game()

    def reset_game(self):
        self.sequence = []
        self.user_sequence = []
        self.set_score(0)
        self.next_round()

if __name__ == '__main__':
    app = SimonGame()
    app.mainloop()
