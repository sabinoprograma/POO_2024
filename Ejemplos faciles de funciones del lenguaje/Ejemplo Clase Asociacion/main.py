from RegistroCivil import RegistroCivil
from Persona import Persona

if __name__ == '__main__':
    registro1 = RegistroCivil("Registro Cuarta Zona", "Av. Cordoba y Urquiza")
    persona1 = Persona(39994996, "Yuste", "Gabriel")
    persona2 = Persona(40482105, "Amado", "Anahi")
    registro1.inscribirPersona(persona1, "07/05/1997")
    registro1.inscribirPersona(persona2, "05/06/1997")
    registro1.mostrarActas()




'''
+----------------+                        +---------------+
| RegistroCivil  |                        | Persona       |
|----------------|  1   inscribe>   1..*  |---------------|
| denominacion:  |<---------------------->| dni: int      |
| string         |           |            | apellido:     |
| domicilio:     |           |            | string        |
| string         |           |            | nombre:       |
| __init__(...)  |           |            | string        |
+----------------+           |            | __init__(...) |
                             |            +---------------+
                             |
                   +---------------------+
                   | ActaNacimiento      |
                   |---------------------|
                   |-fechaDeInscripcion: |
                   |-DateTime            |
                   |-numeroLibro: int    |
                   |-numeroActa: int     |
                   |-__init__(...)       |
                   +---------------------+

'''