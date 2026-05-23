class Nacimiento: #DNI;tipoParto;fecha;hora;pesobb;alturabb
    __dni_mama:int
    __tipo_parto:str
    __fecha:str
    __hora:str
    __peso:float
    __altura:float
    
    def __init__(self,dni_mama,tipo_parto,fecha,hora,peso,altura):
        self.__dni_mama = dni_mama
        self.__tipo_parto= tipo_parto
        self.__fecha =fecha
        self.__hora = hora
        self.__peso = peso
        self.__altura = altura
        
    def __str__(self):
        return f"DNI: {self.__dni}"  #completar
    
    def __eq__(self, otro):
            return self.__fecha == otro
    
    def get_dni(self):
        return self.__dni_mama
        
    def get_tipo(self):
        return self.__tipo_parto
        
    def get_fecha(self):
        return self.__fecha
    
    def get_hora(self):
        return self.__hora
    
    def get_peso(self):
        return self.__peso
    
    def get_altura(self):
        return self.__altura