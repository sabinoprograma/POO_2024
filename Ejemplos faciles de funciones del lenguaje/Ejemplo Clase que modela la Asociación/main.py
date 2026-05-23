from Medico import Medico
from Paciente import Paciente
from Prescripcion import Prescripcion

if __name__ == "__main__":
    med1 = Medico(23457612, 1745, "Reumatologia", "Veller", "Ignacio")
    pac1 = Paciente(15497486, "Gonzalez", "Andrea")
    print(med1)
    print(pac1)
    pres1 = Prescripcion("28/05/2024", "Rinitis", "Hexaler", "10 Comprimidos", "1 por dia", med1, pac1) #Cuando instancio una prescripcion, se generan los enlaces
    print(pres1)
