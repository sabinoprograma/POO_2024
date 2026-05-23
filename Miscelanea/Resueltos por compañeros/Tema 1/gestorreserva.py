#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dr-malito 22
#
# Created:     20/05/2024
# Copyright:   (c) Dr-malito 22 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv
from reserva import Reserva
class GestorReserva:
    __reservas:list
    def __init__(self):
        self.__reservas=[]
    def agregarReseserva(self,Unareserva):
        self.__reservas.append(Unareserva)
    def carga(self):
        arch=open('Reservas.csv')
        reader=csv.reader(arch,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                numero=fila[0]
                nombre=fila[1]
                n_cabana=fila[2]
                fecha_inicio=fila[3]
                n_huespedes=fila[4]
                n_dias=fila[5]
                sena=fila[6]
                Unareserva=Reserva(numero,nombre,n_cabana,fecha_inicio,n_huespedes,int(n_dias),float(sena))
                self.agregarReseserva(Unareserva)
        arch.close()
    def reserva(self, numero):
        i=0
        while i <len(self.__reservas):
            if self.__reservas[i].getNumero() == numero:
                return True
            i+=1
        return False
    def listar_por_fecha(self,fecha,gestor_cabanas):
        i = 0
        print("Reservas para la fecha: ", fecha)
        print ("{:<15} {:<15} {:<15} {:<15} {:<15}".format("N° de cabaña","Importe diario", "Cantidad días",    "Seña" ,  "Importe a cobrar"))
        while i < len(self.__reservas):
            reserva = self.__reservas[i]
            if reserva.getFechainicio() == fecha:
                cabana = gestor_cabanas.buscar_por_numero(reserva.getNcabana())
                importe_a_cobrar = reserva.getNdias() * cabana.getImporte() - reserva.getSena()
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(reserva.getNcabana(), cabana.getImporte(), reserva.getNdias(), reserva.getSena(), importe_a_cobrar))
            i += 1

    def guardar_listado_por_fecha(self, fecha, gestor_cabanas, archivo):
        with open(archivo, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Número de cabaña", "Importe diario", "Cantidad días", "Seña", "Importe a cobrar"])
            i = 0
            while i < len(self.__reservas):
                reserva = self.__reservas[i]
                if reserva.getFechainicio() == fecha:
                    cabana = gestor_cabanas.buscar_por_numero(reserva.getNcabana())
                    if cabana is not None:
                        importe_a_cobrar = reserva.getNdias() * cabana.getImporte() - reserva.getSena()
                        writer.writerow([reserva.getNcabana(), cabana.getImporte(), reserva.getNdias(), reserva.getSena(), importe_a_cobrar])
                i += 1
