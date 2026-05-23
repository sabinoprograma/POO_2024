from gestorEmpleado import GestorEmpleado
from gestorMatricula import GestorMatricula
from gestorPrograma import GestorPrograma




def menu_opciones():
    op = None
    try:
        op = int(input('''
                                                ------MENÚ DE OPCIONES------
                       
    (1) Informa la duración de todos los programas de capacitación en los que está matriculado un ID. 
    (2) Muestre el/los empleados matriculados en un mismo programa de capacitacion.
    (3) Informar aquellos Empleados que no han sido matriculados en ningún programa de capacitación.
    () -
    
    (0) SALIR DEL MENÚ
    Su opción --> '''))
    except ValueError:      # Ver esto
        print(f"Valor ingresado fue invalido")
    return op



if __name__ == '__main__':
    
    Ge=GestorEmpleado()
    Gp=GestorPrograma()
    Gm = GestorMatricula()
    
    try:
        
        Ge.cargar()
        Gp.cargar()
        Gm.cargar(Ge,Gp)
    except Exception as e:
            print(f"Error cargando las listas y/o clases: {e}") 
    opcion = menu_opciones()
    while opcion != 0:
      if opcion == 1:
            try:
                print(" ")
                ide= int((input("Ingrese el ID del empleado: ")))
                  # el método .title() sirve para capitalizar (convertir en mayúsculas) la PRIMERA LETRA de cada palabra.
                
                Gm.informa_programas_matriculados(ide)
                
            except AssertionError:
              print("ERROR - No existe un empleado con ese ID.")
      elif opcion == 2:
            try:
                print(" ")
                nombre = (input("Ingrese el nombre del programa de capacitacion: "))
                print(f"Programa de Capacitacion: {nombre.title()}")
                Gm.muestra_matriculados_programa(nombre)
                
                                  
            except AssertionError:
                print("ERROR - No existe un programa con ese nombre.")
        
      elif opcion == 3:
            try:
                
                
                Gm.muestra_no_matriculados(Ge)
                
            except AssertionError:
                print("-")
        
      #elif opcion == 4:
       #     try:
        #        print("\n")
         #       nombre= (input("Ingrese el nombre de la biblioteca que desea mostrar: "))
          #      muestra=Gh.mostrar(nombre)
            
           # except AssertionError:
            #    print("ERROR - No existe una biblioteca con el nombre ingresado.")
      
      
   
      
      
      
      else:
            print('''   
                                                ------OPCIÓN INVÁLIDA------''')
      opcion = menu_opciones()