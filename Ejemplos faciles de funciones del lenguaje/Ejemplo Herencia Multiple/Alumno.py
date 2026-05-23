from Persona import Persona
class Alumno(Persona):
    __fechaIngreso: str
    __promedio: float
    __carrera: str

    def __init__(self, dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera):
        super().__init__(dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo, fechaIngreso, promedio, carrera)
        self.__fechaIngreso = fechaIngreso
        self.__promedio = promedio
        self.__carrera = carrera

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Datos Alumno\n Fecha Ingreso: {self.__fechaIngreso}\n Promedio: {self.__promedio}\n Carrera: {self.__carrera}")