import numpy as np
import csv
from ClassCabaña import Cabañas
from ClassReserva import Reservas

class GestorDeReserva:
    __lista_reserva: list
    
    def __init__(self):
        self.__lista_reserva=[]
        
    def __str__(self):
        cadena=""
        for reserva in self.__lista_reserva:
            cadena = cadena + str(reserva) + "\n"
        return cadena
    
    def agregar_reserva(self,una_reserva):
        self.__lista_reserva.append(una_reserva)
        
    def test_reserva(self):
        archi = open('Reservas.csv')
        reader = csv.reader(archi,delimiter = ";")
        next(reader) #omito guardar encabezado
        for fila in reader:
            self.agregar_reserva(Reservas(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6]))
        archi.close()
    
    def listar_cabañas(self,gestor_cabaña):
        fecha_ingresada = input("Ingrese fecha para listar: ")
        if self.verificar_fecha(fecha_ingresada):
            print(f"Mostrando reservas para la fecha {fecha_ingresada}: ")
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("N° de cabaña", "Importe diario", "Cantidad de días", "Seña", "Importe a cobrar"))
            for lista in self.__lista_reserva:
                if fecha_ingresada == lista.get_fecha_de_inicio_hospedaje():
                    numero_cabaña = int(lista.get_numero_canaña_asignada())
                    importe_diario = gestor_cabaña.get_importe_diario(numero_cabaña)
                    cantidad_dias = int(lista.get_cantidad_dias())
                    seña = float(lista.get_importe_seña())
                    importe_a_cobrar = (cantidad_dias*importe_diario)-seña
                    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(numero_cabaña, importe_diario, cantidad_dias, seña, importe_a_cobrar))
                    #10/6/2024
        else:
                    print("Error fecha incorrecta")
                    
    def verificar_fecha(self,fecha):
        for reserva in self.__lista_reserva:
            if fecha == reserva.get_fecha_de_inicio_hospedaje():
                return True
        return False
    
    def verifica_reserva(self, numero_cabaña):
        for reserva in self.__lista_reserva:
            if numero_cabaña == int(reserva.get_numero_canaña_asignada()):
                return False
        return True