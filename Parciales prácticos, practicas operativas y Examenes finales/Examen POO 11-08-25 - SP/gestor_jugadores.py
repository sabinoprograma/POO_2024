from nodo import Nodo
from jugadores_individuales import jugadores_individuales
from jugadores_equipo import jugadores_equipo
import csv

class lista:
    __actual: Nodo | None
    __comienzo: Nodo | None
    __indice: int
    __tope: int

    def __init__(self):
        self.__actual= None
        self.__comienzo= None
        self.__indice = 0
        self.__tope= 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == 0:
            self.__actual = self.__comienzo
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return dato
        
    def agregar_por_cabeza(self, dato):
        nuevonodo= Nodo(dato)
        nuevonodo.set_siguiente(self.__comienzo)
        self.__comienzo = nuevonodo
        self.__tope += 1
        #print(dato) #imprime para probar que se carga
        
    def cargar_jugadores(self):
        try:
            with open("Jugadores.csv", encoding="utf-8") as archivo_j, open("Partidas.csv", encoding="utf-8") as archivo_p:
                readerJ = csv.reader(archivo_j, delimiter=';')
                readerP = csv.reader(archivo_p, delimiter=';')
                next(readerJ)
                next(readerP)
                partidas = list(readerP)
                for fila in readerJ:
                    tipo = fila[0]
                    nickname = fila[1]
                    juego = fila[2]
                    nivel = fila[3]
                    modalidad_rol = fila[4]
                    torneos = fila[5]
                    rpm = fila[6]
                    if tipo == "E":
                        jugador = jugadores_equipo(nickname, juego, nivel, modalidad_rol)
                        for p in partidas:
                            if p[0] == nickname:
                                jugador.agregar_partida(p[1], p[2], int(p[3]))
                        self.agregar_por_cabeza(jugador)
                    elif tipo == "I":
                        jugador = jugadores_individuales(nickname, juego, nivel, modalidad_rol,int(torneos), int(rpm))
                        self.agregar_por_cabeza(jugador)
        except FileNotFoundError as e:
            print(f"ERROR No se encontro el archivo: {e.filename}")

    def mostrar_puntaje_mayor(self, puntaje_min): #item 1
        print(f"----------Jugadores con puntaje mayor o igual a {puntaje_min}:----------")
        for jugador in self:
            puntaje_total = jugador.obtener_puntaje()
            if puntaje_total >= puntaje_min:
                print(f"Jugador: {jugador.get_nickname()}, Puntaje: {puntaje_total}")
            
    def mostrar_por_instancia(self):#Item 2: Mostrar para todos los jugadores: nickname, tipo de jugador y su puntaje total.
        print("--------------mostrando datos de jugadores--------------")
        for dato in self:
            if isinstance(dato, jugadores_equipo):
                tipo = "equipo"
            elif isinstance(dato, jugadores_individuales):
                tipo = "individual"
            else:
                tipo = "desconocido"
            print(f"Nickname: {dato.get_nickname()}, Tipo: {tipo}, Puntaje: {dato.obtener_puntaje()}")
            
    def buscar_jugador_por_nickname(self, nickname_buscado):
        actual= self.__comienzo
        i= 0
        flag= False
        jugador= None
        while actual is not None and not flag:
            jugador= actual.get_dato()
            if jugador.get_nickname().lower() == nickname_buscado:
                flag= True
            else:
                actual= actual.get_siguiente()
                i+= 1
        if flag:
            if isinstance(jugador, jugadores_equipo):
                print(f"Jugador de equipo encontrado: {jugador.get_nickname()}\n ROL: {jugador.get_rol()}\n --------------Mostrando historial de partidas--------------")
                for partida in jugador.get_lista_partidas():
                    print(f"   - {partida}")
                print(f"Puntaje total: {jugador.obtener_puntaje()}")
            else:
                print(f"Jugador individual encontrado: {jugador.get_nickname()}")
            return jugador
        else:
            raise ValueError(f"Jugador con nickname {nickname_buscado} no encontrado")

    def agregar_jugador_individual(self, posicion):  #item 4
        if posicion < 0 or posicion > self.__tope:
            raise IndexError("La posicion ingresada no es valida")
        else:
            nickname= input("Ingrese nickname: ").lower()
            actual= self.__comienzo
            while actual is not None:
                jugador= actual.get_dato()
                if jugador.get_nickname().lower() == nickname:
                    raise ValueError("Error: nickname repetido")
                actual= actual.get_siguiente()
            juego= input("Ingrese juego: ")
            nivel= input("Ingrese nivel (principiante/intermedio/profesional): ").lower()
            modalidad_control= input("Ingrese modalidad de control: ")
            torneos= int(input("Ingrese cantidad de torneos ganados: "))
            rpm= int(input("Ingrese rpm: "))
            nuevo_jugador= jugadores_individuales(nickname, juego, nivel, modalidad_control, torneos, rpm)
            self.__insertar_en_posicion(nuevo_jugador, posicion)
        
    def __insertar_en_posicion(self, dato, posicion): #item 4
        nuevo_nodo = Nodo(dato)
        if posicion == 0:
            nuevo_nodo.set_siguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
        else:
            actual = self.__comienzo
            for i in range(posicion - 1):
                actual = actual.get_siguiente()
            nuevo_nodo.set_siguiente(actual.get_siguiente())
            actual.set_siguiente(nuevo_nodo)
        self.__tope += 1