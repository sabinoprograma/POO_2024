from GestorAlquiler import GestorDeAlquiler
from GestorCancha import GestorDeCancha

def menu(): #menu de opciones
    xopcion = int(input(
    """Ingrese un numero de la lista para ejecutar la accion:
    1- Obtener listado ordenado por hora
    2- Ingresa id de cancha y se muestra la cantidad de minutos alquilada
    0- Salir del programa
    """))
    return xopcion

if __name__=='__main__':
    cancha = GestorDeCancha(1,1)
    alquiler = GestorDeAlquiler()
    alquiler.test_alquiler()
    cancha.test_cancha()
    opcion = menu()
    
    while opcion != 0:
        if opcion == 1: #
            alquiler.listar_cabañas(cancha)
            opcion = menu()
        elif opcion == 2: #
            pass
        else:
            print("ERROR opción no valida")