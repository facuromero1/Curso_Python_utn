# El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La
# frase finaliza con un punto, y las palabras están separadas por espacios unicamente. Se debe mostrar:
# Ver el porcentaje de vocales respecto del total de letras de la frase
# La longitud promedio de las palabras
# La longitud de la Palabra mas larga del texto
# CanƟdad de palabras que comienzan con “ta”


texto = ""
vocales = "aeiouAEIOUàèìòù"
longitud_promedio = 0
contador_palabras_frase = 0
contador_vocales = 0
contador_palabras = 0
contador_letras_palabra = 0
palabra_mas_larga = 0
contador_ta = 0
contador_letras_frase = 0

hay_t = False
hay_ta = False

while len(texto) <= 0:
    texto = input('Ingrese el texto a analizar: ')
    if len(texto) <= 0:
        texto = input('Ingrese el texto a analizar: ')

for i in texto:
    if i.isalpha():
        contador_letras_palabra += 1
        contador_letras_frase += 1
        if i in vocales:
            contador_vocales += 1
        if contador_letras_palabra == 1 and i.upper() == "T":
            hay_t = True
        else:
            if hay_t and i.upper() == "A":
                hay_ta = True
                hay_t = False
            if hay_ta:
                contador_ta += 1
                hay_ta = False
    if i == " " or i == ".":
        contador_palabras_frase += 1
        contador_palabras += 1
        palabra_mas_larga = contador_letras_palabra
        if contador_letras_palabra > palabra_mas_larga:
            palabra_mas_larga = contador_letras_palabra
        contador_letras_palabra = 0

if contador_letras_frase != 0:
    longitud_promedio = contador_letras_frase / contador_palabras_frase


if contador_letras_frase != 0:
    porcentaje_vocales = round(contador_vocales * 100 / contador_letras_frase, 2)
else:
    porcentaje_vocales = 0


print(f"El porcentaje de vocales repecto las demas letras de la frase es de: {porcentaje_vocales}.")
print((f"La longitud promedio de las palabras es de: {longitud_promedio} letras."))
print(f"La longitud de la palabra mas larga es de: {palabra_mas_larga} letras.")
print(f"Se encontraron un total de {contador_ta} palabras que cominezan con la silaba ta.")

