#VICTOR ENRIQUE TUZ DZIDZ 

from os import system

if system ("clear") !=0: system ("cls")

print("Conversion de tipos")

print(int('100')+2) #convertir 100 en entero y suma 2

print(int("100"+ str(2))) #converitr el numero 2 a cadena y  lo concatena 

print(type(float("3.1416"))) #conveertir 3.1416 a float y muestra su tipo 

print (int (3.1416)) #elimina la parte decimal 


#Evaluacion valores numeros boleanos 
print(bool(3)) #cualquier numero de 0 es true
print(bool(0)) # flase
print(bool(-1)) # numeros negativos tambien son true

#evaluar cadenas como boolenaos 
print(bool("")) # cadena vacia es falso 
print(bool(" ")) # cadena con esapcio true
print(bool("false")) # cadena con texto, aunque sea "falso", es true

#Redondear un numero decimal
print(round(2.51)) #redondea 

print(int("hola mundo")) #esto genera un ValueError por que 'hola mundo' nones un numero 