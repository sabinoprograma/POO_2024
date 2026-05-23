class Movimiento:
    __numC: int
    __fecha: str
    __descripcion: str
    __tipo: str
    __importe: float
    
    def __init__(self, numC, fecha, descripcion, tipo, imp):
        self.__numC = numC
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipo = tipo
        self.__importe = imp
        
    def __str__(self):
        return "%s %s %s %s %s" % (self.__numC, self.__fecha, self.__descripcion, self.__tipo, self.__importe)
    
    def getNumC(self):
        return self.__numC
    
    def getFecha(self):
        return self.__fecha
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe