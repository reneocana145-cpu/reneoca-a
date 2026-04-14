class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: Guau")

    def comer(self):
       print(f"{self.nombre} come groquetas")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def jugar(self):
        print(f"{self.nombre} está jugando.")       

# Ejemplo de uso
mi_perro = Perro("Firulais", 3)
mi_perro.ladrar()
mi_perro.comer() 
mi_perro.dormir() 
mi_perro.jugar()
