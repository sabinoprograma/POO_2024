from manejadorbiblioteca import ManejadorBiblioteca

def main():
    gestorBiblioteca = ManejadorBiblioteca()
    gestorBiblioteca.cargar_desde_archivo()
    
    while True:
        print("""
              Menú de opciones:
              [1] Agregar libro
              [2] Eliminar libro
              [3] Mostrar nombre de biblioteca, autor y género dado un libro
              [4] Listar libros
              [0] Salir
              """)
        
        op = input("Ingrese opción: ")
        
        if op == "1":
            gestorBiblioteca.mostrar()
            nombre_biblioteca = input("Ingrese nombre de la biblioteca: ")
            i = gestorBiblioteca.buscar_biblioteca(nombre_biblioteca)
            if (i != None):
                print("Se encontró la biblioteca ingresada")
                titulo = input("Ingrese título del libro: ")
                autor = input("Ingrese autor del libro: ")
                isbn = input("Ingrese ISBN del libro: ")
                genero = input("Ingrese genero del libro: ")
                gestorBiblioteca.inciso_a(i, titulo, autor, isbn, genero)
                print("Se agregó correcamente el libro a la biblioteca ingresada.")
                gestorBiblioteca.mostrar()
            else:
                print(f"No se encontró la biblioteca '{nombre_biblioteca}'. Intente nuevamente")
        elif op == "2":
            nombre_biblioteca = input("Ingrese nombre de la biblioteca: ")
            i = gestorBiblioteca.buscar_biblioteca(nombre_biblioteca)
            if (i != None):
                print("Se encontró la biblioteca ingresada")
                nombre_libro = input("Ingrese nombre del libro: ")
                gestorBiblioteca.inciso_b(i, nombre_libro)
                gestorBiblioteca.mostrar()
                print("Libro eliminado")
            else:
                print(f"No se encontró la biblioteca '{nombre_biblioteca}'. Intente nuevamente")
        elif op == "3":
            nombre_libro = input("Ingrese título del libro: ")
            gestorBiblioteca.recorrer_biblioteca(nombre_libro)
        elif op == "4":
            print("Mostrando todos los libros disponibles")
            gestorBiblioteca.mostrar()
        elif op == "0":
            print("Saliendo...")
            return
        
if __name__ == "__main__":
    main()