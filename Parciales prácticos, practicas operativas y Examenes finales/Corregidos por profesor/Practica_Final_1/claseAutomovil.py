from claseVehiculo import Vehiculo

class Automovil(Vehiculo):
    __pMax: int #cantidad max de pasajeros
    __cantPJr: int #cantidad de pasajeros actual o real
    
    def __init__(self, matricula, modelo, costoxKM, cantDeDias ,pMax, cantPJr):
        super().__init__(matricula, modelo, costoxKM, cantDeDias) #Herencia implementada: hereda atributos de la superclase vehiculo
        self.__pMax = pMax
        self.__cantPJr = cantPJr
        
    def getPmax(self):
        return self.__pMax
    
    def getCantPJr(self):
        return self.__cantPJr
    
    def __str__(self):
        return f"Automovil: {super().__str__()}"
        
    def mostrarInfo(self):
        print("Matricula        Modelo          Costo por KM        Dias de Alquiler       Cantidad Maxima de Pasajeros             Cantidad real de Pasajeros Transportados")
        print (f"{super().getMatricula()}            {super().getModelo()}               {super().getCostoxKM()}                   {super().getCantDeDias()}                            {self.__pMax}                                          {self.__cantPJr}")
    
    def porcentaje(self):   #metodo abstracto y polimorfico
        return (5000 * self.__cantPJr)
    