from matriculas import Matricula
from gestorEmpleado import GestorEmpleado
from gestorPrograma import GestorPrograma
import csv
#CLASE ASOCIACION
class GestorMatricula:
  __lista_matriculas:list
  
  def __init__(self):
    self.__lista_matriculas=[]
    
  def cargar(self,ge,gp):
        archivo = open("matriculas.csv",mode="r",encoding = "utf-8")
        lector = csv.reader(archivo,delimiter = ";")
        bandera = True
        cantidad=0
        
        for fila in lector:
            if bandera:
                bandera=False
            else:
                fecha=fila[0]
                empleado=ge.buscar(fila[1])
                programa=gp.busca(fila[2])
                
                if (empleado is not None and programa is not None):
                            
                  unaMatri=Matricula(fecha,empleado,programa)
                  self.__lista_matriculas.append(unaMatri)
                  cantidad+=1
                  print(f"Matricula agregada: {unaMatri}")
                else:
                  print (f"No se pudo agregar matricula porque empleado {fila[1]} no existe y/o el programa {fila[2]} fue motosierrado")
                  
                  
                
                
        print (f"Se agregaron {cantidad} matriculas a la lista.")        
        print (f"La lista de matriculas tiene {len(self.__lista_matriculas)} elementos.")
        archivo.close()
  
  def informa_programas_matriculados(self,ide):
    print(f"Longitud de la lista: {len(self.__lista_matriculas)}")
    durac=0
    total=0
    
    for matricula in self.__lista_matriculas:
      if ide==int(matricula.get_empleado().get_id_empleado()):
        nombre=matricula.get_programas().get_nombre()
        durac=int(matricula.get_programas().get_duracion())
        total+=durac
        print(f"La duracion del programa {nombre}, en el que esta matriculado el ID,  es: {durac}")
    print(f"El total de minutos de programas matriculados es: {total}")
            
    return
  
  def muestra_matriculados_programa(self,nombre):
    
    for i in range (len(self.__lista_matriculas)):
      if nombre.lower()==self.__lista_matriculas[i].get_programas().get_nombre().lower():
        NombreEmp=self.__lista_matriculas[i].get_empleado().get_nya()
        print(f"Empleado: {NombreEmp}")
    
    return
  
  
  
  
  
  def muestra_no_matriculados(self,Ge:GestorEmpleado):
    ListasEmpleados=Ge.get_lista_empleados()
    
    NoMatriculados=True
    for empleado in ListasEmpleados:
      i=0
      matriculado=False
      while i< len(self.__lista_matriculas):
        if self.__lista_matriculas[i].get_empleado().get_nya()==empleado.get_nya():
          matriculado=True
        
        i+=1
      if not matriculado:
        print(f"Empleado: {empleado.get_nya()} Id: {empleado.get_id_empleado()}")
        NoMatriculados=False
      
    if NoMatriculados:
      print("Todos los empleados registrados estan matriculados en al menos un programa")
    return
  
      
    
  
  