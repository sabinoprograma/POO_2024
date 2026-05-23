from claseCancha import cancha
import csv
import numpy as np
class gestor_cancha:
    __cantidad:int
    __dimension:int
    __incremento=3
    __canchas:np.ndarray
    
    def __init__(self,d,i=3):
        self.__cantidad=0
        self.__dimension=d
        self.__incremento=i
        self.__canchas=np.empty(self.__dimension,dtype=cancha)
    
    def agregarCancha(self,unaCancha):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__canchas.resize(self.__dimension)
        self.__canchas[self.__cantidad]=unaCancha
        self.__cantidad +=1
    
    def __str__(self):
        c=""
        for can in self.__canchas:
            c += str(can) + "\n"
        
        return c
    
    
    def testCancha(self):
        archivo=open('RecTema2\Canchas.csv')
        reader=csv.reader(archivo,delimiter=';')
        ban=True
        for fila in reader:
            if ban:
                "Saltear Cabecera"
                ban= not ban
            
            else:
                id=(fila[0])
                tipo=fila[1]
                importe=float(fila[2])
                unaCancha=cancha(id,tipo,importe)
                self.agregarCancha(unaCancha)
        archivo.close()
    
    
    def buscarImporte(self,xC):
        long = self.__cantidad
        i = 0
        ideBase = self.__canchas[i].getId()
        while i<long and xC != ideBase:
            i += 1
            ideBase = self.__canchas[i].getId()
        if xC == ideBase:
            imp = self.__canchas[i].getImporte()
            return imp