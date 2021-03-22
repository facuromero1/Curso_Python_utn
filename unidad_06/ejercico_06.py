# Cargar por teclado una lista de números enteros que irán llegando uno a uno, y que
# representan cantidades mensuales de automóviles nuevos vendidos en el país durante cierto período.
# Para indicar que la carga de datos debe finalizar, se ingresará el valor -1 (menos uno) (note que el
# valor 0 (cero) puede ser un dato valido: es perfectamente posible que no haya habido ventas en un
# mes determinado). Se pide:
# a. Determinar cuántas de esas cantidades fueron mayores o iguales que 0 pero menores que
# 10000 unidades, cuántas fueron mayores o iguales a 10000 pero menores que 15000, y
# cuántas fueron mayores o iguales que 15000.
# b. Determinar la cantidad total de automóviles nuevos que se vendieron en el país.
# c. Determinar si se ingresó al menos una cantidad igual a 0 o no. Informe con un mensaje simple
# en pantalla


c1, c2, c3, acumulador_totales = 0, 0, 0, 0

cantidad_ventas = int(input("ingrese otra cantidad de ventas(con -1 se cancela el programa)"))

ventas_0 = False

while cantidad_ventas != -1:
    if 0 < cantidad_ventas < 10000:
        c1 += 1

    elif 10000 <= cantidad_ventas <= 15000:
        c2 += 1

    elif cantidad_ventas >= 15000:
        c3 += 1
    acumulador_totales = acumulador_totales + cantidad_ventas
    cantidad_ventas = int(input("ingrese otra cantidad de ventas(con -1 se cancela el programa)"))

if ventas_0 == 0:
    ventas_0 = True
if ventas_0:
    print("En alguno de los periodos la venta fue de 0")
else:
    print("En ningun periodo la venta fue de 0")

print(
    f"La cantidad de ventas entre 0 y 10000 fueron {c1}\nLa cantidad de ventas entre 10000 y 15000 fueron{c2}\nLa cantidad de ventas superiores a 15000 fueron {c3}")
print(f"La cantidad total de automoviles vendidos en el pais es de {acumulador_totales}")
