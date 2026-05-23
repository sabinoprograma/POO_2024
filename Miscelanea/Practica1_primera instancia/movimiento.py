class Cmovimiento: # número de cuenta, fecha, descripción, tipo de movimiento (‘C’ – Crédito, ‘P’-Pago), importe
    __numCuenta:int
    __fecha:str
    __descripcion:str
    __tipoMov:str
    __importe:float

    def __init__(self,numCu,fecha,descrip,tipoM,imp):
        """Metodo constructor de cliente"""
        self.__numCuenta=numCu
        self.__fecha=fecha
        self.__descripcion=descrip
        self.__tipoMov=tipoM
        self.__importe=imp

    def getNumCuenta(self):
        """Metodo que retorna nombre"""
        return self.__numCuenta

    def getFecha(self):
        """Metodo que retorna apellido"""
        return self.__fecha

    def geDescripcion(self):
        """Metodo que retorna dni"""
        return self.__descripcion

    def getTipoMov(self):
        """Metodo que retorna num cuenta"""
        return self.__tipoMov

    def getImporte(self):
        """Metodo que retorna saldo anterior"""
        return self.__importe
    
    # def setTiempoReal(self,entrega):
    #     """Metodo que retorna el tiempo real"""
    #     self.__tiempoR=entrega
    #     print('...Tiempo real de entrega modificado!')
    
    # def __lt__(self,otro):
    #     """Sobrecarga del operador < para el ordenamiento"""
    #     #Lo usa internamente la funcion sorted
    #     return self.__patente < otro.getPatente()
