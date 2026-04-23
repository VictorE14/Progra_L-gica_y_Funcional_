#VICTOR ENRIQUE TUZ DZIDZ
#ACTIVIDAD FUNCTIONS


from os import system
if system("clear") !=0: system("cls")

# """ Definición de una función
# 
# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional
# 

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#     print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#     print(f"¡Hola {nombre}!")

# saludar_a("Estudiante")
# saludar_a("jefa")
# saludar_a("profesor")
# saludar_a("Directora")


# ## Funciones con más parámetros
def sumar(a, b):
    suma = a + b
    return suma

result = sumar(2, 3)
print(result)


# ## Documentar las funciones con docstring
def restar(a, b):
    """Resta dos números y devuelve el resultado"""
    return a - b


# # Parámetros por defecto
def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2))      # Usa el default (2 * 2 = 4)
print(multiplicar(2, 3))   # Sobrescribe el default (2 * 3 = 6)


# # Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# Parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("carlos", 25, "pajaro")
describir_persona("persona", "ingeniero", 39)


# # Argumentos por clave (parámetros nombrados)
# Aquí no importa el orden porque indicamos el nombre del parámetro
describir_persona(sexo="perro", nombre="Reyes", edad=25)
describir_persona(sexo="mujer", nombre="Alejandra", edad=21)


# # Argumentos de longitud de variable (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
