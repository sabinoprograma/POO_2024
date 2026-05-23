from abc import ABC,abstractmethod

class  Vehiculo(ABC):        #superclase
    __marca: str
    __modelo: str
    __año_fabri: int
    __cap_pasajeros: int
    __num_plazas: int
    __distancia_recorrida: float
    __tarifa_base: float
    
    def __init__(self,marca,modelo,año_fabri,cap_pasajeros,num_plazas,distancia_recorrida,tarifa_base):
        self.__marca = marca
        self.__modelo = modelo
        self.__año_fabri = año_fabri
        self.__cap_pasajeros = cap_pasajeros
        self.__num_plazas = num_plazas
        self.__distancia_recorrida = distancia_recorrida
        self.__tarifa_base = tarifa_base
        
    def __str__(self): 
        return f"Modelo:{self.__modelo}, Anio de fabricacion:{self.__año_fabri}, Capacidad pasajeros:{self.__cap_pasajeros}"
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_año_fabri(self):
        return self.__año_fabri
    
    def get_cap_pasajeros(self):
        return self.__cap_pasajeros
    
    def get_num_plazas(self):
        return self.__num_plazas
    
    def get_distancia_recorrida(self):
        return self.__distancia_recorrida
    
    def get_tarifa_base(self):
        return self.__tarifa_base
    
    @abstractmethod
    def calcular_tarifa(self)->float:
        pass
    
    def get_listado(self): # modelo, año de fabricación, capacidad de pasajeros y la tarifa del servicio
        print(f"{self.get_modelo():<30} {self.get_año_fabri():<30} {self.get_cap_pasajeros():<30} {self.calcular_tarifa():<30} ")