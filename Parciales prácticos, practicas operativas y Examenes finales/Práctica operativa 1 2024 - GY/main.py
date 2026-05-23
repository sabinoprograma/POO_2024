from GestorClientes import GestorClientes
from GestorMovimientos import GestorMovimientos
import csv

if __name__ == '__main__':
    gc = GestorClientes()
    gc.testClientes()
    gm = GestorMovimientos()
    gm.testMovimientos()
    opcion = input("""      Ingresar alguna de las siguientes opciones:
        1_Ingresar dni de cliente y mostrar un listado de sus datos, los movimientos y el importe actualizado
        2_Ingresar dni e informar cliente que no tuvo movimientos durante el mes de abril 2024. 
        3_Ordenar el gestor por numero de cuenta de menor a mayor
        4_Mostrar Lista de clientes
        5_Mostrar Lista de movimientos
        0_salir
        --> """)
    while opcion != "0":
        if opcion == "1":
            xdni = int(input("Ingrese el DNI del cliente: "))
            listaM = gm.getListaMovimientos()
            gc.actualizarSaldo(listaM, xdni)
        elif opcion == "2":
            otrodni = int(input("Ingrese el dni: "))
            listMovimientos = gm.getListaMovimientos()
            gc.informarMovimientos(listMovimientos, otrodni)
        elif opcion == "3":
            gc.ordenar()
            gc.mostrarClientes()
        elif opcion == "4":
            gc.mostrarClientes()
        elif opcion == "5":
            gm.mostrarMovimientos()
        else:
            print("Opcion incorrecta")
        opcion = input("""      Ingresar alguna de las siguientes opciones:
        1_Ingresar dni de cliente y mostrar un listado de sus datos, los movimientos y el importe actualizado
        2_Ingresar dni e informar cliente que no tuvo movimientos durante el mes de abril 2024. 
        3_Ordenar el gestor por numero de cuenta de menor a mayor
        4_Mostrar Lista de clientes
        5_Mostrar Lista de movimientos
        0_salir
        --> """)
    