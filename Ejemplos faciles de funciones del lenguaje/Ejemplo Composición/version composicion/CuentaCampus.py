class CuentaCampus:
    #Variables de clase
    __dominio = "@unsj-cuim.edu.ar"
    __idCuenta = 0
    #Variables de instancia
    __idUsuario = int
    __nombreUsuario: str
    __clave: str

    @classmethod
    def getDominio(cls):
        return cls.__dominio
    @classmethod
    def getIdCuenta(cls):
        cls.__idCuenta += 1
        return cls.__idCuenta
    
    def __init__(self, idUsuario, nombreUsuario, clave):
        self.__idUsuario = idUsuario
        self.__nombreUsuario = nombreUsuario
        self.__clave = clave
    def __str__(self):
        return f"Usuario: {self.__nombreUsuario}\nClave: {self.__clave}"
    def cambiarClave(self, nuevaClave):
        self.__clave = nuevaClave
    def getUsuario(self):
        return self.__nombreUsuario
    def getIdUsuario(self):
        return self.__idUsuario
    
    def __del__(self):
        print("Se borro el objeto parte cuentacampus")
        del self