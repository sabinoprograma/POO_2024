from clasePadre import Padre
class Nodo:
    __padre: object
    __siguiente: object
    
    def __init__(self, otroPadre):
        self.__padre= otroPadre
        self.__siguiente= None
        
    def setSiguiente(self, siguiente):
        self.__siguiente= siguiente
        
    def get_siguiente(self):
        return self.__siguiente
    
    def get_Padre(self):
        return self.__padre