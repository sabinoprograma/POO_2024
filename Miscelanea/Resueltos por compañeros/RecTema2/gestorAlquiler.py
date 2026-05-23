from claseAlquiler import alquiler
import csv

class gestor_alquiler:
    __listaAlquiler:list
    
    def __init__(self):
        self.__listaAlquiler=[]
    
    def agregarAlquiler(self,unAlquiler):
        self.__listaAlquiler.append(unAlquiler)
    
    def __str__(self):
        a=""
        for alqui in self.__listaAlquiler:
            a += str(alqui) + "\n"
        
        return a
    
    def testAlquiler(self):
        archivo=open('RecTema2\Alquiler.csv')
        reader=csv.reader(archivo,delimiter=';')
        ban=True
        for fila in reader:
            if ban:
                "Saltear Cabecera"
                ban= not ban
            else:
                cliente=fila[0]
                cancha=(fila[1])
                hora=int(fila[2])
                minutos=int(fila[3])
                duracion=int(fila[4])
                unAlquiler=alquiler(cliente,cancha,hora,minutos,duracion)
                self.agregarAlquiler(unAlquiler)
        archivo.close()
    
    def ordena(self):
        self.__listaAlquiler.sort(reverse=self.__listaAlquiler)
    
    def mostrarAlquileres(self,unaCancha):
        acum=0
        print("Hora     |   Id de Cancha  |  Duracion Alquiler  |  Importe Hora  |  Importe Alquiler ")
        for i in range (len(self.__listaAlquiler)):
            hora=self.__listaAlquiler[i].getHoraMin()
            ideC=self.__listaAlquiler[i].getIdeCancha()
            duracion=self.__listaAlquiler[i].getDuracion()
            minutos= duracion % 60
            imp=unaCancha.buscarImporte(ideC)
            impAlquiler=(duracion/60) * imp
            acum = acum + impAlquiler
            print(f""" {hora}    |       {ideC}          |    {int(duracion/60)}:{minutos}             |      {imp}         |    {impAlquiler}""")
        
        
        print("\n")
        print(f"                                                           Total Recaudado: {acum} ")
        print("--------------------------------------------------------------------------------------------------------")
    
    
    
    def mostrarMinutos(self,xTipo):
        acumMin=0
        for i in range (len(self.__listaAlquiler)):
            if xTipo == self.__listaAlquiler[i].getIdeCancha():
                acumMin = acumMin + self.__listaAlquiler[i].getDuracion()
        
        print("\n")
        print(f"La Cancha {xTipo} estuvo alquilada {acumMin} minutos")
        print("---------------------------------------------------------------")