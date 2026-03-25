###
# 02 Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)   # True
print("5 < 3:", 5 < 3)   # False
print("5 == 5:", 5 == 5) # True (igualdad)
print("5 != 3:", 5 != 3) # True (desigualdad)
print("5 >= 5:", 5 >= 5) # True (mayor o igual que)
print("5 <= 3:", 5 <= 3) # False (menor o igual que)

print("\nComparación de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera") # True
print("'Hola' == 'hola'", "Hola" == "hola") # False

# Operadores lógicos: and, or, not
print("\noperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False) # False
print("True or False:", True or False)   # True
print("False or False:", False or False) # False
print("not True:", not True)             # False
print("not False:", not False)           # True

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A\tB\tA and B")
print("True\tTrue\t", True and True)
print("True\tFalse\t", True and False)
print("False\tTrue\t", False and True)
print("False\tFalse\t", False and False)

print("\nor:")
print("A\tB\tA or B")
print("True\tTrue\t", True or True)
print("True\tFalse\t", True or False)
print("False\tTrue\t", False or True)
print("False\tFalse\t", False or False)

print("\nnot:")
print("A\tnot A")
print("True\t", not True)
print("False\t", not False)