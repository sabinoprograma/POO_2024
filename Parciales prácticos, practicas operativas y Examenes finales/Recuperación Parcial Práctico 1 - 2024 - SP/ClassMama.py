class Mama:
    __dni: int
    __edad: int
    __ayn:str
    
    def __init__(self,dni,edad,ayn):
        self.__dni = dni
        self.__edad = edad
        self.__ayn = ayn
        
    def __str__(self):
        return f"DNI: {self.__dni}"
    
    def get_dni(self):
        return self.__dni
        
    def get_edad(self):
        return self.__edad
        
    def get_ayn(self):
        return self.__ayn