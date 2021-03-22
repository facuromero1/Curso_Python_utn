# Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga
# de datos se presenta cuando el usuario ingrese un número negaƟvo.
# Los requerimientos funcionales del programa son:
# La sumatoria de solo los números que estén comprendidos entre 50 y 100.
# Cantidad de valores pares ingresados.
# Cantidad de valores impares ingresados.
# Informar si en la carga de números se ingreso al menos un número 0.
# Informar si la serie conƟene solo números pares e impares alternados
numero_0 = False

suma_num_50_100 = 0
valores_pares = 0
valores_impares = 0
numeros = int(input("ingrese un numero para agregar a la lista (el programa corta con numero negativo)"))

while numeros >= 0:
    pares = numeros % 2
    if pares == 0:
     valores_pares += 1
    else:
        valores_impares += 1
    if 50 <= numeros <= 100:
            suma_num_50_100 += numeros

    if numeros == 0:
        numero_0 = True

    numeros = int(input("ingrese otro numero para agregar a la lista (el programa corta con numero negativo)"))

print(f"La sumatoria de los numeros cargados entre 50 y 100 es de: {suma_num_50_100}")
print(
    f"La cantidad de numeros pares ingresados es de: {valores_pares}\nLa cantidad de numeros impares es de: {valores_impares}")
if numero_0:
    print("se ah ingresado en la cargua uno o mas 0")

#PREGUNTAR TULIO SOBRE ALTERNAN

