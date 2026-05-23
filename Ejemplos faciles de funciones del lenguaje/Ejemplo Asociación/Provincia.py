class Provincia:
    __nombre: str
    __cantidadDeHabitantes: int
    __gobernador: object #Aca se visualiza la asociación entre las clases. Se debe agregar, ya que no figura en diagrama UML

    def __init__(self, nombre, cantidadDeHabitantes, gobernador = None):
        self.__nombre = nombre
        self.__cantidadDeHabitantes = cantidadDeHabitantes
        self.__gobernador = gobernador

    def __str__(self):
        return f"Nombre: {self.__nombre} Habitantes: {self.__cantidadDeHabitantes} Gobernador: {self.__gobernador.getNombreApellido()}"
    
    def getNombre(self):
        return self.__nombre
        
    def getCantHabitantes(self):
        return self.__cantidadDeHabitantes
    
    def getGobernador(self):
        return self.__gobernador
    
    def setGobernador(self, gobernador):
        self.__gobernador = gobernador
    


        
        
