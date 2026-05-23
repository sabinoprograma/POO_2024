import numpy as np
class departamento():
    __id:int
    __Propietario:str
    __piso:int
    __Ndep=int
    __CDormitorios:int
    __CBaños:int
    __sup:int
    def __init__(self,id,pro,piso,NDep,CD,CB,sup) -> None:
        self.__id=int(id)
        self.__Propietario=pro
        self.__Ndep=NDep
        self.__CDormitorios=int(CD)
        self.__piso=int(piso)
        self.__sup=float(sup)
        self.__CBaños=int(CB)
    def __str__(self) -> str:
        return ("--ID:{} Propietario:{} Piso:{} Numero de departamento:{} Cantidad de Habitaciones:{} Cantiadad de baños:{} Superficie:{}m2\n".format(self.__id,self.__Propietario,self.__piso,self.__Ndep,self.__CDormitorios,self.__CBaños,self.__sup))


    def getCB(self):
        return self.__CBaños
    def getCD(self):
        return self.__CDormitorios
    def getsup(self):
        return self.__sup
    def getpiso(self):
        return self.__piso
    def getprop(self):
        return self.__Propietario
    def getid(self):
        return self.__id
    def getND(self):
        return self.__Ndep
