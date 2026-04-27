class figura:
    def calcular_area(self): 
        pass
    def calcular_perimetro(self):
        pass
    def mostraer_informacion(self):
        return f"Area: {self.calcular_area()} - Perimetro: {self.calcular_perimetro()}"
    
class circulo(figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

circulo1 = circulo(5)
print(circulo1.mostraer_informacion())

class cuadrado (figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

cuadrado1 = cuadrado(4)
print(cuadrado1.mostraer_informacion())

class triangulo (figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        # Para simplicidad, asumimos que es un triángulo isósceles
        # y que los lados iguales son de longitud 'lado'
        lado = ((self.base / 2) ** 2 + self.altura ** 2) ** 0.5
        return self.base + 2 * lado

triangulo1 = triangulo(6,5)
print(triangulo1.mostraer_informacion())