#!/usr/bin/python3
# Sumar los nombres repetidos en lista1 y lista2 usando un diccionario y mostrarlo por pantalla

lista1 = ['Ana', 'Luis', 'Pedro', 'Ana', 'Juan', 'Ana']
lista2 = ['Pedro', 'Luis', 'Ana', 'Pedro', 'Marta']

# Definimos el diccionario
diccionario = {}

# Recorre las listas y va guardando en el diccionario
for nombre in lista1 + lista2:
  if nombre in diccionario:
    # Si ya existe el nombre en el diccionario le sumamos 1
    diccionario[nombre] += 1
  else:
    # Si es la primera vez lo cargamos con el valor 1
    diccionario[nombre] = 1

# Recorremos el diccionario para mostrar el resultado
for nombre, cantidad in diccionario.items():
  if cantidad > 1:
    # Si sale mas de una vez
    print(f"{nombre}: {cantidad} veces")
  else:
    # Si solo esta una vez
    print(f"{nombre}: Sale una vez")
