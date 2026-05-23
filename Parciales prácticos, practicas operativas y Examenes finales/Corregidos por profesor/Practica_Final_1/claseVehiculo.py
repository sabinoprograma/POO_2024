import abc
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    __matricula: str
    __modelo: str
    __costoxKM: float
    __cantDeDias: int
    
    def __init__(self, matricula, modelo, costoxKM, cantDeDias):
        self.__matricula = matricula
        self.__modelo = modelo
        self.__costoxKM = costoxKM
        self.__cantDeDias = cantDeDias
    
    def __str__(self) -> str:
        return f"Matricula: {self.__matricula}  Modelo: {self.__modelo}  Costo por KM: {self.__costoxKM}  Cantidad de días: {self.__cantDeDias}"
    
    def getMatricula(self):
        return self.__matricula
    
    def getModelo(self):
        return self.__modelo
    
    def getCostoxKM(self):
        return self.__costoxKM
    
    def getCantDeDias(self):
        return self.__cantDeDias
    
    def calculoAlquiler(self):
        return (self.__cantDeDias * self.__costoxKM) + self.porcentaje() # llamo metodo polimorfico 

    @abstractmethod
    def porcentaje(self) -> float: #metodo abstracto, implementado en las subclases
        pass