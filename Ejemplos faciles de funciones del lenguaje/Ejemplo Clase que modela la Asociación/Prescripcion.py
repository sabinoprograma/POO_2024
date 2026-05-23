
class Prescripcion:
    __fecha: str
    __diagnostico: str
    __medicamento: str
    __presentacion: str
    __dosis: str
    __paciente: object
    __medico: object

    def __init__(self, fecha, diagnostico, medicamento, presentacion, dosis, medico, paciente):
        self.__fecha = fecha
        self.__diagnostico = diagnostico
        self.__medicamento = medicamento
        self.__presentacion = presentacion
        self.__dosis = dosis
        self.__medico = medico          #Se agregan los objetos asociados con esta clase que modela
        self.__paciente = paciente      #Se agregan los objetos asociados con esta clase que modela
        self.__medico.addPrescripcion(self)
        self.__paciente.addPrescripcion(self)
    def __str__(self):
        return f"Fecha: {self.__fecha} Diagnistico: {self.__diagnostico} Medicamento {self.__medicamento} Presentacion: {self.__presentacion} Dosis: {self.__dosis}"
    
    def getFecha(self):
        return self.__fecha
    def getDiagnostico(self):
        return self.__diagnostico
    def getMedicamento(self):
        return self.__medicamento
    def getPresentacion(self):
        return self.__presentacion
    def getDosis(self):
        return self.__dosis

        

