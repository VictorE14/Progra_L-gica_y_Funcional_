from os import system
if system ("clear") !=0: system ("cls")


print('int:')
print(type(10))
print(type(0))
print(type(-5))
print(type(4567898765434567898765456789098765456789))


print('float:') #numeros decimales
print(type(3.14))
print(type(1.0))
print(type(1e3))


print(type('complex:'))#numeros complejod
print(type(1+2j))


print('str:') #cadena  de texto 
print(type('hola'))
print(type(''))
print(type('123'))
print(type("""
           multilinea
        """))


print('bool:') #VALORES BOLEANOS 
print(type(True))
print(type(False))
print(type(1<2))

print('NodeType') #Presenta la usencia de valor
print(type(None))
