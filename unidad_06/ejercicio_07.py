funciones_descuento = 0
funciones_sin_descuento = 0
monto = 0

cantidad_espectadores = int(input("ingrese la cantidad de espectadores (con 0 corta el programa)"))

while cantidad_espectadores != 0:
    descuento = input("Carga S para descuento N para sin descuento")
    if descuento == "S":
        precio = 50
    else:
        precio = 75
    monto = monto + (cantidad_espectadores * precio)

    if descuento == "S":
        funciones_descuento =+ 1
    funciones_sin_descuento =+ 1
    cantidad_espectadores = int(input("ingrese la cantidad de espectadores (con 0 corta el programa)"))

print(f"La recaudacion total fue de: {monto}")

if funciones_sin_descuento != 0:
    porcentaje = funciones_descuento * 100 / (funciones_sin_descuento + funciones_descuento)

    print(f"el porcentaje de las funciones con descuento es del {porcentaje} %")
