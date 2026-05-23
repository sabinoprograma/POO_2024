class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __numCuenta: int
    __saldoAnterior: float
    
    def __init__(self, nom, ape, dni, numC, saldoA):
        self.__nombre = nom
        self.__apellido = ape
        self.__dni = dni
        self.__numCuenta = numC
        self.__saldoAnterior = saldoA
        
    def __str__(self):
        return "%s %s %s %s %s" % (self.__nombre, self.__apellido, self.__dni, self.__numCuenta, self.__saldoAnterior)
    
    def getNom(self):
        return self.__nombre
    
    def getApe(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def getNumC(self):
        return self.__numCuenta
    
    def getSaldoA(self):
        return self.__saldoAnterior
    
    def actualizarSaldo(self, tipo, imp):
        if tipo == "D":
            self.__saldoAnterior -= imp
        elif tipo == "C":
            self.__saldoAnterior += imp
            
    def __lt__(self, otro):
        return self.__numCuenta < otro.getNumC()