
    # Ejercicio 1 - Solo impresión de texto
print("=====================================")
print("   Bienvenido al curso de Python    ")
print("   Programación Estructurada        ")
print("=====================================")
print("")
print("Hoy aprenderemos los fundamentos")
print("usando solo estructuras básicas.")
print("")



# Ejercicio 2 - Uso de funciones de la biblioteca estándar

def mostrar_mensaje_bienvenida(nombre):
    mensaje = f"{nombre}! Bienvenido al paradigma Estructurado."
    print(mensaje)
    print("-" * len(mensaje))


# Programa principal
print("Ejercicio 2 - Uso de funciones propias")
nombre_usuario = input("¿Cuál es tu nombre? ")

mostrar_mensaje_bienvenida(nombre_usuario)

print("\nAlgunas funciones útiles de Python:")
print("Longitud del nombre:", len(nombre_usuario))
print("Nombre en mayúsculas:", nombre_usuario.upper())
print("Nombre en minúsculas:", nombre_usuario.lower())
 

# Ejercicio 3 - Estructuras de decisión (selección)

print("=== Determinar si un número es positivo, negativo o cero ===\n")

try:
    numero = float(input("Ingresa un número: "))
    
    if numero > 0:
        print("El número es POSITIVO")
    elif numero < 0:
        print("El número es NEGATIVO")
    else:
        print("El número es CERO")
        
except ValueError:
    print("¡Error! Debes ingresar un número válido.")




# Ejercicio 4 - Concatenación y formateo de cadenas

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("¿En qué ciudad vives?: ")

# Varias formas de concatenar/combinar

# Forma 1: concatenación con +
saludo1 = "Hola " + nombre + ", tienes " + str(edad) + " años."

# Forma 2: f-strings (recomendada)
saludo2 = f"Hola {nombre}, tienes {edad} años y vives en {ciudad}."

# Forma 3: método format()
saludo3 = "Hola {}, en {} tienes {} años.".format(nombre, ciudad, edad)

print("\nResultados:")
print("Forma 1:", saludo1)
print("Forma 2:", saludo2)
print("Forma 3:", saludo3)

# Concatenación con números y cálculos
promedio = (18 + edad + 25) / 3
print(f"\nSi tuvieras 18 y 25 años, el promedio de edades sería: {promedio:.1f} años")




# Ejercicio 5 - Ejemplo completo de programación estructurada

def obtener_numero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Error: El número debe ser positivo.")
        except ValueError:
            print("Error: Ingresa un número entero válido.")


# Programa principal
print("=== Programa estructurado completo ===\n")

# Entrada
nombre = input("Tu nombre: ")
edad = obtener_numero_positivo("Tu edad: ")
altura = float(input("Tu altura en metros (ej. 1.75): "))

# Procesamiento
mayor_edad = edad >= 18
clasificacion = ""

if edad < 13:
    clasificacion = "Niño"
elif edad < 18:
    clasificacion = "Adolescente"
elif edad < 65:
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto mayor"

# Salida
print("\n" + "="*50)
print(f"RESUMEN DE DATOS")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años → {clasificacion}")
print(f"Mayor de edad: {'SÍ' if mayor_edad else 'NO'}")
print(f"Altura: {altura} m")

if mayor_edad:
    print("¡Puedes votar y sacar licencia de conducir!")
else:
    print("Aún eres menor de edad.")
print("="*50)

