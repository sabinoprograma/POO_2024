class partida: 
    __nombre_del_rival: str
    __resultado: str
    __duracion_minutos: str
    
    def __init__(self,nombre_del_rival,resultado,duracion_minutos):
        self.__nombre_del_rival = nombre_del_rival
        self.__resultado = resultado
        self.__duracion_minutos = duracion_minutos
        
    def __str__(self):
        return f"Rival: {self.__nombre_del_rival}, Resultado: {self.__resultado}, Duracion: {self.__duracion_minutos}min"
    
    def get_nombre_del_rival(self):
        return self.__nombre_del_rival
    
    def get_resultado(self):
        return self.__resultado
    
    def get_duracion_minutos(self):
        return self.__duracion_minutos
    
    def get_victoria(self):
        if self.__resultado == "victoria":
            return 50
        else:
            return 0