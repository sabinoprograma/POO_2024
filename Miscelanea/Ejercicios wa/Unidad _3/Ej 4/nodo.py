from publicacion import publicacion
class Nodo():
    __dato:publicacion
    __sig:object
    def __init__(self,dato) -> None:
        self.__dato=dato
        self.__sig=None
    def getSiguiente(self):
        return self.__sig
    def getDato(self):
        return self.__dato
    def mostrar(self):
        return self.__dato.mostrar()
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
