import csv
from movimiento import Cmovimiento
import numpy as np

class gestorDeMovimiento(): # GESTOR BASADO EN NUMPY 
    __arreglo: np.ndarray
    
    def __init__(self):
        self.__arreglo= np.empty(self.__dimension,dtype=float) #Genero una matriz de 0s con 5 filas y 7 columnas que guardara reales

    # def agregar(self,unamoto):
    #     """Metodo para agregar moto al gestor"""
    #     self.__listaMotos.append(unamoto)

    def agregarMov(self,movi):
        self.__arreglo.append(movi)
        
    def test(self):
        """Metodo para crear/leer movimiento"""
        archivo= open('MovimientosAbril2024.csv')
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarMov(Cmovimiento(fila[0],fila[1],fila[2],fila[3],fila[4]))
        archivo.close()
    
    def mostrarMovimientos(self):
        return self.__arreglo
        
    def __lt__(self, otro): # metodo para sobrecarga
        pass

abc=gestorDeMovimiento()
abc=abc.test()
print(abc.mostrarMovimientos())