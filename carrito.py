# Clase Producto practica 2
class Producto:
    def __init__(self, nombre, precio, cantidadEnStock):
        self.nombre = nombre
        self.precio = precio
        self.cantidadEnStock = cantidadEnStock

    def __str__(self):
        return f"{self.nombre} (Precio: ${self.precio}, Stock: {self.cantidadEnStock})"

# Clase Carrito
class Carrito:
    def __init__(self):
        self.productos = []  # Lista de tuplas (Producto, cantidad)

    def agregarProducto(self, producto, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return
        if cantidad > producto.cantidadEnStock:
            print(f"No hay suficiente stock de {producto.nombre}. Stock disponible: {producto.cantidadEnStock}")
            return
        self.productos.append((producto, cantidad))
        producto.cantidadEnStock -= cantidad
        print(f"Agregado {cantidad} de {producto.nombre} al carrito.")

    def calcularTotal(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.precio * cantidad
        return total

# Demostración
if __name__ == "__main__":
    # Crear productos
    p1 = Producto("Manzana", 2.5, 10)
    p2 = Producto("Pan", 1.2, 5)
    p3 = Producto("Leche", 3.0, 8)

    # Crear carrito
    carrito = Carrito()

    # Mostrar productos
    print("Productos disponibles:")
    for p in [p1, p2, p3]:
        print(p)

    # Agregar productos al carrito
    carrito.agregarProducto(p1, 3)
    carrito.agregarProducto(p2, 2)
    carrito.agregarProducto(p3, 9)  # Intento de agregar más de lo disponible
    carrito.agregarProducto(p3, 5)

    # Mostrar total
    print(f"\nTotal a pagar: ${carrito.calcularTotal():.2f}")

    # Mostrar stock restante
    print("\nStock restante:")
    for p in [p1, p2, p3]:
        print(p)