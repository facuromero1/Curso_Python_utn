# Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus
# vendedores, para ello le solicita un sistemita que le permita calcular dichos montos.
# Se Ɵene conocimiento que la empresa Ɵene cuatro categorías de vendedores (1 a 4). Usted debe
# solicitar el ingreso de la categoría del vendedor y el total de la venta (el proceso termina cuando se
# ingrese una categoría igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores
# de diferentes categorias en base a los siguientes cálculos:
# Categoría 1: cobra una comisión de 10 %
# Categoría 2: cobra una comisión de 25 %
# Categoría 3: cobra una comisión de 30 %
# Categoría 4: cobra una comisión de 40 %
# Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de
# vendedores que Ɵene la empresa junto con el total general


print("ingresar 1 para categoria de comision del 10%(con 0 corta el programa)")
print("ingresar 2 para categoria de comision del 20%(con 0 corta el programa)")
print("ingresar 3 para categoria de comision del 30%(con 0 corta el programa)")
print("ingresar 4 para categoria de comision del 40%(con 0 corta el programa)")
categoria = int(input("ingrese su catergoria"))
acumulador_cat_1 = 0
acumulador_cat_2 = 0
acumulador_cat_3 = 0
acumulador_cat_4 = 0
while 0 < categoria < 5:
    monto_venta = int(input("ingrese el monto vendido por el vendedor"))
    if categoria == 1:
        comision = monto_venta * 0.10
        acumulador_cat_1 += comision

    elif categoria == 2:
        comision = monto_venta * 0.20
        acumulador_cat_2 += comision

    elif categoria == 3:
        comision = monto_venta * 0.30
        acumulador_cat_3 += comision

    else:
        comision = monto_venta * 0.40
        acumulador_cat_4 += comision
    categoria = int(input("ingrese su categoria"))

acumulador_total = acumulador_cat_1 + acumulador_cat_2 + acumulador_cat_3 + acumulador_cat_4
print(f"Las comisiones de la categoria 1 acumulan un total de: {acumulador_cat_1}")
print(f"Las comisiones de la categoria 2 acumulan un total de: {acumulador_cat_2}")
print(f"Las comisiones de la categoria 3 acumulan un total de: {acumulador_cat_3}")
print(f"Las comisiones de la categoria 4 acumulan un total de: {acumulador_cat_4}")
print(f"El total de las comisiones a pagar de la empresa es de: {acumulador_total}")
