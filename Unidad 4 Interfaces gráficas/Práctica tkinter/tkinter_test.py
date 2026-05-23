import tkinter as tk

ventana=tk.Tk()

ventana.geometry("400x500")

etiqueta = tk.Label(ventana, text= "Esta es una prueba")
etiqueta.pack(side = tk.BOTTOM)

def saludo(n):
    print("HOLA "+ n)

botonROJO = tk.Button(ventana, padx = 40, pady =50, command = lambda: saludo("caca"))
botonROJO.pack(side = tk.BOTTOM)

cajaTexto = tk.Entry(ventana, font = "Arial 72")
cajaTexto.pack()

def func():
    texto= cajaTexto.get()
    print(texto)

boton1 = tk.Button(ventana, text = "click", command = func)
boton1.pack()

ventana.mainloop()