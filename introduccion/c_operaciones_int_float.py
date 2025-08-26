"""
Para los datos que tienen numeros se pueden realizar
operaciones matemáticas (sumar, restar, dividir y multiplicar)
"""

a: int = 1
b: float = 3.10

# Suma
print(a + 2)
print(b + 1)


# Resta
print(a - b)


# División
print(a/ b)


# Multiplicación
print(a*b)


"""
Las operaciones son necesarias para hacer calculos
en cualquier programa
"""


# Adicional
# Multiplicar números con string

titulo = "Prueba"

# Multiplicar un string con un entero, hace que se repita la cadena
print(3*titulo)


# Ejercicio propuesto:
# Escribe un programa que pida al usuario dos números, uno entero y uno decimal,
# y luego muestre por pantalla la suma, resta, multiplicación y división de ambos.

# Ejemplo de entrada:
#   Ingresa un número entero: 5
#   Ingresa un número decimal: 2.5

# Ejemplo de salida:
#   Suma: 7.5
#   Resta: 2.5
#   Multiplicación: 12.5
#   División: 2.0

num1 = input("Ingrese un numero entero: ")
num2 =input("Ingrese un numero decimal: ")

num_entero = int(num1)
num_decimal=float(num2)

print(num_entero+num_decimal)
print(num_entero-num_decimal)
print(num_entero*num_decimal)
print(num_entero/num_decimal)
