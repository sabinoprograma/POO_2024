from Persona import Persona
from Docente import Docente
from Alumno import Alumno
class Ayudante(Docente, Alumno):
    __concepto: str
    __horasLIA: int

    def __init__(self, dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera, concepto, horasLIA):
        super().__init__(dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera)
        #Docente.__init__(dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera)
        #Alumno.__init__(dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera)
        self.__concepto = concepto
        self.__horasLIA = horasLIA

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Datos Ayudante\n Concepto {self.__concepto}\n Horas LIA {self.__horasLIA}")
        