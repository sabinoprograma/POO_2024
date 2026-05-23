import numpy as np #se importa la libreria numpy para realizar el ordenamiento

class alumno: #se definen la clase y los atributos a usar
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        
    def __add__(self,otro): #se crea el metodo add para sumar a traves de la sobrecarga de operadores
        return alumno(self.alumno+otro.alumno)
    
    def __repr__(self): #se crea el metodo repr para mostrar datos
        return f"Alumno: {self.nombre}, {self.edad}, {self.promedio}"
    
estudiantes = [ # Crear una lista de estudiantes
    alumno("Juan", 18, 6.5),
    alumno("María", 17, 9.0),
    alumno("Esteban", 20, 5),
    alumno("Jorge", 18, 9.2),
    alumno("Esteban", 20, 6.6),
]    
    
#Ordena los estudiantes por promedio utilizando un array Numpy
estudiantes_np = np.array(estudiantes)
indices_ordenados = np.argsort([estudiante.promedio for estudiante in estudiantes_np])
estudiantes_ordenados = estudiantes_np[indices_ordenados]

print("Estudiantes ordenados por promedio:") #Por ultimo imprime los resultados en manera de lista ordenada
for estudiante in estudiantes_ordenados:
    print(estudiante)