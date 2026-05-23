from claseHabitacion import Habitacion

class Hotel:
    __habitaciones: list
    __nombre: str
    __direccion: str
    __telefono: int
    
    def __init__(self, nombre, direccion, telefono):
        self.__habitaciones= []
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        
    def __str__(self):
        return f"Nombre: {self.__nombre}, Direccion: {self.__direccion}, Telefono: {self.__telefono}"
    
    def crear_habitacion(self, numero, piso, tipo, precio_noche, disponibilidad):     #numero, piso, tipo, precio_noche, disponibilidad
        nueva = Habitacion(numero, piso, tipo, precio_noche, disponibilidad)  #composición: el Hotel la crea
        self.__habitaciones.append(nueva)
        
    def get_habitaciones(self):
        return self.__habitaciones
    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_direccion(self):
        return self.__direccion
    
    def cantidad_habitaciones(self):
        return len(self.__habitaciones)

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono
        
    def buscar_habitacion(self, numero):
    # Retorna la habitación o None
        pass
    
    def reservar_habitacion(self, numero):
        flag = False
        i = 0
        print(f"[Reservando habitacion numero {numero}]")
        while flag is False and i < self.cantidad_habitaciones():
            habitacion_actual = self.__habitaciones[i]
            if habitacion_actual.get_numero() == numero:
                if habitacion_actual.get_disponibilidad_bool() == True:  # Verifico que esté disponible para reservarla /bool True= disponible, False= no disponible
                    habitacion_actual.reservar()
                    flag = True
                else:
                    raise Exception("la habitacion ya se encuentra reservada")
            else:
                i+=1
        if flag:
            print("Habitacion reservada!")
        else:
            raise AttributeError("la habitacion no existe")
        
    def liberar_habitacion(self, numero):
        flag = False
        i = 0
        print(f"-"*50)
        while flag is False and i < self.cantidad_habitaciones():
            habitacion_actual = self.__habitaciones[i]
            if habitacion_actual.get_numero() == numero:
                if habitacion_actual.get_disponibilidad_bool() == False:  # Verifico que esté disponible para reservarla /bool True= disponible, False= no disponible
                    habitacion_actual.liberar()
                    flag = True
                else:
                    raise Exception("la habitacion ya se encuentra libre")
            else:
                i+=1
        if flag:
            print("Habitacion liberada!")
        else:
            raise AttributeError("la habitacion no existe")
        
    def get_habitaciones_disponibles_por_piso(self, nombre_hotel):  #5- Mostrar la cantidad de habitaciones libres por piso.
        cant_total=0
        print(f"{nombre_hotel}")
        print(f"-"*70)
        print(f"{"Piso":<19} {"Habitaciones libres"}")
        for piso in range(1, self.get_cant_pisos()+ 1):
            cant_por_piso=0
            for habitaciones in self.__habitaciones:
                if habitaciones.get_disponibilidad_bool() == True and piso == habitaciones.get_piso():
                    cant_por_piso+=1
                    cant_total+=1
                    #print(f"{habitaciones.get_numero():<20} {habitaciones.get_piso():<20}")
            print(f"{piso:<20}{cant_por_piso:<20}")
        if cant_total <= 0:
            raise Exception("el hotel no tiene habitaciones libres")
        
    def get_cant_pisos(self):
        cant_pisos=0
        for pisos in self.__habitaciones:
            cant_pisos = max((cant_pisos, pisos.get_piso()))
        return cant_pisos
    
    def mostrar_listado(self, nombre_hotel): # Para cada tipo de habitación mostrar el detalle asociado con el siguiente formato
        cuenta_tipo=0
        print(f"{nombre_hotel}")
        print(f"-"*70)
        for tipo in ['sencilla','suite','doble']:
            print(f"Tipo de habitacion {tipo}:")
            for habitacion in self.__habitaciones:
                if habitacion.get_tipo() == tipo.lower():
                    cuenta_tipo+=1
                    print(f"{habitacion.get_numero():<20} {habitacion.get_piso():<20} {habitacion.get_precio_noche():<20} {habitacion.get_disponibilidad():<20}")
        if cuenta_tipo <=0:
            raise AttributeError("Ninguna habitacion disponible para ese tipo")