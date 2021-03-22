#Cargar por teclado una frase, pero a razón de un caracter por vez en una variable. La frase debe
#terminar con un punto (al aparecer el punto, la carga debe finalizar). El programa debe informar:
#Promedio de letras por palabra.
#CanƟdad de palabras que terminan con la letra ’s’ (minúscula).
#CanƟdad de palabras que conƟenen a la sílaba ’sa’ (minúscula).



palabra_sa = False
actual = None
anterior = None
contador_palabra_s = 0
letras = 0
contador_palabras = 0
contador_palabras_sa = 0

while actual != ".":
    actual = input("ingrese caracter (con . corta el programa)")

    if (actual == "." or actual == " ") and anterior != None:
        contador_palabras += 1

        if anterior == "s":
            contador_palabra_s += 1
        if palabra_sa == True:
            contador_palabras_sa += 1
            palabra_sa = False
    else:
        letras += 1
        if actual == "a" and anterior == "s":
            palabra_sa = True
    anterior = actual




if contador_palabras == 0:
    promedio = 0
else:
    promedio = letras / contador_palabras

print(f"El promedio de las letras por palabra es de: {promedio}\nHay {contador_palabra_s} palabras que terminan en s")
print(f"Hay {contador_palabras_sa} palabras que contienen la silaba sa")
