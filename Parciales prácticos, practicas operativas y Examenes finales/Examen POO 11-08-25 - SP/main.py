#!/usr/bin/env python

from gestor_jugadores import lista

def menu():
    while True:
        try:
            op = int(input("""
                            Bienvenido! seleccione opcion para continuar:
                        1- Mostrar puntaje por valor ingresado.
                        2- Mostrar para todos los jugadores: nickname, tipo de jugador y su puntaje total.
                        3- Buscar jugador por nickname.
                        4- Ingresar indice de lista y agregar un jugador individual nuevo.
                        0- Salir.
                        --> """))
            return op
        except ValueError:
            print("Opcion incorrecta: Debe ingresar un numero del menu de opciones.")

if __name__ == "__main__":
    gestor = lista()
    op = menu()
    gestor.cargar_jugadores()
    while op != 0:
        if op == 1: #Item 1: Leer por teclado un valor de puntaje mínimo, y mostrar el nickname de los jugadores cuyo puntaje total sea igual o superior a dicho valor. 
            valor= int(input("Ingrese puntaje minimo para listar jugadores: "))
            gestor.mostrar_puntaje_mayor(valor)
        elif op == 2: #Item 2: Mostrar para todos los jugadores: nickname, tipo de jugador y su puntaje total.
            gestor.mostrar_por_instancia()
        elif op == 3: #Item 3: Buscar nickname de jugador y mostrar datos
            try:
                nickname_buscado= input("Ingrege el nickname para buscar: ").lower()
                gestor.buscar_jugador_por_nickname(nickname_buscado)
            except Exception as e:
                print(e)
        elif op == 4: #Item 4: leer por teclado los datos de un nuevo jugador individual
            try:
                pos = int(input("Ingrese la posicion para agregar un nuevo jugador individual: "))
                gestor.agregar_jugador_individual(pos)
            except IndexError as e:
                print(e)
            except ValueError as v:
                print(v)
        else:
            print("Opcion Incorrecta.")
        op = menu()