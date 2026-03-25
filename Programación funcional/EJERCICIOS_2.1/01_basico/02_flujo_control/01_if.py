###
# 01 – Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") !=0: system("cls")

print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del if
print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
# Además de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si está presente)
nota = 5
if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("¡Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No está calificado!")

print("\n Condiciones múltiples")
tiene_carnet = True
edad = 16

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript:
# && sería and
# || sería or

# En el caso que seas mayor de edad y tengas carnet...
# entonces podrás conducir
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIA !!!!!!")

# En un pueblo de Isla Holbox son más relajados y
# te dejan conducir si eres mayor de edad ó tienes carnet
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Holbox")
else:
    print("Paga al policía y te dejará conducir!!!")

# También tenemos el operador lógico "not"
# que nos permite negar una condición
es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
    print("¡ISC, anda que hay que ir al Tec!")

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
    print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
    print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
    print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación
if es_el_tres:
    print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
#EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("\nEjercicio 1: Mayor de dos números")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Los dos números son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre cero)
print("\nEjercicio 2: Calculadora simple")
num_a = float(input("Introduce el primer número: "))
num_b = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num_a + num_b
    print(f"{num_a} + {num_b} = {resultado}")
elif operacion == "-":
    resultado = num_a - num_b
    print(f"{num_a} - {num_b} = {resultado}")
elif operacion == "*":
    resultado = num_a * num_b
    print(f"{num_a} * {num_b} = {resultado}")
elif operacion == "/":
    if num_b != 0:
        resultado = num_a / num_b
        print(f"{num_a} / {num_b} = {resultado}")
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\nEjercicio 3: Año bisiesto")
anio = int(input("Introduce un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("\nEjercicio 4: Categorizar edades")
edad_usuario = int(input("Introduce tu edad: "))
if edad_usuario <= 2:
    print("Bebé")
elif edad_usuario <= 12:
    print("Niño")
elif edad_usuario <= 17:
    print("Adolescente")
elif edad_usuario <= 64:
    print("Adulto")
else:
    print("Adulto mayor")