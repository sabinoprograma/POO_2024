from biblioteca import Biblioteca
from libro import Libro
import csv
import os

class ManejadorBiblioteca:
    __lista_biblioteca: list
    
    def __init__(self):
        self.__lista_biblioteca = []
    
    def agregar_biblioteca(self, nueva_biblioteca):
        self.__lista_biblioteca.append(nueva_biblioteca)
        
    def cargar_desde_archivo(self):
        i=0
        ruta = os.path.join(os.path.dirname(__file__), "Biblioteca.csv")
        archivo = open(ruta, mode="r")
        lector = csv.reader(archivo, delimiter=";")
        
        for fila in lector:
            if len(fila) == 3:
                unaBiblioteca = Biblioteca(fila[0], fila[1], fila[2])
                self.agregar_biblioteca(unaBiblioteca)
            else:
                titulo = fila[0]
                autor = fila[1]
                isbn = fila[2]
                genero = fila[3]
                unLibro = Libro(titulo, autor, isbn, genero)
                self.__lista_biblioteca[i-1].agregar_libro(unLibro)
        archivo.close()
    
    #Inciso 1  
    def buscar_biblioteca(self, nombre_biblioteca):
        encontrado = False
        i = 0
        valor_retorno = None
        longitud = len(self.__lista_biblioteca)
        
        while not encontrado and i < longitud:
            if self.__lista_biblioteca[i].get_nombre() == nombre_biblioteca:
                encontrado = True
                valor_retorno = i
            else:
                i += 1
        return valor_retorno
    
    def inciso_a(self, i, titulo, autor, isbn, genero):
        libro = Libro(titulo, autor, isbn, genero)
        self.__lista_biblioteca[i].agregar_libro(libro)
        
    #Inciso 2          
    def inciso_b(self, i, nombre_libro):
        self.__lista_biblioteca[i].buscar_libro(nombre_libro)
        
    #Inciso 3
    def recorrer_biblioteca(self, nombre_libro):
        for biblioteca in self.__lista_biblioteca:
            i = biblioteca.buscar_libro2(nombre_libro)
            if (i != None):
                print(f"Biblioteca: {biblioteca.get_nombre()}")
    
    #Inciso 4
    def mostrar(self):
        for biblioteca in self.__lista_biblioteca:
            print(f"{biblioteca.get_nombre()}")
            biblioteca.mostrar_libros()