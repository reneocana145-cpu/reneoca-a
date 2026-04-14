# Clase Libro practica 2
class Libro:
	def __init__(self, titulo, autor, paginas):
		self.titulo = titulo
		self.autor = autor
		self.paginas = paginas

	def mostrarInfo(self):
		print(f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\n")

# Clase Biblioteca
class Biblioteca:
	def __init__(self):
		self.libros = []

	def agregarLibro(self, libro):
		self.libros.append(libro)
		print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

	def listarLibros(self):
		if not self.libros:
			print("La biblioteca está vacía.")
			return
		print("Libros en la biblioteca:")
		for libro in self.libros:
			libro.mostrarInfo()

# Instanciar libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("1984", "George Orwell", 328)
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

# Instanciar biblioteca
biblioteca = Biblioteca()

# Probar funciones
biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)
biblioteca.agregarLibro(libro3)

biblioteca.listarLibros()
