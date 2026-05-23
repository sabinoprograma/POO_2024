class Superclase:
    __nombre: str
    __apellido: str

    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def __str__(self):
        return f"Superclase:\n Nombre: {self.__nombre}\n Apellido: {self.__apellido}"
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def hablar(self):
        print("Hola soy una Superclase")
    
class Subclase(Superclase):
    __numero: int

    def __init__(self, nombre, apellido, numero):
        super().__init__(nombre, apellido)
        self.__numero = numero

    def __str__(self):
        return f"Subclase:\n Nombre: {self.getNombre()}\n Apellido: {self.getApellido()}\n Numero: {self.__numero}"
    
    def hablar(self):
        print("Hola soy una Subclase")

    
objeto = Subclase("juan", "lopez", 4)
print(objeto)
objeto.hablar()
        
        