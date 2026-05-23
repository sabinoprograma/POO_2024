from CuentaCampus import CuentaCampus
class Profesor:
    __dni: int
    __apellido: str
    __nombre: str
    __cargo: str
    __cuentaCampus: object

    def __init__(self, dni, apellido, nombre, cargo):       #En la composicion el constructor es SIEMPRE el metodo que crea los objetos. NO PASAR COMO PARAMETRO, SI NO ES AGREGACION
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__cargo = cargo
        idCuenta = CuentaCampus.getIdCuenta()
        dominio = CuentaCampus.getDominio()
        usuario = nombre.lower() + apellido.lower() + dominio
        self.__cuentaCampus = CuentaCampus(idCuenta, usuario, dni)

    def __str__(self):
        return f"DNI: {self.__dni}\nApellido {self.__apellido}\nNombre {self.__nombre}\nCargo {self.__cargo}\nDatos cuenta:\n{self.__cuentaCampus.getIdUsuario()}\n{self.__cuentaCampus.getUsuario()}\n"
    
    def __del__(self):                                      #Cuando se destruye el todo, se deben destruir las partes
        print("Borrando cuenta de usuario...")
        del self.__cuentaCampus

    def getDni(self):
        return self.__dni
    

