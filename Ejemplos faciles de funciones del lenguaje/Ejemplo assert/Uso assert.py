class Caracter:
    __caracter: str
    __bold: bool
    __italic: bool
    __undeline: bool

    def __init__(self, caracter, bold=False, italic=False, underline=False):
        assert len(caracter) == 1, "Debe ser un caracter culiao"
        self.__caracter = caracter
        self.__bold = bold
        self.__italic = italic
        self.__undeline = underline
        
    def __str__(self):
        bold = "*" if self.__bold else ""
        italic = "/" if self.__italic else ""
        underline = "_" if self.__undeline else ""
        return bold + italic + underline + self.__caracter

car1 = Caracter("sa", underline= True, italic= True)
print(car1)