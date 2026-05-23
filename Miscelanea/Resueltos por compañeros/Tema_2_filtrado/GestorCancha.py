from  ClassAlquiler import Alquiler 
from  ClassCancha import Cancha
import csv
import numpy as np

class GestorDeCancha:
    __cantidad = int
    __dimension = int
    __incremento = 1
    __arre_canchas = np.ndarray
    
    def __init__(self,dimension,incremento):
        self.__arre_canchas = np.empty(dimension, dtype = Cancha)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
    
    def __str__(self):
        cadena=""
        for canchas in self.__arre_canchas[:self.__cantidad]:
            cadena = cadena + str(canchas) + "\n"
        return cadena
    
    def agregar_cancha(self,objeto):
        if self.__cantidad == self.__dimension:
            self.__dimension = self.__dimension + self.__incremento
            self.__arre_canchas.resize(self.__dimension)
        self.__arre_canchas[self.__cantidad] = objeto
        self.__cantidad = self.__cantidad + 1
        
    def test_cancha(self):
        archi = open('Canchas.csv')
        reader = csv.reader(archi, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                id_cancha = fila[0]
                tipo_piso = str(fila[1])
                importe_hora = float((fila[2]))
                una_cancha = Cancha(id_cancha, tipo_piso, importe_hora)
                self.agregar_cancha(una_cancha)
        self.__arre_canchas.resize(self.__cantidad)
        archi.close()
    
    def get_importe_diario(self,indice):
        return self.__arre_canchas[indice].get_importe_hora()
    
    def buscarImporte(self,xC):
        long = self.__cantidad
        i = 0
        ideBase = self.__canchas[i].getId()
        while i<long and xC != ideBase:
            i += 1
            ideBase = self.__canchas[i].getId()
        if xC == ideBase:
            imp = self.__canchas[i].getImporte()
            return imp
    