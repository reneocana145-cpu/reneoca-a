

# Clase Estudiante: practica 1
class Estudiante:
       def __init__(self, nombre, apellido, edad, curso):
              self.nombre = nombre
              self.apellido = apellido
              self.edad = edad
              self.curso = curso

       def obtenerNombreCompleto(self):
              return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Curso: {self.curso}"

       def mostrar_informacion(self):
              print("Nombre: {self.nombre}")
              print("Apellido: {self.apellido}")
              print("Curso: {self.curso}")

# Crear varias instancias de Estudiante
est1 = Estudiante("Ana", "García", 20, "Matemáticas")
est2 = Estudiante("Luis", "Pérez", 22, "Física")
est3 = Estudiante("María", "López", 19, "Química")

# Mostrar nombres completos
print(est1.obtenerNombreCompleto()) 
print(est2.obtenerNombreCompleto())
print(est3.obtenerNombreCompleto())
