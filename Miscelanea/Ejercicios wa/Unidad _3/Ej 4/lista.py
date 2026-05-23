from nodo import Nodo
from LibroImpreso import LibroImpreso
from AudioLibro import AudioLibro
from publicacion import publicacion
import csv
class lista():
    __comienzo=Nodo
    __actual=Nodo
    #__indice:int
    #__tope:int
    def __init__(self) -> None:
        self.__comienzo=None
        self.__actual=None
        #self.__indice=0
        #self.__tope=0
    """""
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
        """""
    def agregar(self,dato):
        nodo=Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        #self.__actual=nodo
        #self.__tope+=1
    def cargar(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 4\\Publicaciones.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if len(fila)==6:
                unlibro=LibroImpreso(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            else:
                unlibro=AudioLibro(fila[0],fila[1],fila[2],fila[3],fila[4])

            self.agregar(unlibro)
        archivo.close()
    def mostrar(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.mostrar())
            aux=aux.getSiguiente()
    def longitud(self):
        cant=0
        aux=self.__comienzo
        while aux!=None:
            cant+=1
            aux=aux.getSiguiente()
        return cant
    def obtener(self,posicion):
        try:
            aux=self.__comienzo
            cant=0
            elemento=self.recorrer(aux,posicion,cant)
            #print("El lemento es" .format(elemento))
            #print(elemento)
            libro=None
            if isinstance(elemento,AudioLibro):
                libro="Audio Libro"
            elif isinstance(elemento,LibroImpreso):
                libro="Libro Impreso"
            return libro
        except TypeError:
            print("Tenemos un problema con el libro")
    def recorrer(self,aux,posicion,cant):
        if cant!=posicion:
            aux=aux.getSiguiente()
            cant+=1
            dato=self.recorrer(aux,posicion,cant)
        else:
            dato=aux.getDato()
            #print(dato)
        #print(dato)

        return dato
    def tipos(self):
        aux=self.__comienzo
        cantA=0
        cantI=0
        while aux!=None:
            if isinstance(aux.getDato(),AudioLibro) :
                cantA+=1
            else:
                cantI+=1
            aux=aux.getSiguiente()
        print("La cantidad de elementos de catologo es\n Audio libros: {} y Libros Impresos: {}".format(cantA,cantI))