"""
    DESCRIPCION DEL RETO:

    Crea una clase llamada "Circulo" que tenga un atributo "radio" y dos métodos: uno para calcular el área del círculo y otro para calcular la circunferencia del círculo. Puedes usar la constante pi de la librería math para hacer los cálculos.
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def display(self):
        print(f'El círculo con radio {self.radius} tiene un área de {self.area()} y un perímetro de {self.perimeter()}')

radio = Circle(5)

radio.display()