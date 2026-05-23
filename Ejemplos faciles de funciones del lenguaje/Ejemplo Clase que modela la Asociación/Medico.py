class Medico:
    __dni: int
    __matricula: int
    __especialidad: str
    __apellido: str
    __nombre: str
    __listaPrescripciones = [] #Se agrega un atributo por la clase asociacion. Es una lista ya que es de 1 a *

    def __init__(self, dni, matricula, especialidad, apellido, nombre):
        self.__dni = dni
        self.__matricula = matricula
        self.__especialidad = especialidad
        self.__apellido = apellido
        self.__nombre = nombre
        self.__listaPrescripciones = []
        
    def __str__(self):
        return f"DNI: {self.__dni} Matricula: {self.__matricula } Especialidad: {self.__especialidad} Nombre: {self.__nombre} Apellido: {self.__apellido}"
    
    def getDni(self):
        return self.__dni
    def getMatricula(self):
        return self.__matricula
    def getEspecialidad(self):
        return self.__matricula
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    
    def addPrescripcion(self, prescripcion):
        self.__listaPrescripciones.append(prescripcion)
