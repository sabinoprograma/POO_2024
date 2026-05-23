class Reservas:
    __numero: int
    __nombre_huesped: str
    __numero_canaña_asignada:int
    __fecha_de_inicio_hospedaje:str
    __cantidad_huespedes:int
    __cantidad_dias:int
    __importe_seña:float

    def __init__(self,numero,nombre_huesped,numero_canaña_asignada,fecha_de_inicio_hospedaje,cantidad_huespedes,cantidad_dias,importe_seña):
        self.__numero=numero
        self.__nombre_huesped = nombre_huesped
        self.__numero_canaña_asignada = numero_canaña_asignada
        self.__fecha_de_inicio_hospedaje = fecha_de_inicio_hospedaje
        self.__cantidad_huespedes = cantidad_huespedes
        self.__cantidad_dias = cantidad_dias
        self.__importe_seña = importe_seña
        
    def __str__(self):
        return f"Numero de reserva: {self.__numero}     Nombre huesped: {self.__nombre_huesped}     Numero de la cabaña asignada: {self.__numero_canaña_asignada}       Fecha de inicio del hospedaje: {self.__fecha_de_inicio_hospedaje}       Cantidad de huespedes: {self.__cantidad_huespedes}      Cantidad de dias reservados: {self.__cantidad_dias}     Importe de la seña: {self.__importe_seña}"
    
    def get_numero_reserva(self):
        return self.__numero
    
    def get_nombre_huesped(self):
        return self.__nombre_huesped
    
    def get_numero_canaña_asignada(self):
        return self.__numero_canaña_asignada
    
    def get_fecha_de_inicio_hospedaje(self):
        return self.__fecha_de_inicio_hospedaje
    
    def get_cantidad_huespedes(self):
        return self.__cantidad_huespedes
    
    def get_cantidad_dias(self):
        return self.__cantidad_dias
    
    def get_importe_seña(self):
        return self.__importe_seña