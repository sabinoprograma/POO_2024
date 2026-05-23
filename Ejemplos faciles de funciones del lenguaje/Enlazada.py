class Nodo:     # Clase Nodo
    def __init__(self, dato):
        self.dato = dato
        self.siguiente: 'Nodo | None' = None

class ListaEnlazada:        # Clase Lista Enlazada
    def __init__(self):
        self.cabeza = None   # Primer nodo de la lista

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()     # Uso
for i in range(70):
    lista.agregar_al_final(i)
lista.mostrar()