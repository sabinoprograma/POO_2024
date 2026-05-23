from Persona import Persona
class Docente(Persona):
    __codigoCargo: int
    __agrupamiento: int
    __catedra: str
    __sueldo: float
                 #(Parametros Persona )(              Parametros Profes                 )(      Parametros Alumno        )
    def __init__(self, dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera):
        super().__init__(dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera)
        self.__codigoCargo = codigoCargo
        self.__agrupamiento = agrupamiento
        self.__catedra = catedra
        self.__sueldo = sueldo
        
    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Datos Docente\n Codigo Cargo: {self.__codigoCargo}\n Agrupamiento: {self.__agrupamiento}\n Catedra: {self.__catedra}\n Sueldo: {self.__sueldo}")

