
#Actividad 03_Ejercicios_ciclos
#Victor Enrique Tuz Dzidz 
#Ejercicios FOR


print("\n Ejercicio 1 ")

for i in range(2, 21, 2):
    print(i)

print("\n Ejercicio 2 ")

numeros = [10, 20, 30, 40, 50]
suma = 0

for n in numeros:
    suma += n

media = suma / len(numeros)
print(f"La media es: {media}")

print("\n Ejercicio 3 ")

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]  # Empezamos asumiendo que el primero es el mayor

for n in numeros:
    if n > maximo:
        maximo = n

print(f"El número máximo es: {maximo}")

print("\n Ejercicio 4 ")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

# Opción A: Bucle for tradicional
filtradas = []
for p in palabras:
    if len(p) > 5:
        filtradas.append(p)

# Opción B: List Comprehension (más Pythonic)
filtradas_comp = [p for p in palabras if len(p) > 5]

print(f"Palabras con más de 5 letras: {filtradas_comp}")


print("\n Ejercicio 5 ")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra_usuario = input("Introduce una letra: ").lower()
contador = 0

for p in palabras:
    if p.lower().startswith(letra_usuario):
        contador += 1

print(f"Hay {contador} palabras que empiezan con la letra '{letra_usuario}'")




