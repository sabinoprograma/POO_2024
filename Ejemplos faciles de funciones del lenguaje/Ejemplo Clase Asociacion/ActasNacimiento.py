

class ActasNacimiento:
    __fechaDeInscripcion: str
    __numeroLibro: int
    __numeroActa: int
    __persona: object           #Atributo que interrelaciona la clase asociación
    __registroCivil: object     #Atributo que interrelaciona la clase asociación

    def __init__(self, fechaDeInscripcion, numeroLibro, numeroActa, persona, registroCivil):
        self.__fechaDeInscripcion = fechaDeInscripcion
        self.__numeroLibro = numeroLibro
        self.__numeroActa = numeroActa
        self.__persona = persona
        self.__registroCivil = registroCivil

    def __str__(self) :
        return f"Fecha de Inscripcion: {self.__fechaDeInscripcion}\nLibro: {self.__numeroLibro} Acta: {self.__numeroActa}\n{self.__persona}\n"

    def getFechaInscripcion(self):
        return self.__fechaDeInscripcion
    def getNumeroLibro(self):
        return self.__numeroLibro
    def getNumeroActa(self):
        return self.__numeroActa
        

