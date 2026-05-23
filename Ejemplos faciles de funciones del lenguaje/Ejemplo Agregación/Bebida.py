class Bebida:
    __denominacion: str
    __presentacion: str
    __precio: float

    def __init__(self, denominacion, presentacion, precio):
        self.__denominacion = denominacion
        self.__presentacion = presentacion
        self.__precio = precio

    def getDenominacion(self):
        return self.__denominacion
    def getPresentacion(self):
        return self.__presentacion
    def getPrecio(self):
        return self.__precio
        