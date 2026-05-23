#PARCIAL 2 PRACTICA - Hecho por Sabino Pignatari
from Gestor import GestorDeVehiculos

def menu():
    op = int(input("""Ingrese opcion:
1- Cargar vehículos a la colección
2- Mostrar por pantalla qué tipo de vehículo se encuentra almacenado en dicha posición
3- Mostrar la cantidad de vehículos de cada tipo
4- Recorrer la colección y mostrar para todos los Vehículos: modelo, año de fabricación, capacidad de pasajeros y la tarifa del servicio.
0- Cerrar programa\n"""))
    return op

if __name__=='__main__':
    op = menu()
    unVehiculo = GestorDeVehiculos()
    unVehiculo.cargar()
    if op == 1:
        print("Operacion realizada con exito")
        unVehiculo.cargar()
        
    elif op == 2:
        pos = int(input("ingrese la posicion en la lista: "))
        unVehiculo.mostrar_por_pos(pos)
        
    elif op == 3:
        unVehiculo.mostrar_cantidad_por_tipo()
        
    elif op == 4:   #4. Recorrer la colección y mostrar para todos los Vehículos: modelo, año de fabricación, capacidad de pasajeros y la tarifa del servicio.
        unVehiculo.recorrer()
        
    else: 
        print("Numero ingresado no corresponde\n")
    opcion = menu()