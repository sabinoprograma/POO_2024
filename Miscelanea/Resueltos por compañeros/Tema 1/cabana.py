#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Dr-malito 22
#
# Created:     20/05/2024
# Copyright:   (c) Dr-malito 22 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Cabana:
    __numero:str
    __cant_hab:str
    __cant_camagde:int
    __cant_camchi:int
    __importe:float
    def __init__ (self,numero,cantidad,camagde,camachi,importe):
        self.__numero=numero
        self.__cant_hab=cantidad
        self.__cant_camagde=camagde
        self.__cant_camchi=camachi
        self.__importe=importe
    def getNumero(self):
        return self.__numero
    def getNhab(self):
        return self.__cant_hab
    def getNcamagde(self):
        return self.__cant_camagde
    def getNcamach(self):
        return self.__cant_camchi
    def getImporte(self):
        return self.__importe
    def capacidad(self):
        return self.__cant_camagde * 2 + self.__cant_camchi
    def __ge__(self,otros):
        capacidad= self.__cant_camagde * 2 + self.__cant_camchi
        return capacidad>=otros

