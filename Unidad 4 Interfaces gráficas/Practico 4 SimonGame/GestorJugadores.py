from claseJugador import Jugador

class GestorJugadores:
    __listaJugadores: list
    
    def __init__(self):
        self.__listaJugadores=[]
        
    def agregarJugador(self, unJugador):
        self.__listaJugadores.append(unJugador)
        
    def mostrarJugadores(self):
        for jugador in self.__listaJugadores:
            print(jugador)
            
    def ordenar(self):
        self.__listaJugadores = sorted(self.__listaJugadores, reverse=True)
        
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            jugadores=[jugador.toJSON() for jugador in self.__listaJugadores]
        )
        return d
    
    def __iter__(self):
        return iter(self.__listaJugadores)