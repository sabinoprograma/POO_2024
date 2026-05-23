from claseCliente import Cliente
import csv

class GestorClientes:
    __ListaClientes: list
    def __init__(self):
        self.__ListaClientes = []
    def agregarCliente(self, unCliente):
        self.__ListaClientes.append(unCliente)
    def mostrarClientes(self):
        for cliente in self.__ListaClientes:
            print(cliente)
    def testClientes(self):
        archivo = open('ClientesFarmaCiudad.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                nom = fila[0]
                ape = fila[1]
                dni = int(fila[2])
                numC = int(fila[3])
                saldoA = float(fila[4])
                unCliente = Cliente(nom, ape, dni, numC, saldoA)
                self.agregarCliente(unCliente)
        archivo.close()
        
    def buscarIndice(self, xdni): #busca el indice del cliente por medio del dni
        band = False
        i = 0
        while band != True and i < len(self.__ListaClientes):
            if self.__ListaClientes[i].getDNI() == xdni:
                band = True
            else:
                i += 1
        if band == True:
            return i
        else:
            return -1
        
    def actualizarSaldo(self, listaM, xdni):
        i = self.buscarIndice(xdni)
        if i == -1:
            print(f"No se encontro la cuenta para el dni: {xdni}")
        else:
            saldoA = self.__ListaClientes[i].getSaldoA()
            numC = self.__ListaClientes[i].getNumC()
            nom = self.__ListaClientes[i].getNom()
            ape = self.__ListaClientes[i].getApe()
            print(f"Cliente: {nom} {ape}            Numero de cuenta: {numC}")
            print(f"Saldo anterior: {saldoA}")
            print(f"Movimientos:")
            print("             Fecha            Descripcion         Importe             Tipo de Movimiento")
            for movimiento in listaM:
                if numC == movimiento[0]:
                    tipo = movimiento[3]
                    imp = movimiento[4]
                    self.__ListaClientes[i].actualizarSaldo(tipo, imp)
                    fecha = movimiento[1]
                    desc = movimiento[2]
                    saldo = self.__ListaClientes[i].getSaldoA()
                    print(f"""          {fecha}         {desc}          {imp}           {tipo}
                            Saldo Actualizado: {saldo}""")
                    
    def informarMovimientos(self, listaM, xdni):
        i = self.buscarIndice(xdni)
        if i == -1:
            print(f"No se encontro la cuenta para el dni: {xdni}")
        else:
            numC = self.__ListaClientes[i].getNumC()
            nom = self.__ListaClientes[i].getNom()
            ape = self.__ListaClientes[i].getApe()
            band = False
            for movimiento in listaM:
                if numC == movimiento[0]:
                    band = True
            if band == False:
                print(f"Cliente: {ape} {nom} ")
            elif band == True:
                print("El cliente tiene movimientos en el mes de abril")
            
    def ordenar(self):
        self.__ListaClientes = sorted(self.__ListaClientes)
