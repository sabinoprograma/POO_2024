class Cancha:
    __id_cancha: str
    __tipo_piso: str
    __importe_hora: float
    
    def __init__(self,id_cancha,tipo_piso,importe_hora) -> None:
        self.__id_cancha = id_cancha
        self.__tipo_piso = tipo_piso
        self.__importe_hora = importe_hora
    
    def get_Id(self):
        return self.__id_cancha
    
    def get_tipo_piso(self):
        return self.__tipo_piso
    
    def get_importe_hora(self):
        return self.__importe_hora