from Persona import Persona
from Docente import Docente
from Alumno import Alumno
from Ayudante import Ayudante

if __name__ == "__main__":
    ayud1 = Ayudante(41987947, "Juarez", "Roberto", 3211, 90, "POO", 45968.85, "10/03/2020", 9.65, "LSI", "Bueno", 5)
    pers1 = Persona(3489576, "Pedro", "Fuentes")

    ayud1.mostrarDatos()
    print("-----------")
    pers1.mostrarDatos()
