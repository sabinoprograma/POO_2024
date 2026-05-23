class Plato:
    __descripcion: str
    __precio: float

    def __init__(self, descripcion, precio):
        self.__descripcion = descripcion
        self.__precio = precio

    def getDescripcion(self):
        return self.__descripcion
    def getPrecio(self):
        return self.__precio