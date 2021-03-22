# Cargar por teclado un conjunto de números enteros, uno a uno. La carga sólo debe
# terminar cuando se ingrese el cero. Determine si los números que se ingresaron eran todos positivos
# o todos negativos (sin importar en qué orden hayan entrado). Por ejemplo, la secuencia {8, 4, 3, 7}
# cumple con la consigna indicada (son todos positivos). La secuencia {-2, -1, -5} también cumple (son
# todos negativos), pero esta otra secuencia {10, -8, 2, 12} no cumple (hay números de distinto signo
# entremezclados). Si todos los números eran efectivamente del mismo signo, muestre también la suma
# de esos números (no mostrar la suma si había números de signos diferentes entremezclados).

verificador_de_signos = True
suma_de_numeros = 0
carga_de_numeros = int(input("ingrese el numero entero (con 0 corta el programa)"))
anterior = carga_de_numeros
while carga_de_numeros != 0:
    suma_de_numeros += carga_de_numeros
    carga_anterior = carga_de_numeros
    carga_de_numeros = int(input("ingrse otro numero entero (con 0 corta el programa)"))
    if anterior * carga_de_numeros < 0:
        verificador_de_signos = False

if verificador_de_signos:
    print(f"todos los numeros eran del mismo signo\nLa suma de ellos es de: {suma_de_numeros}")
else:
    print("Los numeros cargados son de diferentes signos")

