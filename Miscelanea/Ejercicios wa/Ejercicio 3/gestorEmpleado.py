
from empleados import Empleado
import csv
#CLASE ASOCIACION
class GestorEmpleado:
  __lista_empleados:list
  
  def __init__(self):
    self.__lista_empleados=[]
    
  def cargar(self):
        archivo = open("empleados.csv",mode="r",encoding = "utf-8")
        lector = csv.reader(archivo,delimiter = ";")
        bandera = True
        
        for fila in lector:
            if bandera:
                bandera=False
            else:
                unEmpleado=Empleado(fila[0],int(fila[1]),fila[2])
                self.__lista_empleados.append(unEmpleado)
        print(f"Los empleados fueron cargados correctamente.")
        archivo.close()
  
  def buscar(self, nombre):
    i=0
    encontrado=False
    objeto=None
    while not encontrado and i< len(self.__lista_empleados):
      if nombre==self.__lista_empleados[i].get_nya():
        encontrado=True
        
      else:
        i+=1
    if encontrado:
      objeto=self.__lista_empleados[i]
    return objeto
  
  def get_lista_empleados(self):
    
      return self.__lista_empleados
      
    