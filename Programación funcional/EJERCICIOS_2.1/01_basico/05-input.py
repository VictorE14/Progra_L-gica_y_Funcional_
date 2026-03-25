#VICTOR ENRIQUE TUZ DZIDZ 

from os import system

if system ("clear") !=0: system ("cls")


name = input("Hola, como estas\n")
print(f"Hola {name}, encantado de conocerte")

age= input("Cuantos años\n")
age = int (age)
print(f"tienes {age} años")

print("Obtener multiples valores a la vez")
country, city = input("En que pais y cuidad vives\n").split()

print(f"vives en {country}, {city}")