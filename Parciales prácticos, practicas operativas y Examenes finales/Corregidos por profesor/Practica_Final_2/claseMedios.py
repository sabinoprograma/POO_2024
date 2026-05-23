from abc import ABC, abstractmethod

class Medios(ABC): #superclase
    __nombre: str
    __audiencia: int
    
    def __init__(self,nombre,audiencia):
        self.__nombre=nombre
        self.__audiencia=audiencia
        
    def __str__(self):
        return f"{self.__nombre}"
        
    def getNombre(self):
        return self.__nombre
    
    def getAudiencia(self):
        return self.__audiencia
    
    @abstractmethod
    def calcularIndiceAudiencia(self)->float:
        pass
    
    def calcularIndice(self):    #metodo abc para calcularIndice y el mostrar que llama al abc
        indice= self.__audiencia/self.calcularIndiceAudiencia()
        return indice
