"""
Operaciones con strings

- Los strings son una cadena de carácteres
- Son iterables (se pueden recorrer, acceder a letras dentro de la cadena)
- Se pueden modificar
- Se puede incluir nuevo texto o valores de las variables dentro de la cadena
- Se pueden aplicar formatos
"""

a: str = "Hello world"

indices = enumerate(a)
print("Enumerando indices")
for idx, char in indices:
    print(idx, char)


print("\nAccediendo a un caracter en la cadena")
print(a[-1], a[0])

print("\nAccediendo a un rango de carácteres")
print(a[0:5])

b = "1. Titulo de ejemplo"
print(b[3:])


# Agregar texto dentro de la variable
print("\nAgregando datos dentro de la cadena")
saludo: str = "Hola {}, bienvenido al sistema"
nombre1: str = "Armando"
nombre2: str = "Maria"


print(saludo.format(nombre1))
print(saludo.format(nombre2))

resultado: str = "La fecha es: {}"
import datetime  # noqa: E402
ahora: datetime.date = datetime.date.today()

print(resultado.format(ahora))


# Modifica el texto de un cadena
print("\nModificando una cadena")
a += " " + nombre1
print(a)

print(a[::-1])

n = "amanda"
print(n == n[::-1])


# Aplicar formatos
print("\nAplicar formatos")
valor = 3.1415926535
print("El valor con solo dos decimales es: {:.2f}".format(valor))

print(f"{"BIENVENIDO":^20} jksjskjs")
print(f"{"BIENVENIDO":>20} jskjskjs")
print(f"{"BIENVENIDO":<20} jskjskjs")
print(f"{"BIENVENIDO":#<20} jskjskjs")
print(f"{"BIENVENIDO":#>20} jskjskjs")


# Pedir y guardar texto
# En python se utiliza input
# data = input("Ingresa un texto: ")
# print(data)

# Convertir a números (enteros o flotantes)
# edad = int(input("Edad: "))
# nota = float(input("Nota: "))
# print(edad, nota)

# Imprimir tamaño
print(len(resultado))

# Eliminar espacios
print(resultado.replace(" ", ""))

# Separar cadenas
print(resultado.split(" "))

# Ejercicio sencillo sobre strings:
# Escribe un programa que pida al usuario su nombre y luego imprima un mensaje
# indicando cuántas letras tiene su nombre.

# Para pedir texto se usa input

nombre=input("Ingrese su nombre: ")
print(len(nombre))