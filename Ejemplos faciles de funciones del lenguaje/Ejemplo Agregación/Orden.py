# from Mozo import Mozo
# from Bebida import Bebida
# from Plato import Plato

class Orden:
    __idPedido: int             #En funcion de la cantidad de pedidos, se guarda un id de pedido
    __cantidadPedidos = 0       #Lleva registro la cantidad de pedidos instanciados
    __numeroMesa: int
    #__mozo = object             #Clase partes
    #__listaBebidas = list       #Clase partes
    #__listaPlatos = list        #Clase partes
    
    @classmethod
    def getIdPedido(cls):
        cls.__cantidadPedidos += 1
        return cls.__cantidadPedidos

    def __init__(self, numeroMesa, mozo, bebida = None, plato = None):
        self.__idPedido = self.getIdPedido()
        self.__numeroMesa = numeroMesa
        self.__mozo = mozo
        self.__listaBebidas = []
        self.__listaPlatos = []
        if bebida != None:
            self.agregarBebida(bebida, 1)
        if plato != None:
            self.agregarPlato(plato, 1)
    
    def agregarBebida(self, bebida, cantidad):
        for i in range(cantidad):
            self.__listaBebidas.append(bebida)

    def agregarPlato(self, plato, cantidad):
        for i in range(cantidad):
            self.__listaPlatos.append(plato)

    def cerrarOrden(self):
        print("-------------------")
        print(f"Numero Orden: {self.__idPedido}\nMozo: {self.__mozo.getNombre()}")
        total = 0
        print("Bebidas:")
        for bebida in self.__listaBebidas:
            print(f" {bebida.getDenominacion()} {bebida.getPresentacion()} ${bebida.getPrecio()}")
            total += bebida.getPrecio()
        print("Platos:")
        for plato in self.__listaPlatos:
            print(f" {plato.getDescripcion()} ${plato.getPrecio()}")
            total += plato.getPrecio()
        print(f"TOTAL:        ${total}")
        print("-------------------")

