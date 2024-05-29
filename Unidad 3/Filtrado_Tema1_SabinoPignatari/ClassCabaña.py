class Cabañas:
    __numero: int
    __cantidad_habitaciones: int
    __cantidad_camas_grandes:int
    __cantidad_camas_chicas:int
    __importe_por_dia:float

    def __init__(self,numero,cantidad_habitaciones,cantidad_camas_grandes,cantidad_camas_chicas,importe_por_dia):
        self.__numero = numero
        self.__cantidad_habitaciones = cantidad_habitaciones
        self.__cantidad_camas_grandes = cantidad_camas_grandes
        self.__cantidad_camas_chicas = cantidad_camas_chicas
        self.__importe_por_dia = importe_por_dia
        
    def __str__(self):
        return f"Numero: {self.__numero}    Cantidad de habitaciones: {self.__cantidad_habitaciones}    Cantidad de camas grandes: {self.__cantidad_camas_grandes}  Cantidad de camas chicas: {self.__cantidad_camas_chicas}    Capacidad: {self.capacidad()}    Importe por dia: {self.__importe_por_dia}" 
    
    def __ge__(self, otra):
        return self.capacidad() >= otra
        
    def capacidad(self):
        return (self.__cantidad_camas_grandes * 2) + self.__cantidad_camas_chicas
        
    def get_numero_cabaña(self):
        return self.__numero
    
    def get_cantidad_habitaciones(self):
        return self.__cantidad_habitaciones
    
    def get_cantidad_camas_grandes(self):
        return self.__cantidad_camas_grandes
    
    def get_cantidad_camas_chicas(self):
        return self.__cantidad_camas_chicas
    
    def get_importe_por_dia(self):
        return self.__importe_por_dia
    