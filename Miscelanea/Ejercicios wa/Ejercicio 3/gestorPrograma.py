from programas import Programa
import csv
#CLASE ASOCIACION
class GestorPrograma:
  __lista_programas:list
  
  def __init__(self):
    self.__lista_programas=[]
    
  def cargar(self):
        archivo = open("programas.csv",mode="r",encoding = "utf-8")
        lector = csv.reader(archivo,delimiter = ";")
        bandera = True
        
        for fila in lector:
            if bandera:
                bandera=False
            else:
                unPrograma=Programa(fila[0],fila[1],int(fila[2]))
                self.__lista_programas.append(unPrograma)
        print(f"Los programas fueron cargados correctamente.")
        archivo.close()
  
  def busca(self, nombre):
    i=0
    encontrado=False
    objeto=None
    while not encontrado and i< len(self.__lista_programas):
      if nombre==self.__lista_programas[i].get_nombre():
        encontrado=True
        
      else:
        i+=1
    if encontrado:
      objeto=self.__lista_programas[i]
    return objeto