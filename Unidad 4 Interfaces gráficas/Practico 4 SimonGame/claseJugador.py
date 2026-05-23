class Jugador:
    __jugador: str
    __fecha: str
    __hora: str
    __puntaje: int
    __dificultad: str
    
    def __init__(self, jugador, fecha, hora, puntaje, dificultad):
        self.__jugador=jugador
        self.__fecha=fecha
        self.__hora=hora
        self.__puntaje=puntaje
        self.__dificultad=dificultad
        
    def __str__(self):
        return "%s %s %s %s %s" % (self.__jugador, self.__fecha, self.__hora, self.__puntaje, self.__dificultad)
    
    def getJugador(self):
        return self.__jugador
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getPuntaje(self):
        return self.__puntaje
    
    def getDificultad(self):
        return self.__dificultad
    
    def __gt__(self, otro): #sobrecarga de operadores
        return self.__puntaje > otro.getPuntaje()
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                jugador=self.__jugador,
                fecha=self.__fecha,
                hora=self.__hora,
                puntaje=self.__puntaje,
                dificultad=self.__dificultad
            )
        )
        return d