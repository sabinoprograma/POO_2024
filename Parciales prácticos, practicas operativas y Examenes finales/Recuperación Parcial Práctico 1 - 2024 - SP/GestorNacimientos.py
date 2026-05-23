from ClassMama import Mama
from ClassNacimientos import Nacimiento
import csv

class GestorDeNacimiento:
    __lista_nacimientos: list
    
    def __init__(self):
        self.__lista_nacimientos=[]
        
    def __str__(self):
        cadena=""
        for nacimiento in self.__lista_nacimientos:
            cadena = cadena + str(nacimiento) + "\n"
        return cadena

    def agregar_nacimiento(self,una_reserva):
        self.__lista_nacimientos.append(una_reserva)
        
    def test_nacimiento(self):
        archi = open('Nacimientos.csv')
        reader = csv.reader(archi,delimiter = ";")
        next(reader) #omito guardar encabezado
        for fila in reader:
            self.agregar_nacimiento(Nacimiento(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))
        archi.close()
                
    def get_lista_bebes(self, dni):
        print("Peso:            Altura: ")
        for nacimiento in self.__lista_nacimientos:
            if dni == int(nacimiento.get_dni()):
                print(f"{nacimiento.get_peso()} kg             {nacimiento.get_altura()} cm")
                
    def parto(self,gestor_mama):
        fecha=input("Ingrese fecha: ")
        for nacimiento in self.__lista_nacimientos:
            if fecha == nacimiento.get_fecha():
                print("Peso:              Altura: ")
                print(f"{nacimiento.get_peso()}              {nacimiento.get_altura()}") #falto implementar el nombre por falta de tiempo :(
                

    def xparto(self, gestor_mama):
        fecha = input("Ingrese fecha: ")
        for nacimiento in self.__lista_nacimientos:
            if fecha == nacimiento.get_fecha():
                for mama in gestor_mama.get_mamas():
                    if mama.get_dni() == nacimiento.get_dni():
                        print(f"{mama.get_nombre()}")
                        break