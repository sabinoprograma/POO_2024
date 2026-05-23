from menu import menu
from lista import lista
if __name__ =='__main__':
    lis=lista()
    lis.cargar()
    unmenu=menu()
    print("Bienvenido")
    op=input("Ingrese la opcion que desea\n 1-Agregar un libro\n 2-Mostrar publicacion en una posicion\n 3-Mostrar la cantidad de publicaciones de cada tipo\n 4-Mostrar\n 0-Salir\n")
    while(op!='0'):
        unmenu.opcion(op,lis)
        op=input("Ingrese la opcion que desea\n 1-Agregar un libro\n 2-Mostrar publicacion en una posicion\n 3-Mostrar la cantidad de publicaciones de cada tipo\n 4-Mostrar\n 0-Salir\n")
    print("adios")

