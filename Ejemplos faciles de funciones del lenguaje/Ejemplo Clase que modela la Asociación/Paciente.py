
class Paciente:
    __dni: int
    __apellido: str
    __nombre: int
    __listaPrescripciones: list #Se agrega unatrbuto por la asociacion. Como la cardinalidad es de 1 a * se implementa como una lista

    def __init__(self, dni, apellido, nombre):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__listaPrescripciones = []
    def __str__(self) -> str:
        return f"DNI: {self.__dni} Apellido: {self.__apellido} Nombre: {self.__nombre}"
    
    def addPrescripcion(self, prescipcion):
        self.__listaPrescripciones.append(prescipcion)