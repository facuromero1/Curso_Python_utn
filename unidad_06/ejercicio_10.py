# Realice un programa que le ofrezca al usuario un menú de opciones que le permita ejecutar las
# siguientes acciones:
# Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].
# Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].
# Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000]
# y calcular el valor promedio de los números menores a 10.000.
# Cualquier otro número: Salir del programa.

import random

acumulador = 0
suma = 0
print("Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].")
print("Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].")
print("Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000].")
print("Cualquier otro número: Salir del programa.")
opciones = int(input("ingrese su opcion"))

if opciones == 1:
    while acumulador <= 1000:
        aleatorios = random.randint(0, 100000)
        suma += aleatorios
        acumulador += 1
    promedio = suma / 1000
    print(f"El promedio de los 1000 numeros aleatorios es {promedio}")

if opciones == 2:
    mayor_numero = 0

    while acumulador <= 10000:
        aleatorios = random.randint(0, 100000)
        acumulador += 1
        print(f"{aleatorios}")
        if aleatorios > mayor_numero:
            mayor_numero = aleatorios
    print(f"{mayor_numero}")

if opciones == 3:
    menor_numero = 10
    while acumulador < 5000:
        aleatorios = random.randint(1, 100000)
        acumulador += 1
        print(f"{aleatorios}")
        if aleatorios < menor_numero:
            menor_numero = aleatorios
    print(f"{menor_numero}")
