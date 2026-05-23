class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __lista_libros: list
    
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__lista_libros = []
        
    #Getters
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono
    def get_lista(self):
        return self.__lista_libros
    
    #Str
    def __str__(self):
        print(f"{self.__nombre}")
        
    #Inciso 1  
    def agregar_libro(self, nuevo_libro):
        self.__lista_libros.append(nuevo_libro)
        
    #Inciso 2
    def buscar_libro(self, nombre_libro):
        encontrado = False
        i = 0
        longitud = len(self.__lista_libros)
        
        while not encontrado and i < longitud:
            if self.__lista_libros[i].get_titulo() == nombre_libro:
                del self.__lista_libros[i]
                encontrado = True
            else:
                i+=1
                
    #Inciso 3
    def buscar_libro2(self, nombre_libro):
        encontrado = False
        i = 0
        longitud = len(self.__lista_libros)
        valor_retorno = None
        
        while not encontrado and i < longitud:
            if self.__lista_libros[i].get_titulo() == nombre_libro:
                autor = self.__lista_libros[i].get_autor()
                genero = self.__lista_libros[i].get_genero()
                print(f"Autor: {autor} - Género: {genero}")
                valor_retorno = i
                encontrado = True
            else:
                i+=1
        return valor_retorno
    
    #Inciso 4
    def mostrar_libros(self):
        for libro in self.__lista_libros:
            print(libro)