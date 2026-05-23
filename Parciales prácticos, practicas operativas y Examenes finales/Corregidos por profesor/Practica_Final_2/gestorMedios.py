from claseRadio import Radio
from clasePrensa import Prensa
#from clasePrograma import Programa
from datetime import datetime
import csv

class gestorMedios:
    __listaMedios: list
    
    def __init__(self):
        self.__listaMedios= []
        
    def agregarMedio(self, unMedio):
        self.__listaMedios.append(unMedio)
    
    def buscarRadioPorFreq(self, freq):
        #print(f"Buscando frecuencia: '{freq}'")
        flag = False
        i = 0
        while flag is False and i < len(self.__listaMedios):
            if type(self.__listaMedios[i]) == Radio:    #equivalente a: if isinstance(self.__listaMedios[i], Radio):
                #print(f"Comparando con: '{self.__listaMedios[i].getFreq()}'")
                if self.__listaMedios[i].getFreq() == freq:
                    radios= self.__listaMedios[i]
                    return radios
            i += 1
        return None
    
    def buscarRadioPorPrograma(self, programa):
        flag = False
        i=0
        while flag is False and i < len(self.__listaMedios):
            if isinstance(self.__listaMedios[i], Radio):  #solo procesar si es radio / linea equivalente a: if type(self.__listaMedios[i]) == Radio:
                programas = self.__listaMedios[i].getProgramas()
                j=0
                while flag is False and j < len(programas):
                    if programas[j].getNombre().lower() == programa.lower():
                        radio = self.__listaMedios[i]
                        prog = programas[j]
                        return f"Medio: {radio.getNombre()} - Frecuencia: {radio.getFreq()} - Hora inicio: {prog.getInicio()}"
                    else:
                        j+=1
            i+=1
        raise Exception(f"programa {programa} no encontrado")
    
    def mostrarInfoMedios(self):
        print(f"{'Nombre':<20} {'Audiencia':<20} {'Índice':<20}")
        print("-" * 60)
        for medio in self.__listaMedios:
            print(f"{medio.getNombre():<20} {medio.getAudiencia():<20} {medio.calcularIndiceAudiencia():<20}")

    def validarHorarios(self, inicio, fin):
        if inicio < fin:
            return True
        else:
            return False
            
    def agregarManual(self, tipo):
        medio = None    #inicializar variable vacia par evitar errores
        if tipo.lower() in ["prensa", "radio"]:
            nombre= input("Ingrese nombre: ")
            audiencia= input("Ingrese audiencia: ")            
            if tipo.lower() == "prensa":
                periodicidad = input("Ingrese periodicidad: ")
                cantSecciones = input("Ingrese la cantidad de secciones: ")
                medio=Prensa(nombre,int(audiencia),periodicidad,int(cantSecciones))
            elif tipo.lower() == "radio":
                frecuencia=input("Ingrese frecuencia de Radio: ")
                medio=Radio(nombre,int(audiencia),frecuencia)
                op=input("Desea agregar programas? si/no ")
                while op.lower() == "si": #La manana lider,10:00,13:00
                    nombre=input("Ingrese nombre: ")
                    horaInicio=input("Ingrese hora inicio: ")
                    horaFin=input("Ingrese hora fin: ")
                    if self.validarHorarios(horaInicio, horaFin):
                        if medio:
                            medio.crearPrograma(nombre,horaInicio,horaFin)
                    else:
                        raise TypeError("horario invalido")
                    op=input("Desea agregar otro programa? si/no ")
            self.agregarMedio(medio)
        else:
            raise TypeError("tipo invalido")
            
    def cargarDatosMedios(self):
        archivo = open('Practica_Final_2/Medios.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if fila[0] == "P":
                self.agregarMedio(Prensa(fila[1], int(fila[2]), fila[3], int(fila[4])))
                #print(f"{fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}, {fila[4]}")
            elif fila[0] == "R":
                self.agregarMedio(Radio(fila[1], int(fila[2]), fila[3]))
                #print(f"{fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}")
        archivo.close()
        
    def cargarDatosProgramas(self):
        archivo = open('Practica_Final_2/Programas.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            #print(f"Fila leída: {fila}")
            radio = self.buscarRadioPorFreq(fila[0]) #fila[0] = frecuencia radio en el archivo
            try:
                horaInicio= datetime.strptime(fila[2], "%H:%M").time()
                horaFin= datetime.strptime(fila[3], "%H:%M").time()
                if self.validarHorarios(horaInicio, horaFin):
                    #programa= Programa(fila[1],horaInicio,horaFin) #1= nombre
                    if radio:
                        radio.crearPrograma(fila[1],horaInicio,horaFin)
                else:
                    print(f"Horario invalido de programa: {fila[1]} Inicio: {fila[2]} - Fin: {fila[3]}")
            except ValueError as e:
                print(f"Error de formato en horario del programa: {fila[1]}: {e}")
        archivo.close()

