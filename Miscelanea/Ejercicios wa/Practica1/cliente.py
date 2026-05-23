class Ccliente: # nombre, apellido, dni, número de cuenta, saldo anterior.
    __nombre:str
    __apellido:str
    __dni:int
    __numeroCuenta:int
    __saldoAnterior:float

    def __init__(self,nom,ape,dni,numeroCuenta,saldoAnt):
        """Metodo constructor de cliente"""
        self.__nombre=nom
        self.__apellido=ape
        self.__dni=dni
        self.__numeroCuenta=numeroCuenta
        self.__saldoAnterior=saldoAnt

    def getNombre(self):
        """Metodo que retorna nombre"""
        return self.__nombre

    def getApellido(self):
        """Metodo que retorna apellido"""
        return self.__apellido

    def getComida(self):
        """Metodo que retorna dni"""
        return self._dni

    def getTiempoEstimado(self):
        """Metodo que retorna num cuenta"""
        return self.__numeroCuenta

    def getPrecio(self):
        """Metodo que retorna saldo anterior"""
        return self.__saldoAnterior
    
    # def setTiempoReal(self,entrega):
    #     """Metodo que retorna el tiempo real"""
    #     self.__tiempoR=entrega
    #     print('...Tiempo real de entrega modificado!')
    
    # def __lt__(self,otro):
    #     """Sobrecarga del operador < para el ordenamiento"""
    #     #Lo usa internamente la funcion sorted
    #     return self.__patente < otro.getPatente()
