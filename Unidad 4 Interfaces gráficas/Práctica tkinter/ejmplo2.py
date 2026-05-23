import tkinter as tk
from tkinter import messagebox

class SimonGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PySimon-Game')
        self.resizable(False, False)

        self.__score = 0

        self.create_menu()
        self.create_widgets()
    
    def create_menu(self):
        # Crear el menú
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Crear el submenú
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Ver puntajes", command=self.ver_puntajes)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)

    def create_widgets(self):
        # Crear los botones de colores
        self.boton1 = tk.Button(self, bg="#008080", relief='raised')  # Verde
        self.boton2 = tk.Button(self, bg="#FF0000", relief='raised')  # Rojo
        self.boton3 = tk.Button(self, bg="#FFFF00", relief='raised')  # Amarillo
        self.boton4 = tk.Button(self, bg="#0000FF", relief='raised')  # Azul

        self.boton1.grid(row=1, column=0, padx=5, pady=5, ipadx=50, ipady=80)
        self.boton2.grid(row=1, column=1, padx=5, pady=5, ipadx=50, ipady=80)
        self.boton3.grid(row=2, column=0, padx=5, pady=5, ipadx=50, ipady=80)
        self.boton4.grid(row=2, column=1, padx=5, pady=5, ipadx=50, ipady=80)

        # Crear etiqueta de puntaje
        self.puntaje_label = tk.Label(self, text="Puntaje")
        self.puntaje_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.puntaje_value = tk.Label(self, text=self.__score)
        self.puntaje_value.grid(row=0, column=2, columnspan=2, pady=5)

    def ver_puntajes(self):
        # Aquí puedes mostrar una ventana o un mensaje con los puntajes
        messagebox.showinfo("Puntajes", f"El puntaje actual es: {self.__score}")

    def get_puntaje(self):
        return self.__score

    def set_puntaje(self, score):
        self.__score = score
        self.puntaje_value.config(text=self.__score)

if __name__ == '__main__':
    app = SimonGame()
    app.mainloop()
