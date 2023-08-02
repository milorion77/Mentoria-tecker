##realizar un ejercio basico con el random() float y vamos a cortar el numero 1:3,inicio:6 y del fin:-4
## cadena sacar la longitud, inicio hasta longitud 
'''
import random

# Generar una lista de 10 números aleatorios de punto flotante entre 0 y 1
numeros_aleatorios = [random.random() for _ in range(10)]

print("Lista completa de números aleatorios:")
print(numeros_aleatorios)

# Cortar la lista desde el índice 6 hasta la longitud - 4
sublista = numeros_aleatorios[6:len(numeros_aleatorios)-4]

print("Sublista desde el índice 6 hasta longitud - 4:")
print(sublista)
'''

import random

# Generar un número aleatorio de punto flotante entre 0 y 1
numero_aleatorio = random.random()

print("Número aleatorio completo:")
print(numero_aleatorio)

# Obtener el número cortado entre los índices 1 y 3 y el índice 6 hasta los últimos 4 elementos
numero_cortado = str(numero_aleatorio)[1:3] + str(numero_aleatorio)[6:-4]
numero_cortado2 = str(numero_aleatorio)[6:-4]
numero_medido = len(str(numero_aleatorio)[1:3] + str(numero_aleatorio)[6:-4])
print("Número cortado:")
print(numero_cortado)
print("Número cortado:")
print(numero_cortado2)
print(f'Nummero medido:  {numero_medido}')