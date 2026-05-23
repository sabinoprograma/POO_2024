from publicacion import publicacion
import datetime as date
class LibroImpreso(publicacion):
    __nombre:str
    __fecha:str
    __cPaginas:int
    def __init__(self,titulo,categoria,precio,nombre,fecha,CP):
        super().__init__(titulo,categoria,precio)
        self.__nombre=nombre
        self.__cPaginas=CP
        self.__fecha=fecha
     
    def getNombre(self):
        return self.__nombre
    def getFecha(self):
        return self.__fecha
    def getCPaginas(self):
        return self.__cPaginas
    
    def mostrar(self):
        print(super().mostrar())
        print("Autor: {} Fecha: {} Cant. de paginas: {}".format(self.__nombre,self.__fecha,self.__cPaginas))

    def ImporteTotal(self):
        lista=self.__fecha()
        lista.split('/')
        today=date.today()
        año=today.year()
        porcentaje=(super().getPrecio()*(año-int(lista[2])))/100
        total=super().getPrecio()-porcentaje
        return total