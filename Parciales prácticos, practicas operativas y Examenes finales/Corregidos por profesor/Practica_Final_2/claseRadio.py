from claseMedios import Medios
from clasePrograma import Programa

class Radio(Medios): #subclase radio hereda de Medios
    __frecuencia: str
    __listaProgramas: list
    
    def __init__(self,nombre,audiencia,frecuencia):
        super().__init__(nombre, audiencia)
        self.__frecuencia=frecuencia
        self.__listaProgramas= []
        
    def __str__(self):
        return super().__str__()
        
    def getProgramas(self):
        return self.__listaProgramas
    
    def getFreq(self):
        return self.__frecuencia
    
    def crearPrograma(self, nombre, horaInicio, horaFin): #COMPOSICION: Recibe atributos por parametros
        programa = Programa(nombre, horaInicio, horaFin)  # crea objetos
        self.__listaProgramas.append(programa)            # agrega objetos a lista
    
    #def agregarPrograma(self,unPrograma): #metodo mal implementado para composicion ya que no recibe los atrib por parametros y no crea los objetos acá
        #self.__listaProgramas.append(unPrograma)
        
    def contarProgramas(self):
        return len(self.__listaProgramas)
    
    def calcularIndiceAudiencia(self):
        return self.contarProgramas()

    #implementar la busquedad