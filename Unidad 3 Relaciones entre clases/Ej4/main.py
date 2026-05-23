# import csv
from Gestor import GestorDeMoto
from Gestor import GestorDePedido

# archivo = open("datosMotos.csv")
# reader = csv.reader(archivo, delimiter=",")
# for fila in reader:
#     print(fila)

if __name__=='main':
    UnPedido=GestorDeMoto()
    UnPedido=GestorDePedido()
    ListaPedido=GestorDePedido.leerDatos()
    ListaMoto=GestorDeMoto.leerDatos()
    nuevoPedido=GestorDePedido.nuevoPedido(ListaPedido)