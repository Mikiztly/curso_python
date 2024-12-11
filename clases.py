#!/usr/bin/python3

""" crear una clase "Persona" con atributos nombre y edad
Crear un metodo "cumpleaños" que aumente en 1 la edad de la persona cuando se invoque y mostrar la edad """
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1
        print(f"Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")

persona1 = Persona("Juan", 30)
persona1.cumpleaños()
persona1.cumpleaños()
persona1.cumpleaños()
print(f"{persona1.nombre} tiene {persona1.edad} años.")

persona2 = Persona("Pepe", 35)
persona2.cumpleaños()
persona2.cumpleaños()
persona2.cumpleaños()
persona2.cumpleaños()
print(f"{persona2.nombre} tiene {persona2.edad} años.")