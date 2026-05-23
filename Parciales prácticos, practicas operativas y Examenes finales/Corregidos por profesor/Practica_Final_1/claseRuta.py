class Ruta:
    __cod: int
    __destino: str
    __distTotal: float
    __rutaA: bool
    
    def __init__(self, cod, destino, distTotal, rutaA=False):
        self.__cod = cod
        self.__destino = destino
        self.__distTotal = distTotal
        self.__rutaA = rutaA
        
    def __str__(self):
        if self.__rutaA == True:
            asig="Si"
        elif self.__rutaA == False:
            asig="No"
        else: asig= "Sin datos de asignación"
        return f"Codigo: {self.__cod}, Destino: {self.__destino}, Distancia total: {self.__distTotal}, Asignada: {asig}"
        
    def getCod(self):
        return self.__cod
    
    def getDestino(self):
        return self.__destino
    
    def getDistTotal(self):
        return self.__distTotal
    
    def getRutaA(self):
        return self.__rutaA
    
    def setRutaA(self):
        self.__rutaA = True