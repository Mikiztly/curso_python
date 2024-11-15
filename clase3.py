#!/usr/bin/python3

# crearun programa que reciba dos numeros ingresados por el usuario
# verificar por medio de un try y un except que los datos sean numericos
# por medio de una funcion dividir los numeros y verificar por medio de try y except que el divisor no sea 0

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except TypeError:
        return "Error: Ingrese valores numéricos"

while True:
    try:
        num1 = float(input("Ingrese el dividendo: "))
        break
    except ValueError:
        print("Error: Ingrese valores numéricos")

while True:
    try:
        num2 = float(input("Ingrese el divisor: "))
        break
    except ValueError:
        print("Error: Ingrese valores numéricos")

resultado = dividir(num1, num2)
print("El resultado de la división es:", resultado)
