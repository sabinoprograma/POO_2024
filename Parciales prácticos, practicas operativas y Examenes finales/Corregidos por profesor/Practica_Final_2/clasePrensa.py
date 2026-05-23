from claseMedios import Medios

class Prensa(Medios): #subclase prensa hereda de Medios
    __periodicidad:str
    __cantSecciones: int
    
    def __init__(self, nombre, audiencia, periodicidad, cantSecciones): #P,Caras,15000,mensual,8
        super().__init__(nombre, audiencia)
        self.__periodicidad= periodicidad
        self.__cantSecciones= cantSecciones
        
    def calcularIndiceAudiencia(self):
        if self.__periodicidad == "mensual":
            return self.__cantSecciones
        elif self.__periodicidad == "semanal":
            return self.__cantSecciones * 4
        else:
            raise Exception("sin datos")