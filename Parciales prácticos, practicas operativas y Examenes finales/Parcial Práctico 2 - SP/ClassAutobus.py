from ClassVehiculo import Vehiculo

class Autobus(Vehiculo):
    __tipo_servicio: str
    __turno: str
    
    def __init__(self,marca,modelo,año_fabri,cap_pasajeros,num_plazas,distancia_recorrida,tarifa_base,tipo_servicio,turno):
        super().__init__(marca,modelo,año_fabri,cap_pasajeros,num_plazas,distancia_recorrida,tarifa_base)
        self.__tipo_servicio = tipo_servicio
        self.__turno = turno

    def __str__(self):
        return f"Autobus --> {super().__str__()}, Tipo de Servicio: {self.get_tipo_servicio()}, Turno: {self.get_turno()}"
    
    def get_tipo_servicio(self):
        return self.__tipo_servicio
    
    def get_turno(self):
        return self.__turno
    
    def calcular_tarifa(self):
        tarifa_base = super().get_tarifa_base()
        if self.__turno == "noche" and self.__tipo_servicio == "turismo":
            return float(tarifa_base) * float(1.20)
        else:
            return float(tarifa_base) * float(1.05)