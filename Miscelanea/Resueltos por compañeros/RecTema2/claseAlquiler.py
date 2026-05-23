class alquiler:
    __nomPersona:str
    __ideCancha:str
    __hora:int
    __minutos:int
    __duracion:int

    
    def __init__(self,nomP,ideC,hora,min,duracion):
        self.__nomPersona=nomP
        self.__ideCancha=ideC
        self.__hora=hora
        self.__minutos=min
        self.__duracion=duracion
    
    def __str__(self):
        return "%s    %s    %d: %d     %d"%(self.__nomPersona,self.__ideCancha,self.__hora,self.__minutos,self.__duracion)
    
    def getHora(self):
        return self.__hora

    def getMinutos(self):
        return self.__minutos

    def getDuracion(self):
        return self.__duracion
    
    def getIdeCancha(self):
        return self.__ideCancha

    def getHoraMin(self):
        return "%s:%s"%(self.__hora,self.__minutos)

    def __gt__(self,otro):
        if self.__hora > otro.getHora():
            return True
        elif self.__hora == otro.getHora():
            if self.__minutos > otro.getMinutos():
                return True