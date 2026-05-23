#Herencia simple
class Persona: #clase simple
    def __init__(self,edad,nombre,nacionalidad):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        
    def ejemplo(self):
        print("Este es un metodo ejemplo")
        
class Empleado(Persona): #ejemplo herencia simple
    def __init__(self, edad, nombre, nacionalidad, trabajo, salario):
        super().__init__(edad, nombre, nacionalidad)
        self.__trabajo = trabajo
        self.__salario = salario
        
    def ejemplo(self):
        print("METODO EJEMPLO SOBREPUESTO")
        
class Artista: #clase simple
    def __init__(self,habilidad):
        self.__habilidad = habilidad
        
    def mostrar_habilidad(self,nombre):
        print(f"Hola soy {nombre} y mi habilidad es: {self.__habilidad}")
        
class EmpleadoArtista(Empleado,Artista): #ejemplo herencia multiple
    def __init__(self,nombre,edad,nacionalidad,habilidad,trabajo,salario,obras):
        Empleado.__init__(self, edad, nombre, nacionalidad, trabajo, salario)
        Artista.__init__(self,habilidad)
        self.__obras = obras
        
Juan = EmpleadoArtista("Juan",32,"argentino","pintar al oleo","programador", 90000, 102)
Juan.mostrar_habilidad("Juan")

