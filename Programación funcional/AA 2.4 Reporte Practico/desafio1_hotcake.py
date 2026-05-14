# Desafío 1: Ordenar hotcakes para la familia

# Objetivo: Crea un programa que simule la preparación de piezas de hotcake 🥞 y ordena de acuerdo al número de integrantes en tu familia.

def preparar_hotcake():
    """
    1.- Define una función que no reciba parámetros y devuelva el emoji de hotcake.
    Esta función simulará la preparación de una pieza de 🥞 hotcake.
    """
    return "🥞"

def ordenar_hotcakes(numero_piezas):
    """
    2.- Crea una segunda función que reciba un argumento numero_piezas, representando la cantidad de piezas de hotcake a preparar.
    Dentro de la función:
    — Almacena los resultados en una lista llamada piezas_hotcakes.
    — Usa una comprensión de listas para llamar a la función preparar_hotcake tantas veces como el número indicado en numero_piezas.
    — Devuelve la lista piezas_hotcake.
    """
    piezas_hotcakes = [preparar_hotcake() for _ in range(numero_piezas)]
    return piezas_hotcakes

# 4.- Llama a la segunda función solicitando al usuario ingresar el número de integrantes en su familia y almacena el resultado en una variable hotcakes_familia.
hotcakes_familia  = ordenar_hotcakes (int(input("Ingresa el número de integrantes en tu familia: ")))

# 5.- Muestra en pantalla el contenido de la variable hotcakes_familia, que será una lista con varios emojis "🥞".
print(hotcakes_familia)




