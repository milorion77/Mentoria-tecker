# Integrantes: Ana, Sebastian y Camilo

##En Python, una tupla es una colección de elementos ordenados e inmutables. 
# Se representa por utilizar parentesis ()
ej_tupla=('guan', 'tu', 'tri')
print(type(ej_tupla))
#Se utilizan para almacenar múltiples elementos como listas
tupla_con_lista = (1, 2, [3, 4, 5], 6, 7)
#pero a diferencia de las listas las tuplas NO PUEDEN modificarse una vez creadas, Eso da error

#Esto la hace ideal para almacenar datos que no deben cambiar, como valores constantes o datos que no queremos modificar.

#METODOS CON TUPLA:

#Método count():
#Este método se utiliza para contar la cantidad de veces que aparece un elemento específico en la tupla.
#Ejemplo:
nombres = ('jairo', 'jaime', 'jair', 'juan jose persona', 'Maicol')
count_nombre = nombres.count('juan jose persona')
print(count_nombre)  

#Método index():
#Este método se utiliza para obtener el índice de la primera aparición de un elemento en la tupla.
#Ejemplo 1:

animales = ('Perro', 'Chigüiro', 'Gurre', 'Pejelagarto')
index_pejelagarto = animales.index('Pejelagarto')
print(index_pejelagarto) 

#Desempaquetado de tuplas:
#Python permite desempaquetar tuplas, lo que significa asignar sus elementos a variables individuales.
#Ejemplo 1:

coordinates = (10, 20)
x, y = coordinates
print(x)  # imprime: 10
print(y)  # imprime: 20

#Ejemplo 2:

persona = ('Ana', 30, 'Candelaria')
nombre, edad, barrio = persona
print(nombre)  
print(edad)   
print(barrio)  

#PREGUNTAAAAAAAAAA!!!
#si una tupla contiene una lista, puedo editar la lista que esta dentro de esa tupla? 
#Sí, puedes editar una lista que está dentro de una tupla, pero debes recordar que las tuplas 
#son inmutables, lo que significa que no puedes cambiar la tupla en sí, pero sí puedes modificar 
#los elementos mutables que contiene, como una lista. En otras palabras, puedes agregar, eliminar
#o modificar elementos de la lista, pero no puedes cambiar la lista por completo ni agregar
#o eliminar elementos directamente de la tupla.

# Definimos una tupla que contiene una lista
tupla_con_lista = (1, 2, [3, 4, 5], 6, 7)

# Intentamos modificar un elemento de la lista que está dentro de la tupla
tupla_con_lista[2][1] = 10

# Ahora imprimimos la tupla para ver los cambios
print(tupla_con_lista)


#las tuplas pueden contener diccionarios y dentro de los diccionarios pueden haber listas
# y podemos editar los diccionarios y las listas dentro de la tupla?
## SSSSIIIIII jaja
#Ejempo:

# Definimos una tupla que contiene un diccionario que a su vez contiene una lista
tupla_con_diccionario = (
    {'nombre': 'Juan', 'chance': [25, 30, 35]},
    {'nombre': 'María', 'chance': [22, 27, 33]}
)

# Podemos modificar elementos dentro del diccionar io o la lista
tupla_con_diccionario[0]['nombre'] = 'Camilo'
tupla_con_diccionario[1]['chance'][1] = 26

# Ahora imprimimos la tupla para ver los cambios
print(tupla_con_diccionario)
