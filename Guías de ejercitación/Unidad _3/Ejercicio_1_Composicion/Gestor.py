import csv
from claseHotel import Hotel

class gestorHotel:
    def __init__(self):
        self.__listaHoteles = []
        
    def agregar_hotel(self, hotel):
        self.__listaHoteles.append(hotel)
        
    def cantidad_hoteles(self):
        return len(self.__listaHoteles)
    
    def getHoteles(self):
        return self.__listaHoteles

    def agregar_hoteles(self):
        archivo = open('Hoteles.csv')
        reader = csv.reader(archivo, delimiter=';')
        hotel_nuevo = None # inicializo variable vacia para hoteles
        for fila in reader:
            if len(fila) == 3:
                hotel_nuevo = Hotel(fila[0], fila[1], int(fila[2])) #nombre, direccion, telefono
                self.agregar_hotel(hotel_nuevo)
            elif len(fila) == 5 and hotel_nuevo is not None:
                if fila[4].lower() == "true":
                    dispo= True
                else:
                    dispo= False
                hotel_nuevo.crear_habitacion(int(fila[0]), int(fila[1]), fila[2], float(fila[3]), dispo) #numero, piso, tipo, precio_noche, disponibilidad
        archivo.close()
    """
    def listar_hoteles(self):
        print("Lista de hoteles:")
        for i in range(self.cantidad_hoteles()):
            print(f"{i+1}. {self.__listaHoteles[i].get_nombre()}")
        try:
            indice = int(input("Seleccione un hotel (número): ")) - 1
            if 0 <= indice < self.cantidad_hoteles():
                return indice
            else:
                raise Exception("numero de hotel incorrecto")
        except ValueError:
            raise Exception("debe ingresar un numero valido")
    """

    def agregar_nueva_habitacion(self,nombre_hotel): #metodo para agregar habitaciones nuevas, 101;1;sencilla;5000;True 
        hotel= self.buscar_hotel_por_nombre(nombre_hotel)
        numero = input("Ingrese numero de habitacion: ")
        piso= input("Ingrese piso: ")
        tipo = input("Ingrese tipo: sencilla, doble o suite: ")
        precio= input("Ingrese precio por noche: ")
        disponible= input("Ingrese disponibilidad: 1-[Disponible], 0-[No disponible] ") #bool True= disponible, False= no disponible
        if disponible in ["0", "1"]:
            dispo = disponible == "1" # (disponible == "1") --> devuelve valor booleano!!
        else:
            raise Exception("Ingrese un digito 1/0")
        if tipo.lower() in ["sencilla","doble", "suite"]:
            hotel.crear_habitacion(int(numero), int(piso), tipo.lower(), float(precio), dispo)
        else:
            raise TypeError("tipo invalido")
        
    def mostrar_habitaciones_tipo(self, tipo): #Dado un tipo de habitación (sencilla, doble, suite), mostrar número y piso de las habitaciones de ese tipo
        cuenta_tipo=0
        if tipo.lower() in ['sencilla','suite','doble']:
            print(f"Mostrando habitaciones {tipo} del hotel:")
            print(f"{"Numero":<20} {"Piso":<20}")    
            for hotel in self.__listaHoteles:
                for habitaciones in hotel.get_habitaciones():
                    if habitaciones.get_tipo() == tipo.lower():
                        cuenta_tipo+=1
                        print(f"{habitaciones.get_numero():<20} {habitaciones.get_piso():<20}")
            if cuenta_tipo <=0:
                raise AttributeError("Ninguna habitacion encontrada para ese tipo")
        else:
            raise TypeError("tipo invalido")
        
    def reserva_hab(self, nombre_hotel, numero):
        hotel = self.buscar_hotel_por_nombre(nombre_hotel)
        hotel.reservar_habitacion(numero)
        
    def libera_hab(self, nombre_hotel, numero):
        hotel = self.buscar_hotel_por_nombre(nombre_hotel)
        hotel.liberar_habitacion(numero)
        
    def buscar_hotel_por_nombre(self, nombre_hotel):
        flag = False
        i = 0
        while flag is False and i < self.cantidad_hoteles():
            if self.__listaHoteles[i].get_nombre().lower() == nombre_hotel.lower():
                flag = True
            else:
                i += 1
        if flag:
            return self.__listaHoteles[i]
        else:
            raise Exception("nombre invalido")
        
    def mostrar_detalle(self):  #6. Para cada tipo de habitación mostrar el detalle asociado con el siguiente formato
        for hotel in self.__listaHoteles:
            hotel.mostrar_listado(hotel.get_nombre())
        
    def mostrar_libres(self):   #5. Mostrar la cantidad de habitaciones libres por piso.
        for hotel in self.__listaHoteles:
            hotel.get_habitaciones_disponibles_por_piso(hotel.get_nombre())
            
    """
    def mostrar_lista(self):     #5- Mostrar la cantidad de habitaciones libres por piso.
        print(f"Mostrando toda la lista")
        for hotel in self.__listaHoteles:
            for habitaciones in hotel.get_habitaciones():
                    print(f"Numero: {habitaciones.get_numero():<20} Piso: {habitaciones.get_piso():<20} Disponibilidad: {habitaciones.get_disponibilidad():<20}")
    """