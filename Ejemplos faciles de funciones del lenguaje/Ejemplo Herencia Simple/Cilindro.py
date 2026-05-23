import math 
from Circulo import Circulo

class Cilindro(Circulo):
    __altura: float

    def __init__(self, radio, altura):
        super().__init__(radio)
        self. __altura = altura

    def __str__(self):
        return f"Cilindro\n Radio: {self.getRadio()}\n Altura: {self.__altura}\n Superficie: {self.superficie()}"

    def superficie(self):
        superficieLateral = math.pi * 2 * self.getRadio() * self.__altura
        superficieCirculo = super().superficie()
        return superficieLateral + 2*superficieCirculo
    
