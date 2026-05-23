# class Habitacion:
#     __numero: str
#     __piso: int
#     __tipo: str
#     __precio_noche: float
#     __disponibilidad: bool
    
#     def __init__(self, numero, piso, tipo, precio_noche, disponibilidad):
#         self.__numero=numero
#         self.__piso=piso
#         self.__tipo=tipo
#         self.__precio_noche=precio_noche
#         self.__disponibilidad=disponibilidad
class Habitacion:
    __numero: int
    __piso: int
    __tipo: str
    __precio_noche: float
    __disponibilidad: bool

    def __init__(self, numero, piso, tipo, precio_noche, disponibilidad):
        self.__numero = numero
        self.__piso = piso
        self.__tipo = tipo
        self.__precio_noche = precio_noche
        self.__disponibilidad = disponibilidad
        
    def __str__(self):
        return f"Numero: {self.__numero}, Piso: {self.__piso}, Disponibilidad: {self.__disponibilidad}"

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_piso(self):
        return self.__piso

    def set_piso(self, piso):
        self.__piso = piso

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_precio_noche(self):
        return self.__precio_noche

    def set_precio_noche(self, precio_noche):
        self.__precio_noche = precio_noche

    def get_disponibilidad(self):
        if self.__disponibilidad == 1:
            return "libre"
        elif self.__disponibilidad == 0:
            return "ocupada"
        
    def get_disponibilidad_bool(self):
        return self.__disponibilidad

    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad = disponibilidad
        
    def reservar(self):
        if self.__disponibilidad:
            self.__disponibilidad = False
            return True
        return False
        
    def liberar(self):
        if not self.__disponibilidad:
            self.__disponibilidad = True
            return True
        return False