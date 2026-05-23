from claseAutomovil import Automovil
from claseCamion import Camion

class gestorVehiculos:
    __listaVehiculos: list
        
    def __init__(self):
        self.__listaVehiculos = []
        
    def agregarVehiculo(self, nuevoVehiculo):
        self.__listaVehiculos.append(nuevoVehiculo)
    
    def mostrarVehiculos(self):
        print("Lista de Vehiculos: ")
        for vehiculo in self.__listaVehiculos:
            print(f"{vehiculo}")

    def agregarNuevoVehiculo(self, gr):
        print("Seleccione el tipo de Vehiculo")
        op=int(input("1-[Auto] 2-[Camión] 0-[Salir]\n"))
        if op!=0:
            print("Ingrese datos: ")
            matricula= input("Matricula: ")
            modelo= input("Modelo: ")
            costoxKM= float(input("Costo por KM: "))
            cantDeDias= int(input("Cantidad de días de alquiler: "))
            
            if op==1:
                pMax = int(input("Numero maximo de pasajeros: "))
                cantPJr = int(input("Cantidad de pasajeros que viajaran: "))
                nuevoVehiculo = Automovil(matricula, modelo, costoxKM, cantDeDias, pMax, cantPJr)
                self.agregarVehiculo(nuevoVehiculo)
                
            elif op == 2:
                capMax= float(input("Capacidad máxima de carga: "))
                cargReal= float(input("Cantidad en KG de carga transportada: "))
                unCamion= Camion(matricula,modelo, costoxKM,cantDeDias,capMax,cargReal)
                cod = int(input("Ingrese codigo de ruta que recorrera... [Ingrese 0 para salir]"))
                while cod != 0:
                    unaRuta= gr.buscarRuta(cod)
                    unCamion.agregarRuta(unaRuta)
                    print("Ruta asignada correctamente!")
                    cod= int(input("Ingrese codigo de ruta que recorrera... [Ingrese 0 para salir]"))
                unCamion.mostrarRutas()
                self.agregarVehiculo(unCamion)
                
    def buscarMatricula(self, matricula):
        flag = False
        i = 0
        while flag is False and i<len(self.__listaVehiculos):
            if self.__listaVehiculos[i].getMatricula() == matricula:
                flag = True #flag = not flag
            else:
                i += 1
        if flag:
            self.__listaVehiculos[i].mostrarInfo()
        else:
            raise Exception
        
    def indicarDatos(self):
        print(f"{'Matricula':<20}{'Modelo':<20}{'Costo Total':<20}")
        for vehiculo in self.__listaVehiculos:
            print(f"{vehiculo.getMatricula():<20}{vehiculo.getModelo():<20}{vehiculo.calculoAlquiler():<20}")