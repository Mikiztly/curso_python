#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejercicio integrador creado por Mikiztly (Diego Casavilla)

# Primero inicializo la lista
Alumnos = []

# Encabezado del menu
print("Administración de alumnos")
print("-------------------------")

# Comienzo el bucle hasta que el usuario quiera salir
while True:
    
    # Imprimo el menu
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

    # Le doy la entrada para que el usuario ingrese una opcion
    Opcion = input("Seleccione una opción: ")

    # Segun la opcion es la accion que debo hacer
    # Primero es para agregar alumos
    if Opcion == "1":
        Nombre = input("Ingrese el nombre del nuevo alumno: ")
        Cursos = input("Ingrse la cantidad de cuesos que tiene: ")
        Alumnos.append([Nombre,Cursos])
    # Segundo listar alumnos
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
    # Tercero es para salir
    elif Opcion == "3":
        print("Gracias por usar este programa...")
        break
    # Si pone cualquier cosa le digo que es incorrecto
    else:
        print("Opción incorrecta...")