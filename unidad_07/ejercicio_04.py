# Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos
# entre ellos, en forma ascendente y descendente.

numero_1 = int(input("ingrese el primer numero"))
numero_2 = int(input("ingrese el segundo numero"))

if numero_1 > numero_2:
    mayor = numero_1
    menor = numero_2
else:
    mayor = numero_2
    menor = numero_1



if menor % 2 == 0:
    inicio = menor + 1
else:
    inicio = menor

for i in range(inicio, mayor + 1, 2):
    print(f"imapares en forma acendente: {i}")

print("-" * 50)

if mayor % 2 == 0:
    inicio = mayor - 1
else:
    inicio = mayor

for i in range(inicio, menor -1, -2 ):
    print(f"impares en forma decendente: {i}")
