

class Persona:
    __dni: int
    __apellido: str
    __nombre: str
    def __init__(self, dni, apellido, nombre):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
    def __str__(self):
        return f"DNI: {self.__dni}\nApellido: {self.__apellido} Nombre: {self.__nombre}"
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido