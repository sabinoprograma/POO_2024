# SIMON GAME codificado por Sabino Pignatari
from tkinter import *
from tkinter import ttk, font
from datetime import datetime
from pathlib import Path
from ObjectEncoder import ObjectEncoder
from claseJugador import Jugador
from GestorJugadores import GestorJugadores
import json
import random

class Aplicacion():
    #cereo todas las variables necesarias
    __ventana = None
    __puntuacion = None
    __secuencia = None
    __indice = None
    __esperando = None
    __dialogo1 = None
    __dialogo2 = None
    __dialogo3 = None
    __usuario = None
    __gestor = None
    __encoder = None
    __dificultad = None
    __gameOver = None
    __nivelSeleccionado = None
    __timerGeneral = None
    __tiempoMaximo = None
    __tiempoInicio = None
    __tiempoRestante = None

    def __init__(self):
        #config de la ventana principal
        self.__ventana = Tk()
        self.__ventana.title("PySimon-Game")
        self.__ventana.geometry("350x500+500+50")
        self.__ventana.resizable(0, 0)

        #variables para la puntuacion y el usuario
        self.__puntuacion = IntVar()
        self.__puntuacion.set(0)
        self.__usuario = StringVar()
        self.__usuario.set("")

        #variable para la dificultad del juego
        self.__dificultad = IntVar()

        #inicializa el gestor de jugadores y el encoder
        self.__gestor = GestorJugadores()
        self.__encoder = ObjectEncoder("pysimonpuntajes.json")

        #otras variables del juego
        self.__secuencia = []
        self.__indice = 0
        self.__esperando = False
        self.__gameOver = False

        #cargar datos desde el archivo json
        self.cargarDatos()

        #configurar el menu del juego
        self.menu()

        self.__tiempoMaximo = 5900    #tiempo maximo en milisegundos 
        self.__tiempoRestante = StringVar()      #variable para mostrar el tiempo restante

        #configuracion de los botones del juego usando metodo canvas
        self.boton1 = Canvas(self.__ventana, width=140, height=200, bg="#2E8B57", borderwidth=2, relief="raised")
        self.boton1.grid(row=1, column=0, padx=15, pady=0)
        self.boton1.bind("<Button-1>", self.presionarBoton)
        self.boton2 = Canvas(self.__ventana, width=140, height=200, bg="#CCCC00", borderwidth=2, relief="raised")
        self.boton2.grid(row=2, column=0, padx=15, pady=10)
        self.boton2.bind("<Button-1>", self.presionarBoton)
        self.boton3 = Canvas(self.__ventana, width=140, height=200, bg="#660000", borderwidth=2, relief="raised")
        self.boton3.grid(row=1, column=1, padx=0, pady=0)
        self.boton3.bind("<Button-1>", self.presionarBoton)
        self.boton4 = Canvas(self.__ventana, width=140, height=200, bg="#0000FF", borderwidth=2, relief="raised")
        self.boton4.grid(row=2, column=1, padx=0, pady=10)
        self.boton4.bind("<Button-1>", self.presionarBoton)
        self.botones = [self.boton1, self.boton2, self.boton3, self.boton4] #lista con los botones

        #inicializar el juego
        self.iniciar()
        
        #configuracion para mostrar el usuario y la puntuacion
        self.frame2=ttk.Frame(self.__ventana, borderwidth=2)
        self.frame2.grid(row=0, column=0, columnspan=2)
        self.usuarioLbl = ttk.Label(self.frame2, text=self.__usuario.get(), padding=(30, 0))
        self.usuarioLbl.grid(column=0, row=0)
        self.puntuacionLbl = ttk.Label(self.frame2, text=self.__puntuacion.get(), padding=(70, 0))
        self.puntuacionLbl.grid(column=1, row=0)

        #configuracion del selector de nivel de dificultad utilizando una lista desplegable combobox
        self.niveles = ["Principiante", "Experto", "Super Experto"]
        self.__nivelSeleccionado = StringVar()
        self.__nivelSeleccionado.set("Principiante")
        self.seleccioneLbl = ttk.Label(self.frame2, text="Seleccione Nivel", padding=(50,0))
        self.seleccioneLbl.grid(row=1, column=0)
        self.selectorNivel = ttk.Combobox(self.frame2, textvariable=self.__nivelSeleccionado, values=self.niveles)
        self.selectorNivel.grid(row=1, column=1, pady=10)
        self.selectorNivel.bind("<<ComboboxSelected>>", self.seleccionar_nivel)

        #configuracion de la etiqueta para mostrar el tiempo restante
        self.labelTiempo = ttk.Label(self.frame2, textvariable=self.__tiempoRestante, font=('Arial', 14, 'bold'))
        self.__dificultad.set(1)  #seteo la dificultad inicial en principiante
        self.__ventana.after(1000, self.botonAleatorio)
        self.__ventana.mainloop()

    #configuracion del menu de la ventana
    def menu(self):
        barraMenu = Menu(self.__ventana)
        menuPuntaje = Menu(barraMenu, tearoff=0)
        menuPuntaje.add_command(label="Ver Puntajes", command=self.verPuntajes)
        menuPuntaje.add_command(label="Salir", command=self.__ventana.destroy)
        barraMenu.add_cascade(label="Puntajes", menu=menuPuntaje)
        self.__ventana.config(menu=barraMenu)

    #configuracion de la ventana de dialogo para ingresar los datos del jugador
    def iniciar(self):
        self.__dialogo2 = Toplevel()
        self.__dialogo2.geometry("200x100+570+240")
        self.__dialogo2.resizable(0, 0)
        self.__dialogo2.title("PyInterface")
        self.datosLbl = ttk.Label(self.__dialogo2, text="Datos del Jugador", padding=(0, 0))
        self.datosLbl.grid(row=0, column=0)
        self.frame = ttk.Frame(self.__dialogo2, borderwidth=2, padding=(0, 0))
        self.frame.grid(row=1, column=0)
        self.jugadorLbl = ttk.Label(self.frame, text="Jugador", padding=(5, 10))
        self.jugadorLbl.grid(row=1, column=0)
        self.entry = ttk.Entry(self.frame, textvariable=self.__usuario, width=20)
        self.entry.grid(row=1, column=1)
        self.botonIniciar = ttk.Button(self.__dialogo2, text="Iniciar Juego", command=self.cerrarDialogo)
        self.botonIniciar.grid(row=2, column=0)
        self.__dialogo2.transient(master=self.__ventana)
        self.__dialogo2.grab_set()
        self.__ventana.wait_window(self.__dialogo2)

    #metodo para seleccionar el nivel de dificultad
    def seleccionar_nivel(self, event):
        nivel = self.__nivelSeleccionado.get()
        
        if nivel == "Principiante":
            self.__dificultad.set(1)
            self.ocultarTimer()
            self.__secuencia = []
            self.__puntuacion.set(0)
            self.puntuacionLbl.config(text=self.__puntuacion.get())
            self.__indice = 0
            self.__esperando = False
            self.__ventana.after(1000, self.botonAleatorio)
            
        elif nivel == "Experto":
            self.__dificultad.set(2)
            self.__secuencia = []
            self.__puntuacion.set(0)
            self.puntuacionLbl.config(text=self.__puntuacion.get())
            self.__indice = 0
            self.__esperando = False
            self.mostrarTimer()
            self.iniciarJuego()
            
        elif nivel == "Super Experto":
            self.__dificultad.set(3)
            self.__secuencia = []
            self.__puntuacion.set(0)
            self.puntuacionLbl.config(text=self.__puntuacion.get())
            self.__indice = 0
            self.__esperando = False
            self.mostrarTimer()
            self.iniciarJuego()

    #muestra el temporizador en la interfaz
    def mostrarTimer(self):
        self.labelTiempo.grid(row=1, column=0, columnspan=2)

    #funcion para iniciar el juego
    def iniciarJuego(self):
        self.reiniciarTimerGeneral()
        self.__ventana.after(1000, self.botonAleatorio)
    
    #funcion para reiniciar el timer general
    def reiniciarTimerGeneral(self):
        #cancelar el timer anterior si existe
        if self.__timerGeneral:
            self.__ventana.after_cancel(self.__timerGeneral)
        #configurar el nuevo timer general
        if self.labelTiempo.winfo_ismapped():
            self.__tiempoInicio = datetime.now()
            self.actualizarTiempoRestante()
            self.__timerGeneral = self.__ventana.after(self.__tiempoMaximo, self.mostrarError)
    
    #actualiza el temporizador general en la interfaz
    def actualizarTiempoRestante(self):
        tiempo_transcurrido = datetime.now() - self.__tiempoInicio
        tiempo_restante = max(0, self.__tiempoMaximo - int(tiempo_transcurrido.total_seconds() * 1000))
        segundos_restantes = tiempo_restante // 1000
        self.__tiempoRestante.set(f"{segundos_restantes}")
        #programar la actualizacion del tiempo restante cada 100 milisegundos
        self.__ventana.after(100, self.actualizarTiempoRestante)

    #oculta el temporizador en la interfaz
    def ocultarTimer(self):
        if self.__timerGeneral:
            if self.labelTiempo.winfo_ismapped():
                self.labelTiempo.grid_forget()
                self.__ventana.after_cancel(self.__timerGeneral)

    #cierra el dialogo
    def cerrarDialogo(self):
        self.__dialogo2.destroy()
        
    '''
    def presionarBoton(self, event):
        if not self.__esperando:
            return
        if self.__gameOver:
            return
        canvas = event.widget
        dificultad = self.__dificultad.get()
        if dificultad == 1:
            self.resaltarBoton(canvas, 450)
        elif dificultad == 2:
            self.resaltarBoton(canvas,350)
            self.reiniciarTimerGeneral()
        elif dificultad == 3:
            self.resaltarBoton(canvas, 250)
        if canvas == self.__secuencia[self.__indice]:
            self.__indice += 1
            if self.__indice == len(self.__secuencia):
                self.__puntuacion.set(self.__puntuacion.get() + 1)
                self.puntuacionLbl.config(text=self.__puntuacion.get())
                self.__ventana.after(1000, self.botonAleatorio)
                self.__esperando = False
        else:
            self.mostrarError()
    '''
    
    #maneja el evento de presionar un boton del juego
    def presionarBoton(self, event):
        if not self.__esperando: #verifica si el juego esta esperando la entrada del usuario
            return
        if self.__gameOver: #verifica si el juego ha terminado
            return
        canvas = event.widget #identifica el boton presionado por el jugador
        dificultad = self.__dificultad.get()
        if dificultad == 1: #resalta el boton dependiendo del nivel de dificultad
            self.resaltarBoton(canvas, 450)
        elif dificultad == 2: 
            self.resaltarBoton(canvas, 350)
            self.reiniciarTimerGeneral()
        elif dificultad == 3:
            self.resaltarBoton(canvas, 250)
        if canvas == self.__secuencia[self.__indice]: #compara el boton presionado con el boton correspondiente en la secuencia
            self.__indice += 1 #si es correcto se incrementa el indice
            if self.__indice == len(self.__secuencia): #si se ha completado toda la secuencia
                self.__puntuacion.set(self.__puntuacion.get() + 1) #incrementa la puntuacion y actualiza la etiqueta de puntuacion
                self.puntuacionLbl.config(text=self.__puntuacion.get())
                self.__ventana.after(1000, self.botonAleatorio) #agrega un nuevo boton a la secuencia despues de un segundo
                self.__esperando = False #establece esperando a False
        else:
            self.mostrarError() #si el boton presionado no coincide con el boton en la secuencia, muestra error y termina el juego


    #resalta un boton
    def resaltarBoton(self, boton, delay):
        if boton.cget("relief") == "raised":
            boton.config(relief="sunken")
        if boton.cget("bg") == "#2E8B57":
            boton.config(bg="#3CB371")
            self.__ventana.after(delay, lambda: (boton.config(relief="raised"), boton.config(bg="#2E8B57")))
            if self.__dificultad.get()==2 or self.__dificultad.get()==3:
                self.reiniciarTimerGeneral()
        elif boton.cget("bg") == "#CCCC00":
            boton.config(bg="#FFFFCC")
            self.__ventana.after(delay, lambda: (boton.config(relief="raised"), boton.config(bg="#CCCC00")))
            if self.__dificultad.get()==2 or self.__dificultad.get()==3:
                self.reiniciarTimerGeneral()
        elif boton.cget("bg") == "#660000":
            boton.config(bg="#CD5C5C")
            self.__ventana.after(delay, lambda: (boton.config(relief="raised"), boton.config(bg="#660000")))
            if self.__dificultad.get()==2 or self.__dificultad.get()==3:
                self.reiniciarTimerGeneral()
        elif boton.cget("bg") == "#0000FF":
            boton.config(bg="#4169E1")
            self.__ventana.after(delay, lambda: (boton.config(relief="raised"), boton.config(bg="#0000FF")))
            if self.__dificultad.get()==2 or self.__dificultad.get()==3:
                self.reiniciarTimerGeneral()

    #selecciona un boton aleatorio y lo ilumina
    def botonAleatorio(self):
        boton = random.choice(self.botones)
        self.__secuencia.append(boton)
        if self.__dificultad.get() == 3:
            self.__secuencia.append(random.choice(self.botones))
        self.__indice = 0
        self.__esperando = False
        dificultad = self.__dificultad.get()
        if dificultad == 1:
            self.mostrarSecuencia(800, 450)
        elif dificultad == 2:
            self.mostrarSecuencia(600, 350)
        elif dificultad == 3:
            self.mostrarSecuencia(400, 250)

    def mostrarSecuencia(self, delay1, delay2):
        for i in range(len(self.__secuencia)):
            boton = self.__secuencia[i]
            self.__ventana.after(i * delay1, lambda b=boton: self.resaltarBoton(b, delay2))
        self.__ventana.after(len(self.__secuencia) * delay1, self.esperarRespuesta)

    def esperarRespuesta(self):
        self.__esperando = True

    #maaneja el fin del juego, muestra un mensaje y guarda el puntaje
    def mostrarError(self):
        if self.__gameOver:
            return
        self.__gameOver = True
        self.__dialogo1 = Toplevel()
        self.__dialogo1.geometry("250x150+550+200")
        self.__dialogo1.title("GAME OVER")
        self.__dialogo1.resizable(0, 0)
        fuente = font.Font(weight='bold')
        self.gameOverLbl = ttk.Label(self.__dialogo1, text="GAME OVER", font=fuente, padding=(75, 15))
        self.gameOverLbl.grid(row=0, column=0)
        self.puntajeLbl1 = ttk.Label(self.__dialogo1, text="PUNTUACION", font=fuente)
        self.puntajeLbl1.grid(row=1, column=0)
        self.puntajeLbl = ttk.Label(self.__dialogo1, text=self.__puntuacion.get(), padding=(10, 10))
        self.puntajeLbl.grid(row=2, column=0)
        self.botonSalir = ttk.Button(self.__dialogo1, text="Salir", command=self.__dialogo1.destroy)
        self.botonSalir.grid(row=3, column=0)

        self.__dialogo1.transient(master=self.__ventana)
        self.__dialogo1.grab_set()
        self.__ventana.wait_window(self.__dialogo1)

        self.guardarDatosJugador()
        self.__ventana.destroy()

    #carga los datos de puntajes desde un archivo json
    def cargarDatos(self):
        try:
            d = self.__encoder.leerJSONArchivo()
            self.__gestor = self.__encoder.decodificarDiccionario(d)
        except (FileNotFoundError, json.JSONDecodeError):
            self.__gestor = GestorJugadores()

    #guarda una instancia de jugador
    def guardarDatosJugador(self):
        dificultad=''
        if self.__dificultad.get()==1:
            dificultad='Principiante'
        elif self.__dificultad.get()==2:
            dificultad='Experto'
        elif self.__dificultad.get()==3:
            dificultad='Super Experto'
        unJugador = Jugador(self.__usuario.get(), datetime.now().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M:%S"), self.__puntuacion.get(), dificultad)
        self.__gestor.agregarJugador(unJugador)
        self.guardarDatos()

    #guarda los datos de puntajes en un archivo json
    def guardarDatos(self):
        d = self.__gestor.toJSON()
        self.__encoder.guardarJSONArchivo(d)

    #abre una nueva ventana para mostrar los puntajes
    def verPuntajes(self):
        d = self.__encoder.leerJSONArchivo()
        self.__gestor = self.__encoder.decodificarDiccionario(d)
        self.__gestor.ordenar()    
        self.__dialogo3 = Toplevel()
        self.__dialogo3.geometry("540x200+400+50")
        self.__dialogo3.resizable(0, 0)
        self.__dialogo3.title("Galeria de Puntajes")
        self.frame1 = ttk.Frame(self.__dialogo3, borderwidth=2, relief="groove")
        self.frame1.grid(row=0, column=0)
        self.labelJ = ttk.Label(self.frame1, text="Jugador", padding=(25, 5))
        self.labelF = ttk.Label(self.frame1, text="Fecha", padding=(40, 5))
        self.labelH = ttk.Label(self.frame1, text="Hora", padding=(20, 5))
        self.labelP = ttk.Label(self.frame1, text="Puntaje", padding=(40, 5))
        self.labelD = ttk.Label(self.frame1, text="Dificultad", padding=(40, 5))
        self.labelJ.grid(row=0, column=0)
        self.labelF.grid(row=0, column=1)
        self.labelH.grid(row=0, column=2)
        self.labelP.grid(row=0, column=3)
        self.labelD.grid(row=0, column=4)
        self.frame = ttk.Frame(self.__dialogo3, borderwidth=2)
        self.frame.grid(row=1, column=0)
        self.i = 0
        for jugador in self.__gestor:
            self.jugadorLbl = ttk.Label(self.frame, text=jugador.getJugador(), padding=(40, 0))
            self.fechaLbl = ttk.Label(self.frame, text=jugador.getFecha(), padding=(20, 0))
            self.horaLbl = ttk.Label(self.frame, text=jugador.getHora(), padding=(20, 0))
            self.puntLbl = ttk.Label(self.frame, text=jugador.getPuntaje(), padding=(40, 0))
            self.dificultadLbl = ttk.Label(self.frame, text=jugador.getDificultad(), padding=(40,0))
            self.jugadorLbl.grid(row=self.i, column=0)
            self.fechaLbl.grid(row=self.i, column=1)
            self.horaLbl.grid(row=self.i, column=2)
            self.puntLbl.grid(row=self.i, column=3)
            self.dificultadLbl.grid(row=self.i, column=4)
            self.i += 1
        self.botonCerrar = ttk.Button(self.__dialogo3, text="Cerrar", command=self.__dialogo3.destroy)
        self.botonCerrar.grid(row=2, column=0, pady=20)
        self.__dialogo3.transient(master=self.__ventana)
        self.__dialogo3.grab_set()
        self.__ventana.wait_window(self.__dialogo3)

def testApp():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    testApp()