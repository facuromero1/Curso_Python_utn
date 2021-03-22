# Escribir un programa que permita leer la canƟdad de números enteros ingresados por el usuario
# y calcular lo siguiente:
# El segundo menor
# El promedio de los números posiƟvos.
# El mayor de los números negaƟvos.
mayor_negativo = 0
segundo_menor = 0
numero_menor = ""
numero = ""
numero_total_positivos = 0
total_suma_positivos = 0
promedio = 0
n = int(input("Ingrese la cantidad de nros. a procesar: "))

for i in range(n):
    numero = int(input("ingrese el numero"))

    if numero > 0:
        numero_total_positivos += 1
        total_suma_positivos += numero
    else:
        if mayor_negativo == 0:
            mayor_negativo = numero
        elif mayor_negativo > numero:
            mayor_negativo = numero

    if i == 0:
        numero_menor = numero

    elif i == 1:
        if numero < numero_menor:
            segundo_menor = numero_menor
            numero_menor = numero
        else:
            segundo_menor = numero
    else:
        if numero < numero_menor:
            segundo_menor = numero_menor
            numero_menor = numero
        elif numero < segundo_menor:
            segundo_menor = numero

if total_suma_positivos > 0:
    promedio = total_suma_positivos / numero_total_positivos

print(f"(el mayor numero negativo es: {mayor_negativo})\nEl segundo numero menor es: {segundo_menor}")
print(f"(el promedio de los numeros positivos es de: {promedio})")
