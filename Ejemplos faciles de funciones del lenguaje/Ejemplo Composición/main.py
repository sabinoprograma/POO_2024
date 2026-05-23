from CuentaCampus import CuentaCampus
from Profesor import Profesor

if __name__ == "__main__":
    #profesor1 = Profesor(40482105,"Florencia", "Perez", "Interino Matematica")
    #profesor2 = Profesor(34565464,"Juan", "Perez", "Interino Fisica")
    profesor3 = Profesor(40482105,"Amado", "Anahi", "Interino Ingles")
    print(profesor3)
    print("Se elimina el objeto profesor:\n")
    del profesor3
    print("\nSe termina el programa")

