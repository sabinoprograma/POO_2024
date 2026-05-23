#!/usr/bin/env python

class usuario:
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
    
    def __str__(self) -> str:
        return f"Nombre completo: {self.__nombre} {self.__apellido}, DNI: {self.__dni}" #Indico a python como debe interpretar un objeto al usar print() (a través de metodos como mostrar listas)
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_dni(self):
        return self.__dni
    
class gestor:
    __listUsuarios: list
    
    def __init__(self):
        self.__listUsuarios= []
        
    def get_lista(self):
        return self.__listUsuarios
        
    def agregar_usuarios(self,unUser):
        if isinstance(unUser, usuario):
            self.get_lista().append(unUser)
        else:
            raise TypeError("usuario con datos incorrectos!")
        
    def mostrar_usuarios(self): #recorre la lista de objetos usuarios y muestra usando metodo str.
        print("Mostrando usuario/s:")
        for lista in self.__listUsuarios:
            print(f"{lista}")

if __name__ == "__main__":
    gestorUsuarios = gestor()
    Objeto1 = usuario("Sabino","Pignatari",42012435)
    try:
        #gestorUsuarios.agregar_usuarios(Objeto1)
        gestorUsuarios.agregar_usuarios(123) #agrego datos erroneos para producir error adrede.
        gestorUsuarios.mostrar_usuarios()
    except TypeError as e:
        print(f"Error encontrado: {e}")
    gestorUsuarios.agregar_usuarios(Objeto1)    #al capturar error con bloque try/except el programa sigue con la ejecución, no se detiene.
    gestorUsuarios.mostrar_usuarios()