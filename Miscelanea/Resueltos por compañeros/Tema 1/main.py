#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dr-malito 22
#
# Created:     20/05/2024
# Copyright:   (c) Dr-malito 22 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from cabana import Cabana
from reserva import Reserva
from gestorcabana import GestorCabana
from gestorreserva import GestorReserva
def main():
    gescab=GestorCabana()
    gesres=GestorReserva()
    gescab.Carga()
    gesres.carga()
    while True:
        print("Bienvenido: ingrese una opcion")
        print("1. Buscar cabañas por cantidad de huespedes")
        print("2. Generar listado por fecha ")
        print("3. Guardar en un archivo reservas por fecha")
        print("4. Salir")

        opcion=int(input("Ingrese opción:\n"))
        if opcion==1:
            numero=int(input('Ingrese numero de huespedes '))
            gescab.buscar_por_capacidad(numero,gesres)
        elif opcion==2:
            fecha=input('Ingrese Fecha ')
            gesres.listar_por_fecha(fecha,gescab)
        elif opcion ==3:
            fecha = input("Ingrese una fecha (formato dd/mm/aaaa): ")
            archivo = input("Ingrese el nombre del archivo CSV donde guardar el listado: ")
            archivo+=".csv"
            gesres.guardar_listado_por_fecha(fecha, gescab, archivo)

        elif opcion==4:
            break


if __name__ == '__main__':
    main()

