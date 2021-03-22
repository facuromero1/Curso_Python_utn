# Desarrollar un programa que permita procesar los datos del úlƟmo censo de una pequeña población.
# Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al ingresar cualquier
# otro valor para sexo.
# El programa debe informar:
# A qué sexo corresponde la mayor canƟdad de habitantes (considerar que puede ser igual)
# CanƟdad de mujeres en edad escolar (4 a 18 años inclusive)
# Si hay algún varón que supere los 80 años de edad

varones = 0
mujeres = 0
varones_may_80 = False
escolares = 0
mujeres_escolar = 0
adultos_mayores = 0
sexo = input("ingrese el sexo del habitante M para masculino F para femenino")

while sexo == "M" or sexo == "F":
    edad = int(input("ingrese la edad de la persona"))

    if sexo == "M":
        varones += 1
    else:
        mujeres += 1
    if sexo == "F" and 4 <= edad <= 18:
        mujeres_escolar += 1

    if sexo == "M" and edad > 80:
        varones_may_80 = True

    sexo = input("ingrese el sexo del habitante M para masculino F para femenino")

if varones > mujeres:
    a = ("La poblacion tiene mayor cantidad de personas masculinas")
    print(a)
elif mujeres > varones:
    print("La poblacion tiene mayor porcentaje de personas femeninas")
else:
    print("La poblacion tiene la misma cantidad de personas femeninas que masculinas")

print(f"La cantidad de mujeres en edad preescolar es de: {mujeres_escolar}")

if varones_may_80:
    print("hay uno o mas varones que superan los 80 años")
else:
    print("no hay varones que superen los 80 años")
