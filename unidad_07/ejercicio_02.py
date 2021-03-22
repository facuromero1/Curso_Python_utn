#El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La
#frase finaliza con un punto, y las palabras están separadas por espacios unicamente. Se debe mostrar:
#Ver el porcentaje de vocales respecto del total de letras de la frase
#La longitud promedio de las palabras
#La Palabra mas larga del texto
#CanƟdad de palabras que comienzan con “ta”



letra = None
contador_de_palabras = 0
contador_de_letras = 0

palabra_con_t = False
palabras_con_ta = 0
contador_palabras_p = 0
while letra != ".":
    letra = input("ingrese la letra (con . corta)")
    contador_de_letras += 1
    contador_de_letras = 0

    if letra == " " or letra == ".":
        if contador_de_letras > 1:
            contador_de_palabras += 1

        elif contador_de_letras == 1 and letra == "p":
            contador_palabras_p += 1

        elif letra == "t":
            palabra_con_t = True

        elif letra == "a" and palabra_con_t == True:
            palabras_con_ta += 1
        elif contador_de_letras == 1 and letra == "p":
            contador_palabras_p += 1

print(f"{contador_palabras_p}")
print(f"{contador_de_palabras}")
print(f"{contador_de_letras}")
print(f"{palabras_con_ta}")
