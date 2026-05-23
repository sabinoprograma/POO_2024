from jugadores import jugadores

class jugadores_individuales(jugadores):
    __modalidad_control: str
    __cantidad_de_torneos_ganados: int
    __medida_del_rendimiento: float

    def __init__(self,nickname,juego,nivel,modalidad_control,cantidad_de_torneos_ganados,medida_del_rendimiento):
        super().__init__(nickname,juego,nivel)
        self.__modalidad_control = modalidad_control
        self.__cantidad_de_torneos_ganados = cantidad_de_torneos_ganados
        self.__medida_del_rendimiento = medida_del_rendimiento
        
    def __str__(self):
        return super().__str__() + f"Modalidad de control: {self.__modalidad_control}, Cantidad de torneos ganados: {self.__cantidad_de_torneos_ganados}, Medida de rendimiento (rpm): {self.__medida_del_rendimiento}"
    
    def get_modalidad_control(self):
        return self.__modalidad_control
    
    def get_cantidad_de_torneos_ganados(self):
        return self.__cantidad_de_torneos_ganados
    
    def get_medida_del_rendimiento(self):
        return self.__medida_del_rendimiento
    
    def calculo_puntaje(self):
        torneos_ganados= self.get_cantidad_de_torneos_ganados()
        reacciones_por_min= self.get_medida_del_rendimiento()
        return (torneos_ganados*50)+(reacciones_por_min*2)