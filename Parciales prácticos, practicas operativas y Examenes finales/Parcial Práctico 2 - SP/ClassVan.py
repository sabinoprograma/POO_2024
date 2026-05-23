from ClassAutobus import Vehiculo

class Van(Vehiculo):
    __tipo_carroceria: str
    
    def __init__(self,marca,modelo,año_fabri,cap_pasajeros,num_plazas,distancia_recorrida,tarifa_base,tipo_carroceria):
        super().__init__(marca,modelo,año_fabri,cap_pasajeros,num_plazas,distancia_recorrida,tarifa_base)
        self.__tipo_carroceria = tipo_carroceria
        
    def __str__(self):
        return f"Van --> {super().__str__()}, Tipo de Carrocería :{self.get_tipo_carroceria()}"
    
    def get_tipo_carroceria(self):
        return self.__tipo_carroceria
    
    def get_tarifa_base(self):
        return super().get_tarifa_base()
    
    def calcular_tarifa(self):
        tarifa_base = super().get_tarifa_base()
        if self.__tipo_carroceria == "minivan":
            return float(tarifa_base) * float(0.90)
        else:
            return float(tarifa_base) * float(1.025)