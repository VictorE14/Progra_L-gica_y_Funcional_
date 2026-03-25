#VICTOR ENRIQUE TUZ DZIDZ 

from os import system

if system ("clear") !=0: system ("cls")

#Solo se pone el nombre de la variable y asignarle un valor 
my_name= 'Victor'

print(my_name)

age = 22
print(age) #imprime age


#reasigna un nuevo valor a una variante existente 

age=26
print(age) # nuevo valor age


#Tipado dinamico: el tipo de dato se determine en tiempo de ejecucion

name= 'Victor'

name =32
print(type(name ))


print(f"Hola {my_name}, tengo {age+5}años")

name, age, city = "Victor", 22, "FCP"

mi_nombre_de_variable= "ok"
nombre ="ok"

miNombreDeVariable = "no-recomendado"
MiNombreDeVariable = "no-recomendado"
minombredevariable = "no-recomendado"


MI_CONSTANTE = 3.1416

# Anotaciones de tipo (opcinal, para  mayor claridad en el codigo )

is_user_logged_in:bool = True

name : str ="victor"
print(name)