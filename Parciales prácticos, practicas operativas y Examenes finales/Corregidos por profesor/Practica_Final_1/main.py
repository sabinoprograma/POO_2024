#!/usr/bin/env python

from gestorRutas import gestorRutas
from gestorVehiculos import gestorVehiculos

def menu():
    while True:
        try:
            op = int(input("""
                                    Menu de Opciones
                        1-Agregar un nuevo vehiculo al Gestor.
                        2-Mostrar informacion de un vehiculo dada su matricula.
                        3-Indicar datos de cada vehiculo del Gestor.
                        4-Mostrar vehiculos.
                        5-Mostrar rutas.
                        0-Salir
                        --> """))
            return op
        except ValueError:
            print("Opción incorrecta: Debe ingresar un numero del menu de opciones.")


if __name__=='__main__':
    gv = gestorVehiculos()
    gr = gestorRutas()
    gr.cargarGestor()
    op = menu()
    while op != 0:
        if op == 1:
            try:
                gv.agregarNuevoVehiculo(gr)
            except IndexError:
                print(f"La ruta no existe.")
            except IOError:
                print(f"La ruta ya esta asignada a un camion.")
        elif op == 2:
            try:
                matricula= input("Ingrese una matricula de un vehiculo: ")
                gv.buscarMatricula(matricula)
            except Exception:
                print("No se encontro el vehiculo.")
        elif op == 3:
            gv.indicarDatos()
        elif op == 4:
            gv.mostrarVehiculos()
        elif op == 5:
            gr.mostrarRutas()
        else:
            print("Opcion Incorrecta.")
        op = menu()
        
""" lote de prueba:
1
1
AAA001
Suran
350
15
5
3
1
2
CCC001
Scania
550
15
30000
25000
100
0
1
2
CCC002
Volvo
650
20
35000
18000
101
0
1
1
AAA002
Corsa
150
30
5
2
"""