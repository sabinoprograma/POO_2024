from abc import ABC, abstractmethod

class jugadores(ABC): #nickname, juego y nivel (principiante, intermedio o profesional). Además, todos los jugadores pertenecen al mismo país de origen, “ArgenƟna”, por lo que este dato debe ser representado mediante una variable de clase en la clase Jugador. 
    __nickname: str
    __juego: str
    __nivel: str #principiante, intermedio y profesional
    __pais = "Argentina" #atributo de clase, se declara solo aca y se utiliza solo con classmethod

    def __init__(self,nickname,juego,nivel):
        self.__nickname = nickname
        self.__juego = juego
        self.__nivel = nivel

    def __str__(self):
        return f"Nickname: {self.__nickname}, Juego: {self.__juego}, Nivel: {self.__nivel}, Pais: {self.get_pais()} "
    
    def get_nickname(self):
        return self.__nickname
    
    def get_juego(self):
        return self.__juego
    
    def get_nivel(self):
        return self.__nivel
    
    @classmethod #metodo para obtener un atributo o variable de clase
    def get_pais(cls):
        return cls.__pais

    def get_base_por_nivel(self)->int:
        if self.__nivel == "principiante":
            return 100
        elif self.__nivel == "intermedio":
            return 200
        elif self.__nivel == "profesional":
            return 300
        else:
            return 0

    def obtener_puntaje(self):
        return self.get_base_por_nivel() + self.calculo_puntaje()
    
    @abstractmethod
    def calculo_puntaje(self)->float:
        pass
    