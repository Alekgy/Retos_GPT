"""
    DESCRIPCION DEL RETO BASICO:

    Crea una clase llamada "Persona" que tenga los atributos "nombre" y "edad". La clase debe tener un método llamado "presentarse" que imprima un mensaje de la forma "Hola, mi nombre es {nombre} y tengo {edad} años".
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def presentation(self):
        print(f'Hola, mi nombre es {self.name} mi edad es {self.age}')

saludo = Person('Alejandro', 28)

saludo.presentation()