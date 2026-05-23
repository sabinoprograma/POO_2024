from Gestor import gestor
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,

                        }
    def opcion(self,op,GE):
        fun=self.__switcher.get(op,lambda:print("opcion no valida\n"))
        if op=='1' or op=='2' or op=='3' or op=='4' or op =='5':
            fun(GE)
        else:
            fun()
    def opcion1(self,GE):
        if type(GE)== gestor:
            GE.buscarEdicioxNombre(input("Ingrese el nombre del edificio\n"))
        else:
            print("los datos enviados no son validos")
    def opcion2(self,GE):
        if type(GE)== gestor:
            ind=(input("Ingrese el nombre del edificio"))
            GE.BuscarID(ind)
    def opcion3(self,GE):
        if type(GE)== gestor:
            prop=input("Ingrese el nombre del propietario\n")
            GE.buscarprop(prop.upper())
        else:
            print("los datos enviados no son validos")

    def opcion4(self,GE):
        try:
            if type(GE)== gestor:
                numero=int(input("Ingrese el numero de piso\n"))
                GE.buscarpiso(numero)
            else:
                print("los datos enviados no son validos")
        except ValueError:
            print("Se esparaba un numero")
        
    def opcion5(self,GE):
        if type(GE)== gestor:
            GE.mostrar()
        else:
            print("los datos enviados no son validos")

    def leer(self,GE):
        if type(GE)==gestor:
            GE.leer()
        else:
            print("los datos enviados no son validos")
