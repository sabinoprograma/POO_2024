import json
from pathlib import Path
from GestorJugadores import GestorJugadores
from claseJugador import Jugador

class ObjectEncoder(object):
    __pathArchivo: object
    
    def __init__(self, pathArchivo):
        self.__pathArchivo=pathArchivo
        
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='GestorJugadores':
                jugadores=d['jugadores']
                manejador=class_()
                for i in range(len(jugadores)):
                    dJugador=jugadores[i]
                    class_name=dJugador.pop('__class__')
                    class_=eval(class_name)
                    atributos=dJugador['__atributos__']
                    unJugador=class_(**atributos)
                    manejador.agregarJugador(unJugador)
            return manejador
        
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
            
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario