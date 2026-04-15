from os import system
if system("clear") !=0: system("cls")


print("\n Bucle While:")

#bulces con una simple condicion 
contador = 0 

while contador<=5:
    print("contador")
    contador += 1  #Evita el bucle infinito 
    
#utiliza la palabra break, para evitar romoer infinito 

print("\n Bucle While con break ")
contador = 0 

while True: 
    print (contador)
    contador +=1
    if contador == 5:
        break # sale del bucle
    

print("\n Bucle con continue ")  
contador = 0 
while contador <10:
    contador +=1 
    
    if contador % 2 ++ 0:
        continue
    
    
    print (contador)
    
    
    
#else, esta condicion cuando se ejecuta ?

print("\n Bucle While con else ")
contador = 0 
while contador<5:
    print(contador)
    contador+=1
else:
    print("el bucle ha terminado ")
    
#pedir un numeor al usuario
#que debe de ser positivo 

numero = -1 
while numero <0:
    numero= int(input("Escribe un numero positiovo:")) 
    if numero< 0 : 
        print('El numeor debe de ser positivo, intenta otra vez ')

print(f"El numeor que has introducido es {numero}")


numero = -1
while numero <0:
    try:
        numero= int(input("Escribe un numero positivo"))
        if numero < 0:
            print("El numero debe de ser positivo. Intenta otra vez")
    except:
        print("Lo que introduces de ser un numero")
    
print(f"El numeor que has introduccido es {numero}")
