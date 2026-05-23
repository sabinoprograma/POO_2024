from claseVehiculo import Vehiculo

class Camion(Vehiculo):
    __capMax: float #capacidad max de pasajeros
    __cargReal: float #carga real o actual de transporte
    __rutas: list
    
    def __init__(self, matricula, modelo, costoxKM, cantDeDias, capMax, cargReal):
        super().__init__(matricula, modelo, costoxKM, cantDeDias) #Herencia implementada: hereda atributos de la superclase vehiculo
        self.__capMax = capMax
        self.__cargReal = cargReal
        self.__rutas= []
        
    def __str__(self):
        return f"Camión: {super().__str__()}  Capacidad máxima de carga: {self.__capMax}  Cantidad en KG de carga transportada: {self.__cargReal}"
    
    def getCapMax(self):
        return self.__capMax
    
    def getCargReal(self):
        return self.__cargReal
    
    def agregarRuta(self,unaRuta):
        self.__rutas.append(unaRuta)
        
    def mostrarRutas(self):
        print("Listado de rutas")
        for ruta in self.__rutas:
            print(f"[{ruta}]")
    
    def mostrarInfo(self):
        print("Matricula        Modelo          Costo por KM        Dias de Alquiler        Capacidad Maxima de Carga       Cantidad real Transportada")
        print(f"{super().getMatricula()}            {super().getModelo()}              {super().getCostoxKM()}                     {super().getCantDeDias()}                       {self.__capMax}                            {self.__cargReal}")
        self.mostrarRutas()
    
    def porcentaje(self):   #metodo abstracto y polimorfico
        costoxKM = super().getCostoxKM()
        alquiler = 0
        if self.__cargReal > 4500:
            alquiler =  (costoxKM * 0.05) # calcula el 5%  retornar solo (costoxKM * 0.05)
        elif self.__cargReal <= 4500:
            alquiler =  (costoxKM * 0.02) # calcula el 2%   retornar solo (costoxKM * 0.02)
        return alquiler
    