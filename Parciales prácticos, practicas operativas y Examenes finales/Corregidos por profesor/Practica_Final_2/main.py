#!/usr/bin/env python

from gestorMedios import gestorMedios

def menu():
    while True:
        try:
            opcion = int(input("""
                                    Menu de Opciones
                        1- Cargar medio nuevo por teclado
                        2- Buscar programa
                        3- Mostrar información de cada medio (nombre, audiencia estimada e índice de audiencia)
                        0- Salir
                        --> """))
            return opcion
        except ValueError:
            print("Opción incorrecta: Debe ingresar un numero del menu de opciones.")


if __name__ == "__main__":
    gm = gestorMedios()
    print("Cargando archivos...")
    gm.cargarDatosMedios()
    gm.cargarDatosProgramas()
    print("Archivos cargados con exito!")
    opcion= menu()
    while opcion !=0:
        if opcion == 1: #Agregar por teclado
            try:
                tipo= input("Ingrese tipo de medio (prensa o radio): ")
                gm.agregarManual(tipo)
            except TypeError as e:
                print(f"Error: {e}")
        elif opcion == 2:
            try:
                nombre_programa= input("Ingrese nombre de programa: ")
                resultado = gm.buscarRadioPorPrograma(nombre_programa)
                print(resultado)
            except Exception as e:  #capturo el error exception y lo imprimo con la varible "e"
                print(f"[Error {e}]")
        elif opcion == 3:
            gm.mostrarInfoMedios()
        else:
            print("Opción incorrecta")
        opcion= menu()