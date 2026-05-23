from jugadores import jugadores
from partida import partida

class jugadores_equipo(jugadores):# De un jugador de equipo se registra,  además: su historial de parƟdas jugadas y rol dentro de equipo (soporte, líder, atacante, defensa). 
    __rol: str
    __lista_historial_partidas: list
    
    def __init__(self,nickname,juego,nivel,rol):
        super().__init__(nickname, juego, nivel)
        self.__rol = rol
        self.__lista_historial_partidas = [] #lista de partidas por composicion
        
    def __str__(self):
        return super().__str__() + f"Rol: {self.__rol}"
    
    def get_lista_partidas(self):
        return self.__lista_historial_partidas
    
    def get_rol(self):
        return self.__rol
    
    def agregar_partida(self,dato1, dato2, dato3): #se reciben los datos por parametro y crea el objeto por composicion
        dato = partida(dato1, dato2, dato3)
        #print(dato)
        self.__lista_historial_partidas.append(dato)
    
    def calculo_puntaje(self):
        total_victorias = 0
        total_minutos = 0
        for dato in self.__lista_historial_partidas:
            total_victorias += dato.get_victoria()
            total_minutos += int(dato.get_duracion_minutos())
        bonificacion_rol = self.get_bonificacion_rol()
        total = total_victorias + total_minutos + bonificacion_rol
        return total
    
    def get_bonificacion_rol(self):
        if self.__rol.lower() == "lider":
            return 100
        elif self.__rol.lower() == "atacante":
            return 75
        elif self.__rol.lower() == "defensor":
            return 60
        elif self.__rol.lower() == "soporte":
            return 50
        else:
            return 0