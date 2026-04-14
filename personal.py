# Clase Persona practica 5
class Persona:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def saludar(self):
		return f"Hola, soy {self.nombre} {self.apellido}"

# Clase Empleado que hereda de Persona
class Empleado(Persona):
	def __init__(self, nombre, apellido, idEmpleado, salario):
		super().__init__(nombre, apellido)
		self.idEmpleado = idEmpleado
		self.salario = salario

	def saludar(self):
		return f"Hola, soy {self.nombre} {self.apellido} y mi ID es {self.idEmpleado}"

	def calcularSalarioAnual(self):
		return self.salario * 12

# Demostración
persona1 = Persona("Juan", "Pérez")
empleado1 = Empleado("Ana", "García", "E123", 2500)

print(persona1.saludar())
print(empleado1.saludar())
print(f"Salario anual de {empleado1.nombre}: ${empleado1.calcularSalarioAnual()}")
