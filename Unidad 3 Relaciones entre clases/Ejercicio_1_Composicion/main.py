#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Gestor import gestorHotel

def menu():
    while True:
        try:
            op = int(input("""
                                Bienvenido! seleccione opcion para continuar:
                        1- Agregar habitaciones al hotel.
                        2- Reservar una habitación.
                        3- Liberar una habitación.
                        4- Dado un tipo de habitación (sencilla, doble, suite), mostrar número y piso de las habitaciones de ese tipo.
                        5- Mostrar la cantidad de habitaciones libres por piso.
                        6- Para cada tipo de habitación mostrar el detalle asociado con el siguiente formato.
                        0- Salir
                        --> """))
            return op
        except ValueError:
            print("Opción incorrecta: Debe ingresar un numero del menu de opciones.")

if __name__ == "__main__":
    g1 = gestorHotel()
    g1.agregar_hoteles()
    op = menu()
    while op != 0:
        if op == 1:     #1. Agregar habitaciones al hotel. 
            try:
                nombre_hotel=input("Ingrese el nombre del hotel: ")
                g1.agregar_nueva_habitacion(nombre_hotel)
            except Exception as e:
                print(f"Error:{e}")
        elif op == 2:   #2. Reservar una habitación. 
            try:
                #g1.mostrar_lista()
                nombre_hotel=input("Ingrese el nombre del hotel: ")
                numero= int(input("Ingrese numero de habitacion a reservar: "))
                g1.reserva_hab(nombre_hotel,numero)
            except Exception as e:
                print(f"Error: {e}")
        elif op == 3:    #3. Liberar una habitación.
            try:
                nombre_hotel=input("Ingrese el nombre del hotel: ")
                numero= int(input("Ingrese numero de habitacion a liberar: "))
                g1.libera_hab(nombre_hotel, numero)
            except Exception as e:
                print(f"Error: {e}")
        elif op == 4:    #4. Dado un tipo de habitación (sencilla, doble, suite), mostrar número y piso de las habitaciones de ese tipo.
            try:
                tipo = input("Ingrese tipo: sencilla, doble o suite: ")
                g1.mostrar_habitaciones_tipo(tipo)
            except Exception as e:
                print(f"Error: {e}")
        elif op == 5:     #5. Mostrar la cantidad de habitaciones libres por piso.
            try:
                g1.mostrar_libres()
            except Exception as e:
                print(f"Error: {e}")
        elif op == 6:       #6. Para cada tipo de habitación mostrar el detalle asociado con el siguiente formato.
            try:
                g1.mostrar_detalle()
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Opcion Incorrecta.")
        op = menu()