# Un pequeño comercio de papelería cuenta con dos vendedores. Cada vendedor está
# codificado con los números 1 y 2. Considere que la carga de datos se realizará desde teclado, de
# forma que una entrada consta de 3 variables que representan una venta realizada: por cada venta,
# cargar el código del vendedor (1 o 2) que hizo la venta, cantidad de artículos vendida en esa
# operación, e importe de la venta. El fin de datos se indicará con código de vendedor igual a 0 (cero).
# El dueño del comercio desea cierta información estadística y para ello solicita un programa que
# obtenga lo siguiente:
# a.) La cantidad de productos vendida por cada vendedor (dos totales).
# b.) El importe total vendido por cada vendedor (otros dos totales).
# c.) El importe de la menor venta realizada por el vendedor 2.
# d.) El importe promedio de ventas por vendedor (importe total acumulado / 2).


total_productos_vendedor_1 = 0
total_productos_vendedor_2 = 0
importe_total_vendedor_1 = 0
importe_total_vendedor_2 = 0
codigo = -1
aviso_vendedor_2 = False
menor_importe = 0
while codigo < 0 or codigo > 2:
    codigo = int(input("ingrese el codigo del vendedor 1 o 2(con el 0 corta el programa)"))
    if codigo < 0 or codigo > 2:
        print("codigo ingresado no es correcto.Porfavor vuelva a ingresar el codigo del vendedor 1 o 2.gracias!")
    codigo = int(input("ingrese el codigo del vendedor 1 o 2(con el 0 corta el programa)"))

while 1 <= codigo and codigo <= 2:
    cantidad_articulos = int(input("ingrese la cantidad de articulos vendidos"))
    importe = float(input("ingrese el importe de la venta porfavor"))

    if codigo == 1:
        total_productos_vendedor_1 += cantidad_articulos
        importe_total_vendedor_1 += importe

    elif codigo == 2:
        total_productos_vendedor_2 += cantidad_articulos
        importe_total_vendedor_2 += importe

        if not aviso_vendedor_2:
            aviso_vendedor_2 = True
            menor_importe = importe
        elif importe < menor_importe:
            menor_importe = importe

    codigo = int(input("ingrese el codigo del vendedor 1 o 2(con el 0 corta el programa)"))
    if codigo < 0 or codigo > 2:
        print("codigo ingresado no es correcto.Porfavor vuelva a ingresar el codigo del vendedor 1 o 2.gracias!")

promedio_importe_ventas = (importe_total_vendedor_1 + importe_total_vendedor_2) / 2

print(
    f"La cantidad de productos del vendedor 1 es igual a: {total_productos_vendedor_1}\nLa cantidad de productos del vendedor 2 es igual a: {total_productos_vendedor_2}")
print(
    f"El importe total vendido del vendedor 1 es igual a: {importe_total_vendedor_1}\nEl importe total vendido del vendedor 2 es igual a: {importe_total_vendedor_2}")
print(f"El menor importe realizado por ventas del vendedor 2 es igual: {menor_importe}")
print(f"El importe promedio de las ventas de los vendedores es igual a: {promedio_importe_ventas}")
