from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# --- Bloque de prueba ---
if __name__ == "__main__":
    mi_circulo = Circulo(5)
    mi_rectangulo = Rectangulo(10, 4)

    print(f"Area del circulo: {mi_circulo.calcular_area():.2f}")
    print(f"Area del rectangulo: {mi_rectangulo.calcular_area()}")