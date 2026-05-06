# Objetivo: Mostrar el uso de compresión de listas en Python

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doble = [] #lista vacía

for n in numeros:
    doble.append(n*2)

print(doble)

# Genera otra lista de los cuadrados de los números en la lista numeros
cuadrados = [num ** 2 for num in numeros]

lista_cuadruple=list(map(lambda x: x * 4, numeros))
print(lista_cuadruple)

# Genera otra lista con el cubo de cada uno de los numeros de la lista
cubo = [elemento ** 3 for elemento in numeros]

cadena = ["hola " + "que hace" for _ in range(3)]

# Genera una lista de cadenas para cada elemento del rango de 5
saludos = ["hola" for _ in range(5)] #range(0, 5)
saludos2 = ["que hace" for _ in range(3)] #range(0, 3)