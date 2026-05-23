from gestorCancha import gestor_cancha
from gestorAlquiler import gestor_alquiler
def test():
    Cancha=gestor_cancha(6)
    Alquiler=gestor_alquiler()
    
    print("--------------------------------------------------------------------------------")
    Cancha.testCancha()
    print("--------Canchas--------")
    print(Cancha)
    print("--------------------------------------------------------------------------------")
    Alquiler.testAlquiler()
    print("--------Alquileres--------")
    print(Alquiler)
    print("--------------------------------------------------------------------------------")
    
    print("---------MENU DE OPCIONES---------")
    print("a. Emitir un listado ordenado por hora y minutos con todos los alquileres registrados")
    print("b. Ingresar el identificador de una cancha y mostrar la cantidad total de minutos que estuvo alquilada")
    print("c. Salir")
    
    opcion=input("Ingrese Opción: ")
    
    while opcion != 'c':
        if opcion == 'a':
            Alquiler.ordena()
            Alquiler.mostrarAlquileres(Cancha)
        
        elif opcion == 'b':
            ideCancha=input("Ingrese Identificador de la Cancha: ")
            Alquiler.mostrarMinutos(ideCancha)  
            
            
            
        print("---------MENU DE OPCIONES---------")
        print("a. Emitir un listado ordenado por hora y minutos con todos los alquileres registrados")
        print("b. Ingresar el identificador de una cancha y mostrar la cantidad total de minutos que estuvo alquilada")
        print("c. Salir")
        opcion=input("Ingrese Opción: ")


if __name__=='__main__':
    test()
    print("\n")
    print("Fin del Programa")