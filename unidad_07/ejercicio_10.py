contador_palabras = 0
contador_letras = 0
letra = input("ingrese la primera letra de la frase(con . corta)")

while letra != ".":

    if letra == " " or letra == ".":
        contador_palabras += 1
    else:
        if letra.isalpha():
            contador_letras += 1
    letra = input("ingrese la siguiente letras de la frase")
promedio = contador_letras / contador_palabras

print(f"La frase contiene {contador_palabras} palabras\nEl promedio de letras por palabras es de: {promedio} letras")