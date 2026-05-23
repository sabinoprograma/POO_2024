import math
class Circulo:
    __radio: float
    
    def __init__(self, radio):
        self.__radio = radio
    def __str__(self):
        return f"Circulo\n Radio: {self.__radio}\n Superficie: {self.superficie()}"
    
    def getRadio(self):
        return self.__radio

    def superficie(self):
        return math.pi * self.__radio**2
        
        