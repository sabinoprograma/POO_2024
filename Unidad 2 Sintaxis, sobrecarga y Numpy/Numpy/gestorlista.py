from Bocetito.ClassAutobus import *
import csv

class gestor_lista:
    __lista: list
  
    def __init__(self):
        self.__lista=[]
    
    def cargarcsvlista(self):
        with open(".csv", newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv,delimiter=";")
            for fila in reader:
                un = Clase(fila[0],fila[1],fila[2],fila[3],fila[4],)
                self.__lista.append(un)
      
    def mostrar_lista(self):
        for objeto in self.__lista:
            print(objeto)