#La final de una carrera de ciclistas Ɵene n compeƟdores. Se pide cargar los datos de cada compeƟdor (nombre y Ɵempo de carrera, validando que el Ɵempo no sea negaƟvo). La carga finaliza ingresando un cero como nombre del ciclista. Se pide:
#Determinar y mostrar el nombre del ganador de la carrera.
#Ingresar por teclado el Ɵempo record registrado para dicha carrera. Determinar si el Ɵempo del
#ganador es menor al Ɵempo record, mostrar un mensaje.
#Calcular y mostrar el Ɵempo promedio entre todos los ciclistas.



ganador = None
acumulador_tiempo = 0
acumulador_ciclistas = 0

nombre_ciclista = input("ingrese el nombre del ciclista, con 0 corta")

while nombre_ciclista != "0":
    tiempo_carrera = int(input("ingrese el tiempo del ciclista en minutos, gracias"))
    if tiempo_carrera <= 0:
        print("el tiempo ingresado no es correcto.Intentelo de nuevo porfavor!")
        tiempo_carrera = int(input("ingrese el tiempo en numeros positivos.gracias!"))

    if ganador == None or tiempo_carrera < ganador[1]:
        ganador = nombre_ciclista, tiempo_carrera

    acumulador_tiempo += tiempo_carrera
    acumulador_ciclistas += 1
    nombre_ciclista = input("ingrese el nombre del ciclista, con 0 corta")

promedio_ciclistas = acumulador_tiempo / acumulador_ciclistas

if acumulador_ciclistas > 0:
    record = int(input("ingrese el tiempo record de la carrera"))
    if ganador[1] < record:
        print("el ganador ah superado el tiempo record!")

print(f"El ganador de la carrera fue {ganador[0]} con un tiempo de {ganador[1]} minutos")
print(f"El promedio de todos los ciclistas fue de {promedio_ciclistas} minutos")
