"""
"count" es un método que se utiliza en LISTA, es un contador que te ayuda a saber 
cuántas veces aparece algo en una lista
Por ejemplo: si tienes una lista de frutas y quieres saber cuántas papayas tienes, "count" ayuda
a contar cuántas papayas hay en esa lista.

Bueno, asi la usamos
hacemos una lista de frutas:
"""
#Ejemplo:
# Primer pasoneitor definimos la lista de juguetes
frutas = ['papaya', 'piedras', 'papaya', 'bofe', 'chunchurria', 'paloma', 'papayó']

# Aqui contamos cuántas veces aparece la palabra papaya en la lista
cantidad_payayas = frutas.count('papaya')

# Mostramos el resultado
print("Cantidad de papayas:", cantidad_payayas )

#Segundo ejempleichon
# Definimos otraaaa lista de personajes de DBZ
personajes_dbz = ['Goku', 'Vegeta', 'Piccolo', 'Goku', 'Gohan', 'Trunks', 'Goku']

# Contamos cuántas veces aparece el nombre "Goku" en la lista
cantidad_gokus = personajes_dbz.count('Goku')

# Mostramos el resultado
print("Cantidad de veces que aparece Goku:", cantidad_gokus)