from clasePadre import Padre

class Hija2(Padre):
    __a1:str
    __a2:str
    __a3:str
    __a4:str
    __a5:str
    
    def __init__(self,a, b, c, d, e, a1,a2,a3,a4,a5):
        super().__init__(a,b, c, d, e)
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5
        
    def __str__(self):
        return super().__str__() + f" {self.__a1} {self.__a2} {self.__a3} {self.__a4} {self.__a5}"
    
    def geta1(self):
        return self.__a1
    
    def geta2(self):
        return self.__a2
    
    def geta3(self):
        return self.__a3
    
    def geta4(self):
        return self.__a4
    
    def geta5(self):
        return self.__a5

    def claseAbstracta(self):
        pass