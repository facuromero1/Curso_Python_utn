# La idea general del Juego del Punto, es lograr el máximo puntaje en 4(cuatro) vueltas de lanzamiento de 3 dados, y a conƟnuación enumeramos las reglas en base a las cuales se obƟene puntaje:
# 1. Cada jugador dispone de 4(cuatro) Ɵradas o lanzamientos para lograr su objeƟvo, el programa
# solo deberá simular de a una Ɵrada por vez.
# 2. En cada Ɵrada se lanzan 3(tres) dados. Sólo suman puntaje los dados que salgan con un punto
# en el centro (esto es: el 1, el 3 y el 5) (y de allí el nombre del juego). El puntaje de la Ɵrada se
# calcula sumando el aporte de cada dado, de acuerdo a las siguientes pautas:
# Si sale el 1, se suma 1(un) punto (el único que muestra el dado).
# Si sale el 3, se suman 2(dos) puntos (porque a los costados del punto central hay dos puntos).
# Si sale el 5, se suman 4(cuatro) puntos (porque en este caso, hay cuatro puntos a los costados del central).
# Si sale un número par (2, 4 o 6) no se suma ningún punto (porque ese dado no Ɵene punto
# central).
# 3. Si en alguna de las Ɵradas el jugador saca tres números pares iguales, entonces el jugador duplicará los puntos finales que haya sumado al terminar sus cuatro lanzamientos.
# Se pide: que en base a todo lo indicado, se genere un programa que simule 1 Ɵrada de los 3 dados
# y luego habiendo solicitado al usuario que cargue su puntaje previo, informe su puntaje acumulado
# en el caso de haber obtenido puntos, su puntaje previo y el mensaje de que duplica puntos si salieron
# los 3 pares o simplemente su puntaje previo si no sumó ningún punto.


import random

# Carga de puntos

puntos_previos = int(input("Ingrese los puntos previos ya obtenidos"))
puntos = 0
puntos_totales = puntos_previos + puntos
# Tirada de dados

dado_1 = random.randint(1, 6)
dado_2 = random.randint(1, 6)
dado_3 = random.randint(1, 6)
dado_4 = random.randint(1, 6)

print(f"Dado 1 = {dado_1}\nDado 2 = {dado_2}\nDado 3 = {dado_3}\nDado 4 = {dado_4}")

# Si duplica
duplica = False

if (dado_1 % 2) == 0 and dado_2 == dado_1 and dado_3 == dado_1:
    duplica = True
#Dado numero 1
else:
    if dado_1 == 1:
        puntos += 1
    else:
        if dado_1 == 3:
            puntos += 2
        else:
            if dado_1 == 5:
                puntos += 4
# Dado numero 2
if dado_2 == 1:
    puntos += 1
elif dado_2 == 3:
    puntos += 2
elif dado_2 == 5:
    puntos += 4

#Dado numero 3
if dado_3 == 1:
    puntos += 1
elif dado_3 == 3:
    puntos += 2
elif dado_3 == 5:
    puntos += 4

#Dado numero 4
if dado_4 == 1:
    puntos += 1
elif dado_4 == 3:
    puntos += 2
elif dado_4 == 5:
    puntos += 4

puntos_totales = puntos_previos + puntos


print(f"La cantidad de puntos obtenidos fueron {puntos}\nAcumulando un total de {puntos_totales}")
if duplica:
    print("¡Suertudo has duplicado puntos!")
    

