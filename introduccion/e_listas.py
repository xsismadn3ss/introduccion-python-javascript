"""
Listas

- Las listas se utilizan para almacenar conjuntos de datos que tienen cosas en común
"""

dias: list[str] = [
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sabado",
    "domingo",
]
print(type(dias))

# Las listas tienen tamaño
print("Numero de días: ", len(dias))

# Se puede acceder a elementos
print(dias[2])

# En las listas si se puede modificar el indice
dias[1] = "Martes"
print(dias)

# Se pueden usar rangos o cambiar el orden
print(dias[2:4])

# Se puede obtener el indice de un elemento en la lista
dia = dias[-1]
print(dias.index(dia))

# Sumar listas
primer_trimestre = ["enero", "febrero", "marzo"]
segundo_trimestre = ["abril", "mayo", "junio"]

semestre = primer_trimestre + segundo_trimestre
print(semestre)

# Ordenar elementos
semestre.sort()
print(semestre)

# Contar elementos 
nombres = ["Ariana", "Marcos", "Ariana", "Karen", "Ignacio"]
print(nombres.count("Ariana"))

# Ejemplo
notas = [10, 10 , 9, 5, 7, 8, 8, 7, 7, 6, 8]
print(notas.count(8))