from GestorCabaña import GestorDeCabañas
from GestorReserva import GestorDeReserva

def menu(): #menu de opciones
    xopcion = int(input(
    """Ingrese un numero de la lista para ejecutar la accion:
    1- Ingresar cantidad de huespedes y listar las cabañas disponibles
    2- Emitir listado detallado ingresando fecha de reserva
    0- Salir del programa
    """))
    return xopcion

if __name__=='__main__':
    cabaña = GestorDeCabañas(1,5)
    cabaña.test_cabañas()
    reserva = GestorDeReserva()
    reserva.test_reserva()
    opcion = menu()
    while opcion != 0:
        if opcion == 1: #
            huespedes = int(input("Ingrese cantidad de huespedes: "))
            cabaña.mostrar_cabañas(huespedes, reserva)
            opcion = menu()
        elif opcion == 2: #
            reserva.listar_cabañas(cabaña)
            opcion = menu()
        else:
            print("ERROR opción no valida")