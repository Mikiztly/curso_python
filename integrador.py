#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejercicio integrador creado por Mikiztly (Diego Casavilla)

Alumnos = []

print("Administración de alumnos")
print("-------------------------")

while True:
    print(
    """
        Menú de opciones
        -----------------------------------------------------
        Ingrese el número de la operación que desea ejecutar:
        1 - Añadir un alumno a la lista.
        2 - Ver la lista de alumnos.
        3 - Salir
        -----------------------------------------------------
    """)

    Opcion = input("Seleccione una opción: ")

    if Opcion == "1":
        Nombre = input("Ingrese el nombre del nuevo alumno: ")
        Cursos = input("Ingrse la cantidad de cuesos que tiene: ")
        Alumnos.append([Nombre,Cursos])

    elif Opcion == "2":
        if not Alumnos:
            print("No hay alumnos")
        else:
            print("Lista de alumnos:")
            for XLoop in Alumnos:
                if int(XLoop[1]) > 1:
                    print(f"{XLoop[0]} tiene {XLoop[1]} cursos")
                else:
                    print(f"{XLoop[0]} tiene {XLoop[1]} curso")

    elif Opcion == "3":
        print("Gracias por usar este programa...")
        break
    else:
        print("Opción incorrecta...")