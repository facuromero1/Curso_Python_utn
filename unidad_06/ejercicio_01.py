# Conteo de numeros negativos con ciclo While

a = 0
numero = int(input("ingrese un numero (o 0 para terminar)"))

while numero != 0:
    if numero < 0:
        a += 1
    numero = int(input("ingrese un numero (o 0 para terminar)"))

print(f"la cantidad de numeros negativos cargada es de {a}")


