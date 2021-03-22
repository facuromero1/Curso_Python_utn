tot_cat_1 = 0
tot_cat_2 = 0
tot_cat_3 = 0
tot_cat_4 = 0
print('Inicio de calculo de comisión, con categoria 0 el proceso termina')
categoria = int(input('Ingrese la categoria de vendedor (1-4): '))
while categoria != 0:
    venta = float(input('Ingrese el total vendido por este vendedor: '))
    if categoria == 1:
        tot_cat_1 += venta * 0.10
    elif categoria == 2:
        tot_cat_2 += venta * 0.25
    elif categoria == 3:
        tot_cat_3 += venta * 0.30
    else:
        tot_cat_4 += venta * 0.40
    categoria = int(input('Ingrese una nueva categoria de vendedor (1-4): '))
