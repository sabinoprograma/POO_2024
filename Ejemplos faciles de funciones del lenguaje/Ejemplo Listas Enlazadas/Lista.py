from Nodo import Nodo
from Profesor import Profesor
class Lista:
    __comienzo: Nodo
    __actual: Nodo                      #Para adherir al iterator protocol   
    __indice = 0                       #Para adherir al iterator protocol
    __tope = 0                         #Para adherir al iterator protocol
    def __init__(self):
        self.__comienzo = None
        self.__actual = None            #Para adherir al iterator protocol

    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0  # Reiniciar siempre
        return self

    
    def __next__(self):                 #Para adherir al iterator protocol
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
   
    def agregarProfesor(self, unProfesor):
        nodo = Nodo(unProfesor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo            #Para adherir al iterator protocol
        self.__tope += 1                #Para adherir al iterator protocol

    def listarDatos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def eliminarPorDni(self, dni):
        aux = self.__comienzo
        encontrado = False
        if aux.getDato().getDni() == dni:
            encontrado = True
            print(f"Encontrado {aux.getDato()}")
            self.__comienzo = aux.getSiguiente()
            self.__tope -= 1            #Para adherir al iterator protocol
            del aux
        else:
            anterior = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if aux.getDato().getDni() == dni:
                    encontrado = True
                else:
                    anterior = aux
                    aux = aux.getSiguiente() 
            if encontrado:
                print(f"Encontrado {aux.getDato()}")
                anterior.setSiguiente( aux.getSiguiente() )
                self.__tope -= 1
                del aux
            else:
                print(f"El DNI: {dni}, no esta en la lista")

profesor1 = Profesor(43546675,"Florencia", "Perez", "Interino Matematica")
profesor2 = Profesor(34565464,"Juan", "Perez", "Interino Fisica")
profesor3 = Profesor(40482105,"Anahi", "Amado", "Interino Ingles")
lista1 = Lista()
lista1.agregarProfesor(profesor1)
lista1.agregarProfesor(profesor2)
lista1.agregarProfesor(profesor3)

for profe in lista1:
    print(profe)





               
"""
profesor1 = Profesor(43546675,"Florencia", "Perez", "Interino Matematica")
profesor2 = Profesor(34565464,"Juan", "Perez", "Interino Fisica")
profesor3 = Profesor(40482105,"Anahi", "Amado", "Interino Ingles")
lista1 = Lista()
lista1.agregarProfesor(profesor1)
lista1.agregarProfesor(profesor2)
lista1.agregarProfesor(profesor3)
lista1.listarDatos()
lista1.eliminarPorDni(34565464)
print("\n------------lista nueva---------------\n")
lista1.listarDatos()
"""