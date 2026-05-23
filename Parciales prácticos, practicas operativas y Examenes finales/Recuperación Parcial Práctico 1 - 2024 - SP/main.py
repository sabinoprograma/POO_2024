from GestorMamas import GestorDeMama
from GestorNacimientos import GestorDeNacimiento

def menu(): #menu de opciones  Ingresar por teclado el DNI de una mamá, mostrar la siguiente información:
    xopcion = int(input(
    """Ingrese un numero de la lista para ejecutar la accion:
    1- Ingresar por teclado el DNI de una mamá, mostrar listado
    2- Mostrar mamás con parto multiple
    0- Salir del programa
    """))
    return xopcion

if __name__=='__main__':
    mama = GestorDeMama(1,5)
    mama.test_mama()
    nacimiento = GestorDeNacimiento()
    nacimiento.test_nacimiento()
    opcion = menu()
    while opcion != 0:
        if opcion == 1: #
            dni = int(input("Ingrese DNI: "))
            mama.muestra_listado(dni,nacimiento)
            opcion = menu()
        elif opcion == 2: #
            nacimiento.parto(mama)
            opcion = menu()
        else:
            print("ERROR opción no valida")