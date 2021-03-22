# Un observatorio meteorológico ha tomado el registro de temperaturas en disƟntos momentos del
# día. Se solicita el desarrollo de un programa que facilite información estadísƟcas de ellas.
# El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).
# Los requerimientos funcionales son:
# Promedio de temperatura diaria.
# Temperatura máxima.
# Temperatura mínima.
# Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio

temperatura_01 = int(input("ingrese la primera temperatura"))
temperatura_02 = int(input("ingrese la segunda temperatura"))
temperatura_03 = int(input("ingrese la tercera temperatura"))
temperatura_04 = int(input("ingrese la cuarta temperatura"))

promedio_temperatura = (temperatura_04 + temperatura_03 + temperatura_02 + temperatura_01) / 4
temperatura_maxima = max(temperatura_04, temperatura_03, temperatura_02, temperatura_01)
temperatura_minima = min(temperatura_04, temperatura_03, temperatura_02, temperatura_01)

print(
    f"EL valor maximo de temperatura llego a los {temperatura_maxima} grados\nEl valor minimo de la temperatura fue de {temperatura_minima} grados\nLlegando asi a un promedio de temperatura de unos {promedio_temperatura} grados")

if temperatura_01 > promedio_temperatura or temperatura_02 > promedio_temperatura or temperatura_03 > promedio_temperatura or temperatura_04 > promedio_temperatura:
    print("Alguna de las temperaturas supero el valor del promedio de ellas juntas")
