#!/usr/bin/python3

# Ocurre un error y lo muestro
""" try:
  tupla = (1,2,3)
  tupla_entero = int(tupla)
  print(tupla_entero)
except Exception as error:
  print(f"Error: {error}") """

# No ocurre un error pero lo mismo esta mal, fuerzo el error con raise
def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Se requieren dos numeros")
    return a + b

print(sumar("1", "2"))

# print(sumar(1.5, 2.5))
