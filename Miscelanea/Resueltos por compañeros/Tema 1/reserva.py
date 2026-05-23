#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Dr-malito 22
#
# Created:     20/05/2024
# Copyright:   (c) Dr-malito 22 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Reserva:
    __numero:str
    __nombre:str
    __n_cab_asig:str
    __f_inicio_hosp:str
    __cant_huesp:str
    __cant_dias:int
    __importe_sena:float
    def __init__(self,numero,nombre,n_cabana,inicio,huesped,dias,sena):
        self.__numero=numero
        self.__nombre=nombre
        self.__n_cab_asig=n_cabana
        self.__f_inicio_hosp=inicio
        self.__cant_huesp=huesped
        self.__cant_dias=dias
        self.__importe_sena=sena
    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getNcabana(self):
        return self.__n_cab_asig
    def getFechainicio(self):
        return self.__f_inicio_hosp
    def getNhuespedes(self):
        return self.__cant_huesp
    def getNdias(self):
        return self.__cant_dias
    def getSena(self):
        return self.__importe_sena


