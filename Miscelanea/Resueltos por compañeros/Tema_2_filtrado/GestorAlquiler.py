from  ClassAlquiler import Alquiler 
from  ClassCancha import Cancha
import csv

class GestorDeAlquiler:
    __lista_alquiler: list
    
    def __init__(self):
        self.__lista_alquiler=[]
        
    def __str__(self):
        cadena=""
        for reserva in self.__lista_alquiler:
            cadena = cadena + str(reserva) + "\n"
        return cadena
    
    def agregar_alquiler(self,un_alquiler):
        self.__lista_alquiler.append(un_alquiler)
        
    def test_alquiler(self):
        archi = open('Alquiler.csv')
        reader = csv.reader(archi,delimiter = ";")
        next(reader) #omito guardar encabezado
        for fila in reader:
            self.agregar_alquiler(Alquiler(fila[0],fila[1],fila[2],fila[3],fila[4]))
        archi.close()
        
    def get_horario(self):
        for lista in self.__lista_alquiler:
            hora = lista.get_hora()
            min = lista.get_minuto()
            print(hora,":",min)
        #return hora
            
    def ordenar(self):
        self.__lista_alquiler.sort(reverse = self.__lista_alquiler)
    
    def emitir_listado(self,gestor_cancha):
        print(una.get_horario())
    
    def listar_cabañas(self,gestor_cancha):
            print("Emitiendo listado......")
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("Hora", "Id. cancha", "Duración alquiler", "Importe por hora", "Importe alquiler"))
            for i in range(len(self.__lista_alquiler)):
                hora = self.__lista_alquiler[i].get_hora()
                min = self.__lista_alquiler[i].get_minuto()
                id_cancha = self.__lista_alquiler[i].get_id_cancha()
                importe_diario = gestor_cancha.get_importe_diario(i) #def buscar importe?
                print(i)
                print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(hora,":",min,id_cancha,importe_diario))

# una=GestorDeAlquiler()
# una.test_reserva()
# una.ordenar()
#print(una.get_horario())