from lista.claseHija1 import *
from lista.claseHija2 import *
from lista import Lista

def test():
    try:    
        opcion = int(input("""
                            Menu de opciones
            Ingrese opcion: 
            1_Insertar al final objetos
            2_Mostrar elementos insertados al final.
            3_Mostrar Clientes Nacionales
            0_Para finalizar
            ----->""")) 
    except ValueError:
        print(f"Ingrese un valor numerico del menú de opciones.")
    return opcion 
        
if __name__ == '__main__':
    lista = Lista()
      
    op = test()
    while op is not None and op != 0:
        if op == 1:
            tipo = int(input("Ingrese el tipo: [1] [2] [0]salir):"))
            if tipo == 1:
                nombre = input("ingrese :")
                apellido = input("ingrese :")
                email = input("ingrese :")
                contra = input("ingrese :")
                direccion = input("ingrese :")
                tel = input("ingrese : ")
                prov = input("ingrese : ")
                loca = input("ingrese :")
                cod = input("ingrese :")
                cliente = ClienteNacional(nombre, apellido, email, contra, direccion, tel, prov, loca, cod)
                lista.agregar_por_cola(cliente)
            elif tipo == 2:
                nombre = input("ingrese :")
                apellido = input("ingrese :")
                email = input("ingrese :")
                contra = input("ingrese :")
                direccion = input("ingrese :")
                tel = input("ingrese : ")
                cliente = ClienteLocal(nombre, apellido, email, contra, direccion, tel)
                lista.agregar_por_cola(cliente)
        elif op == 2:
            lista.mostrardatos_agregado()
        elif op == 3:
            lista.mostrarnacionales()
        elif op==4:
            pos=int(input("ingrese una pos para buscar tipo de calefactor:"))
            lista.buscar_por_indice(pos-1)
        elif op==5:
            lista.motrarlistado_electrico()
        elif op==6:
            lista.motrarlistado_promo()
        op=test()
        

