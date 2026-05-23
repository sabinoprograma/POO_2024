from claseMovimiento import Movimiento
import numpy as np
import csv

class GestorMovimientos:
    __ListaMov: np.ndarray
    __dimension = int
    __cantidad = int
    __incremento = int
    
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 5
        self.__ListaMov = np.empty(self.__dimension, dtype = Movimiento)
        
    def agregarMovimiento(self, unMovimiento):
        if self.__cantidad == self.__dimension:
            print("Se solicito espacio")
            self.__dimension += self.__incremento
            self.__ListaMov.resize(self.__dimension)
        self.__ListaMov[self.__cantidad] = unMovimiento
        self.__cantidad += 1
        
    def mostrarMovimientos(self):
        for movimiento in self.__ListaMov:
            print(movimiento)
            
    def testMovimientos(self):
        archivo = open('MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                numC = int(fila[0])
                fecha = fila[1]
                desc = fila[2]
                tipo = fila[3]
                imp = float(fila[4])
                unMovi = Movimiento(numC, fecha, desc, tipo, imp)
                self.agregarMovimiento(unMovi)
        self.__ListaMov.resize(self.__cantidad)
        archivo.close()
        
    def getListaMovimientos(self):
        lista = []
        for mov in self.__ListaMov:
            fila = []
            fila.append(mov.getNumC())
            fila.append(mov.getFecha())
            fila.append(mov.getDescripcion())
            fila.append(mov.getTipo())
            fila.append(mov.getImporte())
            lista.append(fila)
        return lista