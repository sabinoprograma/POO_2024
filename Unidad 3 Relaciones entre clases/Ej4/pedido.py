class moto:
    __patente:str
    __marca:str
    __nya:str
    __km:int
    
    def __init__(self,pate,marca,nya,km): # inicio los datos: patente, marca, nya, km
        self.__patente=pate
        self.__marca=marca
        self.__nya=nya
        self.__km=km
        
    def getPatente(self):
        return self.__patente
    
    def getMarca(self):
        return self.__marca
    
    def getNya(self):
        return self.__nya
    
    def getKm(self):
        return self.__km