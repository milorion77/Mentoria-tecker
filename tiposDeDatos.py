# conversion
# en py se puede indentificar el tipo de dato de una variable
# por medio de la ocnversacion
## int
numero=int(3.45)
print(numero)
print(type(numero))
numero=str(3)
print(numero)
print(type(numero))
numero=int(45)
print(numero)
print(type(numero))
#float
decimal=float(12)
print(decimal)
print(type(decimal))
decimal=float("45.3")
print(decimal)
print(type(decimal))
decimal=float(78.2)
print(decimal)
print(type(decimal))
# tipos de datos incorporados
#tipos texto  str
#tipos numericos int, tuplas, range
#tipo de mapeo dict "diccionario"
#boolean bool bytes, bytearray, memoryview
# ningun  tipo Nonetype
#typo de dato complex es un tipo de dato que nos da una parte imaginaria "numeros complejos"
# los numeros complejos se escriben con una "j" como parte imaginaria
<<<<<<< HEAD

z=-5j
print(z)
## numeros aleatorios
## py tiene una funcion ramdom para trabajar con numeros aleatorios
#pero tiene un modulo integrado llamado random que se puede utilizar para los numeros aleatorios
import random
print(random.randrange(1,11)) # 0, 100 omitiendo el 101
# randint()
print(random.randint(1,100))
## getStates()  este metodo usa para capturar el estado del numero generador
print(random.getstate())
# random()
print(random.random())
