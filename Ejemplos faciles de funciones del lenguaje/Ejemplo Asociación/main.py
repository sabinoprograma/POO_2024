from Gobernador import Gobernador
from Provincia import Provincia 
if __name__ == '__main__':
    prov1 = Provincia("San Juan", 670456)
    gob1 = Gobernador(14564936, "Marcelo Orrego", prov1)
    prov1.setGobernador(gob1)
    print(gob1)
    print(prov1)