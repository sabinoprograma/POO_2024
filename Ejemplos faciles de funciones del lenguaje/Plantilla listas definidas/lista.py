#Carga del archivo
    # Metodo leer_csv carga del archivo csv por identificador.
    # Metodo agregar_por_cola agrega los elementos y los muestra en orden A,B,C,D.

#inciso 1- Insertar un objeto en la colección en una posición determinada.
    # Metodo insertar inserta un objetito en una pos ingresada.
    # Metodo mostrarinsertado muestra el objetito insertado en la pos luego de ingresar los datos.
    # Metodo mostrardatos_insertar muestra el archivo csv + el objeto recien insertado.

#Inciso 2- Agregar un OBJETO a la colección (solicitar el tipo de OBJETO, 
#          y luego los datos que correspondan).
    # Metodo agregar_por_cabeza agrega un objetito al principio.
    # Metodo mostrardatos_agregado muestra el archivo csv + el objeto recien agregado.

#Inciso 3-Dada una posición de la Lista:
#         Mostrar por pantalla qué tipo de objeto se encuentra almacenado en esa posición.
    # Metodo buscar_por_indice utiliza isinstance,verifica y muestra que tipo de objeto se encuentra 
    #en dicha pos.
    
#Inciso 4-Mostrar atributo1, atributo2 y atributo3 del tipo de objeto de menor precio.
    # Metodo mostrar_menor_precio muestra todos los objetos de menor precio,
    #utilizando isinstance.
    
#Inciso 5-Dada una atributo de tipo del objeto, mostrar atributo1, atributo2 y atributo3 de lista de 
#         todos los objetos de ese atributo.
    # Metodo motrarlistado_electrico muestra los atributos de un objeto, de acuerdo a un atributo 
    #ingresado por teclado.
    
#inciso 6-Mostrar atributo1, atributo2, atributo3 e atributo4 de todos los objetos
#         que tienen un atributo en promocion,descuento,virtud(si,no,2000,alto,bajo)
    # Metodo motrarlistado_promo muestra los objetos que tienen algo definido por el enunciado.
from nodo import Nodo
from claseHija1 import *
from claseHija2 import *
import csv

class Lista:
    __cabeza: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__cabeza = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        self.__actual = self.__cabeza
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__indice = 0
            self.__actual = self.__cabeza
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_Padre() 
            self.__actual = self.__actual.get_siguiente()
            return dato

    def agregar_por_cola(self, dato):
        nodo = Nodo(dato)
        if self.__cabeza is None:
            self.__cabeza = nodo
        else:
            actual = self.__cabeza
            while actual.get_siguiente() is not None:
                actual = actual.get_siguiente()
            actual.setSiguiente(nodo)
        self.__tope += 1
    
        
    def mostrardatos_agregado(self):
        print("Elementos de la lista c/ elementos insertados:")
        for datito in self:
            print(f"{datito}")
        
    #Buscar por indice o posicion.
    def buscar_por_indice(self, indice):
        if 0 <= indice < self.__tope:
            aux = self.__cabeza
            for _ in range(indice):
                aux = aux.get_siguiente()
            calefactor=aux.get_padre()
            if isinstance(calefactor):
                indice+=1
                print(f"el calefactor de la posicion {indice} es tipo electrico")
            elif isinstance(calefactor):
                indice+=1
                print(f"el calefactor de la posicion {indice} es tipo gas.")
        else:
            raise IndexError("Posicion incorrecta")
        
                    
    def mostrarnacionales(self):
        print("-----Clientes Nacionales-----")
        for cliente in self:
            if isinstance(cliente,ClienteNacional):
                print(f"{cliente.getProv()} {cliente.getNombre()}")


