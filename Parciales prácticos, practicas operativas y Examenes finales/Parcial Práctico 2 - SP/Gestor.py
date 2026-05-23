from ClassAutobus import Autobus
from ClassVan import Van
from ClassVehiculo import Vehiculo
import csv

class GestorDeVehiculos:
    __lista: list
    
    def __init__(self):
        self.__lista=[]
    
    def __str__(self):
        cadena = ""
        for lista in self.__lista:
            cadena = cadena + str(lista) + "\n"
        return cadena
    
    def cargar(self):
        archi = open("vehiculos.csv")
        reader = csv.reader(archi,delimiter=';')
        next(reader)
        for fila in reader:
                tipo = fila[0]
                marca = fila[1]
                modelo = fila[2]
                aniofabri = fila[3]
                cappasaj = fila[4]
                nroplazas = fila[5]
                distancia = fila[6]
                tarifabase = fila[7]
                tiposerv = fila[8]
                if tipo == "A":
                    turno = fila[9]
                    unAutobus = Autobus(marca,modelo,aniofabri,cappasaj,nroplazas,distancia,tarifabase,tiposerv,turno)
                    self.agregar(unAutobus)
                elif tipo == "V":
                    unaVan = Van(marca,modelo,aniofabri,cappasaj,nroplazas,distancia,tarifabase,tiposerv)
                    self.agregar(unaVan)
        archi.close()
    
    def agregar(self,objeto):
        self.__lista.append(objeto)
        
    def mostrar_por_pos(self, pos):
        try:
            vehiculo = self.__lista[pos]
            if isinstance(vehiculo,Autobus):
                print(f"Posicion {pos}: es un Autobus")
            elif isinstance(vehiculo,Van):
                print(f"Posicion {pos}: es una Van")
            else:
                print(f"Posicion {pos}: Error tipo de vehículo desconocido")
        except IndexError:
            print(f"Posicion {pos} fuera de rango. Logitud de la lista: {len(self.__lista)}")
            
    def mostrar_cantidad_por_tipo(self):
        auto=0
        van=0
        for vehiculo in self.__lista:
            if isinstance(vehiculo, Autobus):
                auto+=1
            elif isinstance(vehiculo, Van):
                van+=1
        print(f"Cantidad de autobuses: {auto}")
        print(f"Cantidad de vans: {van}")
        
    def recorrer(self): # modelo, año de fabricación, capacidad de pasajeros y la tarifa del servicio
        print(f"{'Modelo:' :<30}{'Año de fabricacion:' :<30}{'Capacidad de pasajeros:' :<30}{'Tarifa de servicio:' :<30}")
        for vehiculo in self.__lista:   #recerro lista de vehiculos con la llamada del metodo de la superclase
            vehiculo.get_listado()