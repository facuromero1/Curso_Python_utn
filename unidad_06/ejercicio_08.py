#Ingresar una serie de números por teclado que representan la canƟdad de ventas realizadas en las
#diferentes sucursales de un país de una determinada empresa.
#Los requerimientos funcionales del programa son:
#Informar la canƟdad de ventas ingresadas.
#Total de ventas.
#CanƟdad de ventas cuyo valor este comprendido entre 100 y 300 unidades.
#CanƟdad de ventas con 400, 500 y 600 unidades.
#Indicar si hubo una canƟdad de ventas inferior a 50 unidades.
#Usted deberá ingresar canƟdades de ventas hasta que se ingrese un valor negaƟvo.
ventas_total = 0
cantidad_ventas = 0
cantidad_ventas_100_300 = 0
cantidad_ventas_400 = 0
cantidad_ventas_500 = 0
cantidad_ventas_600 = 0
ventas_menor_50 = False

ventas = int(input("ingrese la cantidad de u/vendidas en la primera sucursal (valor negativo corta)"))

while ventas >= 0:
    cantidad_ventas += 1
    ventas_total = ventas_total + ventas
    if 100 <= ventas <= 300:
        cantidad_ventas_100_300 += 1
    elif 300 < ventas <= 400:
        cantidad_ventas_400 += 1
    elif 499 < ventas <= 500:
        cantidad_ventas_500 += 1
    elif 599 < ventas >= 600:
        cantidad_ventas_600 += 1
    elif ventas < 50:
        ventas_menor_50 = True
    ventas = int(input("ingrese la cantidad de u/vendidas en la siguiente sucursal (valor negativo corta)"))

print(f"El total de las ventas fue de {ventas_total} unidades\nFueron {cantidad_ventas} ventas que se realizaron")
print(f"Las ventas entre 100 y 300 unidades fueron {cantidad_ventas_100_300}\nLas ventas de 400 unidades fueron {cantidad_ventas_400}")
print(f"Las ventas de 500 unidades fueron {cantidad_ventas_500}\nLas ventas de 600 o mas unidades fueron {cantidad_ventas_600}")
if ventas_menor_50:
    print("Hubo ventas menores a 50 unidades")


