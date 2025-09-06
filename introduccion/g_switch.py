# Switch
# En python es llamado como match
# - Se usa para lo mismo que un if pero con casos simples

hoy = "x"

match hoy:
    case "L":
        print("es lunes")
    case "M":
        print("es martes")
    case _:
        print("Esta inicial no es valida")

edad = 17


# mecanismo de monedas

# moneda = float(input(f"{"opciones":-^20}\n\
#     - $0.10\n\
#     - $0.05\n\
#     - $0.25\n\
#     - $1.00\n\
# Ingresa una moneda: "))

# match moneda:
#     case 0.05:
#         print("Has agregado cinco centavos")
#     case 0.10:
#         print("Has agregado diez centavos")
#     case 0.25:
#         print("Has agregado 25 centavos")
#     case 1:
#         print("Has agregado un dólar")
#     case _:
#         print("La moneda no es valida")


"""
Ejercicio:
Usa la estructura switch para determinar el día de la semana 0 es lunes y 6 es domingo
"""
import random

days = [0, 1, 2, 3, 4, 5, 6]

day = random.choice(days)


# match
match day:
    case 0:
        print("Es lunes")
    case 1:
        print("Es martes")
    case 2:
        print("Es miercoles")
    case 3:
        print ("Es jueves")
    case 4:
        print ("Es viernes")
    case 5:
        print ("Es sabado")
    case 6:
        print ("Es domingo")                    

# Usando if
if (day == 0):
    print("Es lunes")
if (day == 1):
    print ("Es martes")
if (day == 2):
    print("Es miercoles")
if (day == 3):
    print("Es jueves")
if (day==4):
    print("Es viernes")
if (day==5):
    print ("Es sabado")
if (day==6):
    print ("Es domingo")        
