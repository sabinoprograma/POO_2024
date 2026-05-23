from publicacion import publicacion
class AudioLibro(publicacion):
    __tiempo:int
    __narrador:str
    def __init__(self,titulo,categoria,precio,tiempo,narrador):
        super().__init__(titulo,categoria,precio)
        self.__tiempo=tiempo
        self.__narrador=narrador


    def getTiempo(self):
        return self.__tiempo
    def getNarrador(self):
        return self.__narrador
    def mostrar(self):
        print(super().mostrar())
        print("Tiempo: {}minutos Narrador: {}".format(self.__tiempo,self.__narrador))
    def ImporteTotal(self):
        total=super().getPrecio()+(super().getPrecio()*10/100)
        return total