#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Dr-malito 22
#
# Created:     20/05/2024
# Copyright:   (c) Dr-malito 22 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv
import numpy as np
from cabana import Cabana
class GestorCabana:
    __cantidad =0
    __dimension: int
    __incremento:int
    __cabanas: np.ndarray
    def __init__(self,dimension=0):
        self.__cabanas=np.empty(dimension,dtype=Cabana)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = 1
    def agregarCab(self, Unacabana):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__cabanas.resize(self.__dimension)
        self.__cabanas[self.__cantidad] = Unacabana
        self.__cantidad += 1
    def Carga(self):
        archi=open('Cabañas.csv')
        reader=csv.reader(archi,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                numero=fila[0]
                cantidad_hab=fila[1]
                cantidad_camagde=fila[2]
                cantidad_camachica=fila[3]
                importe=fila[4]
                Unacabana=Cabana(numero,cantidad_hab,int(cantidad_camagde),int(cantidad_camachica),float(importe))
                self.agregarCab(Unacabana)
        archi.close()
    def ordenar_por_capacidad(self):
        indices_ordenados = np.argsort([cabana.capacidad() for cabana in self.__cabanas[:self.__cantidad]])
        self.__cabanas[:self.__cantidad] = self.__cabanas[indices_ordenados]
    def buscar_por_capacidad(self, huespedes, gestor_reservas):
        i = 0
        while i < self.__cantidad:
            cabana = self.__cabanas[i]
            if cabana >= huespedes and not gestor_reservas.reserva(cabana.getNumero()):
                print(f"Cabaña número {cabana.getNumero()} tiene capacidad para {huespedes} huéspedes y no está reservada")
            i += 1
    def buscar_por_numero(self,numero):
        i = 0
        while i < self.__cantidad:
            cabana=self.__cabanas[i]
            if cabana.getNumero() == numero:
                return cabana
            i += 1
        return None