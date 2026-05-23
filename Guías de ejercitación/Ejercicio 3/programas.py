

class Programa:
  __Nombre:str
  __codigo:str
  __duracion:int
  
  def __init__(self, nombre, codigo, duracion):
        self.__Nombre = nombre
        self.__codigo = codigo
        self.__duracion = duracion
        
    #Getters
  def get_nombre(self):
        return self.__Nombre
  def get_codigo(self):
        return self.__codigo
  def get_duracion(self):
        return self.__duracion
    
  def __str__(self):
        return f"Nombre Programa: {self.__Nombre} - Codigo: {self.__codigo} - Duracion: {self.__duracion}"
