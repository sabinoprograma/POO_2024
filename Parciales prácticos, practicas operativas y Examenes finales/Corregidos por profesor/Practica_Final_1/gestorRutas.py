from claseRuta import Ruta
import csv

class gestorRutas:
    __listaRutas: list
    
    def __init__(self):
        self.__listaRutas= []
        
    def agregarRuta(self, unaRuta):
        self.__listaRutas.append(unaRuta)
        
    def mostrarRutas(self):
        print("Listado de rutas: ")
        for rutas in self.__listaRutas:
            print (f"{rutas}")
            
    def cargarGestor(self):
        archivo = open('Rutas.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                if fila[3] == "FALSO":
                    rutaA=False
                elif fila[3] == "VERDADERO":
                    rutaA=True
                else:
                    rutaA=False
                #unaRuta = Ruta(int(fila[0]), fila[1], float(fila[2]), rutaA)
                self.agregarRuta(Ruta(int(fila[0]), fila[1], float(fila[2]), rutaA))
        archivo.close()
        
    def buscarRuta(self, cod):
        flag = False
        i = 0
        while flag is False and i<len(self.__listaRutas):
            if self.__listaRutas[i].getCod() == cod:
                flag = True
            else:
                i += 1
        if flag:
            if self.__listaRutas[i].getRutaA() == False:
                self.__listaRutas[i].setRutaA()
                return self.__listaRutas[i]
            else:
                raise IOError
        else:
            raise IndexError