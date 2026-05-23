class Gobernador:
    __dni: int
    __nombreApellido: str
    __provincia: object #Aca se visualiza la asociación entre las clases. Se debe agregar, ya que no figura en diagrama UML. Se debe prestar atencion a la cardinalidad

    def __init__(self, dni, nombreApellido, provincia = None):
        self.__dni = dni
        self.__nombreApellido = nombreApellido
        self.__provincia = provincia 

    def __str__(self):
        return f"Gobernador: DNI: {self.__dni}, Nombre y Apellido: {self.__nombreApellido}, Provincia: {self.__provincia.getNombre()}"

    def getDni(self):
        return self.__dni

    def getNombreApellido(self):
        return self.__nombreApellido

    def getProvincia(self):
        return self.__provincia
    
    def setProvinicia(self, provincia):
        return self.__provincia

