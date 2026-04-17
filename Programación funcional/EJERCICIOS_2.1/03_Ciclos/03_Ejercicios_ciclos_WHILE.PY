
#Actividad 03_Ejercicios_ciclos
#Victor Enrique Tuz Dzidz 
#Ejercicios FOR

print("\n Ejercicio 1 ")

contador = 10
while contador >= 1:
    print(contador)
    contador -= 1  # Restamos 1 en cada vuelta
    
    
print("\n Ejercicio 2 ")
numero = 1
suma = 0

while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print(f"La suma de los números pares es: {suma}")


print("\n Ejercicio 3")
n = int(input("Introduce un número para calcular su factorial: "))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"El factorial de {n} es: {factorial}")


print("\n Ejercicio 4 ")
password = ""

while len(password) < 8:
    password = input("Introduce una contraseña (mínimo 8 caracteres): ")
    if len(password) < 8:
        print("Contraseña demasiado corta. Inténtalo de nuevo.")

print("Contraseña válida")

print("\n Ejercicio 5 ")
tabla_del = int(input("¿De qué número quieres la tabla?: "))
multiplicador = 1

while multiplicador <= 10:
    resultado = tabla_del * multiplicador
    print(f"{tabla_del} x {multiplicador} = {resultado}")
    multiplicador += 1
    

print("\n Ejercicio 6 ")
limite = int(input("Introduce un número N para buscar primos hasta ahí: "))
numero_actual = 2  # Empezamos en el primer primo

print(f"Números primos hasta {limite}:")

while numero_actual <= limite:
    es_primo = True
    divisor = 2
    
    # Comprobamos si numero_actual tiene divisores
    while divisor * divisor <= numero_actual:
        if numero_actual % divisor == 0:
            es_primo = False
            break
        divisor += 1
        
    if es_primo:
        print(numero_actual, end=" ")
        
    numero_actual += 1
