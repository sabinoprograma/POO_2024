from CuentaCampus import CuentaCampus
from Profesor import Profesor

if __name__ == "__main__":
    idCuenta = CuentaCampus.getIdCuenta()
    dominio = CuentaCampus.getDominio()
    usuario = "anahiamado" + dominio
    cuenta1 = CuentaCampus(idCuenta, usuario, 40482105) #creo el objeto cuenta (parte)

    profesor3 = Profesor(40482105,"Amado", "Anahi", "Interino Ingles", cuenta1) #creo el objeto profesor(continente)

    print(profesor3)
    print("Se elimina el objeto profesor:\n")
    del profesor3
    print("\nSe termina el programa\n")

