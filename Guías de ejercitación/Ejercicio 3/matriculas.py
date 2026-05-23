

class Matricula:
  __fecha:str
  __empleados:object
  __programas:object
  
  def __init__(self, fecha, empleados, programas):
            self.__fecha = fecha
            self.__empleados = empleados
            self.__programas = programas
  
  
  def get_empleado(self):
    return self.__empleados
  
  def get_programas(self):
    return self.__programas
            
  def __str__(self):
            return f"Fecha: {self.__fecha} - Empleado: {self.__empleados} - Programa: {self.__programas}"
  
  
  
