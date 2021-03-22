#Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos
#entre ellos, en forma ascendente y descendente.


par_mayor = 0
menor_impar = 0
primer_impar = True

numero = int(input("ingrese un numero entre positivos(con 0 corta)"))

while numero != 0:
    paridad = numero % 2
    if paridad == 0:
        if numero > par_mayor:
            par_mayor = numero
    else:
        if primer_impar or numero < menor_impar:
            primer_impar = False
            menor_impar = numero

    numero = int(input("ingrese un numero entre positivos(con 0 corta)"))

if par_mayor != 0:
    print(f"El mayor de los numeros pares es: {par_mayor}")

else:
    print("no ingreso numeros pares")

if menor_impar == 0:
    print("no ingreso numeros impares")
else:
    print(f"el menor numero impar es: {menor_impar}")
