from datetime import datetime

class Programa:
    __nombre: str
    __hsInicio: datetime
    __hsFin: datetime
    
    def __init__(self, nombre, hsInicio, hsFin):
        self.__nombre= nombre
        self.__hsInicio= hsInicio
        self.__hsFin= hsFin
        
    def __str__(self):
        return f"Nombre:{self.__nombre} Hora inicio:{self.__hsInicio} Hora fin:{self.__hsFin}"
    
    def getInicio(self):
        return self.__hsInicio
    
    def getNombre(self):
        return self.__nombre
    