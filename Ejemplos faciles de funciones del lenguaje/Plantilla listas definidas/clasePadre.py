import abc
from abc import ABC, abstractmethod
class Padre(ABC):
    __a1:str
    __a2: str
    __a3: str
    __a4: str
    __a5: str
    __atributodeclase = 0

    def __init__(self,a1,a2,a3,a4,a5):
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5

    def __str__(self):
        return f"{self.__a1} {self.__a2} {self.__a3} {self.__a4} {self.__a5}"
    
    def geta1(self):
        return self.__a1
    
    def geta2(self):
        return self.__a2
    
    def geta3(self):
        return self.__a3

    def geta4(self):
        return self.__a4
    
    def geta5(self):
        return self.__a5
    
    
    @classmethod
    def getAtributoDeClase(cls):
        return cls.__atributodeclase
    
    @abc.abstractmethod
    def claseAbstracta(self):
        pass