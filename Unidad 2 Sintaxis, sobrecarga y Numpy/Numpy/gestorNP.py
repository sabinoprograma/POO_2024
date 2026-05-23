from Bocetito.ClassVehiculo import *
import numpy as np
import csv

#ARREGLO NUMPY CARGAR
class gestor_numpy:
    __arreglo:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int

    def __init__(self):
        self.__dimension=0
        self.__cantidad=0
        self.__incremento=1
        self.__arreglo= np.empty(0,dtype=CLASE)
    
    def agregarMovimiento(self,un:CLASE):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo=np.resize(self.__arreglo,(self.__dimension))
        self.__arreglo[self.__cantidad]=un
        self.__cantidad+=1
  
    def cargarcsv(self):
        with open('.csv', newline='') as a:
            reader = csv.reader(a,delimiter=";")
            next(reader)
            for fila in reader:
                un=CLASE(fila[0],fila[1],fila[2],fila[3],float(fila[4]))
             self.agregarMovimiento(un)
            
    def mostrar_arreglo(self):
        for movimiento in self.__arreglo:
            print(movimiento)   