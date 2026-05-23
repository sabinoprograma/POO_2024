from CuentaCampus import CuentaCampus
class Profesor:
    __dni: int
    __apellido: str
    __nombre: str
    __cargo: str
    __cuentaCampus: object

    def __init__(self, dni, apellido, nombre, cargo, cuenta):       #En la composicion el constructor es SIEMPRE el metodo que crea los objetos. NO PASAR COMO PARAMETRO, SI NO ES AGREGACION
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__cargo = cargo
        self.__cuentaCampus = cuenta

    def __str__(self):
        return f"DNI: {self.__dni}\nApellido {self.__apellido}\nNombre {self.__nombre}\nCargo {self.__cargo}\nDatos cuenta:\n{self.__cuentaCampus.getIdUsuario()}\n"
    
    def __del__(self):                                      #Cuando se destruye el todo, se deben destruir las partes
        print("Se borra el objeto profesor")
        del self
    

    def getDni(self):
        return self.__dni
    

