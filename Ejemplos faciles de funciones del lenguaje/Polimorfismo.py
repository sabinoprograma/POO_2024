from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio=radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

class Rectangulo(Figura):
    def __init__(self, l1, l2):
        self.l1=l1
        self.l2=l2

    def calcular_area(self):
        return self.l1*self.l2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        return (self.base*self.altura)/2
    
    
figuras = [
    Circulo(float(input("Ingrese radio del Circulo: "))),
    Rectangulo(float(input("Ingrese lado 1 del Rectangulo: ")), float(input("Ingrese lado 2 del Rectangulo: "))),
    Triangulo(float(input("Ingrese base del Triangulo: ")), float(input("Ingrese altura del Triangulo: ")))
]
    
for figura in figuras:
    nombre = type(figura).__name__  # obtiene "Circulo", "Rectangulo", etc.
    print(f"Área del {nombre}: {figura.calcular_area()}")
