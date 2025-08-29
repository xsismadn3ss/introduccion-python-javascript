"""Estructuras de flujo

- Permiten establecer condiciones
- Se utilizan para decidir si ejecutar una acción en un programa
- Permiten repetir código

Se dividen en:

- For: Repetir acciones un número definido de veces
- While: Repetir acciones un número indefinido de veces mientras se cumple algo
- If: Permite ejecutar algo si se cumple una condición
- Else: Se ejecuta si no se cumple un if
- Switch: es un comparador de casos que permite ejecutar si se cumplen los casos dentro del switch
"""

# For
# Imprimir los primeros diez numeros
print("\nImprimiendo desde 0 a 9")
for i in range(10):  # devuelve de  0 a 9
    print(i)

# de 1 a 10
print("\nImprimiendo desde 1 a 10")
for i in range(1, 11):
    print(i)


# While
print("\nWhile")
print("Numeros desde 1 a 10")
a = 1
while a < 4:
    print(a)
    a = a + 1

# If y else
edad = 17
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

edad = -4
if edad >= 18:
    print("Eres mayor de edad")
if edad < 18 and edad > 0:
    print("Eres menor de edad")
if edad <= 0:
    print("No es una edad valida")


# usando operadores en el if

# OR: se cumple si uno de los dos casos es verdadero
# AND: se cumple si ambos casos son iguales
# NOT: invierte el valor

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
opcion = dias[2]

if opcion == "lunes" or opcion == "viernes":
    print("Esta abierto")
else:
    print("Esta cerrado")

colores = "rojo", "verde", "azul"
tallas = "S", "M", "L", "XL"

color = colores[0]
talla = tallas[1]
if color == "rojo" and talla == "S":
    print("No hay existencia")
else:
    print("Hay existencias")


color = colores[1]
# cond = color == 'rojo'
# print(cond)
# print(not cond)
if not color == "rojo":
    print("No es rojo")
else:
    print("Es rojo")

if color != "rojo":
    print("No es rojo")
else:
    print("Es rojo")


# Ejercicios para FOR
"""
- Imprimir número pares desde el 1 al 10

- Contar vocales
Escribe un programa que recorra una cadena de texto ingresada por el usuario y cuente cuántas vocales (a, e, i, o, u) contiene.

- Tabla de multiplicar
Pide al usuario un número entero y usa un bucle for para imprimir la tabla de multiplicar de ese número del 1 al 10.
"""

num = 3
residuo = num % 2  # si es par el residuo es 0, si es impar el residuo es 1
print(residuo)
if residuo == 0:
    print("Es par")
else:
    print("Es impar")

for i in range(1, 11):
    residuo = i % 2
    if residuo == 0:
        print(i)

numeros: tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
for numero in numeros:
    i = numero
    print(i)

if 1 in numeros:
    print("Si esta")


# Texto ingresado por el usuario
# Conteo de vocales
cadena = input("Ingrese una palabra: ")
conteo = 0
vocales = ["a", "e", "i", "o", "u"]

for letra in cadena:
    if letra in vocales:
        conteo += 1

print("Total de vocales",conteo )