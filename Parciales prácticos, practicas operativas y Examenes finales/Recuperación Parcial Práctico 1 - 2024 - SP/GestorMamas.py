from ClassMama import Mama
from ClassNacimientos import Nacimiento
import numpy as np
import csv

class GestorDeMama:
    __cantidad = int
    __dimension = int
    __incremento = 5
    __arre_mama = np.ndarray
    
    def __init__(self,dimension,incremento):
        self.__arre_mama = np.empty(dimension, dtype = Mama)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
    
    def __str__(self):
        cadena=""
        for cabaña in self.__arre_mama[:self.__cantidad]:
            cadena = cadena + str(cabaña) + "\n"
        return cadena
    
    def agregar_mama(self,objeto):
        if self.__cantidad == self.__dimension:
            self.__dimension = self.__dimension + self.__incremento
            self.__arre_mama.resize(self.__dimension)
        self.__arre_mama[self.__cantidad] = objeto
        self.__cantidad = self.__cantidad + 1
    
    def test_mama(self):
        archi = open('Mamas.csv')
        reader = csv.reader(archi, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                dni = int(fila[0])
                edad = int(fila[1])
                ayn = (fila[2])
                una_mama = Mama(dni,edad,ayn)
                self.agregar_mama(una_mama)
        self.__arre_mama.resize(self.__cantidad)
        archi.close()
        
    def buscar_dni(self, dni):
        i = 0
        while i < self.__cantidad:
            if self.__arre_mama[i].get_dni() == dni:
                return i 
            i += 1
        return -1
    
    def muestra_listado(self,dni,bebes):
        indice = self.buscar_dni(dni)
        if indice != -1 and self.__arre_mama[indice].get_dni() == dni:
            print(self.__arre_mama[indice].get_ayn())
            print(self.__arre_mama[indice].get_dni())
            bebes.get_lista_bebes(dni)
            
        else:
            print("Error DNI no encontrado")
        
    