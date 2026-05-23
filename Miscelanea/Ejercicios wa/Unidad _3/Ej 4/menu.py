from lista import lista
from LibroImpreso import LibroImpreso
from AudioLibro import AudioLibro
class menu():
    __switcher=None
    def __init__(self) -> None:
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,

        }
    def opcion(self,op,lis):
        if type (lis)==lista:
            fun=self.__switcher.get(op,lambda:print("dato erroneo"))
            if op=='1' or op=='2' or op=='3' or op=='4':
                fun(lis)
            else:
                fun()
        else: 
            print("parametro erroneo")
    def opcion2(self,lis):
        long=lis.longitud()
        posicion=int(input("la lista posee una longitud de {} ingrese un numero de 0 a {}->".format(long,long-1)))
        print(lis.obtener(posicion))
    def opcion1(self,lis):
        try:
            op=input("Que tipo de libro desea cargar\n 1-Adio Libro   2-Libro Impreso\n")
            while op!='2' and op !='1':
                print("Dato no valido\n")
                op=input("Que tipo de libro desea cargar\n 1-Adio Libro   2-Libro Impreso\n")
            print("Ingrese los datos los siguienstes datos\n")
            libro=None
            nombre=input("Nombre->")
            genero=input("Genero->")
            preciobase=input("Precio Base->")
            if op=='2':
                autor=input("Autor->")
                fecha=input("Fecha->")
                edicion=int(input("N° de Edicion->"))
                libro=LibroImpreso(nombre,genero,preciobase,autor,fecha,edicion)

            else :
                duracion=input("Duracion->")
                narrador=input("Narrador->")
                libro=AudioLibro(nombre,genero,preciobase,duracion,narrador)
            lis.agregar(libro)


        except ValueError:
            print("Se ingreseso un dato no valido")

    def opcion3(self,lis):
        lis.tipos()
    def opcion4(self,lis):
        lis.mostrar()
