# Clase base Vehiculo
class Vehiculo:
	def __init__(self, marca, modelo, año):
		self.marca = marca
		self.modelo = modelo
		self.año = año

	def obtenerDescripcion(self):
		return f"{self.marca} {self.modelo} ({self.año})"

# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):
	def __init__(self, marca, modelo, año, numeroPuertas):
		super().__init__(marca, modelo, año)
		self.numeroPuertas = numeroPuertas

	def obtenerDescripcion(self):
		return f"{self.marca} {self.modelo} ({self.año}) - Puertas: {self.numeroPuertas}"

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
	def __init__(self, marca, modelo, año, cilindrada):
		super().__init__(marca, modelo, año)
		self.cilindrada = cilindrada

	def obtenerDescripcion(self):
		return f"{self.marca} {self.modelo} ({self.año}) - Cilindrada: {self.cilindrada}cc"

# Crear instancias y mostrar descripciones
coche1 = Coche("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Honda", "CBR600RR", 2022, 600)

print(coche1.obtenerDescripcion())
print(moto1.obtenerDescripcion())
