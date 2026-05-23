import csv
from moto import moto
from pedido import pedido
    
class pedido:
    __patente: str
    __idPedido:int
    __cantPedidos:int
    __ETA:int
    __TRM:int
    __precio:float
      
    def __init__(self,patente,idPedido,cantPedidos,Eta,Trm,precio): #ingreso patente,idPedido,cantPedidos,ETA,TRM,precio
        self.__patente=patente
        self.__idPedido=idPedido
        self.__cantPedidos=cantPedidos
        self.__ETA=Eta
        self.__TRM=Trm
        self.__precio=precio
        
    def getPatente(self):
        return self.__patente
    
    def getId(self):
        return self.__idPedido
    
    def getCantPedidos(self):
        return self.__cantPedidos
    
    def getETA(self):
        return self.__ETA
    
    def getTRM(self):
        return self.__TRM
    
    def setTRM(self,entrega):
        """Metodo que retorna el tiempo real"""
        self.__TRM=entrega
        print('...Tiempo real de entrega modificado!')
        
    def getPrecio(self):
        return self.__precio
    
class GestorDeMoto:
    def leerDatos():
        archivo = open("datosMotos.csv")
        reader = csv.reader(archivo, delimiter=",")
        next(reader) #omito guardar encabezado
        lista=[]
        for fila in reader:
            patente=fila[0]
            marca=fila[1]
            nya=fila[2]
            km=(fila[3].replace(".",","))
            lista.append(fila)
            # print(fila)
        print(lista)
        # return(lista)
        
class GestorDePedido:
    def leerDatos():
        archivo = open("datosPedidos.csv")
        reader = csv.reader(archivo, delimiter=",")
        next(reader) #omito guardar encabezado
        lista=[]
        for fila in reader:
            patente=fila[0]
            idPedido=fila[1]
            cantPedidos=fila[2]
            ETA=fila[3]
            TRM=fila[4]
            precio=(fila[5].replace(".",","))
            lista.append(fila)
            # print(fila)
        print(lista)
        # return(lista)
        
    def nuevoPedido(lista): #patente,idPedido,cantPedidos,ETA,TRM,precio
        listaNuevo=[]
        num=1
        while num!=0:
            print("Ingrese los sig. datos: 0 para finalizar")
            listaNuevo= input("Patente: ")
            listaNuevo= input("Id pedido: ")
            listaNuevo= input("Cantidad articulos: ")
            listaNuevo= input("ETA: ")
            listaNuevo= input("TRM: ")
            listaNuevo= input("precio: ")
            listaNuevo.append(lista)
            input(num)
    
        
# Unpedido=GestorDePedido.leerDatos()
# Unpedido=GestorDeMoto.leerDatos()
# lista=[]
# unPedido=GestorDePedido.nuevoPedido(lista)
