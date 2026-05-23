from Orden import Orden
from Mozo import Mozo
from Bebida import Bebida
from Plato import Plato

if __name__ == '__main__':
    bebida1 = Bebida('Coca Cola','1/2 litro',750)
    bebida2 = Bebida ('Aquarius', '1/2 litro',500)
    bebida3 = Bebida('Sprite', '1 litro', 1200)
    bebida4 = Bebida('Fanta', '1/2 litro', 800)
    plato1 = Plato('Lomo especial',3250)
    plato2 = Plato('Pizza especial', 3900)
    plato3 = Plato('Hamburguesa completa', 2800)
    plato4 = Plato('Ensalada César', 2100)
    papas = Plato('Papa frita chica', 1250)
    mozo1 = Mozo (1, 'López', 'Carlos')

    pedido1 = Orden(1, mozo1, bebida1, plato1)
    pedido2 = Orden(2, mozo1, bebida2, plato2)
    pedido3 = Orden(3, mozo1, bebida3, plato3)
    pedido4 = Orden(4, mozo1, bebida4, plato4)

    pedido2.agregarBebida(bebida1, 2)
    pedido1.cerrarOrden()
    pedido2.cerrarOrden()
    pedido3.cerrarOrden()
    pedido4.cerrarOrden()

    # Ejemplo adicional para demostrar la agregación
    print(f"Mozo {mozo1.getNombre()} atendió {len([p for p in [pedido1, pedido2, pedido3, pedido4]])} órdenes")
    print(f"Bebida {bebida1.getDenominacion()} se vendió en múltiples órdenes")

#Los objetos PARTE mozo1, bebida1, plato1, etc existen independientemente del objeto TODO pedido1