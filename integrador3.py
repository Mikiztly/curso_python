#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejercicio integrador
"""
Una universidad desea crear un programa para contabilizar los cursos que
tiene cada alumno. Para ello debemos realizar primero una aplicación de 
consola la cual debe solicitar el nombre de un alumno y la cantidad de 
cursos en la que se encuentra inscripto. Estos dos valores deben 
almacenarse como una lista de dos elementos (el nombre y la cantidad de
cursos como un número entero) en una lista de alumnos.

Una vez hecho esto, debemos hacer que el programa, al iniciar, pregunte
cuál de las siguientes dos operaciones se debe realizar:
ingresar un alumno o ver la lista de alumnos ingresados. 

Ingrese el número de la operación que desea ejecutar:
1 - Ver la lista de alumnos.
2 - Añadir un alumno a la lista.
3 - Salir.
>>> 2
Ingrese el nombre del alumno: Pablo
Ingrese la cantidad de cursos: 3
¡El alumno fue añadido a la lista!

Ingrese el número de la operación que desea ejecutar:
1 - Ver la lista de alumnos.
2 - Añadir un alumno a la lista.
3 - Salir.
>>> 1
Lista de alumnos:
Pablo - 3 cursos

Ingrese el número de la operación que desea ejecutar:
1 - Ver la lista de alumnos.
2 - Añadir un alumno a la lista.
3 - Salir.
>>> 4
La opción ingresada no es correcta, vuelva a intentarlo.

Ingrese el número de la operación que desea ejecutar:
1 - Ver la lista de alumnos.
2 - Añadir un alumno a la lista.
3 - Salir.
>>> 3
¡Gracias por utilizar el programa!
"""
########### TO DO  ################################
"""
La lista de alumnos que habíamos creado en el módulo
anterior ahora debe ser un diccionario, en donde las claves
serán nombres de alumnos y los valores sus respectivas
cantidades de cursos.
Para esto deberemos modificar el código de las opciones 1
y 2 (agregar un nuevo alumno y ver la lista de alumnos).
La tercera opción será “Ver la cantidad de cursos de un
alumno”. Deberá solicitar el nombre de un alumno e
imprimir en pantalla el número de cursos que tiene
asociados como clave.
La cuarta opción es la de salir, como en la versión anterior. 

"""
####################################################

# alumnos = {"Tito":3, "Ana":5, "Hugo":11}

alumnos = {}

print("Administración de alumnos")
print("-------------------------")

while True:
	
	print(
	"""
		Menú de opciones
	*-----------------------------------*
		1. Ver la lista de alumnos
		2. Añadir un alumno a la lista
		3. Ver la cantidad de cursos de un alumno
		4. Salir
	*-----------------------------------*	
	""")
	
	opcion = input("Seleccione una opción: ")
	
	if opcion == "1":
		if not alumnos:
			print("No hay alumnos")
		else:
			print("Lista de alumnos:")
			for k,v in alumnos.items():
				print(f"{k} - {v} cursos")
			
			
	elif opcion == "2":
		nombre = input("Ingrese el nombre: ")
		cursos = int(input("Ingrese la cantidad de cursos: "))
		alumnos[nombre] = cursos
	
	elif opcion == "3":
		nombre = input("Ingrese el nombre: ")
		nombres = list(alumnos.keys())
		if nombre in nombres:
			print(f"El alumno {nombre} tiene {alumnos[nombre]} cursos")
		else:
			print(f"No existe el alumno {nombre}")
		
		
	elif opcion == "4":	
		print("Gracias por usar este programa...")
		break
	
		
	else:
		print("Opción incorrecta...")