#Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y
#luego:
#Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
#Determinar en qué mes recibió el sueldo más bajo del período.
#Informar el sueldo promedio del semestre




meses = ("Enero", "Febrero", "Marzo", "abril", "mayo", "junio")
total = 0
primer_sueldo = True



for mes in meses:
    sueldo = float(input("ingrese el importe del sueldo del mes de"+ " " + str(mes) + ":"))
    total += sueldo
    if primer_sueldo == True:
      mayor_sueldo = sueldo
      menor_sueldo = sueldo , 1
      primer_sueldo = False
    else:
        if mayor_sueldo < sueldo:
            mayor_sueldo = sueldo
        elif menor_sueldo[0] > sueldo:
            menor_sueldo = sueldo,mes
aguinaldo = mayor_sueldo / 2
sueldo_promedio = total / 6
print(f"el monto y el mes del menor sueldo es de: {menor_sueldo} El mayor sueldo es de: {mayor_sueldo}El sueldo promedio es de: {sueldo_promedio} pesos")
print(f"el aguinaldo es un total de: {aguinaldo} pesos")