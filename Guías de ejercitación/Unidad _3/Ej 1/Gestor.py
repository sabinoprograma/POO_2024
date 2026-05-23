from Edificio import edificio
import csv
class gestor():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def leer(self):
        archivo=open("C:\\Users\\PC\\Desktop\\Uni\\2° año\\2024\\Poo\\Practica\\Unidad 3\\Practica 1\\EdificioNorte.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        
        aux=0
        for fila in reader:
            if aux!= fila[0]:
                aux=fila[0]
                unedificio=edificio(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.__lista.append(unedificio)
            else :
                #Composicion
                self.__lista[int(aux)-1].cargar(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])

                #Agregacion
                #undepa=departamento(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
                #self.__lista[int(aux)-1].cargar(undepa)

        archivo.close()

    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            self.__lista[i].mostraredifios()
    def buscarEdicioxNombre(self,nombre):
        i=0
        long=len(self.__lista)
        while i<long and self.__lista[i].getNombre().upper()!=nombre.upper():
            i+=1
        
        if i<long:
            self.__lista[i].mostrarprop()
        else:
            print("No se encontro el edificio")

    def SuperficieTotal(self):
        long=len(self.__lista)
        for i in range (long):

            print("cantidad total de superficie en {}:{}".format(self.__lista[i].getNombre(),self.__lista[i].suptotal()))


    def BuscarID(self,ind):
        i=0
        while i< len(self.__lista) and self.__lista[i].getNombre().upper()!=ind.upper():
            i+=1
        if i <len(self.__lista):
            acum=self.__lista[i].suptotal()
            print ("la superficie total del edifcio{} es {}".format(self.__lista[i].getNombre(),acum))
        else: 
            print("No se encontro el edificio")
        
    def buscarprop(self,pro):
        band=None
        i=0
        while i<len(self.__lista) and band==None:
            band=self.__lista[i].buscarprop(pro)
            i+=1
        if band!=None:
            total=self.__lista[i].suptotal()
            print("La superficie del propietario {} es de {}m2, la cual representa el {}'%' del total({}m2)".format(pro,band,round((band*100)/total,2),total))
        else:
            print("No se encontro el propietario")
    def buscarpiso(self,numero):
        for i in range(len(self.__lista)):
            if self.__lista[i].getCantP()>=numero:
                print("En {} el piso {} posee los siguientes deptartamentos:\n".format(self.__lista[i].getNombre(),numero))
                total=self.__lista[i].buscarByD(numero)
                print("En total {} posee {} departamentoss con 3 dormitorios y mas de 1 baño\n".format(self.__lista[i].getNombre(),total))
            else:
                print("El {} no posee piso {}".format(self.__lista[i].getNombre(),numero))