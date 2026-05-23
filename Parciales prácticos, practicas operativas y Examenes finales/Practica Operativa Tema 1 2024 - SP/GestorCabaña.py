import numpy as np
import csv
from ClassCabaña import Cabañas
from ClassReserva import Reservas

class GestorDeCabañas:
    __cantidad = int
    __dimension = int
    __incremento = 5
    __array_cabañas = np.ndarray
    
    def __init__(self,dimension,incremento):
        self.__array_cabañas = np.empty(dimension, dtype = Cabañas)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
    
    def __str__(self):
        cadena=""
        for cabaña in self.__array_cabañas[:self.__cantidad]:
            cadena = cadena + str(cabaña) + "\n"
        return cadena
    
    def agregar_cabaña(self,objeto_cabaña):
        if self.__cantidad == self.__dimension:
            self.__dimension = self.__dimension + self.__incremento
            self.__array_cabañas.resize(self.__dimension)
        self.__array_cabañas[self.__cantidad] = objeto_cabaña
        self.__cantidad = self.__cantidad + 1
        
    def get_cabaña(self,indice):
        return self.__array_cabañas[indice]
    
    def get_importe_diario(self,indice):
        return self.__array_cabañas[indice].get_importe_por_dia()
    
    def listar_cabañas(self):
        for i in range(self.__cantidad):
            print(self.__array_cabañas[i])
    
    def test_cabañas(self):
        archi = open('Cabañas.csv')
        reader = csv.reader(archi, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                numero = int(fila[0])
                cantidad_habitaciones = int(fila[1])
                cantidad_camas_grandes = int((fila[2]))
                cantidad_camas_chicas = int(fila[3])
                importe_por_dia = float(fila[4])
                una_cabaña = Cabañas(numero,cantidad_habitaciones,cantidad_camas_grandes,cantidad_camas_chicas,importe_por_dia)
                self.agregar_cabaña(una_cabaña)
        self.__array_cabañas.resize(self.__cantidad)
        archi.close()
           
    def mostrar_cabañas(self,cantidad_huespedes,gestor_reserva):
        if self.verifica_huespedes(cantidad_huespedes):
            print("Cabañas que cumplen con el espacio y estan disponibles (sin reservas): ")
            for i in range(self.__cantidad):
                cabaña = self.__array_cabañas[i]
                if cabaña >= cantidad_huespedes:
                    num_cabaña = cabaña.get_numero_cabaña()
                    if gestor_reserva.verifica_reserva(num_cabaña):
                        print(f"Cabaña: {num_cabaña}")
        else:
            print(f"Ninguna cabaña disponible para {cantidad_huespedes} personas")
            
    def verifica_huespedes(self,cant):
        flag = False
        for cabaña in self.__array_cabañas[:self.__cantidad]:
            if cant == (cabaña.get_cantidad_camas_grandes() * 2) + cabaña.get_cantidad_camas_chicas():
                flag = True
        return flag