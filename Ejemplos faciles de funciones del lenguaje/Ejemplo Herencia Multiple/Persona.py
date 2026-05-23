class Persona:
    __dni: int
    __apellido: str
    __nombre: str
               #(Parametros Persona ) (             Parametros Profes                               )(      Parametros Alumno                   )
    def __init__(self, dni, apellido, nombre, codigoCargo=0, agrupamiento=0, catedra="", sueldo=0.0, fechaIngreso ="", promedio=0.0, carrera="" ):  #Se agregan los TODOS los parametros de las clases hijas
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre

    def mostrarDatos(self):
        print(f"Datos Persona:\n DNI: {self.__dni }\n Apellido: {self.__apellido}, {self.__nombre}")
