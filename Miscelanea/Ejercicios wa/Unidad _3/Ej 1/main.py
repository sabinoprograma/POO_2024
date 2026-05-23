from Gestor import gestor
from Menu import menu

if __name__ =='__main__':
    ungestor=gestor()
    #ungestor.leer()
    unmenu=menu()
    unmenu.leer(ungestor)
    print("Bienvenido\n")
    op=input("Ingrese la opcion que desea\n1-Mostrar propietarios de un edificio.\n2-Mostrar la superficie total cubierta de un edificio.\n3-Mostrar la superficie total cubierta de su departamento e indicar que porcentaje representa del total de la superficie cubierta del edificio.\n4-Contar y mostrar la cantidad de departamentos que tienen 3 dormitorios y más de un baño\n5-Mostrar Datos\n0-Salir\n")
    while op!='0':
        unmenu.opcion(op,ungestor)
        op=input("Ingrese la opcion que desea\n1-Mostrar propietarios de un edificio.\n2-Mostrar la superficie total cubierta de un edificio.\n3-Mostrar la superficie total cubierta de su departamento e indicar que porcentaje representa del total de la superficie cubierta del edificio.\n4-Contar y mostrar la cantidad de departamentos que tienen 3 dormitorios y más de un baño\n5-Mostrar Datos\n0-Salir\n")

    print("adios")
    