from gestorCliente import gestorDeCliente
from gestorMovimiento import gestorDeMovimiento

if __name__=='main':
    unCliente=gestorDeCliente.nuevo()
    
def menu():
    """Menu de opciones"""
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Ingresa dia, numero e importe. Acumular para ese dia y sucursal
          [2] Ingresa sucursal. Calcular su total de facturacion
          [3] Ingresa dia. Mostrar sucursal que mas facturó ese dia
          [4] Calcular sucursal con menos facturacion durante la semana
          [5] Calcular el total facturado por todas las sucursales
          [0] SALIR
          -> """))
    return op
