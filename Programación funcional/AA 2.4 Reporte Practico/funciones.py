
# ejemplo callback
def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

resultado = operar(5, 3, suma)

print(resultado) # Imprime 8

"""
Una callback es una funcion que se pasa a otra funcion como argumento y se  espera que sea llmado dentro de esa Function
las funciones de primer orden son  aquellas que no tomam otras funciones como argumentos ni devuelven funciones


"""
# EJEMPLO FUNCIÓN PRIMERA CLASE

def saludo():
    return "¡Hola!"

mi_variable = saludo() # Ejecutamos la función y la asignamos a una variable
print(mi_variable) # Imprimimos la variable


def saludo2():
    return "¡Que tal!"

mi_variable2 = saludo2 # Asignamos la función sin paréntesis a una variable, pero no ejecutamos
print(mi_variable2()) # Para ejecutar la función más tarde, debes usar paréntesis

"""
Una función de primera clase puede ser asignada a una variable, usarse como argumento para otra función o devolver otra 
función como resultado.
Puede Devolver Funciones:
"""

## EJEMPLO FUNCION DE ORDEN SUPERIOR

def elegir_operacion(operacion): # funcion de orden superior
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2

    if operacion == "multiplicar":
        return multiplicar # Retornamos la función sin ejecutarla
    else:
        return dividir

doble = elegir_operacion("multiplicar") # Devuelve la función multiplicar
print(doble(10))

divide2 = elegir_operacion("dividir") # Devuelve la función dividir
print(divide2(10))

"""
Una función de orden superior es aquella que puede recibir otras funciones como argumentos o devolver una función como resultado.
"""

# EJEMPLO FUNCION ANONIMA = LAMBDA

doble = lambda x: x * 2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

alumnos = ['Alejandro', 'Miguel', 'Vinicio', 'Rodney', 'Marcial']
saludar_alumnos = list(map(lambda nombre: 'Hola ' + nombre, alumnos))
print(saludar_alumnos)

# sin lambda
def saludar(nombre):
    return 'Hola ' + nombre

# Usamos map con la función saludar
lista_saludos = list(map(saludar, alumnos))
# print(lista_saludos)