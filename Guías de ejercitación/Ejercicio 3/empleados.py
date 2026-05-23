

class Empleado:
  __NomyApel:str
  __IdEmp:str
  __Puesto:str
  
  def __init__(self,nombreyapellido,ide,puesto):
    self.__NomyApel=nombreyapellido
    self.__IdEmp=ide
    self.__Puesto=puesto
    
      #Getters
  def get_nya(self):
        return self.__NomyApel
  def get_id_empleado(self):
        return self.__IdEmp
  def get_puesto(self):
        return self.__Puesto
    
    #Str
  def __str__(self):
        return f"Nombre y Apellido: {self.__NomyApel} - Puesto: {self.__Puesto}"
    
  