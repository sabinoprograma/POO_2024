class Mozo:     #Las partes agregadas quedan tal como estan 
    __idMozo: int
    __apellido: str
    __nombre: str

    def __init__(self, idMozo, apellido, nombre):
        self.__idMozo = idMozo
        self.__apellido = apellido
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido