class cancha:
    __ide:str
    __tipoPiso:str
    __impHora:float
    
    
    def __init__(self,ide,tipoP,imp):
        self.__ide=ide
        self.__tipoPiso=tipoP
        self.__impHora=imp
    
    
    def __str__(self):
        return "%s    %s    %.2f"%(self.__ide,self.__tipoPiso,self.__impHora)
    
    
    def getId(self):
        return self.__ide
    
    def getImporte(self):
        return self.__impHora