from ActasNacimiento import ActasNacimiento

class RegistroCivil:
    __denominacion: str
    __domicilio: str
    __listaActas: list
    #Variables de clase
    __actaActual = 100
    __libroActual = 5

    def __init__(self, denominacion, domicilio):
        self.__denominacion = denominacion
        self.__domicilio = domicilio
        self.__listaActas = []
    def __str__(self):
        return f"Denominacion: {self.__denominacion} Domicilio {self.__domicilio}"

    @classmethod
    def getActaActual(cls):
        cls.__actaActual += 1       #Por que lo incrementa en 1?
        return cls.__actaActual    
    @classmethod
    def getLibroActual(cls):
        return cls.__libroActual
    def getDenominacion(self):
        return self.__denominacion
    def getDomicilio(self):
        return self.__domicilio
    
    def inscribirPersona(self, persona, fecha):
        numeroActa = self.getActaActual()
        libro = self.getLibroActual()
        acta = ActasNacimiento(fecha, libro, numeroActa, persona, self) #Se manda self como registro Civil
        self.__listaActas.append(acta)

    def mostrarActas(self):
        for acta in self.__listaActas:
            print(acta)

        