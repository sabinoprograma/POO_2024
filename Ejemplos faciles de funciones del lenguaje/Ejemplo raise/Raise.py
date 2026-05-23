class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __numeroTarjeta: int
    __saldoAnterior: float

    def __init__(self, nomb, ape, dni, numtar, saldant):
        self.__nombre = nomb
        self.__apellido = ape
        self.__dni = dni
        self.__numeroTarjeta = numtar
        self.__saldoAnterior = saldant

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getNumeroTarjeta(self):
        return self.__numeroTarjeta
    def getSaldoAnterior(self):
        return self.__saldoAnterior
    def actualizar_saldo(self, nuevo_saldo):
        self.__saldoAnterior = nuevo_saldo

class GestorClientes:
    __listaClientes: list
    def __init__(self):
        self.__listaClientes=[]
    
    def agregarCliente(self, unCliente):
        if isinstance(unCliente, Cliente):
            self.__listaClientes.append(unCliente)
        else:
            raise TypeError 

def test():
    gestor = GestorClientes()
    objeto1 = Cliente("Hernan", "Castro", 20333111, 5551, 28000)        #Creo un objerto Cliente
    try:
        gestor.agregarCliente(objeto1)                                  #Intento agregarlo al gestor
    except TypeError:                                                   
        print("No se puede agregar un objeto que no es Cliente")        #Si se lanza una excepcion TypeError, se "captura" y se ejecuta este bloque
    else:
        print("Se agregaron los objetos corectamente")                  #Si no se captura una excepcion TypeError, se ejecuta este bloque (OPCIONAL)
    finally:                                    
        print("Test realizado correctamente")                           #Este bloque de codigo siempre se ejecuta (OPCIONAL)
    
"""
if __name__=="__main__":
    test()


"""
if __name__=="__main__":
    gestor = GestorClientes()
    objeto1 = Cliente("Hernan", "Castro", 20333111, 5551, 28000)        #Creo un objero Cliente
    gestor.agregarCliente(objeto1)                                      #Lo agrego al gestor sin problemas, porque es un objeto Cliente
    gestor.agregarCliente(45)                                           #Si trato de agregar un objeto int, se lanza de "forma manual" la excepcion TypeError
    
#"""
