##realizar un ejercio basico con el random() float y vamos a cortar el numero 1:3,inicio:6 y del fin:-4
## cadena sacar la longitud, inicio hasta longitud 

import random

# Generar una lista de 10 números aleatorios de punto flotante entre 0 y 1
numeros_aleatorios = [random.random() for _ in range(10)]

print("Lista completa de números aleatorios:")
print(numeros_aleatorios)

# Cortar la lista desde el índice 6 hasta la longitud - 4
sublista = numeros_aleatorios[6:len(numeros_aleatorios)-4]

print("Sublista desde el índice 6 hasta longitud - 4:")
print(sublista)
