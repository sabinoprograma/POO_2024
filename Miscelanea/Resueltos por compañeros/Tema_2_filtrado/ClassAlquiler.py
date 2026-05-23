class Alquiler:
    __nombre_persona: str
    __id_cancha: str
    __hora: str
    __minuto: str
    __duracion_minutos: int
    
    def __init__(self,nombre_persona,id_cancha,hora,minuto,duracion_minutos):
        self.__nombre_persona = nombre_persona
        self.__id_cancha = id_cancha
        self.__hora = hora
        self.__minuto = minuto
        self.__duracion_minutos = duracion_minutos
        
    def __gt__(self,otro):
        if self.__hora > otro.get_hora():
            return True
        elif self.__hora == otro.get_hora():
            if self.__minuto > otro.get_minuto():
                return True
        
    def get_nombre(self):
        return self.__nombre_persona
    
    def get_id_cancha(self):
        return self.__id_cancha
    
    def get_hora(self):
        return self.__hora
    
    def get_minuto(self):
        return self.__minuto
    
    def get_duracion(self):
        return self.__duracion_minutos